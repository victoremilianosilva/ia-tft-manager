# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **5101**
- Achados: **947**
- CRITICAL: 0 | HIGH: 19 | MEDIUM: 44 | LOW: 884

## Metadados da sessão

- Match ID: aa5d7664-2459-43cb-99c6-1174bda7fd36
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 3d63262fb93d7504bfc05b4e6efd43b7d3bf9e722c0407b8e8b1bd7903bc856d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4348**
- Entradas posteriores à eliminação ignoradas: **753**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 41 | 7 | 12 | 12 | 59 | 2 | 4 | não/inconclusivo | 0 |
| Jogador 6 | 55 | 7 | 12 | 4 | 68 | 2 | 2 | não/inconclusivo | 0 |
| Jogador 7 | 90 | 9 | 38 | 4 | 58 | 2 | 1 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 269 | 89 | 52 | 17 | 0 | 23 | 80 | 0.0868 | 8 | 26 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::MOVE_BOARD: 2, ALL_IN::PASS: 1, ALL_IN::SELL: 8, ECON::BUY: 10, ECON::ITEM: 1, ECON::MOVE_BENCH: 2, ECON::MOVE_BOARD: 6, ECON::PASS: 2, ECON::SELL: 4, FAST8::BUY: 30, FAST8::BUY_XP: 4, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 5, FAST8::MOVE_BOARD: 27, FAST8::PASS: 8, FAST8::SELL: 26, STABILIZE::BUY: 42, STABILIZE::BUY_XP: 13, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 16, STABILIZE::MOVE_BOARD: 22, STABILIZE::PASS: 12, STABILIZE::SELL: 14
- Jogador 1 — recompensas por ação: BUY: média 0.2971 (n=89), BUY_XP: média -0.0024 (n=17), ITEM: média 0.1375 (n=8), MOVE_BENCH: média 0.1857 (n=23), MOVE_BOARD: média -0.0005 (n=57), PASS: média -0.0765 (n=23), SELL: média -0.1277 (n=52)
| Jogador 2 | 167 | 74 | 47 | 3 | 1 | 5 | 29 | 0.0642 | 5 | 16 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 4, ALL_IN::REROLL: 1, ALL_IN::SELL: 3, STABILIZE::BUY: 67, STABILIZE::BUY_XP: 3, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 9, STABILIZE::MOVE_BOARD: 16, STABILIZE::PASS: 5, STABILIZE::SELL: 44
- Jogador 2 — recompensas por ação: BUY: média 0.2222 (n=74), BUY_XP: média -0.0400 (n=3), ITEM: média 0.1913 (n=8), MOVE_BENCH: média 0.1992 (n=13), MOVE_BOARD: média -0.0225 (n=16), PASS: média 0.0000 (n=5), REROLL: média -0.0700 (n=1), SELL: média -0.1977 (n=47)
| Jogador 3 | 164 | 63 | 38 | 3 | 2 | 13 | 40 | 0.0669 | 3 | 21 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 12, ALL_IN::REROLL: 2, ALL_IN::SELL: 13, STABILIZE::BUY: 51, STABILIZE::BUY_XP: 3, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 24, STABILIZE::MOVE_BOARD: 16, STABILIZE::PASS: 13, STABILIZE::SELL: 25
- Jogador 3 — recompensas por ação: BUY: média 0.2465 (n=63), BUY_XP: média -0.0467 (n=3), ITEM: média 0.2120 (n=5), MOVE_BENCH: média -0.0088 (n=24), MOVE_BOARD: média -0.0037 (n=16), PASS: média -0.0138 (n=13), REROLL: média -0.0700 (n=2), SELL: média -0.1284 (n=38)
| Jogador 4 | 194 | 59 | 26 | 12 | 7 | 15 | 65 | 0.1017 | 10 | 19 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 11, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 5, ALL_IN::MOVE_BOARD: 10, ALL_IN::PASS: 3, ALL_IN::REROLL: 5, ALL_IN::SELL: 5, STABILIZE::BUY: 48, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 29, STABILIZE::MOVE_BOARD: 21, STABILIZE::PASS: 12, STABILIZE::REROLL: 2, STABILIZE::SELL: 21
- Jogador 4 — recompensas por ação: BUY: média 0.4741 (n=59), BUY_XP: média -0.0125 (n=12), ITEM: média 0.1690 (n=10), MOVE_BENCH: média 0.0176 (n=34), MOVE_BOARD: média -0.0119 (n=31), PASS: média -0.0933 (n=15), REROLL: média -0.1100 (n=7), SELL: média -0.3019 (n=26)
| Jogador 5 | 296 | 110 | 77 | 16 | 0 | 14 | 68 | 0.0764 | 16 | 48 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 32, ALL_IN::ITEM: 1, ALL_IN::MOVE_BENCH: 2, ALL_IN::MOVE_BOARD: 2, ALL_IN::SELL: 25, STABILIZE::BUY: 78, STABILIZE::BUY_XP: 16, STABILIZE::ITEM: 10, STABILIZE::MOVE_BENCH: 23, STABILIZE::MOVE_BOARD: 41, STABILIZE::PASS: 14, STABILIZE::SELL: 52
- Jogador 5 — recompensas por ação: BUY: média 0.3003 (n=110), BUY_XP: média -0.0244 (n=16), ITEM: média 0.1236 (n=11), MOVE_BENCH: média 0.1504 (n=25), MOVE_BOARD: média -0.0044 (n=43), PASS: média -0.0143 (n=14), SELL: média -0.1918 (n=77)
| Jogador 6 | 188 | 68 | 40 | 12 | 2 | 13 | 43 | 0.0831 | 17 | 32 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 23, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 3, ALL_IN::MOVE_BOARD: 3, ALL_IN::PASS: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 18, STABILIZE::BUY: 45, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 9, STABILIZE::MOVE_BOARD: 28, STABILIZE::PASS: 12, STABILIZE::SELL: 22
- Jogador 6 — recompensas por ação: BUY: média 0.2796 (n=68), BUY_XP: média -0.0458 (n=12), ITEM: média 0.1420 (n=10), MOVE_BENCH: média 0.2442 (n=12), MOVE_BOARD: média -0.0023 (n=31), PASS: média -0.0323 (n=13), REROLL: média -0.1100 (n=2), SELL: média -0.1620 (n=40)
| Jogador 7 | 247 | 58 | 23 | 38 | 0 | 23 | 92 | 0.0670 | 6 | 68 |
- Jogador 7 — ações por estratégia: ECON::BUY: 1, ECON::BUY_XP: 1, FAST8::BUY: 6, FAST8::BUY_XP: 7, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 3, FAST8::MOVE_BOARD: 17, FAST8::PASS: 5, FAST8::SELL: 3, STABILIZE::BUY: 40, STABILIZE::BUY_XP: 13, STABILIZE::ITEM: 6, STABILIZE::MOVE_BENCH: 17, STABILIZE::MOVE_BOARD: 23, STABILIZE::PASS: 9, STABILIZE::SELL: 17, WINSTREAK::BUY: 11, WINSTREAK::BUY_XP: 17, WINSTREAK::ITEM: 3, WINSTREAK::MOVE_BENCH: 9, WINSTREAK::MOVE_BOARD: 23, WINSTREAK::PASS: 9, WINSTREAK::SELL: 3
- Jogador 7 — recompensas por ação: BUY: média 0.4107 (n=58), BUY_XP: média -0.0221 (n=38), ITEM: média 0.1323 (n=13), MOVE_BENCH: média 0.0159 (n=29), MOVE_BOARD: média -0.0022 (n=63), PASS: média -0.0343 (n=23), SELL: média -0.3339 (n=23)
| Jogador 8 | 228 | 91 | 53 | 15 | 2 | 10 | 49 | 0.1143 | 9 | 33 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 15, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 6, ALL_IN::PASS: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 9, FAST8::BUY: 3, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 4, FAST8::PASS: 1, STABILIZE::BUY: 73, STABILIZE::BUY_XP: 15, STABILIZE::ITEM: 6, STABILIZE::MOVE_BENCH: 16, STABILIZE::MOVE_BOARD: 21, STABILIZE::PASS: 8, STABILIZE::SELL: 44
- Jogador 8 — recompensas por ação: BUY: média 0.3702 (n=91), BUY_XP: média -0.0233 (n=15), ITEM: média 0.1650 (n=8), MOVE_BENCH: média 0.2300 (n=18), MOVE_BOARD: média -0.0081 (n=31), PASS: média -0.0620 (n=10), REROLL: média -0.1100 (n=2), SELL: média -0.2200 (n=53)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 07:40:03 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | ? | 07:40:05 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | ? | 07:40:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 07:40:10 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 07:40:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 07:40:11 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-1 | 07:40:12 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 07:40:12 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 07:40:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 07:40:15 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 1-2 | 07:40:18 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-2 | 07:40:18 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 07:40:18 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 07:40:19 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-2 | 07:40:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 07:40:27 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 07:40:27 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 07:40:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 07:40:35 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 07:40:35 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 1-4 | 07:40:36 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 07:40:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-4 | 07:40:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-1 | 07:40:44 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 07:40:45 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.1300 |  |
| Jogador 1 | 2-1 | 07:40:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 07:40:45 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-1 | 07:40:46 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.2800 |  |
| Jogador 1 | 2-1 | 07:40:46 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 07:40:47 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1700 |  |
| Jogador 1 | 2-1 | 07:40:49 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-1 | 07:40:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-2 | 07:40:57 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 1 | 2-2 | 07:40:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 07:40:58 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-2 | 07:40:59 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1800 |  |
| Jogador 1 | 2-2 | 07:40:59 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 1 | 2-2 | 07:41:00 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 07:41:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 07:41:12 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 2-3 | 07:41:13 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.3600 |  |
| Jogador 1 | 2-3 | 07:41:13 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 2-3 | 07:41:14 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.1900 |  |
| Jogador 1 | 2-3 | 07:41:15 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-3 | 07:41:15 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0900 |  |
| Jogador 1 | 2-3 | 07:41:16 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0100 |  |
| Jogador 1 | 2-3 | 07:41:16 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 07:41:17 | MOVE Board -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0200 |  |
| Jogador 1 | 2-4 | 07:41:27 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Ornn | 0.9700 |  |
| Jogador 1 | 2-4 | 07:41:28 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Ornn | 0.0500 |  |
| Jogador 1 | 2-4 | 07:41:28 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 1 | 2-4 | 07:41:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 2-4 | 07:41:29 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 07:41:30 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 2-4 | 07:41:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 2-4 | 07:41:31 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.5000 |  |
| Jogador 1 | 2-4 | 07:41:31 | MOVE Board -> Board: Shen (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 07:41:44 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 1.1200 |  |
| Jogador 1 | 2-5 | 07:41:45 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 1 | 2-5 | 07:41:45 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 1 | 2-5 | 07:41:45 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 2-5 | 07:41:46 | MOVE Board -> Board: Krugue (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 07:41:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 07:41:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 07:42:03 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 2-6 | 07:42:04 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 1 | 2-6 | 07:42:04 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 1 | 2-6 | 07:42:05 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 2-6 | 07:42:05 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 2-6 | 07:42:06 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 1 | 2-6 | 07:42:06 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 1 | 2-6 | 07:42:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 07:42:24 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 1 | 2-7 | 07:42:24 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 2-7 | 07:42:25 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 2-7 | 07:42:25 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 2-7 | 07:42:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 07:42:46 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-1 | 07:42:47 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 1 | 3-1 | 07:42:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 3-1 | 07:42:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 07:42:48 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 3-1 | 07:42:49 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 3-1 | 07:42:49 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-1 | 07:42:50 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-1 | 07:42:50 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-2 | 07:43:10 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 3-2 | 07:43:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 07:43:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 07:43:11 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 3-2 | 07:43:12 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-2 | 07:43:13 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.7100 |  |
| Jogador 1 | 3-2 | 07:43:14 | MOVE Bench -> Board: Rakan (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 3-2 | 07:43:14 | MOVE Bench -> Board: Shen (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 1 | 3-2 | 07:43:15 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.7300 |  |
| Jogador 1 | 3-3 | 07:43:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 3-3 | 07:43:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 3-3 | 07:43:36 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.6000 |  |
| Jogador 1 | 3-3 | 07:43:36 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 1 | 3-3 | 07:43:37 | MOVE Board -> Board: Rakan (i:4.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-3 | 07:43:37 | MOVE Board -> Board: Krugue (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 07:43:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-4 | 07:44:02 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 3-4 | 07:44:03 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 1 | 3-4 | 07:44:03 | MOVE Bench -> Board: Shen (i:8.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-4 | 07:44:04 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 1 | 3-4 | 07:44:05 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 3-4 | 07:44:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 3-4 | 07:44:06 | MOVE Board -> Board: Shen (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-4 | 07:44:06 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 1 | 3-4 | 07:44:07 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 3-5 | 07:44:31 | VENDEU: Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Inferno | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 1 | 3-5 | 07:44:32 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Inferno | DA_KogMaw18_AD | 0.6600 |  |
| Jogador 1 | 3-5 | 07:44:32 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-5 | 07:44:33 | MOVE Board -> Board: Shen (i:8.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-5 | 07:44:33 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 07:45:01 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Inferno | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 3-6 | 07:45:02 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Inferno | DA_KogMaw18_AD | 0.6600 |  |
| Jogador 1 | 3-6 | 07:45:02 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Inferno | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 1 | 3-6 | 07:45:02 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Inferno | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 1 | 3-6 | 07:45:03 | MOVE Board -> Board: Krugue (i:6.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 07:45:03 | MOVE Board -> Board: Rakan (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-6 | 07:45:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-7 | 07:45:33 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Inferno | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 1 | 3-7 | 07:45:34 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_BFSword -> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Inferno | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 3-7 | 07:45:34 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 1 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 3-7 | 07:45:35 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Inferno | DA_KogMaw18_AD | 0.4600 |  |
| Jogador 1 | 3-7 | 07:45:35 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 1 | Inferno | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 3-7 | 07:45:36 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-7 | 07:45:37 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-7 | 07:45:37 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-7 | 07:45:38 | MOVE Board -> Board: Krugue (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-1 | 07:46:07 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 2 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 4-1 | 07:46:08 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 2 | Inferno | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 1 | 4-1 | 07:46:08 | MOVE Board -> Board: Xayah (i:2.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 2 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 07:46:09 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 2 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-1 | 07:46:09 | MOVE Board -> Board: Vi (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 2 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-1 | 07:46:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 2 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 4-2 | 07:46:43 | MOVE Board -> Board: Krugue (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-2 | 07:46:43 | MOVE Board -> Board: Xayah (i:2.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-2 | 07:46:44 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 4-3 | 07:47:20 | VENDEU: Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 4-3 | 07:47:20 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Inferno | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 1 | 4-3 | 07:47:21 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-3 | 07:47:21 | MOVE Board -> Board: Rakan (i:4.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-3 | 07:47:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-4 | 07:47:58 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Inferno | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 1 | 4-4 | 07:47:59 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Inferno | DA_KogMaw18_AD | 0.2600 |  |
| Jogador 1 | 4-4 | 07:47:59 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 4-4 | 07:48:00 | COMPROU: Malphite (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-4 | 07:48:00 | MOVE Board -> Board: Krugue (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-4 | 07:48:00 | MOVE Board -> Board: Vi (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-4 | 07:48:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Inferno | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 1 | 4-5 | 07:48:38 | VENDEU: Malphite (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-5 | 07:48:39 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Inferno | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 1 | 4-5 | 07:48:40 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-5 | 07:48:40 | MOVE Board -> Board: Shen (i:8.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-5 | 07:48:41 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-5 | 07:48:41 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Inferno | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 1 | 4-6 | 07:49:22 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 105 | 5 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 4-6 | 07:49:22 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Inferno | DA_KogMaw18_AD | 0.7200 |  |
| Jogador 1 | 4-6 | 07:49:22 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-6 | 07:49:23 | MOVE Board -> Board: Rakan (i:4.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-6 | 07:49:23 | MOVE Board -> Board: Xayah (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-6 | 07:49:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Inferno | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 1 | 4-7 | 07:50:05 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Inferno | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 4-7 | 07:50:06 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 4-7 | 07:50:06 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Inferno | DA_KogMaw18_AD | -0.4900 |  |
| Jogador 1 | 4-7 | 07:50:07 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Inferno | DA_KogMaw18_AD | 0.9500 |  |
| Jogador 1 | 4-7 | 07:50:07 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 109 | 5 | Inferno | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 1 | 4-7 | 07:50:07 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 106 | 5 | Inferno | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 1 | 4-7 | 07:50:08 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 106 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-7 | 07:50:09 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 106 | 5 | Inferno | DA_KogMaw18_AD | 0.4900 |  |
| Jogador 1 | 4-7 | 07:50:09 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Inferno | DA_KogMaw18_AD | -0.1800 |  |
| Jogador 1 | 5-1 | 07:50:52 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Inferno | DA_KogMaw18_AD | 0.8500 |  |
| Jogador 1 | 5-1 | 07:50:52 | VENDEU: Krugue (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 119 | 5 | Inferno | DA_KogMaw18_AD | -0.4500 |  |
| Jogador 1 | 5-1 | 07:50:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 118 | 5 | Inferno | DA_KogMaw18_AD | 0.9500 |  |
| Jogador 1 | 5-1 | 07:50:53 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 115 | 5 | Inferno | DA_KogMaw18_AD | 1.0200 |  |
| Jogador 1 | 5-1 | 07:50:54 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Inferno | DA_KogMaw18_AD | -0.2400 |  |
| Jogador 1 | 5-1 | 07:50:55 | MOVE Bench -> Board: Fiddlesticks (i:12.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Inferno | DA_KogMaw18_AD | -0.3100 |  |
| Jogador 1 | 5-1 | 07:50:55 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Inferno | DA_KogMaw18_AD | -0.2500 |  |
| Jogador 1 | 5-1 | 07:50:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 105 | 5 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 5-1 | 07:50:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 5-2 | 07:51:42 | VENDEU: Xayah (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 114 | 5 | Inferno | DA_KogMaw18_AD | -0.5900 |  |
| Jogador 1 | 5-2 | 07:51:42 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 113 | 5 | Inferno | DA_KogMaw18_AD | 0.8800 |  |
| Jogador 1 | 5-2 | 07:51:43 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Inferno | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 1 | 5-2 | 07:51:43 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 119 | 5 | Inferno | DA_Fiddlesticks18 | 0.3800 |  |
| Jogador 1 | 5-2 | 07:51:44 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Inferno | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 1 | 5-2 | 07:51:44 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 117 | 5 | Inferno | DA_Fiddlesticks18 | 0.3500 |  |
| Jogador 1 | 5-2 | 07:51:44 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 117 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 5-2 | 07:51:45 | MOVE Bench -> Board: Diana (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 117 | 5 | Inferno | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 1 | 5-2 | 07:51:45 | MOVE Board -> Board: Diana (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 117 | 5 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 1 | 5-3 | 07:52:33 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 130 | 5 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 5-3 | 07:52:34 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 128 | 5 | Inferno | DA_Fiddlesticks18 | 0.9100 |  |
| Jogador 1 | 5-3 | 07:52:34 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 131 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 5-3 | 07:52:35 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 130 | 5 | Inferno | DA_Fiddlesticks18 | 0.2700 |  |
| Jogador 1 | 5-3 | 07:52:35 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 133 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 5-3 | 07:52:35 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 131 | 5 | Inferno | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 1 | 5-3 | 07:52:36 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 131 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 5-3 | 07:52:36 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 127 | 5 | Inferno | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 1 | 5-3 | 07:52:37 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 123 | 5 | Inferno | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 1 | 5-4 | 07:53:22 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 5-4 | 07:53:22 | COMPROU: Lux (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 131 | 5 | Inferno | DA_Fiddlesticks18 | -0.2100 |  |
| Jogador 1 | 5-4 | 07:53:23 | VENDEU: Ahri (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 135 | 5 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 1 | 5-4 | 07:53:23 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 133 | 5 | Inferno | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 1 | 5-4 | 07:53:24 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 135 | 5 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 1 | 5-4 | 07:53:24 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 133 | 5 | Inferno | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 1 | 5-4 | 07:53:25 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 133 | 5 | Inferno | DA_Fiddlesticks18 | 0.5900 |  |
| Jogador 1 | 5-4 | 07:53:25 | COMPROU: Leona (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Inferno | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 1 | 5-4 | 07:53:25 | MOVE Board -> Board: Shen (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 5-5 | 07:54:12 | VENDEU: Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 5-5 | 07:54:13 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 141 | 5 | Inferno | DA_Fiddlesticks18 | 0.9500 |  |
| Jogador 1 | 5-5 | 07:54:13 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 138 | 5 | Inferno | DA_Fiddlesticks18 | 0.4000 |  |
| Jogador 1 | 5-5 | 07:54:14 | VENDEU: Diana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 146 | 5 | Inferno | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 1 | 5-5 | 07:54:14 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Inferno | DA_Fiddlesticks18 | -0.2800 |  |
| Jogador 1 | 5-5 | 07:54:15 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 5-5 | 07:54:15 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 146 | 5 | Inferno | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 1 | 5-5 | 07:54:16 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Inferno | DA_Fiddlesticks18 | -0.2800 |  |
| Jogador 1 | 5-5 | 07:54:16 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 146 | 5 | Inferno | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 1 | 5-6 | 07:55:05 | COMPROU: Lillia (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 153 | 5 | Inferno | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 1 | 5-6 | 07:55:05 | VENDEU: Warwick (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 155 | 5 | Inferno | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 1 | 5-6 | 07:55:06 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 152 | 5 | Inferno | DA_Fiddlesticks18 | 0.2300 |  |
| Jogador 1 | 5-6 | 07:55:06 | MOVE Bench -> Board: Lillia (i:8.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 152 | 5 | Inferno | DA_Fiddlesticks18 | 0.1500 |  |
| Jogador 1 | 5-6 | 07:55:06 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 149 | 5 | Inferno | DA_Fiddlesticks18 | 0.7600 |  |
| Jogador 1 | 5-6 | 07:55:07 | MOVE Board -> Board: Lillia (i:8.0) <-> Fiddlesticks (i:12.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 149 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 5-6 | 07:55:07 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 149 | 5 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 1 | 5-6 | 07:55:08 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 149 | 5 | Inferno | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 1 | 5-7 | 07:55:54 | COMPROU: Shen (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 157 | 5 | Inferno | DA_Fiddlesticks18 | 1.0600 |  |
| Jogador 1 | 5-7 | 07:55:54 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 153 | 5 | Inferno | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 1 | 5-7 | 07:55:54 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Fiddlesticks (i:12.0) (tabuleiro slot 9) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 153 | 5 | Inferno | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 1 | 5-7 | 07:55:55 | VENDEU: Shen (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 158 | 5 | Inferno | DA_Fiddlesticks18 | -0.8500 |  |
| Jogador 1 | 5-7 | 07:55:55 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 155 | 5 | Inferno | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 1 | 5-7 | 07:55:55 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 155 | 5 | Inferno | DA_Fiddlesticks18 | 0.4700 |  |
| Jogador 1 | 5-7 | 07:55:56 | COMPROU: Morgana (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 151 | 5 | Inferno | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 1 | 5-7 | 07:55:57 | MOVE Board -> Board: Diana (i:6.0) <-> Vi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 151 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 5-7 | 07:55:57 | MOVE Board -> Board: Vi (i:6.0) <-> Shen (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 151 | 5 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 1 | 6-1 | 07:56:48 | VENDEU: Master Yi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 164 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 6-1 | 07:56:48 | COMPROU: Akali (Custo 1 \| i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 163 | 5 | Inferno | DA_Fiddlesticks18 | 1.0600 |  |
| Jogador 1 | 6-1 | 07:56:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 162 | 5 | Inferno | DA_Fiddlesticks18 | 0.4700 |  |
| Jogador 1 | 6-1 | 07:56:49 | VENDEU: Akali (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 165 | 5 | Inferno | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 1 | 6-1 | 07:56:49 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 161 | 5 | Inferno | DA_Fiddlesticks18 | 0.4800 |  |
| Jogador 1 | 6-1 | 07:56:50 | MOVE Board -> Board: Shen (i:8.0) <-> Fiddlesticks (i:12.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 161 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 6-1 | 07:56:50 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Lillia (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 161 | 5 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 1 | 6-1 | 07:56:51 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 161 | 5 | Inferno | DA_Fiddlesticks18 | -0.2000 |  |
| Jogador 1 | 6-2 | 07:57:42 | COMPROU: Lux (Florescer) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 166 | 5 | Inferno | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 1 | 6-2 | 07:57:43 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 167 | 5 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 6-2 | 07:57:43 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 165 | 5 | Inferno | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 1 | 6-2 | 07:57:44 | MOVE Board -> Board: Lillia (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 165 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 6-2 | 07:57:44 | MOVE Board -> Board: Nidalee (i:8.0) <-> Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 165 | 5 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 6-2 | 07:57:44 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 165 | 5 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 1 | 6-2 | 07:57:45 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 165 | 5 | Inferno | DA_Fiddlesticks18 | -0.2300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 6-3 | 07:58:42 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 1 | 6-3 | 07:58:42 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 174 | 5 | Inferno | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 1 | 6-3 | 07:58:42 | VENDEU: Morgana (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Inferno | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 1 | 6-3 | 07:58:43 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 174 | 5 | Inferno | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 1 | 6-3 | 07:58:43 | VENDEU: Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 6-3 | 07:58:44 | COMPROU: Ezreal (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 174 | 5 | Inferno | DA_Fiddlesticks18 | -0.2200 |  |
| Jogador 1 | 6-3 | 07:58:44 | MOVE Board -> Board: Diana (i:6.0) <-> Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 174 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 6-3 | 07:58:45 | MOVE Board -> Board: Shen (i:8.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 174 | 5 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 1 | 6-3 | 07:58:45 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 174 | 5 | Inferno | DA_Fiddlesticks18 | -0.6200 |  |
| Jogador 1 | 6-4 | 07:59:43 | VENDEU: Ezreal (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 189 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 6-4 | 07:59:44 | COMPROU: Maokai (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 184 | 5 | Inferno | DA_Fiddlesticks18 | 0.1900 |  |
| Jogador 1 | 6-4 | 07:59:44 | VENDEU: Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 6-4 | 07:59:45 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 184 | 5 | Inferno | DA_Fiddlesticks18 | -0.1300 |  |
| Jogador 1 | 6-4 | 07:59:45 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 6-4 | 07:59:46 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 185 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 6-4 | 07:59:46 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 6-4 | 07:59:46 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 184 | 5 | Inferno | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 1 | 6-4 | 07:59:47 | VENDEU: Sett (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Inferno | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 2 | ? | 07:40:03 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | ? | 07:40:05 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | ? | 07:40:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 07:40:10 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 07:40:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 07:40:11 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 1-1 | 07:40:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 07:40:15 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 1-2 | 07:40:18 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 07:40:18 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 07:40:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 07:40:23 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 07:40:27 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 07:40:27 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 07:40:28 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-3 | 07:40:28 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-3 | 07:40:29 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 07:40:29 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 07:40:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 07:40:35 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 07:40:35 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 07:40:36 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 07:40:36 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 07:40:37 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 1-4 | 07:40:37 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 1-4 | 07:40:38 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-4 | 07:40:38 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-1 | 07:40:44 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 2-1 | 07:40:45 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 2-1 | 07:40:45 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-1 | 07:40:45 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 2-1 | 07:40:46 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-1 | 07:40:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 07:40:47 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-1 | 07:40:49 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-1 | 07:40:49 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-2 | 07:40:57 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-2 | 07:40:58 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 2-2 | 07:40:58 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 07:40:59 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-2 | 07:40:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 07:41:12 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.7700 |  |
| Jogador 2 | 2-3 | 07:41:13 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 2-3 | 07:41:13 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-3 | 07:41:14 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 07:41:15 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 2-3 | 07:41:15 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 2-3 | 07:41:16 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 2-3 | 07:41:16 | MOVE Board -> Board: Xayah (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 07:41:17 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-4 | 07:41:27 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.3200 |  |
| Jogador 2 | 2-4 | 07:41:28 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-4 | 07:41:28 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 07:41:29 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.1900 |  |
| Jogador 2 | 2-4 | 07:41:29 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-4 | 07:41:30 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 2-4 | 07:41:30 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-4 | 07:41:31 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 07:41:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 07:41:44 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 2-5 | 07:41:45 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.2000 |  |
| Jogador 2 | 2-5 | 07:41:45 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-5 | 07:41:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 07:41:46 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-5 | 07:41:47 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-5 | 07:41:48 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Veigar | -0.4200 |  |
| Jogador 2 | 2-5 | 07:41:48 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-5 | 07:41:49 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | 0.3900 |  |
| Jogador 2 | 2-6 | 07:42:03 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 2-6 | 07:42:04 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 2-6 | 07:42:04 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-6 | 07:42:05 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 2-6 | 07:42:05 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-6 | 07:42:06 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Feérico | DA_18_Veigar | -0.3700 |  |
| Jogador 2 | 2-6 | 07:42:06 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 2-6 | 07:42:07 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-6 | 07:42:08 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Feérico | DA_18_Veigar | -0.4600 |  |
| Jogador 2 | 2-7 | 07:42:24 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Feérico | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 2-7 | 07:42:24 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Feérico | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 2-7 | 07:42:25 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-7 | 07:42:25 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 2-7 | 07:42:26 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 2-7 | 07:42:27 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-7 | 07:42:27 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Feérico | DA_18_Veigar | -0.3900 |  |
| Jogador 2 | 2-7 | 07:42:28 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Feérico | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 2-7 | 07:42:28 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Feérico | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 3-1 | 07:42:46 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Feérico | DA_18_Veigar | 0.8900 |  |
| Jogador 2 | 3-1 | 07:42:47 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Feérico | DA_18_Veigar | 0.7500 |  |
| Jogador 2 | 3-1 | 07:42:47 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Veigar | 0.4600 |  |
| Jogador 2 | 3-1 | 07:42:48 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Feérico | DA_18_Veigar | -0.5500 |  |
| Jogador 2 | 3-1 | 07:42:48 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Feérico | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 3-1 | 07:42:49 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Feérico | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 3-1 | 07:42:49 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Feérico | DA_18_Veigar | -0.5700 |  |
| Jogador 2 | 3-1 | 07:42:50 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Feérico | DA_18_Veigar | -0.3000 |  |
| Jogador 2 | 3-1 | 07:42:50 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Feérico | DA_18_Veigar | -0.3200 |  |
| Jogador 2 | 3-2 | 07:43:10 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Feérico | DA_18_Veigar | 0.8600 |  |
| Jogador 2 | 3-2 | 07:43:10 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Feérico | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 3-2 | 07:43:11 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Feérico | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 3-2 | 07:43:11 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 3-2 | 07:43:12 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 3 | Feérico | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 3-2 | 07:43:13 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Feérico | DA_18_Veigar | -0.3400 |  |
| Jogador 2 | 3-2 | 07:43:14 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Feérico | DA_18_Veigar | -0.3500 |  |
| Jogador 2 | 3-2 | 07:43:14 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Feérico | DA_18_Veigar | -0.2600 |  |
| Jogador 2 | 3-2 | 07:43:15 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 3-3 | 07:43:35 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Feérico | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 3-3 | 07:43:35 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 4 | Feérico | DA_18_Veigar | 0.6400 |  |
| Jogador 2 | 3-3 | 07:43:36 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-3 | 07:43:36 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 4 | Feérico | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 3-3 | 07:43:37 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 4 | Feérico | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 3-3 | 07:43:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 4 | Feérico | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | 3-3 | 07:43:38 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 4 | Feérico | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 3-3 | 07:43:39 | MOVE Board -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 4 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 07:43:39 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 4 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-4 | 07:44:02 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-4 | 07:44:03 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Feérico | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 3-4 | 07:44:03 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Feérico | DA_18_Veigar | -0.4700 |  |
| Jogador 2 | 3-4 | 07:44:04 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Feérico | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 3-4 | 07:44:05 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-4 | 07:44:05 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Feérico | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 3-4 | 07:44:06 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-4 | 07:44:06 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-4 | 07:44:07 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Feérico | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 3-5 | 07:44:31 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 3-5 | 07:44:32 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Feérico | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 3-5 | 07:44:32 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-5 | 07:44:33 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-5 | 07:44:33 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-5 | 07:44:34 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-5 | 07:44:34 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-5 | 07:44:35 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 3-5 | 07:44:35 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-6 | 07:45:01 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Feérico | DA_18_Tristana | 0.9700 |  |
| Jogador 2 | 3-6 | 07:45:02 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Feérico | DA_18_Tristana | 0.0100 |  |
| Jogador 2 | 3-6 | 07:45:02 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Tristana | -0.2400 |  |
| Jogador 2 | 3-6 | 07:45:02 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Feérico | DA_18_Veigar | -0.6000 |  |
| Jogador 2 | 3-6 | 07:45:03 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-6 | 07:45:03 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-6 | 07:45:04 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Feérico | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 3-6 | 07:45:05 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-6 | 07:45:05 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-7 | 07:45:33 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Feérico | DA_18_Veigar | 0.8300 |  |
| Jogador 2 | 3-7 | 07:45:34 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Feérico | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 3-7 | 07:45:34 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Feérico | DA_18_Veigar | 0.1700 |  |
| Jogador 2 | 3-7 | 07:45:35 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Feérico | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 3-7 | 07:45:35 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-7 | 07:45:36 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Feérico | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 3-7 | 07:45:37 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-7 | 07:45:37 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Feérico | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 3-7 | 07:45:38 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-1 | 07:46:07 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Feérico | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 4-1 | 07:46:08 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Feérico | DA_18_Veigar | 0.3500 |  |
| Jogador 2 | 4-1 | 07:46:08 | COMPROU: Kobuko (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 99 | 5 | Feérico | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 4-1 | 07:46:09 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Feérico | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 4-1 | 07:46:09 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Feérico | DA_18_Veigar | -0.5700 |  |
| Jogador 2 | 4-1 | 07:46:10 | MOVE Bench -> Board: Kobuko (i:4.0) <-> Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Feérico | DA_18_Veigar | 0.3300 |  |
| Jogador 2 | 4-1 | 07:46:10 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Feérico | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 4-1 | 07:46:11 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Feérico | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 4-1 | 07:46:11 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 4-2 | 07:46:43 | VENDEU: Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Vivaz | DA_18_Veigar | -0.7400 |  |
| Jogador 2 | 4-2 | 07:46:43 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Vivaz | DA_18_Veigar | 0.7400 |  |
| Jogador 2 | 4-2 | 07:46:44 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Kobuko (i:4.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Vivaz | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 4-2 | 07:46:44 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Kobuko (i:4.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Vivaz | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 4-2 | 07:46:45 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Yorick (i:2.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Vivaz | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 4-2 | 07:46:45 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Vivaz | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-2 | 07:46:46 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Vivaz | DA_18_Veigar | 0.4600 |  |
| Jogador 2 | 4-2 | 07:46:46 | VENDEU: Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Vivaz | DA_18_Veigar | -0.7400 |  |
| Jogador 2 | 4-2 | 07:46:47 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Vivaz | DA_18_Veigar | -0.2300 |  |
| Jogador 3 | ? | 07:40:03 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | ? | 07:40:05 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | ? | 07:40:05 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | ? | 07:40:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 07:40:10 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 07:40:11 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 07:40:11 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-1 | 07:40:12 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 1-1 | 07:40:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 07:40:15 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-2 | 07:40:18 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 07:40:18 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 07:40:18 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 07:40:19 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-2 | 07:40:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 07:40:23 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 1-3 | 07:40:27 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 07:40:27 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 07:40:28 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 07:40:28 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 07:40:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 07:40:35 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 1-4 | 07:40:35 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 1-4 | 07:40:36 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 07:40:36 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 07:40:37 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 07:40:37 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 1-4 | 07:40:38 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-4 | 07:40:38 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-1 | 07:40:44 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-1 | 07:40:45 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 07:40:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 07:40:57 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-2 | 07:40:58 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 2-2 | 07:40:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-2 | 07:40:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 07:41:12 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-3 | 07:41:13 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 2-3 | 07:41:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 07:41:27 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 2-4 | 07:41:28 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-4 | 07:41:28 | MOVE Bench -> Board: Diana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.7100 |  |
| Jogador 3 | 2-4 | 07:41:29 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.4700 |  |
| Jogador 3 | 2-4 | 07:41:29 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-4 | 07:41:30 | MOVE Bench -> Board: Akali (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 2-4 | 07:41:30 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 2-4 | 07:41:31 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | -0.6200 |  |
| Jogador 3 | 2-4 | 07:41:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-5 | 07:41:44 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.8700 |  |
| Jogador 3 | 2-5 | 07:41:45 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.4400 |  |
| Jogador 3 | 2-5 | 07:41:45 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.3600 |  |
| Jogador 3 | 2-5 | 07:41:45 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 07:41:46 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 07:41:47 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-5 | 07:41:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 07:42:03 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | 0.8200 |  |
| Jogador 3 | 2-6 | 07:42:04 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-6 | 07:42:04 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 07:42:05 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 2-6 | 07:42:05 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 07:42:06 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 07:42:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 07:42:24 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | 2-7 | 07:42:24 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | -0.5900 |  |
| Jogador 3 | 2-7 | 07:42:25 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.8100 |  |
| Jogador 3 | 2-7 | 07:42:25 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.4200 |  |
| Jogador 3 | 2-7 | 07:42:26 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 2-7 | 07:42:27 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Devastador | DA_18_Akali_AD | -0.4600 |  |
| Jogador 3 | 2-7 | 07:42:27 | MOVE Bench -> Board: Shen (i:4.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Devastador | DA_18_Akali_AD | -0.6400 |  |
| Jogador 3 | 2-7 | 07:42:28 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Devastador | DA_18_Akali_AD | -0.5300 |  |
| Jogador 3 | 2-7 | 07:42:28 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Devastador | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 3-1 | 07:42:46 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | -0.2600 |  |
| Jogador 3 | 3-1 | 07:42:47 | MOVE Bench -> Board: Vi (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | -0.6400 |  |
| Jogador 3 | 3-1 | 07:42:47 | MOVE Bench -> Board: Shen (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | -0.4000 |  |
| Jogador 3 | 3-1 | 07:42:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-2 | 07:43:10 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Devastador | DA_18_Akali_AD | 0.4200 |  |
| Jogador 3 | 3-2 | 07:43:10 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-2 | 07:43:11 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 07:43:11 | MOVE Bench -> Board: Sivir (i:8.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Devastador | DA_18_Akali_AD | -0.4000 |  |
| Jogador 3 | 3-2 | 07:43:12 | MOVE Bench -> Board: Camille (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Devastador | DA_18_Akali_AD | -0.3000 |  |
| Jogador 3 | 3-2 | 07:43:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Devastador | DA_18_Akali_AD | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-3 | 07:43:35 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Devastador | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 3-3 | 07:43:35 | MOVE Bench -> Board: Grompe (i:4.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 07:43:36 | MOVE Bench -> Board: Sivir (i:8.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Devastador | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-3 | 07:43:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Devastador | DA_18_Akali_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-4 | 07:44:02 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 07:44:03 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Devastador | DA_18_Akali_AD | 0.7500 |  |
| Jogador 3 | 3-4 | 07:44:03 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 3-4 | 07:44:04 | COMPROU: Morgana (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Devastador | DA_18_Akali_AD | -0.0800 |  |
| Jogador 3 | 3-4 | 07:44:05 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Devastador | DA_18_Akali_AD | -0.3700 |  |
| Jogador 3 | 3-4 | 07:44:05 | MOVE Bench -> Board: Grompe (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Devastador | DA_18_Akali_AD | -0.3000 |  |
| Jogador 3 | 3-4 | 07:44:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Devastador | DA_18_Akali_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-5 | 07:44:31 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 07:44:32 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 3 | Devastador | DA_18_Akali_AD | 0.8500 |  |
| Jogador 3 | 3-5 | 07:44:32 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 3 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 07:44:33 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Devastador | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 3-5 | 07:44:33 | MOVE Bench -> Board: Shen (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Devastador | DA_18_Akali_AD | 0.1200 |  |
| Jogador 3 | 3-5 | 07:44:34 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-5 | 07:44:34 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 3 | Devastador | DA_18_Akali_AD | -0.6400 |  |
| Jogador 3 | 3-5 | 07:44:35 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 3-5 | 07:44:35 | MOVE Bench -> Board: Camille (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Devastador | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 3-6 | 07:45:01 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Devastador | DA_18_Akali_AD | 0.3500 |  |
| Jogador 3 | 3-6 | 07:45:02 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Devastador | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 3-6 | 07:45:02 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-6 | 07:45:02 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-6 | 07:45:03 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Devastador | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 3-6 | 07:45:03 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 07:45:04 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Devastador | DA_18_Akali_AD | -0.2600 |  |
| Jogador 3 | 3-6 | 07:45:05 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-6 | 07:45:05 | MOVE Bench -> Board: Shen (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Devastador | DA_18_Akali_AD | -0.3400 |  |
| Jogador 3 | 3-7 | 07:45:33 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Devastador | DA_18_Akali_AD | 0.6800 |  |
| Jogador 3 | 3-7 | 07:45:34 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Devastador | DA_18_Akali_AD | 0.1800 |  |
| Jogador 3 | 3-7 | 07:45:34 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Devastador | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 3-7 | 07:45:35 | VENDEU: Morgana (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Devastador | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 3-7 | 07:45:35 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Devastador | DA_18_Akali_AD | -0.1700 |  |
| Jogador 3 | 3-7 | 07:45:36 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-7 | 07:45:37 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-7 | 07:45:37 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-7 | 07:45:38 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Devastador | DA_18_Akali_AD | -0.2900 |  |
| Jogador 3 | 4-1 | 07:46:07 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Devastador | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-1 | 07:46:08 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Devastador | DA_18_Akali_AD | 0.8400 |  |
| Jogador 3 | 4-1 | 07:46:08 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Devastador | DA_18_Akali_AD | -0.4300 |  |
| Jogador 3 | 4-1 | 07:46:09 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Devastador | DA_18_Akali_AD | 0.3200 |  |
| Jogador 3 | 4-1 | 07:46:09 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 07:46:10 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Devastador | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 4-1 | 07:46:10 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Devastador | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-1 | 07:46:11 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 07:46:11 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-2 | 07:46:43 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 07:46:43 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-2 | 07:46:44 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 07:46:44 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-2 | 07:46:45 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-2 | 07:46:45 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-2 | 07:46:46 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Devastador | DA_18_Akali_AD | -0.2800 |  |
| Jogador 3 | 4-2 | 07:46:46 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 4-2 | 07:46:47 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Devastador | DA_18_Akali_AD | -0.2700 |  |
| Jogador 3 | 4-3 | 07:47:20 | VENDEU: Cascalho (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 4-3 | 07:47:20 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Devastador | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-3 | 07:47:21 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-3 | 07:47:21 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Devastador | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-3 | 07:47:22 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 07:47:22 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Devastador | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-3 | 07:47:22 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 07:47:23 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Devastador | DA_18_Akali_AD | -0.2900 |  |
| Jogador 3 | 4-3 | 07:47:23 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Devastador | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 4-4 | 07:47:58 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Devastador | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-4 | 07:47:59 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Devastador | DA_18_Akali_AD | 0.4600 |  |
| Jogador 3 | 4-4 | 07:47:59 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Devastador | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 4-4 | 07:48:00 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 4-4 | 07:48:00 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Devastador | DA_18_Akali_AD | -0.6700 |  |
| Jogador 3 | 4-4 | 07:48:00 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 4-4 | 07:48:01 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-4 | 07:48:01 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 4-4 | 07:48:02 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Devastador | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 4-5 | 07:48:38 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-5 | 07:48:39 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Devastador | DA_18_Akali_AD | 0.9400 |  |
| Jogador 3 | 4-5 | 07:48:40 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Devastador | DA_18_Akali_AD | -0.5600 |  |
| Jogador 3 | 4-5 | 07:48:40 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-5 | 07:48:41 | VENDEU: Rubrivirim (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-5 | 07:48:41 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Devastador | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-5 | 07:48:42 | VENDEU: Ornn (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-5 | 07:48:42 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Devastador | DA_18_Akali_AD | -0.2600 |  |
| Jogador 3 | 4-5 | 07:48:43 | VENDEU: Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 4 | ? | 07:40:03 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | ? | 07:40:05 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | ? | 07:40:05 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | ? | 07:40:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 07:40:10 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 07:40:11 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 07:40:11 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-1 | 07:40:12 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 1-1 | 07:40:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 07:40:15 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4600 |  |
| Jogador 4 | 1-2 | 07:40:18 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 07:40:18 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 07:40:18 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 07:40:19 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-2 | 07:40:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 07:40:27 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 07:40:27 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 07:40:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 07:40:35 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 4 | 1-4 | 07:40:35 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 1-4 | 07:40:36 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-4 | 07:40:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 1-4 | 07:40:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-1 | 07:40:44 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 2-1 | 07:40:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 2-1 | 07:40:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-1 | 07:40:49 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4300 |  |
| Jogador 4 | 2-2 | 07:40:57 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 4 | 2-2 | 07:40:58 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-2 | 07:40:58 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-2 | 07:40:59 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-2 | 07:40:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 07:41:00 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 07:41:00 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 07:41:01 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 4 | 2-2 | 07:41:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 07:41:12 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-3 | 07:41:13 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-3 | 07:41:13 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 4 | 2-3 | 07:41:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-3 | 07:41:15 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-3 | 07:41:15 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 2-3 | 07:41:16 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 2-3 | 07:41:16 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 4 | 2-3 | 07:41:17 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.9500 |  |
| Jogador 4 | 2-4 | 07:41:27 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 1.0000 |  |
| Jogador 4 | 2-4 | 07:41:28 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 2-4 | 07:41:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-4 | 07:41:29 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 4 | 2-4 | 07:41:29 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 4 | 2-4 | 07:41:30 | MOVE Bench -> Board: Diana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 2-4 | 07:41:30 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 4 | 2-4 | 07:41:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 2-4 | 07:41:31 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-5 | 07:41:44 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 4 | 2-5 | 07:41:45 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 2-5 | 07:41:45 | MOVE Board -> Board: Karma (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 2-5 | 07:41:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-5 | 07:41:46 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 2-5 | 07:41:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-6 | 07:42:03 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 4 | 2-6 | 07:42:04 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 4 | 2-6 | 07:42:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-6 | 07:42:05 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 4 | 2-6 | 07:42:05 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.5900 |  |
| Jogador 4 | 2-6 | 07:42:06 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 4 | 2-6 | 07:42:06 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 4 | 2-6 | 07:42:07 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 2-6 | 07:42:08 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 07:42:24 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 2-7 | 07:42:24 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-7 | 07:42:25 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 2-7 | 07:42:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 07:42:26 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 4 | 2-7 | 07:42:27 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-7 | 07:42:27 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 2-7 | 07:42:28 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 2-7 | 07:42:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-1 | 07:42:46 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 4 | 3-1 | 07:42:47 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-1 | 07:42:47 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.6000 |  |
| Jogador 4 | 3-1 | 07:42:48 | MOVE Board -> Board: Yorick (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-1 | 07:42:48 | MOVE Board -> Board: Diana (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 3-1 | 07:42:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-2 | 07:43:10 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 4 | 3-2 | 07:43:10 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 4 | 3-2 | 07:43:11 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | -0.5500 |  |
| Jogador 4 | 3-2 | 07:43:11 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Sejuani (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 4 | 3-2 | 07:43:12 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Sejuani (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 4 | 3-2 | 07:43:13 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Sejuani (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 4 | 3-2 | 07:43:14 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 3-2 | 07:43:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-2 | 07:43:15 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 4 | 3-3 | 07:43:35 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-3 | 07:43:35 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.7000 |  |
| Jogador 4 | 3-3 | 07:43:36 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 3-3 | 07:43:36 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | -0.6200 |  |
| Jogador 4 | 3-3 | 07:43:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-3 | 07:43:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 4 | 3-3 | 07:43:38 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.4200 |  |
| Jogador 4 | 3-3 | 07:43:39 | MOVE Board -> Board: Akali (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 3-3 | 07:43:39 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-4 | 07:44:02 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-4 | 07:44:03 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 4 | 3-4 | 07:44:03 | MOVE Board -> Board: Yorick (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 07:44:04 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 3-4 | 07:44:05 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 4 | 3-4 | 07:44:05 | MOVE Bench -> Board: Alistar (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.4600 |  |
| Jogador 4 | 3-4 | 07:44:06 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 4 | 3-4 | 07:44:06 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 4 | 3-4 | 07:44:07 | MOVE Bench -> Board: Alistar (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 4 | 3-5 | 07:44:31 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-5 | 07:44:32 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 4 | 3-5 | 07:44:32 | MOVE Board -> Board: Karma (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-5 | 07:44:33 | MOVE Bench -> Board: Akali (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.3400 |  |
| Jogador 4 | 3-5 | 07:44:33 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 4 | 3-5 | 07:44:34 | MOVE Bench -> Board: Alistar (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 3-5 | 07:44:34 | MOVE Board -> Board: Master Yi (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 3-5 | 07:44:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 07:45:01 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_MasterYi_AD | 0.8300 |  |
| Jogador 4 | 3-6 | 07:45:02 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_MasterYi_AD | 0.4200 |  |
| Jogador 4 | 3-6 | 07:45:02 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_MasterYi_AD | 0.2300 |  |
| Jogador 4 | 3-6 | 07:45:02 | MOVE Board -> Board: Akali (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_MasterYi_AD | -0.1600 |  |
| Jogador 4 | 3-6 | 07:45:03 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_MasterYi_AD | 0.1400 |  |
| Jogador 4 | 3-6 | 07:45:03 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_MasterYi_AD | 0.0600 |  |
| Jogador 4 | 3-6 | 07:45:04 | MOVE Bench -> Board: Alistar (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_MasterYi_AD | -0.4200 |  |
| Jogador 4 | 3-6 | 07:45:05 | MOVE Bench -> Board: Karma (i:2.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 4 | 3-6 | 07:45:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 07:45:33 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_18_MasterYi_AD | 0.7700 |  |
| Jogador 4 | 3-7 | 07:45:34 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 4 | 3-7 | 07:45:34 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_18_MasterYi_AD | 0.2400 |  |
| Jogador 4 | 3-7 | 07:45:35 | VENDEU: Master Yi (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 3-7 | 07:45:35 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.7100 |  |
| Jogador 4 | 3-7 | 07:45:36 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 4 | 3-7 | 07:45:37 | MOVE Bench -> Board: Alistar (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 4 | 3-7 | 07:45:37 | MOVE Bench -> Board: Karma (i:2.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 4 | 3-7 | 07:45:38 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 4 | 4-1 | 07:46:07 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 4-1 | 07:46:08 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Florescer | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 4 | 4-1 | 07:46:08 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Florescer | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 4 | 4-1 | 07:46:09 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 1 | Florescer | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 4 | 4-1 | 07:46:09 | MOVE Bench -> Board: Yunara (i:8.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 1 | Florescer | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 4-1 | 07:46:10 | REROLL | STABILIZE | STABILIZE: pressão de vida | 9 | 1 | Florescer | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 4 | 4-1 | 07:46:10 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Florescer | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 4 | 4-1 | 07:46:11 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 1 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 4-1 | 07:46:11 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 4-2 | 07:46:43 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Florescer | DA_18_Yunara | 0.7500 |  |
| Jogador 4 | 4-2 | 07:46:43 | REROLL | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Florescer | DA_18_Yunara | -0.1300 |  |
| Jogador 4 | 4-2 | 07:46:44 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Florescer | DA_18_Yunara | -0.5000 |  |
| Jogador 4 | 4-2 | 07:46:44 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Florescer | DA_18_Yunara | -0.2400 |  |
| Jogador 4 | 4-2 | 07:46:45 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Florescer | DA_18_Yunara | -0.4000 |  |
| Jogador 4 | 4-2 | 07:46:45 | MOVE Bench -> Board: Karma (i:2.0) <-> Yunara (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Florescer | DA_18_Yunara | -0.8400 |  |
| Jogador 4 | 4-2 | 07:46:46 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Florescer | DA_18_Yunara | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-3 | 07:47:20 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Florescer | DA_18_Yunara | -0.0700 |  |
| Jogador 4 | 4-3 | 07:47:20 | VENDEU: Yunara (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 25 | 1 | Florescer | DA_18_Sivir | -0.6900 |  |
| Jogador 4 | 4-3 | 07:47:21 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Florescer | DA_18_Sivir | 0.8400 |  |
| Jogador 4 | 4-3 | 07:47:21 | MOVE Bench -> Board: Diana (i:6.0) <-> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Florescer | DA_18_Sivir | -0.3300 |  |
| Jogador 4 | 4-3 | 07:47:22 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Florescer | DA_18_Sivir | -0.0700 |  |
| Jogador 4 | 4-3 | 07:47:22 | VENDEU: Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Florescer | DA_18_Diana | 0.0100 |  |
| Jogador 4 | 4-3 | 07:47:22 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 21 | 1 | Florescer | DA_18_Diana | 0.9100 |  |
| Jogador 4 | 4-3 | 07:47:23 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 21 | 1 | Florescer | DA_18_Diana | 0.1200 |  |
| Jogador 4 | 4-3 | 07:47:23 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 21 | 1 | Florescer | DA_18_Diana | 0.5600 |  |
| Jogador 4 | 4-4 | 07:47:58 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 27 | 2 | Florescer | DA_18_Diana | 0.3300 |  |
| Jogador 4 | 4-4 | 07:47:59 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 2 | Florescer | DA_18_Diana | 0.8600 |  |
| Jogador 4 | 4-4 | 07:47:59 | MOVE Board -> Board: Sejuani (i:4.0) <-> Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 2 | Florescer | DA_18_Diana | -0.0400 |  |
| Jogador 4 | 4-4 | 07:48:00 | MOVE Board -> Board: Akali (i:2.0) <-> LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 2 | Florescer | DA_18_Diana | -0.2500 |  |
| Jogador 4 | 4-4 | 07:48:00 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 24 | 2 | Florescer | DA_18_Diana | -0.3800 |  |
| Jogador 4 | 4-5 | 07:48:38 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 2 | Florescer | DA_Fiddlesticks18 | -0.6100 |  |
| Jogador 4 | 4-5 | 07:48:39 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 40 | 2 | Florescer | DA_Fiddlesticks18 | 0.7900 |  |
| Jogador 4 | 4-5 | 07:48:40 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 40 | 2 | Florescer | DA_Fiddlesticks18 | 0.0400 |  |
| Jogador 4 | 4-5 | 07:48:40 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 38 | 2 | Florescer | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 4 | 4-5 | 07:48:41 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 2 | Florescer | DA_Fiddlesticks18 | -0.6700 |  |
| Jogador 4 | 4-5 | 07:48:41 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 2 | Florescer | DA_Fiddlesticks18 | 0.8900 |  |
| Jogador 4 | 4-5 | 07:48:42 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 2 | Florescer | DA_Fiddlesticks18 | -0.1300 |  |
| Jogador 4 | 4-5 | 07:48:42 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 36 | 2 | Florescer | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 4 | 4-5 | 07:48:43 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 39 | 2 | Florescer | DA_Fiddlesticks18 | -0.7500 |  |
| Jogador 4 | 4-6 | 07:49:22 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 47 | 4 | Florescer | DA_Fiddlesticks18 | 1.0300 |  |
| Jogador 4 | 4-6 | 07:49:22 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 45 | 4 | Florescer | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 4 | 4-6 | 07:49:22 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 4 | Florescer | DA_Fiddlesticks18 | 1.0400 |  |
| Jogador 4 | 4-6 | 07:49:23 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 42 | 4 | Florescer | DA_Fiddlesticks18 | 0.5700 |  |
| Jogador 4 | 4-6 | 07:49:23 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 42 | 4 | Florescer | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 4 | 4-6 | 07:49:24 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 4 | Florescer | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 4 | 4-6 | 07:49:24 | MOVE Board -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 4 | Florescer | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 4 | 4-6 | 07:49:25 | MOVE Board -> Board: Sejuani (i:4.0) <-> Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 4 | Florescer | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 4 | 4-6 | 07:49:25 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 38 | 4 | Florescer | DA_Fiddlesticks18 | -0.5700 |  |
| Jogador 4 | 4-7 | 07:50:05 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_Fiddlesticks18 | 0.2400 |  |
| Jogador 4 | 4-7 | 07:50:06 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_TearOfTheGoddess -> Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 4 | 4-7 | 07:50:06 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Florescer | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 4 | 4-7 | 07:50:07 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Florescer | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 4 | 4-7 | 07:50:07 | MOVE Board -> Board: Akali (i:2.0) <-> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Florescer | DA_Fiddlesticks18 | -0.1400 |  |
| Jogador 4 | 4-7 | 07:50:07 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Florescer | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 4 | 4-7 | 07:50:08 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Florescer | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 4 | 4-7 | 07:50:09 | MOVE Board -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Florescer | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 4 | 4-7 | 07:50:09 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Florescer | DA_Fiddlesticks18 | -0.4500 |  |
| Jogador 5 | ? | 07:40:03 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | ? | 07:40:05 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 5 | ? | 07:40:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 07:40:10 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 07:40:11 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 07:40:11 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-1 | 07:40:12 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 07:40:12 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 07:40:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 07:40:15 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4300 |  |
| Jogador 5 | 1-2 | 07:40:18 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 1-2 | 07:40:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 07:40:27 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 07:40:27 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 07:40:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 07:40:35 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 07:40:35 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 5 | 1-4 | 07:40:36 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 5 | 1-4 | 07:40:36 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 5 | 1-4 | 07:40:37 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 07:40:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 07:40:44 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-1 | 07:40:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 07:40:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 07:40:57 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 5 | 2-2 | 07:40:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 2-2 | 07:40:58 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 5 | 2-2 | 07:40:59 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 07:40:59 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 5 | 2-2 | 07:41:00 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 07:41:00 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0300 |  |
| Jogador 5 | 2-2 | 07:41:01 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-2 | 07:41:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 07:41:12 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | 0.3100 |  |
| Jogador 5 | 2-3 | 07:41:13 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-3 | 07:41:13 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-3 | 07:41:14 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-3 | 07:41:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 07:41:15 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 07:41:16 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 07:41:16 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | 0.1900 |  |
| Jogador 5 | 2-3 | 07:41:17 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.1800 |  |
| Jogador 5 | 2-4 | 07:41:27 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2700 |  |
| Jogador 5 | 2-4 | 07:41:28 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-4 | 07:41:28 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-4 | 07:41:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 07:41:29 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-4 | 07:41:30 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.4100 |  |
| Jogador 5 | 2-4 | 07:41:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-4 | 07:41:31 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1000 |  |
| Jogador 5 | 2-4 | 07:41:31 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3600 |  |
| Jogador 5 | 2-5 | 07:41:44 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | 1.1200 |  |
| Jogador 5 | 2-5 | 07:41:45 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-5 | 07:41:45 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0200 |  |
| Jogador 5 | 2-5 | 07:41:45 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.6300 |  |
| Jogador 5 | 2-5 | 07:41:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-5 | 07:41:47 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1400 |  |
| Jogador 5 | 2-5 | 07:41:48 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1000 |  |
| Jogador 5 | 2-5 | 07:41:48 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1700 |  |
| Jogador 5 | 2-5 | 07:41:49 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1800 |  |
| Jogador 5 | 2-6 | 07:42:03 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2100 |  |
| Jogador 5 | 2-6 | 07:42:04 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1400 |  |
| Jogador 5 | 2-6 | 07:42:04 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1400 |  |
| Jogador 5 | 2-6 | 07:42:05 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-6 | 07:42:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-6 | 07:42:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-7 | 07:42:24 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-7 | 07:42:24 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1300 |  |
| Jogador 5 | 2-7 | 07:42:25 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1600 |  |
| Jogador 5 | 2-7 | 07:42:25 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-7 | 07:42:26 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-7 | 07:42:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 2-7 | 07:42:27 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1000 |  |
| Jogador 5 | 2-7 | 07:42:28 | MOVE Board -> Board: Veigar (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 2-7 | 07:42:28 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 3-1 | 07:42:46 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.7200 |  |
| Jogador 5 | 3-1 | 07:42:47 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 3-1 | 07:42:47 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0500 |  |
| Jogador 5 | 3-1 | 07:42:48 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1300 |  |
| Jogador 5 | 3-1 | 07:42:48 | MOVE Board -> Board: Kobuko (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0200 |  |
| Jogador 5 | 3-1 | 07:42:49 | MOVE Board -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0400 |  |
| Jogador 5 | 3-1 | 07:42:49 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3900 |  |
| Jogador 5 | 3-1 | 07:42:50 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 3-1 | 07:42:50 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 3-2 | 07:43:10 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.7100 |  |
| Jogador 5 | 3-2 | 07:43:10 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2800 |  |
| Jogador 5 | 3-2 | 07:43:11 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2900 |  |
| Jogador 5 | 3-2 | 07:43:11 | MOVE Board -> Board: Veigar (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 3-2 | 07:43:12 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 3-2 | 07:43:13 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3500 |  |
| Jogador 5 | 3-2 | 07:43:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 3-3 | 07:43:35 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.8100 |  |
| Jogador 5 | 3-3 | 07:43:35 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.8100 |  |
| Jogador 5 | 3-3 | 07:43:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 3-3 | 07:43:36 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 3-3 | 07:43:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 3-3 | 07:43:37 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.5400 |  |
| Jogador 5 | 3-3 | 07:43:38 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3300 |  |
| Jogador 5 | 3-3 | 07:43:39 | MOVE Board -> Board: Rammus (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 3-3 | 07:43:39 | MOVE Board -> Board: Veigar (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 3-4 | 07:44:02 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2900 |  |
| Jogador 5 | 3-4 | 07:44:03 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1500 |  |
| Jogador 5 | 3-4 | 07:44:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 3-4 | 07:44:04 | MOVE Board -> Board: Yorick (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 3-4 | 07:44:05 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0200 |  |
| Jogador 5 | 3-4 | 07:44:05 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 3-4 | 07:44:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 3-5 | 07:44:31 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Rammus | 0.8300 |  |
| Jogador 5 | 3-5 | 07:44:32 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Rammus | 0.7100 |  |
| Jogador 5 | 3-5 | 07:44:32 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Rammus | 0.0100 |  |
| Jogador 5 | 3-5 | 07:44:33 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.5600 |  |
| Jogador 5 | 3-5 | 07:44:33 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 5 | 3-5 | 07:44:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0300 |  |
| Jogador 5 | 3-5 | 07:44:34 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 5 | 3-5 | 07:44:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0300 |  |
| Jogador 5 | 3-5 | 07:44:35 | MOVE Board -> Board: Veigar (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 5 | 3-6 | 07:45:01 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.5100 |  |
| Jogador 5 | 3-6 | 07:45:02 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.4300 |  |
| Jogador 5 | 3-6 | 07:45:02 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 5 | 3-6 | 07:45:02 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 5 | 3-6 | 07:45:03 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 3-6 | 07:45:03 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 5 | 3-6 | 07:45:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0300 |  |
| Jogador 5 | 3-6 | 07:45:05 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.4700 |  |
| Jogador 5 | 3-6 | 07:45:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0300 |  |
| Jogador 5 | 3-7 | 07:45:33 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.2800 |  |
| Jogador 5 | 3-7 | 07:45:34 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.3800 |  |
| Jogador 5 | 3-7 | 07:45:34 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1900 |  |
| Jogador 5 | 3-7 | 07:45:35 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1200 |  |
| Jogador 5 | 3-7 | 07:45:35 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.4800 |  |
| Jogador 5 | 3-7 | 07:45:36 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0300 |  |
| Jogador 5 | 3-7 | 07:45:37 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 3-7 | 07:45:37 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 5 | 3-7 | 07:45:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 4-1 | 07:46:07 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 4-1 | 07:46:08 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.8100 |  |
| Jogador 5 | 4-1 | 07:46:08 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0400 |  |
| Jogador 5 | 4-1 | 07:46:09 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0200 |  |
| Jogador 5 | 4-1 | 07:46:09 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.4100 |  |
| Jogador 5 | 4-1 | 07:46:10 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 5 | 4-1 | 07:46:10 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 4-1 | 07:46:11 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 5 | 4-1 | 07:46:11 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 5 | 4-2 | 07:46:43 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 5 | 4-2 | 07:46:43 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.8000 |  |
| Jogador 5 | 4-2 | 07:46:44 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.4600 |  |
| Jogador 5 | 4-2 | 07:46:44 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.8400 |  |
| Jogador 5 | 4-2 | 07:46:45 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.7800 |  |
| Jogador 5 | 4-2 | 07:46:45 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.5800 |  |
| Jogador 5 | 4-2 | 07:46:46 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Aronguejo (i:4.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 5 | 4-2 | 07:46:46 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.2800 |  |
| Jogador 5 | 4-2 | 07:46:47 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.5600 |  |
| Jogador 5 | 4-3 | 07:47:20 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.7200 |  |
| Jogador 5 | 4-3 | 07:47:20 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.9600 |  |
| Jogador 5 | 4-3 | 07:47:21 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.2900 |  |
| Jogador 5 | 4-3 | 07:47:21 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 4-3 | 07:47:22 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 5 | 4-3 | 07:47:22 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 5 | 4-3 | 07:47:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-4 | 07:47:58 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.5900 |  |
| Jogador 5 | 4-4 | 07:47:59 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.8200 |  |
| Jogador 5 | 4-4 | 07:47:59 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.9600 |  |
| Jogador 5 | 4-4 | 07:48:00 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1700 |  |
| Jogador 5 | 4-4 | 07:48:00 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0300 |  |
| Jogador 5 | 4-4 | 07:48:00 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1400 |  |
| Jogador 5 | 4-4 | 07:48:01 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 4-4 | 07:48:01 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 5 | 4-4 | 07:48:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-5 | 07:48:38 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 5 | 4-5 | 07:48:39 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Espinhos Negros | DA_CrimsonRaptor18 | 0.8900 |  |
| Jogador 5 | 4-5 | 07:48:40 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 5 | 4-5 | 07:48:40 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Espinhos Negros | DA_Sentinel18 | -0.4900 |  |
| Jogador 5 | 4-5 | 07:48:41 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Espinhos Negros | DA_Sentinel18 | 0.1600 |  |
| Jogador 5 | 4-5 | 07:48:41 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Espinhos Negros | DA_Sentinel18 | 0.5200 |  |
| Jogador 5 | 4-5 | 07:48:42 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Espinhos Negros | DA_Sentinel18 | 0.0700 |  |
| Jogador 5 | 4-5 | 07:48:42 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 4-5 | 07:48:43 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Espinhos Negros | DA_Sentinel18 | -0.0200 |  |
| Jogador 5 | 4-6 | 07:49:22 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Espinhos Negros | DA_Sentinel18 | -0.0300 |  |
| Jogador 5 | 4-6 | 07:49:22 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Espinhos Negros | DA_Sentinel18 | 0.3500 |  |
| Jogador 5 | 4-6 | 07:49:22 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Espinhos Negros | DA_Sentinel18 | -0.0300 |  |
| Jogador 5 | 4-6 | 07:49:23 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Espinhos Negros | DA_Sentinel18 | -0.2600 |  |
| Jogador 5 | 4-6 | 07:49:23 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 4-6 | 07:49:24 | MOVE Board -> Board: Veigar (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Espinhos Negros | DA_Sentinel18 | -0.2200 |  |
| Jogador 5 | 4-6 | 07:49:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Espinhos Negros | DA_Sentinel18 | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-7 | 07:50:05 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NeedlesslyLargeRod -> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Espinhos Negros | DA_Sentinel18 | 0.0900 |  |
| Jogador 5 | 4-7 | 07:50:06 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Espinhos Negros | DA_Sentinel18 | 0.0800 |  |
| Jogador 5 | 4-7 | 07:50:06 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Espinhos Negros | DA_Sentinel18 | 0.0900 |  |
| Jogador 5 | 4-7 | 07:50:07 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 5 | 4-7 | 07:50:07 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.4900 |  |
| Jogador 5 | 4-7 | 07:50:07 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 5 | 4-7 | 07:50:08 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.5500 |  |
| Jogador 5 | 4-7 | 07:50:09 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Espinhos Negros | DA_KogMaw18_AD | -0.1700 |  |
| Jogador 5 | 4-7 | 07:50:09 | MOVE Board -> Board: Rammus (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-1 | 07:50:52 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 4 | Espinhos Negros | DA_Sentinel18 | -0.5800 |  |
| Jogador 5 | 5-1 | 07:50:52 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 4 | Espinhos Negros | DA_Sentinel18 | 0.7900 |  |
| Jogador 5 | 5-1 | 07:50:53 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Rek'Sai (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 4 | Espinhos Negros | DA_Sentinel18 | 0.0900 |  |
| Jogador 5 | 5-1 | 07:50:53 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Rek'Sai (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 4 | Espinhos Negros | DA_Sentinel18 | 0.0700 |  |
| Jogador 5 | 5-1 | 07:50:54 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 4 | Espinhos Negros | DA_Sentinel18 | -0.0300 |  |
| Jogador 5 | 5-1 | 07:50:55 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 4 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 5-1 | 07:50:55 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 4 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 5-1 | 07:50:56 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 4 | Espinhos Negros | DA_Sentinel18 | -0.0300 |  |
| Jogador 5 | 5-1 | 07:50:56 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 4 | Espinhos Negros | DA_Sentinel18 | -0.1100 |  |
| Jogador 5 | 5-2 | 07:51:42 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0300 |  |
| Jogador 5 | 5-2 | 07:51:42 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Espinhos Negros | DA_Sentinel18 | 0.0700 |  |
| Jogador 5 | 5-2 | 07:51:43 | MOVE Bench -> Board: Krugue (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Espinhos Negros | DA_Sentinel18 | -0.4000 |  |
| Jogador 5 | 5-2 | 07:51:43 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Espinhos Negros | DA_Sentinel18 | -0.3800 |  |
| Jogador 5 | 5-2 | 07:51:44 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Espinhos Negros | DA_Sentinel18 | -0.1000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 5-3 | 07:52:33 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0200 |  |
| Jogador 5 | 5-3 | 07:52:34 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Espinhos Negros | DA_Sentinel18 | 0.9500 |  |
| Jogador 5 | 5-3 | 07:52:34 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Espinhos Negros | DA_Sentinel18 | -0.5900 |  |
| Jogador 5 | 5-3 | 07:52:35 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Espinhos Negros | DA_Sentinel18 | -0.1100 |  |
| Jogador 5 | 5-3 | 07:52:35 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 5-3 | 07:52:35 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Espinhos Negros | DA_Sentinel18 | -0.1100 |  |
| Jogador 5 | 5-3 | 07:52:36 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Espinhos Negros | DA_Sentinel18 | 0.1000 |  |
| Jogador 5 | 5-3 | 07:52:36 | MOVE Bench -> Board: Krugue (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Espinhos Negros | DA_Sentinel18 | -0.4100 |  |
| Jogador 5 | 5-3 | 07:52:37 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Espinhos Negros | DA_Sentinel18 | -0.3100 |  |
| Jogador 5 | 5-4 | 07:53:22 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 5-4 | 07:53:22 | COMPROU: Alune (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 91 | 5 | Espinhos Negros | DA_Sentinel18 | 0.2500 |  |
| Jogador 5 | 5-4 | 07:53:23 | VENDEU: Alune (i:10.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0600 |  |
| Jogador 5 | 5-4 | 07:53:23 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Espinhos Negros | DA_Sentinel18 | 0.2400 |  |
| Jogador 5 | 5-4 | 07:53:24 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0700 |  |
| Jogador 5 | 5-4 | 07:53:24 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Espinhos Negros | DA_Sentinel18 | 0.2200 |  |
| Jogador 5 | 5-4 | 07:53:25 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Espinhos Negros | DA_Sentinel18 | -0.0500 |  |
| Jogador 5 | 5-4 | 07:53:25 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Espinhos Negros | DA_Sentinel18 | -0.1600 |  |
| Jogador 5 | 5-4 | 07:53:25 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Espinhos Negros | DA_Sentinel18 | -0.4000 |  |
| Jogador 5 | 5-5 | 07:54:12 | VENDEU: Azuporã (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 107 | 5 | Espinhos Negros | DA_18_Azir | -0.3900 |  |
| Jogador 5 | 5-5 | 07:54:13 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 105 | 5 | Espinhos Negros | DA_18_Azir | 0.1100 |  |
| Jogador 5 | 5-5 | 07:54:13 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 107 | 5 | Espinhos Negros | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 5-5 | 07:54:14 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 105 | 5 | Espinhos Negros | DA_18_Azir | 0.1100 |  |
| Jogador 5 | 5-5 | 07:54:14 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 107 | 5 | Espinhos Negros | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 5-5 | 07:54:15 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 106 | 5 | Espinhos Negros | DA_18_Azir | -0.0800 |  |
| Jogador 5 | 5-5 | 07:54:15 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 107 | 5 | Espinhos Negros | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 5-5 | 07:54:16 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 105 | 5 | Espinhos Negros | DA_18_Azir | -0.1700 |  |
| Jogador 5 | 5-5 | 07:54:16 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 107 | 5 | Espinhos Negros | DA_18_Azir | 0.0100 |  |
| Jogador 5 | 5-6 | 07:55:05 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Espinhos Negros | DA_18_Azir | 0.6200 |  |
| Jogador 5 | 5-6 | 07:55:05 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Espinhos Negros | DA_18_Azir | -0.5300 |  |
| Jogador 5 | 5-6 | 07:55:06 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Espinhos Negros | DA_18_Azir | 0.2800 |  |
| Jogador 5 | 5-6 | 07:55:06 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Espinhos Negros | DA_18_Azir | -0.0600 |  |
| Jogador 5 | 5-6 | 07:55:06 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Espinhos Negros | DA_18_Azir | 0.2800 |  |
| Jogador 5 | 5-6 | 07:55:07 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Espinhos Negros | DA_18_Azir | -0.0600 |  |
| Jogador 5 | 5-6 | 07:55:07 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Espinhos Negros | DA_18_Azir | 0.2100 |  |
| Jogador 5 | 5-6 | 07:55:08 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Espinhos Negros | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 5-6 | 07:55:08 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Espinhos Negros | DA_18_Azir | -0.1600 |  |
| Jogador 5 | 5-7 | 07:55:54 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Kha'Zix (i:6.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Espinhos Negros | DA_18_Azir | 0.0900 |  |
| Jogador 5 | 5-7 | 07:55:54 | VENDEU: Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Espinhos Negros | DA_18_Azir | 0.0100 |  |
| Jogador 5 | 5-7 | 07:55:54 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Espinhos Negros | DA_18_Azir | 0.0700 |  |
| Jogador 5 | 5-7 | 07:55:55 | VENDEU: Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Espinhos Negros | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 5-7 | 07:55:55 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Espinhos Negros | DA_18_Azir | 0.1400 |  |
| Jogador 5 | 5-7 | 07:55:55 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Espinhos Negros | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 5-7 | 07:55:56 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Espinhos Negros | DA_18_Azir | 0.1400 |  |
| Jogador 5 | 5-7 | 07:55:57 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Espinhos Negros | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 5-7 | 07:55:57 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Espinhos Negros | DA_18_Azir | 0.1300 |  |
| Jogador 5 | 6-1 | 07:56:48 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Espinhos Negros | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 6-1 | 07:56:48 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Espinhos Negros | DA_18_Azir | 1.1100 |  |
| Jogador 5 | 6-1 | 07:56:48 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Espinhos Negros | DA_18_Azir | 0.2800 |  |
| Jogador 5 | 6-1 | 07:56:49 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Espinhos Negros | DA_18_Azir | 0.1600 |  |
| Jogador 5 | 6-1 | 07:56:49 | VENDEU: Azir (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Espinhos Negros | DA_18_Lillia | -0.7400 |  |
| Jogador 5 | 6-1 | 07:56:50 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Espinhos Negros | DA_18_Lillia | -0.1400 |  |
| Jogador 5 | 6-1 | 07:56:50 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Espinhos Negros | DA_18_Lillia | 0.6000 |  |
| Jogador 5 | 6-1 | 07:56:51 | COMPROU: Camille (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Espinhos Negros | DA_18_Lillia | -0.2000 |  |
| Jogador 5 | 6-1 | 07:56:51 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Espinhos Negros | DA_18_Lillia | 0.0000 |  |
| Jogador 5 | 6-2 | 07:57:42 | VENDEU: Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Espinhos Negros | DA_18_Lillia | 0.0100 |  |
| Jogador 5 | 6-2 | 07:57:43 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Espinhos Negros | DA_18_Lillia | 0.5000 |  |
| Jogador 5 | 6-2 | 07:57:43 | VENDEU: Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Espinhos Negros | DA_18_Lillia | 0.0000 |  |
| Jogador 5 | 6-2 | 07:57:44 | COMPROU: Maokai (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Espinhos Negros | DA_18_Lillia | 0.1600 |  |
| Jogador 5 | 6-2 | 07:57:44 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Espinhos Negros | DA_18_Lillia | -0.0600 |  |
| Jogador 5 | 6-2 | 07:57:44 | COMPROU: Lux (Solar) (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Espinhos Negros | DA_18_Lillia | -0.1200 |  |
| Jogador 5 | 6-2 | 07:57:45 | VENDEU: Lux (Solar) (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Espinhos Negros | DA_18_Lillia | -0.0100 |  |
| Jogador 5 | 6-2 | 07:57:45 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Espinhos Negros | DA_18_Lillia | 0.1100 |  |
| Jogador 5 | 6-2 | 07:57:46 | MOVE Board -> Board: Rammus (i:6.0) <-> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Espinhos Negros | DA_18_Lillia | 0.0000 |  |
| Jogador 5 | 6-3 | 07:58:42 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Espinhos Negros | DA_18_Lillia | -0.0100 |  |
| Jogador 5 | 6-3 | 07:58:42 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 151 | 5 | Espinhos Negros | DA_18_Lillia | 0.1400 |  |
| Jogador 5 | 6-3 | 07:58:42 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Espinhos Negros | DA_18_Lillia | -0.0200 |  |
| Jogador 5 | 6-3 | 07:58:43 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Espinhos Negros | DA_18_Lillia | -0.1000 |  |
| Jogador 5 | 6-3 | 07:58:43 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Espinhos Negros | DA_18_Lillia | -0.0100 |  |
| Jogador 5 | 6-3 | 07:58:44 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Espinhos Negros | DA_18_Lillia | 0.0500 |  |
| Jogador 5 | 6-3 | 07:58:44 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Espinhos Negros | DA_18_Lillia | 0.0000 |  |
| Jogador 5 | 6-3 | 07:58:45 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Espinhos Negros | DA_18_Lillia | -0.2300 |  |
| Jogador 5 | 6-3 | 07:58:45 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Espinhos Negros | DA_18_Lillia | 0.0200 |  |
| Jogador 5 | 6-4 | 07:59:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Espinhos Negros | DA_18_Rammus | 1.1100 |  |
| Jogador 5 | 6-4 | 07:59:44 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 160 | 5 | Espinhos Negros | DA_18_Rammus | 0.6100 |  |
| Jogador 5 | 6-4 | 07:59:44 | VENDEU: Rammus (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 168 | 5 | Espinhos Negros | DA_18_Maokai | -0.7400 |  |
| Jogador 5 | 6-4 | 07:59:45 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Espinhos Negros | DA_18_Maokai | 0.6900 |  |
| Jogador 5 | 6-4 | 07:59:45 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 168 | 5 | Espinhos Negros | DA_18_Maokai | -0.6100 |  |
| Jogador 5 | 6-4 | 07:59:46 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 165 | 5 | Espinhos Negros | DA_18_Maokai | 0.0300 |  |
| Jogador 5 | 6-4 | 07:59:46 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 168 | 5 | Espinhos Negros | DA_18_Maokai | 0.0000 |  |
| Jogador 5 | 6-4 | 07:59:46 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 167 | 5 | Espinhos Negros | DA_18_Maokai | -0.2400 |  |
| Jogador 5 | 6-4 | 07:59:47 | VENDEU: Ornn (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 168 | 5 | Espinhos Negros | DA_18_Maokai | 0.0200 |  |
| Jogador 5 | 6-5 | 08:00:45 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Espinhos Negros | DA_18_Maokai | 0.7300 |  |
| Jogador 5 | 6-5 | 08:00:46 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Espinhos Negros | DA_18_Maokai | -0.5900 |  |
| Jogador 5 | 6-5 | 08:00:46 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 174 | 5 | Espinhos Negros | DA_18_Lillia | 1.0700 |  |
| Jogador 5 | 6-5 | 08:00:46 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 171 | 5 | Espinhos Negros | DA_18_Lillia | 0.4900 |  |
| Jogador 5 | 6-5 | 08:00:49 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 167 | 5 | Espinhos Negros | DA_18_Lillia | 0.2300 |  |
| Jogador 5 | 6-5 | 08:00:50 | VENDEU: Lillia (i:16.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Espinhos Negros | DA_18_Maokai | -0.6000 |  |
| Jogador 5 | 6-5 | 08:00:51 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Espinhos Negros | DA_18_Maokai | 0.6000 |  |
| Jogador 5 | 6-5 | 08:00:51 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Espinhos Negros | DA_18_Maokai | -0.1000 |  |
| Jogador 6 | ? | 07:40:03 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 07:40:05 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | -0.1500 |  |
| Jogador 6 | ? | 07:40:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 07:40:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 07:40:11 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 07:40:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 07:40:15 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2200 |  |
| Jogador 6 | 1-2 | 07:40:18 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 6 | 1-2 | 07:40:18 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 6 | 1-2 | 07:40:18 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 07:40:19 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 07:40:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-2 | 07:40:23 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.5700 |  |
| Jogador 6 | 1-3 | 07:40:27 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0200 |  |
| Jogador 6 | 1-3 | 07:40:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 07:40:35 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 1-4 | 07:40:35 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 6 | 1-4 | 07:40:36 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 6 | 1-4 | 07:40:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 6 | 1-4 | 07:40:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 2-1 | 07:40:44 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-1 | 07:40:45 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-1 | 07:40:45 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-1 | 07:40:45 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-1 | 07:40:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 07:40:57 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-2 | 07:40:58 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-2 | 07:40:58 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-2 | 07:40:59 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 07:40:59 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 07:41:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 07:41:12 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-3 | 07:41:13 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-3 | 07:41:13 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | 0.8100 |  |
| Jogador 6 | 2-3 | 07:41:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 07:41:15 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-3 | 07:41:15 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-3 | 07:41:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 07:41:16 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-3 | 07:41:17 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-4 | 07:41:27 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | 0.8600 |  |
| Jogador 6 | 2-4 | 07:41:28 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-4 | 07:41:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 07:41:29 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | -0.4500 |  |
| Jogador 6 | 2-4 | 07:41:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 07:41:30 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | -0.4900 |  |
| Jogador 6 | 2-4 | 07:41:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 6 | 2-4 | 07:41:31 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.2000 |  |
| Jogador 6 | 2-4 | 07:41:31 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Yorick | -0.6300 |  |
| Jogador 6 | 2-5 | 07:41:44 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 6 | 2-5 | 07:41:45 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 2-5 | 07:41:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 6 | 2-5 | 07:41:45 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Yorick | -0.1600 |  |
| Jogador 6 | 2-5 | 07:41:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | -0.0600 |  |
| Jogador 6 | 2-5 | 07:41:47 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | -0.4800 |  |
| Jogador 6 | 2-5 | 07:41:48 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Yorick | -1.0200 |  |
| Jogador 6 | 2-5 | 07:41:48 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.3300 |  |
| Jogador 6 | 2-5 | 07:41:49 | MOVE Bench -> Board: Kayle (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.3700 |  |
| Jogador 6 | 2-6 | 07:42:03 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 2-6 | 07:42:04 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 6 | 2-6 | 07:42:04 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 2-6 | 07:42:05 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 6 | 2-6 | 07:42:05 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Xayah | -0.1600 |  |
| Jogador 6 | 2-6 | 07:42:06 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Xayah | 0.2400 |  |
| Jogador 6 | 2-6 | 07:42:06 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Fumegante | DA_18_Xayah | 0.0300 |  |
| Jogador 6 | 2-6 | 07:42:07 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Xayah | 0.2000 |  |
| Jogador 6 | 2-6 | 07:42:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Xayah | -0.0400 |  |
| Jogador 6 | 2-7 | 07:42:24 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 6 | 2-7 | 07:42:24 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_Fiddlesticks18 | 0.1900 |  |
| Jogador 6 | 2-7 | 07:42:25 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 6 | 2-7 | 07:42:25 | MOVE Bench -> Board: Elise (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_Fiddlesticks18 | -0.3300 |  |
| Jogador 6 | 2-7 | 07:42:26 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Ahri | -0.1000 |  |
| Jogador 6 | 2-7 | 07:42:27 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Ahri | 0.0000 |  |
| Jogador 6 | 2-7 | 07:42:27 | MOVE Board -> Board: Elise (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Ahri | -0.0700 |  |
| Jogador 6 | 2-7 | 07:42:28 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Ahri | -0.0900 |  |
| Jogador 6 | 2-7 | 07:42:28 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Fumegante | DA_18_Xayah | -0.0200 |  |
| Jogador 6 | 3-1 | 07:42:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Fumegante | DA_18_Rakan | 0.8400 |  |
| Jogador 6 | 3-1 | 07:42:47 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Fumegante | DA_18_Rakan | 0.8300 |  |
| Jogador 6 | 3-1 | 07:42:47 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Fumegante | DA_18_Rakan | 0.1800 |  |
| Jogador 6 | 3-1 | 07:42:48 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Fumegante | DA_18_Rakan | -0.4200 |  |
| Jogador 6 | 3-1 | 07:42:48 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Fumegante | DA_18_Rakan | 0.1600 |  |
| Jogador 6 | 3-1 | 07:42:49 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Fumegante | DA_18_Rakan | 0.1900 |  |
| Jogador 6 | 3-1 | 07:42:49 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Fumegante | DA_18_Rakan | 0.1400 |  |
| Jogador 6 | 3-1 | 07:42:50 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Fumegante | DA_18_Rakan | -0.0300 |  |
| Jogador 6 | 3-1 | 07:42:50 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Fumegante | DA_18_Rakan | -0.1100 |  |
| Jogador 6 | 3-2 | 07:43:10 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Fumegante | DA_18_Rakan | -0.1200 |  |
| Jogador 6 | 3-2 | 07:43:10 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Fumegante | DA_18_Tristana | -0.5500 |  |
| Jogador 6 | 3-2 | 07:43:11 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Fumegante | DA_18_Tristana | -0.3700 |  |
| Jogador 6 | 3-2 | 07:43:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Tristana | 0.0300 |  |
| Jogador 6 | 3-2 | 07:43:12 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 3-2 | 07:43:13 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 3-2 | 07:43:14 | MOVE Board -> Board: Yorick (i:2.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-2 | 07:43:14 | MOVE Board -> Board: Elise (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | 0.2800 |  |
| Jogador 6 | 3-2 | 07:43:15 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | 0.4200 |  |
| Jogador 6 | 3-3 | 07:43:35 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Tristana | 0.0900 |  |
| Jogador 6 | 3-3 | 07:43:35 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | 0.1200 |  |
| Jogador 6 | 3-3 | 07:43:36 | MOVE Board -> Board: Xayah (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-3 | 07:43:36 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-3 | 07:43:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-4 | 07:44:02 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Tristana | 0.2800 |  |
| Jogador 6 | 3-4 | 07:44:03 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | 0.3100 |  |
| Jogador 6 | 3-4 | 07:44:03 | MOVE Board -> Board: Varus (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-4 | 07:44:04 | MOVE Board -> Board: Xayah (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-4 | 07:44:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-5 | 07:44:31 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Tristana | 0.6300 |  |
| Jogador 6 | 3-5 | 07:44:32 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Diana | 0.7500 |  |
| Jogador 6 | 3-5 | 07:44:32 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Diana | -0.0100 |  |
| Jogador 6 | 3-5 | 07:44:33 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Diana | 0.0200 |  |
| Jogador 6 | 3-5 | 07:44:33 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Diana | -0.0600 |  |
| Jogador 6 | 3-5 | 07:44:34 | MOVE Board -> Board: Xayah (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Diana | 0.0100 |  |
| Jogador 6 | 3-5 | 07:44:34 | MOVE Board -> Board: Varus (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Diana | -0.0100 |  |
| Jogador 6 | 3-5 | 07:44:35 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Diana | -0.0800 |  |
| Jogador 6 | 3-5 | 07:44:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Diana | 0.0000 |  |
| Jogador 6 | 3-6 | 07:45:01 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Diana | 0.6000 |  |
| Jogador 6 | 3-6 | 07:45:02 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Diana | 0.4400 |  |
| Jogador 6 | 3-6 | 07:45:02 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Diana | 0.0700 |  |
| Jogador 6 | 3-6 | 07:45:02 | MOVE Board -> Board: Tristana (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Diana | -0.0400 |  |
| Jogador 6 | 3-6 | 07:45:03 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Diana | 0.0100 |  |
| Jogador 6 | 3-6 | 07:45:03 | MOVE Board -> Board: Xayah (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Diana | -0.0100 |  |
| Jogador 6 | 3-6 | 07:45:04 | MOVE Board -> Board: Tristana (i:6.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Diana | -0.0100 |  |
| Jogador 6 | 3-6 | 07:45:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Diana | 0.0000 |  |
| Jogador 6 | 3-7 | 07:45:33 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Fumegante | DA_18_Diana | 0.1300 |  |
| Jogador 6 | 3-7 | 07:45:34 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Fumegante | DA_18_Diana | 0.1300 |  |
| Jogador 6 | 3-7 | 07:45:34 | VENDEU: Diana (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Fumegante | DA_18_Zyra | 0.0000 |  |
| Jogador 6 | 3-7 | 07:45:35 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Fumegante | DA_18_Zyra | 0.5800 |  |
| Jogador 6 | 3-7 | 07:45:35 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Fumegante | DA_18_Zyra | 0.0700 |  |
| Jogador 6 | 3-7 | 07:45:36 | MOVE Board -> Board: Varus (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Fumegante | DA_18_Zyra | -0.2200 |  |
| Jogador 6 | 3-7 | 07:45:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Fumegante | DA_18_Zyra | 0.2100 |  |
| Jogador 6 | 3-7 | 07:45:37 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Fumegante | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 3-7 | 07:45:38 | MOVE Board -> Board: Xayah (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Fumegante | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 4-1 | 07:46:07 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Fumegante | DA_18_Zyra | -0.1100 |  |
| Jogador 6 | 4-1 | 07:46:08 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 0 | Fumegante | DA_18_Zyra | -0.0300 |  |
| Jogador 6 | 4-1 | 07:46:08 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 0 | Fumegante | DA_18_Zyra | -0.1800 |  |
| Jogador 6 | 4-1 | 07:46:09 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 15 | 0 | Fumegante | DA_18_Zyra | 0.0000 |  |
| Jogador 6 | 4-1 | 07:46:09 | MOVE Board -> Board: Xayah (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 0 | Fumegante | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 4-1 | 07:46:10 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 15 | 0 | Fumegante | DA_18_Zyra | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-2 | 07:46:43 | VENDEU: Kobuko (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 23 | 1 | Fumegante | DA_18_Zyra | 0.0100 |  |
| Jogador 6 | 4-2 | 07:46:43 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 21 | 1 | Fumegante | DA_18_Zyra | 0.8600 |  |
| Jogador 6 | 4-2 | 07:46:44 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Fumegante | DA_18_Zyra | -0.0200 |  |
| Jogador 6 | 4-2 | 07:46:44 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Fumegante | DA_18_Zyra | 0.1200 |  |
| Jogador 6 | 4-2 | 07:46:45 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 18 | 1 | Fumegante | DA_18_Zyra | -0.1500 |  |
| Jogador 6 | 4-2 | 07:46:45 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 21 | 1 | Fumegante | DA_18_Zyra | 0.0400 |  |
| Jogador 6 | 4-2 | 07:46:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Fumegante | DA_18_Zyra | 0.3400 |  |
| Jogador 6 | 4-2 | 07:46:46 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Fumegante | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 4-2 | 07:46:47 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 21 | 1 | Fumegante | DA_18_Zyra | 0.0100 |  |
| Jogador 6 | 4-3 | 07:47:20 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Fumegante | DA_18_Zyra | 0.0600 |  |
| Jogador 6 | 4-3 | 07:47:20 | COMPROU: Varus (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 31 | 2 | Fumegante | DA_18_Zyra | 0.8800 |  |
| Jogador 6 | 4-3 | 07:47:21 | VENDEU: Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Fumegante | DA_18_Zyra | -0.0300 |  |
| Jogador 6 | 4-3 | 07:47:21 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Fumegante | DA_18_Zyra | 0.0000 |  |
| Jogador 6 | 4-3 | 07:47:22 | MOVE Board -> Board: Xayah (i:2.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Fumegante | DA_18_Zyra | 0.0000 |  |
| Jogador 6 | 4-3 | 07:47:22 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Fumegante | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 4-3 | 07:47:22 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Fumegante | DA_18_Zyra | -0.3900 |  |
| Jogador 6 | 4-4 | 07:47:58 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Fumegante | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 4-4 | 07:47:59 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Fumegante | DA_18_Zyra | 0.7500 |  |
| Jogador 6 | 4-4 | 07:47:59 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 3 | Fumegante | DA_18_Zyra | 0.0800 |  |
| Jogador 6 | 4-4 | 07:48:00 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Fumegante | DA_18_Zyra | 0.0200 |  |
| Jogador 6 | 4-4 | 07:48:00 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 33 | 3 | Fumegante | DA_18_Zyra | -0.0700 |  |
| Jogador 6 | 4-4 | 07:48:00 | VENDEU: Caitlyn (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Fumegante | DA_18_Zyra | -0.0600 |  |
| Jogador 6 | 4-4 | 07:48:01 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Fumegante | DA_18_Zyra | 0.8600 |  |
| Jogador 6 | 4-4 | 07:48:01 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 3 | Fumegante | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 4-4 | 07:48:02 | COMPROU: Alistar (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Fumegante | DA_18_Zyra | 0.0100 |  |
| Jogador 6 | 4-5 | 07:48:38 | VENDEU: Alistar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 45 | 3 | Fumegante | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 4-5 | 07:48:39 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Fumegante | DA_18_Zyra | 1.0100 |  |
| Jogador 6 | 4-5 | 07:48:40 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 39 | 3 | Fumegante | DA_18_Zyra | 0.3800 |  |
| Jogador 6 | 4-5 | 07:48:40 | MOVE Bench -> Board: Lillia (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 39 | 3 | Fumegante | DA_18_Zyra | 0.4000 |  |
| Jogador 6 | 4-5 | 07:48:41 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 36 | 3 | Fumegante | DA_18_Zyra | 0.2300 |  |
| Jogador 6 | 4-5 | 07:48:41 | VENDEU: Kayle (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Fumegante | DA_18_Zyra | -0.6200 |  |
| Jogador 6 | 4-5 | 07:48:42 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Fumegante | DA_18_Zyra | -0.2400 |  |
| Jogador 6 | 4-5 | 07:48:42 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Fumegante | DA_18_Zyra | 0.0900 |  |
| Jogador 6 | 4-5 | 07:48:43 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Fumegante | DA_18_Zyra | -0.2600 |  |
| Jogador 6 | 4-6 | 07:49:22 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 3 | Fumegante | DA_18_Zyra | 0.0900 |  |
| Jogador 6 | 4-6 | 07:49:22 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 47 | 3 | Fumegante | DA_18_Zyra | 0.1400 |  |
| Jogador 6 | 4-6 | 07:49:22 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 3 | Fumegante | DA_18_Zyra | 0.0500 |  |
| Jogador 6 | 4-6 | 07:49:23 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 48 | 3 | Fumegante | DA_18_Zyra | 0.0300 |  |
| Jogador 6 | 4-6 | 07:49:23 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 3 | Fumegante | DA_18_Zyra | 0.0700 |  |
| Jogador 6 | 4-6 | 07:49:24 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 48 | 3 | Fumegante | DA_18_Zyra | -0.0300 |  |
| Jogador 6 | 4-6 | 07:49:24 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 3 | Fumegante | DA_18_Zyra | 0.0800 |  |
| Jogador 6 | 4-6 | 07:49:25 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Fumegante | DA_18_Zyra | -0.2100 |  |
| Jogador 6 | 4-6 | 07:49:25 | MOVE Board -> Board: Lillia (i:8.0) <-> Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Fumegante | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 4-7 | 07:50:05 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 4 | Fumegante | DA_18_Zyra | 0.1000 |  |
| Jogador 6 | 4-7 | 07:50:06 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 4 | Fumegante | DA_18_Zyra | 0.1000 |  |
| Jogador 6 | 4-7 | 07:50:06 | VENDEU: Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Fumegante | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 4-7 | 07:50:07 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 4 | Fumegante | DA_18_Zyra | 1.0600 |  |
| Jogador 6 | 4-7 | 07:50:07 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 58 | 4 | Fumegante | DA_18_Zyra | 0.1800 |  |
| Jogador 6 | 4-7 | 07:50:07 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 55 | 4 | Fumegante | DA_18_Zyra | 0.0600 |  |
| Jogador 6 | 4-7 | 07:50:08 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 55 | 4 | Fumegante | DA_18_Zyra | 0.4000 |  |
| Jogador 6 | 4-7 | 07:50:09 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Fumegante | DA_18_Zyra | -0.1600 |  |
| Jogador 6 | 4-7 | 07:50:09 | VENDEU: Xayah (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 55 | 4 | Fumegante | DA_18_Zyra | -0.7100 |  |
| Jogador 7 | ? | 07:40:03 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 07:40:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 07:40:10 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 07:40:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 07:40:11 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-1 | 07:40:12 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-1 | 07:40:12 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 07:40:14 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 07:40:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 07:40:15 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 7 | 1-2 | 07:40:18 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 07:40:18 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 07:40:18 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 07:40:19 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 07:40:20 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 07:40:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 07:40:27 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-3 | 07:40:27 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 7 | 1-3 | 07:40:28 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 07:40:28 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2000 |  |
| Jogador 7 | 1-3 | 07:40:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 07:40:35 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8300 |  |
| Jogador 7 | 1-4 | 07:40:35 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-4 | 07:40:36 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-4 | 07:40:36 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 7 | 1-4 | 07:40:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 07:40:44 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 07:40:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-1 | 07:40:45 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 07:40:45 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 07:40:46 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 07:40:46 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-1 | 07:40:47 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | -0.6300 |  |
| Jogador 7 | 2-1 | 07:40:49 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 2-1 | 07:40:49 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.3200 |  |
| Jogador 7 | 2-2 | 07:40:57 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 1.0500 |  |
| Jogador 7 | 2-2 | 07:40:58 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.6800 |  |
| Jogador 7 | 2-2 | 07:40:58 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1400 |  |
| Jogador 7 | 2-2 | 07:40:59 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 07:40:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-3 | 07:41:12 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.3100 |  |
| Jogador 7 | 2-3 | 07:41:13 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 2-3 | 07:41:13 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Sentinel18 | -0.1300 |  |
| Jogador 7 | 2-3 | 07:41:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-3 | 07:41:15 | MOVE Board -> Board: Varus (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | -0.3200 |  |
| Jogador 7 | 2-3 | 07:41:15 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 2-3 | 07:41:16 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.2300 |  |
| Jogador 7 | 2-3 | 07:41:16 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | -0.1100 |  |
| Jogador 7 | 2-3 | 07:41:17 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 07:41:27 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.3200 |  |
| Jogador 7 | 2-4 | 07:41:28 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | 0.3300 |  |
| Jogador 7 | 2-4 | 07:41:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-4 | 07:41:29 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.4600 |  |
| Jogador 7 | 2-4 | 07:41:29 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 07:41:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 07:41:44 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 1.0100 |  |
| Jogador 7 | 2-5 | 07:41:45 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.9600 |  |
| Jogador 7 | 2-5 | 07:41:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 07:41:45 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.6200 |  |
| Jogador 7 | 2-5 | 07:41:46 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | -0.6300 |  |
| Jogador 7 | 2-5 | 07:41:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 2-5 | 07:41:48 | VENDEU: Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 2-5 | 07:41:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 2-5 | 07:41:49 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.6500 |  |
| Jogador 7 | 2-6 | 07:42:03 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.2900 |  |
| Jogador 7 | 2-6 | 07:42:04 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 2-6 | 07:42:04 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 7 | 2-6 | 07:42:05 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 2-6 | 07:42:05 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 7 | 2-6 | 07:42:06 | MOVE Board -> Board: Hecarim (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 7 | 2-6 | 07:42:06 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 2-6 | 07:42:07 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 2-6 | 07:42:08 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 2-7 | 07:42:24 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 7 | 2-7 | 07:42:24 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 7 | 2-7 | 07:42:25 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 7 | 2-7 | 07:42:25 | MOVE Board -> Board: Yorick (i:2.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 2-7 | 07:42:26 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 7 | 2-7 | 07:42:27 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 2-7 | 07:42:27 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 7 | 2-7 | 07:42:28 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 2-7 | 07:42:28 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_KogMaw18_AD | -0.3200 |  |
| Jogador 7 | 3-1 | 07:42:46 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 7 | 3-1 | 07:42:47 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 7 | 3-1 | 07:42:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Colosso | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 7 | 3-1 | 07:42:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 1 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-1 | 07:42:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 1 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-1 | 07:42:49 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 1 | Colosso | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 7 | 3-1 | 07:42:49 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 1 | Colosso | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 7 | 3-1 | 07:42:50 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 1 | Colosso | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 7 | 3-1 | 07:42:50 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 1 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 3-2 | 07:43:10 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 7 | 3-2 | 07:43:10 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 3-2 | 07:43:11 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Hecarim (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 7 | 3-2 | 07:43:11 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 7 | 3-2 | 07:43:12 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 7 | 3-2 | 07:43:13 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-2 | 07:43:14 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 7 | 3-2 | 07:43:14 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 7 | 3-2 | 07:43:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-3 | 07:43:35 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 7 | 3-3 | 07:43:35 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 7 | 3-3 | 07:43:36 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 7 | 3-3 | 07:43:36 | MOVE Bench -> Board: Kog'Maw (i:12.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 7 | 3-3 | 07:43:37 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 7 | 3-3 | 07:43:37 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 7 | 3-3 | 07:43:38 | MOVE Bench -> Board: Kog'Maw (i:12.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.4200 |  |
| Jogador 7 | 3-3 | 07:43:39 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 7 | 3-3 | 07:43:39 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 7 | 3-4 | 07:44:02 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.7800 |  |
| Jogador 7 | 3-4 | 07:44:03 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 7 | 3-4 | 07:44:03 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.6900 |  |
| Jogador 7 | 3-4 | 07:44:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 7 | 3-4 | 07:44:05 | MOVE Bench -> Board: Kog'Maw (i:12.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 7 | 3-4 | 07:44:05 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 7 | 3-4 | 07:44:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-5 | 07:44:31 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 7 | 3-5 | 07:44:32 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 3-5 | 07:44:32 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.1800 |  |
| Jogador 7 | 3-5 | 07:44:33 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-5 | 07:44:33 | MOVE Bench -> Board: Kog'Maw (i:12.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 7 | 3-5 | 07:44:34 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 3-5 | 07:44:34 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.7300 |  |
| Jogador 7 | 3-5 | 07:44:35 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-5 | 07:44:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-6 | 07:45:01 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.7300 |  |
| Jogador 7 | 3-6 | 07:45:02 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.7300 |  |
| Jogador 7 | 3-6 | 07:45:02 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 7 | 3-6 | 07:45:02 | MOVE Board -> Board: Azuporã (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-6 | 07:45:03 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 3-6 | 07:45:03 | MOVE Board -> Board: Hecarim (i:6.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-6 | 07:45:04 | MOVE Board -> Board: Azuporã (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-6 | 07:45:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-7 | 07:45:33 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 3-7 | 07:45:34 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 3-7 | 07:45:34 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-7 | 07:45:35 | MOVE Board -> Board: Grompe (i:4.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-7 | 07:45:35 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-1 | 07:46:07 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-1 | 07:46:08 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-1 | 07:46:08 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-2 | 07:46:43 | MOVE Board -> Board: Vi (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-2 | 07:46:43 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 4-2 | 07:46:44 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 4-3 | 07:47:20 | VENDEU: Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Colosso | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 7 | 4-3 | 07:47:20 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_KogMaw18_AD | 0.6500 |  |
| Jogador 7 | 4-3 | 07:47:21 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Varus (i:4.0) (tabuleiro slot 12) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 7 | 4-3 | 07:47:21 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Varus (i:4.0) (tabuleiro slot 12) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 7 | 4-3 | 07:47:22 | MOVE Board -> Board: Grompe (i:4.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 4-3 | 07:47:22 | MOVE Board -> Board: Azuporã (i:8.0) <-> Varus (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 7 | 4-3 | 07:47:22 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 4-3 | 07:47:23 | MOVE Board -> Board: Grompe (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 7 | 4-3 | 07:47:23 | MOVE Board -> Board: Vi (i:6.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-4 | 07:47:58 | MOVE Board -> Board: Azuporã (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-4 | 07:47:59 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 4-4 | 07:47:59 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Colosso | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 7 | 4-5 | 07:48:38 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 4 | Colosso | DA_Sentinel18 | -0.6000 |  |
| Jogador 7 | 4-5 | 07:48:39 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 4 | Colosso | DA_Sentinel18 | 0.3000 |  |
| Jogador 7 | 4-5 | 07:48:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 4-5 | 07:48:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 4 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 4-5 | 07:48:41 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 4-5 | 07:48:41 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 4 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 4-5 | 07:48:42 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 4 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 4-5 | 07:48:42 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 4 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 4-5 | 07:48:43 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 4 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 4-6 | 07:49:22 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 3 | Colosso | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 4-6 | 07:49:22 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Colosso | DA_Sentinel18 | 0.8100 |  |
| Jogador 7 | 4-6 | 07:49:22 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Colosso | DA_Sentinel18 | 0.7000 |  |
| Jogador 7 | 4-6 | 07:49:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 4-6 | 07:49:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_Sentinel18 | -0.1000 |  |
| Jogador 7 | 4-6 | 07:49:24 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 35 | 3 | Colosso | DA_Sentinel18 | 0.0600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 7 | 4-6 | 07:49:24 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 35 | 3 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 4-6 | 07:49:25 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 32 | 3 | Colosso | DA_Sentinel18 | 0.8400 |  |
| Jogador 7 | 4-6 | 07:49:25 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 32 | 3 | Colosso | DA_Sentinel18 | 0.3000 |  |
| Jogador 7 | 4-7 | 07:50:05 | COMPROU: Grompe (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 41 | 3 | Colosso | DA_Sentinel18 | 0.9100 |  |
| Jogador 7 | 4-7 | 07:50:06 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 41 | 3 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 4-7 | 07:50:06 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_RecurveBow -> Azuporã (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 41 | 3 | Colosso | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 4-7 | 07:50:07 | MOVE Bench -> Board: Grompe (i:8.0) <-> Kog'Maw (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 41 | 3 | Colosso | DA_Sentinel18 | 0.0800 |  |
| Jogador 7 | 4-7 | 07:50:07 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Hecarim (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 41 | 3 | Colosso | DA_Sentinel18 | -0.5100 |  |
| Jogador 7 | 4-7 | 07:50:07 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Grompe (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 41 | 3 | Colosso | DA_Sentinel18 | 0.1100 |  |
| Jogador 7 | 4-7 | 07:50:08 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 37 | 3 | Colosso | DA_Sentinel18 | -0.1000 |  |
| Jogador 7 | 4-7 | 07:50:09 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 33 | 3 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 4-7 | 07:50:09 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 29 | 3 | Colosso | DA_Sentinel18 | -0.1000 |  |
| Jogador 7 | 5-1 | 07:50:52 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 38 | 3 | Colosso | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 5-1 | 07:50:52 | COMPROU: Sivir (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 34 | 3 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-1 | 07:50:53 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 30 | 3 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-1 | 07:50:53 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 26 | 3 | Colosso | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 5-1 | 07:50:54 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 22 | 3 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-1 | 07:50:55 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 3 | Colosso | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 5-1 | 07:50:55 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 14 | 3 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-1 | 07:50:56 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 10 | 3 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-1 | 07:50:56 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 3 | Colosso | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 5-2 | 07:51:42 | VENDEU: Grompe (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 20 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 07:51:42 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 17 | 0 | Colosso | DA_Sentinel18 | 0.6100 |  |
| Jogador 7 | 5-2 | 07:51:43 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 13 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 07:51:43 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 9 | 0 | Colosso | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 5-2 | 07:51:44 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 07:51:44 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-2 | 07:51:44 | MOVE Board -> Board: Hecarim (i:12.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 07:51:45 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Sentinel18 | -0.2000 |  |
| Jogador 7 | 5-2 | 07:51:45 | COMPROU: Veigar (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-3 | 07:52:33 | VENDEU: Aronguejo (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 14 | 0 | Colosso | DA_Sentinel18 | -0.5000 |  |
| Jogador 7 | 5-3 | 07:52:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 11 | 0 | Colosso | DA_Sentinel18 | 0.8000 |  |
| Jogador 7 | 5-3 | 07:52:34 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 11 | 0 | Colosso | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 5-3 | 07:52:35 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 9 | 0 | Colosso | DA_Sentinel18 | 0.1800 |  |
| Jogador 7 | 5-3 | 07:52:35 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Veigar (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 9 | 0 | Colosso | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 5-3 | 07:52:35 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Colosso | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 5-3 | 07:52:36 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-3 | 07:52:36 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 5-3 | 07:52:37 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Hecarim (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-4 | 07:53:22 | COMPROU: Zyra (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Colosso | DA_Sentinel18 | 0.2400 |  |
| Jogador 7 | 5-4 | 07:53:22 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-4 | 07:53:23 | MOVE Board -> Board: Hecarim (i:12.0) <-> Vi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-4 | 07:53:23 | MOVE Board -> Board: Vi (i:6.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-4 | 07:53:24 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-5 | 07:54:12 | COMPROU: Morgana (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 5-5 | 07:54:13 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 5-5 | 07:54:13 | MOVE Board -> Board: Vi (i:6.0) <-> Aronguejo (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-5 | 07:54:14 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Hecarim (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-5 | 07:54:14 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-6 | 07:55:05 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 12 | 0 | Colosso | DA_Sentinel18 | 0.7800 |  |
| Jogador 7 | 5-6 | 07:55:05 | MOVE Board -> Board: Morgana (i:8.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 12 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-6 | 07:55:06 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 12 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-6 | 07:55:06 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 12 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-7 | 07:55:54 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Hecarim (i:12.0) (tabuleiro slot 24) | WINSTREAK | WINSTREAK: preservar vantagem atual | 21 | 1 | Colosso | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 5-7 | 07:55:54 | MOVE Board -> Board: Vi (i:6.0) <-> Aronguejo (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 21 | 1 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-7 | 07:55:54 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Azuporã (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 21 | 1 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-7 | 07:55:55 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 21 | 1 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-1 | 07:56:48 | MOVE Board -> Board: Azuporã (i:8.0) <-> Varus (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 32 | 2 | Colosso | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 6-1 | 07:56:48 | MOVE Board -> Board: Varus (i:4.0) <-> Hecarim (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 32 | 2 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-1 | 07:56:48 | MOVE Board -> Board: Hecarim (i:12.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 32 | 2 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-1 | 07:56:49 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 32 | 2 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-2 | 07:57:42 | MOVE Board -> Board: Varus (i:4.0) <-> Aronguejo (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 44 | 3 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-2 | 07:57:43 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 44 | 3 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-2 | 07:57:43 | MOVE Board -> Board: Vi (i:6.0) <-> Morgana (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 44 | 3 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-2 | 07:57:44 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 44 | 3 | Colosso | DA_Sentinel18 | -0.1900 |  |
| Jogador 7 | 6-3 | 07:58:42 | MOVE Board -> Board: Morgana (i:8.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 57 | 4 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-3 | 07:58:42 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Azuporã (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 57 | 4 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-3 | 07:58:42 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 57 | 4 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 6-4 | 07:59:43 | VENDEU: Kog'Maw (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 78 | 5 | Colosso | DA_Sentinel18 | -0.6000 |  |
| Jogador 7 | 6-4 | 07:59:44 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 75 | 5 | Colosso | DA_Sentinel18 | 0.9000 |  |
| Jogador 7 | 6-4 | 07:59:44 | MOVE Board -> Board: Azuporã (i:8.0) <-> Hecarim (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 75 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-4 | 07:59:45 | MOVE Board -> Board: Hecarim (i:12.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 75 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-4 | 07:59:45 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 75 | 5 | Colosso | DA_Sentinel18 | -0.2300 |  |
| Jogador 7 | 6-5 | 08:00:45 | MOVE Board -> Board: Azuporã (i:8.0) <-> Varus (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 89 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-5 | 08:00:46 | MOVE Board -> Board: Varus (i:4.0) <-> Vi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 89 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 6-5 | 08:00:46 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 89 | 5 | Colosso | DA_Sentinel18 | -0.2400 |  |
| Jogador 8 | ? | 07:40:03 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | ? | 07:40:05 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | ? | 07:40:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 07:40:10 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 07:40:11 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-1 | 07:40:11 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-1 | 07:40:12 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3600 |  |
| Jogador 8 | 1-1 | 07:40:12 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-1 | 07:40:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 07:40:15 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5000 |  |
| Jogador 8 | 1-2 | 07:40:18 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 8 | 1-2 | 07:40:18 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 8 | 1-2 | 07:40:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 07:40:27 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-3 | 07:40:27 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 8 | 1-3 | 07:40:28 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1700 |  |
| Jogador 8 | 1-3 | 07:40:28 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 8 | 1-3 | 07:40:29 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 8 | 1-3 | 07:40:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 07:40:35 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.1100 |  |
| Jogador 8 | 1-4 | 07:40:35 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 1-4 | 07:40:36 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 1-4 | 07:40:36 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 1-4 | 07:40:37 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 1.1000 |  |
| Jogador 8 | 1-4 | 07:40:37 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 1-4 | 07:40:38 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 1-4 | 07:40:38 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.3200 |  |
| Jogador 8 | 2-1 | 07:40:44 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-1 | 07:40:45 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.3000 |  |
| Jogador 8 | 2-1 | 07:40:45 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1900 |  |
| Jogador 8 | 2-1 | 07:40:45 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | -0.2100 |  |
| Jogador 8 | 2-1 | 07:40:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-1 | 07:40:46 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-1 | 07:40:47 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-1 | 07:40:49 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.1700 |  |
| Jogador 8 | 2-1 | 07:40:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-2 | 07:40:57 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | 0.9900 |  |
| Jogador 8 | 2-2 | 07:40:58 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.3600 |  |
| Jogador 8 | 2-2 | 07:40:58 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | -0.0700 |  |
| Jogador 8 | 2-2 | 07:40:59 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 2-2 | 07:40:59 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Karma18 | -0.1300 |  |
| Jogador 8 | 2-2 | 07:41:00 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2500 |  |
| Jogador 8 | 2-2 | 07:41:00 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | -0.1500 |  |
| Jogador 8 | 2-2 | 07:41:01 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Karma18 | -0.3300 |  |
| Jogador 8 | 2-2 | 07:41:01 | MOVE Bench -> Board: Veigar (i:2.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 2-3 | 07:41:12 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 2-3 | 07:41:13 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | — | DA_Karma18 | 0.2100 |  |
| Jogador 8 | 2-3 | 07:41:13 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | — | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-3 | 07:41:14 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | — | DA_Karma18 | 0.3500 |  |
| Jogador 8 | 2-3 | 07:41:15 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | — | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-3 | 07:41:15 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | — | DA_Karma18 | -0.0700 |  |
| Jogador 8 | 2-3 | 07:41:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 1 | — | DA_Karma18 | -0.1200 |  |
| Jogador 8 | 2-3 | 07:41:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | — | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-3 | 07:41:17 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 1 | — | DA_18_MasterYi_AD | -0.6300 |  |
| Jogador 8 | 2-4 | 07:41:27 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 1.0300 |  |
| Jogador 8 | 2-4 | 07:41:28 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 8 | 2-4 | 07:41:28 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.3200 |  |
| Jogador 8 | 2-4 | 07:41:29 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 8 | 2-4 | 07:41:29 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.4300 |  |
| Jogador 8 | 2-4 | 07:41:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 8 | 2-4 | 07:41:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 8 | 2-4 | 07:41:31 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.3800 |  |
| Jogador 8 | 2-4 | 07:41:31 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.1200 |  |
| Jogador 8 | 2-5 | 07:41:44 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.2500 |  |
| Jogador 8 | 2-5 | 07:41:45 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.4800 |  |
| Jogador 8 | 2-5 | 07:41:45 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 8 | 2-5 | 07:41:45 | MOVE Board -> Board: Diana (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.2000 |  |
| Jogador 8 | 2-5 | 07:41:46 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 8 | 2-5 | 07:41:47 | MOVE Bench -> Board: Soraka (i:8.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.2600 |  |
| Jogador 8 | 2-5 | 07:41:48 | MOVE Board -> Board: Rakan (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 8 | 2-5 | 07:41:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 8 | 2-6 | 07:42:03 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.3400 |  |
| Jogador 8 | 2-6 | 07:42:04 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.2900 |  |
| Jogador 8 | 2-6 | 07:42:04 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.1800 |  |
| Jogador 8 | 2-6 | 07:42:05 | MOVE Board -> Board: Diana (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 8 | 2-6 | 07:42:05 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 8 | 2-6 | 07:42:06 | MOVE Board -> Board: Soraka (i:8.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 8 | 2-6 | 07:42:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 8 | 2-7 | 07:42:24 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 8 | 2-7 | 07:42:24 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_SparringGloves -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.1700 |  |
| Jogador 8 | 2-7 | 07:42:25 | MOVE Board -> Board: Diana (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 8 | 2-7 | 07:42:25 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0600 |  |
| Jogador 8 | 2-7 | 07:42:26 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0700 |  |
| Jogador 8 | 2-7 | 07:42:27 | MOVE Board -> Board: Teemo (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0200 |  |
| Jogador 8 | 2-7 | 07:42:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 8 | 2-7 | 07:42:28 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 8 | 2-7 | 07:42:28 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0800 |  |
| Jogador 8 | 3-1 | 07:42:46 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.1700 |  |
| Jogador 8 | 3-1 | 07:42:47 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 8 | 3-1 | 07:42:47 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0600 |  |
| Jogador 8 | 3-1 | 07:42:48 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.1000 |  |
| Jogador 8 | 3-1 | 07:42:48 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0700 |  |
| Jogador 8 | 3-1 | 07:42:49 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.3800 |  |
| Jogador 8 | 3-1 | 07:42:49 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.3000 |  |
| Jogador 8 | 3-1 | 07:42:50 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.2200 |  |
| Jogador 8 | 3-1 | 07:42:50 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Enfeitiçador | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 8 | 3-2 | 07:43:10 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_MasterYi_AD | 0.3100 |  |
| Jogador 8 | 3-2 | 07:43:10 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Enfeitiçador | DA_18_MasterYi_AD | 0.2500 |  |
| Jogador 8 | 3-2 | 07:43:11 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Enfeitiçador | DA_18_MasterYi_AD | 0.2200 |  |
| Jogador 8 | 3-2 | 07:43:11 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Enfeitiçador | DA_18_MasterYi_AD | -0.4300 |  |
| Jogador 8 | 3-2 | 07:43:12 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_MasterYi_AD | -0.3800 |  |
| Jogador 8 | 3-2 | 07:43:13 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 8 | 3-2 | 07:43:14 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_MasterYi_AD | -0.3700 |  |
| Jogador 8 | 3-2 | 07:43:14 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_18_MasterYi_AD | -0.6300 |  |
| Jogador 8 | 3-2 | 07:43:15 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_18_MasterYi_AD | -0.4600 |  |
| Jogador 8 | 3-3 | 07:43:35 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Enfeitiçador | DA_18_MasterYi_AD | 0.8900 |  |
| Jogador 8 | 3-3 | 07:43:35 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Enfeitiçador | DA_18_MasterYi_AD | 0.1400 |  |
| Jogador 8 | 3-3 | 07:43:36 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Enfeitiçador | DA_18_MasterYi_AD | -0.1900 |  |
| Jogador 8 | 3-3 | 07:43:36 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 3 | Enfeitiçador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 8 | 3-3 | 07:43:37 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 3 | Enfeitiçador | DA_18_MasterYi_AD | 0.5600 |  |
| Jogador 8 | 3-3 | 07:43:37 | MOVE Board -> Board: Veigar (i:2.0) <-> Soraka (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 3 | Enfeitiçador | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 8 | 3-3 | 07:43:38 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Enfeitiçador | DA_18_MasterYi_AD | -0.6300 |  |
| Jogador 8 | 3-3 | 07:43:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 3 | Enfeitiçador | DA_18_MasterYi_AD | -0.0700 |  |
| Jogador 8 | 3-3 | 07:43:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 3 | Enfeitiçador | DA_18_MasterYi_AD | 0.0100 |  |
| Jogador 8 | 3-4 | 07:44:02 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_MasterYi_AD | 0.3200 |  |
| Jogador 8 | 3-4 | 07:44:03 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_18_MasterYi_AD | 0.7500 |  |
| Jogador 8 | 3-4 | 07:44:03 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_MasterYi_AD | 0.2800 |  |
| Jogador 8 | 3-4 | 07:44:04 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 8 | 3-4 | 07:44:05 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Enfeitiçador | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 8 | 3-4 | 07:44:05 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 8 | 3-4 | 07:44:06 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_18_MasterYi_AD | -0.4000 |  |
| Jogador 8 | 3-4 | 07:44:06 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_18_MasterYi_AD | -0.1300 |  |
| Jogador 8 | 3-4 | 07:44:07 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Enfeitiçador | DA_18_MasterYi_AD | -0.4900 |  |
| Jogador 8 | 3-5 | 07:44:31 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Enfeitiçador | DA_18_LeBlanc | 0.9000 |  |
| Jogador 8 | 3-5 | 07:44:32 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Enfeitiçador | DA_18_LeBlanc | 0.2600 |  |
| Jogador 8 | 3-5 | 07:44:32 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Enfeitiçador | DA_18_LeBlanc | 0.3000 |  |
| Jogador 8 | 3-5 | 07:44:33 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Enfeitiçador | DA_18_Soraka | -0.5500 |  |
| Jogador 8 | 3-5 | 07:44:33 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Enfeitiçador | DA_18_Soraka | 0.0900 |  |
| Jogador 8 | 3-5 | 07:44:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 3 | Enfeitiçador | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 3-5 | 07:44:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 3 | Enfeitiçador | DA_18_Soraka | -0.0800 |  |
| Jogador 8 | 3-5 | 07:44:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 3 | Enfeitiçador | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 3-5 | 07:44:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 3 | Enfeitiçador | DA_18_Soraka | 0.1100 |  |
| Jogador 8 | 3-6 | 07:45:01 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_Soraka | 0.2500 |  |
| Jogador 8 | 3-6 | 07:45:02 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Enfeitiçador | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 3-6 | 07:45:02 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Enfeitiçador | DA_18_Soraka | 0.0700 |  |
| Jogador 8 | 3-6 | 07:45:02 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Enfeitiçador | DA_18_Soraka | -0.3700 |  |
| Jogador 8 | 3-6 | 07:45:03 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Soraka | -0.0500 |  |
| Jogador 8 | 3-6 | 07:45:03 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_18_Soraka | -0.3400 |  |
| Jogador 8 | 3-6 | 07:45:04 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_18_Soraka | 0.4200 |  |
| Jogador 8 | 3-6 | 07:45:05 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Soraka | -0.2400 |  |
| Jogador 8 | 3-6 | 07:45:05 | MOVE Board -> Board: Azir (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 3-7 | 07:45:33 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_18_Soraka | 0.9400 |  |
| Jogador 8 | 3-7 | 07:45:34 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_18_Soraka | 0.7400 |  |
| Jogador 8 | 3-7 | 07:45:34 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_18_Soraka | 0.1600 |  |
| Jogador 8 | 3-7 | 07:45:35 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_18_Soraka | 0.1800 |  |
| Jogador 8 | 3-7 | 07:45:35 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_Soraka | 0.5900 |  |
| Jogador 8 | 3-7 | 07:45:36 | MOVE Bench -> Board: Diana (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_Soraka | 0.0900 |  |
| Jogador 8 | 3-7 | 07:45:37 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Enfeitiçador | DA_18_Soraka | 0.3900 |  |
| Jogador 8 | 3-7 | 07:45:37 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Enfeitiçador | DA_18_Soraka | 0.1400 |  |
| Jogador 8 | 3-7 | 07:45:38 | MOVE Board -> Board: Master Yi (i:6.0) <-> Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Enfeitiçador | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 4-1 | 07:46:07 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Enfeitiçador | DA_18_Soraka | -0.0600 |  |
| Jogador 8 | 4-1 | 07:46:08 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Enfeitiçador | DA_18_Soraka | 0.0600 |  |
| Jogador 8 | 4-1 | 07:46:08 | MOVE Board -> Board: Azir (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Enfeitiçador | DA_18_Soraka | 0.0200 |  |
| Jogador 8 | 4-1 | 07:46:09 | MOVE Board -> Board: Diana (i:6.0) <-> Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Enfeitiçador | DA_18_Soraka | -0.0300 |  |
| Jogador 8 | 4-1 | 07:46:09 | MOVE Board -> Board: Teemo (i:4.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Enfeitiçador | DA_18_Soraka | -0.0200 |  |
| Jogador 8 | 4-1 | 07:46:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Enfeitiçador | DA_18_Soraka | -0.0300 |  |
| Jogador 8 | 4-2 | 07:46:43 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Enfeitiçador | DA_18_Soraka | -0.5800 |  |
| Jogador 8 | 4-2 | 07:46:43 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Enfeitiçador | DA_18_Diana | 0.8900 |  |
| Jogador 8 | 4-2 | 07:46:44 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Enfeitiçador | DA_18_Diana | 0.2100 |  |
| Jogador 8 | 4-2 | 07:46:44 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 31 | 2 | Enfeitiçador | DA_18_Diana | 0.8300 |  |
| Jogador 8 | 4-2 | 07:46:45 | VENDEU: Diana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 2 | Enfeitiçador | DA_18_Soraka | -0.5700 |  |
| Jogador 8 | 4-2 | 07:46:45 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Rakan (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 39 | 2 | Enfeitiçador | DA_18_Soraka | 0.1300 |  |
| Jogador 8 | 4-2 | 07:46:46 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Enfeitiçador | DA_18_Soraka | 0.3100 |  |
| Jogador 8 | 4-2 | 07:46:46 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Enfeitiçador | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 4-2 | 07:46:47 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Enfeitiçador | DA_18_Soraka | -0.0900 |  |
| Jogador 8 | 4-3 | 07:47:20 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 2 | Enfeitiçador | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 4-3 | 07:47:20 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Enfeitiçador | DA_18_Soraka | 0.8500 |  |
| Jogador 8 | 4-3 | 07:47:21 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 2 | Enfeitiçador | DA_18_Soraka | 0.0300 |  |
| Jogador 8 | 4-3 | 07:47:21 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Enfeitiçador | DA_18_Soraka | 0.8300 |  |
| Jogador 8 | 4-3 | 07:47:22 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 40 | 2 | Enfeitiçador | DA_18_Soraka | 0.0700 |  |
| Jogador 8 | 4-3 | 07:47:22 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 2 | Enfeitiçador | DA_18_Soraka | 0.8400 |  |
| Jogador 8 | 4-3 | 07:47:22 | MOVE Board -> Board: Tristana (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 2 | Enfeitiçador | DA_18_Soraka | -0.2200 |  |
| Jogador 8 | 4-3 | 07:47:23 | MOVE Board -> Board: Master Yi (i:6.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 2 | Enfeitiçador | DA_18_Soraka | 0.1200 |  |
| Jogador 8 | 4-3 | 07:47:23 | MOVE Board -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 38 | 2 | Enfeitiçador | DA_18_Soraka | 0.0300 |  |
| Jogador 8 | 4-4 | 07:47:58 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Enfeitiçador | DA_18_Soraka | 0.7800 |  |
| Jogador 8 | 4-4 | 07:47:59 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Enfeitiçador | DA_18_Soraka | 0.8400 |  |
| Jogador 8 | 4-4 | 07:47:59 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 3 | Enfeitiçador | DA_18_Soraka | -0.5800 |  |
| Jogador 8 | 4-4 | 07:48:00 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Enfeitiçador | DA_18_Soraka | 0.9200 |  |
| Jogador 8 | 4-4 | 07:48:00 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Enfeitiçador | DA_18_Soraka | 0.2500 |  |
| Jogador 8 | 4-4 | 07:48:00 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Enfeitiçador | DA_18_Soraka | -0.2500 |  |
| Jogador 8 | 4-4 | 07:48:01 | MOVE Board -> Board: Tristana (i:6.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Enfeitiçador | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 4-4 | 07:48:01 | MOVE Board -> Board: Azir (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Enfeitiçador | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 4-4 | 07:48:02 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Enfeitiçador | DA_18_Soraka | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 4-5 | 07:48:38 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.9600 |  |
| Jogador 8 | 4-5 | 07:48:39 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.7000 |  |
| Jogador 8 | 4-5 | 07:48:40 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 8 | 4-5 | 07:48:40 | VENDEU: Teemo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Enfeitiçador | DA_Fiddlesticks18 | -0.5000 |  |
| Jogador 8 | 4-5 | 07:48:41 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.4600 |  |
| Jogador 8 | 4-5 | 07:48:41 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 44 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 8 | 4-5 | 07:48:42 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 40 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 8 | 4-5 | 07:48:42 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 40 | 4 | Enfeitiçador | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 4-5 | 07:48:43 | MOVE Bench -> Board: Fiddlesticks (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 40 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.6300 |  |
| Jogador 8 | 4-6 | 07:49:22 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 47 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.8700 |  |
| Jogador 8 | 4-6 | 07:49:22 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 4 | Enfeitiçador | DA_Fiddlesticks18 | -0.1300 |  |
| Jogador 8 | 4-6 | 07:49:22 | VENDEU: Master Yi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 8 | 4-6 | 07:49:23 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 4 | Enfeitiçador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 8 | 4-6 | 07:49:23 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 8 | 4-6 | 07:49:24 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 8 | 4-6 | 07:49:24 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 8 | 4-6 | 07:49:25 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 48 | 4 | Enfeitiçador | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 8 | 4-6 | 07:49:25 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Enfeitiçador | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 8 | 4-7 | 07:50:05 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.5500 |  |
| Jogador 8 | 4-7 | 07:50:06 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 8 | 4-7 | 07:50:06 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NegatronCloak -> Fiddlesticks (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 8 | 4-7 | 07:50:07 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 8 | 4-7 | 07:50:07 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.2200 |  |
| Jogador 8 | 4-7 | 07:50:07 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 8 | 4-7 | 07:50:08 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.2000 |  |
| Jogador 8 | 4-7 | 07:50:09 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.4600 |  |
| Jogador 8 | 4-7 | 07:50:09 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 8 | 5-1 | 07:50:52 | VENDEU: Ornn (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 8 | 5-1 | 07:50:52 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.9600 |  |
| Jogador 8 | 5-1 | 07:50:53 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.4300 |  |
| Jogador 8 | 5-1 | 07:50:53 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.1700 |  |
| Jogador 8 | 5-1 | 07:50:54 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Fiddlesticks (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.2500 |  |
| Jogador 8 | 5-1 | 07:50:55 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.2600 |  |
| Jogador 8 | 5-1 | 07:50:55 | MOVE Board -> Board: Azir (i:6.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 8 | 5-1 | 07:50:56 | MOVE Board -> Board: Tristana (i:6.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 8 | 5-1 | 07:50:56 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.5100 |  |
| Jogador 8 | 5-2 | 07:51:42 | VENDEU: Hecarim (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 8 | 5-2 | 07:51:42 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 1.1000 |  |
| Jogador 8 | 5-2 | 07:51:43 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 8 | 5-2 | 07:51:43 | VENDEU: Cassiopeia (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 8 | 5-2 | 07:51:44 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 8 | 5-2 | 07:51:44 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 8 | 5-2 | 07:51:44 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 5-2 | 07:51:45 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 8 | 5-2 | 07:51:45 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 1.1000 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 37 | 37 | 185 | 37 | 17 | 269 | 8 | 26 |
| Jogador 2 | 21 | 22 | 110 | 21 | 12 | 167 | 5 | 16 |
| Jogador 3 | 24 | 26 | 130 | 24 | 15 | 164 | 3 | 21 |
| Jogador 4 | 26 | 33 | 165 | 26 | 16 | 194 | 10 | 19 |
| Jogador 5 | 38 | 38 | 190 | 38 | 17 | 296 | 16 | 48 |
| Jogador 6 | 26 | 28 | 140 | 26 | 17 | 188 | 17 | 32 |
| Jogador 7 | 38 | 38 | 190 | 38 | 18 | 247 | 6 | 68 |
| Jogador 8 | 28 | 30 | 150 | 28 | 16 | 228 | 9 | 33 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 269 | 269 | 269 | 0 | 261 | 0 | 269 | 269 | 269 | 89/74 |
| Jogador 2 | 167 | 167 | 167 | 0 | 159 | 0 | 167 | 167 | 167 | 74/61 |
| Jogador 3 | 164 | 164 | 164 | 0 | 159 | 0 | 164 | 164 | 164 | 63/50 |
| Jogador 4 | 194 | 194 | 194 | 0 | 184 | 0 | 194 | 194 | 194 | 59/44 |
| Jogador 5 | 296 | 296 | 296 | 0 | 285 | 0 | 296 | 296 | 296 | 110/95 |
| Jogador 6 | 188 | 188 | 188 | 0 | 178 | 0 | 188 | 188 | 188 | 68/54 |
| Jogador 7 | 247 | 247 | 247 | 0 | 234 | 0 | 247 | 247 | 247 | 58/41 |
| Jogador 8 | 228 | 228 | 228 | 0 | 220 | 0 | 228 | 228 | 228 | 91/79 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.20922301709651947 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.25060486793518066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23841141164302826 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22248587012290955 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013312771916389465 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42622989416122437 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3469875156879425 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25063249468803406 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 31 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0387866497039795 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.031377911567688 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 53 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9796043038368225 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19132192432880402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17696425318717957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 56 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 57 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3357411324977875 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 63 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.129820317029953 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 2-2 | 64 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06030553579330444 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2756745219230652 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00807955488562584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 68 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1726420670747757 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 2-2 | 69 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3274238407611847 | 0.0 | 0.0 | +e76c0caf-1c3d-493f-9a21-659dd8587fc2 / -— |
| Jogador 1 | 2-2 | 70 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3528043329715729 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 74 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33444297313690186 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 75 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17819413542747498 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 1 | 2-3 | 76 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1511172354221344 | 0.0 | 0.0 | +— / -e76c0caf-1c3d-493f-9a21-659dd8587fc2 |
| Jogador 1 | 2-3 | 77 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 78 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1169861555099487 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-4 | 83 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36417505145072937 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42867907881736755 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 85 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19476816058158875 | 0.0 | 0.0 | +7d8f4f6b-4eba-4c31-9834-bd81a3765520 / -— |
| Jogador 1 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002366695087403059 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 87 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09324062615633011 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 88 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01360281277447939 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 89 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014595994725823402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015672916546463966 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9662520289421082 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 93 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05416328087449074 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 94 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 1 | 2-5 | 95 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00031991899595595896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 97 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04899999871850014 | 0.0 | 0.0 | +— / -7d8f4f6b-4eba-4c31-9834-bd81a3765520 |
| Jogador 1 | 2-5 | 98 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5041335821151733 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 100 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014980697073042393 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 102 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.117992639541626 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 103 | BUY | STABILIZE | 100.0 | 6 | 6 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28147950768470764 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 104 | BUY | STABILIZE | 100.0 | 6 | 3 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28170570731163025 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 105 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.400149405002594 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01498666126281023 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 108 | PASS | STABILIZE | 100.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 112 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0476200580596924 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-7 | 113 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9422693252563477 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 5 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34344515204429626 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 115 | BUY | STABILIZE | 100.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05106889083981514 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 1 | 2-7 | 116 | BUY | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01850918121635914 | 0.0 | 0.0 | +acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce / -— |
| Jogador 1 | 2-7 | 117 | BUY | STABILIZE | 100.0 | 6 | 2 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2731601595878601 | 0.0 | 0.0 | +07130d94-c79f-4052-b3e9-7f867421f01b / -— |
| Jogador 1 | 2-7 | 118 | SELL | STABILIZE | 100.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -af132466-c7bd-40ad-9848-b79d59a5915c |
| Jogador 1 | 2-7 | 119 | PASS | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 122 | BUY | STABILIZE | 100.0 | 6 | 10 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.119765505194664 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 1 | 3-1 | 123 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.01913905143737793 | 0.0 | 0.0 | +dca8bf82-80ac-4054-9a77-3891a7de23e2 / -— |
| Jogador 1 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1675085723400116 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 125 | BUY | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05406203866004944 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 126 | PASS | STABILIZE | 100.0 | 6 | 3 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 132 | SELL | STABILIZE | 100.0 | 6 | 12 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024117255583405495 | 0.0 | 0.0 | +— / -acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce |
| Jogador 1 | 3-2 | 133 | BUY | STABILIZE | 100.0 | 6 | 13 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24248795211315155 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 1 | 3-2 | 134 | BUY_XP | STABILIZE | 100.0 | 6 | 10 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 135 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 136 | SELL | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -07130d94-c79f-4052-b3e9-7f867421f01b |
| Jogador 1 | 3-2 | 137 | BUY | STABILIZE | 100.0 | 6 | 4 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057275593280792236 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 138 | SELL | STABILIZE | 100.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -dca8bf82-80ac-4054-9a77-3891a7de23e2 |
| Jogador 1 | 3-2 | 139 | BUY | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10428836941719055 | 0.0 | 0.0 | +1e504283-c5d1-4eb3-915e-20533ec3a756 / -— |
| Jogador 1 | 3-2 | 140 | SELL | STABILIZE | 100.0 | 6 | 1 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02414027228951454 | 0.0 | 0.0 | +— / -1e504283-c5d1-4eb3-915e-20533ec3a756 |
| Jogador 1 | 3-3 | 142 | BUY | STABILIZE | 100.0 | 6 | 11 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050307098776102066 | 0.0 | 0.0 | +e6ee6b15-d413-4678-8ffb-29272199a53d / -— |
| Jogador 1 | 3-3 | 143 | BUY_XP | STABILIZE | 100.0 | 6 | 8 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 144 | BUY_XP | STABILIZE | 100.0 | 6 | 4 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 145 | SELL | STABILIZE | 100.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -15893185-b1a5-4725-9e46-964e149ec287 |
| Jogador 1 | 3-3 | 146 | BUY | STABILIZE | 100.0 | 6 | 3 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09809727221727371 | 0.0 | 0.0 | +66b5ed5e-7fdf-4135-a334-e693715e302d / -— |
| Jogador 1 | 3-3 | 147 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7138770818710327 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 148 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059529200196266174 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 149 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08488105237483978 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 150 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.728053629398346 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 152 | BUY_XP | STABILIZE | 100.0 | 6 | 10 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 153 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06353499740362167 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 2 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5974194407463074 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 155 | BUY | STABILIZE | 100.0 | 7 | 2 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12341626733541489 | 0.0 | 0.0 | +7a60e1b2-fc20-4070-b163-2f9fb6f93264 / -— |
| Jogador 1 | 3-4 | 156 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 158 | PASS | STABILIZE | 100.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 162 | SELL | STABILIZE | 100.0 | 7 | 9 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05450671166181564 | 0.0 | 0.0 | +— / -7a60e1b2-fc20-4070-b163-2f9fb6f93264 |
| Jogador 1 | 3-5 | 163 | BUY | STABILIZE | 100.0 | 7 | 10 | 1 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7558178305625916 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09985638409852982 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 165 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 8 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1359972208738327 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 166 | BUY | STABILIZE | 100.0 | 7 | 8 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04591652750968933 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 1 | 3-5 | 167 | BUY_XP | STABILIZE | 100.0 | 7 | 5 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.78405388801184e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 169 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3860282003879547 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 170 | BUY | FAST8 | 100.0 | 7 | 1 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08000429719686508 | 0.0 | 0.0 | +a9184317-58b7-4804-9aef-3e2c08c20935 / -— |
| Jogador 1 | 3-6 | 172 | SELL | FAST8 | 100.0 | 7 | 9 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08596666902303696 | 0.0 | 0.0 | +— / -a9184317-58b7-4804-9aef-3e2c08c20935 |
| Jogador 1 | 3-6 | 173 | BUY | FAST8 | 100.0 | 7 | 10 | 1 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6570901274681091 | 0.0 | 0.0 | +600071dd-5c17-4f03-903f-d1cd6c20bb28 / -— |
| Jogador 1 | 3-6 | 174 | MOVE_BOARD | FAST8 | 100.0 | 7 | 9 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 175 | MOVE_BOARD | FAST8 | 100.0 | 7 | 9 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 176 | PASS | FAST8 | 100.0 | 7 | 9 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 182 | SELL | FAST8 | 100.0 | 7 | 19 | 1 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05312823876738548 | 0.0 | 0.0 | +— / -8e819ba6-a356-4d9b-a8c9-7493332900fb |
| Jogador 1 | 3-7 | 183 | BUY | FAST8 | 100.0 | 7 | 21 | 2 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6627744436264038 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 1 | 3-7 | 184 | SELL | FAST8 | 100.0 | 7 | 18 | 1 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08918855339288712 | 0.0 | 0.0 | +— / -7c218f01-e884-46da-8a1a-2d2db27a5ff1 |
| Jogador 1 | 3-7 | 185 | BUY | FAST8 | 100.0 | 7 | 21 | 2 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1380200833082199 | 0.0 | 0.0 | +c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 / -— |
| Jogador 1 | 3-7 | 186 | MOVE_BOARD | FAST8 | 100.0 | 7 | 18 | 1 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 187 | MOVE_BOARD | FAST8 | 100.0 | 7 | 18 | 1 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 188 | PASS | FAST8 | 100.0 | 7 | 18 | 1 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 100.0 | 7 | 27 | 2 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13875418901443481 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 100.0 | 7 | 27 | 2 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07261498272418976 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 194 | SELL | FAST8 | 100.0 | 7 | 27 | 2 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04696805775165558 | 0.0 | 0.0 | +— / -66b5ed5e-7fdf-4135-a334-e693715e302d |
| Jogador 1 | 4-1 | 195 | BUY | FAST8 | 100.0 | 7 | 29 | 2 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46080532670021057 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 1 | 4-1 | 196 | SELL | FAST8 | 100.0 | 7 | 26 | 2 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0636231079697609 | 0.0 | 0.0 | +— / -9fe58106-e0c4-4ecc-b152-13c8c0eb564e |
| Jogador 1 | 4-1 | 197 | BUY | FAST8 | 100.0 | 7 | 29 | 2 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005757293198257685 | 0.0 | 0.0 | +75d9034d-80ed-40d3-a330-44554cc2bb9e / -— |
| Jogador 1 | 4-1 | 198 | MOVE_BOARD | FAST8 | 100.0 | 7 | 26 | 2 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.779320299050596e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 199 | MOVE_BOARD | FAST8 | 100.0 | 7 | 26 | 2 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000042505562305 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 200 | MOVE_BOARD | FAST8 | 100.0 | 7 | 26 | 2 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015161956660449505 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 202 | SELL | FAST8 | 100.0 | 7 | 37 | 3 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06460729241371155 | 0.0 | 0.0 | +— / -75d9034d-80ed-40d3-a330-44554cc2bb9e |
| Jogador 1 | 4-2 | 203 | BUY | FAST8 | 100.0 | 7 | 40 | 4 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.208457350730896 | 0.0 | 0.0 | +6fa83356-562b-4a26-a77d-3e989089e70a / -— |
| Jogador 1 | 4-2 | 204 | MOVE_BOARD | FAST8 | 100.0 | 7 | 39 | 3 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00016244534344878048 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 205 | MOVE_BOARD | FAST8 | 100.0 | 7 | 39 | 3 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999630860984325 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 206 | MOVE_BOARD | FAST8 | 100.0 | 7 | 39 | 3 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 207 | PASS | FAST8 | 100.0 | 7 | 39 | 3 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04214285686612129 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 212 | MOVE_BOARD | FAST8 | 100.0 | 7 | 52 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017790694255381823 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 213 | MOVE_BOARD | FAST8 | 100.0 | 7 | 52 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013220981694757938 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 214 | PASS | FAST8 | 100.0 | 7 | 52 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08101436495780945 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 222 | SELL | FAST8 | 100.0 | 7 | 66 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -145f7470-8c0f-4957-b8d6-97939ddaeba1 |
| Jogador 1 | 4-4 | 223 | BUY | FAST8 | 100.0 | 7 | 70 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7989487648010254 | 0.0 | 0.0 | +e4764e13-e26d-4358-980a-c7c625e26726 / -— |
| Jogador 1 | 4-4 | 224 | MOVE_BOARD | FAST8 | 100.0 | 7 | 67 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.573697782144336e-08 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 225 | MOVE_BOARD | FAST8 | 100.0 | 7 | 67 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 226 | PASS | FAST8 | 100.0 | 7 | 67 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0906796008348465 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 232 | SELL | FAST8 | 100.0 | 7 | 80 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4998680353164673 | 0.0 | 0.0 | +— / -b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 1 | 4-5 | 233 | BUY | FAST8 | 100.0 | 7 | 82 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26386067271232605 | 0.0 | 0.0 | +f99cdd31-4a55-4a5e-941a-2800b8afdd7a / -— |
| Jogador 1 | 4-5 | 234 | SELL | FAST8 | 100.0 | 7 | 79 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04712608829140663 | 0.0 | 0.0 | +— / -760d5bee-7d64-4f03-abf0-6357c914a1ed |
| Jogador 1 | 4-5 | 235 | BUY | FAST8 | 100.0 | 7 | 81 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09245222061872482 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -— |
| Jogador 1 | 4-5 | 236 | MOVE_BOARD | FAST8 | 100.0 | 7 | 77 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 237 | MOVE_BOARD | FAST8 | 100.0 | 7 | 77 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018920328468084335 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 238 | PASS | FAST8 | 100.0 | 7 | 77 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09776484221220016 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 242 | SELL | FAST8 | 100.0 | 7 | 91 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -bc0aa086-b5e5-4809-833f-193c5c0da181 |
| Jogador 1 | 4-6 | 243 | BUY | FAST8 | 100.0 | 7 | 95 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1584237664937973 | 0.0 | 0.0 | +b0c1aba5-b1bd-48df-abec-19efa8e49d6d / -— |
| Jogador 1 | 4-6 | 244 | MOVE_BOARD | FAST8 | 100.0 | 7 | 92 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0039108144119381905 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 245 | MOVE_BOARD | FAST8 | 100.0 | 7 | 92 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01501481607556343 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 246 | MOVE_BOARD | FAST8 | 100.0 | 7 | 92 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01551057305186987 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 247 | PASS | FAST8 | 100.0 | 7 | 92 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10888254642486572 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 252 | SELL | FAST8 | 87.0 | 7 | 102 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07013333588838577 | 0.0 | 0.0 | +— / -b0c1aba5-b1bd-48df-abec-19efa8e49d6d |
| Jogador 1 | 4-7 | 253 | BUY | FAST8 | 87.0 | 7 | 105 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7178575396537781 | 0.0 | 0.0 | +a64cf09b-42bf-494e-9603-d387b6740200 / -— |
| Jogador 1 | 4-7 | 254 | MOVE_BOARD | FAST8 | 87.0 | 7 | 102 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00012154587602708489 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 255 | MOVE_BOARD | FAST8 | 87.0 | 7 | 102 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016978319734334946 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 256 | MOVE_BOARD | FAST8 | 87.0 | 7 | 102 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012608304619789124 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 257 | PASS | FAST8 | 87.0 | 7 | 102 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11653128266334534 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 87.0 | 7 | 112 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16544033586978912 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 87.0 | 7 | 112 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09794104099273682 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 264 | SELL | FAST8 | 87.0 | 7 | 112 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.485072523355484 | 0.0 | 0.0 | +— / -844f869e-0e0e-423a-8507-27efd66131f5 |
| Jogador 1 | 5-1 | 265 | BUY | FAST8 | 87.0 | 7 | 115 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9533164501190186 | 0.0 | 0.0 | +45ae38c5-7e69-41bb-9a93-f14db3af3587 / -227dbcdb-af5c-4318-94d1-f01a7847d100,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 5-1 | 266 | BUY | FAST8 | 87.0 | 7 | 112 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9440485835075378 | 0.0 | 0.0 | +79b461e3-2c4f-40a2-b967-e0b6d5248bf6 / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad,a64cf09b-42bf-494e-9603-d387b6740200 |
| Jogador 1 | 5-1 | 267 | BUY | STABILIZE | 87.0 | 7 | 109 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15277495980262756 | 0.0 | 0.0 | +da6c9f59-1fc3-467d-8845-bf7b38b4232c / -— |
| Jogador 1 | 5-1 | 268 | MOVE_BOARD | STABILIZE | 87.0 | 7 | 106 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00011371604341547936 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 269 | MOVE_BENCH | STABILIZE | 87.0 | 7 | 106 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4899195730686188 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 270 | BUY | FAST8 | 87.0 | 7 | 106 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18491142988204956 | 0.0 | 0.0 | +986fbe1e-1826-4be7-a5d6-410a4c0a3f2f / -— |
| Jogador 1 | 5-2 | 272 | BUY | FAST8 | 87.0 | 7 | 114 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8454821109771729 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 1 | 5-2 | 273 | SELL | FAST8 | 87.0 | 7 | 111 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4470444321632385 | 0.0 | 0.0 | +— / -79b461e3-2c4f-40a2-b967-e0b6d5248bf6 |
| Jogador 1 | 5-2 | 274 | BUY | FAST8 | 87.0 | 7 | 119 | 5 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9507668614387512 | 0.0 | 0.0 | +4b1f1146-d580-41e9-987f-c32b1eb98b75 / -600071dd-5c17-4f03-903f-d1cd6c20bb28,cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 5-2 | 275 | BUY | STABILIZE | 87.0 | 7 | 118 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.022971510887146 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -c8968d39-6c58-42c5-a3aa-a5643e7ec8d5,e4764e13-e26d-4358-980a-c7c625e26726 |
| Jogador 1 | 5-2 | 276 | BUY | STABILIZE | 87.0 | 7 | 115 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2438250333070755 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -— |
| Jogador 1 | 5-2 | 277 | MOVE_BENCH | STABILIZE | 87.0 | 7 | 111 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3129625618457794 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 278 | BUY | FAST8 | 87.0 | 7 | 111 | 5 | 40.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25309687852859497 | 0.0 | 0.0 | +f84cc827-410f-47eb-bd95-bd650acfdd4b / -— |
| Jogador 1 | 5-2 | 279 | BUY_XP | FAST8 | 87.0 | 7 | 109 | 5 | 40.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05511999875307083 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 280 | BUY_XP | FAST8 | 87.0 | 7 | 105 | 5 | 40.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05511999875307083 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 282 | SELL | FAST8 | 72.0 | 7 | 111 | 5 | 40.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -4b1f1146-d580-41e9-987f-c32b1eb98b75 |
| Jogador 1 | 5-3 | 283 | BUY | FAST8 | 72.0 | 7 | 114 | 5 | 40.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8841695189476013 | 0.0 | 0.0 | +64d87de4-68df-4a72-8b8d-f78039ae4ce5 / -— |
| Jogador 1 | 5-3 | 284 | SELL | FAST8 | 72.0 | 7 | 113 | 5 | 40.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -45ae38c5-7e69-41bb-9a93-f14db3af3587 |
| Jogador 1 | 5-3 | 285 | BUY | FAST8 | 72.0 | 7 | 121 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38418132066726685 | 0.0 | 0.0 | +b2517873-8317-401b-8461-1d86969edbd7 / -— |
| Jogador 1 | 5-3 | 286 | SELL | FAST8 | 72.0 | 7 | 119 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -f84cc827-410f-47eb-bd95-bd650acfdd4b |
| Jogador 1 | 5-3 | 287 | BUY | FAST8 | 72.0 | 7 | 121 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34780874848365784 | 0.0 | 0.0 | +f0264dc3-6749-4682-929e-fab42383532a / -— |
| Jogador 1 | 5-3 | 288 | MOVE_BOARD | FAST8 | 72.0 | 7 | 117 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 289 | MOVE_BENCH | FAST8 | 72.0 | 7 | 117 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08431228250265121 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 290 | MOVE_BOARD | FAST8 | 72.0 | 7 | 117 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 292 | SELL | FAST8 | 57.0 | 7 | 128 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01772754080593586 | 0.0 | 0.0 | +— / -3fc2815d-c456-47c3-bb27-783336b3cdfa |
| Jogador 1 | 5-4 | 293 | BUY | FAST8 | 57.0 | 7 | 130 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9107109308242798 | 0.0 | 0.0 | +6fb5e8f1-2656-486b-9478-161c1b430d5f / -— |
| Jogador 1 | 5-4 | 294 | SELL | FAST8 | 57.0 | 7 | 128 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -da6c9f59-1fc3-467d-8845-bf7b38b4232c |
| Jogador 1 | 5-4 | 295 | BUY | FAST8 | 57.0 | 7 | 131 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2733725309371948 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -— |
| Jogador 1 | 5-4 | 296 | SELL | FAST8 | 57.0 | 7 | 130 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -986fbe1e-1826-4be7-a5d6-410a4c0a3f2f |
| Jogador 1 | 5-4 | 297 | BUY | FAST8 | 57.0 | 7 | 133 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12143231928348541 | 0.0 | 0.0 | +d30c92eb-1279-4532-b763-7c30826c8430 / -— |
| Jogador 1 | 5-4 | 298 | MOVE_BOARD | FAST8 | 57.0 | 7 | 131 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.286070518195629e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 299 | BUY_XP | FAST8 | 57.0 | 7 | 131 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05511999875307083 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 300 | BUY_XP | FAST8 | 57.0 | 7 | 127 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05511999875307083 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 302 | SELL | FAST8 | 57.0 | 7 | 134 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015533333644270897 | 0.0 | 0.0 | +— / -d30c92eb-1279-4532-b763-7c30826c8430 |
| Jogador 1 | 5-5 | 303 | BUY | FAST8 | 57.0 | 7 | 136 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2053813338279724 | 0.0 | 0.0 | +bbfa514f-8d07-411b-aa19-4511ae5fb5cd / -— |
| Jogador 1 | 5-5 | 304 | SELL | FAST8 | 57.0 | 7 | 131 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 |
| Jogador 1 | 5-5 | 305 | BUY | FAST8 | 57.0 | 7 | 135 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06762725859880447 | 0.0 | 0.0 | +7de5aac5-85d7-4add-b5a7-1c89be9d7e40 / -— |
| Jogador 1 | 5-5 | 306 | SELL | FAST8 | 57.0 | 7 | 133 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -7de5aac5-85d7-4add-b5a7-1c89be9d7e40 |
| Jogador 1 | 5-5 | 307 | BUY | FAST8 | 57.0 | 7 | 135 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0676271915435791 | 0.0 | 0.0 | +2b89bd83-8449-4c63-9da2-62a46c68bdf5 / -— |
| Jogador 1 | 5-5 | 308 | MOVE_BENCH | FAST8 | 57.0 | 7 | 133 | 5 | 42.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5945584774017334 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 309 | BUY | FAST8 | 57.0 | 7 | 133 | 5 | 46.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08899655938148499 | 0.0 | 0.0 | +674bcfdb-fddd-498c-ba65-ef3a3b989f07 / -— |
| Jogador 1 | 5-5 | 310 | MOVE_BOARD | FAST8 | 57.0 | 7 | 132 | 5 | 46.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 312 | SELL | FAST8 | 57.0 | 7 | 143 | 5 | 46.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015206250362098217 | 0.0 | 0.0 | +— / -674bcfdb-fddd-498c-ba65-ef3a3b989f07 |
| Jogador 1 | 5-6 | 313 | BUY | FAST8 | 57.0 | 7 | 144 | 5 | 46.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9536295533180237 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -e1055913-2340-4af0-8527-e175c8bc1ccb,f99cdd31-4a55-4a5e-941a-2800b8afdd7a |
| Jogador 1 | 5-6 | 314 | BUY | FAST8 | 57.0 | 7 | 141 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4038890600204468 | 0.0 | 0.0 | +0a29573e-2a7b-4719-9b6e-49c2f476bc04 / -— |
| Jogador 1 | 5-6 | 315 | SELL | FAST8 | 57.0 | 7 | 138 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.592330276966095 | 0.0 | 0.0 | +— / -f078e755-d142-4dad-99d0-7e7599e3016d |
| Jogador 1 | 5-6 | 316 | BUY | FAST8 | 57.0 | 7 | 146 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28284958004951477 | 0.0 | 0.0 | +d4c27edc-9b7e-4a31-a967-3aa80766b470 / -— |
| Jogador 1 | 5-6 | 317 | MOVE_BOARD | FAST8 | 57.0 | 7 | 144 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.373754902393557e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 318 | SELL | FAST8 | 57.0 | 7 | 144 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -d4c27edc-9b7e-4a31-a967-3aa80766b470 |
| Jogador 1 | 5-6 | 319 | BUY | FAST8 | 57.0 | 7 | 146 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2832790017127991 | 0.0 | 0.0 | +54574f38-262f-44ac-83da-03088b8bdea3 / -— |
| Jogador 1 | 5-6 | 320 | SELL | FAST8 | 57.0 | 7 | 144 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -54574f38-262f-44ac-83da-03088b8bdea3 |
| Jogador 1 | 5-7 | 322 | BUY | ECON | 57.0 | 8 | 157 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1755257248878479 | 0.0 | 0.0 | +8faad4f9-9f15-49e8-94af-b4d28879cc0d / -— |
| Jogador 1 | 5-7 | 323 | SELL | ECON | 57.0 | 8 | 153 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -2b89bd83-8449-4c63-9da2-62a46c68bdf5 |
| Jogador 1 | 5-7 | 324 | BUY | ECON | 57.0 | 8 | 155 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2278643548488617 | 0.0 | 0.0 | +27079fe2-8808-47b7-8b10-9fb2834bb6ed / -— |
| Jogador 1 | 5-7 | 325 | MOVE_BENCH | ECON | 57.0 | 8 | 152 | 5 | 40.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15062972903251648 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 326 | BUY | ECON | 57.0 | 8 | 152 | 5 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7588539719581604 | 0.0 | 0.0 | +3365b4aa-125c-4f72-bcc5-01c5a205b9b0 / -— |
| Jogador 1 | 5-7 | 327 | MOVE_BOARD | ECON | 57.0 | 8 | 149 | 5 | 48.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 328 | MOVE_BOARD | ECON | 57.0 | 8 | 149 | 5 | 48.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014967148192226887 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 329 | PASS | ECON | 57.0 | 8 | 149 | 5 | 48.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1695929616689682 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 332 | BUY | ECON | 57.0 | 8 | 159 | 5 | 50.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.062568187713623 | 0.0 | 0.0 | +1f349179-be2a-4738-bda1-072f7fae2147 / -6fb5e8f1-2656-486b-9478-161c1b430d5f,b2517873-8317-401b-8461-1d86969edbd7 |
| Jogador 1 | 6-1 | 333 | BUY | ECON | 57.0 | 8 | 157 | 5 | 46.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.12221776694059372 | 0.0 | 0.0 | +bdee5671-864a-47c9-9576-9e0d8d2a7c6a / -— |
| Jogador 1 | 6-1 | 334 | EQUIP_FROM_INVENTORY | ECON | 57.0 | 8 | 153 | 5 | 46.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08170471340417862 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 335 | SELL | ECON | 57.0 | 8 | 153 | 5 | 46.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8500000238418579 | 0.0 | 0.0 | +— / -1f349179-be2a-4738-bda1-072f7fae2147 |
| Jogador 1 | 6-1 | 336 | BUY | ECON | 57.0 | 8 | 158 | 5 | 46.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05274656414985657 | 0.0 | 0.0 | +0a0e7d41-96bf-404f-a3bf-98df0a182b63 / -— |
| Jogador 1 | 6-1 | 337 | MOVE_BENCH | ECON | 57.0 | 8 | 155 | 5 | 46.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46610140800476074 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 338 | BUY | ECON | 57.0 | 8 | 155 | 5 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2591865062713623 | 0.0 | 0.0 | +c5520bc4-3123-40f3-b275-83fa8cb06309 / -— |
| Jogador 1 | 6-1 | 339 | MOVE_BOARD | ECON | 57.0 | 8 | 151 | 5 | 52.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 340 | MOVE_BOARD | ECON | 57.0 | 8 | 151 | 5 | 52.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 342 | SELL | ECON | 57.0 | 8 | 161 | 5 | 52.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00426666671410203 | 0.0 | 0.0 | +— / -0a0e7d41-96bf-404f-a3bf-98df0a182b63 |
| Jogador 1 | 6-2 | 343 | BUY | ECON | 57.0 | 8 | 164 | 5 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0612503290176392 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -64d87de4-68df-4a72-8b8d-f78039ae4ce5,6fa83356-562b-4a26-a77d-3e989089e70a |
| Jogador 1 | 6-2 | 344 | BUY | ECON | 57.0 | 8 | 163 | 5 | 50.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46881917119026184 | 0.0 | 0.0 | +920ec426-49cf-489f-aad8-3f5461b93be6 / -— |
| Jogador 1 | 6-2 | 345 | SELL | ECON | 57.0 | 8 | 162 | 5 | 50.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -4261ad99-2607-4d90-978c-9e9abffd6d95 |
| Jogador 1 | 6-2 | 346 | BUY | ECON | 57.0 | 8 | 165 | 5 | 50.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48477935791015625 | 0.0 | 0.0 | +b1d58916-6d8b-4071-a37d-a478395e6a1e / -— |
| Jogador 1 | 6-2 | 347 | MOVE_BOARD | ECON | 57.0 | 8 | 161 | 5 | 50.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 348 | MOVE_BOARD | ECON | 57.0 | 8 | 161 | 5 | 50.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 349 | PASS | ECON | 57.0 | 8 | 161 | 5 | 50.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19694802165031433 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 352 | BUY | STABILIZE | 38.0 | 8 | 171 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16147634387016296 | 0.0 | 0.0 | +92bac611-1820-42eb-8243-499f20058673 / -— |
| Jogador 1 | 6-3 | 353 | SELL | STABILIZE | 38.0 | 8 | 166 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019866665825247765 | 0.0 | 0.0 | +— / -ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 |
| Jogador 1 | 6-3 | 354 | BUY | STABILIZE | 38.0 | 8 | 167 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02549423649907112 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -— |
| Jogador 1 | 6-3 | 355 | MOVE_BOARD | STABILIZE | 38.0 | 8 | 165 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.955716450349428e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 356 | MOVE_BOARD | STABILIZE | 38.0 | 8 | 165 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500015240162611 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 357 | MOVE_BOARD | STABILIZE | 38.0 | 8 | 165 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 358 | PASS | STABILIZE | 38.0 | 8 | 165 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.230290025472641 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-4 | 362 | SELL | ALL_IN | 19.0 | 8 | 176 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -2b10436d-ccfe-4329-aef8-2769899b3787 |
| Jogador 1 | 6-4 | 363 | BUY | ALL_IN | 19.0 | 8 | 178 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1239551454782486 | 0.0 | 0.0 | +5e8a73b8-846a-49a9-be41-30c3baf2cb55 / -— |
| Jogador 1 | 6-4 | 364 | SELL | ALL_IN | 19.0 | 8 | 174 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -c5520bc4-3123-40f3-b275-83fa8cb06309 |
| Jogador 1 | 6-4 | 365 | BUY | ALL_IN | 19.0 | 8 | 178 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06541743874549866 | 0.0 | 0.0 | +46b04fe4-ef4d-4449-94d0-d8bc9660c4e0 / -— |
| Jogador 1 | 6-4 | 366 | SELL | ALL_IN | 19.0 | 8 | 174 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02057906612753868 | 0.0 | 0.0 | +— / -46b04fe4-ef4d-4449-94d0-d8bc9660c4e0 |
| Jogador 1 | 6-4 | 367 | BUY | ALL_IN | 19.0 | 8 | 178 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21907992660999298 | 0.0 | 0.0 | +5d95f8bc-0c01-4c67-8764-4410eb32ee93 / -— |
| Jogador 1 | 6-4 | 368 | MOVE_BOARD | ALL_IN | 19.0 | 8 | 174 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-4 | 369 | MOVE_BOARD | ALL_IN | 19.0 | 8 | 174 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-4 | 370 | PASS | ALL_IN | 19.0 | 8 | 174 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6226933002471924 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 372 | SELL | ALL_IN | 19.0 | 8 | 185 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -5d95f8bc-0c01-4c67-8764-4410eb32ee93 |
| Jogador 1 | 6-5 | 373 | BUY | ALL_IN | 19.0 | 8 | 189 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.190597265958786 | 0.0 | 0.0 | +07080859-42b2-498e-9c11-257fea02f14b / -— |
| Jogador 1 | 6-5 | 374 | SELL | ALL_IN | 19.0 | 8 | 184 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -5e8a73b8-846a-49a9-be41-30c3baf2cb55 |
| Jogador 1 | 6-5 | 375 | BUY | ALL_IN | 19.0 | 8 | 188 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12511500716209412 | 0.0 | 0.0 | +ffd44f6f-388e-4792-ae4f-77f2faa3e95f / -— |
| Jogador 1 | 6-5 | 376 | SELL | ALL_IN | 19.0 | 8 | 184 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -ffd44f6f-388e-4792-ae4f-77f2faa3e95f |
| Jogador 1 | 6-5 | 377 | BUY | ALL_IN | 19.0 | 8 | 188 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004419643431901932 | 0.0 | 0.0 | +249d7b90-0660-4e4f-885a-7791c1cac21a / -— |
| Jogador 1 | 6-5 | 378 | SELL | ALL_IN | 19.0 | 8 | 185 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00426666671410203 | 0.0 | 0.0 | +— / -249d7b90-0660-4e4f-885a-7791c1cac21a |
| Jogador 1 | 6-5 | 379 | BUY | ALL_IN | 19.0 | 8 | 188 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25819408893585205 | 0.0 | 0.0 | +b0f8dc80-dd2b-4dde-87a9-b855a1c13da5 / -— |
| Jogador 1 | 6-5 | 380 | SELL | ALL_IN | 19.0 | 8 | 184 | 5 | 58.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -b0f8dc80-dd2b-4dde-87a9-b855a1c13da5 |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29996994137763977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.16027452051639557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43195363879203796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5009031295776367 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1178059577941895 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11989116668701172 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3088749945163727 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4079098701477051 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0720369815826416 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 44 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20235595107078552 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 45 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40033191442489624 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 46 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024478765204548836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012103810906410217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 48 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 53 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.037959098815918 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18197010457515717 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2734133303165436 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26543864607810974 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 57 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14788657426834106 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047933466732501984 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1965295523405075 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 2 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028999745845794678 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 62 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479700565338135 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 63 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2336135059595108 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 64 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15114977955818176 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 65 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2306191772222519 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 66 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8824999928474426 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-2 | 67 | BUY_XP | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 68 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19457465410232544 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01434213388711214 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 70 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011931832879781723 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.296958863735199 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 73 | BUY | STABILIZE | 90.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.037823885679244995 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 74 | BUY | STABILIZE | 90.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006377584650181234 | 0.0 | 0.0 | +e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 / -— |
| Jogador 2 | 2-3 | 75 | SELL | STABILIZE | 90.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 |
| Jogador 2 | 2-3 | 76 | PASS | STABILIZE | 90.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 82 | BUY | STABILIZE | 85.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7671656012535095 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 2 | 2-4 | 83 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2947123944759369 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 84 | BUY | STABILIZE | 85.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0747293084859848 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 85 | SELL | STABILIZE | 85.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00026666666963137686 | 0.0 | 0.0 | +— / -e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 |
| Jogador 2 | 2-4 | 86 | SELL | STABILIZE | 85.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15261638164520264 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 2-4 | 87 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40151524543762207 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 88 | BUY | STABILIZE | 85.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1598563939332962 | 0.0 | 0.0 | +ce928be1-b3ba-4640-b93c-d15c8a92833e / -— |
| Jogador 2 | 2-4 | 89 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008618667721748352 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032048508524894714 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 92 | BUY | STABILIZE | 85.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3184008300304413 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 93 | BUY | STABILIZE | 85.0 | 5 | 5 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026639046147465706 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 94 | SELL | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03909999877214432 | 0.0 | 0.0 | +— / -ce928be1-b3ba-4640-b93c-d15c8a92833e |
| Jogador 2 | 2-5 | 95 | BUY | STABILIZE | 85.0 | 5 | 3 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19138306379318237 | 0.0 | 0.0 | +6a071ec5-c3f4-41b3-a0d8-c1aee62cffee / -— |
| Jogador 2 | 2-5 | 96 | SELL | STABILIZE | 85.0 | 5 | 0 | 0 | 12.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010601846501231194 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-5 | 97 | BUY | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28094491362571716 | 0.0 | 0.0 | +eb214f08-2367-4b33-af94-8aa504781450 / -— |
| Jogador 2 | 2-5 | 98 | SELL | STABILIZE | 85.0 | 5 | 1 | 0 | 12.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010300000198185444 | 0.0 | 0.0 | +— / -eb214f08-2367-4b33-af94-8aa504781450 |
| Jogador 2 | 2-5 | 99 | SELL | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043666668236255646 | 0.0 | 0.0 | +— / -8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 2-5 | 100 | BUY_XP | STABILIZE | 85.0 | 5 | 5 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 102 | BUY | STABILIZE | 79.0 | 5 | 7 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13221433758735657 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 103 | BUY | STABILIZE | 79.0 | 5 | 4 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19613094627857208 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 104 | SELL | STABILIZE | 79.0 | 5 | 2 | 0 | 12.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010105929337441921 | 0.0 | 0.0 | +— / -6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 2-6 | 105 | BUY_XP | STABILIZE | 79.0 | 5 | 4 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 106 | SELL | STABILIZE | 79.0 | 5 | 0 | 0 | 12.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -6a071ec5-c3f4-41b3-a0d8-c1aee62cffee |
| Jogador 2 | 2-6 | 107 | SELL | STABILIZE | 79.0 | 5 | 3 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -d1840f93-35b0-4e88-b58e-eea7267beedc |
| Jogador 2 | 2-6 | 108 | SELL | STABILIZE | 79.0 | 5 | 6 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42233332991600037 | 0.0 | 0.0 | +— / -97fc5647-5995-4f21-aa03-13454546919a |
| Jogador 2 | 2-6 | 109 | BUY | STABILIZE | 79.0 | 5 | 9 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05966707691550255 | 0.0 | 0.0 | +8ea1c095-e10b-46d0-8097-a70a211e2881 / -— |
| Jogador 2 | 2-6 | 110 | BUY | STABILIZE | 79.0 | 5 | 8 | 0 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39170825481414795 | 0.0 | 0.0 | +752d9bcf-a330-4d9c-aedb-d009c9820888 / -— |
| Jogador 2 | 2-7 | 112 | BUY | STABILIZE | 79.0 | 5 | 13 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3131493031978607 | 0.0 | 0.0 | +0067f61f-504d-440a-b071-de7f18886e3d / -— |
| Jogador 2 | 2-7 | 113 | BUY | STABILIZE | 79.0 | 5 | 12 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045020103454589844 | 0.0 | 0.0 | +6340ebaf-bd41-4f47-bdce-50e06faa4044 / -— |
| Jogador 2 | 2-7 | 114 | SELL | STABILIZE | 79.0 | 5 | 10 | 1 | 12.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0413183756172657 | 0.0 | 0.0 | +— / -6340ebaf-bd41-4f47-bdce-50e06faa4044 |
| Jogador 2 | 2-7 | 115 | SELL | STABILIZE | 79.0 | 5 | 12 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09432800859212875 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 2-7 | 116 | BUY | STABILIZE | 79.0 | 5 | 15 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019108980894088745 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 117 | SELL | STABILIZE | 79.0 | 5 | 12 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37166666984558105 | 0.0 | 0.0 | +— / -729ccd5b-adc5-4bca-9523-dcb532e93ecb |
| Jogador 2 | 2-7 | 118 | SELL | STABILIZE | 79.0 | 5 | 15 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14843736588954926 | 0.0 | 0.0 | +— / -081b684f-5d42-45c5-9a68-12127e5330a7 |
| Jogador 2 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 79.0 | 5 | 18 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0274671521037817 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 120 | SELL | STABILIZE | 79.0 | 5 | 18 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45766666531562805 | 0.0 | 0.0 | +— / -8ea1c095-e10b-46d0-8097-a70a211e2881 |
| Jogador 2 | 3-1 | 122 | BUY | STABILIZE | 79.0 | 5 | 25 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.30506476759910583 | 0.0 | 0.0 | +bbdd0918-bfda-49bc-9ae0-8894eaf11a5c / -— |
| Jogador 2 | 3-1 | 123 | BUY | STABILIZE | 79.0 | 5 | 24 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5012803077697754 | 0.0 | 0.0 | +7115c5a0-d443-49d8-b8a4-e51e259572df / -752d9bcf-a330-4d9c-aedb-d009c9820888,bbdd0918-bfda-49bc-9ae0-8894eaf11a5c |
| Jogador 2 | 3-1 | 124 | BUY | STABILIZE | 79.0 | 5 | 23 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.007034269627183676 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 125 | CRAFT_AND_EQUIP | STABILIZE | 79.0 | 5 | 20 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2577115595340729 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 126 | BUY | STABILIZE | 79.0 | 5 | 20 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0819958746433258 | 0.0 | 0.0 | +4312fba1-1471-4fb3-af6f-257248fa1437 / -— |
| Jogador 2 | 3-1 | 127 | SELL | STABILIZE | 79.0 | 5 | 18 | 1 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017000000923871994 | 0.0 | 0.0 | +— / -7115c5a0-d443-49d8-b8a4-e51e259572df |
| Jogador 2 | 3-1 | 128 | SELL | STABILIZE | 79.0 | 5 | 21 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3940137028694153 | 0.0 | 0.0 | +— / -4312fba1-1471-4fb3-af6f-257248fa1437 |
| Jogador 2 | 3-1 | 129 | SELL | STABILIZE | 79.0 | 5 | 23 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.395135760307312 | 0.0 | 0.0 | +— / -e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 3-1 | 130 | BUY | STABILIZE | 79.0 | 5 | 26 | 2 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0753912553191185 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-2 | 132 | BUY | STABILIZE | 70.0 | 5 | 32 | 3 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8865513801574707 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -7ca9b803-76eb-4283-9648-7f98bfd81149,d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 2 | 3-2 | 133 | BUY | STABILIZE | 70.0 | 5 | 31 | 3 | 10.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7515708804130554 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 134 | BUY | STABILIZE | 70.0 | 5 | 30 | 3 | 10.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45633435249328613 | 0.0 | 0.0 | +e6614d74-9c11-4502-8719-4d49167f44ab / -— |
| Jogador 2 | 3-2 | 135 | SELL | STABILIZE | 70.0 | 5 | 29 | 2 | 10.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5490000247955322 | 0.0 | 0.0 | +— / -5489a8f6-2466-4171-b91e-64c367875d3c |
| Jogador 2 | 3-2 | 136 | BUY | STABILIZE | 70.0 | 5 | 32 | 3 | 10.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2510748505592346 | 0.0 | 0.0 | +e86a4466-cd1f-48a3-a825-cab2e361b72a / -— |
| Jogador 2 | 3-2 | 137 | SELL | STABILIZE | 70.0 | 5 | 31 | 3 | 10.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3596666753292084 | 0.0 | 0.0 | +— / -e86a4466-cd1f-48a3-a825-cab2e361b72a |
| Jogador 2 | 3-2 | 138 | SELL | STABILIZE | 70.0 | 5 | 32 | 3 | 10.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5679555535316467 | 0.0 | 0.0 | +— / -2ace989d-3e9e-483b-9b14-cd6b8f171f17 |
| Jogador 2 | 3-2 | 139 | BUY | STABILIZE | 70.0 | 5 | 35 | 3 | 10.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3016919791698456 | 0.0 | 0.0 | +f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 / -— |
| Jogador 2 | 3-2 | 140 | SELL | STABILIZE | 70.0 | 5 | 34 | 3 | 10.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3230000138282776 | 0.0 | 0.0 | +— / -f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 |
| Jogador 2 | 3-3 | 142 | BUY | STABILIZE | 59.0 | 6 | 44 | 4 | 10.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8553507924079895 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 143 | MOVE_BENCH | STABILIZE | 59.0 | 6 | 41 | 4 | 10.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15098270773887634 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 144 | BUY | STABILIZE | 59.0 | 6 | 41 | 4 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35761210322380066 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 145 | BUY | STABILIZE | 59.0 | 6 | 37 | 3 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08973710238933563 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 146 | BUY | STABILIZE | 59.0 | 6 | 34 | 3 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11188394576311111 | 0.0 | 0.0 | +c30a99f5-ce2d-4bbf-9aab-93017ad40255 / -— |
| Jogador 2 | 3-3 | 147 | SELL | STABILIZE | 59.0 | 6 | 32 | 3 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3356666564941406 | 0.0 | 0.0 | +— / -c30a99f5-ce2d-4bbf-9aab-93017ad40255 |
| Jogador 2 | 3-3 | 148 | SELL | STABILIZE | 59.0 | 6 | 34 | 3 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3503333330154419 | 0.0 | 0.0 | +— / -3880fbd9-322b-4375-b855-fbb779a0cb47 |
| Jogador 2 | 3-3 | 149 | SELL | STABILIZE | 59.0 | 6 | 37 | 3 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25833332538604736 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 3-3 | 150 | MOVE_BENCH | STABILIZE | 59.0 | 6 | 41 | 4 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08886723965406418 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 152 | BUY | STABILIZE | 49.0 | 6 | 51 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04579595848917961 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 2 | 3-4 | 153 | BUY | STABILIZE | 49.0 | 6 | 49 | 4 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6448215246200562 | 0.0 | 0.0 | +a15ff9dc-bf8a-49e0-9893-f92a212263d8 / -— |
| Jogador 2 | 3-4 | 154 | BUY | STABILIZE | 49.0 | 6 | 47 | 4 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04330659285187721 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -— |
| Jogador 2 | 3-4 | 155 | BUY | STABILIZE | 49.0 | 6 | 45 | 4 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4138418138027191 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 2 | 3-4 | 156 | BUY | STABILIZE | 49.0 | 6 | 43 | 4 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2743561863899231 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 41 | 4 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1560012251138687 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 41 | 4 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14091330766677856 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 41 | 4 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 41 | 4 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030564527958631516 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 162 | SELL | STABILIZE | 49.0 | 6 | 51 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 3-5 | 163 | BUY | STABILIZE | 49.0 | 6 | 53 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2962067425251007 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 164 | SELL | STABILIZE | 49.0 | 6 | 50 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47380638122558594 | 0.0 | 0.0 | +— / -c4c0b136-020d-4c1e-9517-8e0bf4c5a628 |
| Jogador 2 | 3-5 | 165 | BUY | STABILIZE | 49.0 | 6 | 52 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05725182592868805 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 166 | SELL | STABILIZE | 49.0 | 6 | 50 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01527232863008976 | 0.0 | 0.0 | +— / -c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 2 | 3-5 | 167 | BUY | STABILIZE | 49.0 | 6 | 52 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2667824923992157 | 0.0 | 0.0 | +c5a8f36d-74b1-4944-a3db-bfb601a89b59 / -— |
| Jogador 2 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 51 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06654360890388489 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 169 | SELL | STABILIZE | 49.0 | 6 | 51 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01133333332836628 | 0.0 | 0.0 | +— / -c5a8f36d-74b1-4944-a3db-bfb601a89b59 |
| Jogador 2 | 3-5 | 170 | BUY | STABILIZE | 49.0 | 6 | 52 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28913307189941406 | 0.0 | 0.0 | +b5cec20a-0619-4060-9f1b-e72942ac34dd / -— |
| Jogador 2 | 3-6 | 172 | SELL | STABILIZE | 38.0 | 6 | 62 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -b5cec20a-0619-4060-9f1b-e72942ac34dd |
| Jogador 2 | 3-6 | 173 | BUY | STABILIZE | 38.0 | 6 | 63 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3574425280094147 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-6 | 174 | SELL | STABILIZE | 38.0 | 6 | 62 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030572667717933655 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 3-6 | 175 | BUY | STABILIZE | 38.0 | 6 | 64 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011198184452950954 | 0.0 | 0.0 | +33a860e2-992f-4355-ab24-85b4a2576f90 / -— |
| Jogador 2 | 3-6 | 176 | SELL | STABILIZE | 38.0 | 6 | 61 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02261989377439022 | 0.0 | 0.0 | +— / -33a860e2-992f-4355-ab24-85b4a2576f90 |
| Jogador 2 | 3-6 | 177 | BUY | STABILIZE | 38.0 | 6 | 64 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013848028145730495 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 178 | SELL | STABILIZE | 38.0 | 6 | 61 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014591259881854057 | 0.0 | 0.0 | +— / -23157bd6-5e8f-4416-bb7f-2e5d71a06543 |
| Jogador 2 | 3-6 | 179 | BUY | STABILIZE | 38.0 | 6 | 64 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06118147447705269 | 0.0 | 0.0 | +8fb80cc8-4120-41a0-bc96-35f81a466ed9 / -— |
| Jogador 2 | 3-6 | 180 | SELL | STABILIZE | 38.0 | 6 | 61 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00426666671410203 | 0.0 | 0.0 | +— / -8fb80cc8-4120-41a0-bc96-35f81a466ed9 |
| Jogador 2 | 3-7 | 182 | BUY | STABILIZE | 26.0 | 6 | 76 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9703097939491272 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -0c15e414-bc67-46de-a087-fb7708db0dfe,e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-7 | 183 | BUY | STABILIZE | 26.0 | 6 | 73 | 5 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007770395837724209 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 2 | 3-7 | 184 | BUY | STABILIZE | 26.0 | 6 | 70 | 5 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24493847787380219 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 185 | SELL | STABILIZE | 26.0 | 6 | 67 | 5 | 14.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 3-7 | 186 | BUY | STABILIZE | 26.0 | 6 | 75 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07405386120080948 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 2 | 3-7 | 187 | SELL | STABILIZE | 26.0 | 6 | 73 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -74b1cd6f-12f4-4287-a5f6-9d016663ccf5 |
| Jogador 2 | 3-7 | 188 | BUY | STABILIZE | 26.0 | 6 | 75 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2711171507835388 | 0.0 | 0.0 | +813260b6-a1b8-4a5c-978e-acd60b6b1082 / -— |
| Jogador 2 | 3-7 | 189 | SELL | STABILIZE | 26.0 | 6 | 74 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01133333332836628 | 0.0 | 0.0 | +— / -813260b6-a1b8-4a5c-978e-acd60b6b1082 |
| Jogador 2 | 3-7 | 190 | SELL | STABILIZE | 26.0 | 6 | 75 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04580000042915344 | 0.0 | 0.0 | +— / -e0445166-70a5-4135-a45e-ff238a95b228 |
| Jogador 2 | 4-1 | 192 | BUY | STABILIZE | 26.0 | 6 | 90 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8274874687194824 | 0.0 | 0.0 | +1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 / -— |
| Jogador 2 | 4-1 | 193 | BUY | STABILIZE | 26.0 | 6 | 89 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04878898337483406 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 2 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 26.0 | 6 | 87 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17452141642570496 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 195 | CRAFT_AND_EQUIP | STABILIZE | 26.0 | 6 | 87 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21882480382919312 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 196 | SELL | STABILIZE | 26.0 | 6 | 87 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030588921159505844 | 0.0 | 0.0 | +— / -1be0cdcc-ee10-44dc-ad1b-de9b53b25164 |
| Jogador 2 | 4-1 | 197 | BUY | STABILIZE | 26.0 | 6 | 89 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2789134681224823 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 2 | 4-1 | 198 | SELL | STABILIZE | 26.0 | 6 | 85 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02276284620165825 | 0.0 | 0.0 | +— / -ed0dab77-fd87-4677-8428-7505ccd34b86 |
| Jogador 2 | 4-1 | 199 | BUY | STABILIZE | 26.0 | 6 | 88 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2909563183784485 | 0.0 | 0.0 | +a4188ec8-4188-4fdf-8d76-c559fc0c7daf / -— |
| Jogador 2 | 4-1 | 200 | SELL | STABILIZE | 26.0 | 6 | 86 | 5 | 14.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -a4188ec8-4188-4fdf-8d76-c559fc0c7daf |
| Jogador 2 | 4-2 | 202 | BUY | ALL_IN | 15.0 | 6 | 101 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.044968843460083 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-2 | 203 | MOVE_BENCH | ALL_IN | 15.0 | 6 | 100 | 5 | 10.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3458654582500458 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 204 | BUY | ALL_IN | 15.0 | 6 | 100 | 5 | 14.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0447601079940796 | 0.0 | 0.0 | +9cb61b5c-2c8a-43a2-a854-517f4377f6db / -046de242-84d0-4f44-a171-345f16a6e719,1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 |
| Jogador 2 | 4-2 | 205 | BUY | ALL_IN | 15.0 | 6 | 99 | 5 | 12.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3604779541492462 | 0.0 | 0.0 | +3fdd5708-2e07-4636-a598-d872f57e1c16 / -— |
| Jogador 2 | 4-2 | 206 | MOVE_BENCH | ALL_IN | 15.0 | 6 | 96 | 5 | 12.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5683593153953552 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 207 | MOVE_BENCH | ALL_IN | 15.0 | 6 | 96 | 5 | 10.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3324226140975952 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 208 | MOVE_BENCH | ALL_IN | 15.0 | 6 | 96 | 5 | 12.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12563414871692657 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 209 | BUY | ALL_IN | 15.0 | 6 | 96 | 5 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10277137160301208 | 0.0 | 0.0 | +c617e958-b482-40ce-ab24-acff4dc48bc0 / -— |
| Jogador 2 | 4-2 | 210 | REROLL | ALL_IN | 15.0 | 6 | 95 | 5 | 16.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 212 | SELL | ALL_IN | 2.0 | 6 | 106 | 5 | 16.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7383000254631042 | 0.0 | 0.0 | +— / -23793b7b-2dab-48f0-a8ba-db85fc14c1c5 |
| Jogador 2 | 4-3 | 213 | BUY | ALL_IN | 2.0 | 6 | 109 | 5 | 16.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7434768080711365 | 0.0 | 0.0 | +7bcf9a7f-a7c9-44a7-9d12-e1ba998b23ed / -— |
| Jogador 2 | 4-3 | 214 | EQUIP_FROM_INVENTORY | ALL_IN | 2.0 | 6 | 108 | 5 | 16.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12990611791610718 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 215 | EQUIP_FROM_INVENTORY | ALL_IN | 2.0 | 6 | 108 | 5 | 16.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.16194897890090942 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 216 | EQUIP_FROM_INVENTORY | ALL_IN | 2.0 | 6 | 108 | 5 | 16.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1435757577419281 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 217 | SELL | ALL_IN | 2.0 | 6 | 108 | 5 | 16.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028877247124910355 | 0.0 | 0.0 | +— / -3fdd5708-2e07-4636-a598-d872f57e1c16 |
| Jogador 2 | 4-3 | 218 | BUY | ALL_IN | 2.0 | 6 | 111 | 5 | 16.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4624471366405487 | 0.0 | 0.0 | +60138930-82d5-4f1c-a5fe-a22ea4b70d36 / -— |
| Jogador 2 | 4-3 | 219 | SELL | ALL_IN | 2.0 | 6 | 109 | 5 | 16.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7357000112533569 | 0.0 | 0.0 | +— / -f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 4-3 | 220 | BUY | ALL_IN | 2.0 | 6 | 110 | 5 | 16.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22888648509979248 | 0.0 | 0.0 | +26462e09-ab6e-4b87-85a8-6bda974b0c45 / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22444601356983185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0904720276594162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40667274594306946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0396608114242554 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.117977499961853 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009961719624698162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 31 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5896894335746765 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22666983306407928 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2118057906627655 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 46 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 53 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26502329111099243 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25187569856643677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23012398183345795 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3955835998058319 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 57 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21856972575187683 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007629113737493753 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012296375818550587 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015378622338175774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9592280387878418 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 63 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3373398184776306 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 64 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3326306939125061 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2671065330505371 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 75 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8901202082633972 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 83 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 84 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8980504274368286 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.947550356388092 | 0.0 | 0.0 | +492fa74a-22b8-4f7d-a4f9-346fdcf565be / -c70251e8-af44-4466-808f-d49e9e5f57e9,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-5 | 94 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 12.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7087385058403015 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 95 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47410520911216736 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020538339391350746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09967894107103348 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 98 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049516402184963226 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 99 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -492fa74a-22b8-4f7d-a4f9-346fdcf565be |
| Jogador 3 | 2-5 | 100 | BUY_XP | STABILIZE | 95.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 102 | BUY | STABILIZE | 89.0 | 5 | 10 | 1 | 18.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8683999180793762 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 9 | 0 | 16.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43676409125328064 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 104 | BUY | STABILIZE | 89.0 | 5 | 9 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3551364541053772 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -— |
| Jogador 3 | 2-6 | 105 | BUY | STABILIZE | 89.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002625570632517338 | 0.0 | 0.0 | +d97b6383-1870-48d1-a9b8-6a8ce153c9ce / -— |
| Jogador 3 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 5 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012297529028728604 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 5 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02490667812526226 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 108 | PASS | STABILIZE | 89.0 | 5 | 5 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 112 | BUY | STABILIZE | 84.0 | 5 | 11 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.820499062538147 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 113 | BUY | STABILIZE | 84.0 | 5 | 8 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8886560797691345 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 3 | 2-7 | 114 | SELL | STABILIZE | 84.0 | 5 | 6 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00286666676402092 | 0.0 | 0.0 | +— / -d97b6383-1870-48d1-a9b8-6a8ce153c9ce |
| Jogador 3 | 2-7 | 115 | BUY | STABILIZE | 84.0 | 5 | 8 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16189250349998474 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.551115123125783e-17 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007911337539553642 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 118 | PASS | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23765182495117188 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 123 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5879999995231628 | 0.0 | 0.0 | +— / -e2f28d51-690c-476e-b097-e5c69258f933 |
| Jogador 3 | 3-1 | 124 | BUY | STABILIZE | 84.0 | 5 | 14 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8143919110298157 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 13 | 1 | 18.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42145174741744995 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0329902246594429 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 127 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4607555568218231 | 0.0 | 0.0 | +— / -2fa86b11-4e28-4652-890e-f00a79068223 |
| Jogador 3 | 3-1 | 128 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 16 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.644633412361145 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 129 | SELL | STABILIZE | 84.0 | 5 | 16 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5274560451507568 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 3-1 | 130 | BUY | STABILIZE | 84.0 | 5 | 19 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09884177893400192 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-2 | 132 | BUY | STABILIZE | 74.0 | 5 | 23 | 2 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25702425837516785 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 3 | 3-2 | 133 | MOVE_BENCH | STABILIZE | 74.0 | 5 | 20 | 2 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6370076537132263 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 74.0 | 5 | 20 | 2 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40302368998527527 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 135 | PASS | STABILIZE | 74.0 | 5 | 20 | 2 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05849999934434891 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 142 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 29 | 2 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4248037040233612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 143 | BUY | STABILIZE | 63.0 | 6 | 29 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003091435879468918 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-3 | 144 | BUY | STABILIZE | 63.0 | 6 | 25 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01290359441190958 | 0.0 | 0.0 | +ffdee27e-2d30-40b5-9937-92be68ab1390 / -— |
| Jogador 3 | 3-3 | 145 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 23 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3993009030818939 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 146 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 23 | 2 | 32.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2968563139438629 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 147 | PASS | STABILIZE | 63.0 | 6 | 23 | 2 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05999999865889549 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 152 | BUY | STABILIZE | 53.0 | 6 | 33 | 3 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.585380494594574 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 3 | 3-4 | 153 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 30 | 3 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012704057153314352 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 30 | 3 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09380791336297989 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 155 | PASS | STABILIZE | 53.0 | 6 | 30 | 3 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 162 | SELL | STABILIZE | 53.0 | 6 | 41 | 4 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -ffdee27e-2d30-40b5-9937-92be68ab1390 |
| Jogador 3 | 3-5 | 163 | BUY | STABILIZE | 53.0 | 6 | 43 | 4 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7529258131980896 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -c3f8419e-a450-4247-bb65-8de8dba1c8ee,d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 3 | 3-5 | 164 | BUY | STABILIZE | 53.0 | 6 | 40 | 4 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1041836366057396 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 165 | BUY | STABILIZE | 53.0 | 6 | 37 | 3 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07934707403182983 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 3 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 33 | 3 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3701084852218628 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 167 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 33 | 3 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29882127046585083 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 168 | PASS | STABILIZE | 53.0 | 6 | 33 | 3 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026499999687075615 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 172 | SELL | STABILIZE | 44.0 | 6 | 44 | 4 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004966666456311941 | 0.0 | 0.0 | +— / -a9c52953-4532-455b-851f-04079adfd354 |
| Jogador 3 | 3-6 | 173 | BUY | STABILIZE | 44.0 | 6 | 52 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8465235233306885 | 0.0 | 0.0 | +1489b596-9339-407a-b49f-d01ecfdd6f78 / -— |
| Jogador 3 | 3-6 | 174 | SELL | STABILIZE | 44.0 | 6 | 51 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 |
| Jogador 3 | 3-6 | 175 | BUY | STABILIZE | 44.0 | 6 | 54 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8993514180183411 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0,bca8862c-5e5b-4a51-9173-79218fbfea3d |
| Jogador 3 | 3-6 | 176 | MOVE_BENCH | STABILIZE | 44.0 | 6 | 52 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11981713771820068 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 177 | BUY | STABILIZE | 44.0 | 6 | 52 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012530059553682804 | 0.0 | 0.0 | +27102740-ce4d-4bec-a9eb-ed936f6bc364 / -— |
| Jogador 3 | 3-6 | 178 | SELL | STABILIZE | 44.0 | 6 | 50 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6414999961853027 | 0.0 | 0.0 | +— / -0e31b1ec-3ead-480e-8577-f59bb5486d00 |
| Jogador 3 | 3-6 | 179 | BUY | STABILIZE | 44.0 | 6 | 55 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23950234055519104 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 3 | 3-6 | 180 | MOVE_BENCH | STABILIZE | 44.0 | 6 | 52 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09261798113584518 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 182 | BUY | STABILIZE | 35.0 | 6 | 65 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34681493043899536 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 183 | SELL | STABILIZE | 35.0 | 6 | 62 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06617359071969986 | 0.0 | 0.0 | +— / -27102740-ce4d-4bec-a9eb-ed936f6bc364 |
| Jogador 3 | 3-7 | 184 | BUY | STABILIZE | 35.0 | 6 | 64 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016639014706015587 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-7 | 185 | SELL | STABILIZE | 35.0 | 6 | 61 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed |
| Jogador 3 | 3-7 | 186 | BUY | STABILIZE | 35.0 | 6 | 64 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06314697116613388 | 0.0 | 0.0 | +cbcde5b6-8f03-4d96-ade5-1ef113ab25bc / -— |
| Jogador 3 | 3-7 | 187 | SELL | STABILIZE | 35.0 | 6 | 63 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004525742959231138 | 0.0 | 0.0 | +— / -cbcde5b6-8f03-4d96-ade5-1ef113ab25bc |
| Jogador 3 | 3-7 | 188 | BUY | STABILIZE | 35.0 | 6 | 64 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2621900141239166 | 0.0 | 0.0 | +2822845b-56e7-4a10-8766-3f7aa579ffcb / -— |
| Jogador 3 | 3-7 | 189 | SELL | STABILIZE | 35.0 | 6 | 63 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -2822845b-56e7-4a10-8766-3f7aa579ffcb |
| Jogador 3 | 3-7 | 190 | MOVE_BENCH | STABILIZE | 35.0 | 6 | 64 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3411875367164612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 192 | BUY | STABILIZE | 35.0 | 6 | 77 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6783250570297241 | 0.0 | 0.0 | +f64919a5-eb2c-4e23-91ed-0067b3d90951 / -— |
| Jogador 3 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 35.0 | 6 | 74 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1799062043428421 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 35.0 | 6 | 74 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16073273122310638 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 195 | SELL | STABILIZE | 35.0 | 6 | 74 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036752134561538696 | 0.0 | 0.0 | +— / -ccdd8153-af58-4fe7-994c-d49f0a7a17f8 |
| Jogador 3 | 4-1 | 196 | BUY | STABILIZE | 35.0 | 6 | 78 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17441055178642273 | 0.0 | 0.0 | +48be5cb2-e7b3-41f8-b212-79e21249fa6a / -— |
| Jogador 3 | 4-1 | 197 | SELL | STABILIZE | 35.0 | 6 | 74 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -48be5cb2-e7b3-41f8-b212-79e21249fa6a |
| Jogador 3 | 4-1 | 198 | BUY | STABILIZE | 35.0 | 6 | 78 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015077137388288975 | 0.0 | 0.0 | +15d93457-0760-419e-87db-74223c1cb7f4 / -— |
| Jogador 3 | 4-1 | 199 | SELL | STABILIZE | 35.0 | 6 | 75 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -15d93457-0760-419e-87db-74223c1cb7f4 |
| Jogador 3 | 4-1 | 200 | BUY | STABILIZE | 35.0 | 6 | 78 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2857643663883209 | 0.0 | 0.0 | +f8d6cf7b-e18c-4a52-87c6-8858f03eef72 / -— |
| Jogador 3 | 4-2 | 202 | SELL | STABILIZE | 35.0 | 6 | 87 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -f8d6cf7b-e18c-4a52-87c6-8858f03eef72 |
| Jogador 3 | 4-2 | 203 | BUY | STABILIZE | 35.0 | 6 | 89 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8354982137680054 | 0.0 | 0.0 | +9bd6852a-b7a4-468c-a8cc-5318f7906eae / -— |
| Jogador 3 | 4-2 | 204 | SELL | STABILIZE | 35.0 | 6 | 87 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4265666604042053 | 0.0 | 0.0 | +— / -b75c9bc5-9bc7-465a-a97c-59156e5c482d |
| Jogador 3 | 4-2 | 205 | BUY | STABILIZE | 35.0 | 6 | 90 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3167288303375244 | 0.0 | 0.0 | +974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 / -— |
| Jogador 3 | 4-2 | 206 | SELL | STABILIZE | 35.0 | 6 | 88 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -9028d514-586b-4d0e-b042-07389323c8cf |
| Jogador 3 | 4-2 | 207 | BUY | STABILIZE | 35.0 | 6 | 91 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15843833982944489 | 0.0 | 0.0 | +bd0fdf98-49ca-4e4b-b4ec-72ac9a91e87b / -— |
| Jogador 3 | 4-2 | 208 | SELL | STABILIZE | 35.0 | 6 | 89 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05263393372297287 | 0.0 | 0.0 | +— / -bd0fdf98-49ca-4e4b-b4ec-72ac9a91e87b |
| Jogador 3 | 4-2 | 209 | BUY | STABILIZE | 35.0 | 6 | 91 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.211039287038147e-05 | 0.0 | 0.0 | +0534477f-2ff8-47a7-b71b-1a1d5430589e / -— |
| Jogador 3 | 4-2 | 210 | SELL | STABILIZE | 35.0 | 6 | 88 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -0534477f-2ff8-47a7-b71b-1a1d5430589e |
| Jogador 3 | 4-3 | 212 | BUY | STABILIZE | 35.0 | 6 | 103 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0023712855763733387 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -— |
| Jogador 3 | 4-3 | 213 | SELL | STABILIZE | 35.0 | 6 | 100 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020266667008399963 | 0.0 | 0.0 | +— / -d8ecc66e-097d-4caa-a657-90fcd1286c2b |
| Jogador 3 | 4-3 | 214 | BUY | STABILIZE | 35.0 | 6 | 103 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0025962544605135918 | 0.0 | 0.0 | +16acc555-c819-4f7c-b406-2f48f11ffc87 / -— |
| Jogador 3 | 4-3 | 215 | SELL | STABILIZE | 35.0 | 6 | 100 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020206142216920853 | 0.0 | 0.0 | +— / -16acc555-c819-4f7c-b406-2f48f11ffc87 |
| Jogador 3 | 4-3 | 216 | BUY | STABILIZE | 35.0 | 6 | 103 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010462254285812378 | 0.0 | 0.0 | +333b0a0b-8868-40b2-96e9-71e468c5dd1f / -— |
| Jogador 3 | 4-3 | 217 | SELL | STABILIZE | 35.0 | 6 | 100 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03322863206267357 | 0.0 | 0.0 | +— / -333b0a0b-8868-40b2-96e9-71e468c5dd1f |
| Jogador 3 | 4-3 | 218 | BUY | STABILIZE | 35.0 | 6 | 103 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2767696976661682 | 0.0 | 0.0 | +72c247af-bdc3-410c-98dd-dd72b56f2818 / -— |
| Jogador 3 | 4-3 | 219 | SELL | STABILIZE | 35.0 | 6 | 99 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -72c247af-bdc3-410c-98dd-dd72b56f2818 |
| Jogador 3 | 4-3 | 220 | BUY | STABILIZE | 35.0 | 6 | 103 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2688661515712738 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 3 | 4-4 | 222 | SELL | ALL_IN | 24.0 | 6 | 112 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009600000455975533 | 0.0 | 0.0 | +— / -27a4bd22-9c1f-4f9f-9192-06ea4933feb5 |
| Jogador 3 | 4-4 | 223 | BUY | ALL_IN | 24.0 | 6 | 113 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017004286870360374 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -— |
| Jogador 3 | 4-4 | 224 | SELL | ALL_IN | 24.0 | 6 | 110 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03322868421673775 | 0.0 | 0.0 | +— / -e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 |
| Jogador 3 | 4-4 | 225 | BUY | ALL_IN | 24.0 | 6 | 113 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04913104698061943 | 0.0 | 0.0 | +677ea844-e1bf-4c68-a0b0-136abb86ba7b / -— |
| Jogador 3 | 4-4 | 226 | SELL | ALL_IN | 24.0 | 6 | 112 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026666666381061077 | 0.0 | 0.0 | +— / -677ea844-e1bf-4c68-a0b0-136abb86ba7b |
| Jogador 3 | 4-4 | 227 | BUY | ALL_IN | 24.0 | 6 | 113 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049124300479888916 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 3 | 4-4 | 228 | SELL | ALL_IN | 24.0 | 6 | 112 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026666666381061077 | 0.0 | 0.0 | +— / -b755a0c5-f515-4f95-8f58-1e05f40ad302 |
| Jogador 3 | 4-4 | 229 | BUY | ALL_IN | 24.0 | 6 | 113 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2874540388584137 | 0.0 | 0.0 | +15c93ffb-d63e-43e6-aa46-ba2beed9cb53 / -— |
| Jogador 3 | 4-4 | 230 | REROLL | ALL_IN | 24.0 | 6 | 111 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 232 | SELL | ALL_IN | 24.0 | 6 | 119 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -15c93ffb-d63e-43e6-aa46-ba2beed9cb53 |
| Jogador 3 | 4-5 | 233 | BUY | ALL_IN | 24.0 | 6 | 121 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.455725759267807 | 0.0 | 0.0 | +ac547bcb-d285-480d-b50e-3cfba572db5a / -— |
| Jogador 3 | 4-5 | 234 | SELL | ALL_IN | 24.0 | 6 | 120 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09613333642482758 | 0.0 | 0.0 | +— / -974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 |
| Jogador 3 | 4-5 | 235 | BUY | ALL_IN | 24.0 | 6 | 122 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014475357718765736 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -— |
| Jogador 3 | 4-5 | 236 | SELL | ALL_IN | 24.0 | 6 | 120 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6740999817848206 | 0.0 | 0.0 | +— / -ac547bcb-d285-480d-b50e-3cfba572db5a |
| Jogador 3 | 4-5 | 237 | BUY | ALL_IN | 24.0 | 6 | 121 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24415014684200287 | 0.0 | 0.0 | +262702a6-b710-4129-9dc6-0c1a04514ff9 / -— |
| Jogador 3 | 4-5 | 238 | SELL | ALL_IN | 24.0 | 6 | 118 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -262702a6-b710-4129-9dc6-0c1a04514ff9 |
| Jogador 3 | 4-5 | 239 | BUY | ALL_IN | 24.0 | 6 | 121 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24414072930812836 | 0.0 | 0.0 | +84981e98-bfb7-4c49-a020-51cf6d864881 / -— |
| Jogador 3 | 4-5 | 240 | REROLL | ALL_IN | 24.0 | 6 | 118 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 242 | SELL | ALL_IN | 11.0 | 6 | 127 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -84981e98-bfb7-4c49-a020-51cf6d864881 |
| Jogador 3 | 4-6 | 243 | BUY | ALL_IN | 11.0 | 6 | 130 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9420357942581177 | 0.0 | 0.0 | +06332ba7-fc4e-431e-ab25-2fb284c08c33 / -— |
| Jogador 3 | 4-6 | 244 | SELL | ALL_IN | 11.0 | 6 | 128 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5642004013061523 | 0.0 | 0.0 | +— / -99511886-d1a7-4910-b099-5072e5385c63 |
| Jogador 3 | 4-6 | 245 | BUY | ALL_IN | 11.0 | 6 | 129 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0032078877557069063 | 0.0 | 0.0 | +18e21ac6-f873-4310-95c8-bd8e62612479 / -— |
| Jogador 3 | 4-6 | 246 | SELL | ALL_IN | 11.0 | 6 | 128 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -18e21ac6-f873-4310-95c8-bd8e62612479 |
| Jogador 3 | 4-6 | 247 | BUY | ALL_IN | 11.0 | 6 | 129 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04742870479822159 | 0.0 | 0.0 | +27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 / -— |
| Jogador 3 | 4-6 | 248 | SELL | ALL_IN | 11.0 | 6 | 128 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026666666381061077 | 0.0 | 0.0 | +— / -27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 |
| Jogador 3 | 4-6 | 249 | BUY | ALL_IN | 11.0 | 6 | 129 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2607603967189789 | 0.0 | 0.0 | +8b75555c-d84d-4b8a-8d6c-012585a05b99 / -— |
| Jogador 3 | 4-6 | 250 | SELL | ALL_IN | 11.0 | 6 | 128 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -8b75555c-d84d-4b8a-8d6c-012585a05b99 |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2201479971408844 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09193183481693268 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4641140401363373 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16314318776130676 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0601743720471859 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 31 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0128071308135986 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33921104669570923 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 53 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9801995158195496 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18384495377540588 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21620437502861023 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 56 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 57 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9554777145385742 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 63 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 64 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 70 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42860743403434753 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 72 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9438580274581909 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 73 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.043445110321045 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 74 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3041417598724365 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 75 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Camille | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5619999766349792 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 76 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 77 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1003502607345581 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 79 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5416666865348816 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-3 | 80 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13732856512069702 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2376100718975067 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15833333134651184 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005146525800228119 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11433333158493042 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08100000023841858 | 0.0 | 0.0 | +— / -0b62545c-1de0-47d8-bb4c-119f7e1526b3 |
| Jogador 4 | 2-4 | 89 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24995191395282745 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 90 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9549352526664734 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 4 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.001156210899353 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -86c535a4-a22b-4667-bc0f-46b4843d97cc,8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38448765873908997 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 4 | 2-5 | 94 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20774877071380615 | 0.0 | 0.0 | +— / -4b07138d-44fd-4515-8b65-d7db84f4639c |
| Jogador 4 | 2-5 | 96 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21663181483745575 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3975070118904114 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 98 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5793896913528442 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 2-5 | 99 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013033811934292316 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 102 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3260316252708435 | 0.0 | 0.0 | +f71a7192-663d-46a0-93ef-b900c59c3bde / -— |
| Jogador 4 | 2-6 | 103 | BUY | STABILIZE | 90.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2837255001068115 | 0.0 | 0.0 | +814d07bd-0296-44af-9626-26a8a224d86f / -— |
| Jogador 4 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008337188512086868 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014826050959527493 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01666545867919922 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 107 | PASS | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 112 | BUY | STABILIZE | 84.0 | 6 | 8 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9389603734016418 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -— |
| Jogador 4 | 2-7 | 113 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3618030250072479 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 114 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 115 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2590000033378601 | 0.0 | 0.0 | +— / -5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 2-7 | 116 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5897884964942932 | 0.0 | 0.0 | +— / -814d07bd-0296-44af-9626-26a8a224d86f |
| Jogador 4 | 2-7 | 117 | BUY | STABILIZE | 84.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13401184976100922 | 0.0 | 0.0 | +53a27943-148b-4522-9826-3f2e0b8a7858 / -— |
| Jogador 4 | 2-7 | 118 | SELL | STABILIZE | 84.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15007710456848145 | 0.0 | 0.0 | +— / -4a0403a3-c999-4d4c-83f0-7270e8576aed |
| Jogador 4 | 2-7 | 119 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39851123094558716 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 122 | BUY | STABILIZE | 84.0 | 6 | 9 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8029270172119141 | 0.0 | 0.0 | +8052731e-e34c-4de7-84b1-2b986cfeddaa / -— |
| Jogador 4 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24370227754116058 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 124 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04628751799464226 | 0.0 | 0.0 | +31aa0a5f-4d66-48c2-b6d4-b76ac220c752 / -— |
| Jogador 4 | 3-1 | 125 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 126 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -53a27943-148b-4522-9826-3f2e0b8a7858 |
| Jogador 4 | 3-1 | 127 | BUY | STABILIZE | 84.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041133664548397064 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 128 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04899999871850014 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 3-1 | 129 | SELL | STABILIZE | 84.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -31aa0a5f-4d66-48c2-b6d4-b76ac220c752 |
| Jogador 4 | 3-1 | 130 | BUY_XP | STABILIZE | 84.0 | 6 | 5 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 132 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.837992787361145 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 133 | BUY | STABILIZE | 84.0 | 6 | 6 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879989445209503 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 5 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6043182611465454 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 135 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 5 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014222576282918453 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 5 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05018498748540878 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 137 | PASS | STABILIZE | 84.0 | 6 | 5 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 142 | BUY | STABILIZE | 74.0 | 6 | 10 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.754861056804657 | 0.0 | 0.0 | +52018505-08c9-471f-83b9-fd5066efe55a / -8052731e-e34c-4de7-84b1-2b986cfeddaa,c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 4 | 3-3 | 143 | BUY | STABILIZE | 74.0 | 6 | 8 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1873987764120102 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 144 | SELL | STABILIZE | 74.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5490000247955322 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 3-3 | 145 | EQUIP_FROM_INVENTORY | STABILIZE | 74.0 | 6 | 10 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07346650958061218 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 146 | EQUIP_FROM_INVENTORY | STABILIZE | 74.0 | 6 | 10 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08923202008008957 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 147 | EQUIP_FROM_INVENTORY | STABILIZE | 74.0 | 6 | 10 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0884859710931778 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 148 | BUY | STABILIZE | 74.0 | 6 | 10 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0759669840335846 | 0.0 | 0.0 | +58c38a13-23c5-4ac1-8601-f0636aeb33ab / -— |
| Jogador 4 | 3-3 | 149 | BUY_XP | STABILIZE | 74.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 74.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02360757626593113 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 152 | BUY | STABILIZE | 74.0 | 6 | 9 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2854951322078705 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 4 | 3-4 | 153 | BUY | STABILIZE | 74.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.699629008769989 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -— |
| Jogador 4 | 3-4 | 154 | BUY | STABILIZE | 74.0 | 6 | 6 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2794145941734314 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 155 | SELL | STABILIZE | 74.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -52018505-08c9-471f-83b9-fd5066efe55a |
| Jogador 4 | 3-4 | 156 | BUY_XP | STABILIZE | 74.0 | 6 | 8 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 157 | BUY_XP | STABILIZE | 74.0 | 6 | 4 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0609700009226799 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 158 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 0 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41540753841400146 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 0 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03633603826165199 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 0 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005709315184503794 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 162 | BUY | STABILIZE | 74.0 | 7 | 5 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8017778396606445 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 4 | 3-5 | 163 | BUY | STABILIZE | 74.0 | 7 | 2 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26531359553337097 | 0.0 | 0.0 | +661b176a-5963-4715-b9dd-aca29f552fa9 / -— |
| Jogador 4 | 3-5 | 164 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 0 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0008229927043430507 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 0 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016725311055779457 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 0 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07588078081607819 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 167 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 0 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4622284173965454 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 168 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 0 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07069998979568481 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 169 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 0 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08670883625745773 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 170 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 0 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09773123264312744 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 172 | BUY | STABILIZE | 62.0 | 7 | 5 | 0 | 28.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8049315810203552 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -— |
| Jogador 4 | 3-6 | 173 | BUY | STABILIZE | 62.0 | 7 | 3 | 0 | 28.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11443809419870377 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 174 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 0 | 0 | 28.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012600736692547798 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 175 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 0 | 0 | 28.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3447566330432892 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 176 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 0 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08319409936666489 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 177 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 0 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11376532912254333 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 0 | 0 | 28.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015039783902466297 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 179 | PASS | STABILIZE | 62.0 | 7 | 0 | 0 | 28.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 182 | BUY | STABILIZE | 51.0 | 7 | 6 | 0 | 28.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8335996270179749 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,40f2a32f-1ace-4700-8a79-e6b5d3212036 |
| Jogador 4 | 3-7 | 183 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 3 | 0 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4190485179424286 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 184 | BUY | STABILIZE | 51.0 | 7 | 3 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23197528719902039 | 0.0 | 0.0 | +e3fdce1f-991f-4305-9aaa-fbf72ede6c01 / -— |
| Jogador 4 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 1 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1567424237728119 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 1 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13891690969467163 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 187 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 1 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0599142387509346 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 188 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 1 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4240948259830475 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 189 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 1 | 0 | 26.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.051994431763887405 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 190 | PASS | STABILIZE | 51.0 | 7 | 1 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 192 | BUY | STABILIZE | 51.0 | 7 | 7 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7723308205604553 | 0.0 | 0.0 | +465ecc70-f5da-47f4-a7c0-2005a8ed24c1 / -— |
| Jogador 4 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 51.0 | 7 | 5 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19563210010528564 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 51.0 | 7 | 5 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23602049052715302 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 195 | SELL | STABILIZE | 51.0 | 7 | 5 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03999999910593033 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 4 | 4-1 | 196 | BUY | STABILIZE | 51.0 | 7 | 13 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.70924973487854 | 0.0 | 0.0 | +42733dbd-0bc3-461b-95ab-76daf5ad6296 / -— |
| Jogador 4 | 4-1 | 197 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 10 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12943576276302338 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 198 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 10 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3585263192653656 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 199 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 10 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07833213359117508 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 200 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 10 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07408419251441956 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 202 | SELL | STABILIZE | 37.0 | 7 | 17 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -661b176a-5963-4715-b9dd-aca29f552fa9 |
| Jogador 4 | 4-2 | 203 | BUY | STABILIZE | 37.0 | 7 | 19 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8348775506019592 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -23f4d10f-2614-47b2-bfb2-4fb276764b5e,7fd03119-ac82-49e1-b3bb-3a0caa31011f |
| Jogador 4 | 4-2 | 204 | BUY | STABILIZE | 37.0 | 7 | 17 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04434844106435776 | 0.0 | 0.0 | +55944609-f4df-4e53-a1d1-31c79a148b22 / -— |
| Jogador 4 | 4-2 | 205 | BUY | STABILIZE | 37.0 | 7 | 15 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04630673676729202 | 0.0 | 0.0 | +090f2ba6-5514-49ba-a80d-a0711cd06245 / -— |
| Jogador 4 | 4-2 | 206 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 11 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1010558158159256 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 207 | REROLL | STABILIZE | 37.0 | 7 | 11 | 1 | 28.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21400000154972076 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 208 | SELL | STABILIZE | 37.0 | 7 | 9 | 0 | 28.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07263333350419998 | 0.0 | 0.0 | +— / -58c38a13-23c5-4ac1-8601-f0636aeb33ab |
| Jogador 4 | 4-2 | 209 | BUY | STABILIZE | 37.0 | 7 | 12 | 1 | 28.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28591135144233704 | 0.0 | 0.0 | +6388773b-0e99-40a9-8d68-895dcf16fce6 / -— |
| Jogador 4 | 4-2 | 210 | SELL | STABILIZE | 37.0 | 7 | 10 | 1 | 28.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02468198537826538 | 0.0 | 0.0 | +— / -090f2ba6-5514-49ba-a80d-a0711cd06245 |
| Jogador 4 | 4-3 | 212 | BUY | STABILIZE | 27.0 | 7 | 21 | 2 | 28.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7509043216705322 | 0.0 | 0.0 | +badbffc5-dd49-4cd8-8b4d-941ae020e6e3 / -— |
| Jogador 4 | 4-3 | 213 | REROLL | STABILIZE | 27.0 | 7 | 19 | 1 | 28.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1340000033378601 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 214 | SELL | STABILIZE | 27.0 | 7 | 17 | 1 | 28.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5037046670913696 | 0.0 | 0.0 | +— / -ac8f2a7d-1627-4aa4-a35b-805bce651b0e |
| Jogador 4 | 4-3 | 215 | BUY | STABILIZE | 27.0 | 7 | 18 | 1 | 28.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24369284510612488 | 0.0 | 0.0 | +f4173576-aa2e-4a93-94ec-ecd49d90d2b7 / -— |
| Jogador 4 | 4-3 | 216 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 14 | 1 | 28.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3980337679386139 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 217 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 14 | 1 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8430936336517334 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 218 | PASS | STABILIZE | 27.0 | 7 | 14 | 1 | 24.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 222 | REROLL | ALL_IN | 14.0 | 7 | 22 | 2 | 24.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 223 | SELL | ALL_IN | 14.0 | 7 | 20 | 2 | 24.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6908000111579895 | 0.0 | 0.0 | +— / -4363594b-375b-45d4-9b1a-0c1ab96367a1 |
| Jogador 4 | 4-4 | 224 | BUY | ALL_IN | 14.0 | 7 | 25 | 2 | 24.0 | Florescer/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8424651026725769 | 0.0 | 0.0 | +226f36b1-cb9a-464a-a10a-3f21ebd41f24 / -— |
| Jogador 4 | 4-4 | 225 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 22 | 2 | 24.0 | Florescer/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33116406202316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 226 | REROLL | ALL_IN | 14.0 | 7 | 22 | 2 | 28.0 | Florescer/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 227 | SELL | ALL_IN | 14.0 | 7 | 20 | 2 | 28.0 | Florescer/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0141333332285285 | 0.0 | 0.0 | +— / -f4173576-aa2e-4a93-94ec-ecd49d90d2b7 |
| Jogador 4 | 4-4 | 228 | BUY | ALL_IN | 14.0 | 7 | 24 | 2 | 28.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9098069071769714 | 0.0 | 0.0 | +477a3c7c-70fe-4f67-ab00-8c9c397365bf / -226f36b1-cb9a-464a-a10a-3f21ebd41f24,a92eca5d-299f-4f4d-a16b-d23981ef719f |
| Jogador 4 | 4-4 | 229 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 21 | 2 | 16.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12479992210865021 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 230 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 21 | 2 | 18.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5635707974433899 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 232 | BUY | ALL_IN | 14.0 | 7 | 30 | 3 | 22.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32968997955322266 | 0.0 | 0.0 | +0f5471bd-1451-4979-adc9-aced6bb63610 / -— |
| Jogador 4 | 4-5 | 233 | BUY | ALL_IN | 14.0 | 7 | 27 | 2 | 22.0 | Florescer/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8598620295524597 | 0.0 | 0.0 | +4c1dab77-0e6d-401b-a341-40117b445957 / -— |
| Jogador 4 | 4-5 | 234 | MOVE_BOARD | ALL_IN | 14.0 | 7 | 24 | 2 | 22.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038735900074243546 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 235 | MOVE_BOARD | ALL_IN | 14.0 | 7 | 24 | 2 | 22.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24794772267341614 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 236 | PASS | ALL_IN | 14.0 | 7 | 24 | 2 | 22.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3771470785140991 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 242 | SELL | ALL_IN | 3.0 | 7 | 34 | 3 | 22.0 | Florescer/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.61326664686203 | 0.0 | 0.0 | +— / -477a3c7c-70fe-4f67-ab00-8c9c397365bf |
| Jogador 4 | 4-6 | 243 | BUY | ALL_IN | 3.0 | 7 | 42 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7932529449462891 | 0.0 | 0.0 | +68301141-c9f1-4303-9775-753520772836 / -— |
| Jogador 4 | 4-6 | 244 | MOVE_BOARD | ALL_IN | 3.0 | 7 | 40 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03856690227985382 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 245 | REROLL | ALL_IN | 3.0 | 7 | 40 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 246 | SELL | ALL_IN | 3.0 | 7 | 38 | 3 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6656000018119812 | 0.0 | 0.0 | +— / -0f5471bd-1451-4979-adc9-aced6bb63610 |
| Jogador 4 | 4-6 | 247 | BUY | ALL_IN | 3.0 | 7 | 41 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8893589377403259 | 0.0 | 0.0 | +80130f72-2d7c-49db-8d6f-4c0a962260e8 / -— |
| Jogador 4 | 4-6 | 248 | MOVE_BENCH | ALL_IN | 3.0 | 7 | 38 | 3 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1300746500492096 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 249 | REROLL | ALL_IN | 3.0 | 7 | 38 | 3 | 26.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 250 | SELL | ALL_IN | 3.0 | 7 | 36 | 3 | 26.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7455999851226807 | 0.0 | 0.0 | +— / -80130f72-2d7c-49db-8d6f-4c0a962260e8 |
| Jogador 4 | 4-7 | 252 | BUY | ALL_IN | 3.0 | 7 | 49 | 4 | 26.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0254051685333252 | 0.0 | 0.0 | +02e125a0-3563-47ec-a82a-cba5178731dd / -465ecc70-f5da-47f4-a7c0-2005a8ed24c1,e3fdce1f-991f-4305-9aaa-fbf72ede6c01 |
| Jogador 4 | 4-7 | 253 | REROLL | ALL_IN | 3.0 | 7 | 47 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 254 | BUY | ALL_IN | 3.0 | 7 | 45 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0353885889053345 | 0.0 | 0.0 | +9af900db-c181-448a-9736-30f08f062a00 / -42733dbd-0bc3-461b-95ab-76daf5ad6296,8e1a5a7a-d27d-47c9-a197-b383c1c3da3b |
| Jogador 4 | 4-7 | 255 | MOVE_BENCH | ALL_IN | 3.0 | 7 | 42 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5743851065635681 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 256 | MOVE_BOARD | ALL_IN | 3.0 | 7 | 42 | 4 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0566452220082283 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 257 | BUY | ALL_IN | 3.0 | 7 | 42 | 4 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13806520402431488 | 0.0 | 0.0 | +89ef75a2-6ac2-4c6c-b2b8-492aec985a01 / -— |
| Jogador 4 | 4-7 | 258 | MOVE_BOARD | ALL_IN | 3.0 | 7 | 38 | 3 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 259 | MOVE_BOARD | ALL_IN | 3.0 | 7 | 38 | 3 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02671796828508377 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 260 | PASS | ALL_IN | 3.0 | 7 | 38 | 3 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5711174607276917 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 3.0 | 7 | 46 | 4 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23692484200000763 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 3.0 | 7 | 46 | 4 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11960634589195251 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 264 | BUY | ALL_IN | 3.0 | 7 | 46 | 4 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13661248981952667 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -— |
| Jogador 4 | 5-1 | 265 | BUY | ALL_IN | 3.0 | 7 | 43 | 4 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04503512382507324 | 0.0 | 0.0 | +99857cfa-b422-4167-bb01-d9fd94a55d88 / -— |
| Jogador 4 | 5-1 | 266 | MOVE_BOARD | ALL_IN | 3.0 | 7 | 41 | 4 | 24.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13851594924926758 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 267 | MOVE_BOARD | ALL_IN | 3.0 | 7 | 41 | 4 | 24.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1840970665216446 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 268 | MOVE_BOARD | ALL_IN | 3.0 | 7 | 41 | 4 | 24.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012282642535865307 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 269 | MOVE_BOARD | ALL_IN | 3.0 | 7 | 41 | 4 | 24.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 270 | PASS | ALL_IN | 3.0 | 7 | 41 | 4 | 24.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4500619173049927 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.26577791571617126 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.24549612402915955 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12370830029249191 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11255644261837006 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17292346060276031 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012102286331355572 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4293290078639984 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2171582281589508 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 28 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3299944996833801 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28838351368904114 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 53 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0326346158981323 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19878919422626495 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21278688311576843 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4088495075702667 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 57 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2263445407152176 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 58 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9719067215919495 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 64 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0441429615020752 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12275978177785873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 75 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24612870812416077 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4363296329975128 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 77 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16280953586101532 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03177344799041748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 79 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25788190960884094 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 80 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31068912148475647 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 83 | BUY | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21864677965641022 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 84 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05810000002384186 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 85 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08822011202573776 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-4 | 86 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 87 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09731132537126541 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-4 | 88 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1047755628824234 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-4 | 89 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18893489241600037 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 90 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17965556681156158 | 0.0 | 0.0 | +32b7b452-7702-43a3-b3c4-8eda786225b9 / -— |
| Jogador 5 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2671777904033661 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 93 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3246571719646454 | 0.0 | 0.0 | +de78e1b7-ed58-42dd-8374-76b578543e94 / -— |
| Jogador 5 | 2-5 | 94 | SELL | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030366666615009308 | 0.0 | 0.0 | +— / -32b7b452-7702-43a3-b3c4-8eda786225b9 |
| Jogador 5 | 2-5 | 95 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 96 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030533334240317345 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-5 | 97 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40817776322364807 | 0.0 | 0.0 | +— / -de78e1b7-ed58-42dd-8374-76b578543e94 |
| Jogador 5 | 2-5 | 98 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0983823761343956 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3566199839115143 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 102 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179386377334595 | 0.0 | 0.0 | +53312511-4e10-4904-82c0-8a8e69c039cd / -02c39b42-90d5-4e01-9380-460b6c1cb993,eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 2-6 | 103 | BUY | STABILIZE | 100.0 | 6 | 6 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03245232626795769 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 104 | BUY | STABILIZE | 100.0 | 6 | 4 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017284218221902847 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 105 | SELL | STABILIZE | 100.0 | 6 | 2 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -53312511-4e10-4904-82c0-8a8e69c039cd |
| Jogador 5 | 2-6 | 106 | BUY_XP | STABILIZE | 100.0 | 6 | 5 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14187052845954895 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1014888659119606 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 109 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16827690601348877 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1781054586172104 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 112 | BUY | STABILIZE | 93.0 | 6 | 6 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.206015944480896 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -— |
| Jogador 5 | 2-7 | 113 | BUY | STABILIZE | 93.0 | 6 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1374874860048294 | 0.0 | 0.0 | +6eee9a92-4235-46af-ae42-c38acd6847ef / -— |
| Jogador 5 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13745157420635223 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 115 | SELL | STABILIZE | 93.0 | 6 | 3 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08807259798049927 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 2-7 | 116 | BUY_XP | STABILIZE | 93.0 | 6 | 4 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 117 | PASS | STABILIZE | 93.0 | 6 | 0 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 122 | BUY | STABILIZE | 93.0 | 6 | 5 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2208625227212906 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 93.0 | 6 | 2 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13043656945228577 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 124 | BUY | STABILIZE | 93.0 | 6 | 2 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16165415942668915 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 5 | 3-1 | 125 | SELL | STABILIZE | 93.0 | 6 | 0 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 3-1 | 126 | SELL | STABILIZE | 93.0 | 6 | 2 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09749244153499603 | 0.0 | 0.0 | +— / -a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 |
| Jogador 5 | 3-1 | 127 | BUY_XP | STABILIZE | 93.0 | 6 | 4 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 128 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 0 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.100835882127285 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 129 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 130 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04400578513741493 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 132 | BUY | STABILIZE | 93.0 | 6 | 6 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7171378135681152 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 133 | BUY | STABILIZE | 93.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06004583463072777 | 0.0 | 0.0 | +d218597b-b641-4a4c-867a-41227b83fcff / -— |
| Jogador 5 | 3-2 | 134 | SELL | STABILIZE | 93.0 | 6 | 1 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05152793973684311 | 0.0 | 0.0 | +— / -135065df-1ebc-413d-86f1-4df28bd3ee41 |
| Jogador 5 | 3-2 | 135 | BUY | STABILIZE | 93.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13041961193084717 | 0.0 | 0.0 | +1662b43d-12f4-45d6-b1bf-3733d5214808 / -— |
| Jogador 5 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022326402366161346 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0449877567589283 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 138 | SELL | STABILIZE | 93.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3903333246707916 | 0.0 | 0.0 | +— / -1662b43d-12f4-45d6-b1bf-3733d5214808 |
| Jogador 5 | 3-2 | 139 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0002657681470736861 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 140 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014947233721613884 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 142 | BUY | STABILIZE | 93.0 | 6 | 10 | 1 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.714759886264801 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-3 | 143 | BUY | STABILIZE | 93.0 | 6 | 7 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2838689386844635 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 144 | BUY | STABILIZE | 93.0 | 6 | 4 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.285076767206192 | 0.0 | 0.0 | +a29f1c5b-c2f0-48be-b39c-0aa0d57fb94a / -— |
| Jogador 5 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005866598803550005 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014974881894886494 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 147 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35341382026672363 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 148 | PASS | STABILIZE | 93.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 152 | BUY | STABILIZE | 93.0 | 6 | 9 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8053116202354431 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 153 | BUY | STABILIZE | 93.0 | 6 | 7 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8058580756187439 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -— |
| Jogador 5 | 3-4 | 154 | BUY_XP | STABILIZE | 93.0 | 6 | 6 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 155 | SELL | STABILIZE | 93.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -d218597b-b641-4a4c-867a-41227b83fcff |
| Jogador 5 | 3-4 | 156 | BUY_XP | STABILIZE | 93.0 | 6 | 4 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 157 | SELL | STABILIZE | 93.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5423402190208435 | 0.0 | 0.0 | +— / -e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 3-4 | 158 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3327900171279907 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 3 | 0 | 26.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05793766304850578 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 3 | 0 | 26.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21746140718460083 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 162 | BUY | STABILIZE | 93.0 | 7 | 9 | 0 | 26.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28734084963798523 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -— |
| Jogador 5 | 3-5 | 163 | BUY | STABILIZE | 93.0 | 7 | 8 | 0 | 26.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15472358465194702 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-5 | 164 | BUY_XP | STABILIZE | 93.0 | 7 | 5 | 0 | 26.0 | Espinhos Negros/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 93.0 | 7 | 1 | 0 | 26.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003246899927034974 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 93.0 | 7 | 1 | 0 | 26.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01578385755419731 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 93.0 | 7 | 1 | 0 | 26.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014486290514469147 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 168 | PASS | STABILIZE | 93.0 | 7 | 1 | 0 | 26.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 172 | BUY | STABILIZE | 83.0 | 7 | 6 | 0 | 28.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.832558810710907 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -486e92ad-4dcf-4c0e-a470-e0b87777d380,a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 5 | 3-6 | 173 | BUY | STABILIZE | 83.0 | 7 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7137535214424133 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-6 | 174 | MOVE_BOARD | STABILIZE | 83.0 | 7 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011218015104532242 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 175 | SELL | STABILIZE | 83.0 | 7 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5615250468254089 | 0.0 | 0.0 | +— / -750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 5 | 3-6 | 176 | BUY | STABILIZE | 83.0 | 7 | 8 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019620263949036598 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -— |
| Jogador 5 | 3-6 | 177 | BUY_XP | STABILIZE | 83.0 | 7 | 6 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 178 | SELL | STABILIZE | 83.0 | 7 | 2 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 |
| Jogador 5 | 3-6 | 179 | BUY_XP | STABILIZE | 83.0 | 7 | 4 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 180 | MOVE_BOARD | STABILIZE | 83.0 | 7 | 0 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00988190807402134 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 182 | BUY | STABILIZE | 72.0 | 7 | 6 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5087301731109619 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 183 | SELL | STABILIZE | 72.0 | 7 | 3 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43165066838264465 | 0.0 | 0.0 | +— / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 5 | 3-7 | 184 | BUY | STABILIZE | 72.0 | 7 | 6 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011886966414749622 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 5 | 3-7 | 185 | SELL | STABILIZE | 72.0 | 7 | 3 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 5 | 3-7 | 186 | BUY | STABILIZE | 72.0 | 7 | 6 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0029476829804480076 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 187 | SELL | STABILIZE | 72.0 | 7 | 3 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012360524386167526 | 0.0 | 0.0 | +— / -8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 |
| Jogador 5 | 3-7 | 188 | BUY_XP | STABILIZE | 72.0 | 7 | 6 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 189 | SELL | STABILIZE | 72.0 | 7 | 2 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4740857779979706 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-7 | 190 | BUY_XP | STABILIZE | 72.0 | 7 | 5 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 192 | BUY | STABILIZE | 72.0 | 7 | 7 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.27993813157081604 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 193 | BUY | STABILIZE | 72.0 | 7 | 4 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.37879928946495056 | 0.0 | 0.0 | +6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 / -— |
| Jogador 5 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 72.0 | 7 | 2 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19146858155727386 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 195 | CRAFT_AND_EQUIP | STABILIZE | 72.0 | 7 | 2 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12126117944717407 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 196 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 2 | 0 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4794131815433502 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 197 | BUY | STABILIZE | 72.0 | 7 | 2 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03411897271871567 | 0.0 | 0.0 | +f6de9b7d-1373-459e-b34a-7b878d1a1268 / -— |
| Jogador 5 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0002045064902631566 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 200 | PASS | STABILIZE | 72.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 202 | SELL | STABILIZE | 72.0 | 7 | 6 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00026666666963137686 | 0.0 | 0.0 | +— / -f6de9b7d-1373-459e-b34a-7b878d1a1268 |
| Jogador 5 | 4-2 | 203 | BUY | STABILIZE | 72.0 | 7 | 8 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.806129515171051 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 5 | 4-2 | 204 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 7 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03812794014811516 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 205 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 7 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02265000529587269 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 206 | SELL | STABILIZE | 72.0 | 7 | 7 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41069358587265015 | 0.0 | 0.0 | +— / -6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 |
| Jogador 5 | 4-2 | 207 | BUY | STABILIZE | 72.0 | 7 | 9 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0855097845196724 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 5 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 5 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.230187864275649e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 209 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 5 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014970647171139717 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 210 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 5 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 212 | SELL | STABILIZE | 72.0 | 7 | 12 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -d9fdb961-a3e3-4e39-9970-e46ffd59fc3b |
| Jogador 5 | 4-3 | 213 | BUY | STABILIZE | 72.0 | 7 | 16 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8038633465766907 | 0.0 | 0.0 | +c7841e00-91da-410b-b00f-62f4bf32f666 / -— |
| Jogador 5 | 4-3 | 214 | SELL | STABILIZE | 72.0 | 7 | 13 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4552531838417053 | 0.0 | 0.0 | +— / -60255a84-4f78-49f0-a4f1-d598704c7ee7 |
| Jogador 5 | 4-3 | 215 | BUY | STABILIZE | 72.0 | 7 | 16 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8376704454421997 | 0.0 | 0.0 | +485dab1f-b3a1-4170-8ed6-c0035072ae9b / -9593a62e-442f-410a-8a0c-7d781e2487cc,ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 4-3 | 216 | BUY | STABILIZE | 72.0 | 7 | 15 | 1 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7848243713378906 | 0.0 | 0.0 | +f5cca112-4fa0-4ee6-a863-20a5d49ab7ef / -— |
| Jogador 5 | 4-3 | 217 | SELL | STABILIZE | 72.0 | 7 | 12 | 1 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -485dab1f-b3a1-4170-8ed6-c0035072ae9b |
| Jogador 5 | 4-3 | 218 | EQUIP_FROM_INVENTORY | STABILIZE | 72.0 | 7 | 15 | 1 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08937104046344757 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 219 | BUY | STABILIZE | 72.0 | 7 | 15 | 1 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27573361992836 | 0.0 | 0.0 | +17d5d3f2-999d-4788-852b-bda84adb4350 / -— |
| Jogador 5 | 4-3 | 220 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 12 | 1 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5644981265068054 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 222 | BUY | STABILIZE | 72.0 | 7 | 20 | 2 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7248266339302063 | 0.0 | 0.0 | +8995f621-b355-44ec-816e-797184bdc266 / -— |
| Jogador 5 | 4-4 | 223 | SELL | STABILIZE | 72.0 | 7 | 17 | 1 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9556666612625122 | 0.0 | 0.0 | +— / -ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 4-4 | 224 | BUY | STABILIZE | 72.0 | 7 | 18 | 1 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28767621517181396 | 0.0 | 0.0 | +167110eb-b0d0-4873-9ffe-38286dcc5ca2 / -— |
| Jogador 5 | 4-4 | 225 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 17 | 1 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009655745816417038 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 226 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 17 | 1 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014493666589260101 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 227 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 17 | 1 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014799192547798157 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 228 | PASS | STABILIZE | 72.0 | 7 | 17 | 1 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026428570970892906 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 232 | SELL | STABILIZE | 72.0 | 7 | 24 | 2 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5879999995231628 | 0.0 | 0.0 | +— / -167110eb-b0d0-4873-9ffe-38286dcc5ca2 |
| Jogador 5 | 4-5 | 233 | BUY | STABILIZE | 72.0 | 7 | 25 | 2 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.81719571352005 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 5 | 4-5 | 234 | SELL | STABILIZE | 72.0 | 7 | 24 | 2 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9556666612625122 | 0.0 | 0.0 | +— / -7fb0217d-521c-42b5-995c-81e299b3b934 |
| Jogador 5 | 4-5 | 235 | BUY | STABILIZE | 72.0 | 7 | 25 | 2 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16683517396450043 | 0.0 | 0.0 | +a5c83255-d413-4d36-92a8-3552e6785108 / -— |
| Jogador 5 | 4-5 | 236 | SELL | STABILIZE | 72.0 | 7 | 23 | 2 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028866667300462723 | 0.0 | 0.0 | +— / -a5c83255-d413-4d36-92a8-3552e6785108 |
| Jogador 5 | 4-5 | 237 | BUY | STABILIZE | 72.0 | 7 | 25 | 2 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13712362945079803 | 0.0 | 0.0 | +42aa4dc8-e388-40dd-a210-4c59e358afcd / -— |
| Jogador 5 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 24 | 2 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00010567874414846301 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 24 | 2 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014597355388104916 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 240 | PASS | STABILIZE | 72.0 | 7 | 24 | 2 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03142857179045677 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 242 | SELL | STABILIZE | 72.0 | 7 | 33 | 3 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023499999195337296 | 0.0 | 0.0 | +— / -42aa4dc8-e388-40dd-a210-4c59e358afcd |
| Jogador 5 | 4-6 | 243 | BUY | STABILIZE | 72.0 | 7 | 34 | 3 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8937967419624329 | 0.0 | 0.0 | +5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 / -1457cd1e-c240-4ce5-9217-a91bddfc8807,4af85188-f11e-4aca-8165-ba8e7f535670 |
| Jogador 5 | 4-6 | 244 | BUY | STABILIZE | 72.0 | 7 | 31 | 3 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09509298950433731 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 5 | 4-6 | 245 | SELL | STABILIZE | 72.0 | 7 | 27 | 2 | 22.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 |
| Jogador 5 | 4-6 | 246 | BUY | STABILIZE | 72.0 | 7 | 35 | 3 | 22.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15523330867290497 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -— |
| Jogador 5 | 4-6 | 247 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 34 | 3 | 22.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.516775369644165 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 248 | BUY | STABILIZE | 72.0 | 7 | 34 | 3 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07492662221193314 | 0.0 | 0.0 | +6eecc806-dcf8-47df-bc1d-bc5bc5f07099 / -— |
| Jogador 5 | 4-6 | 249 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 33 | 3 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002214133972302079 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 250 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 33 | 3 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015008840709924698 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 252 | SELL | STABILIZE | 72.0 | 7 | 42 | 4 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025979306548833847 | 0.0 | 0.0 | +— / -6eecc806-dcf8-47df-bc1d-bc5bc5f07099 |
| Jogador 5 | 4-7 | 253 | BUY | STABILIZE | 72.0 | 7 | 43 | 4 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3491114377975464 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 5 | 4-7 | 254 | SELL | STABILIZE | 72.0 | 7 | 42 | 4 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025998692959547043 | 0.0 | 0.0 | +— / -3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 |
| Jogador 5 | 4-7 | 255 | BUY | STABILIZE | 72.0 | 7 | 43 | 4 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.256759375333786 | 0.0 | 0.0 | +18d25cfb-d559-4efa-b708-c9987987590b / -— |
| Jogador 5 | 4-7 | 256 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 39 | 3 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0006174482987262309 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 257 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 39 | 3 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22201292216777802 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 258 | PASS | STABILIZE | 72.0 | 7 | 39 | 3 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04214285686612129 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 72.0 | 7 | 48 | 4 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09381753206253052 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 72.0 | 7 | 48 | 4 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08079323917627335 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 264 | SELL | STABILIZE | 72.0 | 7 | 48 | 4 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08753333240747452 | 0.0 | 0.0 | +— / -18d25cfb-d559-4efa-b708-c9987987590b |
| Jogador 5 | 5-1 | 265 | BUY | STABILIZE | 72.0 | 7 | 52 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9378108382225037 | 0.0 | 0.0 | +7a48aa2d-a43b-4e49-8230-77f4f2860cb2 / -0f1b15a2-9978-4691-a15e-483ccd03db7f,f5cca112-4fa0-4ee6-a863-20a5d49ab7ef |
| Jogador 5 | 5-1 | 266 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 49 | 4 | 16.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4902971386909485 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 267 | BUY | STABILIZE | 72.0 | 7 | 49 | 4 | 18.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2186068594455719 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -— |
| Jogador 5 | 5-1 | 268 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 46 | 4 | 18.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5511929392814636 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 269 | BUY | STABILIZE | 72.0 | 7 | 46 | 4 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1694476455450058 | 0.0 | 0.0 | +b701c6c1-2e19-44b9-ad6e-e5d64e1d364c / -— |
| Jogador 5 | 5-1 | 270 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 42 | 4 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 272 | SELL | STABILIZE | 72.0 | 7 | 54 | 5 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5780666470527649 | 0.0 | 0.0 | +— / -7a48aa2d-a43b-4e49-8230-77f4f2860cb2 |
| Jogador 5 | 5-2 | 273 | BUY | STABILIZE | 72.0 | 7 | 62 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7898686528205872 | 0.0 | 0.0 | +2f2b455f-7035-4948-9429-612018ae7063 / -— |
| Jogador 5 | 5-2 | 274 | EQUIP_FROM_INVENTORY | STABILIZE | 72.0 | 7 | 61 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09237135946750641 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 275 | EQUIP_FROM_INVENTORY | STABILIZE | 72.0 | 7 | 61 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07314752042293549 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 276 | SELL | STABILIZE | 72.0 | 7 | 61 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030117588117718697 | 0.0 | 0.0 | +— / -a5deb295-89d5-4573-8ace-e370a0718266 |
| Jogador 5 | 5-2 | 277 | BUY | STABILIZE | 72.0 | 7 | 64 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0029945620335638523 | 0.0 | 0.0 | +a899fe97-90e4-4ae3-941c-af3dee48fed3 / -— |
| Jogador 5 | 5-2 | 278 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 61 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 279 | SELL | STABILIZE | 72.0 | 7 | 61 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -a899fe97-90e4-4ae3-941c-af3dee48fed3 |
| Jogador 5 | 5-2 | 280 | BUY | STABILIZE | 72.0 | 7 | 64 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10550375282764435 | 0.0 | 0.0 | +39b89fbe-9520-4eaa-80f9-81e03232c83c / -— |
| Jogador 5 | 5-3 | 282 | SELL | STABILIZE | 57.0 | 7 | 71 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -39b89fbe-9520-4eaa-80f9-81e03232c83c |
| Jogador 5 | 5-3 | 283 | BUY | STABILIZE | 57.0 | 7 | 74 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0655473917722702 | 0.0 | 0.0 | +95eba9e8-10f5-48d5-86de-3d9a446b2e65 / -— |
| Jogador 5 | 5-3 | 284 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 71 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3962894380092621 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 285 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 71 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3786885440349579 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 286 | PASS | STABILIZE | 57.0 | 7 | 71 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10282160341739655 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 292 | SELL | STABILIZE | 57.0 | 7 | 82 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -b701c6c1-2e19-44b9-ad6e-e5d64e1d364c |
| Jogador 5 | 5-4 | 293 | BUY | STABILIZE | 57.0 | 7 | 86 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9464770555496216 | 0.0 | 0.0 | +95a2e19e-619f-4497-ba52-e9bbf06b364f / -— |
| Jogador 5 | 5-4 | 294 | SELL | STABILIZE | 57.0 | 7 | 85 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -9c678a7f-3209-4d1b-addd-385f7d4b89fa |
| Jogador 5 | 5-4 | 295 | BUY | STABILIZE | 57.0 | 7 | 86 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10979103296995163 | 0.0 | 0.0 | +0e5921d4-a056-4f42-951e-93de5f2834bb / -— |
| Jogador 5 | 5-4 | 296 | SELL | STABILIZE | 57.0 | 7 | 83 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -0e5921d4-a056-4f42-951e-93de5f2834bb |
| Jogador 5 | 5-4 | 297 | BUY | STABILIZE | 57.0 | 7 | 86 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11066947877407074 | 0.0 | 0.0 | +babdcded-7f64-4c88-a087-ff2e10b58b8d / -— |
| Jogador 5 | 5-4 | 298 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 83 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09958107769489288 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 299 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 83 | 5 | 24.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4146921932697296 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 300 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 83 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3148898482322693 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 302 | SELL | STABILIZE | 57.0 | 7 | 93 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -babdcded-7f64-4c88-a087-ff2e10b58b8d |
| Jogador 5 | 5-5 | 303 | BUY | STABILIZE | 57.0 | 7 | 96 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24757355451583862 | 0.0 | 0.0 | +e5f61076-ec13-419b-a4e8-d91b9975cfd6 / -— |
| Jogador 5 | 5-5 | 304 | SELL | STABILIZE | 57.0 | 7 | 91 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06233333423733711 | 0.0 | 0.0 | +— / -e5f61076-ec13-419b-a4e8-d91b9975cfd6 |
| Jogador 5 | 5-5 | 305 | BUY | STABILIZE | 57.0 | 7 | 96 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23907415568828583 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 5 | 5-5 | 306 | SELL | STABILIZE | 57.0 | 7 | 93 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07174031436443329 | 0.0 | 0.0 | +— / -0c5adb43-b194-486e-b59c-c0f3b5479d40 |
| Jogador 5 | 5-5 | 307 | BUY | STABILIZE | 57.0 | 7 | 96 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22191622853279114 | 0.0 | 0.0 | +9c07608c-00e1-40f1-9671-6d8bc584a6c9 / -— |
| Jogador 5 | 5-5 | 308 | SELL | STABILIZE | 57.0 | 7 | 93 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050125449895858765 | 0.0 | 0.0 | +— / -9c07608c-00e1-40f1-9671-6d8bc584a6c9 |
| Jogador 5 | 5-5 | 309 | BUY | STABILIZE | 57.0 | 7 | 96 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16440385580062866 | 0.0 | 0.0 | +e978e901-0a52-4f01-ba52-a83fbcc3b439 / -— |
| Jogador 5 | 5-5 | 310 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 93 | 5 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000776410102844 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 312 | SELL | STABILIZE | 39.0 | 7 | 103 | 5 | 32.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3922434449195862 | 0.0 | 0.0 | +— / -bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 5 | 5-6 | 313 | BUY | STABILIZE | 39.0 | 7 | 107 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11193089932203293 | 0.0 | 0.0 | +0a6e3194-ed55-43ad-ac66-31e08ccda7aa / -— |
| Jogador 5 | 5-6 | 314 | SELL | STABILIZE | 39.0 | 7 | 105 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -0a6e3194-ed55-43ad-ac66-31e08ccda7aa |
| Jogador 5 | 5-6 | 315 | BUY | STABILIZE | 39.0 | 7 | 107 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11189905554056168 | 0.0 | 0.0 | +caeaaabc-213a-4018-97f3-8797a0711863 / -— |
| Jogador 5 | 5-6 | 316 | SELL | STABILIZE | 39.0 | 7 | 105 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -caeaaabc-213a-4018-97f3-8797a0711863 |
| Jogador 5 | 5-6 | 317 | BUY | STABILIZE | 39.0 | 7 | 107 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0843685120344162 | 0.0 | 0.0 | +3eccad10-cc50-4695-852e-0809356dd33b / -— |
| Jogador 5 | 5-6 | 318 | SELL | STABILIZE | 39.0 | 7 | 106 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007572358939796686 | 0.0 | 0.0 | +— / -3eccad10-cc50-4695-852e-0809356dd33b |
| Jogador 5 | 5-6 | 319 | BUY | STABILIZE | 39.0 | 7 | 107 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1653885841369629 | 0.0 | 0.0 | +3ae84928-bc2a-4c1e-8663-b7ad05da4501 / -— |
| Jogador 5 | 5-6 | 320 | SELL | STABILIZE | 39.0 | 7 | 105 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -3ae84928-bc2a-4c1e-8663-b7ad05da4501 |
| Jogador 5 | 5-7 | 322 | BUY | ALL_IN | 25.0 | 7 | 118 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6156895160675049 | 0.0 | 0.0 | +40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b / -— |
| Jogador 5 | 5-7 | 323 | SELL | ALL_IN | 25.0 | 7 | 116 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5310210585594177 | 0.0 | 0.0 | +— / -40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b |
| Jogador 5 | 5-7 | 324 | BUY | ALL_IN | 25.0 | 7 | 118 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27829959988594055 | 0.0 | 0.0 | +7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 / -— |
| Jogador 5 | 5-7 | 325 | SELL | ALL_IN | 25.0 | 7 | 115 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 |
| Jogador 5 | 5-7 | 326 | BUY | ALL_IN | 25.0 | 7 | 118 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2783035337924957 | 0.0 | 0.0 | +b58c0c0e-9c6f-4977-91d1-177b7113c439 / -— |
| Jogador 5 | 5-7 | 327 | SELL | ALL_IN | 25.0 | 7 | 115 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -b58c0c0e-9c6f-4977-91d1-177b7113c439 |
| Jogador 5 | 5-7 | 328 | BUY | ALL_IN | 25.0 | 7 | 118 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21256425976753235 | 0.0 | 0.0 | +c2bf43be-e6e1-47ed-bcb4-606e37f26671 / -— |
| Jogador 5 | 5-7 | 329 | SELL | ALL_IN | 25.0 | 7 | 116 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0302069541066885 | 0.0 | 0.0 | +— / -c2bf43be-e6e1-47ed-bcb4-606e37f26671 |
| Jogador 5 | 5-7 | 330 | BUY | ALL_IN | 25.0 | 7 | 118 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1614980697631836 | 0.0 | 0.0 | +d58ebcea-d18b-42f8-a6ca-984d15656662 / -— |
| Jogador 5 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ALL_IN | 25.0 | 7 | 128 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08789557218551636 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 333 | SELL | ALL_IN | 25.0 | 7 | 128 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -d58ebcea-d18b-42f8-a6ca-984d15656662 |
| Jogador 5 | 6-1 | 334 | BUY | ALL_IN | 25.0 | 7 | 129 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06688293069601059 | 0.0 | 0.0 | +7d8564c6-8151-4e04-b028-2121cb064215 / -— |
| Jogador 5 | 6-1 | 335 | SELL | ALL_IN | 25.0 | 7 | 125 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00157662364654243 | 0.0 | 0.0 | +— / -7d8564c6-8151-4e04-b028-2121cb064215 |
| Jogador 5 | 6-1 | 336 | BUY | ALL_IN | 25.0 | 7 | 129 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1414724737405777 | 0.0 | 0.0 | +c93990ff-0a6f-46bc-8fc1-12623d55abc1 / -— |
| Jogador 5 | 6-1 | 337 | SELL | ALL_IN | 25.0 | 7 | 127 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -c93990ff-0a6f-46bc-8fc1-12623d55abc1 |
| Jogador 5 | 6-1 | 338 | BUY | ALL_IN | 25.0 | 7 | 129 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14148922264575958 | 0.0 | 0.0 | +1ad1f705-7e6b-4c1f-811c-2863dbf2db9e / -— |
| Jogador 5 | 6-1 | 339 | SELL | ALL_IN | 25.0 | 7 | 127 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -1ad1f705-7e6b-4c1f-811c-2863dbf2db9e |
| Jogador 5 | 6-1 | 340 | BUY | ALL_IN | 25.0 | 7 | 129 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1303219199180603 | 0.0 | 0.0 | +2a2b613e-8850-4c70-ab66-bc18356178e8 / -— |
| Jogador 5 | 6-2 | 342 | SELL | ALL_IN | 4.0 | 8 | 139 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010333333164453506 | 0.0 | 0.0 | +— / -2a2b613e-8850-4c70-ab66-bc18356178e8 |
| Jogador 5 | 6-2 | 343 | BUY | ALL_IN | 4.0 | 8 | 140 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1113543510437012 | 0.0 | 0.0 | +9af00d66-f862-45b7-98d4-93fbd69fedba / -1d7b6420-388f-4cb1-b25c-2e5a3dfec742,c7841e00-91da-410b-b00f-62f4bf32f666 |
| Jogador 5 | 6-2 | 344 | BUY | ALL_IN | 4.0 | 8 | 137 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2782849967479706 | 0.0 | 0.0 | +b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 / -— |
| Jogador 5 | 6-2 | 345 | BUY | ALL_IN | 4.0 | 8 | 134 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16314026713371277 | 0.0 | 0.0 | +bfe7ca8a-6e89-4673-b142-262e012398a9 / -— |
| Jogador 5 | 6-2 | 346 | SELL | ALL_IN | 4.0 | 8 | 130 | 5 | 32.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7391999959945679 | 0.0 | 0.0 | +— / -9af00d66-f862-45b7-98d4-93fbd69fedba |
| Jogador 5 | 6-2 | 347 | BUY | ALL_IN | 4.0 | 8 | 138 | 5 | 32.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14454145729541779 | 0.0 | 0.0 | +17279599-f3fc-4cf2-874f-da62a23ac238 / -— |
| Jogador 5 | 6-2 | 348 | MOVE_BENCH | ALL_IN | 4.0 | 8 | 134 | 5 | 32.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5974586009979248 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 349 | BUY | ALL_IN | 4.0 | 8 | 134 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20042863488197327 | 0.0 | 0.0 | +85d35881-ba70-4310-8d5f-bae796309eed / -— |
| Jogador 5 | 6-2 | 350 | MOVE_BOARD | ALL_IN | 4.0 | 8 | 133 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 352 | SELL | ALL_IN | 4.0 | 8 | 144 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01133333332836628 | 0.0 | 0.0 | +— / -85d35881-ba70-4310-8d5f-bae796309eed |
| Jogador 5 | 6-3 | 353 | BUY | ALL_IN | 4.0 | 8 | 145 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5006996393203735 | 0.0 | 0.0 | +425a58b3-d906-4381-9afc-00f9852c9982 / -— |
| Jogador 5 | 6-3 | 354 | SELL | ALL_IN | 4.0 | 8 | 142 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -17279599-f3fc-4cf2-874f-da62a23ac238 |
| Jogador 5 | 6-3 | 355 | BUY | ALL_IN | 4.0 | 8 | 146 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15663541853427887 | 0.0 | 0.0 | +2ac6d717-87f1-4421-929e-1934a9317e72 / -— |
| Jogador 5 | 6-3 | 356 | SELL | ALL_IN | 4.0 | 8 | 141 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 |
| Jogador 5 | 6-3 | 357 | BUY | ALL_IN | 4.0 | 8 | 144 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11975684762001038 | 0.0 | 0.0 | +3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 / -— |
| Jogador 5 | 6-3 | 358 | SELL | ALL_IN | 4.0 | 8 | 139 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01119999960064888 | 0.0 | 0.0 | +— / -3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 |
| Jogador 5 | 6-3 | 359 | BUY | ALL_IN | 4.0 | 8 | 144 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1117980033159256 | 0.0 | 0.0 | +ae9da355-52b7-402c-be6e-41fa1148a550 / -— |
| Jogador 5 | 6-3 | 360 | MOVE_BOARD | ALL_IN | 4.0 | 8 | 142 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 362 | SELL | ALL_IN | 4.0 | 8 | 153 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -ae9da355-52b7-402c-be6e-41fa1148a550 |
| Jogador 5 | 6-4 | 363 | BUY | ALL_IN | 4.0 | 8 | 155 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13560651242733002 | 0.0 | 0.0 | +4321582a-0b45-4666-a119-7b49e92d012a / -— |
| Jogador 5 | 6-4 | 364 | SELL | ALL_IN | 4.0 | 8 | 151 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -4321582a-0b45-4666-a119-7b49e92d012a |
| Jogador 5 | 6-4 | 365 | BUY | ALL_IN | 4.0 | 8 | 155 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10197868943214417 | 0.0 | 0.0 | +04ebf9b8-7683-4270-b98a-a3bfb342dcf8 / -— |
| Jogador 5 | 6-4 | 366 | SELL | ALL_IN | 4.0 | 8 | 152 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -04ebf9b8-7683-4270-b98a-a3bfb342dcf8 |
| Jogador 5 | 6-4 | 367 | BUY | ALL_IN | 4.0 | 8 | 155 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048021793365478516 | 0.0 | 0.0 | +0f186e00-6f9d-4a22-a1ed-5ccd1b14613d / -— |
| Jogador 5 | 6-4 | 368 | SELL | ALL_IN | 4.0 | 8 | 153 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -0f186e00-6f9d-4a22-a1ed-5ccd1b14613d |
| Jogador 5 | 6-4 | 369 | BUY | ALL_IN | 4.0 | 8 | 155 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2309236228466034 | 0.0 | 0.0 | +d47034a1-8b51-4b82-b1b4-5f2aee8f959a / -— |
| Jogador 5 | 6-4 | 370 | SELL | ALL_IN | 4.0 | 8 | 152 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -d47034a1-8b51-4b82-b1b4-5f2aee8f959a |
| Jogador 5 | 6-5 | 372 | BUY | ALL_IN | 4.0 | 8 | 166 | 5 | 34.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1111924648284912 | 0.0 | 0.0 | +c71adf7d-8d74-439d-8863-dac0f4f20cd1 / -17d5d3f2-999d-4788-852b-bda84adb4350,8995f621-b355-44ec-816e-797184bdc266 |
| Jogador 5 | 6-5 | 373 | BUY | ALL_IN | 4.0 | 8 | 163 | 5 | 28.0 | Espinhos Negros/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6052041053771973 | 0.0 | 0.0 | +f1ece814-0986-421f-b5df-0b457ebaa484 / -— |
| Jogador 5 | 6-5 | 374 | SELL | ALL_IN | 4.0 | 8 | 160 | 5 | 28.0 | Espinhos Negros/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7391999959945679 | 0.0 | 0.0 | +— / -c71adf7d-8d74-439d-8863-dac0f4f20cd1 |
| Jogador 5 | 6-5 | 375 | BUY | ALL_IN | 4.0 | 8 | 168 | 5 | 28.0 | Espinhos Negros/DA_18_Maokai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6912596821784973 | 0.0 | 0.0 | +5184a53b-fca3-448c-b5ab-7daa37b0c259 / -— |
| Jogador 5 | 6-5 | 376 | SELL | ALL_IN | 4.0 | 8 | 166 | 5 | 28.0 | Espinhos Negros/DA_18_Maokai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.612614631652832 | 0.0 | 0.0 | +— / -5184a53b-fca3-448c-b5ab-7daa37b0c259 |
| Jogador 5 | 6-5 | 377 | BUY | ALL_IN | 4.0 | 8 | 168 | 5 | 28.0 | Espinhos Negros/DA_18_Maokai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027006888762116432 | 0.0 | 0.0 | +e1be174a-f112-4e1b-8bf6-738af52f27e8 / -— |
| Jogador 5 | 6-5 | 378 | SELL | ALL_IN | 4.0 | 8 | 165 | 5 | 28.0 | Espinhos Negros/DA_18_Maokai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004399999976158142 | 0.0 | 0.0 | +— / -e1be174a-f112-4e1b-8bf6-738af52f27e8 |
| Jogador 5 | 6-5 | 379 | BUY | ALL_IN | 4.0 | 8 | 168 | 5 | 28.0 | Espinhos Negros/DA_18_Maokai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23951780796051025 | 0.0 | 0.0 | +87726d3e-4b0d-41ae-bf43-893d4092bd5b / -— |
| Jogador 5 | 6-5 | 380 | SELL | ALL_IN | 4.0 | 8 | 167 | 5 | 28.0 | Espinhos Negros/DA_18_Maokai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -87726d3e-4b0d-41ae-bf43-893d4092bd5b |
| Jogador 5 | 6-6 | 382 | BUY | ALL_IN | 4.0 | 8 | 179 | 5 | 28.0 | Espinhos Negros/DA_18_Maokai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7332097291946411 | 0.0 | 0.0 | +158c7931-f8db-44bd-a279-53dd6e59b352 / -— |
| Jogador 5 | 6-6 | 383 | SELL | ALL_IN | 4.0 | 8 | 175 | 5 | 28.0 | Espinhos Negros/DA_18_Maokai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5906999707221985 | 0.0 | 0.0 | +— / -f1ece814-0986-421f-b5df-0b457ebaa484 |
| Jogador 5 | 6-6 | 384 | BUY | ALL_IN | 4.0 | 8 | 178 | 5 | 28.0 | Espinhos Negros/DA_18_Maokai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0689038038253784 | 0.0 | 0.0 | +13169f05-0cd0-4012-89a6-7b47246b475e / -158c7931-f8db-44bd-a279-53dd6e59b352,bfe7ca8a-6e89-4673-b142-262e012398a9 |
| Jogador 5 | 6-6 | 385 | BUY | ALL_IN | 4.0 | 8 | 174 | 5 | 28.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49116891622543335 | 0.0 | 0.0 | +335c4988-791a-4579-a473-f387b986806c / -— |
| Jogador 5 | 6-6 | 386 | BUY | ALL_IN | 4.0 | 8 | 171 | 5 | 28.0 | Espinhos Negros/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23453256487846375 | 0.0 | 0.0 | +40263a7a-96e9-4752-b149-8235892508e0 / -— |
| Jogador 5 | 6-6 | 387 | SELL | ALL_IN | 4.0 | 8 | 167 | 5 | 28.0 | Espinhos Negros/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5971888899803162 | 0.0 | 0.0 | +— / -13169f05-0cd0-4012-89a6-7b47246b475e |
| Jogador 5 | 6-6 | 388 | MOVE_BENCH | ALL_IN | 4.0 | 8 | 178 | 5 | 28.0 | Espinhos Negros/DA_18_Maokai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5985002517700195 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 389 | BUY | ALL_IN | 4.0 | 8 | 178 | 5 | 34.0 | Espinhos Negros/DA_18_Maokai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10440581291913986 | 0.0 | 0.0 | +94e47e85-54f4-4546-af6a-3700e3c325a8 / -— |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | -0.15334774553775787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Sentry | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17399217188358307 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2196885347366333 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0373011827468872 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039901405572891235 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012773334980010986 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011599136516451836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 31 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5747041702270508 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0239715576171875 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 43 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12833119928836823 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15204384922981262 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2898862063884735 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 56 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 57 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26361411809921265 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 63 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24760934710502625 | 0.0 | 0.0 | +048e9074-b134-49ed-a105-88dca63d1aa3 / -— |
| Jogador 6 | 2-2 | 64 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -6a01f661-884f-4c25-9dbe-384a6fe3a5e6 |
| Jogador 6 | 2-2 | 65 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07944674044847488 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 66 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 72 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2894051969051361 | 0.0 | 0.0 | +b1ecd1fa-793c-40ad-a9e3-9d35d5030339 / -— |
| Jogador 6 | 2-3 | 73 | BUY | STABILIZE | 89.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1798442304134369 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 74 | BUY | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23805347084999084 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 75 | SELL | STABILIZE | 89.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14511153101921082 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-3 | 76 | SELL | STABILIZE | 89.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15191352367401123 | 0.0 | 0.0 | +— / -b1ecd1fa-793c-40ad-a9e3-9d35d5030339 |
| Jogador 6 | 2-3 | 77 | PASS | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 82 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1828940510749817 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 83 | BUY | STABILIZE | 83.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24063338339328766 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 84 | BUY | STABILIZE | 83.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8069520592689514 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 85 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 86 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013266666792333126 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-4 | 87 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10965367406606674 | 0.0 | 0.0 | +— / -048e9074-b134-49ed-a105-88dca63d1aa3 |
| Jogador 6 | 2-4 | 88 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 89 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14378099143505096 | 0.0 | 0.0 | +— / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 |
| Jogador 6 | 2-4 | 90 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14377939701080322 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-5 | 92 | BUY | STABILIZE | 83.0 | 5 | 10 | 1 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8596822023391724 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 93 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2884290814399719 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 94 | BUY_XP | STABILIZE | 83.0 | 5 | 7 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 95 | SELL | STABILIZE | 83.0 | 5 | 3 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45227327942848206 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-5 | 96 | BUY_XP | STABILIZE | 83.0 | 5 | 5 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 97 | SELL | STABILIZE | 83.0 | 5 | 1 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4931741952896118 | 0.0 | 0.0 | +— / -a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 2-5 | 98 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 0 | 0 | 8.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2040659636259079 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 100 | SELL | STABILIZE | 83.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-6 | 102 | BUY | STABILIZE | 76.0 | 6 | 9 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3035968244075775 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 103 | BUY | STABILIZE | 76.0 | 6 | 6 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3205978274345398 | 0.0 | 0.0 | +f5511428-5be8-475d-949c-1d840a0aed4d / -— |
| Jogador 6 | 2-6 | 104 | BUY_XP | STABILIZE | 76.0 | 6 | 5 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 105 | SELL | STABILIZE | 76.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16131465137004852 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 2-6 | 106 | BUY_XP | STABILIZE | 76.0 | 6 | 4 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 107 | SELL | STABILIZE | 76.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.476666659116745 | 0.0 | 0.0 | +— / -f5511428-5be8-475d-949c-1d840a0aed4d |
| Jogador 6 | 2-6 | 108 | SELL | STABILIZE | 76.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-6 | 109 | BUY | STABILIZE | 76.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32842352986335754 | 0.0 | 0.0 | +53bbd605-d60b-4555-b5e8-29f1cfbb83b4 / -— |
| Jogador 6 | 2-6 | 110 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3656124472618103 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 112 | BUY | STABILIZE | 69.0 | 6 | 7 | 0 | 14.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3172356188297272 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 113 | BUY | STABILIZE | 69.0 | 6 | 4 | 0 | 14.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22876891493797302 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 2-7 | 114 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 1 | 0 | 14.0 | Feérico/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0006979470490477979 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 115 | SELL | STABILIZE | 69.0 | 6 | 1 | 0 | 14.0 | Feérico/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12424468249082565 | 0.0 | 0.0 | +— / -9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 2-7 | 116 | SELL | STABILIZE | 69.0 | 6 | 4 | 0 | 14.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1610238254070282 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 2-7 | 117 | BUY | STABILIZE | 69.0 | 6 | 7 | 0 | 14.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23924864828586578 | 0.0 | 0.0 | +dc83202b-476c-4438-90aa-a615b764b7e4 / -— |
| Jogador 6 | 2-7 | 118 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 6 | 0 | 14.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03404929116368294 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 119 | BUY | STABILIZE | 69.0 | 6 | 6 | 0 | 14.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20262658596038818 | 0.0 | 0.0 | +eafa585a-9474-415b-b46b-d3ce86f4a066 / -— |
| Jogador 6 | 2-7 | 120 | BUY_XP | STABILIZE | 69.0 | 6 | 4 | 0 | 14.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 122 | BUY | STABILIZE | 69.0 | 6 | 7 | 0 | 14.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14370743930339813 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 69.0 | 6 | 4 | 0 | 14.0 | Fumegante/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18733781576156616 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 124 | BUY | STABILIZE | 69.0 | 6 | 4 | 0 | 14.0 | Fumegante/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08503413945436478 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 0 | 0 | 14.0 | Fumegante/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3305019438266754 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 126 | SELL | STABILIZE | 69.0 | 6 | 0 | 0 | 16.0 | Fumegante/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09566666930913925 | 0.0 | 0.0 | +— / -a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 |
| Jogador 6 | 3-1 | 127 | BUY | STABILIZE | 69.0 | 6 | 3 | 0 | 16.0 | Fumegante/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013845140347257257 | 0.0 | 0.0 | +91f05e8c-f467-4f22-9cb0-c814ffa93198 / -— |
| Jogador 6 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 1 | 0 | 16.0 | Fumegante/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07421156764030457 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 129 | SELL | STABILIZE | 69.0 | 6 | 1 | 0 | 16.0 | Fumegante/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09353887289762497 | 0.0 | 0.0 | +— / -91f05e8c-f467-4f22-9cb0-c814ffa93198 |
| Jogador 6 | 3-1 | 130 | SELL | STABILIZE | 69.0 | 6 | 3 | 0 | 16.0 | Fumegante/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017866667360067368 | 0.0 | 0.0 | +— / -4eedd873-e4ec-41e5-9f5e-48e443e80f86 |
| Jogador 6 | 3-2 | 132 | BUY | STABILIZE | 69.0 | 6 | 13 | 1 | 16.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8359752297401428 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -18934be2-4988-4f62-9f62-07ba151231f2,53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 3-2 | 133 | BUY | STABILIZE | 69.0 | 6 | 12 | 1 | 16.0 | Fumegante/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8278694152832031 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 11 | 1 | 12.0 | Fumegante/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1810385286808014 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 135 | SELL | STABILIZE | 69.0 | 6 | 11 | 1 | 14.0 | Fumegante/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4199768304824829 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 3-2 | 136 | EQUIP_FROM_INVENTORY | STABILIZE | 69.0 | 6 | 14 | 1 | 14.0 | Fumegante/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15578892827033997 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 137 | EQUIP_FROM_INVENTORY | STABILIZE | 69.0 | 6 | 14 | 1 | 14.0 | Fumegante/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.18792887032032013 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 138 | EQUIP_FROM_INVENTORY | STABILIZE | 69.0 | 6 | 14 | 1 | 14.0 | Fumegante/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14461596310138702 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 139 | BUY_XP | STABILIZE | 69.0 | 6 | 14 | 1 | 14.0 | Fumegante/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 140 | BUY_XP | STABILIZE | 69.0 | 6 | 10 | 1 | 14.0 | Fumegante/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 142 | BUY | STABILIZE | 60.0 | 6 | 11 | 1 | 14.0 | Fumegante/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11795728653669357 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 143 | SELL | STABILIZE | 60.0 | 6 | 8 | 0 | 14.0 | Fumegante/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5490000247955322 | 0.0 | 0.0 | +— / -e29364db-c484-4e4d-954d-7f4940131ffc |
| Jogador 6 | 3-3 | 144 | BUY | STABILIZE | 60.0 | 6 | 11 | 1 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3736010491847992 | 0.0 | 0.0 | +50f9a30c-27db-4ed0-804e-548f87950b17 / -— |
| Jogador 6 | 3-3 | 145 | BUY_XP | STABILIZE | 60.0 | 6 | 8 | 0 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02827499993145466 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 146 | MOVE_BENCH | STABILIZE | 60.0 | 7 | 4 | 0 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0821150690317154 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 147 | BUY | STABILIZE | 60.0 | 7 | 4 | 0 | 20.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025138184428215027 | 0.0 | 0.0 | +31c30451-3999-47b1-8bcf-77e137137b2a / -— |
| Jogador 6 | 3-3 | 148 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 2 | 0 | 20.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001194948679767549 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 2 | 0 | 20.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28300100564956665 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 150 | MOVE_BENCH | STABILIZE | 60.0 | 7 | 2 | 0 | 20.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4201287031173706 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 152 | BUY | STABILIZE | 50.0 | 7 | 8 | 0 | 22.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09419075399637222 | 0.0 | 0.0 | +2ed895f2-1e83-426c-88fc-b9fb6403835d / -— |
| Jogador 6 | 3-4 | 153 | BUY | STABILIZE | 50.0 | 7 | 4 | 0 | 22.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12342699617147446 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 6 | 3-4 | 154 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 155 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014762654900550842 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 156 | PASS | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 162 | BUY | STABILIZE | 50.0 | 7 | 7 | 0 | 22.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2835802733898163 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 163 | BUY | STABILIZE | 50.0 | 7 | 4 | 0 | 22.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3146786093711853 | 0.0 | 0.0 | +06db3a99-d008-406a-ac86-30884335d7c2 / -— |
| Jogador 6 | 3-5 | 164 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014700951054692268 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 166 | PASS | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 172 | BUY | STABILIZE | 50.0 | 7 | 7 | 0 | 22.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6268405318260193 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 173 | BUY | STABILIZE | 50.0 | 7 | 4 | 0 | 22.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7471848130226135 | 0.0 | 0.0 | +ab472080-6e4b-4b75-b37d-cf10da9a5a0d / -333cdd27-0114-4d36-8ffa-e79b0f43b8e8,cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 3-6 | 174 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0129470843821764 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015537590719759464 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 176 | BUY | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055878933519124985 | 0.0 | 0.0 | +171724e7-58bd-404f-820b-2bb32c5c193e / -— |
| Jogador 6 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 0 | 0 | 22.0 | Fumegante/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008505337871611118 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 0 | 0 | 22.0 | Fumegante/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 179 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 0 | 0 | 22.0 | Fumegante/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08430851250886917 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 180 | PASS | STABILIZE | 50.0 | 7 | 0 | 0 | 22.0 | Fumegante/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 182 | BUY | STABILIZE | 50.0 | 7 | 7 | 0 | 22.0 | Fumegante/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5990233421325684 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 6 | 3-7 | 183 | BUY | STABILIZE | 50.0 | 7 | 3 | 0 | 22.0 | Fumegante/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43677830696105957 | 0.0 | 0.0 | +604a85af-ff68-41a7-8795-73fdc7723c0e / -— |
| Jogador 6 | 3-7 | 184 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0678802877664566 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043468017131090164 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011849295347929 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 187 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 188 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 189 | PASS | STABILIZE | 50.0 | 7 | 1 | 0 | 22.0 | Fumegante/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 50.0 | 7 | 7 | 0 | 22.0 | Fumegante/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1336543709039688 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 50.0 | 7 | 7 | 0 | 22.0 | Fumegante/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1312219798564911 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 194 | SELL | STABILIZE | 50.0 | 7 | 7 | 0 | 22.0 | Fumegante/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0031666667200624943 | 0.0 | 0.0 | +— / -ab472080-6e4b-4b75-b37d-cf10da9a5a0d |
| Jogador 6 | 4-1 | 195 | BUY | STABILIZE | 50.0 | 7 | 15 | 1 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.582513153553009 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -06db3a99-d008-406a-ac86-30884335d7c2,50f9a30c-27db-4ed0-804e-548f87950b17 |
| Jogador 6 | 4-1 | 196 | BUY | STABILIZE | 50.0 | 7 | 12 | 1 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06562432646751404 | 0.0 | 0.0 | +a8a8381a-f3a8-45ec-9106-293d73fca0c8 / -— |
| Jogador 6 | 4-1 | 197 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 9 | 0 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21990732848644257 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 9 | 0 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20684440433979034 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 9 | 0 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014583351090550423 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 9 | 0 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 202 | BUY | STABILIZE | 38.0 | 7 | 14 | 1 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11300992220640182 | 0.0 | 0.0 | +6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb / -— |
| Jogador 6 | 4-2 | 203 | SELL | STABILIZE | 38.0 | 7 | 11 | 1 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03312145173549652 | 0.0 | 0.0 | +— / -f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 6 | 4-2 | 204 | BUY | STABILIZE | 38.0 | 7 | 19 | 1 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18430744111537933 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 6 | 4-2 | 205 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 15 | 1 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00022928098042029887 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 15 | 1 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 207 | PASS | STABILIZE | 38.0 | 7 | 15 | 1 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027074074372649193 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 212 | SELL | ALL_IN | 25.0 | 7 | 22 | 2 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014633333310484886 | 0.0 | 0.0 | +— / -171724e7-58bd-404f-820b-2bb32c5c193e |
| Jogador 6 | 4-3 | 213 | BUY | ALL_IN | 25.0 | 7 | 23 | 2 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8572351336479187 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 6 | 4-3 | 214 | SELL | ALL_IN | 25.0 | 7 | 21 | 2 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb |
| Jogador 6 | 4-3 | 215 | BUY | ALL_IN | 25.0 | 7 | 24 | 2 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1243244856595993 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 6 | 4-3 | 216 | REROLL | ALL_IN | 25.0 | 7 | 20 | 2 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 217 | SELL | ALL_IN | 25.0 | 7 | 18 | 1 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036760978400707245 | 0.0 | 0.0 | +— / -a8a8381a-f3a8-45ec-9106-293d73fca0c8 |
| Jogador 6 | 4-3 | 218 | BUY | ALL_IN | 25.0 | 7 | 21 | 2 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33954712748527527 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 6 | 4-3 | 219 | SELL | ALL_IN | 25.0 | 7 | 20 | 2 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -86530a1f-5325-45fa-bf43-86419ccfda54 |
| Jogador 6 | 4-3 | 220 | BUY | ALL_IN | 25.0 | 7 | 24 | 2 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010970459319651127 | 0.0 | 0.0 | +b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 / -— |
| Jogador 6 | 4-4 | 222 | SELL | ALL_IN | 25.0 | 7 | 29 | 2 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05675581842660904 | 0.0 | 0.0 | +— / -b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 |
| Jogador 6 | 4-4 | 223 | BUY | ALL_IN | 25.0 | 7 | 32 | 3 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8836521506309509 | 0.0 | 0.0 | +d53646ff-bb49-4f82-b761-faa4657f01cc / -— |
| Jogador 6 | 4-4 | 224 | SELL | ALL_IN | 25.0 | 7 | 31 | 3 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030326375737786293 | 0.0 | 0.0 | +— / -1fa69553-5270-4459-986b-600f748711b7 |
| Jogador 6 | 4-4 | 225 | BUY | ALL_IN | 25.0 | 7 | 35 | 3 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00019386113854125142 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 6 | 4-4 | 226 | MOVE_BOARD | ALL_IN | 25.0 | 7 | 33 | 3 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 227 | MOVE_BOARD | ALL_IN | 25.0 | 7 | 33 | 3 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0147691136226058 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 228 | PASS | ALL_IN | 25.0 | 7 | 33 | 3 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3851163983345032 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 232 | SELL | ALL_IN | 25.0 | 7 | 41 | 4 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -d175e09c-3ed6-4fb3-8c97-0c167862e29e |
| Jogador 6 | 4-5 | 233 | BUY | ALL_IN | 25.0 | 7 | 43 | 4 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7539578676223755 | 0.0 | 0.0 | +f3e882b5-333e-44e3-ae82-cacacc8b1137 / -31c30451-3999-47b1-8bcf-77e137137b2a,604a85af-ff68-41a7-8795-73fdc7723c0e |
| Jogador 6 | 4-5 | 234 | BUY | ALL_IN | 25.0 | 7 | 41 | 4 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0827852338552475 | 0.0 | 0.0 | +cba152f4-af54-4d82-a35d-67aa165174be / -— |
| Jogador 6 | 4-5 | 235 | BUY | ALL_IN | 25.0 | 7 | 37 | 3 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016504187136888504 | 0.0 | 0.0 | +20a4e507-09d3-42d7-b748-4dde14e82ddf / -— |
| Jogador 6 | 4-5 | 236 | REROLL | ALL_IN | 25.0 | 7 | 35 | 3 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 237 | SELL | ALL_IN | 25.0 | 7 | 33 | 3 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05753333494067192 | 0.0 | 0.0 | +— / -f3e882b5-333e-44e3-ae82-cacacc8b1137 |
| Jogador 6 | 4-5 | 238 | BUY | ALL_IN | 25.0 | 7 | 38 | 3 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8578662872314453 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 6 | 4-5 | 239 | SELL | ALL_IN | 25.0 | 7 | 35 | 3 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009305602870881557 | 0.0 | 0.0 | +— / -20a4e507-09d3-42d7-b748-4dde14e82ddf |
| Jogador 6 | 4-5 | 240 | BUY | ALL_IN | 25.0 | 7 | 37 | 3 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009436899796128273 | 0.0 | 0.0 | +3bfc4626-3226-44b6-a401-ff9c18761448 / -— |
| Jogador 6 | 4-6 | 242 | SELL | ALL_IN | 12.0 | 7 | 43 | 4 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00839214213192463 | 0.0 | 0.0 | +— / -3bfc4626-3226-44b6-a401-ff9c18761448 |
| Jogador 6 | 4-6 | 243 | BUY | ALL_IN | 12.0 | 7 | 45 | 4 | 22.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0086915493011475 | 0.0 | 0.0 | +6722b147-c2a7-4fd0-a943-5036adb3e3a1 / -53bbd605-d60b-4555-b5e8-29f1cfbb83b4,e85c6ab6-f36c-40b4-88e2-b7380b4c9652 |
| Jogador 6 | 4-6 | 244 | BUY | ALL_IN | 12.0 | 7 | 43 | 4 | 18.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3772090971469879 | 0.0 | 0.0 | +755060be-13bb-4686-9ee9-e53fef2d75b2 / -— |
| Jogador 6 | 4-6 | 245 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 39 | 3 | 18.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40014129877090454 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 246 | BUY | ALL_IN | 12.0 | 7 | 39 | 3 | 26.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23247666656970978 | 0.0 | 0.0 | +1388df2e-8cb4-4e29-8b30-776c29406917 / -— |
| Jogador 6 | 4-6 | 247 | SELL | ALL_IN | 12.0 | 7 | 36 | 3 | 26.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6164000034332275 | 0.0 | 0.0 | +— / -6722b147-c2a7-4fd0-a943-5036adb3e3a1 |
| Jogador 6 | 4-6 | 248 | BUY | ALL_IN | 12.0 | 7 | 41 | 4 | 26.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24011552333831787 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 6 | 4-6 | 249 | SELL | ALL_IN | 12.0 | 7 | 38 | 3 | 26.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08910000324249268 | 0.0 | 0.0 | +— / -04520fe5-4449-4632-b275-e5e28d642007 |
| Jogador 6 | 4-6 | 250 | BUY | ALL_IN | 12.0 | 7 | 41 | 4 | 26.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25872746109962463 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -— |
| Jogador 6 | 4-7 | 252 | SELL | ALL_IN | 12.0 | 7 | 47 | 4 | 26.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09430000185966492 | 0.0 | 0.0 | +— / -3b934078-806c-40f0-b102-e9131220f70e |
| Jogador 6 | 4-7 | 253 | BUY | ALL_IN | 12.0 | 7 | 50 | 5 | 26.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14006467163562775 | 0.0 | 0.0 | +e5f38fbd-826a-4067-a33f-86cf7eb98f30 / -— |
| Jogador 6 | 4-7 | 254 | SELL | ALL_IN | 12.0 | 7 | 47 | 4 | 26.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050966665148735046 | 0.0 | 0.0 | +— / -e5f38fbd-826a-4067-a33f-86cf7eb98f30 |
| Jogador 6 | 4-7 | 255 | BUY | ALL_IN | 12.0 | 7 | 50 | 5 | 26.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028568318113684654 | 0.0 | 0.0 | +98b600a1-736b-437d-a69e-8a7f7235d9c3 / -— |
| Jogador 6 | 4-7 | 256 | SELL | ALL_IN | 12.0 | 7 | 48 | 4 | 26.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07167588174343109 | 0.0 | 0.0 | +— / -98b600a1-736b-437d-a69e-8a7f7235d9c3 |
| Jogador 6 | 4-7 | 257 | BUY | ALL_IN | 12.0 | 7 | 50 | 5 | 26.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029926016926765442 | 0.0 | 0.0 | +9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 / -— |
| Jogador 6 | 4-7 | 258 | SELL | ALL_IN | 12.0 | 7 | 48 | 4 | 26.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08467590063810349 | 0.0 | 0.0 | +— / -9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 |
| Jogador 6 | 4-7 | 259 | BUY | ALL_IN | 12.0 | 7 | 50 | 5 | 26.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21031294763088226 | 0.0 | 0.0 | +55cd39c0-65d5-410e-917e-501f584115fa / -— |
| Jogador 6 | 4-7 | 260 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 49 | 4 | 26.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006124112755060196 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 12.0 | 7 | 58 | 5 | 26.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09654881805181503 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 12.0 | 7 | 58 | 5 | 26.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10284899920225143 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 264 | SELL | ALL_IN | 12.0 | 7 | 58 | 5 | 26.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -55cd39c0-65d5-410e-917e-501f584115fa |
| Jogador 6 | 5-1 | 265 | BUY | ALL_IN | 12.0 | 7 | 59 | 5 | 26.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0580812692642212 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -3cb4d077-df9a-4fd2-9a68-7301aff1b657,3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 5-1 | 266 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 58 | 5 | 22.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18317800760269165 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 267 | BUY | ALL_IN | 12.0 | 7 | 58 | 5 | 28.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06247861683368683 | 0.0 | 0.0 | +c7762d7d-bcfa-4694-a3fc-038d7242207f / -— |
| Jogador 6 | 5-1 | 268 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 55 | 5 | 28.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40118372440338135 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 269 | BUY | ALL_IN | 12.0 | 7 | 55 | 5 | 34.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15912313759326935 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -— |
| Jogador 6 | 5-1 | 270 | SELL | ALL_IN | 12.0 | 7 | 52 | 5 | 34.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7103000283241272 | 0.0 | 0.0 | +— / -4688e6f1-26c5-402d-8d27-0f9bce3a9681 |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589178562164307 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2799173593521118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.143971249461174 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 21 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012334865517914295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40434256196022034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0484532117843628 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23116838932037354 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004352054558694363 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005867671221494675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 32 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.036877989768982 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24497109651565552 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007539904909208417 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1995791792869568 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 46 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 53 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8279920220375061 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19963383674621582 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24531260132789612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30116716027259827 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 57 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475666522979736 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15446913242340088 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 65 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17887981235980988 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04722195118665695 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 68 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-2 | 69 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11032035946846008 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 70 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.3236997425556183 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 72 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.0476534366607666 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 73 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.678756058216095 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 74 | EQUIP_FROM_INVENTORY | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1414402574300766 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 75 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09767267107963562 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 76 | PASS | STABILIZE | 95.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.306017130613327 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20851215720176697 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12752917408943176 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32358306646347046 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08233333379030228 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 7 | 2-4 | 88 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2289443463087082 | 0.0 | 0.0 | +3280b28e-bd8f-494b-a78d-111744e2178b / -— |
| Jogador 7 | 2-4 | 89 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10899388045072556 | 0.0 | 0.0 | +— / -3280b28e-bd8f-494b-a78d-111744e2178b |
| Jogador 7 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0011077991221100092 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3232491910457611 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3267826735973358 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 94 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4610659182071686 | 0.0 | 0.0 | +— / -dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 7 | 2-5 | 96 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043657150119543076 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 2-5 | 97 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0054152011871338 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 7 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.963241457939148 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 104 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 105 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6157711744308472 | 0.0 | 0.0 | +— / -caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 7 | 2-6 | 106 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6251819133758545 | 0.0 | 0.0 | +— / -599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 7 | 2-6 | 107 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050634998828172684 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 108 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6269999742507935 | 0.0 | 0.0 | +— / -fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 2-6 | 109 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 110 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6489103436470032 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 112 | BUY | STABILIZE | 95.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29327529668807983 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 113 | BUY | STABILIZE | 95.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034345921128988266 | 0.0 | 0.0 | +ac02c0c4-a10d-497d-b6c1-d458ad7ae58c / -— |
| Jogador 7 | 2-7 | 114 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03459138795733452 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026100894436240196 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028291137889027596 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 118 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003997583407908678 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03314436599612236 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 122 | BUY | STABILIZE | 95.0 | 6 | 9 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28436699509620667 | 0.0 | 0.0 | +033a84d9-70f6-46a8-a6eb-a2f03be70400 / -— |
| Jogador 7 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19662314653396606 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 124 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04761466011404991 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 7 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006945035420358181 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 126 | SELL | STABILIZE | 95.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -ac02c0c4-a10d-497d-b6c1-d458ad7ae58c |
| Jogador 7 | 3-1 | 127 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06175648048520088 | 0.0 | 0.0 | +5d00c8ab-55fb-42ec-b8ec-75011c7722fc / -— |
| Jogador 7 | 3-1 | 128 | SELL | STABILIZE | 95.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3583333194255829 | 0.0 | 0.0 | +— / -5d00c8ab-55fb-42ec-b8ec-75011c7722fc |
| Jogador 7 | 3-1 | 129 | SELL | STABILIZE | 95.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 3-1 | 130 | SELL | STABILIZE | 95.0 | 6 | 9 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31566667556762695 | 0.0 | 0.0 | +— / -ad1693cd-1ab5-43a9-8164-25929b8bd68e |
| Jogador 7 | 3-2 | 132 | BUY | STABILIZE | 85.0 | 6 | 18 | 1 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2752093970775604 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -— |
| Jogador 7 | 3-2 | 133 | BUY | STABILIZE | 85.0 | 6 | 15 | 1 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038874365389347076 | 0.0 | 0.0 | +46320c4e-6bc0-49d6-b150-be378fa422cf / -— |
| Jogador 7 | 3-2 | 134 | BUY_XP | STABILIZE | 85.0 | 6 | 12 | 1 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 135 | BUY_XP | STABILIZE | 85.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 136 | BUY_XP | STABILIZE | 85.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 137 | SELL | STABILIZE | 85.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11566666513681412 | 0.0 | 0.0 | +— / -46320c4e-6bc0-49d6-b150-be378fa422cf |
| Jogador 7 | 3-2 | 138 | BUY | STABILIZE | 85.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27186837792396545 | 0.0 | 0.0 | +fa331d8d-1e0c-49b4-848e-8ad58859331c / -— |
| Jogador 7 | 3-2 | 139 | SELL | STABILIZE | 85.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -fa331d8d-1e0c-49b4-848e-8ad58859331c |
| Jogador 7 | 3-2 | 140 | SELL | STABILIZE | 85.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6309999823570251 | 0.0 | 0.0 | +— / -033a84d9-70f6-46a8-a6eb-a2f03be70400 |
| Jogador 7 | 3-3 | 142 | BUY | STABILIZE | 85.0 | 6 | 11 | 1 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379288911819458 | 0.0 | 0.0 | +652ff984-c3ac-48d7-9fb6-e95aed0a047d / -242805ca-f275-4e04-a2f5-81e0b6680dd1,7159421f-b5ea-4d10-9cc5-59186d62983d |
| Jogador 7 | 3-3 | 143 | SELL | STABILIZE | 85.0 | 6 | 10 | 1 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -652ff984-c3ac-48d7-9fb6-e95aed0a047d |
| Jogador 7 | 3-3 | 144 | EQUIP_FROM_INVENTORY | STABILIZE | 85.0 | 6 | 13 | 1 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04892914742231369 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 145 | BUY | STABILIZE | 85.0 | 6 | 13 | 1 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06260673701763153 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 146 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 10 | 1 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15820246934890747 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 147 | BUY | STABILIZE | 85.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02593536488711834 | 0.0 | 0.0 | +4d03897d-0113-4a29-a864-75305c142d97 / -— |
| Jogador 7 | 3-3 | 148 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15646806359291077 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.044236257672309875 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 150 | BUY_XP | STABILIZE | 85.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 152 | BUY | STABILIZE | 85.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379822969436646 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -4e206e09-40e3-4699-81cb-8aaf01109dea,a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 7 | 3-4 | 153 | BUY | STABILIZE | 85.0 | 6 | 10 | 1 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7536168694496155 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -2c7e844d-925a-43bb-8be8-65a71d11f964,6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 7 | 0 | 10.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14659681916236877 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 155 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 7 | 0 | 14.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11500503867864609 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 156 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10672067105770111 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 157 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25759169459342957 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 158 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 7 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4229483902454376 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 159 | BUY | STABILIZE | 85.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28499484062194824 | 0.0 | 0.0 | +7e545d27-1847-4016-b42b-e7db1960ae89 / -— |
| Jogador 7 | 3-4 | 160 | BUY | STABILIZE | 85.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19903446733951569 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 7 | 3-5 | 162 | BUY | STABILIZE | 85.0 | 6 | 8 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7778008580207825 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 163 | BUY | STABILIZE | 85.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13039737939834595 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 7 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6886773109436035 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 165 | BUY_XP | STABILIZE | 85.0 | 6 | 4 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02827499993145466 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 85.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12232273817062378 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 167 | MOVE_BENCH | STABILIZE | 85.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41125595569610596 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 168 | PASS | STABILIZE | 85.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 172 | BUY | FAST8 | 85.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21116489171981812 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 173 | MOVE_BENCH | FAST8 | 85.0 | 7 | 3 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09303677082061768 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 174 | MOVE_BENCH | FAST8 | 85.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17598967254161835 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 175 | BUY | STABILIZE | 85.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026270244270563126 | 0.0 | 0.0 | +69ccc61a-403b-4025-8359-b2061dc6ad10 / -— |
| Jogador 7 | 3-6 | 176 | MOVE_BENCH | STABILIZE | 85.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20617948472499847 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 177 | MOVE_BENCH | FAST8 | 85.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07701248675584793 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 178 | MOVE_BENCH | FAST8 | 85.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7349849939346313 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 179 | MOVE_BOARD | STABILIZE | 85.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007997071370482445 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 180 | PASS | STABILIZE | 85.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 182 | BUY | FAST8 | 85.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7300989627838135 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 183 | BUY | FAST8 | 85.0 | 7 | 3 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7349960207939148 | 0.0 | 0.0 | +21135c93-ae87-47a0-899c-7eaa0c2c30b8 / -— |
| Jogador 7 | 3-7 | 184 | BUY | FAST8 | 85.0 | 7 | 1 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06169601157307625 | 0.0 | 0.0 | +328e1a7d-391c-48e0-b268-64d26b4db788 / -— |
| Jogador 7 | 3-7 | 185 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 186 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08141405880451202 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 187 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 188 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 189 | PASS | FAST8 | 85.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 85.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07868088781833649 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 85.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09286648780107498 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 194 | MOVE_BOARD | FAST8 | 85.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0008221859461627901 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 195 | MOVE_BOARD | FAST8 | 85.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011067477986216545 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 196 | PASS | FAST8 | 85.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 202 | MOVE_BOARD | FAST8 | 85.0 | 7 | 14 | 1 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 203 | MOVE_BOARD | FAST8 | 85.0 | 7 | 14 | 1 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014423351734876633 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 204 | PASS | FAST8 | 85.0 | 7 | 14 | 1 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 212 | MOVE_BOARD | FAST8 | 85.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 213 | MOVE_BOARD | FAST8 | 85.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020816868171095848 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 214 | PASS | FAST8 | 85.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03142857179045677 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 222 | SELL | FAST8 | 85.0 | 7 | 35 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -1ff50c59-5133-459e-8bf1-d449c26efabf |
| Jogador 7 | 4-4 | 223 | BUY | FAST8 | 85.0 | 7 | 38 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.6548970341682434 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 7 | 4-4 | 224 | EQUIP_FROM_INVENTORY | FAST8 | 85.0 | 7 | 35 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.157291978597641 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 225 | EQUIP_FROM_INVENTORY | FAST8 | 85.0 | 7 | 35 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07359491288661957 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 226 | MOVE_BOARD | FAST8 | 85.0 | 7 | 35 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032833244651556015 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 227 | MOVE_BOARD | FAST8 | 85.0 | 7 | 35 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019199715927243233 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 228 | MOVE_BOARD | FAST8 | 85.0 | 7 | 35 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06494110822677612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 229 | MOVE_BOARD | FAST8 | 85.0 | 7 | 35 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03438332676887512 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 230 | MOVE_BOARD | FAST8 | 85.0 | 7 | 35 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 232 | MOVE_BOARD | FAST8 | 85.0 | 7 | 46 | 4 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 233 | MOVE_BOARD | FAST8 | 85.0 | 7 | 46 | 4 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017239248380064964 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 234 | PASS | FAST8 | 85.0 | 7 | 46 | 4 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04714285582304001 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 242 | SELL | FAST8 | 85.0 | 7 | 59 | 5 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 4-6 | 243 | BUY | FAST8 | 85.0 | 7 | 67 | 5 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2974747121334076 | 0.0 | 0.0 | +57d86f23-f167-472f-9878-21dcddc0a5f7 / -— |
| Jogador 7 | 4-6 | 244 | BUY_XP | FAST8 | 85.0 | 7 | 64 | 5 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05012800171971321 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 245 | BUY_XP | FAST8 | 85.0 | 7 | 60 | 5 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05012800171971321 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 246 | BUY_XP | FAST8 | 85.0 | 7 | 56 | 5 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05012800171971321 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 247 | BUY_XP | FAST8 | 85.0 | 7 | 52 | 5 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047704000025987625 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 248 | BUY_XP | FAST8 | 85.0 | 7 | 48 | 4 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025696000084280968 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 249 | BUY_XP | FAST8 | 85.0 | 7 | 44 | 4 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025696000084280968 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 250 | BUY_XP | FAST8 | 85.0 | 7 | 40 | 4 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05430399999022484 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 252 | SELL | FAST8 | 85.0 | 7 | 48 | 4 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08579999953508377 | 0.0 | 0.0 | +— / -69ccc61a-403b-4025-8359-b2061dc6ad10 |
| Jogador 7 | 4-7 | 253 | BUY | FAST8 | 85.0 | 7 | 51 | 5 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.808823823928833 | 0.0 | 0.0 | +50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de / -21135c93-ae87-47a0-899c-7eaa0c2c30b8,7e545d27-1847-4016-b42b-e7db1960ae89 |
| Jogador 7 | 4-7 | 254 | BUY | STABILIZE | 85.0 | 7 | 49 | 4 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7029728293418884 | 0.0 | 0.0 | +af98a89b-ee97-45ce-972a-3f41e280b6b2 / -— |
| Jogador 7 | 4-7 | 255 | BUY_XP | STABILIZE | 85.0 | 7 | 47 | 4 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022065000608563423 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 256 | BUY_XP | STABILIZE | 85.0 | 7 | 43 | 4 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10206499695777893 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 257 | BUY_XP | STABILIZE | 85.0 | 7 | 39 | 3 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05980312451720238 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 258 | MOVE_BENCH | ECON | 85.0 | 8 | 35 | 3 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12276855111122131 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 259 | BUY | WINSTREAK | 85.0 | 8 | 35 | 3 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8432890772819519 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -0cf5c315-d2f3-4854-a95b-07912b83ea81,5b96c8f7-bacb-47df-8666-30d30d49549d |
| Jogador 7 | 4-7 | 260 | MOVE_BENCH | ECON | 85.0 | 8 | 32 | 3 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2992384135723114 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 262 | BUY | WINSTREAK | 85.0 | 8 | 43 | 4 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9067105054855347 | 0.0 | 0.0 | +aee0c45d-0178-4238-987f-5ee83dae7bce / -4d03897d-0113-4a29-a864-75305c142d97,af98a89b-ee97-45ce-972a-3f41e280b6b2 |
| Jogador 7 | 5-1 | 263 | CRAFT_AND_EQUIP | WINSTREAK | 85.0 | 8 | 41 | 4 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11587559431791306 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 264 | CRAFT_AND_EQUIP | WINSTREAK | 85.0 | 8 | 41 | 4 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14723734557628632 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 265 | MOVE_BENCH | WINSTREAK | 85.0 | 8 | 41 | 4 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07578396797180176 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 266 | MOVE_BENCH | WINSTREAK | 85.0 | 8 | 41 | 4 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5136268734931946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 267 | MOVE_BENCH | WINSTREAK | 85.0 | 8 | 41 | 4 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10612393170595169 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 268 | BUY_XP | WINSTREAK | 85.0 | 8 | 41 | 4 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10085000097751617 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 269 | BUY_XP | WINSTREAK | 85.0 | 8 | 37 | 3 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02085000090301037 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 270 | BUY_XP | WINSTREAK | 85.0 | 8 | 33 | 3 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10085000097751617 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 272 | BUY | WINSTREAK | 85.0 | 8 | 41 | 4 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07417339831590652 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -— |
| Jogador 7 | 5-2 | 273 | BUY | WINSTREAK | 85.0 | 8 | 38 | 3 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00350438361056149 | 0.0 | 0.0 | +64215569-2a69-410d-a2f9-172544bef858 / -— |
| Jogador 7 | 5-2 | 274 | BUY_XP | WINSTREAK | 85.0 | 8 | 34 | 3 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004920000210404396 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 275 | BUY_XP | WINSTREAK | 85.0 | 8 | 30 | 3 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0849199965596199 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 276 | BUY_XP | WINSTREAK | 85.0 | 8 | 26 | 2 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004920000210404396 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 277 | BUY_XP | WINSTREAK | 85.0 | 8 | 22 | 2 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0849199965596199 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 278 | BUY_XP | WINSTREAK | 85.0 | 8 | 18 | 1 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004920000210404396 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 279 | BUY_XP | WINSTREAK | 85.0 | 8 | 14 | 1 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004920000210404396 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 280 | BUY_XP | WINSTREAK | 85.0 | 8 | 10 | 1 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0849199965596199 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 282 | SELL | WINSTREAK | 85.0 | 8 | 15 | 1 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004636714700609446 | 0.0 | 0.0 | +— / -aee0c45d-0178-4238-987f-5ee83dae7bce |
| Jogador 7 | 5-3 | 283 | BUY | WINSTREAK | 85.0 | 8 | 20 | 2 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6096979975700378 | 0.0 | 0.0 | +f00a538c-0607-4d8b-babe-7c13daf80c42 / -— |
| Jogador 7 | 5-3 | 284 | BUY_XP | WINSTREAK | 85.0 | 8 | 17 | 1 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004920000210404396 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 285 | BUY_XP | WINSTREAK | 85.0 | 8 | 13 | 1 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0849199965596199 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 286 | BUY_XP | WINSTREAK | 85.0 | 8 | 9 | 0 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004920000210404396 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 287 | BUY_XP | WINSTREAK | 85.0 | 8 | 5 | 0 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 288 | MOVE_BOARD | WINSTREAK | 85.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003465416841208935 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 289 | MOVE_BENCH | WINSTREAK | 85.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19999903440475464 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 290 | BUY | WINSTREAK | 85.0 | 8 | 1 | 0 | 48.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00472905021160841 | 0.0 | 0.0 | +2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d / -— |
| Jogador 7 | 5-4 | 292 | SELL | WINSTREAK | 85.0 | 8 | 9 | 0 | 48.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de |
| Jogador 7 | 5-4 | 293 | BUY | WINSTREAK | 85.0 | 8 | 14 | 1 | 48.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.799893856048584 | 0.0 | 0.0 | +f087511a-d834-4f41-9b99-00bf0f6dc061 / -57d86f23-f167-472f-9878-21dcddc0a5f7,f00a538c-0607-4d8b-babe-7c13daf80c42 |
| Jogador 7 | 5-4 | 294 | MOVE_BENCH | WINSTREAK | 85.0 | 8 | 11 | 1 | 36.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10388685017824173 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 295 | BUY | WINSTREAK | 85.0 | 8 | 11 | 1 | 38.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18464989960193634 | 0.0 | 0.0 | +efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 / -— |
| Jogador 7 | 5-4 | 296 | MOVE_BENCH | WINSTREAK | 85.0 | 8 | 9 | 0 | 38.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14704297482967377 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 297 | BUY_XP | WINSTREAK | 85.0 | 8 | 9 | 0 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06268750131130219 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 298 | BUY_XP | WINSTREAK | 85.0 | 9 | 5 | 0 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 299 | MOVE_BENCH | WINSTREAK | 85.0 | 9 | 1 | 0 | 40.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1501922756433487 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 300 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 1 | 0 | 42.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 302 | BUY | WINSTREAK | 85.0 | 9 | 9 | 0 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23905602097511292 | 0.0 | 0.0 | +08731924-b808-4070-8c85-2c747847d835 / -— |
| Jogador 7 | 5-5 | 303 | BUY_XP | WINSTREAK | 85.0 | 9 | 5 | 0 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 304 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 1 | 0 | 42.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 305 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 1 | 0 | 42.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 306 | PASS | WINSTREAK | 85.0 | 9 | 1 | 0 | 42.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 312 | BUY | WINSTREAK | 85.0 | 9 | 10 | 1 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04917014762759209 | 0.0 | 0.0 | +1bf15a91-4832-4245-9b48-382a27410263 / -— |
| Jogador 7 | 5-6 | 313 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 6 | 0 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048314016312360764 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 314 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 6 | 0 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 315 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 6 | 0 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 316 | PASS | WINSTREAK | 85.0 | 9 | 6 | 0 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 322 | BUY | WINSTREAK | 85.0 | 9 | 14 | 1 | 58.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7844024896621704 | 0.0 | 0.0 | +b311d350-7bab-48ee-9833-0883606b4a2f / -— |
| Jogador 7 | 5-7 | 323 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 12 | 1 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 324 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 12 | 1 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 325 | PASS | WINSTREAK | 85.0 | 9 | 12 | 1 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 332 | EQUIP_FROM_INVENTORY | WINSTREAK | 85.0 | 9 | 21 | 2 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10478164255619049 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 333 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 21 | 2 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 334 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 21 | 2 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 335 | PASS | WINSTREAK | 85.0 | 9 | 21 | 2 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 342 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 32 | 3 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010360888205468655 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 343 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 32 | 3 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014996428973972797 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 344 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 32 | 3 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014974480494856834 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 345 | PASS | WINSTREAK | 85.0 | 9 | 32 | 3 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 352 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 44 | 4 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.0068087653489783e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 353 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 44 | 4 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 354 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 44 | 4 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 355 | PASS | WINSTREAK | 85.0 | 9 | 44 | 4 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19285714626312256 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 362 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 57 | 5 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 363 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 57 | 5 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 364 | PASS | WINSTREAK | 85.0 | 9 | 57 | 5 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04682892560958862 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 372 | SELL | WINSTREAK | 85.0 | 9 | 70 | 5 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -f087511a-d834-4f41-9b99-00bf0f6dc061 |
| Jogador 7 | 6-5 | 373 | BUY | WINSTREAK | 85.0 | 9 | 78 | 5 | 58.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9037564396858215 | 0.0 | 0.0 | +ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 / -— |
| Jogador 7 | 6-5 | 374 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 75 | 5 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 375 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 75 | 5 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999926090240479 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 376 | PASS | WINSTREAK | 85.0 | 9 | 75 | 5 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2295873910188675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 382 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 89 | 5 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.5291337048402056e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 383 | MOVE_BOARD | WINSTREAK | 85.0 | 9 | 89 | 5 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016162607818841934 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 384 | PASS | WINSTREAK | 85.0 | 9 | 89 | 5 | 58.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2419457882642746 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031589943915605545 | 0.0 | 0.0 | +88a02960-5ebe-4b20-b667-1a8ce2728578 / -— |
| Jogador 8 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16182130575180054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3620654344558716 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012301865965127945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5032565593719482 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0140845775604248 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36052340269088745 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28077805042266846 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9758638739585876 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 44 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1734657883644104 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 45 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2513078451156616 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 46 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11591774970293045 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 47 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 53 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1142356395721436 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -88a02960-5ebe-4b20-b667-1a8ce2728578,dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2009154111146927 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17923711240291595 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05874161794781685 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 57 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.103344440460205 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12421705573797226 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03411445766687393 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-1 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32108795642852783 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 62 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26145410537719727 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 63 | BUY | STABILIZE | 94.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29642850160598755 | 0.0 | 0.0 | +ebe77c97-f249-4265-ae03-bc8115a4795f / -— |
| Jogador 8 | 2-2 | 64 | BUY | STABILIZE | 94.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19020919501781464 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 65 | SELL | STABILIZE | 94.0 | 4 | 2 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21272717416286469 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-2 | 66 | BUY_XP | STABILIZE | 94.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09122847020626068 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 68 | SELL | STABILIZE | 94.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-2 | 69 | BUY | STABILIZE | 94.0 | 4 | 2 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17285007238388062 | 0.0 | 0.0 | +3c6ac558-6b59-4a97-814e-bff0ff895232 / -— |
| Jogador 8 | 2-2 | 70 | PASS | STABILIZE | 94.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 72 | BUY | STABILIZE | 89.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.986449658870697 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 73 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3647615611553192 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 74 | SELL | STABILIZE | 89.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0667666643857956 | 0.0 | 0.0 | +— / -3c6ac558-6b59-4a97-814e-bff0ff895232 |
| Jogador 8 | 2-3 | 75 | SELL | STABILIZE | 89.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-3 | 76 | SELL | STABILIZE | 89.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13300000131130219 | 0.0 | 0.0 | +— / -ebe77c97-f249-4265-ae03-bc8115a4795f |
| Jogador 8 | 2-3 | 77 | BUY | STABILIZE | 89.0 | 4 | 8 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24976009130477905 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 78 | SELL | STABILIZE | 89.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1453673392534256 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 2-3 | 79 | SELL | STABILIZE | 89.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33422523736953735 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-3 | 80 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 10 | 1 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08348256349563599 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 82 | BUY | STABILIZE | 83.0 | 5 | 17 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18296171724796295 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 83 | BUY | STABILIZE | 83.0 | 5 | 14 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21314342319965363 | 0.0 | 0.0 | +3644801e-2247-403d-8b81-d2d3f15c2f55 / -— |
| Jogador 8 | 2-4 | 84 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 13 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05875919759273529 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 85 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 13 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3469950556755066 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 86 | BUY | STABILIZE | 83.0 | 5 | 13 | 1 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08821163326501846 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 87 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 10 | 1 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06682410836219788 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 88 | BUY_XP | STABILIZE | 83.0 | 5 | 10 | 1 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 89 | BUY_XP | STABILIZE | 83.0 | 5 | 6 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 90 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc |
| Jogador 8 | 2-5 | 92 | BUY | STABILIZE | 83.0 | 5 | 11 | 1 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0272233486175537 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 93 | BUY | STABILIZE | 83.0 | 5 | 10 | 1 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07615206390619278 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 94 | BUY | STABILIZE | 83.0 | 5 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32314610481262207 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 95 | SELL | STABILIZE | 83.0 | 5 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09146511554718018 | 0.0 | 0.0 | +— / -3644801e-2247-403d-8b81-d2d3f15c2f55 |
| Jogador 8 | 2-5 | 96 | SELL | STABILIZE | 83.0 | 5 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42541003227233887 | 0.0 | 0.0 | +— / -35e1a0f6-207d-4df2-b096-fc07962d094a |
| Jogador 8 | 2-5 | 97 | BUY_XP | STABILIZE | 83.0 | 5 | 8 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 98 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 99 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.380355566740036 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-5 | 100 | BUY | STABILIZE | 83.0 | 5 | 3 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12230958789587021 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-6 | 102 | BUY | STABILIZE | 83.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24916398525238037 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4757331907749176 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 104 | BUY | STABILIZE | 83.0 | 6 | 4 | 0 | 22.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20352338254451752 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 22.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1992843896150589 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 22.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0856911912560463 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 107 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 0 | 0 | 22.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2648916244506836 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 109 | PASS | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 112 | BUY | STABILIZE | 83.0 | 6 | 7 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34422415494918823 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 113 | BUY | STABILIZE | 83.0 | 6 | 4 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28706127405166626 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 114 | BUY | STABILIZE | 83.0 | 6 | 3 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1804666817188263 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00013956762268207967 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01497931033372879 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 118 | PASS | STABILIZE | 83.0 | 6 | 0 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 122 | BUY | STABILIZE | 83.0 | 6 | 6 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.199207603931427 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 83.0 | 6 | 2 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16558775305747986 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 124 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 2 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01823311857879162 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 125 | SELL | STABILIZE | 83.0 | 6 | 2 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0625 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 3-1 | 126 | BUY | STABILIZE | 83.0 | 6 | 3 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07314469665288925 | 0.0 | 0.0 | +7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 / -— |
| Jogador 8 | 3-1 | 127 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 1 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01824404112994671 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 1 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015348882414400578 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 129 | SELL | STABILIZE | 83.0 | 6 | 1 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011533332988619804 | 0.0 | 0.0 | +— / -c0d8da9e-5ede-4a26-8c5c-e2a908318bfd |
| Jogador 8 | 3-1 | 130 | SELL | STABILIZE | 83.0 | 6 | 3 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07566666603088379 | 0.0 | 0.0 | +— / -7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 |
| Jogador 8 | 3-2 | 132 | BUY | STABILIZE | 72.0 | 6 | 10 | 1 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1689247190952301 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 133 | BUY | STABILIZE | 72.0 | 6 | 9 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09103728085756302 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 134 | SELL | STABILIZE | 72.0 | 6 | 5 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0625 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-2 | 135 | SELL | STABILIZE | 72.0 | 6 | 6 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09700000286102295 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 3-2 | 136 | BUY | STABILIZE | 72.0 | 6 | 9 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07466305047273636 | 0.0 | 0.0 | +5326031a-1b7e-4dbd-b58b-1e81029d42a1 / -— |
| Jogador 8 | 3-2 | 137 | SELL | STABILIZE | 72.0 | 6 | 7 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38233333826065063 | 0.0 | 0.0 | +— / -5326031a-1b7e-4dbd-b58b-1e81029d42a1 |
| Jogador 8 | 3-2 | 138 | SELL | STABILIZE | 72.0 | 6 | 9 | 0 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2983333468437195 | 0.0 | 0.0 | +— / -4ac49c80-f0c3-47ae-a031-96928d244e13 |
| Jogador 8 | 3-2 | 139 | SELL | STABILIZE | 72.0 | 6 | 13 | 1 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2153039127588272 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 3-2 | 140 | SELL | STABILIZE | 72.0 | 6 | 16 | 1 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04289352893829346 | 0.0 | 0.0 | +— / -4d995451-2e5c-43c2-93f0-22e074e35ab2 |
| Jogador 8 | 3-3 | 142 | BUY | STABILIZE | 72.0 | 6 | 28 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30515173077583313 | 0.0 | 0.0 | +1af578c1-57cf-4752-93e7-d0eebc6e8ae5 / -— |
| Jogador 8 | 3-3 | 143 | BUY | STABILIZE | 72.0 | 6 | 26 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24843835830688477 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 144 | BUY | STABILIZE | 72.0 | 6 | 23 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21829676628112793 | 0.0 | 0.0 | +3bf8af53-85e7-4e5b-8cf8-b7198a955e8d / -— |
| Jogador 8 | 3-3 | 145 | SELL | STABILIZE | 72.0 | 6 | 22 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42633333802223206 | 0.0 | 0.0 | +— / -3bf8af53-85e7-4e5b-8cf8-b7198a955e8d |
| Jogador 8 | 3-3 | 146 | SELL | STABILIZE | 72.0 | 6 | 23 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.380355566740036 | 0.0 | 0.0 | +— / -e4605ac7-0b51-4f1c-a658-f7d25f9a9dae |
| Jogador 8 | 3-3 | 147 | BUY | STABILIZE | 72.0 | 6 | 26 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0762549489736557 | 0.0 | 0.0 | +8df39648-f588-452a-b234-32da76c43aff / -— |
| Jogador 8 | 3-3 | 148 | SELL | STABILIZE | 72.0 | 6 | 25 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37299999594688416 | 0.0 | 0.0 | +— / -8df39648-f588-452a-b234-32da76c43aff |
| Jogador 8 | 3-3 | 149 | SELL | STABILIZE | 72.0 | 6 | 26 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6309999823570251 | 0.0 | 0.0 | +— / -1af578c1-57cf-4752-93e7-d0eebc6e8ae5 |
| Jogador 8 | 3-3 | 150 | SELL | STABILIZE | 72.0 | 6 | 28 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4588988125324249 | 0.0 | 0.0 | +— / -2e656a3d-eed0-40bb-a831-443d972d6588 |
| Jogador 8 | 3-4 | 152 | BUY | STABILIZE | 62.0 | 6 | 39 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8929812908172607 | 0.0 | 0.0 | +eb7e36f0-cef9-4a2e-979a-f8a357da73e8 / -5de56114-806a-4f58-8241-b3b8434a2154,b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 3-4 | 153 | BUY | STABILIZE | 62.0 | 6 | 38 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13718295097351074 | 0.0 | 0.0 | +e8355df5-8ee7-44a3-ab88-3708c14fd5dc / -— |
| Jogador 8 | 3-4 | 154 | BUY | STABILIZE | 62.0 | 6 | 37 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18516722321510315 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 155 | BUY | STABILIZE | 62.0 | 6 | 34 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00023452947789337486 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 156 | BUY | STABILIZE | 62.0 | 6 | 32 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5577376484870911 | 0.0 | 0.0 | +41782483-877e-4dce-bef9-4f1f3d5757bd / -— |
| Jogador 8 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 30 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001010720618069172 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 158 | SELL | STABILIZE | 62.0 | 6 | 30 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -eb7e36f0-cef9-4a2e-979a-f8a357da73e8 |
| Jogador 8 | 3-4 | 159 | BUY_XP | STABILIZE | 62.0 | 6 | 33 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06834399700164795 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 160 | BUY_XP | STABILIZE | 62.0 | 6 | 29 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011656000278890133 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 162 | BUY | STABILIZE | 62.0 | 6 | 32 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3159148395061493 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 163 | BUY | STABILIZE | 62.0 | 6 | 30 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7518115043640137 | 0.0 | 0.0 | +6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 / -— |
| Jogador 8 | 3-5 | 164 | BUY | STABILIZE | 62.0 | 6 | 28 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2842874526977539 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 8 | 3-5 | 165 | SELL | STABILIZE | 62.0 | 6 | 25 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09351331740617752 | 0.0 | 0.0 | +— / -e8355df5-8ee7-44a3-ab88-3708c14fd5dc |
| Jogador 8 | 3-5 | 166 | BUY | STABILIZE | 62.0 | 6 | 26 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14583280682563782 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 8 | 3-5 | 167 | SELL | STABILIZE | 62.0 | 6 | 23 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04233333468437195 | 0.0 | 0.0 | +— / -82e109f9-54c8-492d-93e5-7e0dd0034b15 |
| Jogador 8 | 3-5 | 168 | SELL | STABILIZE | 62.0 | 6 | 26 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39554575085639954 | 0.0 | 0.0 | +— / -bd4236f8-c8ff-4536-934a-b12b71012724 |
| Jogador 8 | 3-5 | 169 | SELL | STABILIZE | 62.0 | 6 | 29 | 2 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1303333342075348 | 0.0 | 0.0 | +— / -9af097e2-729d-474a-9a7e-b266c665c606 |
| Jogador 8 | 3-5 | 170 | SELL | STABILIZE | 62.0 | 6 | 32 | 3 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49085503816604614 | 0.0 | 0.0 | +— / -d5848998-33f3-4632-94c0-60388a7cc6b8 |
| Jogador 8 | 3-6 | 172 | BUY | STABILIZE | 62.0 | 6 | 43 | 4 | 28.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8992260694503784 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1,9b5e9e71-6772-49bc-979f-11f446f27b11 |
| Jogador 8 | 3-6 | 173 | BUY | STABILIZE | 62.0 | 6 | 41 | 4 | 28.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26318976283073425 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 174 | BUY | STABILIZE | 62.0 | 6 | 38 | 3 | 28.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3039359152317047 | 0.0 | 0.0 | +b55260cd-3c6a-4cb8-99d0-b7c6471103ad / -— |
| Jogador 8 | 3-6 | 175 | SELL | STABILIZE | 62.0 | 6 | 35 | 3 | 28.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5450000166893005 | 0.0 | 0.0 | +— / -b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 |
| Jogador 8 | 3-6 | 176 | BUY | STABILIZE | 62.0 | 6 | 40 | 4 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09470298141241074 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 177 | BUY_XP | STABILIZE | 62.0 | 6 | 36 | 3 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005050000036135316 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 178 | BUY_XP | STABILIZE | 62.0 | 6 | 32 | 3 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07949499785900116 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 179 | BUY_XP | STABILIZE | 62.0 | 6 | 28 | 2 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005050000036135316 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 180 | BUY_XP | STABILIZE | 62.0 | 6 | 24 | 2 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10628499835729599 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 182 | BUY | STABILIZE | 62.0 | 7 | 29 | 2 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2496342957019806 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 183 | BUY | STABILIZE | 62.0 | 7 | 26 | 2 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012771186418831348 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 8 | 3-7 | 184 | BUY | STABILIZE | 62.0 | 7 | 23 | 2 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06672309339046478 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 8 | 3-7 | 185 | SELL | STABILIZE | 62.0 | 7 | 22 | 2 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37299999594688416 | 0.0 | 0.0 | +— / -a14e4b8f-77c5-4909-a9ee-0044b836a877 |
| Jogador 8 | 3-7 | 186 | SELL | STABILIZE | 62.0 | 7 | 23 | 2 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0513949990272522 | 0.0 | 0.0 | +— / -41782483-877e-4dce-bef9-4f1f3d5757bd |
| Jogador 8 | 3-7 | 187 | SELL | STABILIZE | 62.0 | 7 | 25 | 2 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3449999988079071 | 0.0 | 0.0 | +— / -112206a4-c285-4f76-878a-056248cba468 |
| Jogador 8 | 3-7 | 188 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 28 | 2 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4225112497806549 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 189 | BUY | STABILIZE | 62.0 | 7 | 28 | 2 | 34.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2432486116886139 | 0.0 | 0.0 | +3625f791-4c9f-4b95-bdf7-4a322dcd55d3 / -— |
| Jogador 8 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 25 | 2 | 34.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0001515424228273332 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 192 | BUY | STABILIZE | 62.0 | 7 | 33 | 3 | 34.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9354987144470215 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -64afe66e-d5a9-466c-a4ff-9d32c9f153ce,f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 4-1 | 193 | BUY | STABILIZE | 62.0 | 7 | 32 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7351503372192383 | 0.0 | 0.0 | +2c153083-6c43-425e-90d5-23f7f2058592 / -— |
| Jogador 8 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 62.0 | 7 | 29 | 2 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15700572729110718 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 195 | CRAFT_AND_EQUIP | STABILIZE | 62.0 | 7 | 29 | 2 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18042071163654327 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 196 | BUY | STABILIZE | 62.0 | 7 | 29 | 2 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.585736095905304 | 0.0 | 0.0 | +88035b70-61e0-4279-9d55-e451f412f0d3 / -— |
| Jogador 8 | 4-1 | 197 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 26 | 2 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08872877061367035 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 198 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 26 | 2 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38691088557243347 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 199 | BUY | FAST8 | 62.0 | 7 | 26 | 2 | 38.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14288628101348877 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 8 | 4-1 | 200 | MOVE_BOARD | FAST8 | 62.0 | 7 | 23 | 2 | 38.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0001591444161022082 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 202 | BUY | FAST8 | 50.0 | 7 | 30 | 3 | 38.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05513455718755722 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -— |
| Jogador 8 | 4-2 | 203 | BUY | FAST8 | 50.0 | 7 | 27 | 2 | 38.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05507982149720192 | 0.0 | 0.0 | +fb7e519a-8419-414a-8bdc-706c584ddeed / -— |
| Jogador 8 | 4-2 | 204 | MOVE_BOARD | FAST8 | 50.0 | 7 | 25 | 2 | 38.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01535443589091301 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 205 | MOVE_BOARD | FAST8 | 50.0 | 7 | 25 | 2 | 38.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03094852715730667 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 206 | MOVE_BOARD | FAST8 | 50.0 | 7 | 25 | 2 | 38.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015070966444909573 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 207 | PASS | FAST8 | 50.0 | 7 | 25 | 2 | 38.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03214285895228386 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 212 | SELL | STABILIZE | 38.0 | 7 | 33 | 3 | 38.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -2faa526c-d29e-47a9-9eb3-5030750cb483 |
| Jogador 8 | 4-3 | 213 | BUY | STABILIZE | 38.0 | 7 | 36 | 3 | 38.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8929266333580017 | 0.0 | 0.0 | +7dfeef88-7e1d-43b8-b012-017278ec61dc / -2c153083-6c43-425e-90d5-23f7f2058592,6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 4-3 | 214 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 33 | 3 | 26.0 | Enfeitiçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21447008848190308 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 215 | BUY | STABILIZE | 38.0 | 7 | 33 | 3 | 32.0 | Enfeitiçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8308923244476318 | 0.0 | 0.0 | +157648c2-e9b6-4eb2-b42c-19c554a3a41e / -— |
| Jogador 8 | 4-3 | 216 | SELL | STABILIZE | 38.0 | 7 | 31 | 3 | 32.0 | Enfeitiçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5740000009536743 | 0.0 | 0.0 | +— / -7dfeef88-7e1d-43b8-b012-017278ec61dc |
| Jogador 8 | 4-3 | 217 | EQUIP_FROM_INVENTORY | STABILIZE | 38.0 | 7 | 39 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13246075809001923 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 218 | BUY | STABILIZE | 38.0 | 7 | 39 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3124426603317261 | 0.0 | 0.0 | +696f53ae-1413-47cc-b491-9870b7bcba51 / -— |
| Jogador 8 | 4-3 | 219 | BUY_XP | STABILIZE | 38.0 | 7 | 37 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007728000171482563 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 220 | BUY_XP | STABILIZE | 38.0 | 7 | 33 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08772800117731094 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 222 | SELL | STABILIZE | 28.0 | 7 | 37 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004290026146918535 | 0.0 | 0.0 | +— / -fb7e519a-8419-414a-8bdc-706c584ddeed |
| Jogador 8 | 4-4 | 223 | BUY | STABILIZE | 28.0 | 7 | 39 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8482679724693298 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -— |
| Jogador 8 | 4-4 | 224 | SELL | STABILIZE | 28.0 | 7 | 36 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -3625f791-4c9f-4b95-bdf7-4a322dcd55d3 |
| Jogador 8 | 4-4 | 225 | BUY | STABILIZE | 28.0 | 7 | 39 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8328888416290283 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -— |
| Jogador 8 | 4-4 | 226 | SELL | STABILIZE | 28.0 | 7 | 37 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07263333350419998 | 0.0 | 0.0 | +— / -dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 |
| Jogador 8 | 4-4 | 227 | BUY | STABILIZE | 28.0 | 7 | 40 | 4 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8449549078941345 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -5f9e16e2-0766-403f-a85a-f6a735c04261,696f53ae-1413-47cc-b491-9870b7bcba51 |
| Jogador 8 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 38 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22402100265026093 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 229 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 38 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11713609099388123 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 230 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 38 | 3 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025002053007483482 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 232 | BUY | STABILIZE | 28.0 | 7 | 47 | 4 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.777804434299469 | 0.0 | 0.0 | +241a8a03-6e6f-4a9a-8550-e9154f3e1e76 / -— |
| Jogador 8 | 4-5 | 233 | BUY | STABILIZE | 28.0 | 7 | 44 | 4 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8439850211143494 | 0.0 | 0.0 | +c65dacb1-5745-49d1-b7d4-e45d8e24aa84 / -— |
| Jogador 8 | 4-5 | 234 | SELL | STABILIZE | 28.0 | 7 | 43 | 4 | 32.0 | Enfeitiçador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -734c25e1-eddf-4452-a04a-1b39db3b94d0 |
| Jogador 8 | 4-5 | 235 | BUY | STABILIZE | 28.0 | 7 | 48 | 4 | 32.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9246867895126343 | 0.0 | 0.0 | +7e0d7932-1b83-4918-9292-6e60957e6022 / -157648c2-e9b6-4eb2-b42c-19c554a3a41e,a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 8 | 4-5 | 236 | MOVE_BENCH | STABILIZE | 28.0 | 7 | 46 | 4 | 28.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24986816942691803 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 237 | BUY | STABILIZE | 28.0 | 7 | 46 | 4 | 34.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24509020149707794 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -— |
| Jogador 8 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 43 | 4 | 34.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 43 | 4 | 34.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 240 | PASS | STABILIZE | 28.0 | 7 | 43 | 4 | 34.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07522222399711609 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 242 | BUY | STABILIZE | 28.0 | 7 | 53 | 5 | 40.0 | Enfeitiçador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9638673663139343 | 0.0 | 0.0 | +deb56311-9843-48be-9a22-3529305d04e5 / -23366968-ed3f-43d0-9f24-bb7691bf5d45,45da6d00-829e-4e2e-a1a5-318498fd007b |
| Jogador 8 | 4-6 | 243 | BUY | STABILIZE | 28.0 | 7 | 50 | 5 | 34.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7005678415298462 | 0.0 | 0.0 | +de8de4b5-48ea-4947-ae08-2b90d94b0fc1 / -— |
| Jogador 8 | 4-6 | 244 | BUY | STABILIZE | 28.0 | 7 | 47 | 4 | 34.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005303950514644384 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -— |
| Jogador 8 | 4-6 | 245 | SELL | STABILIZE | 28.0 | 7 | 45 | 4 | 34.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -7e0d7932-1b83-4918-9292-6e60957e6022 |
| Jogador 8 | 4-6 | 246 | BUY | STABILIZE | 28.0 | 7 | 50 | 5 | 34.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4589185416698456 | 0.0 | 0.0 | +d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 / -— |
| Jogador 8 | 4-6 | 247 | BUY_XP | STABILIZE | 28.0 | 7 | 48 | 4 | 34.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 248 | BUY_XP | STABILIZE | 28.0 | 7 | 44 | 4 | 34.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 249 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 40 | 4 | 34.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06586013734340668 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 250 | MOVE_BENCH | STABILIZE | 28.0 | 7 | 40 | 4 | 34.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6332589983940125 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 252 | BUY | ALL_IN | 16.0 | 7 | 50 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8693385720252991 | 0.0 | 0.0 | +0d120db3-34e2-47e3-a57c-0d65dcc56342 / -5f2c89f5-15c2-4a77-943e-4ba5492d925b,88035b70-61e0-4279-9d55-e451f412f0d3 |
| Jogador 8 | 4-7 | 253 | BUY | ALL_IN | 16.0 | 7 | 47 | 4 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1268613636493683 | 0.0 | 0.0 | +2949d735-3c16-4a45-835b-e11a9c12b16a / -— |
| Jogador 8 | 4-7 | 254 | SELL | ALL_IN | 16.0 | 7 | 44 | 4 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.054366666823625565 | 0.0 | 0.0 | +— / -0d120db3-34e2-47e3-a57c-0d65dcc56342 |
| Jogador 8 | 4-7 | 255 | BUY | ALL_IN | 16.0 | 7 | 52 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013789361342787743 | 0.0 | 0.0 | +c69a2be1-356a-4576-9887-6d1790221a5e / -— |
| Jogador 8 | 4-7 | 256 | SELL | ALL_IN | 16.0 | 7 | 49 | 4 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09939999878406525 | 0.0 | 0.0 | +— / -50edcbf1-13cd-4f98-bf35-d5a474fbe20c |
| Jogador 8 | 4-7 | 257 | BUY | ALL_IN | 16.0 | 7 | 52 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07132352888584137 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 8 | 4-7 | 258 | MOVE_BOARD | ALL_IN | 16.0 | 7 | 50 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1435248851776123 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 259 | REROLL | ALL_IN | 16.0 | 7 | 50 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 260 | SELL | ALL_IN | 16.0 | 7 | 48 | 4 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07106667011976242 | 0.0 | 0.0 | +— / -d78561b4-3dcc-42fb-9983-2ed5d62f8606 |
| Jogador 8 | 5-1 | 262 | BUY | ALL_IN | 16.0 | 7 | 61 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5497851967811584 | 0.0 | 0.0 | +4e6b6f57-7f94-46ba-b832-c3198d4a5949 / -— |
| Jogador 8 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 16.0 | 7 | 58 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12188028544187546 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 264 | CRAFT_AND_EQUIP | ALL_IN | 16.0 | 7 | 58 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18407097458839417 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 265 | SELL | ALL_IN | 16.0 | 7 | 58 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -2949d735-3c16-4a45-835b-e11a9c12b16a |
| Jogador 8 | 5-1 | 266 | BUY | ALL_IN | 16.0 | 7 | 61 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21868859231472015 | 0.0 | 0.0 | +22f3c707-2635-41cb-a228-10d5ed1883b3 / -— |
| Jogador 8 | 5-1 | 267 | SELL | ALL_IN | 16.0 | 7 | 58 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04846666753292084 | 0.0 | 0.0 | +— / -22f3c707-2635-41cb-a228-10d5ed1883b3 |
| Jogador 8 | 5-1 | 268 | BUY | ALL_IN | 16.0 | 7 | 61 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20121031999588013 | 0.0 | 0.0 | +d22aa2b7-7c7c-4d47-89be-0f1b8755971c / -— |
| Jogador 8 | 5-1 | 269 | MOVE_BENCH | ALL_IN | 16.0 | 7 | 58 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45713603496551514 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 270 | BUY | ALL_IN | 16.0 | 7 | 58 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06179530546069145 | 0.0 | 0.0 | +b6883c6a-7149-4088-8506-20bd8dfed6a5 / -— |
| Jogador 8 | 5-2 | 272 | SELL | ALL_IN | 2.0 | 7 | 69 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010333333164453506 | 0.0 | 0.0 | +— / -b6883c6a-7149-4088-8506-20bd8dfed6a5 |
| Jogador 8 | 5-2 | 273 | BUY | ALL_IN | 2.0 | 7 | 70 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9590528011322021 | 0.0 | 0.0 | +438ec27b-d901-437b-82b5-64e6d46fccb1 / -4e6b6f57-7f94-46ba-b832-c3198d4a5949,c69a2be1-356a-4576-9887-6d1790221a5e |
| Jogador 8 | 5-2 | 274 | BUY | ALL_IN | 2.0 | 7 | 67 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42998355627059937 | 0.0 | 0.0 | +a5e92183-8d5d-434c-9294-47c6b7bfb91b / -— |
| Jogador 8 | 5-2 | 275 | BUY | ALL_IN | 2.0 | 7 | 65 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16780616343021393 | 0.0 | 0.0 | +d8392323-28e4-4e98-a466-5958bf400729 / -— |
| Jogador 8 | 5-2 | 276 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 62 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24832165241241455 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 277 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 62 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25651562213897705 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 278 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 62 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012027719058096409 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 279 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 62 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 280 | PASS | ALL_IN | 2.0 | 7 | 62 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5085453987121582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 282 | SELL | ALL_IN | 2.0 | 7 | 73 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08183333277702332 | 0.0 | 0.0 | +— / -438ec27b-d901-437b-82b5-64e6d46fccb1 |
| Jogador 8 | 5-3 | 283 | BUY | ALL_IN | 2.0 | 7 | 81 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.097685694694519 | 0.0 | 0.0 | +aea521ef-8511-4b98-9c6d-e83b814777df / -b55260cd-3c6a-4cb8-99d0-b7c6471103ad,de8de4b5-48ea-4947-ae08-2b90d94b0fc1 |
| Jogador 8 | 5-3 | 284 | BUY | ALL_IN | 2.0 | 7 | 78 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0834018811583519 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -— |
| Jogador 8 | 5-3 | 285 | SELL | ALL_IN | 2.0 | 7 | 75 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14640000462532043 | 0.0 | 0.0 | +— / -aea521ef-8511-4b98-9c6d-e83b814777df |
| Jogador 8 | 5-3 | 286 | BUY | ALL_IN | 2.0 | 7 | 83 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019122354686260223 | 0.0 | 0.0 | +3329c812-11fa-4335-a982-f03e6ab28ee0 / -— |
| Jogador 8 | 5-3 | 287 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 81 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002659703022800386 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 288 | REROLL | ALL_IN | 2.0 | 7 | 81 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 289 | SELL | ALL_IN | 2.0 | 7 | 79 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0042779711075127125 | 0.0 | 0.0 | +— / -3329c812-11fa-4335-a982-f03e6ab28ee0 |
| Jogador 8 | 5-3 | 290 | BUY | ALL_IN | 2.0 | 7 | 81 | 5 | 40.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1014788150787354 | 0.0 | 0.0 | +f2dbe099-e518-4261-b120-9f327b112dcb / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,c65dacb1-5745-49d1-b7d4-e45d8e24aa84 |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 269 | 286 | 150 | 9 | 14 | 0 | 0 | 0 | 188 | 58.0 |
- Jogador 1 — gasto por ação: BUY: 218g, BUY_XP: 68g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 58g, stage 3: 62g, stage 4: 23g, stage 5: 83g, stage 6: 54g
| Jogador 2 | 167 | 150 | 110 | 4 | 3 | 0 | 1 | 0 | 109 | 16.0 |
- Jogador 2 — gasto por ação: BUY: 136g, BUY_XP: 12g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 58g, stage 3: 64g, stage 4: 21g
| Jogador 3 | 164 | 148 | 97 | 3 | 3 | 0 | 2 | 0 | 129 | 26.0 |
- Jogador 3 — gasto por ação: BUY: 132g, BUY_XP: 12g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 39g, stage 3: 42g, stage 4: 60g
| Jogador 4 | 194 | 186 | 77 | 9 | 9 | 1 | 7 | 0 | 41 | 24.0 |
- Jogador 4 — gasto por ação: BUY: 124g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 14g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 58g, stage 3: 56g, stage 4: 61g, stage 5: 5g
| Jogador 5 | 296 | 326 | 219 | 5 | 14 | 0 | 0 | 0 | 175 | 34.0 |
- Jogador 5 — gasto por ação: BUY: 262g, BUY_XP: 64g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 60g, stage 3: 75g, stage 4: 44g, stage 5: 59g, stage 6: 81g
| Jogador 6 | 188 | 207 | 112 | 14 | 10 | 0 | 2 | 0 | 55 | 34.0 |
- Jogador 6 — gasto por ação: BUY: 155g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 72g, stage 3: 57g, stage 4: 66g, stage 5: 7g
| Jogador 7 | 247 | 284 | 72 | 17 | 34 | 1 | 0 | 0 | 89 | 58.0 |
- Jogador 7 — gasto por ação: BUY: 132g, BUY_XP: 152g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 58g, stage 3: 68g, stage 4: 53g, stage 5: 96g, stage 6: 3g
| Jogador 8 | 228 | 262 | 148 | 17 | 14 | 1 | 2 | 0 | 80 | 38.0 |
- Jogador 8 — gasto por ação: BUY: 198g, BUY_XP: 60g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 64g, stage 3: 85g, stage 4: 77g, stage 5: 29g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 17 | 8 |
- Jogador 1 · 3-6 · step 176: PASS com 9g, HP 100, nível 7/8 (FAST8).
- Jogador 1 · 3-7 · step 188: PASS com 18g, HP 100, nível 7/8 (FAST8).
- Jogador 1 · 4-2 · step 207: PASS com 39g, HP 100, nível 7/8 (FAST8).
- Jogador 1 · 4-3 · step 214: PASS com 52g, HP 100, nível 7/8 (FAST8).
- Jogador 1 · 4-4 · step 226: PASS com 67g, HP 100, nível 7/8 (FAST8).
- Jogador 1 · 4-5 · step 238: PASS com 77g, HP 100, nível 7/8 (FAST8).
- Jogador 1 · 4-6 · step 247: PASS com 92g, HP 100, nível 7/8 (FAST8).
- Jogador 1 · 4-7 · step 257: PASS com 102g, HP 87, nível 7/8 (FAST8).
| Jogador 2 | 3 | 1 |
- Jogador 2 · 4-2 · step 210: REROLL com 95g, HP 15, nível 6/8 (ALL_IN).
| Jogador 3 | 3 | 8 |
- Jogador 3 · 2-6 · step 108: PASS com 5g, HP 89, nível 5/8 (STABILIZE).
- Jogador 3 · 2-7 · step 118: PASS com 7g, HP 84, nível 5/8 (STABILIZE).
- Jogador 3 · 3-2 · step 135: PASS com 20g, HP 74, nível 5/8 (STABILIZE).
- Jogador 3 · 3-3 · step 147: PASS com 23g, HP 63, nível 6/8 (STABILIZE).
- Jogador 3 · 3-4 · step 155: PASS com 30g, HP 53, nível 6/8 (STABILIZE).
- Jogador 3 · 3-5 · step 168: PASS com 33g, HP 53, nível 6/8 (STABILIZE).
- Jogador 3 · 4-4 · step 230: REROLL com 111g, HP 24, nível 6/8 (ALL_IN).
- Jogador 3 · 4-5 · step 240: REROLL com 118g, HP 24, nível 6/8 (ALL_IN).
| Jogador 4 | 12 | 12 |
- Jogador 4 · 3-2 · step 137: PASS com 5g, HP 84, nível 6/8 (STABILIZE).
- Jogador 4 · 4-2 · step 207: REROLL com 11g, HP 37, nível 7/8 (STABILIZE).
- Jogador 4 · 4-3 · step 213: REROLL com 19g, HP 27, nível 7/8 (STABILIZE).
- Jogador 4 · 4-3 · step 218: PASS com 14g, HP 27, nível 7/8 (STABILIZE).
- Jogador 4 · 4-4 · step 222: REROLL com 22g, HP 14, nível 7/8 (ALL_IN).
- Jogador 4 · 4-4 · step 226: REROLL com 22g, HP 14, nível 7/8 (ALL_IN).
- Jogador 4 · 4-5 · step 236: PASS com 24g, HP 14, nível 7/8 (ALL_IN).
- Jogador 4 · 4-6 · step 245: REROLL com 40g, HP 3, nível 7/8 (ALL_IN).
- Jogador 4 · 4-6 · step 249: REROLL com 38g, HP 3, nível 7/8 (ALL_IN).
- Jogador 4 · 4-7 · step 253: REROLL com 47g, HP 3, nível 7/8 (ALL_IN).
- Jogador 4 · 4-7 · step 260: PASS com 38g, HP 3, nível 7/8 (ALL_IN).
- Jogador 4 · 5-1 · step 270: PASS com 41g, HP 3, nível 7/8 (ALL_IN).
| Jogador 5 | 16 | 4 |
- Jogador 5 · 4-4 · step 228: PASS com 17g, HP 72, nível 7/8 (STABILIZE).
- Jogador 5 · 4-5 · step 240: PASS com 24g, HP 72, nível 7/8 (STABILIZE).
- Jogador 5 · 4-7 · step 258: PASS com 39g, HP 72, nível 7/8 (STABILIZE).
- Jogador 5 · 5-3 · step 286: PASS com 71g, HP 57, nível 7/8 (STABILIZE).
| Jogador 6 | 12 | 4 |
- Jogador 6 · 4-2 · step 207: PASS com 15g, HP 38, nível 7/8 (STABILIZE).
- Jogador 6 · 4-3 · step 216: REROLL com 20g, HP 25, nível 7/8 (ALL_IN).
- Jogador 6 · 4-4 · step 228: PASS com 33g, HP 25, nível 7/8 (ALL_IN).
- Jogador 6 · 4-5 · step 236: REROLL com 35g, HP 25, nível 7/8 (ALL_IN).
| Jogador 7 | 38 | 4 |
- Jogador 7 · 4-1 · step 196: PASS com 6g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 4-2 · step 204: PASS com 14g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 4-3 · step 214: PASS com 24g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 4-5 · step 234: PASS com 46g, HP 85, nível 7/8 (FAST8).
| Jogador 8 | 15 | 5 |
- Jogador 8 · 4-2 · step 207: PASS com 25g, HP 50, nível 7/8 (FAST8).
- Jogador 8 · 4-5 · step 240: PASS com 43g, HP 28, nível 7/8 (STABILIZE).
- Jogador 8 · 4-7 · step 259: REROLL com 50g, HP 16, nível 7/8 (ALL_IN).
- Jogador 8 · 5-2 · step 280: PASS com 62g, HP 2, nível 7/8 (ALL_IN).
- Jogador 8 · 5-3 · step 288: REROLL com 81g, HP 2, nível 7/8 (ALL_IN).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 2 | 2 | 0 | 0.0% |
| Jogador 3 | 2 | 1 | 1 | 50.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 2 | 2 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 269 | 57 | 45 | 167 | 0.0043 | 0.5680 | 0.0028 | 0.3099 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0274 (89 ações), BUY_XP: Δ 0.0085 (17 ações), CRAFT_AND_EQUIP: Δ 0.0020 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0112 (23 ações), MOVE_BOARD: Δ 0.0421 (57 ações), PASS: Δ 0.0001 (23 ações), SELL: Δ 0.0152 (52 ações)
| Jogador 2 | 167 | 21 | 27 | 119 | -0.0000 | 0.0546 | -0.0012 | 0.2778 | 0.0012 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0027 (74 ações), BUY_XP: Δ 0.0000 (3 ações), CRAFT_AND_EQUIP: Δ 0.0014 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0619 (13 ações), MOVE_BOARD: Δ -0.0579 (16 ações), PASS: Δ 0.0000 (5 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0065 (47 ações)
| Jogador 3 | 164 | 33 | 38 | 93 | 0.0003 | 0.1681 | -0.0000 | 0.1983 | 0.0004 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0214 (63 ações), BUY_XP: Δ 0.0000 (3 ações), CRAFT_AND_EQUIP: Δ 0.0148 (5 ações), MOVE_BENCH: Δ 0.0214 (24 ações), MOVE_BOARD: Δ 0.0024 (16 ações), PASS: Δ 0.0000 (13 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0205 (38 ações)
| Jogador 4 | 194 | 52 | 41 | 101 | 0.0029 | -0.0209 | 0.0018 | 0.3921 | 0.0011 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0123 (59 ações), BUY_XP: Δ 0.0125 (12 ações), CRAFT_AND_EQUIP: Δ 0.0057 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0007 (3 ações), MOVE_BENCH: Δ 0.0237 (34 ações), MOVE_BOARD: Δ -0.0046 (31 ações), PASS: Δ 0.0000 (15 ações), REROLL: Δ 0.0000 (7 ações), SELL: Δ 0.0165 (26 ações)
| Jogador 5 | 296 | 68 | 54 | 174 | 0.0027 | 0.1517 | 0.0014 | 0.3174 | 0.0014 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0221 (110 ações), BUY_XP: Δ 0.0061 (16 ações), CRAFT_AND_EQUIP: Δ 0.0841 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0064 (4 ações), MOVE_BENCH: Δ 0.0151 (25 ações), MOVE_BOARD: Δ 0.0154 (43 ações), PASS: Δ 0.0000 (14 ações), SELL: Δ 0.0193 (77 ações)
| Jogador 6 | 188 | 38 | 41 | 109 | 0.0025 | -0.4305 | 0.0013 | 0.4925 | 0.0012 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0106 (68 ações), BUY_XP: Δ 0.0062 (12 ações), CRAFT_AND_EQUIP: Δ 0.0141 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0506 (12 ações), MOVE_BOARD: Δ -0.0080 (31 ações), PASS: Δ 0.0000 (13 ações), REROLL: Δ -0.0004 (2 ações), SELL: Δ 0.0166 (40 ações)
| Jogador 7 | 247 | 53 | 41 | 153 | 0.0023 | -0.0333 | 0.0013 | 0.2661 | 0.0010 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0165 (58 ações), BUY_XP: Δ 0.0038 (38 ações), CRAFT_AND_EQUIP: Δ 0.0086 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0300 (6 ações), MOVE_BENCH: Δ -0.0046 (29 ações), MOVE_BOARD: Δ 0.0136 (63 ações), PASS: Δ 0.0000 (23 ações), SELL: Δ 0.0183 (23 ações)
| Jogador 8 | 228 | 48 | 36 | 144 | 0.0049 | 0.0109 | 0.0030 | 0.4038 | 0.0019 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0087 (91 ações), BUY_XP: Δ 0.0033 (15 ações), CRAFT_AND_EQUIP: Δ 0.0025 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0352 (18 ações), MOVE_BOARD: Δ -0.0021 (31 ações), PASS: Δ 0.0600 (10 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0125 (53 ações)
- Jogador 1 — rounds avaliados: 37; correlação estrutural/combate: 0.081; posicional/combate: -0.102.
- Jogador 1 — combate positive: score estrutural prévio 0.592
  score posicional prévio 0.305
- Jogador 1 — combate negative: score estrutural prévio 0.539
  score posicional prévio 0.339
- Jogador 2 — rounds avaliados: 21; correlação estrutural/combate: -0.339; posicional/combate: 0.313.
- Jogador 2 — combate positive: score estrutural prévio -0.060
  score posicional prévio 0.308
- Jogador 2 — combate negative: score estrutural prévio 0.125
  score posicional prévio 0.262
- Jogador 3 — rounds avaliados: 24; correlação estrutural/combate: 0.033; posicional/combate: -0.473.
- Jogador 3 — combate positive: score estrutural prévio 0.190
  score posicional prévio 0.173
- Jogador 3 — combate negative: score estrutural prévio 0.164
  score posicional prévio 0.213
- Jogador 4 — rounds avaliados: 26; correlação estrutural/combate: 0.157; posicional/combate: -0.065.
- Jogador 4 — combate positive: score estrutural prévio 0.057
  score posicional prévio 0.418
- Jogador 4 — combate negative: score estrutural prévio -0.039
  score posicional prévio 0.405
- Jogador 5 — rounds avaliados: 38; correlação estrutural/combate: -0.185; posicional/combate: -0.219.
- Jogador 5 — combate positive: score estrutural prévio 0.070
  score posicional prévio 0.302
- Jogador 5 — combate negative: score estrutural prévio 0.196
  score posicional prévio 0.348
- Jogador 6 — rounds avaliados: 26; correlação estrutural/combate: 0.138; posicional/combate: -0.121.
- Jogador 6 — combate positive: score estrutural prévio -0.184
  score posicional prévio 0.462
- Jogador 6 — combate negative: score estrutural prévio -0.492
  score posicional prévio 0.500
- Jogador 7 — rounds avaliados: 38; correlação estrutural/combate: 0.195; posicional/combate: 0.054.
- Jogador 7 — combate positive: score estrutural prévio 0.080
  score posicional prévio 0.279
- Jogador 7 — combate negative: score estrutural prévio -0.210
  score posicional prévio 0.244
- Jogador 8 — rounds avaliados: 28; correlação estrutural/combate: 0.366; posicional/combate: 0.162.
- Jogador 8 — combate positive: score estrutural prévio 0.278
  score posicional prévio 0.439
- Jogador 8 — combate negative: score estrutural prévio -0.165
  score posicional prévio 0.405

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 305 | OK (305) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Crownguard, TFT_Item_Deathblade, TFT_Item_JeweledGauntlet, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon, TFT_Item_SpectralGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 187 | OK (187) | 5 | 0 | 0 | 1 | 5 | 3 |
- Jogador 2 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 187 | OK (187) | 5 | 0 | 0 | 1 | 5 | 0 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_InfinityEdge, TFT_Item_Redemption, TFT_Item_SteraksGage, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 219 | OK (219) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_BlueBuff, TFT_Item_JeweledGauntlet, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 333 | OK (333) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 5 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_GuinsoosRageblade, TFT_Item_IonicSpark, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 213 | OK (213) | 4 | 0 | 3 | 0 | 7 | 3 |
- Jogador 6 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_JeweledGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 285 | OK (285) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 7 — IDs equipados observados: TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_RunaansHurricane, TFT_Item_StatikkShiv, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 255 | OK (255) | 4 | 3 | 0 | 0 | 7 | 1 |
- Jogador 8 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_DragonsClaw, TFT_Item_HextechGunblade, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.110 | 0.000 |
| Jogador 1 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.001 | 0.000 |
| Jogador 1 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 1 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.012 | 0.000 |
| Jogador 1 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 6 | 5 | 4 → 4 | -0.014 | 0.427 |
| Jogador 1 | 2-2 | 10 | 2.000 | 0.000 | 0 → 0 | 3 → 3 | 14% → 18% | 6 → 8 | 9 | 4 → 5 | -0.027 | 0.269 |
| Jogador 1 | 2-3 | 8 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 18% → 18% | 8 → 7 | 11 | 5 → 5 | 0.000 | 0.320 |
| Jogador 1 | 2-4 | 10 | 2.000 | 8.000 | 0 → 0 | 3 → 2 | 18% → 18% | 7 → 7 | 6 | 5 → 5 | 0.057 | 0.000 |
| Jogador 1 | 2-5 | 10 | 4.000 | -4.000 | 0 → 0 | 2 → 3 | 18% → 21% | 7 → 7 | 12 | 5 → 6 | 0.042 | 0.285 |
| Jogador 1 | 2-6 | 8 | 4.000 | 8.000 | 0 → 0 | 3 → 2 | 21% → 21% | 7 → 8 | 7 | 6 → 6 | -0.000 | 0.330 |
| Jogador 1 | 2-7 | 9 | 4.000 | 6.000 | 0 → 1 | 2 → 2 | 21% → 21% | 8 → 10 | 8 | 6 → 6 | 0.005 | 0.000 |
| Jogador 1 | 3-1 | 6 | 0.000 | 14.000 | 1 → 1 | 2 → 2 | 21% → 21% | 10 → 12 | 7 | 6 → 6 | 0.000 | 0.477 |
| Jogador 1 | 3-2 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 12 → 11 | 16 | 6 → 6 | 0.000 | 0.290 |
| Jogador 1 | 3-3 | 10 | 2.000 | 2.000 | 1 → 0 | 2 → 2 | 21% → 21% | 11 → 10 | 13 | 6 → 6 | -0.012 | 0.281 |
| Jogador 1 | 3-4 | 8 | 4.000 | -2.000 | 0 → 1 | 2 → 2 | 21% → 25% | 10 → 9 | 9 | 6 → 7 | 0.021 | 0.000 |
| Jogador 1 | 3-5 | 10 | 6.000 | 0.000 | 1 → 2 | 2 → 1 | 25% → 25% | 9 → 9 | 10 | 7 → 7 | 0.008 | 0.293 |
| Jogador 1 | 3-6 | 6 | 0.000 | 0.000 | 2 → 2 | 1 → 2 | 25% → 25% | 9 → 19 | 1 | 7 → 7 | 0.000 | 0.492 |
| Jogador 1 | 3-7 | 8 | 0.000 | 2.000 | 2 → 2 | 2 → 3 | 25% → 25% | 19 → 27 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | 2.000 | 2 → 2 | 3 → 4 | 25% → 25% | 27 → 37 | 6 | 7 → 7 | -0.045 | 0.288 |
| Jogador 1 | 4-2 | 7 | 0.000 | -4.000 | 2 → 2 | 4 → 4 | 25% → 25% | 37 → 52 | 1 | 7 → 7 | 0.094 | 0.405 |
| Jogador 1 | 4-3 | 4 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 25% → 25% | 52 → 66 | 0 | 7 → 7 | -0.005 | 0.728 |
| Jogador 1 | 4-4 | 6 | 0.000 | -2.000 | 2 → 2 | 4 → 5 | 25% → 25% | 66 → 80 | 3 | 7 → 7 | -0.002 | 0.000 |
| Jogador 1 | 4-5 | 8 | 0.000 | 6.000 | 2 → 2 | 5 → 4 | 25% → 25% | 80 → 91 | 7 | 7 → 7 | -0.118 | 0.376 |
| Jogador 1 | 4-6 | 7 | 0.000 | -2.000 | 2 → 2 | 4 → 4 | 25% → 25% | 91 → 102 | 3 | 7 → 7 | 0.029 | -0.400 |
| Jogador 1 | 4-7 | 7 | 0.000 | 0.000 | 2 → 2 | 4 → 5 | 25% → 25% | 102 → 112 | 3 | 7 → 7 | 0.107 | 0.000 |
| Jogador 1 | 5-1 | 10 | 0.000 | 6.000 | 2 → 2 | 5 → 2 | 25% → 25% | 112 → 114 | 12 | 7 → 7 | -0.019 | 0.296 |
| Jogador 1 | 5-2 | 10 | 4.000 | 2.000 | 2 → 3 | 2 → 1 | 25% → 21% | 114 → 111 | 21 | 7 → 7 | -0.053 | -0.285 |
| Jogador 1 | 5-3 | 10 | 2.000 | -8.000 | 3 → 3 | 1 → 2 | 21% → 21% | 111 → 128 | 7 | 7 → 7 | 0.019 | -0.285 |
| Jogador 1 | 5-4 | 10 | 0.000 | -6.000 | 3 → 3 | 2 → 3 | 21% → 21% | 128 → 134 | 13 | 7 → 7 | 0.001 | 0.000 |
| Jogador 1 | 5-5 | 10 | 4.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 25% | 134 → 143 | 10 | 7 → 7 | -0.004 | 0.000 |
| Jogador 1 | 5-6 | 10 | -6.000 | -2.000 | 3 → 3 | 3 → 3 | 25% → 21% | 143 → 157 | 10 | 7 → 8 | 0.003 | 0.289 |
| Jogador 1 | 5-7 | 9 | 10.000 | 6.000 | 3 → 3 | 3 → 4 | 21% → 29% | 157 → 159 | 10 | 8 → 8 | 0.002 | 0.000 |
| Jogador 1 | 6-1 | 10 | 2.000 | 12.000 | 3 → 3 | 4 → 3 | 29% → 29% | 159 → 161 | 13 | 8 → 8 | 0.001 | 0.000 |
| Jogador 1 | 6-2 | 9 | 6.000 | -6.000 | 3 → 3 | 3 → 3 | 29% → 29% | 161 → 171 | 6 | 8 → 8 | 0.002 | -0.317 |
| Jogador 1 | 6-3 | 8 | 0.000 | 12.000 | 3 → 3 | 3 → 3 | 29% → 29% | 171 → 176 | 7 | 8 → 8 | 0.017 | -0.344 |
| Jogador 1 | 6-4 | 10 | 0.000 | 4.000 | 3 → 3 | 3 → 3 | 29% → 29% | 176 → 185 | 12 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-5 | 10 | -58.000 | -66.000 | 3 → 0 | 3 → 0 | 29% → 0% | 185 → 188 | 16 | 8 → 8 | -0.106 | -0.285 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 35, COMPOSITION_COMPATIBILITY: 27, IMMEDIATE_UPGRADE: 11, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 60 ações e piorou em 51.
- Jogador 1 — estado final: ouro 188, nível 8, vida 19.0, colocação 3.
| Jogador 2 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.161 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.109 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 3 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 9 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 11% → 14% | 4 → 5 | 5 | 4 → 4 | -0.003 | -0.257 |
| Jogador 2 | 2-2 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 1 | 14% → 14% | 5 → 6 | 8 | 4 → 4 | 0.023 | -0.253 |
| Jogador 2 | 2-3 | 6 | 0.000 | 10.000 | 1 → 1 | 1 → 1 | 14% → 14% | 6 → 7 | 6 | 4 → 5 | 0.008 | -0.404 |
| Jogador 2 | 2-4 | 10 | 2.000 | 8.000 | 1 → 1 | 1 → 2 | 14% → 18% | 7 → 8 | 8 | 5 → 5 | -0.037 | 0.000 |
| Jogador 2 | 2-5 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 18% → 18% | 8 → 7 | 14 | 5 → 5 | -0.000 | -0.253 |
| Jogador 2 | 2-6 | 10 | 0.000 | -8.000 | 1 → 1 | 2 → 3 | 18% → 18% | 7 → 13 | 11 | 5 → 5 | 0.000 | 0.251 |
| Jogador 2 | 2-7 | 10 | 0.000 | -12.000 | 1 → 1 | 3 → 2 | 18% → 18% | 13 → 25 | 6 | 5 → 5 | 0.046 | 0.000 |
| Jogador 2 | 3-1 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 18% | 25 → 32 | 8 | 5 → 5 | 0.000 | -0.259 |
| Jogador 2 | 3-2 | 10 | -2.000 | -4.000 | 1 → 1 | 2 → 3 | 18% → 14% | 32 → 44 | 5 | 5 → 6 | 0.006 | -0.288 |
| Jogador 2 | 3-3 | 10 | 4.000 | 2.000 | 1 → 1 | 3 → 4 | 14% → 21% | 44 → 51 | 12 | 6 → 6 | 0.014 | -0.268 |
| Jogador 2 | 3-4 | 10 | 0.000 | 20.000 | 1 → 1 | 4 → 6 | 21% → 21% | 51 → 51 | 10 | 6 → 6 | -0.059 | 0.000 |
| Jogador 2 | 3-5 | 10 | 0.000 | 0.000 | 1 → 1 | 6 → 5 | 21% → 21% | 51 → 62 | 7 | 6 → 6 | -0.019 | -0.273 |
| Jogador 2 | 3-6 | 10 | 0.000 | -4.000 | 1 → 1 | 5 → 5 | 21% → 21% | 62 → 76 | 10 | 6 → 6 | 0.000 | -0.291 |
| Jogador 2 | 3-7 | 10 | 0.000 | -6.000 | 1 → 1 | 5 → 4 | 21% → 21% | 76 → 90 | 12 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 10 | 0.000 | 4.000 | 1 → 1 | 4 → 5 | 21% → 21% | 90 → 101 | 9 | 6 → 6 | 0.000 | -0.278 |
| Jogador 2 | 4-2 | 10 | 2.000 | 6.000 | 1 → 2 | 5 → 3 | 21% → 18% | 101 → 106 | 8 | 6 → 6 | -0.005 | -0.295 |
| Jogador 2 | 4-3 | 10 | -16.000 | -36.000 | 2 → 0 | 3 → 0 | 18% → 0% | 106 → 109 | 4 | 6 → 6 | -0.008 | -0.295 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 27, COMPOSITION_COMPATIBILITY: 27, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 13; mudanças de composição: 1; posicionamento melhorou em 25 ações e piorou em 28.
- Jogador 2 — estado final: ouro 109, nível 6, vida 2.0, colocação 8.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.060 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 3 | 1-4 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.002 | 0.000 |
| Jogador 3 | 2-1 | 9 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.004 | 0.290 |
| Jogador 3 | 2-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.641 |
| Jogador 3 | 2-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 6 | 7 | 4 → 5 | 0.006 | -0.484 |
| Jogador 3 | 2-4 | 4 | 4.000 | -2.000 | 1 → 1 | 1 → 2 | 14% → 18% | 6 → 6 | 5 | 5 → 5 | 0.026 | 0.000 |
| Jogador 3 | 2-5 | 10 | 2.000 | -8.000 | 1 → 1 | 2 → 2 | 18% → 18% | 6 → 10 | 7 | 5 → 5 | -0.027 | -0.253 |
| Jogador 3 | 2-6 | 8 | 2.000 | 6.000 | 1 → 2 | 2 → 1 | 18% → 18% | 10 → 11 | 5 | 5 → 5 | 0.002 | -0.296 |
| Jogador 3 | 2-7 | 8 | 0.000 | 8.000 | 2 → 2 | 1 → 3 | 18% → 18% | 11 → 13 | 6 | 5 → 5 | 0.006 | 0.000 |
| Jogador 3 | 3-1 | 10 | 0.000 | -4.000 | 2 → 1 | 3 → 2 | 18% → 18% | 13 → 23 | 4 | 5 → 5 | -0.001 | -0.263 |
| Jogador 3 | 3-2 | 5 | 4.000 | 2.000 | 1 → 1 | 2 → 2 | 18% → 18% | 23 → 29 | 3 | 5 → 6 | 0.016 | -0.545 |
| Jogador 3 | 3-3 | 7 | 6.000 | 6.000 | 1 → 1 | 2 → 2 | 18% → 21% | 29 → 33 | 6 | 6 → 6 | 0.021 | -0.376 |
| Jogador 3 | 3-4 | 5 | -2.000 | 8.000 | 1 → 1 | 2 → 3 | 21% → 21% | 33 → 41 | 3 | 6 → 6 | -0.090 | 0.000 |
| Jogador 3 | 3-5 | 8 | 2.000 | 8.000 | 1 → 1 | 3 → 2 | 21% → 21% | 41 → 44 | 10 | 6 → 6 | 0.009 | -0.317 |
| Jogador 3 | 3-6 | 10 | -4.000 | -10.000 | 1 → 1 | 2 → 2 | 21% → 21% | 44 → 65 | 8 | 6 → 6 | 0.066 | -0.254 |
| Jogador 3 | 3-7 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 21% → 21% | 65 → 77 | 8 | 6 → 6 | -0.041 | 0.000 |
| Jogador 3 | 4-1 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 4 | 21% → 21% | 77 → 87 | 12 | 6 → 6 | -0.012 | 0.295 |
| Jogador 3 | 4-2 | 10 | 0.000 | -8.000 | 1 → 1 | 4 → 4 | 21% → 21% | 87 → 103 | 9 | 6 → 6 | 0.000 | 0.276 |
| Jogador 3 | 4-3 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 103 → 112 | 14 | 6 → 6 | -0.006 | -0.268 |
| Jogador 3 | 4-4 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 112 → 119 | 9 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 119 → 127 | 11 | 6 → 6 | 0.006 | -0.285 |
| Jogador 3 | 4-6 | 10 | -26.000 | -42.000 | 1 → 0 | 4 → 0 | 21% → 0% | 127 → 129 | 5 | 6 → 6 | -0.031 | -0.263 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 24, COMPOSITION_COMPATIBILITY: 21, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 12; mudanças de composição: 1; posicionamento melhorou em 38 ações e piorou em 39.
- Jogador 3 — estado final: ouro 129, nível 6, vida 11.0, colocação 7.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 4 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.065 | 0.000 |
| Jogador 4 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 4 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.013 | 0.000 |
| Jogador 4 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 5 | 5 | 4 → 4 | -0.021 | -0.404 |
| Jogador 4 | 2-2 | 5 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 14% → 18% | 5 → 6 | 5 | 4 → 5 | 0.027 | 0.547 |
| Jogador 4 | 2-3 | 10 | 4.000 | -4.000 | 0 → 0 | 3 → 2 | 18% → 18% | 6 → 9 | 9 | 5 → 5 | 0.005 | 0.269 |
| Jogador 4 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 10 | 12 | 5 → 5 | -0.013 | 0.000 |
| Jogador 4 | 2-5 | 10 | 6.000 | -2.000 | 0 → 0 | 3 → 2 | 18% → 21% | 10 → 5 | 14 | 5 → 6 | -0.003 | -0.232 |
| Jogador 4 | 2-6 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 5 → 8 | 3 | 6 → 6 | 0.019 | -0.354 |
| Jogador 4 | 2-7 | 10 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 9 | 10 | 6 → 6 | 0.009 | 0.000 |
| Jogador 4 | 3-1 | 10 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 21% → 21% | 9 → 7 | 15 | 6 → 6 | -0.000 | 0.281 |
| Jogador 4 | 3-2 | 7 | 0.000 | 2.000 | 0 → 0 | 3 → 2 | 21% → 21% | 7 → 10 | 2 | 6 → 6 | -0.052 | -0.390 |
| Jogador 4 | 3-3 | 10 | 0.000 | 4.000 | 0 → 0 | 2 → 1 | 21% → 21% | 10 → 9 | 10 | 6 → 6 | 0.012 | 0.286 |
| Jogador 4 | 3-4 | 10 | 2.000 | 2.000 | 0 → 0 | 1 → 2 | 21% → 25% | 9 → 5 | 14 | 6 → 7 | 0.020 | 0.000 |
| Jogador 4 | 3-5 | 10 | 4.000 | 6.000 | 0 → 0 | 2 → 3 | 25% → 25% | 5 → 5 | 5 | 7 → 7 | -0.021 | -0.276 |
| Jogador 4 | 3-6 | 9 | 0.000 | 10.000 | 0 → 0 | 3 → 4 | 25% → 25% | 5 → 6 | 5 | 7 → 7 | 0.062 | -0.297 |
| Jogador 4 | 3-7 | 10 | -4.000 | 8.000 | 0 → 0 | 4 → 3 | 25% → 25% | 6 → 7 | 5 | 7 → 7 | -0.087 | 0.000 |
| Jogador 4 | 4-1 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 5 | 25% → 25% | 7 → 17 | 5 | 7 → 7 | 0.036 | -0.293 |
| Jogador 4 | 4-2 | 10 | 4.000 | -6.000 | 0 → 1 | 5 → 4 | 25% → 25% | 17 → 21 | 12 | 7 → 7 | 0.003 | -0.258 |
| Jogador 4 | 4-3 | 8 | -4.000 | 14.000 | 1 → 0 | 4 → 4 | 25% → 25% | 21 → 22 | 8 | 7 → 7 | -0.039 | -0.344 |
| Jogador 4 | 4-4 | 10 | -2.000 | -8.000 | 0 → 0 | 4 → 4 | 25% → 25% | 22 → 30 | 10 | 7 → 7 | 0.010 | 0.000 |
| Jogador 4 | 4-5 | 6 | 0.000 | 12.000 | 0 → 0 | 4 → 5 | 25% → 25% | 30 → 34 | 6 | 7 → 7 | -0.066 | -0.438 |
| Jogador 4 | 4-6 | 10 | 4.000 | -18.000 | 0 → 0 | 5 → 5 | 25% → 25% | 34 → 49 | 9 | 7 → 7 | 0.071 | 0.280 |
| Jogador 4 | 4-7 | 10 | -2.000 | 10.000 | 0 → 0 | 5 → 3 | 25% → 25% | 49 → 46 | 11 | 7 → 7 | -0.038 | 0.000 |
| Jogador 4 | 5-1 | 10 | -24.000 | -44.000 | 0 → 0 | 3 → 0 | 25% → 0% | 46 → 41 | 5 | 7 → 7 | -0.015 | -0.280 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 15, COMPOSITION_COMPATIBILITY: 18, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 17; mudanças de composição: 0; posicionamento melhorou em 55 ações e piorou em 43.
- Jogador 4 — estado final: ouro 41, nível 7, vida 3.0, colocação 6.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.112 | 0.000 |
| Jogador 5 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.003 | 0.000 |
| Jogador 5 | 2-1 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.000 | 0.347 |
| Jogador 5 | 2-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.641 |
| Jogador 5 | 2-3 | 10 | 6.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 7 | 11 | 4 → 5 | -0.007 | 0.256 |
| Jogador 5 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 8 | 12 | 5 → 5 | 0.006 | 0.000 |
| Jogador 5 | 2-5 | 10 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 8 → 7 | 12 | 5 → 6 | -0.010 | 0.269 |
| Jogador 5 | 2-6 | 10 | 2.000 | 2.000 | 0 → 0 | 1 → 0 | 21% → 21% | 7 → 6 | 9 | 6 → 6 | -0.025 | -0.269 |
| Jogador 5 | 2-7 | 7 | -2.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 6 → 5 | 7 | 6 → 6 | 0.051 | 0.000 |
| Jogador 5 | 3-1 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 5 → 6 | 9 | 6 → 6 | -0.008 | 0.295 |
| Jogador 5 | 3-2 | 10 | 0.000 | 6.000 | 0 → 0 | 0 → 1 | 21% → 21% | 6 → 10 | 6 | 6 → 6 | 0.041 | 0.291 |
| Jogador 5 | 3-3 | 8 | 0.000 | 16.000 | 0 → 0 | 1 → 2 | 21% → 21% | 10 → 9 | 8 | 6 → 6 | -0.112 | 0.351 |
| Jogador 5 | 3-4 | 10 | 4.000 | -8.000 | 0 → 0 | 2 → 3 | 21% → 21% | 9 → 9 | 11 | 6 → 7 | 0.074 | 0.000 |
| Jogador 5 | 3-5 | 8 | 2.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 25% | 9 → 6 | 8 | 7 → 7 | 0.013 | -0.329 |
| Jogador 5 | 3-6 | 10 | -6.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 21% | 6 → 6 | 16 | 7 → 7 | 0.008 | -0.278 |
| Jogador 5 | 3-7 | 10 | 0.000 | -6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 7 | 17 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 10 | 2.000 | 12.000 | 0 → 0 | 3 → 4 | 21% → 25% | 7 → 6 | 7 | 7 → 7 | 0.004 | 0.288 |
| Jogador 5 | 4-2 | 10 | 0.000 | 2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 6 → 12 | 5 | 7 → 7 | -0.008 | 0.311 |
| Jogador 5 | 4-3 | 10 | 4.000 | -4.000 | 0 → 0 | 4 → 5 | 25% → 25% | 12 → 20 | 10 | 7 → 7 | -0.012 | 0.285 |
| Jogador 5 | 4-4 | 8 | 0.000 | 6.000 | 0 → 0 | 5 → 5 | 25% → 25% | 20 → 24 | 4 | 7 → 7 | 0.016 | 0.000 |
| Jogador 5 | 4-5 | 10 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 25% → 25% | 24 → 33 | 4 | 7 → 7 | 0.006 | 0.280 |
| Jogador 5 | 4-6 | 10 | 0.000 | -2.000 | 0 → 0 | 5 → 4 | 25% → 25% | 33 → 42 | 9 | 7 → 7 | -0.002 | 0.000 |
| Jogador 5 | 4-7 | 8 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 25% → 25% | 42 → 48 | 5 | 7 → 7 | -0.087 | 0.000 |
| Jogador 5 | 5-1 | 10 | -4.000 | 10.000 | 0 → 0 | 4 → 3 | 25% → 25% | 48 → 54 | 10 | 7 → 7 | 0.018 | 0.292 |
| Jogador 5 | 5-2 | 10 | 0.000 | -10.000 | 0 → 0 | 3 → 4 | 25% → 25% | 54 → 71 | 7 | 7 → 7 | 0.009 | -0.280 |
| Jogador 5 | 5-3 | 6 | 4.000 | -4.000 | 0 → 0 | 4 → 4 | 25% → 25% | 71 → 82 | 3 | 7 → 7 | 0.065 | 0.501 |
| Jogador 5 | 5-4 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 5 | 25% → 25% | 82 → 93 | 7 | 7 → 7 | 0.006 | 0.000 |
| Jogador 5 | 5-5 | 10 | 4.000 | -4.000 | 0 → 0 | 5 → 5 | 25% → 25% | 93 → 103 | 14 | 7 → 7 | -0.002 | -0.290 |
| Jogador 5 | 5-6 | 10 | 0.000 | -8.000 | 0 → 0 | 5 → 5 | 25% → 25% | 103 → 118 | 7 | 7 → 7 | 0.004 | -0.273 |
| Jogador 5 | 5-7 | 10 | 0.000 | 2.000 | 0 → 0 | 5 → 5 | 25% → 25% | 118 → 128 | 11 | 7 → 7 | -0.006 | 0.000 |
| Jogador 5 | 6-1 | 10 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 25% → 25% | 128 → 139 | 9 | 7 → 8 | 0.002 | -0.300 |
| Jogador 5 | 6-2 | 10 | 2.000 | 8.000 | 0 → 0 | 5 → 4 | 25% → 29% | 139 → 144 | 15 | 8 → 8 | 0.010 | 0.000 |
| Jogador 5 | 6-3 | 10 | 0.000 | 4.000 | 0 → 0 | 4 → 4 | 29% → 29% | 144 → 153 | 15 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 6-4 | 10 | 0.000 | -4.000 | 0 → 0 | 4 → 4 | 29% → 29% | 153 → 166 | 12 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 6-5 | 10 | -6.000 | 0.000 | 0 → 0 | 4 → 4 | 29% → 25% | 166 → 179 | 12 | 8 → 8 | -0.010 | 0.000 |
| Jogador 5 | 6-6 | 9 | -28.000 | -42.000 | 0 → 0 | 4 → 0 | 25% → 0% | 179 → 175 | 18 | 8 → 8 | -0.074 | -0.311 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 54, COMPOSITION_COMPATIBILITY: 26, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 21; mudanças de composição: 0; posicionamento melhorou em 72 ações e piorou em 56.
- Jogador 5 — estado final: ouro 175, nível 8, vida 4.0, colocação 2.
| Jogador 6 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.163 | 0.000 |
| Jogador 6 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.039 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.021 | -0.412 |
| Jogador 6 | 2-2 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | -0.010 | -0.430 |
| Jogador 6 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 9 | 5 | 4 → 5 | -0.005 | -0.369 |
| Jogador 6 | 2-4 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 3 | 14% → 14% | 9 → 10 | 13 | 5 → 5 | 0.006 | 0.000 |
| Jogador 6 | 2-5 | 10 | 2.000 | -12.000 | 0 → 0 | 3 → 4 | 14% → 18% | 10 → 9 | 15 | 5 → 6 | 0.052 | -0.269 |
| Jogador 6 | 2-6 | 10 | 4.000 | -2.000 | 0 → 0 | 4 → 3 | 18% → 21% | 9 → 7 | 14 | 6 → 6 | -0.018 | -0.264 |
| Jogador 6 | 2-7 | 10 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 7 → 7 | 13 | 6 → 6 | 0.011 | 0.000 |
| Jogador 6 | 3-1 | 10 | 2.000 | -2.000 | 0 → 0 | 3 → 3 | 21% → 21% | 7 → 13 | 9 | 6 → 6 | -0.018 | 0.277 |
| Jogador 6 | 3-2 | 10 | -2.000 | -2.000 | 0 → 0 | 3 → 1 | 21% → 18% | 13 → 11 | 10 | 6 → 6 | 0.028 | -0.254 |
| Jogador 6 | 3-3 | 10 | 8.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 25% | 11 → 8 | 12 | 6 → 7 | 0.080 | -0.263 |
| Jogador 6 | 3-4 | 6 | 0.000 | 14.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 7 | 7 | 7 → 7 | 0.009 | 0.000 |
| Jogador 6 | 3-5 | 6 | 0.000 | 12.000 | 0 → 0 | 1 → 2 | 25% → 25% | 7 → 7 | 6 | 7 → 7 | -0.063 | 0.469 |
| Jogador 6 | 3-6 | 10 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 25% → 25% | 7 → 7 | 7 | 7 → 7 | -0.017 | 0.272 |
| Jogador 6 | 3-7 | 9 | 0.000 | 12.000 | 0 → 0 | 2 → 4 | 25% → 25% | 7 → 7 | 6 | 7 → 7 | 0.036 | 0.000 |
| Jogador 6 | 4-1 | 10 | 0.000 | -6.000 | 0 → 0 | 4 → 3 | 25% → 25% | 7 → 14 | 6 | 7 → 7 | 0.013 | -0.271 |
| Jogador 6 | 4-2 | 7 | 0.000 | 2.000 | 0 → 0 | 3 → 3 | 25% → 25% | 14 → 22 | 7 | 7 → 7 | 0.003 | -0.407 |
| Jogador 6 | 4-3 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 4 | 25% → 25% | 22 → 29 | 12 | 7 → 7 | -0.000 | 0.311 |
| Jogador 6 | 4-4 | 8 | 0.000 | -8.000 | 0 → 0 | 4 → 5 | 25% → 25% | 29 → 41 | 3 | 7 → 7 | 0.005 | 0.000 |
| Jogador 6 | 4-5 | 10 | 0.000 | 6.000 | 0 → 0 | 5 → 5 | 25% → 25% | 41 → 43 | 15 | 7 → 7 | -0.000 | -0.285 |
| Jogador 6 | 4-6 | 10 | 4.000 | 4.000 | 0 → 0 | 5 → 4 | 25% → 25% | 43 → 47 | 15 | 7 → 7 | 0.009 | 0.288 |
| Jogador 6 | 4-7 | 10 | 0.000 | -4.000 | 0 → 0 | 4 → 4 | 25% → 25% | 47 → 58 | 8 | 7 → 7 | -0.035 | 0.000 |
| Jogador 6 | 5-1 | 10 | -26.000 | -48.000 | 0 → 0 | 4 → 0 | 25% → 0% | 58 → 55 | 7 | 7 → 7 | -0.040 | -0.275 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 21, COMPOSITION_COMPATIBILITY: 29, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 11; mudanças de composição: 1; posicionamento melhorou em 41 ações e piorou em 43.
- Jogador 6 — estado final: ouro 55, nível 7, vida 12.0, colocação 5.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.043 | 0.000 |
| Jogador 7 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.077 | 0.000 |
| Jogador 7 | 2-1 | 6 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.016 | 0.456 |
| Jogador 7 | 2-2 | 10 | 4.000 | -2.000 | 0 → 0 | 3 → 2 | 14% → 14% | 8 → 8 | 8 | 4 → 4 | 0.005 | -0.242 |
| Jogador 7 | 2-3 | 6 | 2.000 | 6.000 | 0 → 1 | 2 → 2 | 14% → 14% | 8 → 9 | 5 | 4 → 5 | 0.088 | 0.456 |
| Jogador 7 | 2-4 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 14% → 14% | 9 → 8 | 13 | 5 → 5 | -0.074 | 0.000 |
| Jogador 7 | 2-5 | 7 | 6.000 | -2.000 | 1 → 1 | 2 → 1 | 14% → 18% | 8 → 9 | 8 | 5 → 5 | 0.013 | 0.352 |
| Jogador 7 | 2-6 | 10 | 2.000 | -10.000 | 1 → 1 | 1 → 3 | 18% → 21% | 9 → 8 | 16 | 5 → 6 | 0.011 | 0.285 |
| Jogador 7 | 2-7 | 10 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 21% → 21% | 8 → 9 | 5 | 6 → 6 | 0.011 | 0.000 |
| Jogador 7 | 3-1 | 10 | 0.000 | -6.000 | 1 → 1 | 3 → 3 | 21% → 21% | 9 → 18 | 7 | 6 → 6 | -0.001 | -0.268 |
| Jogador 7 | 3-2 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 18 → 11 | 20 | 6 → 6 | 0.000 | 0.272 |
| Jogador 7 | 3-3 | 10 | 4.000 | 2.000 | 1 → 1 | 3 → 2 | 21% → 21% | 11 → 11 | 10 | 6 → 6 | 0.006 | 0.281 |
| Jogador 7 | 3-4 | 10 | 6.000 | 4.000 | 1 → 2 | 2 → 0 | 21% → 18% | 11 → 8 | 9 | 6 → 6 | -0.005 | 0.000 |
| Jogador 7 | 3-5 | 8 | 6.000 | 2.000 | 2 → 2 | 0 → 1 | 18% → 21% | 8 → 7 | 8 | 6 → 7 | -0.055 | 0.340 |
| Jogador 7 | 3-6 | 10 | 0.000 | 14.000 | 2 → 1 | 1 → 1 | 21% → 25% | 7 → 7 | 7 | 7 → 7 | 0.044 | 0.308 |
| Jogador 7 | 3-7 | 9 | 0.000 | 14.000 | 1 → 1 | 1 → 3 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | 0.037 | 0.000 |
| Jogador 7 | 4-1 | 6 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 6 → 14 | 0 | 7 → 7 | 0.017 | 0.514 |
| Jogador 7 | 4-2 | 4 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 14 → 24 | 0 | 7 → 7 | 0.010 | 0.753 |
| Jogador 7 | 4-3 | 4 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 24 → 35 | 0 | 7 → 7 | -0.045 | 0.690 |
| Jogador 7 | 4-4 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 4 | 25% → 25% | 35 → 46 | 3 | 7 → 7 | 0.008 | 0.000 |
| Jogador 7 | 4-5 | 4 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 46 → 59 | 0 | 7 → 7 | -0.014 | 0.753 |
| Jogador 7 | 4-6 | 10 | 0.000 | -6.000 | 1 → 1 | 4 → 4 | 25% → 25% | 59 → 48 | 31 | 7 → 7 | 0.006 | 0.296 |
| Jogador 7 | 4-7 | 10 | 8.000 | -10.000 | 1 → 2 | 4 → 3 | 25% → 25% | 48 → 43 | 19 | 7 → 8 | -0.014 | 0.000 |
| Jogador 7 | 5-1 | 10 | -4.000 | 4.000 | 2 → 2 | 3 → 2 | 25% → 21% | 43 → 41 | 14 | 8 → 8 | -0.021 | 0.299 |
| Jogador 7 | 5-2 | 10 | 0.000 | 14.000 | 2 → 2 | 2 → 2 | 21% → 21% | 41 → 15 | 35 | 8 → 8 | 0.000 | 0.301 |
| Jogador 7 | 5-3 | 10 | 6.000 | -6.000 | 2 → 2 | 2 → 3 | 21% → 25% | 15 → 9 | 20 | 8 → 8 | -0.008 | 0.317 |
| Jogador 7 | 5-4 | 10 | -6.000 | 2.000 | 2 → 2 | 3 → 2 | 25% → 25% | 9 → 9 | 13 | 8 → 9 | 0.013 | 0.000 |
| Jogador 7 | 5-5 | 6 | 8.000 | 0.000 | 2 → 2 | 2 → 2 | 25% → 29% | 9 → 10 | 8 | 9 → 9 | -0.004 | 0.516 |
| Jogador 7 | 5-6 | 6 | 8.000 | 0.000 | 2 → 2 | 2 → 2 | 29% → 32% | 10 → 14 | 4 | 9 → 9 | 0.032 | 0.000 |
| Jogador 7 | 5-7 | 5 | 0.000 | 4.000 | 2 → 2 | 2 → 3 | 32% → 32% | 14 → 21 | 2 | 9 → 9 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 5 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 32% → 32% | 21 → 32 | 0 | 9 → 9 | 0.000 | 0.644 |
| Jogador 7 | 6-2 | 5 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 32% → 32% | 32 → 44 | 0 | 9 → 9 | 0.117 | 0.611 |
| Jogador 7 | 6-3 | 5 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 32% → 32% | 44 → 57 | 0 | 9 → 9 | 0.082 | 0.591 |
| Jogador 7 | 6-4 | 4 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 32% → 32% | 57 → 70 | 0 | 9 → 9 | 0.000 | 0.000 |
| Jogador 7 | 6-5 | 6 | 0.000 | -6.000 | 2 → 2 | 3 → 4 | 32% → 32% | 70 → 89 | 3 | 9 → 9 | 0.015 | 0.511 |
| Jogador 7 | 6-6 | 4 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 32% → 32% | 89 → 90 | 0 | 9 → 9 | -0.217 | 0.754 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 15, COMPOSITION_COMPATIBILITY: 20, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 14; mudanças de composição: 0; posicionamento melhorou em 59 ações e piorou em 44.
- Jogador 7 — estado final: ouro 90, nível 9, vida 85.0, colocação 1.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.113 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.074 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 3 | 3 → 4 | 0.007 | 0.000 |
| Jogador 8 | 2-1 | 9 | 6.000 | 0.000 | 0 → 1 | 2 → 0 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.016 | -0.287 |
| Jogador 8 | 2-2 | 10 | 0.000 | 4.000 | 1 → 1 | 0 → 0 | 14% → 14% | 6 → 7 | 9 | 4 → 4 | 0.019 | -0.242 |
| Jogador 8 | 2-3 | 10 | -2.000 | -4.000 | 1 → 0 | 0 → 1 | 14% → 14% | 7 → 17 | 5 | 4 → 5 | -0.032 | -0.253 |
| Jogador 8 | 2-4 | 10 | 6.000 | 4.000 | 0 → 0 | 1 → 1 | 14% → 18% | 17 → 11 | 15 | 5 → 5 | 0.036 | 0.000 |
| Jogador 8 | 2-5 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 18% → 18% | 11 → 7 | 16 | 5 → 6 | 0.005 | 0.269 |
| Jogador 8 | 2-6 | 9 | 12.000 | 2.000 | 0 → 0 | 2 → 2 | 18% → 21% | 7 → 7 | 7 | 6 → 6 | 0.069 | 0.312 |
| Jogador 8 | 2-7 | 8 | 0.000 | 14.000 | 0 → 0 | 2 → 2 | 21% → 21% | 7 → 6 | 7 | 6 → 6 | 0.006 | 0.000 |
| Jogador 8 | 3-1 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 2 | 21% → 21% | 6 → 10 | 6 | 6 → 6 | -0.009 | -0.278 |
| Jogador 8 | 3-2 | 10 | 0.000 | -20.000 | 0 → 0 | 2 → 2 | 21% → 21% | 10 → 28 | 7 | 6 → 6 | 0.000 | 0.305 |
| Jogador 8 | 3-3 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 28 → 39 | 7 | 6 → 6 | 0.000 | -0.263 |
| Jogador 8 | 3-4 | 10 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 21% → 21% | 39 → 32 | 17 | 6 → 6 | 0.047 | 0.000 |
| Jogador 8 | 3-5 | 10 | 0.000 | -4.000 | 0 → 0 | 2 → 2 | 21% → 21% | 32 → 43 | 10 | 6 → 6 | 0.000 | 0.290 |
| Jogador 8 | 3-6 | 10 | 0.000 | 12.000 | 0 → 0 | 2 → 1 | 21% → 21% | 43 → 29 | 28 | 6 → 7 | 0.005 | 0.285 |
| Jogador 8 | 3-7 | 10 | 6.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 25% | 29 → 33 | 10 | 7 → 7 | -0.039 | 0.000 |
| Jogador 8 | 4-1 | 10 | 4.000 | 14.000 | 0 → 0 | 1 → 2 | 25% → 25% | 33 → 30 | 10 | 7 → 7 | -0.046 | -0.271 |
| Jogador 8 | 4-2 | 7 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 25% → 25% | 30 → 33 | 5 | 7 → 7 | 0.071 | -0.381 |
| Jogador 8 | 4-3 | 10 | -6.000 | -2.000 | 0 → 0 | 2 → 2 | 25% → 21% | 33 → 37 | 15 | 7 → 7 | -0.007 | -0.258 |
| Jogador 8 | 4-4 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 3 | 21% → 21% | 37 → 47 | 7 | 7 → 7 | -0.012 | 0.000 |
| Jogador 8 | 4-5 | 10 | 8.000 | -2.000 | 0 → 0 | 3 → 4 | 21% → 25% | 47 → 53 | 9 | 7 → 7 | 0.063 | 0.000 |
| Jogador 8 | 4-6 | 10 | 6.000 | 0.000 | 0 → 1 | 4 → 5 | 25% → 25% | 53 → 50 | 18 | 7 → 7 | -0.035 | -0.271 |
| Jogador 8 | 4-7 | 10 | -6.000 | 0.000 | 1 → 1 | 5 → 4 | 25% → 21% | 50 → 61 | 13 | 7 → 7 | 0.002 | 0.000 |
| Jogador 8 | 5-1 | 10 | 6.000 | 2.000 | 1 → 1 | 4 → 5 | 21% → 25% | 61 → 69 | 10 | 7 → 7 | 0.000 | -0.283 |
| Jogador 8 | 5-2 | 10 | 0.000 | 8.000 | 1 → 1 | 5 → 4 | 25% → 25% | 69 → 73 | 8 | 7 → 7 | 0.037 | 0.296 |
| Jogador 8 | 5-3 | 10 | -46.000 | -52.000 | 1 → 0 | 4 → 0 | 25% → 0% | 73 → 80 | 11 | 7 → 7 | -0.069 | -0.300 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 38, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 13, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 54 ações e piorou em 37.
- Jogador 8 — estado final: ouro 80, nível 7, vida 2.0, colocação 4.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 89 | 52 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 1 | 0 |
| Jogador 2 | 74 | 47 | 4 | 5 | 6 | 1 | 1 | 0 | 13 | 1 | 0 | 0 |
| Jogador 3 | 63 | 38 | 0 | 0 | 0 | 2 | 0 | 0 | 23 | 0 | 0 | 0 |
| Jogador 4 | 59 | 26 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 3 | 0 | 0 |
| Jogador 5 | 110 | 77 | 0 | 0 | 1 | 0 | 0 | 1 | 42 | 5 | 0 | 0 |
| Jogador 6 | 68 | 40 | 0 | 1 | 1 | 1 | 0 | 1 | 10 | 3 | 3 | 0 |
| Jogador 7 | 58 | 23 | 2 | 2 | 2 | 1 | 0 | 0 | 0 | 1 | 1 | 0 |
| Jogador 8 | 91 | 53 | 4 | 5 | 8 | 0 | 1 | 0 | 8 | 0 | 3 | 0 |
- Jogador 1 — venda DA_18_Ornn (2-5, step 94): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Akali_AD (2-7, step 118): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 1 — venda DA_Gromp18_AP (4-5, step 232): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Vi18 (5-1, step 264): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 1 — venda DA_Krug18 (5-2, step 273): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 1 — venda DA_KogMaw18_AD (5-3, step 284): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Shen (6-1, step 335): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 2 — venda DA_18_Sentry (2-7, step 120): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Warwick (3-5, step 164): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rakan (4-3, step 212): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_RekSai (3-1, step 127): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Yorick (3-1, step 129): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Scuttlecrab18 (3-6, step 178): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_KhaZix (4-2, step 204): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Rakan (2-5, step 98): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_18_Rakan (2-7, step 116): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_18_Akali_AD (4-3, step 214): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_18_Diana (4-6, step 242): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_MasterYi_AD (4-6, step 246): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_18_MasterYi_AD (4-6, step 250): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (2-6, step 105): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (3-4, step 157): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Cassiopeia (3-7, step 183): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Scuttlecrab18 (4-2, step 206): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Kobuko (4-4, step 223): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Kobuko (4-5, step 234): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_KogMaw18_AD (5-2, step 272): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Veigar (5-4, step 294): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Sentinel18 (5-6, step 312): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Scuttlecrab18 (5-7, step 323): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Azir (6-2, step 346): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_Rammus (6-5, step 374): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Scuttlecrab18 (6-5, step 376): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Cassiopeia (6-6, step 383): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Lillia (6-6, step 387): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 6 — venda DA_18_Yorick (2-6, step 108): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 6 — venda DA_18_Sentry (3-2, step 135): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Rakan (3-3, step 143): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 6 — venda DA_18_Xayah (5-1, step 270): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Camille (2-5, step 95): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 7 — venda DA_18_Rakan (4-4, step 222): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_KogMaw18_AD (4-6, step 242): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Karma18 (3-4, step 158): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Sejuani (3-5, step 170): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Veigar (4-3, step 212): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Diana (4-3, step 216): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **5**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| LOW | Jogador 1 | 2-3 | 75 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 1 | 2-5 | 94 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-5 | 232 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 5-3 | 284 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 2-2 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 527 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-3 | 634 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 771 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-5 | 903 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-6 | 1014 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1225 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1360 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1498 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1608 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1747 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 2456 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-6 | 2559 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-2 | 2946 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-3 | 3088 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-4 | 3223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-5 | 3361 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-6 | 3500 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-7 | 3625 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-1 | 3767 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-2 | 3896 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-3 | 4011 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-4 | 4150 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-5 | 4289 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 6-5 | 4290 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 6-2 | 3988 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-7 | 117 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_KhaZix) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-7 | 120 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sentry' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-1 | 128 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-2 | 137 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-2 | 140 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-3 | 147 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Yunara) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-3 | 148 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-5 | 164 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 4-3 | 212 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-4 | 810 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-5 | 944 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-6 | 1076 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-7 | 1214 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-1 | 1349 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-5 | 1899 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-6 | 2039 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-7 | 2176 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-1 | 2315 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-2 | 2458 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-2 | 2459 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2602 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 4-3 | 2603 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| HIGH | Jogador 3 | 3-1 | 127 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 3-1 | 129 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 3-6 | 178 | SOLD_CORE_UNIT | Venda de 'DA_Scuttlecrab18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 4-2 | 204 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-5 | 793 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-6 | 903 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-7 | 1011 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-1 | 1144 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1145 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-2 | 1217 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1218 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-3 | 1314 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-3 | 1315 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1388 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-4 | 1389 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1499 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-7 | 1773 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 1911 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 2047 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-3 | 2185 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-4 | 2321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-5 | 2458 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-6 | 2595 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 4-6 | 2596 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 3-1 | 1194 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-2 | 1291 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-3 | 1365 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-4 | 1476 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-1 | 128 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 4 | 4-6 | 242 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 4-6 | 250 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 217 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 218 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 226 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 3-5 | 1737 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-5 | 1738 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-6 | 1858 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 1989 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-7 | 1990 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-1 | 2127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-2 | 2262 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-3 | 2374 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-4 | 2513 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-4 | 2514 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 2602 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-5 | 2603 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-6 | 2737 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-6 | 2738 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-7 | 2875 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-7 | 2876 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-1 | 3016 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-1 | 3017 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 4-2 | 2351 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 5 | 2-6 | 105 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-2 | 138 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-7 | 183 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-2 | 206 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-4 | 223 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-5 | 234 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 5-2 | 272 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 5-4 | 294 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 5-6 | 312 | SOLD_CORE_UNIT | Venda de 'DA_Sentinel18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-7 | 323 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 6-5 | 374 | SOLD_CORE_UNIT | Venda de 'DA_18_Rammus' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-5 | 376 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 2-1 | 57 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 58 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 61 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 75 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 76 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 77 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 78 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 79 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 100 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 107 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 108 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 109 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 110 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 148 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 179 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 207 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 208 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 209 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 210 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 217 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 218 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 219 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 220 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 226 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 227 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 228 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 238 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 239 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 240 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 248 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 249 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 250 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 253 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 254 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 255 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 256 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 257 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 258 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 261 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 262 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 263 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 264 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-3 | 558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 822 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 956 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-7 | 1052 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-1 | 1184 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1323 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-3 | 1434 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-3 | 1435 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-4 | 1567 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-4 | 1568 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-5 | 1678 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1679 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-6 | 1813 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1814 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-7 | 1948 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-7 | 1949 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-1 | 2089 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-1 | 2090 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-2 | 2233 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 2234 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-3 | 2376 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2377 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-4 | 2491 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-4 | 2492 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-5 | 2634 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-5 | 2635 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 2780 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-6 | 2781 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-7 | 2896 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-7 | 2897 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 3040 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-1 | 3041 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-2 | 3185 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-2 | 3186 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 3276 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-4 | 3419 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-5 | 3557 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-6 | 3701 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-7 | 3844 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-1 | 3986 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-2 | 4133 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-3 | 4276 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-4 | 4414 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-5 | 4554 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-6 | 4681 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 6-6 | 4682 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 4-3 | 2468 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-4 | 2611 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-6 | 2873 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-2 | 3253 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 2-3 | 76 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 2-7 | 115 | PURCHASE_SALE_REVIEW | Compra de DA_Vi18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 2-7 | 116 | PURCHASE_SALE_REVIEW | Compra de DA_KogMaw18_AD foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 3-1 | 129 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Alistar) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 6 | 3-2 | 135 | SOLD_CORE_UNIT | Venda de 'DA_18_Sentry' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 5-1 | 270 | SOLD_CORE_UNIT | Venda de 'DA_18_Xayah' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 2-2 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 75 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 76 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 77 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 179 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 207 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 217 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 218 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 219 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 220 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 226 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 227 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 228 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 238 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 239 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 240 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 248 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 249 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 250 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 253 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 254 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 255 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 256 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 257 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 258 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 259 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 260 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 261 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 262 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 263 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 264 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 265 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 266 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 267 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 268 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 269 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-3 | 223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-4 | 270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-1 | 355 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-2 | 439 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 537 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 672 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-5 | 805 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-6 | 940 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1074 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1209 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1210 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-2 | 1349 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1350 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-3 | 1483 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1568 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1657 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-6 | 1792 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1919 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 2056 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 2157 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 2293 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 2405 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-5 | 2547 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 2681 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 2682 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 2826 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-7 | 2827 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-1 | 2971 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-1 | 2972 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 4-1 | 2134 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 6 | 4-1 | 2120 | TEXT_MOVE_OSCILLATION | Possível alternância de duas unidades; confirme identidade/estado nos snapshots estruturados. |
| LOW | Jogador 7 | 2-4 | 89 | PURCHASE_SALE_REVIEW | Compra de DA_Scuttlecrab18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 7 | 3-1 | 128 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Yunara) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 3-2 | 139 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Murkwolf18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 7 | 4-4 | 222 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 4-6 | 242 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 2-4 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 107 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 108 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 109 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 110 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 148 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 149 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 179 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 429 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 566 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 567 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-3 | 653 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-4 | 790 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-4 | 791 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-5 | 887 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-5 | 888 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-6 | 1023 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-6 | 1024 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-7 | 1160 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-7 | 1161 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1298 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-1 | 1299 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1435 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-2 | 1436 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1574 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-3 | 1575 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1715 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-4 | 1716 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1823 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-5 | 1824 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1957 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-6 | 1958 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 2082 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-7 | 2083 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 2173 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-1 | 2174 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2239 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-2 | 2240 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2305 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-3 | 2306 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2449 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-4 | 2450 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2515 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-5 | 2516 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2643 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-6 | 2644 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2784 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-7 | 2785 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 2924 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-1 | 2925 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-2 | 3055 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-2 | 3056 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-3 | 3191 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-3 | 3192 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-4 | 3327 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-4 | 3328 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-5 | 3417 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-5 | 3418 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-6 | 3508 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-6 | 3509 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-7 | 3589 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-7 | 3590 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-1 | 3667 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-1 | 3668 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 5 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-2 | 3748 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-2 | 3749 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-3 | 3825 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-3 | 3826 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-4 | 3892 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-4 | 3893 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-5 | 3984 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-5 | 3985 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-6 | 4051 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-6 | 4052 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| MEDIUM | Jogador 7 | 4-6 | 2720 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 8 | 1-4 | 46 | PURCHASE_SALE_REVIEW | Compra de DA_18_RekSai foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 8 | 2-3 | 79 | PURCHASE_SALE_REVIEW | Compra de DA_18_Cassiopeia foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 8 | 2-5 | 96 | PURCHASE_SALE_REVIEW | Compra de DA_18_Warwick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 3-1 | 130 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Murkwolf18) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-2 | 137 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-3 | 145 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-3 | 146 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_KhaZix) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-3 | 148 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 8 | 3-4 | 158 | SOLD_CORE_UNIT | Venda de 'DA_Karma18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-5 | 168 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Vi18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-5 | 170 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-7 | 185 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-7 | 187 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rengar) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 8 | 4-3 | 216 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 2-4 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-4 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 100 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-5 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 107 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 108 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 109 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-6 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-7 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 148 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 149 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-3 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 169 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 170 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 248 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 249 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 250 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 253 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 254 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 255 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 256 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 257 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 258 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 259 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 260 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-7 | 261 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 262 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 263 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 264 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 265 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 266 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 267 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 268 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 269 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 270 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-1 | 271 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-2 | 272 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-2 | 273 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-2 | 274 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-2 | 275 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-2 | 276 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-2 | 277 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-2 | 278 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-2 | 279 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-2 | 280 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-2 | 281 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 282 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 283 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 284 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 285 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 286 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 287 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 288 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 289 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 290 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 291 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-3 | 224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-4 | 321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 445 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-2 | 576 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-3 | 711 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 843 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-5 | 976 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1205 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-1 | 1346 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-2 | 1484 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-3 | 1617 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-4 | 1751 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-5 | 1886 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-6 | 2016 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-7 | 2149 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 2289 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 2290 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2393 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2536 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 2674 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 2811 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-6 | 2947 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-6 | 2948 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-7 | 3084 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-7 | 3085 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-1 | 3221 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-1 | 3222 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-2 | 3362 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-2 | 3363 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-3 | 3503 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 5-3 | 3504 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 4-4 | 2788 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
