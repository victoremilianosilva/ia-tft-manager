# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **5326**
- Achados: **1027**
- CRITICAL: 0 | HIGH: 11 | MEDIUM: 67 | LOW: 949

## Metadados da sessão

- Match ID: 06e2412f-517f-4880-8acc-668759e3204e
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 3d63262fb93d7504bfc05b4e6efd43b7d3bf9e722c0407b8e8b1bd7903bc856d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4685**
- Entradas posteriores à eliminação ignoradas: **641**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 74 | 7 | 8 | 8 | 65 | 3 | 3 | não/inconclusivo | 0 |
| Jogador 6 | 88 | 7 | 9 | 7 | 75 | 2 | 2 | não/inconclusivo | 0 |
| Jogador 7 | 178 | 8 | 16 | 9 | 91 | 7 | 0 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 235 | 77 | 49 | 8 | 1 | 18 | 75 | 0.0708 | 10 | 33 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 8, ALL_IN::MOVE_BOARD: 11, ALL_IN::PASS: 2, ALL_IN::REROLL: 1, ALL_IN::SELL: 9, STABILIZE::BUY: 69, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 19, STABILIZE::MOVE_BOARD: 45, STABILIZE::PASS: 16, STABILIZE::SELL: 40
- Jogador 1 — recompensas por ação: BUY: média 0.2816 (n=77), BUY_XP: média 0.0262 (n=8), ITEM: média 0.1900 (n=7), MOVE_BENCH: média 0.2037 (n=19), MOVE_BOARD: média -0.0093 (n=56), PASS: média -0.0839 (n=18), REROLL: média -0.0700 (n=1), SELL: média -0.1706 (n=49)
| Jogador 2 | 298 | 108 | 75 | 11 | 1 | 11 | 83 | 0.0475 | 9 | 30 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 8, ALL_IN::MOVE_BENCH: 8, ALL_IN::PASS: 1, ALL_IN::SELL: 7, STABILIZE::BUY: 100, STABILIZE::BUY_XP: 11, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 50, STABILIZE::MOVE_BOARD: 25, STABILIZE::PASS: 10, STABILIZE::REROLL: 1, STABILIZE::SELL: 68
- Jogador 2 — recompensas por ação: BUY: média 0.2261 (n=108), BUY_XP: média -0.0091 (n=11), ITEM: média 0.1444 (n=9), MOVE_BENCH: média -0.0266 (n=58), MOVE_BOARD: média -0.0140 (n=25), PASS: média -0.0709 (n=11), REROLL: média -0.1600 (n=1), SELL: média -0.1152 (n=75)
| Jogador 3 | 257 | 82 | 49 | 13 | 0 | 24 | 79 | 0.0830 | 5 | 41 |
- Jogador 3 — ações por estratégia: FAST8::BUY: 37, FAST8::ITEM: 7, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 30, FAST8::PASS: 11, FAST8::SELL: 30, STABILIZE::BUY: 45, STABILIZE::BUY_XP: 13, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 16, STABILIZE::MOVE_BOARD: 32, STABILIZE::PASS: 13, STABILIZE::SELL: 19
- Jogador 3 — recompensas por ação: BUY: média 0.3046 (n=82), BUY_XP: média -0.0392 (n=13), ITEM: média 0.1360 (n=10), MOVE_BENCH: média 0.2276 (n=17), MOVE_BOARD: média -0.0034 (n=62), PASS: média -0.0275 (n=24), SELL: média -0.1533 (n=49)
| Jogador 4 | 182 | 65 | 32 | 8 | 1 | 16 | 52 | 0.0888 | 6 | 16 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 14, ALL_IN::MOVE_BENCH: 4, ALL_IN::MOVE_BOARD: 7, ALL_IN::PASS: 3, ALL_IN::REROLL: 1, ALL_IN::SELL: 6, STABILIZE::BUY: 51, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 20, STABILIZE::MOVE_BOARD: 21, STABILIZE::PASS: 13, STABILIZE::SELL: 26
- Jogador 4 — recompensas por ação: BUY: média 0.4297 (n=65), BUY_XP: média -0.0288 (n=8), ITEM: média 0.1475 (n=8), MOVE_BENCH: média -0.0308 (n=24), MOVE_BOARD: média -0.0186 (n=28), PASS: média -0.1212 (n=16), REROLL: média -0.0700 (n=1), SELL: média -0.2953 (n=32)
| Jogador 5 | 201 | 92 | 61 | 6 | 3 | 8 | 24 | 0.0829 | 13 | 35 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 21, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 3, ALL_IN::MOVE_BOARD: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 16, STABILIZE::BUY: 71, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 7, STABILIZE::PASS: 8, STABILIZE::REROLL: 1, STABILIZE::SELL: 45
- Jogador 5 — recompensas por ação: BUY: média 0.2892 (n=92), BUY_XP: média -0.0183 (n=6), ITEM: média 0.1529 (n=7), MOVE_BENCH: média 0.1469 (n=16), MOVE_BOARD: média 0.0325 (n=8), PASS: média -0.0138 (n=8), REROLL: média -0.1000 (n=3), SELL: média -0.2147 (n=61)
| Jogador 6 | 210 | 75 | 50 | 9 | 4 | 13 | 46 | 0.0837 | 12 | 35 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 27, ALL_IN::ITEM: 5, ALL_IN::MOVE_BENCH: 3, ALL_IN::MOVE_BOARD: 10, ALL_IN::PASS: 2, ALL_IN::REROLL: 3, ALL_IN::SELL: 21, STABILIZE::BUY: 48, STABILIZE::BUY_XP: 9, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 10, STABILIZE::MOVE_BOARD: 23, STABILIZE::PASS: 11, STABILIZE::REROLL: 1, STABILIZE::SELL: 29
- Jogador 6 — recompensas por ação: BUY: média 0.2640 (n=75), BUY_XP: média -0.0456 (n=9), ITEM: média 0.1692 (n=13), MOVE_BENCH: média 0.3285 (n=13), MOVE_BOARD: média 0.0024 (n=33), PASS: média -0.0685 (n=13), REROLL: média -0.1025 (n=4), SELL: média -0.1412 (n=50)
| Jogador 7 | 284 | 91 | 57 | 16 | 2 | 22 | 75 | 0.0864 | 9 | 53 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 17, ALL_IN::ITEM: 5, ALL_IN::MOVE_BENCH: 9, ALL_IN::SELL: 14, STABILIZE::BUY: 74, STABILIZE::BUY_XP: 16, STABILIZE::ITEM: 16, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 52, STABILIZE::PASS: 22, STABILIZE::REROLL: 2, STABILIZE::SELL: 43
- Jogador 7 — recompensas por ação: BUY: média 0.3258 (n=91), BUY_XP: média -0.0144 (n=16), ITEM: média 0.1233 (n=21), MOVE_BENCH: média 0.1465 (n=23), MOVE_BOARD: média -0.0048 (n=52), PASS: média -0.0236 (n=22), REROLL: média -0.1600 (n=2), SELL: média -0.1712 (n=57)
| Jogador 8 | 218 | 81 | 49 | 1 | 11 | 11 | 58 | 0.0557 | 5 | 20 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 19, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 1, ALL_IN::REROLL: 6, ALL_IN::SELL: 17, FAST8::BUY: 6, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 3, FAST8::REROLL: 3, FAST8::SELL: 5, STABILIZE::BUY: 56, STABILIZE::BUY_XP: 1, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 46, STABILIZE::MOVE_BOARD: 7, STABILIZE::PASS: 11, STABILIZE::REROLL: 2, STABILIZE::SELL: 27
- Jogador 8 — recompensas por ação: BUY: média 0.4057 (n=81), BUY_XP: média 0.0500 (n=1), ITEM: média 0.1714 (n=7), MOVE_BENCH: média -0.1367 (n=48), MOVE_BOARD: média 0.0070 (n=10), PASS: média -0.0682 (n=11), REROLL: média -0.1354 (n=11), SELL: média -0.2700 (n=49)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 15:05:25 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | ? | 15:05:27 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | ? | 15:05:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 15:05:32 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 15:05:32 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 15:05:33 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-1 | 15:05:34 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 15:05:35 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 15:05:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 15:05:37 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 1-2 | 15:05:40 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-2 | 15:05:40 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 15:05:40 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 15:05:42 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-2 | 15:05:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 15:05:48 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 15:05:48 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 15:05:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 15:05:56 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 15:05:56 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 1-4 | 15:05:57 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 15:05:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-4 | 15:05:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-1 | 15:06:05 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 15:06:06 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.1300 |  |
| Jogador 1 | 2-1 | 15:06:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 15:06:06 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-1 | 15:06:07 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.2800 |  |
| Jogador 1 | 2-1 | 15:06:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 15:06:08 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1700 |  |
| Jogador 1 | 2-1 | 15:06:08 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-1 | 15:06:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-2 | 15:06:15 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 1 | 2-2 | 15:06:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 15:06:16 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-2 | 15:06:17 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1800 |  |
| Jogador 1 | 2-2 | 15:06:17 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 1 | 2-2 | 15:06:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 15:06:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 15:06:26 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 2-3 | 15:06:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3600 |  |
| Jogador 1 | 2-3 | 15:06:27 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 2-3 | 15:06:28 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 15:06:29 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 15:06:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-4 | 15:06:39 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Ornn | 1.0200 |  |
| Jogador 1 | 2-4 | 15:06:40 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Ornn | 0.3300 |  |
| Jogador 1 | 2-4 | 15:06:40 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 1 | 2-4 | 15:06:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 2-4 | 15:06:41 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 15:06:41 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 2-4 | 15:06:42 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 15:06:43 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 2-4 | 15:06:43 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 15:06:54 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 2-5 | 15:06:54 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 2-5 | 15:06:54 | MOVE Bench -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 1 | 2-5 | 15:06:55 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 1 | 2-5 | 15:06:56 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 2-5 | 15:06:56 | MOVE Board -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 15:06:57 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 15:06:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 15:07:10 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 2-6 | 15:07:11 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 1 | 2-6 | 15:07:11 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 1 | 2-6 | 15:07:12 | MOVE Bench -> Board: Shen (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 1 | 2-6 | 15:07:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 15:07:15 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 1 | 2-7 | 15:07:29 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | 0.2600 |  |
| Jogador 1 | 2-7 | 15:07:29 | MOVE Bench -> Board: Shen (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 1 | 2-7 | 15:07:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 1 | 2-7 | 15:07:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 2-7 | 15:07:31 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 15:07:32 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 2-7 | 15:07:32 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 2-7 | 15:07:33 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 15:07:33 | MOVE Board -> Board: Akali (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-1 | 15:07:49 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-1 | 15:07:49 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 3-1 | 15:07:50 | MOVE Board -> Board: Shen (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 15:07:51 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 15:07:52 | MOVE Board -> Board: Shen (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 15:07:52 | MOVE Board -> Board: Shen (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-1 | 15:07:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-2 | 15:08:09 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-2 | 15:08:10 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-2 | 15:08:10 | MOVE Board -> Board: Akali (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 3-2 | 15:08:11 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 15:08:12 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 1 | 3-2 | 15:08:12 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-2 | 15:08:13 | MOVE Board -> Board: Akali (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 1 | 3-2 | 15:08:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-3 | 15:08:31 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-3 | 15:08:32 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-3 | 15:08:32 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 15:08:33 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 15:08:33 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 15:08:34 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 3-3 | 15:08:34 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-3 | 15:08:35 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 1 | 3-3 | 15:08:35 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-4 | 15:08:55 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 1 | 3-4 | 15:08:57 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 1 | 3-4 | 15:08:58 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-4 | 15:08:58 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Inferno | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 1 | 3-4 | 15:08:59 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.4400 |  |
| Jogador 1 | 3-4 | 15:08:59 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 1 | 3-4 | 15:09:00 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 3-4 | 15:09:01 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.2600 |  |
| Jogador 1 | 3-4 | 15:09:01 | MOVE Board -> Board: Azir (i:6.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-5 | 15:09:22 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 1 | 3-5 | 15:09:23 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-5 | 15:09:23 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Inferno | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 1 | 3-5 | 15:09:24 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-5 | 15:09:24 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Inferno | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 1 | 3-5 | 15:09:25 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-5 | 15:09:25 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Inferno | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 1 | 3-5 | 15:09:26 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-5 | 15:09:26 | MOVE Board -> Board: Azir (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-6 | 15:09:50 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 3-6 | 15:09:50 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 3-6 | 15:09:51 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Inferno | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 3-6 | 15:09:51 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 15:09:52 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-6 | 15:09:52 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 15:09:53 | MOVE Board -> Board: Akali (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Inferno | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 1 | 3-6 | 15:09:53 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Inferno | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 1 | 3-6 | 15:09:54 | MOVE Board -> Board: Akali (i:4.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Inferno | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 1 | 3-7 | 15:10:20 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Inferno | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 1 | 3-7 | 15:10:20 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Inferno | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 1 | 3-7 | 15:10:21 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 3-7 | 15:10:21 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Inferno | DA_KogMaw18_AD | 0.6800 |  |
| Jogador 1 | 3-7 | 15:10:22 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Inferno | DA_KogMaw18_AD | -0.4600 |  |
| Jogador 1 | 3-7 | 15:10:22 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Inferno | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 1 | 3-7 | 15:10:23 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-7 | 15:10:24 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-7 | 15:10:24 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 4-1 | 15:10:50 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 4-1 | 15:10:50 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Inferno | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 1 | 4-1 | 15:10:51 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-1 | 15:10:52 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-1 | 15:10:52 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Inferno | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 1 | 4-1 | 15:10:53 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-1 | 15:10:53 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Inferno | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 1 | 4-1 | 15:10:54 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Inferno | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 1 | 4-1 | 15:10:54 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Inferno | DA_KogMaw18_AD | -0.3200 |  |
| Jogador 1 | 4-2 | 15:11:22 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Inferno | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 1 | 4-2 | 15:11:23 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Inferno | DA_KogMaw18_AD | -0.2300 |  |
| Jogador 1 | 4-2 | 15:11:24 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Inferno | DA_KogMaw18_AD | -0.6400 |  |
| Jogador 1 | 4-2 | 15:11:24 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 4-2 | 15:11:25 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Inferno | DA_KogMaw18_AD | -0.3500 |  |
| Jogador 1 | 4-2 | 15:11:25 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 4 | Inferno | DA_KogMaw18_AD | -0.3500 |  |
| Jogador 1 | 4-2 | 15:11:26 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-2 | 15:11:26 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 4 | Inferno | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 1 | 4-2 | 15:11:27 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 4 | Inferno | DA_KogMaw18_AD | -0.5200 |  |
| Jogador 1 | 4-3 | 15:11:54 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Inferno | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 1 | 4-3 | 15:11:55 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 70 | 5 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-3 | 15:11:56 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-3 | 15:11:56 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 70 | 5 | Inferno | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 1 | 4-3 | 15:11:57 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Inferno | DA_KogMaw18_AD | -0.3800 |  |
| Jogador 1 | 4-3 | 15:11:57 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 70 | 5 | Inferno | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 1 | 4-3 | 15:11:58 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Inferno | DA_KogMaw18_AD | -0.3300 |  |
| Jogador 1 | 4-3 | 15:11:58 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 4-3 | 15:11:59 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Inferno | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 1 | 4-4 | 15:12:29 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Inferno | DA_KogMaw18_AD | 0.4400 |  |
| Jogador 1 | 4-4 | 15:12:30 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Inferno | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 1 | 4-4 | 15:12:30 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 77 | 5 | Inferno | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 4-4 | 15:12:31 | MOVE Bench -> Board: Diana (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 77 | 5 | Inferno | DA_KogMaw18_AD | 0.4500 |  |
| Jogador 1 | 4-4 | 15:12:31 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Inferno | DA_KogMaw18_AD | -0.2400 |  |
| Jogador 1 | 4-4 | 15:12:32 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 77 | 5 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 4-4 | 15:12:32 | BUY XP | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Inferno | DA_KogMaw18_AD | 0.4800 |  |
| Jogador 1 | 4-4 | 15:12:33 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 4-4 | 15:12:33 | MOVE Board -> Board: Tristana (i:6.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-5 | 15:13:07 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Inferno | DA_KogMaw18_AD | 0.9900 |  |
| Jogador 1 | 4-5 | 15:13:07 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Feérico | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 4-5 | 15:13:08 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Feérico | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 1 | 4-5 | 15:13:09 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Feérico | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 4-5 | 15:13:09 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-5 | 15:13:10 | MOVE Board -> Board: Akali (i:4.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-5 | 15:13:10 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Feérico | DA_KogMaw18_AD | -0.1000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-6 | 15:13:47 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 87 | 5 | Feérico | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 4-6 | 15:13:48 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Feérico | DA_KogMaw18_AD | 0.4500 |  |
| Jogador 1 | 4-6 | 15:13:48 | MOVE Board -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-6 | 15:13:49 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Feérico | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 4-6 | 15:13:50 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Feérico | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 1 | 4-6 | 15:13:50 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-6 | 15:13:51 | MOVE Board -> Board: Tristana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-6 | 15:13:51 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Feérico | DA_KogMaw18_AD | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-7 | 15:14:28 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Xayah (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Feérico | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 1 | 4-7 | 15:14:29 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Rakan (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Feérico | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 4-7 | 15:14:30 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-7 | 15:14:30 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Feérico | DA_KogMaw18_AD | 0.9300 |  |
| Jogador 1 | 4-7 | 15:14:30 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-7 | 15:14:31 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Feérico | DA_CrimsonRaptor18 | 1.0200 |  |
| Jogador 1 | 4-7 | 15:14:32 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Feérico | DA_CrimsonRaptor18 | 0.4500 |  |
| Jogador 1 | 4-7 | 15:14:32 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Feérico | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 1 | 4-7 | 15:14:32 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Feérico | DA_CrimsonRaptor18 | -0.2500 |  |
| Jogador 1 | 5-1 | 15:15:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Feérico | DA_CrimsonRaptor18 | 1.0200 |  |
| Jogador 1 | 5-1 | 15:15:10 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Feérico | DA_CrimsonRaptor18 | -0.1200 |  |
| Jogador 1 | 5-1 | 15:15:11 | MOVE Bench -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Feérico | DA_CrimsonRaptor18 | 0.4900 |  |
| Jogador 1 | 5-1 | 15:15:11 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Feérico | DA_CrimsonRaptor18 | 0.5300 |  |
| Jogador 1 | 5-1 | 15:15:12 | MOVE Board -> Board: Xayah (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Feérico | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 1 | 5-1 | 15:15:12 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Feérico | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 1 | 5-1 | 15:15:13 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Feérico | DA_CrimsonRaptor18 | -0.1700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 5-2 | 15:15:51 | VENDEU: Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Xayah | -0.7000 |  |
| Jogador 1 | 5-2 | 15:15:51 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Feérico | DA_18_Xayah | 0.4800 |  |
| Jogador 1 | 5-2 | 15:15:52 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Feérico | DA_18_Xayah | 0.0000 |  |
| Jogador 1 | 5-2 | 15:15:52 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Feérico | DA_18_Xayah | 0.1100 |  |
| Jogador 1 | 5-2 | 15:15:53 | VENDEU: Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Feérico | DA_18_Xayah | -0.0400 |  |
| Jogador 1 | 5-2 | 15:15:53 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Xayah | -0.0100 |  |
| Jogador 1 | 5-2 | 15:15:54 | MOVE Board -> Board: Akali (i:4.0) <-> Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Xayah | 0.0100 |  |
| Jogador 1 | 5-2 | 15:15:54 | MOVE Board -> Board: Azir (i:6.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Xayah | -0.0100 |  |
| Jogador 1 | 5-2 | 15:15:55 | MOVE Board -> Board: Tristana (i:6.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Xayah | -0.0200 |  |
| Jogador 1 | 5-3 | 15:16:35 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Feérico | DA_18_Xayah | -0.0100 |  |
| Jogador 1 | 5-3 | 15:16:36 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Xayah | 0.4800 |  |
| Jogador 1 | 5-3 | 15:16:36 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Xayah | 0.0000 |  |
| Jogador 1 | 5-3 | 15:16:36 | MOVE Board -> Board: Diana (i:6.0) <-> Xayah (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Xayah | -0.0900 |  |
| Jogador 1 | 5-3 | 15:16:38 | MOVE Board -> Board: Xayah (i:4.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Xayah | 0.0600 |  |
| Jogador 1 | 5-3 | 15:16:39 | MOVE Board -> Board: Xayah (i:4.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Xayah | -0.0200 |  |
| Jogador 1 | 5-3 | 15:16:39 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Akali (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Xayah | -0.0500 |  |
| Jogador 1 | 5-3 | 15:16:40 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Xayah | -0.5600 |  |
| Jogador 1 | 5-4 | 15:17:22 | VENDEU: Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Feérico | DA_18_Xayah | -0.0400 |  |
| Jogador 1 | 5-4 | 15:17:23 | COMPROU: Lux (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Feérico | DA_18_Xayah | -0.2400 |  |
| Jogador 1 | 5-4 | 15:17:23 | MOVE Board -> Board: Akali (i:4.0) <-> Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Feérico | DA_18_Xayah | -0.2800 |  |
| Jogador 1 | 5-4 | 15:17:23 | MOVE Board -> Board: Azir (i:6.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Feérico | DA_18_Xayah | -0.0100 |  |
| Jogador 1 | 5-4 | 15:17:24 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Feérico | DA_18_Xayah | -0.5700 |  |
| Jogador 1 | 5-5 | 15:18:08 | VENDEU: Lux (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Feérico | DA_18_Xayah | -0.0100 |  |
| Jogador 1 | 5-5 | 15:18:08 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Feérico | DA_18_Xayah | 0.9400 |  |
| Jogador 1 | 5-5 | 15:18:09 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Feérico | DA_18_Xayah | 0.1700 |  |
| Jogador 1 | 5-5 | 15:18:10 | VENDEU: Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Feérico | DA_18_Xayah | -0.7400 |  |
| Jogador 1 | 5-5 | 15:18:10 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Feérico | DA_18_Xayah | -0.0100 |  |
| Jogador 1 | 5-5 | 15:18:11 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Feérico | DA_18_Xayah | -0.0200 |  |
| Jogador 1 | 5-5 | 15:18:11 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Feérico | DA_18_Xayah | 0.0000 |  |
| Jogador 1 | 5-5 | 15:18:12 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Feérico | DA_18_Xayah | -0.0700 |  |
| Jogador 1 | 5-5 | 15:18:12 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Feérico | DA_18_Xayah | -0.0200 |  |
| Jogador 2 | ? | 15:05:25 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | ? | 15:05:27 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | ? | 15:05:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 15:05:32 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 15:05:32 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 15:05:33 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 1-1 | 15:05:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 15:05:37 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 1-2 | 15:05:40 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 15:05:40 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 15:05:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 15:05:45 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 15:05:48 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 15:05:48 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 15:05:49 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-3 | 15:05:49 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-3 | 15:05:50 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 15:05:50 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 15:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 15:05:56 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 15:05:56 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 15:05:57 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 15:05:57 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 15:05:58 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 1-4 | 15:05:59 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 1-4 | 15:06:00 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 2-1 | 15:06:05 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 2-1 | 15:06:06 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 2-1 | 15:06:06 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-1 | 15:06:06 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-1 | 15:06:07 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 2-1 | 15:06:07 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-1 | 15:06:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 15:06:08 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-1 | 15:06:09 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-2 | 15:06:15 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-2 | 15:06:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-2 | 15:06:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 15:06:26 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.9700 |  |
| Jogador 2 | 2-3 | 15:06:27 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.3300 |  |
| Jogador 2 | 2-3 | 15:06:27 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 15:06:28 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-3 | 15:06:29 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 2-3 | 15:06:29 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 2-3 | 15:06:30 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-3 | 15:06:30 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 2-3 | 15:06:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-4 | 15:06:39 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 2-4 | 15:06:40 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 2-4 | 15:06:40 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 2-4 | 15:06:41 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-4 | 15:06:41 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-4 | 15:06:41 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-4 | 15:06:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 15:06:43 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.4100 |  |
| Jogador 2 | 2-4 | 15:06:43 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 2-5 | 15:06:54 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-5 | 15:06:54 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-5 | 15:06:54 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 2-5 | 15:06:55 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-5 | 15:06:56 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-5 | 15:06:56 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.3400 |  |
| Jogador 2 | 2-5 | 15:06:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 15:06:57 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-5 | 15:06:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-6 | 15:07:10 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 2-6 | 15:07:11 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 2-6 | 15:07:11 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.5900 |  |
| Jogador 2 | 2-6 | 15:07:12 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-6 | 15:07:13 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-6 | 15:07:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-7 | 15:07:29 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-7 | 15:07:29 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-7 | 15:07:30 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.2500 |  |
| Jogador 2 | 2-7 | 15:07:31 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 2-7 | 15:07:31 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-7 | 15:07:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-7 | 15:07:32 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-7 | 15:07:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-1 | 15:07:49 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-1 | 15:07:49 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | 0.8400 |  |
| Jogador 2 | 3-1 | 15:07:50 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | 0.4200 |  |
| Jogador 2 | 3-1 | 15:07:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | 0.7700 |  |
| Jogador 2 | 3-1 | 15:07:52 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-1 | 15:07:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 15:07:53 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 3-1 | 15:07:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 15:07:53 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-2 | 15:08:09 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-2 | 15:08:10 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 3-2 | 15:08:10 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 15:08:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 15:08:12 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.4300 |  |
| Jogador 2 | 3-2 | 15:08:12 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-2 | 15:08:13 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-2 | 15:08:14 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-2 | 15:08:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 15:08:31 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 3-3 | 15:08:32 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 3-3 | 15:08:32 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.4800 |  |
| Jogador 2 | 3-3 | 15:08:33 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-3 | 15:08:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 15:08:34 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.4900 |  |
| Jogador 2 | 3-3 | 15:08:34 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-3 | 15:08:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 15:08:35 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-4 | 15:08:55 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-4 | 15:08:57 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-4 | 15:08:58 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 3-4 | 15:08:58 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-4 | 15:08:59 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-4 | 15:08:59 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.5700 |  |
| Jogador 2 | 3-4 | 15:09:00 | MOVE Board -> Board: Tristana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-4 | 15:09:01 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-4 | 15:09:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-5 | 15:09:22 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Veigar | 0.2100 |  |
| Jogador 2 | 3-5 | 15:09:23 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.2500 |  |
| Jogador 2 | 3-5 | 15:09:23 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 3-5 | 15:09:24 | MOVE Board -> Board: Rakan (i:2.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-5 | 15:09:24 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-5 | 15:09:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-6 | 15:09:50 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 3-6 | 15:09:50 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Tristana | 0.7500 |  |
| Jogador 2 | 3-6 | 15:09:51 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Tristana | 0.1400 |  |
| Jogador 2 | 3-6 | 15:09:51 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Tristana | 0.5900 |  |
| Jogador 2 | 3-6 | 15:09:52 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 3-6 | 15:09:52 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 3-6 | 15:09:53 | MOVE Board -> Board: Veigar (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 3-6 | 15:09:53 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Veigar | -0.5700 |  |
| Jogador 2 | 3-6 | 15:09:54 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-7 | 15:10:20 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 3-7 | 15:10:20 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 3-7 | 15:10:21 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-7 | 15:10:21 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Veigar | -0.1700 |  |
| Jogador 2 | 3-7 | 15:10:22 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-7 | 15:10:22 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-7 | 15:10:23 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-7 | 15:10:24 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Veigar | -0.3500 |  |
| Jogador 2 | 3-7 | 15:10:24 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 4-1 | 15:10:50 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 4-1 | 15:10:50 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 4-1 | 15:10:51 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 4-1 | 15:10:52 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 4-1 | 15:10:52 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 4-1 | 15:10:53 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 4-1 | 15:10:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 4-1 | 15:10:54 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 4-1 | 15:10:54 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Feérico | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 4-2 | 15:11:22 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-2 | 15:11:23 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Feérico | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 4-2 | 15:11:24 | VENDEU: Malphite (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-2 | 15:11:24 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Feérico | DA_18_Veigar | -0.1700 |  |
| Jogador 2 | 4-2 | 15:11:25 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-2 | 15:11:25 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Feérico | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 4-2 | 15:11:26 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-2 | 15:11:26 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Feérico | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 4-2 | 15:11:27 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-3 | 15:11:54 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 4-3 | 15:11:55 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-3 | 15:11:56 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Feérico | DA_18_Veigar | -0.2600 |  |
| Jogador 2 | 4-3 | 15:11:56 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-3 | 15:11:57 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Feérico | DA_18_Veigar | -0.1900 |  |
| Jogador 2 | 4-3 | 15:11:57 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-3 | 15:11:58 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Feérico | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 4-3 | 15:11:58 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Feérico | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 4-3 | 15:11:59 | MOVE Bench -> Board: Zyra (i:8.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Feérico | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 4-4 | 15:12:29 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Feérico | DA_18_Veigar | 0.8800 |  |
| Jogador 2 | 4-4 | 15:12:30 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Feérico | DA_18_Veigar | -0.1300 |  |
| Jogador 2 | 4-4 | 15:12:30 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 4-4 | 15:12:31 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-4 | 15:12:31 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_18_Veigar | -0.2600 |  |
| Jogador 2 | 4-4 | 15:12:32 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-4 | 15:12:32 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Feérico | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 4-4 | 15:12:33 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-4 | 15:12:33 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Feérico | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 4-5 | 15:13:07 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-5 | 15:13:07 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Feérico | DA_18_Veigar | 0.9000 |  |
| Jogador 2 | 4-5 | 15:13:08 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Feérico | DA_18_Veigar | -0.5500 |  |
| Jogador 2 | 4-5 | 15:13:09 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Feérico | DA_18_Veigar | 0.9600 |  |
| Jogador 2 | 4-5 | 15:13:09 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 4-5 | 15:13:10 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Feérico | DA_18_Veigar | -0.5900 |  |
| Jogador 2 | 4-5 | 15:13:10 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Kobuko (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Feérico | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 4-5 | 15:13:11 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 4-5 | 15:13:11 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-6 | 15:13:47 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Feérico | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 4-6 | 15:13:48 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-6 | 15:13:48 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Feérico | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 4-6 | 15:13:49 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-6 | 15:13:50 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 4-6 | 15:13:50 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-6 | 15:13:51 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Vivaz | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 4-6 | 15:13:51 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-6 | 15:13:52 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Vivaz | DA_18_Veigar | -0.2100 |  |
| Jogador 2 | 4-7 | 15:14:28 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Vivaz | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-7 | 15:14:29 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Vivaz | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 4-7 | 15:14:30 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Vivaz | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-7 | 15:14:30 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Vivaz | DA_18_Veigar | 0.3700 |  |
| Jogador 2 | 4-7 | 15:14:30 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Vivaz | DA_18_Veigar | -0.4700 |  |
| Jogador 2 | 4-7 | 15:14:31 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Vivaz | DA_18_Veigar | 0.3800 |  |
| Jogador 2 | 4-7 | 15:14:32 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Vivaz | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 4-7 | 15:14:32 | COMPROU: Lux (Sabugueiro) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Vivaz | DA_18_Veigar | -0.1700 |  |
| Jogador 2 | 4-7 | 15:14:32 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Vivaz | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-1 | 15:15:10 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Vivaz | DA_18_Veigar | 1.0200 |  |
| Jogador 2 | 5-1 | 15:15:10 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Vivaz | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 5-1 | 15:15:11 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Vivaz | DA_18_Veigar | -0.2200 |  |
| Jogador 2 | 5-1 | 15:15:11 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Vivaz | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 5-1 | 15:15:12 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Vivaz | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 5-1 | 15:15:12 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Vivaz | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 5-1 | 15:15:13 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Vivaz | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 5-1 | 15:15:13 | REROLL | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Vivaz | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | 5-1 | 15:15:14 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Vivaz | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 5-2 | 15:15:51 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Vivaz | DA_18_Veigar | 1.0200 |  |
| Jogador 2 | 5-2 | 15:15:51 | COMPROU: Alune (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Vivaz | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 5-2 | 15:15:52 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Vivaz | DA_18_Veigar | 0.5500 |  |
| Jogador 2 | 5-2 | 15:15:52 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Vivaz | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 5-2 | 15:15:53 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Vivaz | DA_18_Veigar | -0.8500 |  |
| Jogador 2 | 5-2 | 15:15:53 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Vivaz | DA_18_Veigar | -0.1300 |  |
| Jogador 2 | 5-2 | 15:15:54 | MOVE Board -> Board: Azir (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-2 | 15:15:54 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Vivaz | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-2 | 15:15:55 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Vivaz | DA_18_Veigar | -0.1400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-3 | 15:16:35 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Vivaz | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 5-3 | 15:16:36 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Vivaz | DA_18_Veigar | 0.8900 |  |
| Jogador 2 | 5-3 | 15:16:36 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Vivaz | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-3 | 15:16:36 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Vivaz | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 5-3 | 15:16:38 | MOVE Bench -> Board: Zyra (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Vivaz | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 5-3 | 15:16:39 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Vivaz | DA_18_Veigar | -0.4100 |  |
| Jogador 2 | 5-3 | 15:16:39 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Vivaz | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 5-3 | 15:16:40 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Vivaz | DA_18_Veigar | -0.4100 |  |
| Jogador 2 | 5-3 | 15:16:40 | MOVE Bench -> Board: Zyra (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Vivaz | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 5-4 | 15:17:22 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Vivaz | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 5-4 | 15:17:23 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Vivaz | DA_18_Veigar | 0.9300 |  |
| Jogador 2 | 5-4 | 15:17:23 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Vivaz | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 5-4 | 15:17:23 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Vivaz | DA_18_Veigar | 0.9100 |  |
| Jogador 2 | 5-4 | 15:17:24 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Vivaz | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 5-4 | 15:17:24 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Vivaz | DA_18_Veigar | -0.4100 |  |
| Jogador 2 | 5-4 | 15:17:25 | MOVE Bench -> Board: Zyra (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Vivaz | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 5-4 | 15:17:25 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Vivaz | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 5-4 | 15:17:26 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Vivaz | DA_18_Veigar | -0.4100 |  |
| Jogador 2 | 5-5 | 15:18:08 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-5 | 15:18:08 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 114 | 5 | Vivaz | DA_18_Veigar | 1.0200 |  |
| Jogador 2 | 5-5 | 15:18:09 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 111 | 5 | Vivaz | DA_18_Azir | 1.0200 |  |
| Jogador 2 | 5-5 | 15:18:10 | MOVE Bench -> Board: Zyra (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 111 | 5 | Vivaz | DA_18_Azir | 0.1000 |  |
| Jogador 2 | 5-5 | 15:18:10 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 111 | 5 | Vivaz | DA_18_Azir | 0.0500 |  |
| Jogador 2 | 5-5 | 15:18:11 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 111 | 5 | Vivaz | DA_18_Azir | -0.7200 |  |
| Jogador 2 | 5-5 | 15:18:11 | MOVE Bench -> Board: Zyra (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 111 | 5 | Vivaz | DA_18_Azir | 0.0900 |  |
| Jogador 2 | 5-5 | 15:18:12 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 111 | 5 | Vivaz | DA_18_Azir | 0.0500 |  |
| Jogador 2 | 5-5 | 15:18:12 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 111 | 5 | Vivaz | DA_18_Azir | 0.1500 |  |
| Jogador 2 | 5-6 | 15:18:55 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 121 | 5 | Vivaz | DA_18_Azir | 0.0300 |  |
| Jogador 2 | 5-6 | 15:18:56 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 118 | 5 | Vivaz | DA_18_Azir | -0.1000 |  |
| Jogador 2 | 5-6 | 15:18:56 | MOVE Bench -> Board: Krugue (i:6.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 118 | 5 | Vivaz | DA_18_Azir | 0.0400 |  |
| Jogador 2 | 5-6 | 15:18:57 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 118 | 5 | Vivaz | DA_18_Azir | 0.0100 |  |
| Jogador 2 | 5-6 | 15:18:58 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 118 | 5 | Vivaz | DA_18_Azir | 0.0600 |  |
| Jogador 2 | 5-6 | 15:18:58 | MOVE Bench -> Board: Krugue (i:6.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 118 | 5 | Vivaz | DA_18_Azir | 0.0300 |  |
| Jogador 2 | 5-6 | 15:18:58 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 118 | 5 | Vivaz | DA_18_Azir | 0.0000 |  |
| Jogador 2 | 5-6 | 15:18:59 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 118 | 5 | Vivaz | DA_18_Azir | -0.7700 |  |
| Jogador 2 | 5-6 | 15:18:59 | MOVE Bench -> Board: Zyra (i:8.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 118 | 5 | Vivaz | DA_18_Azir | 0.1000 |  |
| Jogador 2 | 5-7 | 15:19:45 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Krugue (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 130 | 5 | Vivaz | DA_18_Azir | 0.0800 |  |
| Jogador 2 | 5-7 | 15:19:46 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 138 | 5 | Vivaz | DA_18_Azir | -0.6000 |  |
| Jogador 2 | 5-7 | 15:19:46 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Vivaz | DA_18_Azir | 0.4400 |  |
| Jogador 2 | 5-7 | 15:19:47 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Vivaz | DA_18_Azir | 0.0200 |  |
| Jogador 2 | 5-7 | 15:19:47 | MOVE Bench -> Board: Krugue (i:6.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Vivaz | DA_18_Azir | -0.7700 |  |
| Jogador 2 | 5-7 | 15:19:48 | MOVE Bench -> Board: Zyra (i:8.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Vivaz | DA_18_Azir | 0.0900 |  |
| Jogador 2 | 5-7 | 15:19:48 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Vivaz | DA_18_Azir | 0.0100 |  |
| Jogador 2 | 5-7 | 15:19:48 | MOVE Bench -> Board: Krugue (i:6.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Vivaz | DA_18_Azir | -0.7700 |  |
| Jogador 2 | 5-7 | 15:19:49 | MOVE Bench -> Board: Zyra (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 135 | 5 | Vivaz | DA_18_Azir | 0.1000 |  |
| Jogador 2 | 6-1 | 15:20:37 | VENDEU: Azir (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 157 | 5 | Vivaz | DA_18_Alune | -0.6000 |  |
| Jogador 2 | 6-1 | 15:20:37 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Vivaz | DA_18_Alune | 0.4300 |  |
| Jogador 2 | 6-1 | 15:20:38 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Vivaz | DA_18_Alune | 0.0800 |  |
| Jogador 2 | 6-1 | 15:20:38 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Vivaz | DA_18_Alune | 0.0100 |  |
| Jogador 2 | 6-1 | 15:20:39 | MOVE Bench -> Board: Krugue (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Vivaz | DA_18_Alune | -0.0100 |  |
| Jogador 2 | 6-1 | 15:20:39 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Vivaz | DA_18_Alune | 0.0700 |  |
| Jogador 2 | 6-1 | 15:20:39 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Vivaz | DA_18_Alune | 0.0100 |  |
| Jogador 2 | 6-1 | 15:20:40 | MOVE Bench -> Board: Krugue (i:6.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Vivaz | DA_18_Alune | -0.7500 |  |
| Jogador 2 | 6-1 | 15:20:40 | MOVE Bench -> Board: Zyra (i:8.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Vivaz | DA_18_Alune | 0.1000 |  |
| Jogador 2 | 6-2 | 15:21:33 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 167 | 5 | Vivaz | DA_18_Alune | 0.0100 |  |
| Jogador 2 | 6-2 | 15:21:33 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 164 | 5 | Vivaz | DA_18_Alune | 0.9900 |  |
| Jogador 2 | 6-2 | 15:21:34 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 164 | 5 | Vivaz | DA_18_Alune | 0.0500 |  |
| Jogador 2 | 6-2 | 15:21:34 | VENDEU: Alune (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 169 | 5 | Vivaz | DA_18_Lux_Elderwood | -0.0600 |  |
| Jogador 2 | 6-2 | 15:21:35 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Vivaz | DA_18_Lux_Elderwood | 0.4500 |  |
| Jogador 2 | 6-2 | 15:21:35 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 169 | 5 | Vivaz | DA_18_Lux_Elderwood | -0.1400 |  |
| Jogador 2 | 6-2 | 15:21:35 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 165 | 5 | Vivaz | DA_18_Lux_Elderwood | 0.4100 |  |
| Jogador 2 | 6-2 | 15:21:36 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 165 | 5 | Vivaz | DA_18_Lux_Elderwood | -0.7700 |  |
| Jogador 2 | 6-2 | 15:21:36 | MOVE Bench -> Board: Zyra (i:8.0) <-> Lux (Sabugueiro) (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 165 | 5 | Vivaz | DA_18_Lux_Elderwood | 0.0900 |  |
| Jogador 2 | 6-3 | 15:22:29 | VENDEU: Lux (Sabugueiro) (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 181 | 5 | Vivaz | DA_18_Zyra | -0.0100 |  |
| Jogador 2 | 6-3 | 15:22:29 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Vivaz | DA_18_Zyra | 0.9600 |  |
| Jogador 2 | 6-3 | 15:22:30 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Vivaz | DA_18_Zyra | 0.1000 |  |
| Jogador 2 | 6-3 | 15:22:30 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Vivaz | DA_18_Zyra | -0.7800 |  |
| Jogador 2 | 6-3 | 15:22:31 | MOVE Bench -> Board: Zyra (i:8.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Vivaz | DA_18_Zyra | -0.3000 |  |
| Jogador 2 | 6-3 | 15:22:31 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Vivaz | DA_18_Zyra | -0.6400 |  |
| Jogador 2 | 6-4 | 15:23:24 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 185 | 5 | Vivaz | DA_18_Zyra | 0.4500 |  |
| Jogador 2 | 6-4 | 15:23:25 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Vivaz | DA_18_Zyra | -0.1400 |  |
| Jogador 2 | 6-4 | 15:23:25 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 187 | 5 | Vivaz | DA_18_Zyra | 0.1700 |  |
| Jogador 2 | 6-4 | 15:23:26 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Vivaz | DA_18_Zyra | -0.0300 |  |
| Jogador 2 | 6-4 | 15:23:28 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 185 | 5 | Vivaz | DA_18_Zyra | -0.2400 |  |
| Jogador 2 | 6-4 | 15:23:28 | MOVE Bench -> Board: Zyra (i:8.0) <-> Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 185 | 5 | Vivaz | DA_18_Zyra | -0.4000 |  |
| Jogador 2 | 6-4 | 15:23:29 | MOVE Bench -> Board: Zyra (i:8.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 185 | 5 | Vivaz | DA_18_Zyra | 0.0800 |  |
| Jogador 2 | 6-4 | 15:23:29 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Vivaz | DA_18_Zyra | 0.0200 |  |
| Jogador 2 | 6-4 | 15:23:30 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 185 | 5 | Vivaz | DA_18_Zyra | -0.2600 |  |
| Jogador 3 | ? | 15:05:25 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | ? | 15:05:27 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | ? | 15:05:27 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | ? | 15:05:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 15:05:32 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 15:05:32 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 15:05:33 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-1 | 15:05:34 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 1-1 | 15:05:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 15:05:37 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-2 | 15:05:40 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 15:05:40 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 15:05:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 15:05:42 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-2 | 15:05:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 15:05:45 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 1-3 | 15:05:48 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 15:05:48 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 15:05:49 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 15:05:49 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 15:05:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 15:05:56 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 1-4 | 15:05:56 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 1-4 | 15:05:57 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 15:05:57 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 15:05:58 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 15:05:59 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 1-4 | 15:06:00 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-1 | 15:06:05 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-1 | 15:06:06 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 15:06:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 15:06:15 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-2 | 15:06:15 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 2-2 | 15:06:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-2 | 15:06:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 15:06:26 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-3 | 15:06:27 | MOVE Bench -> Board: Camille (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | -0.3900 |  |
| Jogador 3 | 2-3 | 15:06:27 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 2-3 | 15:06:28 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 2-3 | 15:06:29 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 2-3 | 15:06:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-3 | 15:06:30 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 15:06:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 15:06:39 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 2-4 | 15:06:40 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-4 | 15:06:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 15:06:54 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-5 | 15:06:54 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 15:06:54 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.1100 |  |
| Jogador 3 | 2-5 | 15:06:55 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 15:06:56 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 2-5 | 15:06:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 2-5 | 15:06:57 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.2700 |  |
| Jogador 3 | 2-5 | 15:06:57 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 2-5 | 15:06:58 | MOVE Board -> Board: Yunara (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 15:07:10 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-6 | 15:07:11 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 2-6 | 15:07:11 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | -0.5800 |  |
| Jogador 3 | 2-6 | 15:07:12 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 2-6 | 15:07:13 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 15:07:13 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 2-6 | 15:07:14 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.5100 |  |
| Jogador 3 | 2-6 | 15:07:15 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.1200 |  |
| Jogador 3 | 2-6 | 15:07:15 | MOVE Board -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 15:07:29 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_SparringGloves -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 2-7 | 15:07:29 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 15:07:30 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.2800 |  |
| Jogador 3 | 2-7 | 15:07:31 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 15:07:31 | MOVE Board -> Board: Akali (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-7 | 15:07:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-7 | 15:07:32 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 15:07:33 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-7 | 15:07:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 15:07:49 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 15:07:49 | MOVE Board -> Board: Akali (i:4.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-1 | 15:07:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-2 | 15:08:09 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 15:08:10 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Akali_AD | 0.8100 |  |
| Jogador 3 | 3-2 | 15:08:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-2 | 15:08:11 | MOVE Board -> Board: Yunara (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-2 | 15:08:12 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 15:08:12 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 15:08:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 15:08:31 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-3 | 15:08:32 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Akali_AD | 0.8000 |  |
| Jogador 3 | 3-3 | 15:08:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-3 | 15:08:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 15:08:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 15:08:34 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 15:08:34 | MOVE Bench -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 3-3 | 15:08:35 | MOVE Board -> Board: Diana (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-3 | 15:08:35 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 3-4 | 15:08:55 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 3-4 | 15:08:57 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.8300 |  |
| Jogador 3 | 3-4 | 15:08:58 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 3-4 | 15:08:58 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 15:08:59 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 15:08:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 15:09:22 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.8400 |  |
| Jogador 3 | 3-5 | 15:09:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 3-5 | 15:09:23 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-5 | 15:09:24 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 15:09:24 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-5 | 15:09:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 15:09:50 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Akali_AD | -0.7500 |  |
| Jogador 3 | 3-6 | 15:09:50 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Vi18 | 0.2000 |  |
| Jogador 3 | 3-6 | 15:09:51 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_Scuttlecrab18 | -0.4900 |  |
| Jogador 3 | 3-6 | 15:09:51 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_Scuttlecrab18 | 0.3700 |  |
| Jogador 3 | 3-6 | 15:09:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_Scuttlecrab18 | -0.1100 |  |
| Jogador 3 | 3-6 | 15:09:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 3-6 | 15:09:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 3-6 | 15:09:53 | MOVE Board -> Board: Akali (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-6 | 15:09:54 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-7 | 15:10:20 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Scuttlecrab18 | 0.7300 |  |
| Jogador 3 | 3-7 | 15:10:20 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Scuttlecrab18 | 0.1100 |  |
| Jogador 3 | 3-7 | 15:10:21 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Scuttlecrab18 | 0.0900 |  |
| Jogador 3 | 3-7 | 15:10:21 | VENDEU: Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 3-7 | 15:10:22 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Scuttlecrab18 | 0.7300 |  |
| Jogador 3 | 3-7 | 15:10:22 | MOVE Board -> Board: Grompe (i:4.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-7 | 15:10:23 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-7 | 15:10:24 | MOVE Board -> Board: Akali (i:4.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 3-7 | 15:10:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-1 | 15:10:50 | MOVE Board -> Board: Diana (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-1 | 15:10:50 | MOVE Board -> Board: Grompe (i:4.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-1 | 15:10:51 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-2 | 15:11:22 | MOVE Board -> Board: Akali (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-2 | 15:11:23 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-2 | 15:11:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 4-3 | 15:11:54 | MOVE Board -> Board: Diana (i:6.0) <-> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-3 | 15:11:55 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 4-3 | 15:11:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 4-4 | 15:12:29 | VENDEU: Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 4-4 | 15:12:30 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Colosso | DA_Scuttlecrab18 | 0.8200 |  |
| Jogador 3 | 4-4 | 15:12:30 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Colosso | DA_Scuttlecrab18 | 0.1500 |  |
| Jogador 3 | 4-4 | 15:12:31 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Colosso | DA_Scuttlecrab18 | 0.1200 |  |
| Jogador 3 | 4-4 | 15:12:31 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-4 | 15:12:32 | MOVE Board -> Board: Diana (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 4-4 | 15:12:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 4-5 | 15:13:07 | VENDEU: Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 2 | Colosso | DA_Scuttlecrab18 | -0.4900 |  |
| Jogador 3 | 4-5 | 15:13:07 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 2 | Colosso | DA_18_Diana | 0.8500 |  |
| Jogador 3 | 4-5 | 15:13:08 | MOVE Bench -> Board: Diana (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 2 | Colosso | DA_18_Diana | 0.3300 |  |
| Jogador 3 | 4-5 | 15:13:09 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 2 | Colosso | DA_18_Diana | 0.2700 |  |
| Jogador 3 | 4-5 | 15:13:09 | MOVE Board -> Board: Diana (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 2 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 4-5 | 15:13:10 | MOVE Board -> Board: Grompe (i:4.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 2 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 4-5 | 15:13:10 | MOVE Board -> Board: Akali (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 2 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 4-5 | 15:13:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 2 | Colosso | DA_18_Diana | -0.0400 |  |
| Jogador 3 | 4-6 | 15:13:47 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Colosso | DA_18_Diana | 0.3000 |  |
| Jogador 3 | 4-6 | 15:13:48 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Diana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 4-6 | 15:13:48 | MOVE Board -> Board: Diana (i:12.0) <-> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 4-6 | 15:13:49 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 4-6 | 15:13:50 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Colosso | DA_18_Diana | -0.0800 |  |
| Jogador 3 | 4-7 | 15:14:28 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Colosso | DA_18_Diana | 0.1500 |  |
| Jogador 3 | 4-7 | 15:14:29 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Colosso | DA_18_Diana | 0.1200 |  |
| Jogador 3 | 4-7 | 15:14:30 | MOVE Board -> Board: Akali (i:4.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 4-7 | 15:14:30 | MOVE Board -> Board: Grompe (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 4-7 | 15:14:30 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Colosso | DA_18_Diana | -0.1000 |  |
| Jogador 3 | 5-1 | 15:15:10 | VENDEU: Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 80 | 5 | Colosso | DA_18_Diana | -0.0400 |  |
| Jogador 3 | 5-1 | 15:15:10 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Colosso | DA_18_Diana | 0.8800 |  |
| Jogador 3 | 5-1 | 15:15:11 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 5-1 | 15:15:11 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Diana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 5-1 | 15:15:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Colosso | DA_18_Diana | -0.1100 |  |
| Jogador 3 | 5-2 | 15:15:51 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Colosso | DA_18_Diana | -0.5900 |  |
| Jogador 3 | 5-2 | 15:15:51 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 87 | 5 | Colosso | DA_18_Diana | 0.8400 |  |
| Jogador 3 | 5-2 | 15:15:52 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Colosso | DA_18_Diana | -0.4300 |  |
| Jogador 3 | 5-2 | 15:15:52 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_18_Diana | 0.6500 |  |
| Jogador 3 | 5-2 | 15:15:53 | MOVE Board -> Board: Diana (i:12.0) <-> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 5-2 | 15:15:53 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 5-2 | 15:15:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_18_Diana | -0.1200 |  |
| Jogador 3 | 5-3 | 15:16:35 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Colosso | DA_18_Diana | -0.5100 |  |
| Jogador 3 | 5-3 | 15:16:36 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Colosso | DA_18_Diana | 0.9500 |  |
| Jogador 3 | 5-3 | 15:16:36 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Colosso | DA_18_Diana | 0.4000 |  |
| Jogador 3 | 5-3 | 15:16:36 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Colosso | DA_18_Diana | 0.2800 |  |
| Jogador 3 | 5-3 | 15:16:38 | MOVE Board -> Board: Akali (i:4.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 5-3 | 15:16:39 | MOVE Board -> Board: Grompe (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 5-3 | 15:16:39 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 5-3 | 15:16:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Colosso | DA_18_Diana | -0.1200 |  |
| Jogador 3 | 5-4 | 15:17:22 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Colosso | DA_18_Diana | -0.6000 |  |
| Jogador 3 | 5-4 | 15:17:23 | COMPROU: Lux (Espinhos Negros) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 107 | 5 | Colosso | DA_18_Diana | 0.1000 |  |
| Jogador 3 | 5-4 | 15:17:23 | VENDEU: Lux (Espinhos Negros) (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Colosso | DA_18_Diana | -0.0500 |  |
| Jogador 3 | 5-4 | 15:17:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Colosso | DA_18_Diana | 0.1500 |  |
| Jogador 3 | 5-4 | 15:17:24 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Colosso | DA_18_Diana | -0.5900 |  |
| Jogador 3 | 5-4 | 15:17:24 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 108 | 5 | Colosso | DA_18_Diana | 0.1500 |  |
| Jogador 3 | 5-4 | 15:17:25 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Colosso | DA_18_Diana | -0.0600 |  |
| Jogador 3 | 5-4 | 15:17:25 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 108 | 5 | Colosso | DA_18_Diana | -0.0800 |  |
| Jogador 3 | 5-4 | 15:17:26 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 108 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 5-5 | 15:18:08 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 123 | 5 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 5-5 | 15:18:08 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 120 | 5 | Colosso | DA_18_Diana | 0.1500 |  |
| Jogador 3 | 5-5 | 15:18:09 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 123 | 5 | Colosso | DA_18_Diana | -0.0600 |  |
| Jogador 3 | 5-5 | 15:18:10 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 120 | 5 | Colosso | DA_18_Diana | -0.0800 |  |
| Jogador 3 | 5-5 | 15:18:10 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 123 | 5 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 5-5 | 15:18:11 | COMPROU: Ahri (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 119 | 5 | Colosso | DA_18_Diana | -0.2500 |  |
| Jogador 3 | 5-5 | 15:18:11 | VENDEU: Ahri (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 123 | 5 | Colosso | DA_18_Diana | 0.0100 |  |
| Jogador 3 | 5-5 | 15:18:12 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Colosso | DA_18_Diana | -0.0900 |  |
| Jogador 3 | 5-5 | 15:18:12 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Diana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 5-6 | 15:18:55 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Colosso | DA_18_Diana | -0.0700 |  |
| Jogador 3 | 5-6 | 15:18:56 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 135 | 5 | Colosso | DA_18_Diana | 0.8700 |  |
| Jogador 3 | 5-6 | 15:18:56 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 137 | 5 | Colosso | DA_18_Diana | -0.3500 |  |
| Jogador 3 | 5-6 | 15:18:57 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Colosso | DA_18_Diana | 0.1500 |  |
| Jogador 3 | 5-6 | 15:18:58 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 137 | 5 | Colosso | DA_18_Diana | -0.0600 |  |
| Jogador 3 | 5-6 | 15:18:58 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Colosso | DA_18_Diana | -0.0500 |  |
| Jogador 3 | 5-6 | 15:18:58 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Colosso | DA_18_Diana | -0.4600 |  |
| Jogador 3 | 5-6 | 15:18:59 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Colosso | DA_18_Diana | -0.0300 |  |
| Jogador 3 | 5-6 | 15:18:59 | MOVE Board -> Board: Diana (i:12.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 5-7 | 15:19:45 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Grompe (i:4.0) (tabuleiro slot 12) | FAST8 | FAST8: composição planejada exige nível 8 | 145 | 5 | Colosso | DA_18_Diana | 0.0400 |  |
| Jogador 3 | 5-7 | 15:19:46 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 5-7 | 15:19:46 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Colosso | DA_18_Diana | 0.3400 |  |
| Jogador 3 | 5-7 | 15:19:47 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Colosso | DA_18_Diana | -0.4300 |  |
| Jogador 3 | 5-7 | 15:19:47 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Colosso | DA_18_Diana | 0.0800 |  |
| Jogador 3 | 5-7 | 15:19:48 | VENDEU: Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Colosso | DA_18_Diana | -0.0400 |  |
| Jogador 3 | 5-7 | 15:19:48 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Colosso | DA_18_Diana | -0.0900 |  |
| Jogador 3 | 5-7 | 15:19:48 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 5-7 | 15:19:49 | COMPROU: Ahri (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 143 | 5 | Colosso | DA_18_Diana | -0.2500 |  |
| Jogador 3 | 6-1 | 15:20:37 | VENDEU: Ahri (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 158 | 5 | Colosso | DA_18_Diana | 0.0100 |  |
| Jogador 3 | 6-1 | 15:20:37 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Colosso | DA_18_Diana | -0.0900 |  |
| Jogador 3 | 6-1 | 15:20:38 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 158 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 6-1 | 15:20:38 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Colosso | DA_18_Diana | -0.2000 |  |
| Jogador 3 | 6-1 | 15:20:39 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 158 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 6-1 | 15:20:39 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 156 | 5 | Colosso | DA_18_Diana | -0.0900 |  |
| Jogador 3 | 6-1 | 15:20:39 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 158 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 6-1 | 15:20:40 | COMPROU: Karma (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Colosso | DA_18_Diana | -0.2700 |  |
| Jogador 3 | 6-1 | 15:20:40 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 6-2 | 15:21:33 | VENDEU: Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 170 | 5 | Colosso | DA_18_Diana | 0.0200 |  |
| Jogador 3 | 6-2 | 15:21:33 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 169 | 5 | Colosso | DA_18_Diana | 1.0000 |  |
| Jogador 3 | 6-2 | 15:21:34 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Colosso | DA_18_Diana | 0.3200 |  |
| Jogador 3 | 6-2 | 15:21:34 | VENDEU: Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 170 | 5 | Colosso | DA_18_Diana | -0.4300 |  |
| Jogador 3 | 6-2 | 15:21:35 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Colosso | DA_18_Diana | -0.0800 |  |
| Jogador 3 | 6-2 | 15:21:35 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Grompe (i:4.0) (tabuleiro slot 12) | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Colosso | DA_18_Diana | 0.0600 |  |
| Jogador 3 | 6-2 | 15:21:35 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Grompe (i:4.0) (tabuleiro slot 12) | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Colosso | DA_18_Diana | 0.0600 |  |
| Jogador 3 | 6-2 | 15:21:36 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 170 | 5 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 6-2 | 15:21:36 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Colosso | DA_18_Diana | -0.2700 |  |
| Jogador 3 | 6-3 | 15:22:29 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 180 | 5 | Colosso | DA_18_Diana | 0.0200 |  |
| Jogador 3 | 6-3 | 15:22:29 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 178 | 5 | Colosso | DA_18_Diana | 0.6300 |  |
| Jogador 3 | 6-3 | 15:22:30 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 180 | 5 | Colosso | DA_18_Diana | -0.1000 |  |
| Jogador 3 | 6-3 | 15:22:30 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 176 | 5 | Colosso | DA_18_Diana | 0.2100 |  |
| Jogador 3 | 6-3 | 15:22:31 | VENDEU: Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 180 | 5 | Colosso | DA_18_Diana | -0.0800 |  |
| Jogador 3 | 6-3 | 15:22:31 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 177 | 5 | Colosso | DA_18_Diana | -0.0300 |  |
| Jogador 3 | 6-3 | 15:22:32 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 180 | 5 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 6-3 | 15:22:32 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 178 | 5 | Colosso | DA_18_Diana | 0.0200 |  |
| Jogador 3 | 6-3 | 15:22:32 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 178 | 5 | Colosso | DA_18_Diana | 0.4200 |  |
| Jogador 3 | 6-4 | 15:23:24 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 185 | 5 | Colosso | DA_18_Diana | 0.1800 |  |
| Jogador 3 | 6-4 | 15:23:25 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 187 | 5 | Colosso | DA_18_Diana | -0.0400 |  |
| Jogador 3 | 6-4 | 15:23:25 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 186 | 5 | Colosso | DA_18_Diana | 0.1200 |  |
| Jogador 3 | 6-4 | 15:23:26 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 187 | 5 | Colosso | DA_18_Diana | -0.0300 |  |
| Jogador 3 | 6-4 | 15:23:28 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 185 | 5 | Colosso | DA_18_Diana | -0.1800 |  |
| Jogador 3 | 6-4 | 15:23:28 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 187 | 5 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 6-4 | 15:23:29 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 186 | 5 | Colosso | DA_18_Diana | -0.2400 |  |
| Jogador 3 | 6-4 | 15:23:29 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 186 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 6-4 | 15:23:30 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 186 | 5 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 6-5 | 15:24:21 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 198 | 5 | Colosso | DA_18_Diana | 0.0200 |  |
| Jogador 3 | 6-5 | 15:24:22 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 194 | 5 | Colosso | DA_18_Diana | 0.3800 |  |
| Jogador 3 | 6-5 | 15:24:22 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Colosso | DA_18_Diana | -0.0500 |  |
| Jogador 3 | 6-5 | 15:24:23 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 195 | 5 | Colosso | DA_18_Diana | 0.1300 |  |
| Jogador 3 | 6-5 | 15:24:23 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Colosso | DA_18_Diana | -0.0400 |  |
| Jogador 3 | 6-5 | 15:24:23 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 196 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 6-5 | 15:24:24 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 6-5 | 15:24:24 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 196 | 5 | Colosso | DA_18_Diana | -0.0500 |  |
| Jogador 3 | 6-5 | 15:24:25 | MOVE Board -> Board: Akali (i:4.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 196 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 4 | ? | 15:05:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | ? | 15:05:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | ? | 15:05:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | ? | 15:05:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 15:05:32 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 15:05:32 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 15:05:33 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-1 | 15:05:34 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 1-1 | 15:05:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 15:05:37 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4600 |  |
| Jogador 4 | 1-2 | 15:05:40 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 15:05:40 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 15:05:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 15:05:42 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-2 | 15:05:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 15:05:48 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 15:05:48 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 15:05:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 15:05:56 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 4 | 1-4 | 15:05:56 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 1-4 | 15:05:57 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-4 | 15:05:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 1-4 | 15:05:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-1 | 15:06:05 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 2-1 | 15:06:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 2-1 | 15:06:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-2 | 15:06:15 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 4 | 2-2 | 15:06:15 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-2 | 15:06:16 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-2 | 15:06:17 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-2 | 15:06:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 15:06:18 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 15:06:18 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 15:06:18 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 4 | 2-2 | 15:06:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 15:06:26 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-3 | 15:06:27 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-3 | 15:06:27 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 4 | 2-3 | 15:06:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-3 | 15:06:29 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-3 | 15:06:29 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 2-3 | 15:06:30 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 2-3 | 15:06:30 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 4 | 2-3 | 15:06:31 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.9500 |  |
| Jogador 4 | 2-4 | 15:06:39 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 1.0000 |  |
| Jogador 4 | 2-4 | 15:06:40 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 2-4 | 15:06:40 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 4 | 2-4 | 15:06:41 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 4 | 2-4 | 15:06:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-4 | 15:06:41 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.6200 |  |
| Jogador 4 | 2-4 | 15:06:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 2-4 | 15:06:43 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 4 | 2-4 | 15:06:43 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 4 | 2-5 | 15:06:54 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 4 | 2-5 | 15:06:54 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 4 | 2-5 | 15:06:54 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.4300 |  |
| Jogador 4 | 2-5 | 15:06:55 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-5 | 15:06:56 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 4 | 2-5 | 15:06:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-5 | 15:06:57 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 4 | 2-5 | 15:06:57 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 4 | 2-5 | 15:06:58 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-6 | 15:07:10 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 1.1200 |  |
| Jogador 4 | 2-6 | 15:07:11 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 4 | 2-6 | 15:07:11 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 4 | 2-6 | 15:07:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-6 | 15:07:13 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 4 | 2-6 | 15:07:13 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 2-6 | 15:07:14 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-6 | 15:07:15 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-6 | 15:07:15 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 4 | 2-7 | 15:07:29 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 2-7 | 15:07:29 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 4 | 2-7 | 15:07:30 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.2700 |  |
| Jogador 4 | 2-7 | 15:07:31 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-7 | 15:07:31 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.4300 |  |
| Jogador 4 | 2-7 | 15:07:32 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 4 | 2-7 | 15:07:32 | MOVE Board -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-7 | 15:07:33 | MOVE Board -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 2-7 | 15:07:33 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-1 | 15:07:49 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 4 | 3-1 | 15:07:49 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-1 | 15:07:50 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 4 | 3-1 | 15:07:51 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 3-1 | 15:07:52 | MOVE Bench -> Board: Rakan (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.3800 |  |
| Jogador 4 | 3-1 | 15:07:52 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.5200 |  |
| Jogador 4 | 3-1 | 15:07:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-1 | 15:07:53 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 4 | 3-1 | 15:07:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-2 | 15:08:09 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-2 | 15:08:10 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 4 | 3-2 | 15:08:10 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 4 | 3-2 | 15:08:11 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 4 | 3-2 | 15:08:12 | MOVE Board -> Board: Rakan (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.1800 |  |
| Jogador 4 | 3-2 | 15:08:12 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-2 | 15:08:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-3 | 15:08:31 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Florescer | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 4 | 3-3 | 15:08:32 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | 0.7200 |  |
| Jogador 4 | 3-3 | 15:08:32 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Sejuani (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 4 | 3-3 | 15:08:33 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Sejuani (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 4 | 3-3 | 15:08:33 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Sejuani (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 4 | 3-3 | 15:08:34 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 3-3 | 15:08:34 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 4 | 3-3 | 15:08:35 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.6800 |  |
| Jogador 4 | 3-3 | 15:08:35 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 15:08:55 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-4 | 15:08:57 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Florescer | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 4 | 3-4 | 15:08:58 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Florescer | DA_KogMaw18_AD | 0.4500 |  |
| Jogador 4 | 3-4 | 15:08:58 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-4 | 15:08:59 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Florescer | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 4 | 3-4 | 15:08:59 | MOVE Bench -> Board: Yunara (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Florescer | DA_KogMaw18_AD | -0.6600 |  |
| Jogador 4 | 3-4 | 15:09:00 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Florescer | DA_KogMaw18_AD | -0.3900 |  |
| Jogador 4 | 3-4 | 15:09:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-5 | 15:09:22 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-5 | 15:09:23 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Florescer | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 4 | 3-5 | 15:09:23 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 15:09:24 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Florescer | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 4 | 3-5 | 15:09:24 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Florescer | DA_KogMaw18_AD | -0.4900 |  |
| Jogador 4 | 3-5 | 15:09:25 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Florescer | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 4 | 3-5 | 15:09:25 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 4 | 3-5 | 15:09:26 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 3-5 | 15:09:26 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Florescer | DA_KogMaw18_AD | -0.4900 |  |
| Jogador 4 | 3-6 | 15:09:50 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Florescer | DA_18_MasterYi_AD | 0.8700 |  |
| Jogador 4 | 3-6 | 15:09:50 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Florescer | DA_18_MasterYi_AD | 0.4000 |  |
| Jogador 4 | 3-6 | 15:09:51 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Florescer | DA_18_MasterYi_AD | -0.1400 |  |
| Jogador 4 | 3-6 | 15:09:51 | MOVE Board -> Board: Sejuani (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Florescer | DA_18_MasterYi_AD | -0.1100 |  |
| Jogador 4 | 3-6 | 15:09:52 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Florescer | DA_18_MasterYi_AD | -0.2400 |  |
| Jogador 4 | 3-6 | 15:09:52 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Florescer | DA_18_MasterYi_AD | 0.1100 |  |
| Jogador 4 | 3-6 | 15:09:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 3-6 | 15:09:53 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Florescer | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 4 | 3-6 | 15:09:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Florescer | DA_18_MasterYi_AD | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-7 | 15:10:20 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Florescer | DA_18_MasterYi_AD | 0.8400 |  |
| Jogador 4 | 3-7 | 15:10:20 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Florescer | DA_18_MasterYi_AD | 0.1700 |  |
| Jogador 4 | 3-7 | 15:10:21 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Florescer | DA_18_MasterYi_AD | 0.2100 |  |
| Jogador 4 | 3-7 | 15:10:21 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_18_MasterYi_AD | 0.3200 |  |
| Jogador 4 | 3-7 | 15:10:22 | MOVE Bench -> Board: Warwick (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_18_MasterYi_AD | -0.4000 |  |
| Jogador 4 | 3-7 | 15:10:22 | MOVE Bench -> Board: Rakan (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_18_MasterYi_AD | -0.6800 |  |
| Jogador 4 | 3-7 | 15:10:23 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_18_MasterYi_AD | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-1 | 15:10:50 | VENDEU: Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 49 | 3 | Florescer | DA_Fiddlesticks18 | -0.5700 |  |
| Jogador 4 | 4-1 | 15:10:50 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Florescer | DA_Fiddlesticks18 | 0.9300 |  |
| Jogador 4 | 4-1 | 15:10:51 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Florescer | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 4 | 4-1 | 15:10:52 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Florescer | DA_Fiddlesticks18 | -0.2400 |  |
| Jogador 4 | 4-1 | 15:10:52 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 49 | 3 | Florescer | DA_Fiddlesticks18 | -0.6200 |  |
| Jogador 4 | 4-1 | 15:10:53 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 51 | 3 | Florescer | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 4 | 4-1 | 15:10:53 | MOVE Bench -> Board: Warwick (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 51 | 3 | Florescer | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 4 | 4-1 | 15:10:54 | MOVE Bench -> Board: Rakan (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 51 | 3 | Florescer | DA_Fiddlesticks18 | -0.7200 |  |
| Jogador 4 | 4-1 | 15:10:54 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 51 | 3 | Florescer | DA_Fiddlesticks18 | -0.2500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-2 | 15:11:22 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_Fiddlesticks18 | 0.4600 |  |
| Jogador 4 | 4-2 | 15:11:23 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 5 | Florescer | DA_Fiddlesticks18 | 0.4200 |  |
| Jogador 4 | 4-2 | 15:11:24 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 5 | Florescer | DA_Fiddlesticks18 | 0.3800 |  |
| Jogador 4 | 4-2 | 15:11:24 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 5 | Florescer | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 4 | 4-2 | 15:11:25 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 54 | 5 | Florescer | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 4 | 4-2 | 15:11:25 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 5 | Florescer | DA_Fiddlesticks18 | -0.5200 |  |
| Jogador 4 | 4-2 | 15:11:26 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 54 | 5 | Florescer | DA_Fiddlesticks18 | 0.9400 |  |
| Jogador 4 | 4-2 | 15:11:26 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 5 | Florescer | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 4 | 4-2 | 15:11:27 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 54 | 5 | Florescer | DA_Fiddlesticks18 | 1.0400 |  |
| Jogador 4 | 4-3 | 15:11:54 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Florescer | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 4 | 4-3 | 15:11:55 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Florescer | DA_Fiddlesticks18 | 0.4000 |  |
| Jogador 4 | 4-3 | 15:11:56 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Florescer | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 4 | 4-3 | 15:11:56 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 55 | 5 | Florescer | DA_Fiddlesticks18 | -0.2100 |  |
| Jogador 4 | 4-3 | 15:11:57 | VENDEU: Yunara (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 60 | 5 | Florescer | DA_Fiddlesticks18 | -0.7000 |  |
| Jogador 4 | 4-3 | 15:11:57 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 5 | Florescer | DA_Fiddlesticks18 | 0.4100 |  |
| Jogador 4 | 4-3 | 15:11:58 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 5 | Florescer | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 4 | 4-3 | 15:11:58 | MOVE Board -> Board: Sejuani (i:4.0) <-> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 5 | Florescer | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 4 | 4-3 | 15:11:59 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 57 | 5 | Florescer | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 4 | 4-4 | 15:12:29 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Florescer | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 4 | 4-4 | 15:12:30 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Florescer | DA_Fiddlesticks18 | 0.9400 |  |
| Jogador 4 | 4-4 | 15:12:30 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Florescer | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 4 | 4-4 | 15:12:31 | COMPROU: Ezreal (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Florescer | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 4 | 4-4 | 15:12:31 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Florescer | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 4 | 4-4 | 15:12:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Florescer | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 4 | 4-4 | 15:12:32 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Florescer | DA_Fiddlesticks18 | -0.3600 |  |
| Jogador 4 | 4-4 | 15:12:33 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Florescer | DA_Fiddlesticks18 | -0.4700 |  |
| Jogador 4 | 4-5 | 15:13:07 | VENDEU: Ezreal (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Florescer | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 4 | 4-5 | 15:13:07 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Florescer | DA_Fiddlesticks18 | 1.0900 |  |
| Jogador 4 | 4-5 | 15:13:08 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Florescer | DA_Fiddlesticks18 | 0.1300 |  |
| Jogador 4 | 4-5 | 15:13:09 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Florescer | DA_Fiddlesticks18 | -0.7700 |  |
| Jogador 4 | 4-5 | 15:13:09 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Florescer | DA_Fiddlesticks18 | 0.6300 |  |
| Jogador 4 | 4-5 | 15:13:10 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Florescer | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 4 | 4-5 | 15:13:10 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Florescer | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 4 | 4-5 | 15:13:11 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Florescer | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 4 | 4-5 | 15:13:11 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Florescer | DA_Fiddlesticks18 | -0.5000 |  |
| Jogador 5 | ? | 15:05:25 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | ? | 15:05:27 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 5 | ? | 15:05:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 15:05:32 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 15:05:32 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 15:05:33 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-1 | 15:05:34 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 15:05:35 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 15:05:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 15:05:37 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4300 |  |
| Jogador 5 | 1-2 | 15:05:40 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 1-2 | 15:05:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 15:05:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 15:05:48 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 15:05:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 15:05:56 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 15:05:56 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 5 | 1-4 | 15:05:57 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 5 | 1-4 | 15:05:57 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 5 | 1-4 | 15:05:58 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 15:05:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 15:06:05 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-1 | 15:06:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 15:06:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 15:06:15 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 5 | 2-2 | 15:06:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 2-2 | 15:06:16 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 5 | 2-2 | 15:06:17 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 15:06:17 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 5 | 2-2 | 15:06:18 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 15:06:18 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0300 |  |
| Jogador 5 | 2-2 | 15:06:18 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-2 | 15:06:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 15:06:26 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.3100 |  |
| Jogador 5 | 2-3 | 15:06:27 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-3 | 15:06:27 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-3 | 15:06:28 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-3 | 15:06:29 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.1700 |  |
| Jogador 5 | 2-3 | 15:06:29 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0800 |  |
| Jogador 5 | 2-3 | 15:06:30 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 15:06:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 15:06:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-4 | 15:06:39 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2900 |  |
| Jogador 5 | 2-4 | 15:06:40 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3400 |  |
| Jogador 5 | 2-4 | 15:06:40 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 2-4 | 15:06:41 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1200 |  |
| Jogador 5 | 2-4 | 15:06:41 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-4 | 15:06:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 15:06:42 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3500 |  |
| Jogador 5 | 2-4 | 15:06:43 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-4 | 15:06:43 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.4000 |  |
| Jogador 5 | 2-5 | 15:06:54 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3600 |  |
| Jogador 5 | 2-5 | 15:06:54 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0900 |  |
| Jogador 5 | 2-5 | 15:06:54 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 15:06:55 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 15:06:56 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-5 | 15:06:56 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 2-5 | 15:06:57 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.4300 |  |
| Jogador 5 | 2-5 | 15:06:57 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-5 | 15:06:58 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-6 | 15:07:10 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Cassiopeia | 1.0400 |  |
| Jogador 5 | 2-6 | 15:07:11 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.3400 |  |
| Jogador 5 | 2-6 | 15:07:11 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.9600 |  |
| Jogador 5 | 2-6 | 15:07:12 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.6300 |  |
| Jogador 5 | 2-6 | 15:07:13 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-6 | 15:07:13 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0700 |  |
| Jogador 5 | 2-6 | 15:07:14 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.6000 |  |
| Jogador 5 | 2-6 | 15:07:15 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-6 | 15:07:15 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.1500 |  |
| Jogador 5 | 2-7 | 15:07:29 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Yunara | 0.7500 |  |
| Jogador 5 | 2-7 | 15:07:29 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Yunara | 0.3500 |  |
| Jogador 5 | 2-7 | 15:07:30 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Yunara | 0.1800 |  |
| Jogador 5 | 2-7 | 15:07:31 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Yunara | 0.1300 |  |
| Jogador 5 | 2-7 | 15:07:31 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Yunara | 0.1100 |  |
| Jogador 5 | 2-7 | 15:07:32 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Tristana | -0.6200 |  |
| Jogador 5 | 2-7 | 15:07:32 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Tristana | 0.1500 |  |
| Jogador 5 | 2-7 | 15:07:33 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | -0.0400 |  |
| Jogador 5 | 2-7 | 15:07:33 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 3-1 | 15:07:49 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Tristana | 0.6900 |  |
| Jogador 5 | 3-1 | 15:07:49 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_18_Tristana | 0.2700 |  |
| Jogador 5 | 3-1 | 15:07:50 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Enfeitiçador | DA_18_Tristana | -0.2300 |  |
| Jogador 5 | 3-1 | 15:07:51 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_18_Tristana | -0.3400 |  |
| Jogador 5 | 3-1 | 15:07:52 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_18_Tristana | -0.4300 |  |
| Jogador 5 | 3-1 | 15:07:52 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Enfeitiçador | DA_18_Tristana | -0.0600 |  |
| Jogador 5 | 3-1 | 15:07:53 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-1 | 15:07:53 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Tristana | -0.3400 |  |
| Jogador 5 | 3-1 | 15:07:53 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_18_Tristana | -0.0700 |  |
| Jogador 5 | 3-2 | 15:08:09 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_Tristana | 0.7200 |  |
| Jogador 5 | 3-2 | 15:08:10 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Tristana | 0.2800 |  |
| Jogador 5 | 3-2 | 15:08:10 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Enfeitiçador | DA_18_Tristana | 0.2800 |  |
| Jogador 5 | 3-2 | 15:08:11 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Enfeitiçador | DA_18_Tristana | 0.0400 |  |
| Jogador 5 | 3-2 | 15:08:12 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 3-2 | 15:08:12 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 1 | Enfeitiçador | DA_18_Tristana | 0.1100 |  |
| Jogador 5 | 3-2 | 15:08:13 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-2 | 15:08:14 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_18_Tristana | -0.3200 |  |
| Jogador 5 | 3-2 | 15:08:14 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_18_Tristana | -0.2600 |  |
| Jogador 5 | 3-3 | 15:08:31 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_18_Tristana | 0.8300 |  |
| Jogador 5 | 3-3 | 15:08:32 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Tristana | 0.7000 |  |
| Jogador 5 | 3-3 | 15:08:32 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_Tristana | 0.0200 |  |
| Jogador 5 | 3-3 | 15:08:33 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Tristana | 0.0600 |  |
| Jogador 5 | 3-3 | 15:08:33 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_18_Tristana | -0.5400 |  |
| Jogador 5 | 3-3 | 15:08:34 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Enfeitiçador | DA_18_Tristana | -0.5400 |  |
| Jogador 5 | 3-3 | 15:08:34 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Enfeitiçador | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 3-3 | 15:08:35 | MOVE Bench -> Board: Yunara (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Enfeitiçador | DA_18_Tristana | -0.3800 |  |
| Jogador 5 | 3-3 | 15:08:35 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Enfeitiçador | DA_18_Tristana | -0.3800 |  |
| Jogador 5 | 3-4 | 15:08:55 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_Tristana | 0.1900 |  |
| Jogador 5 | 3-4 | 15:08:57 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Enfeitiçador | DA_18_Tristana | 0.0600 |  |
| Jogador 5 | 3-4 | 15:08:58 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 3-4 | 15:08:58 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Enfeitiçador | DA_18_Tristana | 0.1500 |  |
| Jogador 5 | 3-4 | 15:08:59 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 3-4 | 15:08:59 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Enfeitiçador | DA_18_Tristana | -0.1500 |  |
| Jogador 5 | 3-4 | 15:09:00 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-4 | 15:09:01 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_18_Tristana | -0.3700 |  |
| Jogador 5 | 3-4 | 15:09:01 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 5 | 3-5 | 15:09:22 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Enfeitiçador | DA_CrimsonRaptor18 | 0.1600 |  |
| Jogador 5 | 3-5 | 15:09:23 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Enfeitiçador | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 5 | 3-5 | 15:09:23 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Enfeitiçador | DA_CrimsonRaptor18 | 0.0300 |  |
| Jogador 5 | 3-5 | 15:09:24 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Enfeitiçador | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 5 | 3-5 | 15:09:24 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Enfeitiçador | DA_CrimsonRaptor18 | -0.3700 |  |
| Jogador 5 | 3-5 | 15:09:25 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Enfeitiçador | DA_18_Azir | -0.0400 |  |
| Jogador 5 | 3-5 | 15:09:25 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_18_Azir | -0.3600 |  |
| Jogador 5 | 3-5 | 15:09:26 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Enfeitiçador | DA_18_Azir | -0.2100 |  |
| Jogador 5 | 3-5 | 15:09:26 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_18_Azir | -0.3400 |  |
| Jogador 5 | 3-6 | 15:09:50 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Azir | 0.9100 |  |
| Jogador 5 | 3-6 | 15:09:50 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Enfeitiçador | DA_18_Azir | 0.3200 |  |
| Jogador 5 | 3-6 | 15:09:51 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 4 | Enfeitiçador | DA_18_Azir | -0.1900 |  |
| Jogador 5 | 3-6 | 15:09:51 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 4 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 3-6 | 15:09:52 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 4 | Enfeitiçador | DA_18_Azir | 0.0100 |  |
| Jogador 5 | 3-6 | 15:09:52 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Enfeitiçador | DA_18_Azir | -0.3600 |  |
| Jogador 5 | 3-6 | 15:09:53 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Azir | -0.3800 |  |
| Jogador 5 | 3-6 | 15:09:53 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Cassiopeia | -0.6400 |  |
| Jogador 5 | 3-6 | 15:09:54 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Enfeitiçador | DA_18_Cassiopeia | -0.0500 |  |
| Jogador 5 | 3-7 | 15:10:20 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Enfeitiçador | DA_18_LeBlanc | 1.0000 |  |
| Jogador 5 | 3-7 | 15:10:20 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 5 | Enfeitiçador | DA_18_LeBlanc | 0.4200 |  |
| Jogador 5 | 3-7 | 15:10:21 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 5 | Enfeitiçador | DA_18_LeBlanc | 0.1200 |  |
| Jogador 5 | 3-7 | 15:10:21 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 5 | Enfeitiçador | DA_18_LeBlanc | 0.1100 |  |
| Jogador 5 | 3-7 | 15:10:22 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 5 | Enfeitiçador | DA_18_LeBlanc | 0.1500 |  |
| Jogador 5 | 3-7 | 15:10:22 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 5 | Enfeitiçador | DA_18_LeBlanc | -0.1800 |  |
| Jogador 5 | 3-7 | 15:10:23 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.6400 |  |
| Jogador 5 | 3-7 | 15:10:24 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 5 | 3-7 | 15:10:24 | MOVE Bench -> Board: Karma (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 5 | 4-1 | 15:10:50 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.9000 |  |
| Jogador 5 | 4-1 | 15:10:50 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 5 | 4-1 | 15:10:51 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.2400 |  |
| Jogador 5 | 4-1 | 15:10:52 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 5 | 4-1 | 15:10:52 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.7300 |  |
| Jogador 5 | 4-1 | 15:10:53 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.4700 |  |
| Jogador 5 | 4-1 | 15:10:53 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.9200 |  |
| Jogador 5 | 4-1 | 15:10:54 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 5 | 4-1 | 15:10:54 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.2400 |  |
| Jogador 5 | 4-2 | 15:11:22 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.9600 |  |
| Jogador 5 | 4-2 | 15:11:23 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.3200 |  |
| Jogador 5 | 4-2 | 15:11:24 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.3200 |  |
| Jogador 5 | 4-2 | 15:11:24 | MOVE Bench -> Board: Yunara (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.3900 |  |
| Jogador 5 | 4-2 | 15:11:25 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.3100 |  |
| Jogador 5 | 4-2 | 15:11:25 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-3 | 15:11:54 | VENDEU: Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 5 | 4-3 | 15:11:55 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 1.0100 |  |
| Jogador 5 | 4-3 | 15:11:56 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 5 | 4-3 | 15:11:56 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.2100 |  |
| Jogador 5 | 4-3 | 15:11:57 | VENDEU: Rek'Sai (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.6800 |  |
| Jogador 5 | 4-3 | 15:11:57 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 5 | 4-3 | 15:11:58 | VENDEU: Karma (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.6800 |  |
| Jogador 5 | 4-3 | 15:11:58 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.3000 |  |
| Jogador 5 | 4-3 | 15:11:59 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 5 | 4-4 | 15:12:29 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 5 | 4-4 | 15:12:30 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.3800 |  |
| Jogador 5 | 4-4 | 15:12:30 | VENDEU: Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 5 | 4-4 | 15:12:31 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1900 |  |
| Jogador 5 | 4-4 | 15:12:31 | VENDEU: Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 5 | 4-4 | 15:12:32 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.2100 |  |
| Jogador 5 | 4-4 | 15:12:32 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 5 | 4-4 | 15:12:33 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.2100 |  |
| Jogador 5 | 4-4 | 15:12:33 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 5 | 4-5 | 15:13:07 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 5 | 4-5 | 15:13:07 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.9800 |  |
| Jogador 5 | 4-5 | 15:13:08 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 5 | 4-5 | 15:13:09 | COMPROU: Kobuko (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.9200 |  |
| Jogador 5 | 4-5 | 15:13:09 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 5 | 4-5 | 15:13:10 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1400 |  |
| Jogador 5 | 4-5 | 15:13:10 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 5 | 4-5 | 15:13:11 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 5 | 4-5 | 15:13:11 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 5 | 4-6 | 15:13:47 | VENDEU: Kayle (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 5 | 4-6 | 15:13:48 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.9200 |  |
| Jogador 5 | 4-6 | 15:13:48 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 5 | 4-6 | 15:13:49 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.6800 |  |
| Jogador 5 | 4-6 | 15:13:50 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 5 | 4-6 | 15:13:50 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.4300 |  |
| Jogador 5 | 4-6 | 15:13:51 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.6300 |  |
| Jogador 5 | 4-6 | 15:13:51 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 5 | 4-6 | 15:13:52 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 5 | 4-7 | 15:14:28 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 1.1100 |  |
| Jogador 5 | 4-7 | 15:14:29 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 5 | 4-7 | 15:14:30 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 5 | 4-7 | 15:14:30 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.2100 |  |
| Jogador 5 | 4-7 | 15:14:30 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.9500 |  |
| Jogador 5 | 4-7 | 15:14:31 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 5 | 4-7 | 15:14:32 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.5900 |  |
| Jogador 5 | 4-7 | 15:14:32 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1900 |  |
| Jogador 5 | 4-7 | 15:14:32 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | ? | 15:05:25 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 15:05:27 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | -0.1500 |  |
| Jogador 6 | ? | 15:05:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 15:05:32 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 15:05:32 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 15:05:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 15:05:37 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2200 |  |
| Jogador 6 | 1-2 | 15:05:40 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 6 | 1-2 | 15:05:40 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 6 | 1-2 | 15:05:40 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 15:05:42 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 15:05:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-2 | 15:05:45 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.5800 |  |
| Jogador 6 | 1-3 | 15:05:48 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0200 |  |
| Jogador 6 | 1-3 | 15:05:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 15:05:56 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 1-4 | 15:05:56 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 6 | 1-4 | 15:05:57 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 6 | 1-4 | 15:05:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 6 | 1-4 | 15:05:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 2-1 | 15:06:05 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-1 | 15:06:06 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-1 | 15:06:06 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-1 | 15:06:06 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-1 | 15:06:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 15:06:15 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-2 | 15:06:15 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-2 | 15:06:16 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-2 | 15:06:17 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 15:06:17 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 15:06:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 15:06:26 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-3 | 15:06:27 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-3 | 15:06:27 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | 0.8100 |  |
| Jogador 6 | 2-3 | 15:06:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 15:06:29 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-3 | 15:06:29 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-3 | 15:06:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 15:06:30 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-3 | 15:06:31 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-4 | 15:06:39 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | 0.8600 |  |
| Jogador 6 | 2-4 | 15:06:40 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Tristana | 0.3100 |  |
| Jogador 6 | 2-4 | 15:06:40 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 15:06:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 15:06:41 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | -0.4800 |  |
| Jogador 6 | 2-4 | 15:06:41 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | -0.4900 |  |
| Jogador 6 | 2-4 | 15:06:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 6 | 2-4 | 15:06:43 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.2100 |  |
| Jogador 6 | 2-4 | 15:06:43 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Yorick | -0.6300 |  |
| Jogador 6 | 2-5 | 15:06:54 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 2-5 | 15:06:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 6 | 2-5 | 15:06:54 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Yorick | -0.1900 |  |
| Jogador 6 | 2-5 | 15:06:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | -0.0600 |  |
| Jogador 6 | 2-5 | 15:06:56 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | 0.0100 |  |
| Jogador 6 | 2-5 | 15:06:56 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Yorick | -1.0200 |  |
| Jogador 6 | 2-5 | 15:06:57 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.1600 |  |
| Jogador 6 | 2-5 | 15:06:57 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.6000 |  |
| Jogador 6 | 2-5 | 15:06:58 | MOVE Board -> Board: Rakan (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 2-6 | 15:07:10 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 6 | 2-6 | 15:07:11 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 6 | 2-6 | 15:07:11 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 6 | 2-6 | 15:07:12 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 2-6 | 15:07:13 | MOVE Board -> Board: Cascalho (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 6 | 2-6 | 15:07:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 2-7 | 15:07:29 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 6 | 2-7 | 15:07:29 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 6 | 2-7 | 15:07:30 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 6 | 2-7 | 15:07:31 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 6 | 2-7 | 15:07:31 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 6 | 2-7 | 15:07:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 2-7 | 15:07:32 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 6 | 2-7 | 15:07:33 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 6 | 2-7 | 15:07:33 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 6 | 3-1 | 15:07:49 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 6 | 3-1 | 15:07:49 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 6 | 3-1 | 15:07:50 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 6 | 3-1 | 15:07:51 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | 0.4500 |  |
| Jogador 6 | 3-1 | 15:07:52 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 6 | 3-1 | 15:07:52 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 6 | 3-1 | 15:07:53 | MOVE Board -> Board: Rakan (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 3-1 | 15:07:53 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 6 | 3-1 | 15:07:53 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 6 | 3-2 | 15:08:09 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 6 | 3-2 | 15:08:10 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 6 | 3-2 | 15:08:10 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | -0.4900 |  |
| Jogador 6 | 3-2 | 15:08:11 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 6 | 3-2 | 15:08:12 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 6 | 3-2 | 15:08:12 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 6 | 3-2 | 15:08:13 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 3-2 | 15:08:14 | MOVE Board -> Board: Tristana (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 3-2 | 15:08:14 | MOVE Board -> Board: Xayah (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 3-3 | 15:08:31 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 6 | 3-3 | 15:08:32 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 6 | 3-3 | 15:08:32 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 6 | 3-3 | 15:08:33 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 6 | 3-3 | 15:08:33 | MOVE Board -> Board: Rakan (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.1300 |  |
| Jogador 6 | 3-3 | 15:08:34 | MOVE Board -> Board: Tristana (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 3-3 | 15:08:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-4 | 15:08:55 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 6 | 3-4 | 15:08:57 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 3-4 | 15:08:58 | MOVE Board -> Board: Xayah (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-4 | 15:08:58 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-4 | 15:08:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-5 | 15:09:22 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 6 | 3-5 | 15:09:23 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_KogMaw18_AD | 0.4600 |  |
| Jogador 6 | 3-5 | 15:09:23 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 6 | 3-5 | 15:09:24 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 6 | 3-5 | 15:09:24 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 6 | 3-5 | 15:09:25 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 6 | 3-5 | 15:09:25 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 6 | 3-5 | 15:09:26 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 6 | 3-5 | 15:09:26 | MOVE Board -> Board: Rakan (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 6 | 3-6 | 15:09:50 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Feérico | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 6 | 3-6 | 15:09:50 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 6 | 3-6 | 15:09:51 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 3-6 | 15:09:51 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 6 | 3-6 | 15:09:52 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 3-6 | 15:09:52 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 6 | 3-6 | 15:09:53 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 6 | 3-6 | 15:09:53 | MOVE Board -> Board: Tristana (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-6 | 15:09:54 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Feérico | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 6 | 3-7 | 15:10:20 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 6 | 3-7 | 15:10:20 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 6 | 3-7 | 15:10:21 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 6 | 3-7 | 15:10:21 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Feérico | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 3-7 | 15:10:22 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 6 | 3-7 | 15:10:22 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_KogMaw18_AD | -0.3400 |  |
| Jogador 6 | 3-7 | 15:10:23 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 6 | 3-7 | 15:10:24 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 3-7 | 15:10:24 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Feérico | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 6 | 4-1 | 15:10:50 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 21 | 1 | Feérico | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 6 | 4-1 | 15:10:50 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Feérico | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 6 | 4-1 | 15:10:51 | MOVE Bench -> Board: Lillia (i:8.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Feérico | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 6 | 4-1 | 15:10:52 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Feérico | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 4-1 | 15:10:52 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Feérico | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 4-1 | 15:10:53 | MOVE Board -> Board: Lillia (i:8.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-1 | 15:10:53 | MOVE Board -> Board: Rakan (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Feérico | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 6 | 4-1 | 15:10:54 | MOVE Board -> Board: Xayah (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-1 | 15:10:54 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Feérico | DA_KogMaw18_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-2 | 15:11:22 | VENDEU: Kayle (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 25 | 1 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-2 | 15:11:23 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Feérico | DA_KogMaw18_AD | 0.3500 |  |
| Jogador 6 | 4-2 | 15:11:24 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 27 | 1 | Feérico | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 4-2 | 15:11:24 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-2 | 15:11:25 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 27 | 1 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-2 | 15:11:25 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Feérico | DA_KogMaw18_AD | -0.2400 |  |
| Jogador 6 | 4-2 | 15:11:26 | MOVE Board -> Board: Tristana (i:6.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-2 | 15:11:26 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Feérico | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 6 | 4-2 | 15:11:27 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Feérico | DA_KogMaw18_AD | -0.3700 |  |
| Jogador 6 | 4-3 | 15:11:54 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Feérico | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 6 | 4-3 | 15:11:55 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Feérico | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 6 | 4-3 | 15:11:56 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 36 | 2 | Feérico | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 6 | 4-3 | 15:11:56 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 34 | 2 | Feérico | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 6 | 4-3 | 15:11:57 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 36 | 2 | Feérico | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 4-3 | 15:11:57 | COMPROU: Varus (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Feérico | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 6 | 4-3 | 15:11:58 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Feérico | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 6 | 4-3 | 15:11:58 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 36 | 2 | Feérico | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 4-3 | 15:11:59 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Feérico | DA_KogMaw18_AD | 0.8700 |  |
| Jogador 6 | 4-4 | 15:12:29 | VENDEU: Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-4 | 15:12:30 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Feérico | DA_18_Tristana | 0.9700 |  |
| Jogador 6 | 4-4 | 15:12:30 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 4-4 | 15:12:31 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Feérico | DA_18_Tristana | 0.5300 |  |
| Jogador 6 | 4-4 | 15:12:31 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 4-4 | 15:12:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Feérico | DA_18_Tristana | 0.1600 |  |
| Jogador 6 | 4-4 | 15:12:32 | MOVE Board -> Board: Rakan (i:4.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 4-4 | 15:12:33 | MOVE Board -> Board: Lillia (i:8.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Feérico | DA_18_Tristana | 0.0100 |  |
| Jogador 6 | 4-4 | 15:12:33 | MOVE Board -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 4-5 | 15:13:07 | VENDEU: Tristana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 3 | Feérico | DA_18_Rakan | -0.5900 |  |
| Jogador 6 | 4-5 | 15:13:07 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 3 | Feérico | DA_Fiddlesticks18 | 1.0000 |  |
| Jogador 6 | 4-5 | 15:13:08 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Feérico | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 6 | 4-5 | 15:13:09 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Feérico | DA_Fiddlesticks18 | -0.2200 |  |
| Jogador 6 | 4-5 | 15:13:09 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Feérico | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 6 | 4-5 | 15:13:10 | VENDEU: Fiddlesticks (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Feérico | DA_18_Rakan | -0.6600 |  |
| Jogador 6 | 4-5 | 15:13:10 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Feérico | DA_18_Rakan | 0.0800 |  |
| Jogador 6 | 4-5 | 15:13:11 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Feérico | DA_18_Rakan | 0.0100 |  |
| Jogador 6 | 4-5 | 15:13:11 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 47 | 3 | Feérico | DA_18_Rakan | -0.0500 |  |
| Jogador 6 | 4-6 | 15:13:47 | VENDEU: Varus (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Feérico | DA_18_Rakan | -0.0300 |  |
| Jogador 6 | 4-6 | 15:13:48 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Feérico | DA_18_Rakan | 1.0500 |  |
| Jogador 6 | 4-6 | 15:13:48 | VENDEU: Xayah (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Feérico | DA_18_Rakan | -0.7000 |  |
| Jogador 6 | 4-6 | 15:13:49 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Feérico | DA_18_Rakan | 0.4600 |  |
| Jogador 6 | 4-6 | 15:13:50 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Rakan (i:4.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Feérico | DA_18_Rakan | 0.1800 |  |
| Jogador 6 | 4-6 | 15:13:50 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Feérico | DA_18_Rakan | 0.1600 |  |
| Jogador 6 | 4-6 | 15:13:51 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Feérico | DA_18_Rakan | 0.8900 |  |
| Jogador 6 | 4-6 | 15:13:51 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Rakan (i:2.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Feérico | DA_18_Rakan | 0.1500 |  |
| Jogador 6 | 4-6 | 15:13:52 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Rakan (i:2.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Feérico | DA_18_Rakan | 0.1400 |  |
| Jogador 6 | 4-7 | 15:14:28 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Feérico | DA_18_Rakan | 0.1900 |  |
| Jogador 6 | 4-7 | 15:14:29 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Feérico | DA_18_Rakan | 0.1100 |  |
| Jogador 6 | 4-7 | 15:14:30 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 4-7 | 15:14:30 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Feérico | DA_18_Rakan | 0.4000 |  |
| Jogador 6 | 4-7 | 15:14:30 | VENDEU: Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 4-7 | 15:14:31 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Feérico | DA_18_Rakan | -0.0600 |  |
| Jogador 6 | 4-7 | 15:14:32 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Feérico | DA_18_Rakan | 0.4000 |  |
| Jogador 6 | 4-7 | 15:14:32 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Feérico | DA_18_Rakan | -0.0300 |  |
| Jogador 6 | 4-7 | 15:14:32 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 5-1 | 15:15:10 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 5-1 | 15:15:10 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Feérico | DA_18_Rakan | 0.7000 |  |
| Jogador 6 | 5-1 | 15:15:11 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 5-1 | 15:15:11 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Feérico | DA_18_Rakan | -0.0400 |  |
| Jogador 6 | 5-1 | 15:15:12 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Feérico | DA_18_Rakan | 0.0100 |  |
| Jogador 6 | 5-1 | 15:15:12 | MOVE Board -> Board: Hecarim (i:6.0) <-> Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 5-1 | 15:15:13 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 5-1 | 15:15:13 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Feérico | DA_18_Rakan | -0.4900 |  |
| Jogador 6 | 5-2 | 15:15:51 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Feérico | DA_18_Rakan | -0.0300 |  |
| Jogador 6 | 5-2 | 15:15:51 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Feérico | DA_18_Rakan | 0.9900 |  |
| Jogador 6 | 5-2 | 15:15:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Feérico | DA_18_Rakan | 0.4400 |  |
| Jogador 6 | 5-2 | 15:15:52 | VENDEU: Master Yi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Feérico | DA_18_Rakan | -0.0800 |  |
| Jogador 6 | 5-2 | 15:15:53 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Feérico | DA_18_Rakan | 0.4000 |  |
| Jogador 6 | 5-2 | 15:15:53 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Feérico | DA_18_Rakan | -0.0700 |  |
| Jogador 6 | 5-2 | 15:15:54 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Feérico | DA_18_Rakan | -0.0400 |  |
| Jogador 6 | 5-2 | 15:15:54 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Feérico | DA_18_Rakan | 1.0200 |  |
| Jogador 6 | 5-2 | 15:15:55 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Feérico | DA_18_Rakan | -0.6200 |  |
| Jogador 7 | ? | 15:05:25 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 15:05:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 15:05:32 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 15:05:32 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 15:05:33 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-1 | 15:05:34 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-1 | 15:05:35 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 15:05:36 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 15:05:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 15:05:37 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 7 | 1-2 | 15:05:40 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 15:05:40 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 15:05:40 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 15:05:42 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 15:05:42 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 15:05:43 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 15:05:48 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-3 | 15:05:48 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 7 | 1-3 | 15:05:49 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 15:05:49 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2000 |  |
| Jogador 7 | 1-3 | 15:05:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 15:05:56 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8300 |  |
| Jogador 7 | 1-4 | 15:05:56 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-4 | 15:05:57 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-4 | 15:05:57 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 7 | 1-4 | 15:05:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 15:06:05 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 15:06:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-1 | 15:06:06 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 15:06:06 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 15:06:07 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 15:06:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-1 | 15:06:08 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | -0.6300 |  |
| Jogador 7 | 2-1 | 15:06:08 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 2-1 | 15:06:09 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Varus (i:2.0) (tabuleiro slot 9) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1500 |  |
| Jogador 7 | 2-2 | 15:06:15 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 1.0500 |  |
| Jogador 7 | 2-2 | 15:06:15 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.6500 |  |
| Jogador 7 | 2-2 | 15:06:16 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1700 |  |
| Jogador 7 | 2-2 | 15:06:17 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 15:06:17 | VENDEU: Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | -0.6200 |  |
| Jogador 7 | 2-2 | 15:06:18 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1400 |  |
| Jogador 7 | 2-2 | 15:06:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Hecarim | 0.0200 |  |
| Jogador 7 | 2-2 | 15:06:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-3 | 15:06:26 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Hecarim | 0.3100 |  |
| Jogador 7 | 2-3 | 15:06:27 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.2600 |  |
| Jogador 7 | 2-3 | 15:06:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 15:06:39 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.2900 |  |
| Jogador 7 | 2-4 | 15:06:40 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.3100 |  |
| Jogador 7 | 2-4 | 15:06:40 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 15:06:41 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-4 | 15:06:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 15:06:54 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 0.9100 |  |
| Jogador 7 | 2-5 | 15:06:54 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.8900 |  |
| Jogador 7 | 2-5 | 15:06:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 15:06:55 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 15:06:56 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.4800 |  |
| Jogador 7 | 2-5 | 15:06:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 15:06:57 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 15:06:57 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-5 | 15:06:58 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.4800 |  |
| Jogador 7 | 2-6 | 15:07:10 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Sentinel18 | -0.2700 |  |
| Jogador 7 | 2-6 | 15:07:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 2-6 | 15:07:11 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.4600 |  |
| Jogador 7 | 2-6 | 15:07:12 | MOVE Board -> Board: Azuporã (i:8.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-6 | 15:07:13 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-6 | 15:07:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-7 | 15:07:29 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Sentinel18 | 0.2800 |  |
| Jogador 7 | 2-7 | 15:07:29 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 2-7 | 15:07:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-7 | 15:07:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-7 | 15:07:31 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-7 | 15:07:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-1 | 15:07:49 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | 0.2800 |  |
| Jogador 7 | 3-1 | 15:07:49 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-1 | 15:07:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-2 | 15:08:09 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.2700 |  |
| Jogador 7 | 3-2 | 15:08:10 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.2000 |  |
| Jogador 7 | 3-2 | 15:08:10 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 3-2 | 15:08:11 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 3-2 | 15:08:12 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 3-2 | 15:08:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-2 | 15:08:13 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.1300 |  |
| Jogador 7 | 3-2 | 15:08:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-2 | 15:08:14 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-3 | 15:08:31 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Sentinel18 | 0.8400 |  |
| Jogador 7 | 3-3 | 15:08:32 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 7 | 3-3 | 15:08:32 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 7 | 3-3 | 15:08:33 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 7 | 3-3 | 15:08:33 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-3 | 15:08:34 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 3-3 | 15:08:34 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Hecarim (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 3-3 | 15:08:35 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Hecarim (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 7 | 3-3 | 15:08:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-4 | 15:08:55 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.7700 |  |
| Jogador 7 | 3-4 | 15:08:57 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 7 | 3-4 | 15:08:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 7 | 3-4 | 15:08:58 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 7 | 3-4 | 15:08:59 | MOVE Board -> Board: Xayah (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-4 | 15:08:59 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-4 | 15:09:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-4 | 15:09:01 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.5700 |  |
| Jogador 7 | 3-5 | 15:09:22 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 7 | 3-5 | 15:09:23 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-5 | 15:09:23 | MOVE Board -> Board: Yorick (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 3-5 | 15:09:24 | MOVE Board -> Board: Xayah (i:2.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-5 | 15:09:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-6 | 15:09:50 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_KogMaw18_AD | 0.7200 |  |
| Jogador 7 | 3-6 | 15:09:50 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 7 | 3-6 | 15:09:51 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.5800 |  |
| Jogador 7 | 3-6 | 15:09:51 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 3-6 | 15:09:52 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-6 | 15:09:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-7 | 15:10:20 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 3-7 | 15:10:20 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 7 | 3-7 | 15:10:21 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 3-7 | 15:10:21 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.2200 |  |
| Jogador 7 | 3-7 | 15:10:22 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-7 | 15:10:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-7 | 15:10:23 | MOVE Board -> Board: Hecarim (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-7 | 15:10:24 | MOVE Board -> Board: Yorick (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 3-7 | 15:10:24 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 4-1 | 15:10:50 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.2700 |  |
| Jogador 7 | 4-1 | 15:10:50 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-1 | 15:10:51 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-1 | 15:10:52 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 7 | 4-1 | 15:10:52 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-1 | 15:10:53 | MOVE Board -> Board: Yorick (i:2.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-1 | 15:10:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-2 | 15:11:22 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Colosso | DA_Sentinel18 | -0.5700 |  |
| Jogador 7 | 4-2 | 15:11:23 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Cassiopeia (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Colosso | DA_Sentinel18 | 0.0800 |  |
| Jogador 7 | 4-2 | 15:11:24 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Colosso | DA_Sentinel18 | -0.1400 |  |
| Jogador 7 | 4-2 | 15:11:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 4-2 | 15:11:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 4-2 | 15:11:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-2 | 15:11:26 | MOVE Board -> Board: Hecarim (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-2 | 15:11:26 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-2 | 15:11:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-3 | 15:11:54 | VENDEU: Azuporã (i:16.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 0 | Colosso | DA_18_Soraka | -0.4900 |  |
| Jogador 7 | 4-3 | 15:11:55 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Colosso | DA_18_Soraka | 0.8200 |  |
| Jogador 7 | 4-3 | 15:11:56 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 0 | Colosso | DA_18_Soraka | 0.0100 |  |
| Jogador 7 | 4-3 | 15:11:56 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Colosso | DA_18_Soraka | 0.7800 |  |
| Jogador 7 | 4-3 | 15:11:57 | MOVE Board -> Board: Yorick (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 7 | 4-3 | 15:11:57 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Colosso | DA_18_Soraka | -0.0200 |  |
| Jogador 7 | 4-3 | 15:11:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Colosso | DA_18_Soraka | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-4 | 15:12:29 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Soraka | -0.0400 |  |
| Jogador 7 | 4-4 | 15:12:30 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 7 | 4-4 | 15:12:30 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Colosso | DA_18_Soraka | 0.0300 |  |
| Jogador 7 | 4-4 | 15:12:31 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Soraka | 0.1700 |  |
| Jogador 7 | 4-4 | 15:12:31 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Colosso | DA_18_Soraka | -0.0400 |  |
| Jogador 7 | 4-4 | 15:12:32 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Soraka | 0.1700 |  |
| Jogador 7 | 4-4 | 15:12:32 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 7 | 4-4 | 15:12:33 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Soraka | -0.0200 |  |
| Jogador 7 | 4-4 | 15:12:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Soraka | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-5 | 15:13:07 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Colosso | DA_18_Soraka | -0.0500 |  |
| Jogador 7 | 4-5 | 15:13:07 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_18_Soraka | -0.0900 |  |
| Jogador 7 | 4-5 | 15:13:08 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Colosso | DA_18_Soraka | -0.0200 |  |
| Jogador 7 | 4-5 | 15:13:09 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Soraka | 0.0600 |  |
| Jogador 7 | 4-5 | 15:13:09 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 7 | 4-5 | 15:13:10 | MOVE Board -> Board: Yorick (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Soraka | -0.0200 |  |
| Jogador 7 | 4-5 | 15:13:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Soraka | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-6 | 15:13:47 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Colosso | DA_18_Soraka | -0.0300 |  |
| Jogador 7 | 4-6 | 15:13:48 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Colosso | DA_18_Hecarim | 0.9600 |  |
| Jogador 7 | 4-6 | 15:13:48 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_18_Hecarim | 0.9600 |  |
| Jogador 7 | 4-6 | 15:13:49 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_18_Hecarim | 0.3400 |  |
| Jogador 7 | 4-6 | 15:13:50 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Colosso | DA_18_Hecarim | -0.1500 |  |
| Jogador 7 | 4-6 | 15:13:50 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Colosso | DA_18_Hecarim | 0.3200 |  |
| Jogador 7 | 4-6 | 15:13:51 | MOVE Board -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Colosso | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-6 | 15:13:51 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Colosso | DA_18_Hecarim | -0.0200 |  |
| Jogador 7 | 4-6 | 15:13:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Colosso | DA_18_Hecarim | -0.1900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-7 | 15:14:28 | COMPROU: Ashe (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Colosso | DA_18_Hecarim | 0.0500 |  |
| Jogador 7 | 4-7 | 15:14:29 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Colosso | DA_18_Hecarim | 0.1400 |  |
| Jogador 7 | 4-7 | 15:14:30 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Colosso | DA_18_Hecarim | 0.1500 |  |
| Jogador 7 | 4-7 | 15:14:30 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_18_Hecarim | 0.0400 |  |
| Jogador 7 | 4-7 | 15:14:30 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-7 | 15:14:31 | MOVE Board -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_18_Hecarim | -0.0200 |  |
| Jogador 7 | 4-7 | 15:14:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_18_Hecarim | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 5-1 | 15:15:10 | VENDEU: Hecarim (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 70 | 5 | Colosso | DA_18_Ashe | -0.6000 |  |
| Jogador 7 | 5-1 | 15:15:10 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Colosso | DA_18_Ashe | 0.5100 |  |
| Jogador 7 | 5-1 | 15:15:11 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Yorick (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Colosso | DA_18_Ashe | 0.1000 |  |
| Jogador 7 | 5-1 | 15:15:11 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Yorick (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Colosso | DA_18_Ashe | 0.1500 |  |
| Jogador 7 | 5-1 | 15:15:12 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_18_Ashe | -0.0400 |  |
| Jogador 7 | 5-1 | 15:15:12 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Colosso | DA_18_Ashe | 0.0200 |  |
| Jogador 7 | 5-1 | 15:15:13 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Colosso | DA_18_Ashe | 0.0000 |  |
| Jogador 7 | 5-1 | 15:15:13 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_18_Ashe | -0.0200 |  |
| Jogador 7 | 5-1 | 15:15:14 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Colosso | DA_18_Ashe | 0.0200 |  |
| Jogador 7 | 5-2 | 15:15:51 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 82 | 5 | Colosso | DA_18_Ashe | -0.0300 |  |
| Jogador 7 | 5-2 | 15:15:51 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Colosso | DA_18_Ashe | -0.2200 |  |
| Jogador 7 | 5-2 | 15:15:52 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 82 | 5 | Colosso | DA_18_Ashe | 0.0000 |  |
| Jogador 7 | 5-2 | 15:15:52 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Colosso | DA_18_Ashe | 0.0200 |  |
| Jogador 7 | 5-2 | 15:15:53 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 82 | 5 | Colosso | DA_18_Ashe | -0.0100 |  |
| Jogador 7 | 5-2 | 15:15:53 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Colosso | DA_18_Ashe | -0.2400 |  |
| Jogador 7 | 5-2 | 15:15:54 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 82 | 5 | Colosso | DA_18_Ashe | 0.0100 |  |
| Jogador 7 | 5-2 | 15:15:54 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Colosso | DA_18_Ashe | -0.2400 |  |
| Jogador 7 | 5-2 | 15:15:55 | MOVE Board -> Board: Ezreal (i:8.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Colosso | DA_18_Ashe | 0.0000 |  |
| Jogador 7 | 5-3 | 15:16:35 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 92 | 5 | Colosso | DA_18_Ashe | 0.0100 |  |
| Jogador 7 | 5-3 | 15:16:36 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 89 | 5 | Colosso | DA_18_Ashe | -0.0600 |  |
| Jogador 7 | 5-3 | 15:16:36 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 92 | 5 | Colosso | DA_18_Ashe | -0.0300 |  |
| Jogador 7 | 5-3 | 15:16:36 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Colosso | DA_18_Ashe | 0.0400 |  |
| Jogador 7 | 5-3 | 15:16:38 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 92 | 5 | Colosso | DA_18_Ashe | -0.0400 |  |
| Jogador 7 | 5-3 | 15:16:39 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Colosso | DA_18_Ashe | 0.1200 |  |
| Jogador 7 | 5-3 | 15:16:39 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Colosso | DA_18_Ashe | 0.0000 |  |
| Jogador 7 | 5-3 | 15:16:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Colosso | DA_18_Ashe | -0.0100 |  |
| Jogador 7 | 5-3 | 15:16:40 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Colosso | DA_18_Ashe | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 5-4 | 15:17:22 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Colosso | DA_18_Ashe | -0.0400 |  |
| Jogador 7 | 5-4 | 15:17:23 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Colosso | DA_18_Ashe | 0.9300 |  |
| Jogador 7 | 5-4 | 15:17:23 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Colosso | DA_18_Ashe | -0.4600 |  |
| Jogador 7 | 5-4 | 15:17:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Colosso | DA_18_Ashe | -0.0600 |  |
| Jogador 7 | 5-4 | 15:17:24 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Colosso | DA_18_Ashe | -0.0200 |  |
| Jogador 7 | 5-4 | 15:17:24 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 100 | 5 | Colosso | DA_18_Ashe | 0.1300 |  |
| Jogador 7 | 5-4 | 15:17:25 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Colosso | DA_18_Ashe | -0.0400 |  |
| Jogador 7 | 5-4 | 15:17:25 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 101 | 5 | Colosso | DA_18_Ashe | -0.1900 |  |
| Jogador 7 | 5-4 | 15:17:26 | MOVE Board -> Board: Yorick (i:2.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 101 | 5 | Colosso | DA_18_Ashe | 0.0000 |  |
| Jogador 7 | 5-5 | 15:18:08 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Colosso | DA_18_Ashe | -0.0100 |  |
| Jogador 7 | 5-5 | 15:18:08 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Colosso | DA_18_Ashe | 0.1300 |  |
| Jogador 7 | 5-5 | 15:18:09 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Colosso | DA_18_Ashe | -0.0500 |  |
| Jogador 7 | 5-5 | 15:18:10 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 110 | 5 | Colosso | DA_18_Ashe | 0.0400 |  |
| Jogador 7 | 5-5 | 15:18:10 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Colosso | DA_18_Ashe | -0.0200 |  |
| Jogador 7 | 5-5 | 15:18:11 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 110 | 5 | Colosso | DA_18_Ashe | 0.0300 |  |
| Jogador 7 | 5-5 | 15:18:11 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Colosso | DA_18_Ashe | -0.0300 |  |
| Jogador 7 | 5-5 | 15:18:12 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Colosso | DA_18_Ashe | 0.0400 |  |
| Jogador 7 | 5-5 | 15:18:12 | REROLL | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 109 | 5 | Colosso | DA_18_Ashe | -0.1600 |  |
| Jogador 7 | 5-6 | 15:18:55 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 123 | 5 | Colosso | DA_18_Ashe | -0.0300 |  |
| Jogador 7 | 5-6 | 15:18:56 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 121 | 5 | Colosso | DA_18_Ashe | 0.8500 |  |
| Jogador 7 | 5-6 | 15:18:56 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 123 | 5 | Colosso | DA_18_Ashe | -0.5900 |  |
| Jogador 7 | 5-6 | 15:18:57 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 119 | 5 | Colosso | DA_18_Ashe | 0.6400 |  |
| Jogador 7 | 5-6 | 15:18:58 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 123 | 5 | Colosso | DA_18_Ashe | -0.4900 |  |
| Jogador 7 | 5-6 | 15:18:58 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 121 | 5 | Colosso | DA_18_Ashe | 0.1200 |  |
| Jogador 7 | 5-6 | 15:18:58 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 123 | 5 | Colosso | DA_18_Ashe | -0.0500 |  |
| Jogador 7 | 5-6 | 15:18:59 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 120 | 5 | Colosso | DA_18_Ashe | 0.0400 |  |
| Jogador 7 | 5-6 | 15:18:59 | REROLL | STABILIZE | STABILIZE: pressão de vida | 118 | 5 | Colosso | DA_18_Ashe | -0.1600 |  |
| Jogador 7 | 5-7 | 15:19:45 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Yorick (i:2.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Colosso | DA_18_Ashe | 0.1400 |  |
| Jogador 7 | 5-7 | 15:19:46 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 132 | 5 | Colosso | DA_18_Ashe | -0.0200 |  |
| Jogador 7 | 5-7 | 15:19:46 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Colosso | DA_18_Ashe | 1.0800 |  |
| Jogador 7 | 5-7 | 15:19:47 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Colosso | DA_18_Ashe | 0.1900 |  |
| Jogador 7 | 5-7 | 15:19:47 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Colosso | DA_18_Ashe | 0.5200 |  |
| Jogador 7 | 5-7 | 15:19:48 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 123 | 5 | Colosso | DA_18_Ashe | 0.0900 |  |
| Jogador 7 | 5-7 | 15:19:48 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 131 | 5 | Colosso | DA_18_Ashe | -0.6000 |  |
| Jogador 7 | 5-7 | 15:19:48 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Colosso | DA_18_Ashe | -0.2400 |  |
| Jogador 7 | 5-7 | 15:19:49 | MOVE Board -> Board: Vi (i:6.0) <-> Ezreal (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Colosso | DA_18_Ashe | 0.0000 |  |
| Jogador 7 | 6-1 | 15:20:37 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Colosso | DA_18_Ashe | 0.0100 |  |
| Jogador 7 | 6-1 | 15:20:37 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Colosso | DA_18_Ashe | 0.2100 |  |
| Jogador 7 | 6-1 | 15:20:38 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Colosso | DA_18_Ashe | -0.0500 |  |
| Jogador 7 | 6-1 | 15:20:38 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_18_Ashe | -0.1400 |  |
| Jogador 7 | 6-1 | 15:20:39 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Colosso | DA_18_Ashe | -0.0300 |  |
| Jogador 7 | 6-1 | 15:20:39 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Colosso | DA_18_Ashe | -0.0300 |  |
| Jogador 7 | 6-1 | 15:20:39 | VENDEU: Rubrivira (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Colosso | DA_18_Ashe | 0.0000 |  |
| Jogador 7 | 6-1 | 15:20:40 | COMPROU: Alistar (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Colosso | DA_18_Ashe | 0.0400 |  |
| Jogador 7 | 6-1 | 15:20:40 | VENDEU: Alistar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Colosso | DA_18_Ashe | -0.0300 |  |
| Jogador 7 | 6-2 | 15:21:33 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 149 | 5 | Colosso | DA_18_Ashe | 0.4600 |  |
| Jogador 7 | 6-2 | 15:21:33 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Colosso | DA_18_Ashe | -0.0600 |  |
| Jogador 7 | 6-2 | 15:21:34 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Colosso | DA_18_Ashe | 0.4300 |  |
| Jogador 7 | 6-2 | 15:21:34 | VENDEU: Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Colosso | DA_18_Ashe | -0.0200 |  |
| Jogador 7 | 6-2 | 15:21:35 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 151 | 5 | Colosso | DA_18_Ashe | 0.1300 |  |
| Jogador 7 | 6-2 | 15:21:35 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Colosso | DA_18_Ashe | -0.0300 |  |
| Jogador 7 | 6-2 | 15:21:35 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Colosso | DA_18_Ashe | 0.0600 |  |
| Jogador 7 | 6-2 | 15:21:36 | VENDEU: Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Colosso | DA_18_Ashe | -0.0200 |  |
| Jogador 7 | 6-2 | 15:21:36 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Colosso | DA_18_Ashe | -0.0500 |  |
| Jogador 7 | 6-3 | 15:22:29 | VENDEU: Cascalho (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 165 | 5 | Colosso | DA_18_Ashe | 0.0100 |  |
| Jogador 7 | 6-3 | 15:22:29 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 162 | 5 | Colosso | DA_18_Ashe | 0.9800 |  |
| Jogador 7 | 6-3 | 15:22:30 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 164 | 5 | Colosso | DA_18_Ashe | -0.6500 |  |
| Jogador 7 | 6-3 | 15:22:30 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Colosso | DA_18_Ashe | 1.1100 |  |
| Jogador 7 | 6-3 | 15:22:31 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Colosso | DA_18_Ashe | 0.2400 |  |
| Jogador 7 | 6-3 | 15:22:31 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Colosso | DA_18_Ashe | 0.0100 |  |
| Jogador 7 | 6-3 | 15:22:32 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Mamãe Bicuda (i:6.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Colosso | DA_18_Ashe | 0.1400 |  |
| Jogador 7 | 6-3 | 15:22:32 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Mamãe Bicuda (i:6.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Colosso | DA_18_Ashe | 0.0700 |  |
| Jogador 7 | 6-3 | 15:22:32 | VENDEU: Yorick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 162 | 5 | Colosso | DA_18_Ashe | -0.7100 |  |
| Jogador 7 | 6-4 | 15:23:24 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 170 | 5 | Colosso | DA_18_Ashe | 1.1100 |  |
| Jogador 7 | 6-4 | 15:23:25 | MOVE Bench -> Board: Ahri (i:8.0) <-> Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 170 | 5 | Colosso | DA_18_Ashe | -0.7500 |  |
| Jogador 7 | 6-4 | 15:23:25 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Colosso | DA_18_Ashe | 0.2200 |  |
| Jogador 7 | 6-4 | 15:23:26 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Ezreal (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Colosso | DA_18_Ashe | 0.1000 |  |
| Jogador 7 | 6-4 | 15:23:28 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Colosso | DA_18_Ashe | 0.0100 |  |
| Jogador 7 | 6-4 | 15:23:28 | MOVE Bench -> Board: Ahri (i:8.0) <-> Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Colosso | DA_18_Ashe | -0.7600 |  |
| Jogador 7 | 6-4 | 15:23:29 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Ezreal (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Colosso | DA_18_Ashe | 0.0800 |  |
| Jogador 7 | 6-4 | 15:23:29 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Colosso | DA_18_Ashe | 0.0100 |  |
| Jogador 7 | 6-4 | 15:23:30 | MOVE Bench -> Board: Ashe (i:10.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Colosso | DA_18_Ashe | 0.1500 |  |
| Jogador 7 | 6-5 | 15:24:21 | COMPROU: Ezreal (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 173 | 5 | Colosso | DA_18_Ashe | 0.7600 |  |
| Jogador 7 | 6-5 | 15:24:22 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Mamãe Bicuda (i:6.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 173 | 5 | Colosso | DA_18_Ashe | 0.1400 |  |
| Jogador 7 | 6-5 | 15:24:22 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Xayah (i:2.0) (tabuleiro slot 23) | ALL_IN | HP crítico: gastar para sobreviver | 173 | 5 | Colosso | DA_18_Ashe | 0.0800 |  |
| Jogador 7 | 6-5 | 15:24:23 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Xayah (i:2.0) (tabuleiro slot 23) | ALL_IN | HP crítico: gastar para sobreviver | 173 | 5 | Colosso | DA_18_Ashe | 0.0600 |  |
| Jogador 7 | 6-5 | 15:24:23 | VENDEU: Vi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 181 | 5 | Colosso | DA_18_Ashe | -0.7200 |  |
| Jogador 7 | 6-5 | 15:24:23 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Colosso | DA_18_Ashe | 0.7700 |  |
| Jogador 7 | 6-5 | 15:24:24 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 182 | 5 | Colosso | DA_18_Ashe | -0.0400 |  |
| Jogador 7 | 6-5 | 15:24:24 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Colosso | DA_18_Ashe | 0.0800 |  |
| Jogador 7 | 6-5 | 15:24:25 | MOVE Bench -> Board: Lillia (i:8.0) <-> Ezreal (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 178 | 5 | Colosso | DA_18_Ashe | -0.0900 |  |
| Jogador 8 | ? | 15:05:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | ? | 15:05:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | ? | 15:05:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 15:05:32 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 15:05:32 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-1 | 15:05:33 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-1 | 15:05:34 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3600 |  |
| Jogador 8 | 1-1 | 15:05:35 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-1 | 15:05:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 15:05:37 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5000 |  |
| Jogador 8 | 1-2 | 15:05:40 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 8 | 1-2 | 15:05:40 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 8 | 1-2 | 15:05:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 15:05:48 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-3 | 15:05:48 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 8 | 1-3 | 15:05:49 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1700 |  |
| Jogador 8 | 1-3 | 15:05:49 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 8 | 1-3 | 15:05:50 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 8 | 1-3 | 15:05:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 15:05:56 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.1100 |  |
| Jogador 8 | 1-4 | 15:05:56 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 1-4 | 15:05:57 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 1-4 | 15:05:57 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 1-4 | 15:05:58 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 1.1000 |  |
| Jogador 8 | 1-4 | 15:05:59 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 1-4 | 15:06:00 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 2-1 | 15:06:05 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-1 | 15:06:06 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.2100 |  |
| Jogador 8 | 2-1 | 15:06:06 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 2-1 | 15:06:06 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 2-1 | 15:06:07 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 2-1 | 15:06:07 | MOVE Board -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 2-1 | 15:06:08 | MOVE Bench -> Board: Teemo (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.5200 |  |
| Jogador 8 | 2-1 | 15:06:08 | MOVE Bench -> Board: Karma (i:4.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-1 | 15:06:09 | MOVE Bench -> Board: Xayah (i:4.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1500 |  |
| Jogador 8 | 2-2 | 15:06:15 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.9800 |  |
| Jogador 8 | 2-2 | 15:06:15 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.9500 |  |
| Jogador 8 | 2-2 | 15:06:16 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.3300 |  |
| Jogador 8 | 2-2 | 15:06:17 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 2-2 | 15:06:17 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.2700 |  |
| Jogador 8 | 2-2 | 15:06:18 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.4300 |  |
| Jogador 8 | 2-2 | 15:06:18 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.2300 |  |
| Jogador 8 | 2-2 | 15:06:18 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | -0.2200 |  |
| Jogador 8 | 2-2 | 15:06:19 | MOVE Bench -> Board: Teemo (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 2-3 | 15:06:26 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Karma18 | 0.8800 |  |
| Jogador 8 | 2-3 | 15:06:27 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-3 | 15:06:27 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-3 | 15:06:28 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | -0.5800 |  |
| Jogador 8 | 2-3 | 15:06:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-3 | 15:06:29 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-3 | 15:06:30 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.1700 |  |
| Jogador 8 | 2-3 | 15:06:30 | MOVE Board -> Board: Kobuko (i:2.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-3 | 15:06:31 | MOVE Board -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 2-4 | 15:06:39 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_Karma18 | 0.9000 |  |
| Jogador 8 | 2-4 | 15:06:40 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-4 | 15:06:40 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_Karma18 | 0.6000 |  |
| Jogador 8 | 2-4 | 15:06:41 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 2-4 | 15:06:41 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_Karma18 | 0.1300 |  |
| Jogador 8 | 2-4 | 15:06:41 | MOVE Bench -> Board: Warwick (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_Karma18 | -0.3700 |  |
| Jogador 8 | 2-4 | 15:06:42 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 2-4 | 15:06:43 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-4 | 15:06:43 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_Karma18 | -0.1100 |  |
| Jogador 8 | 2-5 | 15:06:54 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 2-5 | 15:06:54 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_Karma18 | 0.9000 |  |
| Jogador 8 | 2-5 | 15:06:54 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-5 | 15:06:55 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-5 | 15:06:56 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 2-5 | 15:06:56 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 2-5 | 15:06:57 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | -0.2900 |  |
| Jogador 8 | 2-5 | 15:06:57 | MOVE Bench -> Board: Warwick (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | -0.4000 |  |
| Jogador 8 | 2-5 | 15:06:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-6 | 15:07:10 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Enfeitiçador | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-6 | 15:07:11 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-6 | 15:07:11 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Enfeitiçador | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-6 | 15:07:12 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-6 | 15:07:13 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Enfeitiçador | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-6 | 15:07:13 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-6 | 15:07:14 | MOVE Bench -> Board: Vi (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_Karma18 | -0.4000 |  |
| Jogador 8 | 2-6 | 15:07:15 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 2-6 | 15:07:15 | MOVE Bench -> Board: Vi (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_Karma18 | -0.4100 |  |
| Jogador 8 | 2-7 | 15:07:29 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Enfeitiçador | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 2-7 | 15:07:29 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Enfeitiçador | DA_Karma18 | -0.3200 |  |
| Jogador 8 | 2-7 | 15:07:30 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-7 | 15:07:31 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 2-7 | 15:07:31 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 2-7 | 15:07:32 | MOVE Bench -> Board: Vi (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_Karma18 | -0.4100 |  |
| Jogador 8 | 2-7 | 15:07:32 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 2-7 | 15:07:33 | MOVE Bench -> Board: Vi (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_Karma18 | -0.4100 |  |
| Jogador 8 | 2-7 | 15:07:33 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_Karma18 | -0.7600 |  |
| Jogador 8 | 3-1 | 15:07:49 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Enfeitiçador | DA_18_Lillia | -0.5800 |  |
| Jogador 8 | 3-1 | 15:07:49 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_18_Lillia | 0.2000 |  |
| Jogador 8 | 3-1 | 15:07:50 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Enfeitiçador | DA_18_Lillia | -0.0400 |  |
| Jogador 8 | 3-1 | 15:07:51 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_Lillia | -0.0600 |  |
| Jogador 8 | 3-1 | 15:07:52 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_Lillia | -0.7000 |  |
| Jogador 8 | 3-1 | 15:07:52 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-1 | 15:07:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_Lillia | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-2 | 15:08:09 | MOVE Bench -> Board: Vi (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Enfeitiçador | DA_18_Lillia | -0.1900 |  |
| Jogador 8 | 3-2 | 15:08:10 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Enfeitiçador | DA_18_Lillia | 0.1000 |  |
| Jogador 8 | 3-2 | 15:08:10 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Enfeitiçador | DA_18_Lillia | 0.2600 |  |
| Jogador 8 | 3-2 | 15:08:11 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Enfeitiçador | DA_18_Lillia | -0.0800 |  |
| Jogador 8 | 3-2 | 15:08:12 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Enfeitiçador | DA_18_Lillia | 0.2000 |  |
| Jogador 8 | 3-2 | 15:08:12 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Enfeitiçador | DA_18_Lillia | -0.0400 |  |
| Jogador 8 | 3-2 | 15:08:13 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Enfeitiçador | DA_18_Lillia | -0.2600 |  |
| Jogador 8 | 3-2 | 15:08:14 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Enfeitiçador | DA_18_Lillia | -0.6300 |  |
| Jogador 8 | 3-2 | 15:08:14 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Enfeitiçador | DA_18_Lillia | 0.0200 |  |
| Jogador 8 | 3-3 | 15:08:31 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 3 | Enfeitiçador | DA_18_Lillia | 0.0900 |  |
| Jogador 8 | 3-3 | 15:08:32 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Enfeitiçador | DA_18_Lillia | 0.9000 |  |
| Jogador 8 | 3-3 | 15:08:32 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Enfeitiçador | DA_18_Lillia | 0.8100 |  |
| Jogador 8 | 3-3 | 15:08:33 | MOVE Bench -> Board: Vi (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Enfeitiçador | DA_18_Lillia | -0.2000 |  |
| Jogador 8 | 3-3 | 15:08:33 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Enfeitiçador | DA_18_Lillia | -0.7800 |  |
| Jogador 8 | 3-3 | 15:08:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Enfeitiçador | DA_18_Lillia | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-4 | 15:08:55 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Enfeitiçador | DA_18_Lillia | 0.8500 |  |
| Jogador 8 | 3-4 | 15:08:57 | MOVE Bench -> Board: Warwick (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Enfeitiçador | DA_18_Lillia | -0.1400 |  |
| Jogador 8 | 3-4 | 15:08:58 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Enfeitiçador | DA_18_Lillia | -0.2200 |  |
| Jogador 8 | 3-4 | 15:08:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Enfeitiçador | DA_18_Lillia | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-4 | 15:09:01 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Enfeitiçador | DA_18_Lillia | 0.5800 |  |
| Jogador 8 | 3-5 | 15:09:22 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_18_Lillia | 0.9000 |  |
| Jogador 8 | 3-5 | 15:09:23 | MOVE Bench -> Board: Vi (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_18_Lillia | -0.3700 |  |
| Jogador 8 | 3-5 | 15:09:23 | MOVE Bench -> Board: Karma (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_18_Lillia | 0.3600 |  |
| Jogador 8 | 3-5 | 15:09:24 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_18_Lillia | -0.2400 |  |
| Jogador 8 | 3-5 | 15:09:24 | MOVE Bench -> Board: Vi (i:6.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_18_Lillia | -0.4100 |  |
| Jogador 8 | 3-5 | 15:09:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_18_Lillia | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-6 | 15:09:50 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 74 | 5 | Enfeitiçador | DA_18_Lillia | 0.1400 |  |
| Jogador 8 | 3-6 | 15:09:50 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Enfeitiçador | DA_18_Lillia | 0.0500 |  |
| Jogador 8 | 3-6 | 15:09:51 | MOVE Bench -> Board: Karma (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Enfeitiçador | DA_18_Lillia | 0.2600 |  |
| Jogador 8 | 3-6 | 15:09:51 | MOVE Bench -> Board: Vi (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Enfeitiçador | DA_18_Lillia | -0.2200 |  |
| Jogador 8 | 3-6 | 15:09:52 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Enfeitiçador | DA_18_Lillia | -0.8400 |  |
| Jogador 8 | 3-6 | 15:09:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Enfeitiçador | DA_18_Lillia | -0.1700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-7 | 15:10:20 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Enfeitiçador | DA_18_Lillia | 0.9600 |  |
| Jogador 8 | 3-7 | 15:10:20 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Enfeitiçador | DA_18_Lillia | 0.3800 |  |
| Jogador 8 | 3-7 | 15:10:21 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_SparringGloves -> Azir (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Enfeitiçador | DA_18_Lillia | 0.1800 |  |
| Jogador 8 | 3-7 | 15:10:21 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Azir (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Enfeitiçador | DA_18_Lillia | 0.1300 |  |
| Jogador 8 | 3-7 | 15:10:22 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Enfeitiçador | DA_18_Lillia | 0.1200 |  |
| Jogador 8 | 3-7 | 15:10:22 | MOVE Bench -> Board: Karma (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Enfeitiçador | DA_18_Lillia | 0.2400 |  |
| Jogador 8 | 3-7 | 15:10:23 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Enfeitiçador | DA_18_Lillia | -0.1600 |  |
| Jogador 8 | 3-7 | 15:10:24 | MOVE Bench -> Board: Vi (i:6.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Enfeitiçador | DA_18_Lillia | -0.5300 |  |
| Jogador 8 | 3-7 | 15:10:24 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Enfeitiçador | DA_18_Lillia | -0.1000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 4-1 | 15:10:50 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 87 | 5 | Enfeitiçador | DA_18_Lillia | 0.4700 |  |
| Jogador 8 | 4-1 | 15:10:50 | VENDEU: Kobuko (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Enfeitiçador | DA_18_Lillia | -0.5100 |  |
| Jogador 8 | 4-1 | 15:10:51 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 89 | 5 | Enfeitiçador | DA_18_Lillia | 0.2800 |  |
| Jogador 8 | 4-1 | 15:10:52 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 89 | 5 | Enfeitiçador | DA_18_Lillia | 0.1100 |  |
| Jogador 8 | 4-1 | 15:10:52 | VENDEU: Karma (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Enfeitiçador | DA_18_Lillia | -0.5900 |  |
| Jogador 8 | 4-1 | 15:10:53 | COMPROU: Sivir (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Enfeitiçador | DA_18_Lillia | -0.0300 |  |
| Jogador 8 | 4-1 | 15:10:53 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Enfeitiçador | DA_18_Lillia | 0.1000 |  |
| Jogador 8 | 4-1 | 15:10:54 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Enfeitiçador | DA_18_Lillia | -0.0900 |  |
| Jogador 8 | 4-1 | 15:10:54 | MOVE Bench -> Board: Sivir (i:8.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Enfeitiçador | DA_18_Lillia | -0.2700 |  |
| Jogador 8 | 4-2 | 15:11:22 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Enfeitiçador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 4-2 | 15:11:23 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Enfeitiçador | DA_18_Lillia | 0.3100 |  |
| Jogador 8 | 4-2 | 15:11:24 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Enfeitiçador | DA_18_Lillia | -0.0200 |  |
| Jogador 8 | 4-2 | 15:11:24 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Enfeitiçador | DA_18_Lillia | 0.2900 |  |
| Jogador 8 | 4-2 | 15:11:25 | VENDEU: Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Enfeitiçador | DA_18_Warwick | -0.0200 |  |
| Jogador 8 | 4-2 | 15:11:25 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Enfeitiçador | DA_18_Warwick | 0.1000 |  |
| Jogador 8 | 4-2 | 15:11:26 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Enfeitiçador | DA_18_Warwick | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-2 | 15:11:26 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Enfeitiçador | DA_18_Warwick | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-2 | 15:11:27 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Enfeitiçador | DA_18_Warwick | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 8 | 4-3 | 15:11:54 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 110 | 5 | Enfeitiçador | DA_18_Warwick | -0.5900 |  |
| Jogador 8 | 4-3 | 15:11:55 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Enfeitiçador | DA_18_Warwick | 0.9000 |  |
| Jogador 8 | 4-3 | 15:11:56 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 110 | 5 | Enfeitiçador | DA_18_Warwick | -0.4600 |  |
| Jogador 8 | 4-3 | 15:11:56 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Enfeitiçador | DA_18_Warwick | 0.8800 |  |
| Jogador 8 | 4-3 | 15:11:57 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 111 | 5 | Enfeitiçador | DA_18_Warwick | -0.3300 |  |
| Jogador 8 | 4-3 | 15:11:57 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 110 | 5 | Enfeitiçador | DA_18_Warwick | 0.0600 |  |
| Jogador 8 | 4-3 | 15:11:58 | REROLL | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Enfeitiçador | DA_18_Warwick | -0.1600 |  |
| Jogador 8 | 4-3 | 15:11:58 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Enfeitiçador | DA_18_Warwick | -0.0300 |  |
| Jogador 8 | 4-3 | 15:11:59 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Enfeitiçador | DA_18_Warwick | 0.8700 |  |
| Jogador 8 | 4-4 | 15:12:29 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Enfeitiçador | DA_18_Warwick | -0.5900 |  |
| Jogador 8 | 4-4 | 15:12:30 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 114 | 5 | Enfeitiçador | DA_18_Warwick | 0.9600 |  |
| Jogador 8 | 4-4 | 15:12:30 | MOVE Bench -> Board: Cassiopeia (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 114 | 5 | Enfeitiçador | DA_18_Warwick | 0.6000 |  |
| Jogador 8 | 4-4 | 15:12:31 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Enfeitiçador | DA_18_Warwick | 0.0500 |  |
| Jogador 8 | 4-4 | 15:12:31 | MOVE Board -> Board: Cassiopeia (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Enfeitiçador | DA_18_Warwick | 0.0000 |  |
| Jogador 8 | 4-4 | 15:12:32 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 111 | 5 | Enfeitiçador | DA_18_Warwick | 0.0500 |  |
| Jogador 8 | 4-4 | 15:12:32 | REROLL | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Enfeitiçador | DA_18_Warwick | -0.1600 |  |
| Jogador 8 | 4-4 | 15:12:33 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 110 | 5 | Enfeitiçador | DA_18_Warwick | -0.0100 |  |
| Jogador 8 | 4-4 | 15:12:33 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Enfeitiçador | DA_18_Warwick | 0.5100 |  |
| Jogador 8 | 4-5 | 15:13:07 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Enfeitiçador | DA_18_Warwick | -0.5600 |  |
| Jogador 8 | 4-5 | 15:13:07 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Enfeitiçador | DA_18_Warwick | 0.6800 |  |
| Jogador 8 | 4-5 | 15:13:08 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Enfeitiçador | DA_18_Warwick | -0.0100 |  |
| Jogador 8 | 4-5 | 15:13:09 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Enfeitiçador | DA_18_Warwick | 0.5300 |  |
| Jogador 8 | 4-5 | 15:13:09 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Enfeitiçador | DA_18_Warwick | -0.5400 |  |
| Jogador 8 | 4-5 | 15:13:10 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Enfeitiçador | DA_18_Warwick | 0.0600 |  |
| Jogador 8 | 4-5 | 15:13:10 | MOVE Bench -> Board: Rammus (i:6.0) <-> Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Enfeitiçador | DA_18_Warwick | -0.2200 |  |
| Jogador 8 | 4-5 | 15:13:11 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Enfeitiçador | DA_18_Warwick | -0.0700 |  |
| Jogador 8 | 4-5 | 15:13:11 | VENDEU: Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Enfeitiçador | DA_18_Warwick | -0.5700 |  |
| Jogador 8 | 4-6 | 15:13:47 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Enfeitiçador | DA_18_Warwick | 0.0600 |  |
| Jogador 8 | 4-6 | 15:13:48 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Enfeitiçador | DA_18_Warwick | -0.0100 |  |
| Jogador 8 | 4-6 | 15:13:48 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Enfeitiçador | DA_18_Warwick | 0.0600 |  |
| Jogador 8 | 4-6 | 15:13:49 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Enfeitiçador | DA_18_Warwick | -0.0700 |  |
| Jogador 8 | 4-6 | 15:13:50 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Enfeitiçador | DA_18_Warwick | -0.0100 |  |
| Jogador 8 | 4-6 | 15:13:50 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Enfeitiçador | DA_18_Warwick | 0.4300 |  |
| Jogador 8 | 4-6 | 15:13:51 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Enfeitiçador | DA_18_Warwick | -0.0700 |  |
| Jogador 8 | 4-6 | 15:13:51 | VENDEU: Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Enfeitiçador | DA_18_Warwick | -0.0200 |  |
| Jogador 8 | 4-6 | 15:13:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Enfeitiçador | DA_18_Warwick | 0.4300 |  |
| Jogador 8 | 4-7 | 15:14:28 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Enfeitiçador | DA_18_Warwick | 0.1200 |  |
| Jogador 8 | 4-7 | 15:14:29 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NegatronCloak -> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Enfeitiçador | DA_18_Warwick | 0.1900 |  |
| Jogador 8 | 4-7 | 15:14:30 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Enfeitiçador | DA_18_Warwick | -0.6800 |  |
| Jogador 8 | 4-7 | 15:14:30 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Enfeitiçador | DA_18_Warwick | 1.0500 |  |
| Jogador 8 | 4-7 | 15:14:30 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Enfeitiçador | DA_18_Warwick | 0.7900 |  |
| Jogador 8 | 4-7 | 15:14:31 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Enfeitiçador | DA_18_Warwick | 0.4600 |  |
| Jogador 8 | 4-7 | 15:14:32 | VENDEU: LeBlanc (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Enfeitiçador | DA_18_Warwick | -0.6800 |  |
| Jogador 8 | 4-7 | 15:14:32 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Enfeitiçador | DA_18_Warwick | 0.9800 |  |
| Jogador 8 | 4-7 | 15:14:32 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Enfeitiçador | DA_18_Warwick | -0.0700 |  |
| Jogador 8 | 5-1 | 15:15:10 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Enfeitiçador | DA_18_Warwick | -0.6800 |  |
| Jogador 8 | 5-1 | 15:15:10 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Enfeitiçador | DA_18_Warwick | 0.4500 |  |
| Jogador 8 | 5-1 | 15:15:11 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Enfeitiçador | DA_18_Warwick | -0.6800 |  |
| Jogador 8 | 5-1 | 15:15:11 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Enfeitiçador | DA_18_Warwick | 0.4500 |  |
| Jogador 8 | 5-1 | 15:15:12 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Enfeitiçador | DA_18_Warwick | -0.0700 |  |
| Jogador 8 | 5-1 | 15:15:12 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Enfeitiçador | DA_18_Warwick | -0.6800 |  |
| Jogador 8 | 5-1 | 15:15:13 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Enfeitiçador | DA_18_Warwick | 0.4500 |  |
| Jogador 8 | 5-1 | 15:15:13 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Enfeitiçador | DA_18_Warwick | -0.6800 |  |
| Jogador 8 | 5-1 | 15:15:14 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Enfeitiçador | DA_18_Warwick | 0.4200 |  |
| Jogador 8 | 5-2 | 15:15:51 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Enfeitiçador | DA_18_Warwick | -0.7200 |  |
| Jogador 8 | 5-2 | 15:15:51 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Enfeitiçador | DA_18_Warwick | 0.4800 |  |
| Jogador 8 | 5-2 | 15:15:52 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Enfeitiçador | DA_18_Warwick | -0.7300 |  |
| Jogador 8 | 5-2 | 15:15:52 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Enfeitiçador | DA_18_Warwick | 0.0400 |  |
| Jogador 8 | 5-2 | 15:15:53 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 151 | 5 | Enfeitiçador | DA_18_Warwick | -0.0700 |  |
| Jogador 8 | 5-2 | 15:15:53 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Enfeitiçador | DA_18_Warwick | -0.0100 |  |
| Jogador 8 | 5-2 | 15:15:54 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Enfeitiçador | DA_18_Warwick | 0.9200 |  |
| Jogador 8 | 5-2 | 15:15:54 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Enfeitiçador | DA_18_Warwick | -0.6800 |  |
| Jogador 8 | 5-2 | 15:15:55 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Enfeitiçador | DA_18_Warwick | 0.4800 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 31 | 32 | 160 | 31 | 16 | 235 | 10 | 33 |
| Jogador 2 | 37 | 38 | 190 | 37 | 17 | 298 | 9 | 30 |
| Jogador 3 | 38 | 38 | 190 | 38 | 17 | 257 | 5 | 41 |
| Jogador 4 | 24 | 25 | 125 | 24 | 15 | 182 | 6 | 16 |
| Jogador 5 | 26 | 29 | 145 | 26 | 16 | 201 | 13 | 35 |
| Jogador 6 | 28 | 32 | 160 | 28 | 16 | 210 | 12 | 35 |
| Jogador 7 | 38 | 40 | 200 | 38 | 19 | 284 | 9 | 53 |
| Jogador 8 | 28 | 39 | 195 | 28 | 16 | 218 | 5 | 20 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 235 | 235 | 235 | 0 | 228 | 0 | 235 | 235 | 235 | 77/63 |
| Jogador 2 | 298 | 298 | 298 | 0 | 289 | 0 | 298 | 298 | 298 | 108/93 |
| Jogador 3 | 257 | 257 | 257 | 0 | 247 | 0 | 257 | 257 | 257 | 82/67 |
| Jogador 4 | 182 | 182 | 182 | 0 | 174 | 0 | 182 | 182 | 182 | 65/50 |
| Jogador 5 | 201 | 201 | 201 | 0 | 194 | 0 | 201 | 201 | 201 | 92/77 |
| Jogador 6 | 210 | 210 | 210 | 0 | 197 | 0 | 210 | 210 | 210 | 75/62 |
| Jogador 7 | 284 | 284 | 284 | 0 | 263 | 0 | 284 | 284 | 284 | 91/77 |
| Jogador 8 | 218 | 218 | 218 | 0 | 211 | 0 | 218 | 218 | 218 | 81/67 |

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
| Jogador 1 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.34675195813179016 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2500632703304291 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 32 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0387905836105347 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0313513278961182 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9796043038368225 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19132192432880402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17696425318717957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 57 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 58 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33574986457824707 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 63 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12980356812477112 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 2-2 | 64 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060316212475299835 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27567100524902344 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00807955488562584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 68 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17264987528324127 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 2-2 | 69 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3274087905883789 | 0.0 | 0.0 | +e76c0caf-1c3d-493f-9a21-659dd8587fc2 / -— |
| Jogador 1 | 2-2 | 70 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.352801114320755 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 74 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3344477415084839 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 75 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17819906771183014 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 1 | 2-3 | 76 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15111081302165985 | 0.0 | 0.0 | +— / -e76c0caf-1c3d-493f-9a21-659dd8587fc2 |
| Jogador 1 | 2-3 | 77 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 78 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 82 | BUY | STABILIZE | 93.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1169859170913696 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-4 | 83 | BUY | STABILIZE | 93.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.364176869392395 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 84 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4286784827709198 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 85 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012633305042982101 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 87 | PASS | STABILIZE | 93.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 92 | BUY | STABILIZE | 93.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0242516994476318 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 93 | BUY | STABILIZE | 93.0 | 5 | 4 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32582294940948486 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 94 | SELL | STABILIZE | 93.0 | 5 | 2 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 1 | 2-5 | 95 | BUY_XP | STABILIZE | 93.0 | 5 | 5 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0037288148887455463 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 97 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06561169028282166 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 98 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004718039184808731 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 99 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015006372705101967 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 100 | PASS | STABILIZE | 93.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 102 | BUY | STABILIZE | 93.0 | 6 | 7 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479967594146729 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 103 | BUY | STABILIZE | 93.0 | 6 | 6 | 0 | 10.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07185867428779602 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 3 | 0 | 10.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27010679244995117 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 105 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 3 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2985333800315857 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 106 | BUY | STABILIZE | 93.0 | 6 | 3 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06937354803085327 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.690438698977232e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014103122986853123 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 109 | PASS | STABILIZE | 93.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 112 | BUY | STABILIZE | 93.0 | 6 | 7 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0474052429199219 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-7 | 113 | BUY | STABILIZE | 93.0 | 6 | 6 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9376266598701477 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 4 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3587802052497864 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 115 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 4 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 116 | PASS | STABILIZE | 93.0 | 6 | 4 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 120 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 4 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3429917097091675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 93.0 | 6 | 10 | 1 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2631056606769562 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 123 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 10 | 1 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08154261112213135 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 124 | BUY_XP | STABILIZE | 93.0 | 6 | 10 | 1 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 125 | BUY_XP | STABILIZE | 93.0 | 6 | 6 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 2 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0023640748113393784 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 127 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 2 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3987067639827728 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 128 | BUY | STABILIZE | 93.0 | 6 | 2 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012025037780404091 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 1 | 3-1 | 129 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0014168692287057638 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 130 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015427687205374241 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 132 | BUY | STABILIZE | 93.0 | 6 | 7 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10312627255916595 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 1 | 3-2 | 133 | BUY | STABILIZE | 93.0 | 6 | 4 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07151003181934357 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 134 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013103440403938293 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 135 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0040281699039042 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01613207347691059 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 138 | PASS | STABILIZE | 93.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 142 | BUY | STABILIZE | 93.0 | 6 | 7 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009308427572250366 | 0.0 | 0.0 | +e6ee6b15-d413-4678-8ffb-29272199a53d / -— |
| Jogador 1 | 3-3 | 143 | BUY | STABILIZE | 93.0 | 6 | 4 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009431720711290836 | 0.0 | 0.0 | +c30e7bdb-41d6-423c-9d7d-2e146472e724 / -— |
| Jogador 1 | 3-3 | 144 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 1 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08060761541128159 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 145 | SELL | STABILIZE | 93.0 | 6 | 1 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010413674637675285 | 0.0 | 0.0 | +— / -8e819ba6-a356-4d9b-a8c9-7493332900fb |
| Jogador 1 | 3-3 | 146 | BUY | STABILIZE | 93.0 | 6 | 3 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18640245497226715 | 0.0 | 0.0 | +45450b46-63b4-488f-9469-3348c6da8f4b / -— |
| Jogador 1 | 3-3 | 147 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01619788259267807 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 148 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10495531558990479 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 149 | PASS | STABILIZE | 93.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 152 | SELL | STABILIZE | 84.0 | 6 | 5 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0114569878205657 | 0.0 | 0.0 | +— / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 3-4 | 153 | BUY | STABILIZE | 84.0 | 6 | 8 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017345400992780924 | 0.0 | 0.0 | +0450963e-c7e2-4ff5-a2f5-09e65fa63527 / -— |
| Jogador 1 | 3-4 | 154 | SELL | STABILIZE | 84.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -0450963e-c7e2-4ff5-a2f5-09e65fa63527 |
| Jogador 1 | 3-4 | 155 | BUY | STABILIZE | 84.0 | 6 | 8 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009533167816698551 | 0.0 | 0.0 | +54b47885-6cb9-42e7-a9bb-049e0e2d2956 / -— |
| Jogador 1 | 3-4 | 156 | SELL | STABILIZE | 84.0 | 6 | 7 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0070333331823349 | 0.0 | 0.0 | +— / -54b47885-6cb9-42e7-a9bb-049e0e2d2956 |
| Jogador 1 | 3-4 | 157 | BUY | STABILIZE | 84.0 | 6 | 8 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08230060338973999 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 158 | SELL | STABILIZE | 84.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -bddefab1-7dd7-4954-816c-45dbd44b947b |
| Jogador 1 | 3-4 | 159 | BUY | STABILIZE | 84.0 | 6 | 8 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2813367247581482 | 0.0 | 0.0 | +7a60e1b2-fc20-4070-b163-2f9fb6f93264 / -— |
| Jogador 1 | 3-4 | 160 | SELL | STABILIZE | 84.0 | 6 | 7 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01180189661681652 | 0.0 | 0.0 | +— / -7a60e1b2-fc20-4070-b163-2f9fb6f93264 |
| Jogador 1 | 3-5 | 162 | BUY | STABILIZE | 84.0 | 6 | 13 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.834733247756958 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 163 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 11 | 1 | 16.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1098669022321701 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 164 | BUY | STABILIZE | 84.0 | 6 | 11 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016370749101042747 | 0.0 | 0.0 | +a9184317-58b7-4804-9aef-3e2c08c20935 / -— |
| Jogador 1 | 3-5 | 165 | SELL | STABILIZE | 84.0 | 6 | 10 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 |
| Jogador 1 | 3-5 | 166 | BUY | STABILIZE | 84.0 | 6 | 15 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.435349702835083 | 0.0 | 0.0 | +f6e6e08d-ecfe-4c84-acfa-6ad8292968ee / -— |
| Jogador 1 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2368418127298355 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09107664227485657 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 169 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2637118399143219 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 170 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 14 | 1 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 172 | BUY | STABILIZE | 84.0 | 6 | 21 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8126763105392456 | 0.0 | 0.0 | +600071dd-5c17-4f03-903f-d1cd6c20bb28 / -— |
| Jogador 1 | 3-6 | 173 | SELL | STABILIZE | 84.0 | 6 | 20 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007366666570305824 | 0.0 | 0.0 | +— / -c30e7bdb-41d6-423c-9d7d-2e146472e724 |
| Jogador 1 | 3-6 | 174 | BUY | STABILIZE | 84.0 | 6 | 23 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2932051420211792 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -— |
| Jogador 1 | 3-6 | 175 | SELL | STABILIZE | 84.0 | 6 | 21 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022099999710917473 | 0.0 | 0.0 | +— / -e6ee6b15-d413-4678-8ffb-29272199a53d |
| Jogador 1 | 3-6 | 176 | BUY | STABILIZE | 84.0 | 6 | 24 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8134503364562988 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 22 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008455449715256691 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 22 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04236752167344093 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 179 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 22 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 180 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 22 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011117677204310894 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 182 | SELL | STABILIZE | 75.0 | 6 | 29 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057733334600925446 | 0.0 | 0.0 | +— / -145f7470-8c0f-4957-b8d6-97939ddaeba1 |
| Jogador 1 | 3-7 | 183 | BUY | STABILIZE | 75.0 | 6 | 33 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024173643440008163 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 1 | 3-7 | 184 | SELL | STABILIZE | 75.0 | 6 | 29 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05484476685523987 | 0.0 | 0.0 | +— / -7306c9be-466e-498c-819e-274ff070c72b |
| Jogador 1 | 3-7 | 185 | BUY | STABILIZE | 75.0 | 6 | 33 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0028466894291341305 | 0.0 | 0.0 | +c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 / -— |
| Jogador 1 | 3-7 | 186 | SELL | STABILIZE | 75.0 | 6 | 31 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 |
| Jogador 1 | 3-7 | 187 | BUY | STABILIZE | 75.0 | 6 | 33 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0028446000069379807 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 1 | 3-7 | 188 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 31 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23768070340156555 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 189 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 31 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.148210346698761 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 31 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1485983431339264 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 75.0 | 6 | 39 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19432389736175537 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 75.0 | 6 | 39 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20449523627758026 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 194 | SELL | STABILIZE | 75.0 | 6 | 39 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05806666612625122 | 0.0 | 0.0 | +— / -227dbcdb-af5c-4318-94d1-f01a7847d100 |
| Jogador 1 | 4-1 | 195 | BUY | STABILIZE | 75.0 | 6 | 41 | 4 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6813240647315979 | 0.0 | 0.0 | +e7c8751e-5d30-4953-9508-35488b6c45db / -— |
| Jogador 1 | 4-1 | 196 | SELL | STABILIZE | 75.0 | 6 | 38 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4620000123977661 | 0.0 | 0.0 | +— / -a9184317-58b7-4804-9aef-3e2c08c20935 |
| Jogador 1 | 4-1 | 197 | BUY | STABILIZE | 75.0 | 6 | 39 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09176795184612274 | 0.0 | 0.0 | +75d9034d-80ed-40d3-a330-44554cc2bb9e / -— |
| Jogador 1 | 4-1 | 198 | SELL | STABILIZE | 75.0 | 6 | 37 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0070333331823349 | 0.0 | 0.0 | +— / -f6e6e08d-ecfe-4c84-acfa-6ad8292968ee |
| Jogador 1 | 4-1 | 199 | BUY | STABILIZE | 75.0 | 6 | 38 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010531242936849594 | 0.0 | 0.0 | +502a6e8c-8f81-456f-a1ef-c6bb8dd6fc7e / -— |
| Jogador 1 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 35 | 3 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008707152679562569 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 202 | SELL | STABILIZE | 75.0 | 6 | 44 | 4 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028866667300462723 | 0.0 | 0.0 | +— / -75d9034d-80ed-40d3-a330-44554cc2bb9e |
| Jogador 1 | 4-2 | 203 | BUY | STABILIZE | 75.0 | 6 | 46 | 4 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3779985010623932 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -— |
| Jogador 1 | 4-2 | 204 | SELL | STABILIZE | 75.0 | 6 | 45 | 4 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011252655647695065 | 0.0 | 0.0 | +— / -502a6e8c-8f81-456f-a1ef-c6bb8dd6fc7e |
| Jogador 1 | 4-2 | 205 | BUY | STABILIZE | 75.0 | 6 | 48 | 4 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012797974981367588 | 0.0 | 0.0 | +c617e958-b482-40ce-ab24-acff4dc48bc0 / -— |
| Jogador 1 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 46 | 4 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28496333956718445 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 207 | SELL | STABILIZE | 75.0 | 6 | 46 | 4 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -c617e958-b482-40ce-ab24-acff4dc48bc0 |
| Jogador 1 | 4-2 | 208 | SELL | STABILIZE | 75.0 | 6 | 48 | 4 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -b7e13ed2-571b-4245-ba21-401b1eef8660 |
| Jogador 1 | 4-2 | 209 | BUY | STABILIZE | 75.0 | 6 | 49 | 4 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2841355502605438 | 0.0 | 0.0 | +9cb61b5c-2c8a-43a2-a854-517f4377f6db / -— |
| Jogador 1 | 4-2 | 210 | SELL | STABILIZE | 75.0 | 6 | 46 | 4 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3190000057220459 | 0.0 | 0.0 | +— / -9cb61b5c-2c8a-43a2-a854-517f4377f6db |
| Jogador 1 | 4-3 | 212 | BUY | STABILIZE | 65.0 | 6 | 58 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9618664979934692 | 0.0 | 0.0 | +3f488391-7117-4e28-b6cc-7416722351d4 / -9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8,d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 4-3 | 213 | BUY | STABILIZE | 65.0 | 6 | 56 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2339557707309723 | 0.0 | 0.0 | +235510e3-df54-4de9-9bcf-bff6d47e364a / -— |
| Jogador 1 | 4-3 | 214 | SELL | STABILIZE | 65.0 | 6 | 53 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6414999961853027 | 0.0 | 0.0 | +— / -3f488391-7117-4e28-b6cc-7416722351d4 |
| Jogador 1 | 4-3 | 215 | BUY | STABILIZE | 65.0 | 6 | 58 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06931936740875244 | 0.0 | 0.0 | +395ae945-c8a2-4d80-98a4-5eb6887b8f78 / -— |
| Jogador 1 | 4-3 | 216 | SELL | STABILIZE | 65.0 | 6 | 57 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3509666621685028 | 0.0 | 0.0 | +— / -395ae945-c8a2-4d80-98a4-5eb6887b8f78 |
| Jogador 1 | 4-3 | 217 | SELL | STABILIZE | 65.0 | 6 | 58 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3549000024795532 | 0.0 | 0.0 | +— / -235510e3-df54-4de9-9bcf-bff6d47e364a |
| Jogador 1 | 4-3 | 218 | BUY | STABILIZE | 65.0 | 6 | 61 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09197580814361572 | 0.0 | 0.0 | +506f421d-7a3c-46d7-9cac-6c107bc35e31 / -— |
| Jogador 1 | 4-3 | 219 | SELL | STABILIZE | 65.0 | 6 | 60 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3603000044822693 | 0.0 | 0.0 | +— / -506f421d-7a3c-46d7-9cac-6c107bc35e31 |
| Jogador 1 | 4-3 | 220 | SELL | STABILIZE | 65.0 | 6 | 61 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5182820558547974 | 0.0 | 0.0 | +— / -760d5bee-7d64-4f03-abf0-6357c914a1ed |
| Jogador 1 | 4-4 | 222 | BUY | STABILIZE | 54.0 | 6 | 74 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3885752260684967 | 0.0 | 0.0 | +fb551efa-6ad5-4f97-aa05-bc5eb70943d4 / -— |
| Jogador 1 | 4-4 | 223 | BUY | STABILIZE | 54.0 | 6 | 72 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010372533462941647 | 0.0 | 0.0 | +ea88d306-ae6b-4dbe-b559-3371ba39613a / -— |
| Jogador 1 | 4-4 | 224 | BUY | STABILIZE | 54.0 | 6 | 70 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08501464128494263 | 0.0 | 0.0 | +b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 / -— |
| Jogador 1 | 4-4 | 225 | SELL | STABILIZE | 54.0 | 6 | 68 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3649333417415619 | 0.0 | 0.0 | +— / -b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 |
| Jogador 1 | 4-4 | 226 | SELL | STABILIZE | 54.0 | 6 | 70 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37560001015663147 | 0.0 | 0.0 | +— / -ea88d306-ae6b-4dbe-b559-3371ba39613a |
| Jogador 1 | 4-4 | 227 | BUY | STABILIZE | 54.0 | 6 | 72 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28059056401252747 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 1 | 4-4 | 228 | SELL | STABILIZE | 54.0 | 6 | 70 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32760000228881836 | 0.0 | 0.0 | +— / -29a44465-8a09-49e7-abfc-a27e987543f1 |
| Jogador 1 | 4-4 | 229 | SELL | STABILIZE | 54.0 | 6 | 72 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07773904502391815 | 0.0 | 0.0 | +— / -b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 1 | 4-4 | 230 | SELL | STABILIZE | 54.0 | 6 | 74 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10893333703279495 | 0.0 | 0.0 | +— / -fb551efa-6ad5-4f97-aa05-bc5eb70943d4 |
| Jogador 1 | 4-5 | 232 | BUY | STABILIZE | 54.0 | 6 | 87 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44221463799476624 | 0.0 | 0.0 | +f99cdd31-4a55-4a5e-941a-2800b8afdd7a / -— |
| Jogador 1 | 4-5 | 233 | BUY | STABILIZE | 54.0 | 6 | 84 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13193348050117493 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -— |
| Jogador 1 | 4-5 | 234 | BUY | STABILIZE | 54.0 | 6 | 80 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030987940728664398 | 0.0 | 0.0 | +b82f90f3-6914-4db5-bc7c-74543cf91aef / -— |
| Jogador 1 | 4-5 | 235 | MOVE_BENCH | STABILIZE | 54.0 | 6 | 77 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4490298330783844 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 236 | BUY | STABILIZE | 54.0 | 6 | 77 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23894760012626648 | 0.0 | 0.0 | +d6a00f0c-4823-44d6-b326-67595876998d / -— |
| Jogador 1 | 4-5 | 237 | SELL | STABILIZE | 54.0 | 6 | 74 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02889999933540821 | 0.0 | 0.0 | +— / -15893185-b1a5-4725-9e46-964e149ec287 |
| Jogador 1 | 4-5 | 238 | BUY_XP | STABILIZE | 54.0 | 6 | 77 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47769126296043396 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 239 | MOVE_BENCH | STABILIZE | 54.0 | 7 | 73 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40037301182746887 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 240 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 73 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 242 | BUY | STABILIZE | 43.0 | 7 | 84 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9851917624473572 | 0.0 | 0.0 | +27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 / -— |
| Jogador 1 | 4-6 | 243 | BUY | STABILIZE | 43.0 | 7 | 81 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02638394944369793 | 0.0 | 0.0 | +8b75555c-d84d-4b8a-8d6c-012585a05b99 / -— |
| Jogador 1 | 4-6 | 244 | BUY | STABILIZE | 43.0 | 7 | 79 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1893310248851776 | 0.0 | 0.0 | +06332ba7-fc4e-431e-ab25-2fb284c08c33 / -— |
| Jogador 1 | 4-6 | 245 | BUY | STABILIZE | 43.0 | 7 | 76 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03245560824871063 | 0.0 | 0.0 | +18e21ac6-f873-4310-95c8-bd8e62612479 / -— |
| Jogador 1 | 4-6 | 246 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 75 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0013791659148409963 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 247 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 75 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013626467436552048 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 248 | PASS | STABILIZE | 43.0 | 7 | 75 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10221171379089355 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 252 | SELL | STABILIZE | 43.0 | 7 | 86 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027666667476296425 | 0.0 | 0.0 | +— / -18e21ac6-f873-4310-95c8-bd8e62612479 |
| Jogador 1 | 4-7 | 253 | BUY | STABILIZE | 43.0 | 7 | 87 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4453657865524292 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 1 | 4-7 | 254 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 84 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.2935171980643645e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 255 | SELL | STABILIZE | 43.0 | 7 | 84 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03855985775589943 | 0.0 | 0.0 | +— / -8b75555c-d84d-4b8a-8d6c-012585a05b99 |
| Jogador 1 | 4-7 | 256 | BUY | STABILIZE | 43.0 | 7 | 86 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21085570752620697 | 0.0 | 0.0 | +ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 / -— |
| Jogador 1 | 4-7 | 257 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 83 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 258 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 83 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014993620105087757 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 259 | PASS | STABILIZE | 43.0 | 7 | 83 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10878825187683105 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 43.0 | 7 | 93 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13704784214496613 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 43.0 | 7 | 93 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16656650602817535 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 264 | SELL | STABILIZE | 43.0 | 7 | 93 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004399999976158142 | 0.0 | 0.0 | +— / -ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 |
| Jogador 1 | 5-1 | 265 | BUY | STABILIZE | 43.0 | 7 | 96 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9286399483680725 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -— |
| Jogador 1 | 5-1 | 266 | SELL | STABILIZE | 43.0 | 7 | 93 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -06332ba7-fc4e-431e-ab25-2fb284c08c33 |
| Jogador 1 | 5-1 | 267 | BUY | STABILIZE | 43.0 | 7 | 96 | 5 | 34.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0231057405471802 | 0.0 | 0.0 | +c7762d7d-bcfa-4694-a3fc-038d7242207f / -27146a6e-fcf0-46e2-b3fc-5e7b659a5d47,9fe58106-e0c4-4ecc-b152-13c8c0eb564e |
| Jogador 1 | 5-1 | 268 | MOVE_BENCH | STABILIZE | 43.0 | 7 | 93 | 5 | 28.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45076489448547363 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 269 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 93 | 5 | 34.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015022012405097485 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 270 | BUY | STABILIZE | 43.0 | 7 | 93 | 5 | 34.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25279343128204346 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -— |
| Jogador 1 | 5-2 | 272 | BUY | STABILIZE | 29.0 | 7 | 100 | 5 | 34.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.021220326423645 | 0.0 | 0.0 | +0c96798c-ee23-488b-974f-74e8e3da6aa6 / -600071dd-5c17-4f03-903f-d1cd6c20bb28,cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 5-2 | 273 | BUY | STABILIZE | 29.0 | 7 | 99 | 5 | 32.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11507512629032135 | 0.0 | 0.0 | +eb418af1-c963-4da2-b052-86a153fc5ba1 / -— |
| Jogador 1 | 5-2 | 274 | MOVE_BENCH | STABILIZE | 29.0 | 7 | 96 | 5 | 32.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48769518733024597 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 275 | BUY | STABILIZE | 29.0 | 7 | 96 | 5 | 36.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5289725065231323 | 0.0 | 0.0 | +95eba9e8-10f5-48d5-86de-3d9a446b2e65 / -— |
| Jogador 1 | 5-2 | 276 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 93 | 5 | 36.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 277 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 93 | 5 | 36.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024870559573173523 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 278 | PASS | STABILIZE | 29.0 | 7 | 93 | 5 | 36.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16513676941394806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 282 | SELL | ALL_IN | 17.0 | 7 | 104 | 5 | 36.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7027999758720398 | 0.0 | 0.0 | +— / -c7762d7d-bcfa-4694-a3fc-038d7242207f |
| Jogador 1 | 5-3 | 283 | BUY | ALL_IN | 17.0 | 7 | 112 | 5 | 36.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47602418065071106 | 0.0 | 0.0 | +83a3ef65-b342-4ec8-b2d1-be99c3602f81 / -— |
| Jogador 1 | 5-3 | 284 | SELL | ALL_IN | 17.0 | 7 | 111 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -7313188a-ce84-4a52-b2d0-a94b2c420cdb |
| Jogador 1 | 5-3 | 285 | BUY | ALL_IN | 17.0 | 7 | 114 | 5 | 36.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10503420233726501 | 0.0 | 0.0 | +e5f61076-ec13-419b-a4e8-d91b9975cfd6 / -— |
| Jogador 1 | 5-3 | 286 | SELL | ALL_IN | 17.0 | 7 | 110 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042399998754262924 | 0.0 | 0.0 | +— / -e5f61076-ec13-419b-a4e8-d91b9975cfd6 |
| Jogador 1 | 5-3 | 287 | BUY | ALL_IN | 17.0 | 7 | 114 | 5 | 36.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014981033280491829 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 1 | 5-3 | 288 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 112 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005822737701237202 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 289 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 112 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 290 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 112 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01693003810942173 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 292 | SELL | ALL_IN | 17.0 | 7 | 123 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -0c5adb43-b194-486e-b59c-c0f3b5479d40 |
| Jogador 1 | 5-4 | 293 | BUY | ALL_IN | 17.0 | 7 | 125 | 5 | 36.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4768430292606354 | 0.0 | 0.0 | +bdee5671-864a-47c9-9576-9e0d8d2a7c6a / -— |
| Jogador 1 | 5-4 | 294 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 124 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0016799750737845898 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 295 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 124 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08922886103391647 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 296 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 124 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05928822606801987 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 297 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 124 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015918368473649025 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 298 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 124 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05336622893810272 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 299 | PASS | ALL_IN | 17.0 | 7 | 124 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5578107237815857 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 302 | SELL | ALL_IN | 17.0 | 7 | 134 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042399998754262924 | 0.0 | 0.0 | +— / -bc0aa086-b5e5-4809-833f-193c5c0da181 |
| Jogador 1 | 5-5 | 303 | BUY | ALL_IN | 17.0 | 7 | 138 | 5 | 36.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24468323588371277 | 0.0 | 0.0 | +bfe7ca8a-6e89-4673-b142-262e012398a9 / -— |
| Jogador 1 | 5-5 | 304 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 133 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2812829613685608 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 305 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 133 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 306 | PASS | ALL_IN | 17.0 | 7 | 133 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5662664771080017 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 312 | SELL | ALL_IN | 2.0 | 7 | 143 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -bfe7ca8a-6e89-4673-b142-262e012398a9 |
| Jogador 1 | 5-6 | 313 | BUY | ALL_IN | 2.0 | 7 | 148 | 5 | 36.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9405243992805481 | 0.0 | 0.0 | +4b4293ce-1cca-473e-8c07-b441686985ac / -— |
| Jogador 1 | 5-6 | 314 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 145 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17393885552883148 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 315 | SELL | ALL_IN | 2.0 | 7 | 145 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7357000112533569 | 0.0 | 0.0 | +— / -bdee5671-864a-47c9-9576-9e0d8d2a7c6a |
| Jogador 1 | 5-6 | 316 | BUY | ALL_IN | 2.0 | 7 | 146 | 5 | 36.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007433616556227207 | 0.0 | 0.0 | +00497e43-57ef-4c25-a34b-0be0155bb92d / -— |
| Jogador 1 | 5-6 | 317 | SELL | ALL_IN | 2.0 | 7 | 143 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -00497e43-57ef-4c25-a34b-0be0155bb92d |
| Jogador 1 | 5-6 | 318 | BUY | ALL_IN | 2.0 | 7 | 146 | 5 | 36.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0024117419961839914 | 0.0 | 0.0 | +8025eaf5-b02b-4f94-b381-b94321bca206 / -— |
| Jogador 1 | 5-6 | 319 | REROLL | ALL_IN | 2.0 | 7 | 144 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 320 | SELL | ALL_IN | 2.0 | 7 | 142 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018707985058426857 | 0.0 | 0.0 | +— / -8025eaf5-b02b-4f94-b381-b94321bca206 |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29996994137763977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.16027452051639557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43195363879203796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5009031295776367 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.117805004119873 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11796945333480835 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 30 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30811062455177307 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40792572498321533 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0720852613449097 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 44 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20215077698230743 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 45 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40031278133392334 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 46 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024478765204548836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012103810906410217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 48 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0379713773727417 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18181772530078888 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2733555734157562 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 57 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2658882141113281 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 58 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14804960787296295 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047599975019693375 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1965634673833847 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 2 | 2-2 | 62 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479710102081299 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 63 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23222024738788605 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 64 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14978505671024323 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 65 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047096773982048035 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 66 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24561917781829834 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 67 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8824999928474426 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-2 | 68 | BUY_XP | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19457465410232544 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 70 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01434213388711214 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2975618541240692 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 73 | BUY_XP | STABILIZE | 90.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 74 | PASS | STABILIZE | 90.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 82 | BUY | STABILIZE | 90.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9692935347557068 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 2 | 2-4 | 83 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3294220268726349 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 84 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0008978793048299849 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 85 | SELL | STABILIZE | 90.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 |
| Jogador 2 | 2-4 | 86 | BUY | STABILIZE | 90.0 | 5 | 4 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12595048546791077 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 87 | SELL | STABILIZE | 90.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15264102816581726 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 2-4 | 88 | BUY | STABILIZE | 90.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1918126493692398 | 0.0 | 0.0 | +ce928be1-b3ba-4640-b93c-d15c8a92833e / -— |
| Jogador 2 | 2-4 | 89 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3990757465362549 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014684390276670456 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 92 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31084248423576355 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 93 | BUY | STABILIZE | 90.0 | 5 | 3 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19954931735992432 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 94 | SELL | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10754162818193436 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-5 | 95 | BUY | STABILIZE | 90.0 | 5 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010788431391119957 | 0.0 | 0.0 | +be53a299-cc3e-4af3-94f6-343f9de1e0a0 / -— |
| Jogador 2 | 2-5 | 96 | SELL | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10219023376703262 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 2-5 | 97 | SELL | STABILIZE | 90.0 | 5 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1223333328962326 | 0.0 | 0.0 | +— / -081b684f-5d42-45c5-9a68-12127e5330a7 |
| Jogador 2 | 2-5 | 98 | BUY_XP | STABILIZE | 90.0 | 5 | 7 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 99 | SELL | STABILIZE | 90.0 | 5 | 3 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4125783443450928 | 0.0 | 0.0 | +— / -be53a299-cc3e-4af3-94f6-343f9de1e0a0 |
| Jogador 2 | 2-5 | 100 | BUY | STABILIZE | 90.0 | 5 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056665465235710144 | 0.0 | 0.0 | +6a071ec5-c3f4-41b3-a0d8-c1aee62cffee / -— |
| Jogador 2 | 2-6 | 102 | BUY | STABILIZE | 84.0 | 5 | 6 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18723787367343903 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 103 | BUY | STABILIZE | 84.0 | 5 | 3 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03426995128393173 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 104 | SELL | STABILIZE | 84.0 | 5 | 1 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07934979349374771 | 0.0 | 0.0 | +— / -6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 2-6 | 105 | SELL | STABILIZE | 84.0 | 5 | 3 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07469619810581207 | 0.0 | 0.0 | +— / -6a071ec5-c3f4-41b3-a0d8-c1aee62cffee |
| Jogador 2 | 2-6 | 106 | BUY | STABILIZE | 84.0 | 5 | 6 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058672964572906494 | 0.0 | 0.0 | +8ea1c095-e10b-46d0-8097-a70a211e2881 / -— |
| Jogador 2 | 2-6 | 107 | SELL | STABILIZE | 84.0 | 5 | 5 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3409999907016754 | 0.0 | 0.0 | +— / -8ea1c095-e10b-46d0-8097-a70a211e2881 |
| Jogador 2 | 2-6 | 108 | BUY_XP | STABILIZE | 84.0 | 5 | 6 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 109 | SELL | STABILIZE | 84.0 | 5 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1223333328962326 | 0.0 | 0.0 | +— / -97fc5647-5995-4f21-aa03-13454546919a |
| Jogador 2 | 2-6 | 110 | BUY_XP | STABILIZE | 84.0 | 5 | 5 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 112 | BUY | STABILIZE | 78.0 | 6 | 7 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.360278457403183 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 113 | BUY | STABILIZE | 78.0 | 6 | 3 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12442957609891891 | 0.0 | 0.0 | +068d0768-4134-4a5f-a132-0642c23d91e1 / -— |
| Jogador 2 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 1 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5940611958503723 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01504937931895256 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015456832945346832 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 117 | PASS | STABILIZE | 78.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 122 | BUY | STABILIZE | 78.0 | 6 | 7 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14793577790260315 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 123 | BUY | STABILIZE | 78.0 | 6 | 4 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1451442688703537 | 0.0 | 0.0 | +4312fba1-1471-4fb3-af6f-257248fa1437 / -— |
| Jogador 2 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 78.0 | 6 | 2 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24931600689888 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 125 | BUY | STABILIZE | 78.0 | 6 | 2 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07945946604013443 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005132489604875445 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 127 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015329618938267231 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017038557678461075 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 129 | PASS | STABILIZE | 78.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 132 | SELL | STABILIZE | 78.0 | 6 | 7 | 0 | 18.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02176666632294655 | 0.0 | 0.0 | +— / -ce928be1-b3ba-4640-b93c-d15c8a92833e |
| Jogador 2 | 3-2 | 133 | BUY | STABILIZE | 78.0 | 6 | 8 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379440307617188 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -7ca9b803-76eb-4283-9648-7f98bfd81149,d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 2 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 7 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4187695384025574 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 135 | BUY | STABILIZE | 78.0 | 6 | 7 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7692378759384155 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 6 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 137 | BUY_XP | STABILIZE | 78.0 | 6 | 6 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 138 | SELL | STABILIZE | 78.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -5489a8f6-2466-4171-b91e-64c367875d3c |
| Jogador 2 | 3-2 | 139 | BUY_XP | STABILIZE | 78.0 | 6 | 5 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 140 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 142 | BUY | STABILIZE | 78.0 | 6 | 8 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8035222887992859 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 143 | BUY | STABILIZE | 78.0 | 6 | 5 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25608503818511963 | 0.0 | 0.0 | +e08cb89b-8a77-44fe-be4c-46c2b45cbe9b / -— |
| Jogador 2 | 3-3 | 144 | SELL | STABILIZE | 78.0 | 6 | 3 | 0 | 22.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005817997734993696 | 0.0 | 0.0 | +— / -4312fba1-1471-4fb3-af6f-257248fa1437 |
| Jogador 2 | 3-3 | 145 | BUY_XP | STABILIZE | 78.0 | 6 | 5 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 146 | SELL | STABILIZE | 78.0 | 6 | 1 | 0 | 22.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4323333203792572 | 0.0 | 0.0 | +— / -e08cb89b-8a77-44fe-be4c-46c2b45cbe9b |
| Jogador 2 | 3-3 | 147 | BUY | STABILIZE | 78.0 | 6 | 3 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03346244990825653 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 148 | SELL | STABILIZE | 78.0 | 6 | 0 | 0 | 22.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020999999716877937 | 0.0 | 0.0 | +— / -068d0768-4134-4a5f-a132-0642c23d91e1 |
| Jogador 2 | 3-3 | 149 | SELL | STABILIZE | 78.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050333332270383835 | 0.0 | 0.0 | +— / -3880fbd9-322b-4375-b855-fbb779a0cb47 |
| Jogador 2 | 3-3 | 150 | BUY_XP | STABILIZE | 78.0 | 6 | 5 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 152 | BUY | STABILIZE | 78.0 | 6 | 8 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08226115256547928 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 153 | BUY | STABILIZE | 78.0 | 6 | 6 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01573885791003704 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -— |
| Jogador 2 | 3-4 | 154 | BUY | STABILIZE | 78.0 | 6 | 4 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47582539916038513 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 2 | 3-4 | 155 | SELL | STABILIZE | 78.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02019999921321869 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 3-4 | 156 | BUY_XP | STABILIZE | 78.0 | 6 | 4 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 157 | SELL | STABILIZE | 78.0 | 6 | 0 | 0 | 22.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4856666624546051 | 0.0 | 0.0 | +— / -c4c0b136-020d-4c1e-9517-8e0bf4c5a628 |
| Jogador 2 | 3-4 | 158 | SELL | STABILIZE | 78.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0689999982714653 | 0.0 | 0.0 | +— / -c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 2 | 3-4 | 159 | BUY_XP | STABILIZE | 78.0 | 6 | 4 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 0 | 0 | 22.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.681248356064316e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 162 | BUY | STABILIZE | 78.0 | 7 | 6 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7971019744873047 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 163 | BUY | STABILIZE | 78.0 | 7 | 3 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003218004945665598 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 164 | BUY | STABILIZE | 78.0 | 7 | 1 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24807116389274597 | 0.0 | 0.0 | +c5a8f36d-74b1-4944-a3db-bfb601a89b59 / -— |
| Jogador 2 | 3-5 | 165 | SELL | STABILIZE | 78.0 | 7 | 0 | 0 | 22.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014633333310484886 | 0.0 | 0.0 | +— / -c5a8f36d-74b1-4944-a3db-bfb601a89b59 |
| Jogador 2 | 3-5 | 166 | SELL | STABILIZE | 78.0 | 7 | 1 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06709864735603333 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 3-5 | 167 | MOVE_BENCH | STABILIZE | 78.0 | 7 | 3 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5722643136978149 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 3 | 0 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01485569216310978 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 169 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 3 | 0 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014978107064962387 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 170 | PASS | STABILIZE | 78.0 | 7 | 3 | 0 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 172 | BUY | STABILIZE | 78.0 | 7 | 10 | 1 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20796139538288116 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-6 | 173 | BUY | STABILIZE | 78.0 | 7 | 9 | 0 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24630416929721832 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 174 | BUY | STABILIZE | 78.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06447755545377731 | 0.0 | 0.0 | +8fb80cc8-4120-41a0-bc96-35f81a466ed9 / -— |
| Jogador 2 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 2 | 0 | 28.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 2 | 0 | 28.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014926167204976082 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 177 | PASS | STABILIZE | 78.0 | 7 | 2 | 0 | 28.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 182 | SELL | STABILIZE | 67.0 | 7 | 7 | 0 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08563333004713058 | 0.0 | 0.0 | +— / -8fb80cc8-4120-41a0-bc96-35f81a466ed9 |
| Jogador 2 | 3-7 | 183 | BUY | STABILIZE | 67.0 | 7 | 10 | 1 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7539846301078796 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -0c15e414-bc67-46de-a087-fb7708db0dfe,e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-7 | 184 | BUY | STABILIZE | 67.0 | 7 | 7 | 0 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1360320895910263 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 185 | MOVE_BENCH | STABILIZE | 67.0 | 7 | 3 | 0 | 22.0 | Feérico/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5875200033187866 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 186 | BUY | STABILIZE | 67.0 | 7 | 3 | 0 | 24.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01454504020512104 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 2 | 3-7 | 187 | MOVE_BOARD | STABILIZE | 67.0 | 7 | 0 | 0 | 24.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002476694528013468 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 188 | MOVE_BOARD | STABILIZE | 67.0 | 7 | 0 | 0 | 24.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014714875258505344 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 189 | SELL | STABILIZE | 67.0 | 7 | 0 | 0 | 24.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5740000009536743 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 3-7 | 190 | BUY | STABILIZE | 67.0 | 7 | 8 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03735974058508873 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 2 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 67.0 | 7 | 10 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08686518669128418 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 67.0 | 7 | 10 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06219828501343727 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 194 | SELL | STABILIZE | 67.0 | 7 | 10 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00563333323225379 | 0.0 | 0.0 | +— / -ed0dab77-fd87-4677-8428-7505ccd34b86 |
| Jogador 2 | 4-1 | 195 | BUY | STABILIZE | 67.0 | 7 | 13 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1736961305141449 | 0.0 | 0.0 | +a4188ec8-4188-4fdf-8d76-c559fc0c7daf / -— |
| Jogador 2 | 4-1 | 196 | SELL | STABILIZE | 67.0 | 7 | 10 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0038999998942017555 | 0.0 | 0.0 | +— / -a4188ec8-4188-4fdf-8d76-c559fc0c7daf |
| Jogador 2 | 4-1 | 197 | BUY | STABILIZE | 67.0 | 7 | 13 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05066831409931183 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 2 | 4-1 | 198 | SELL | STABILIZE | 67.0 | 7 | 10 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -1be0cdcc-ee10-44dc-ad1b-de9b53b25164 |
| Jogador 2 | 4-1 | 199 | BUY | STABILIZE | 67.0 | 7 | 13 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35055404901504517 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 2 | 4-1 | 200 | SELL | STABILIZE | 67.0 | 7 | 9 | 0 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10713333636522293 | 0.0 | 0.0 | +— / -59304448-26ee-4e38-a52e-014e22ece127 |
| Jogador 2 | 4-2 | 202 | BUY | STABILIZE | 55.0 | 7 | 20 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2536959648132324 | 0.0 | 0.0 | +0534477f-2ff8-47a7-b71b-1a1d5430589e / -— |
| Jogador 2 | 4-2 | 203 | SELL | STABILIZE | 55.0 | 7 | 17 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07609999924898148 | 0.0 | 0.0 | +— / -0534477f-2ff8-47a7-b71b-1a1d5430589e |
| Jogador 2 | 4-2 | 204 | BUY | STABILIZE | 55.0 | 7 | 20 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0675358772277832 | 0.0 | 0.0 | +bd0fdf98-49ca-4e4b-b4ec-72ac9a91e87b / -— |
| Jogador 2 | 4-2 | 205 | SELL | STABILIZE | 55.0 | 7 | 19 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07123333215713501 | 0.0 | 0.0 | +— / -bd0fdf98-49ca-4e4b-b4ec-72ac9a91e87b |
| Jogador 2 | 4-2 | 206 | BUY | STABILIZE | 55.0 | 7 | 20 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3558271527290344 | 0.0 | 0.0 | +967ab606-d775-468a-9c11-5ad0fd0e92f8 / -— |
| Jogador 2 | 4-2 | 207 | SELL | STABILIZE | 55.0 | 7 | 18 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10400000214576721 | 0.0 | 0.0 | +— / -967ab606-d775-468a-9c11-5ad0fd0e92f8 |
| Jogador 2 | 4-2 | 208 | BUY | STABILIZE | 55.0 | 7 | 20 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3558271527290344 | 0.0 | 0.0 | +9bd6852a-b7a4-468c-a8cc-5318f7906eae / -— |
| Jogador 2 | 4-2 | 209 | SELL | STABILIZE | 55.0 | 7 | 18 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10400000214576721 | 0.0 | 0.0 | +— / -9bd6852a-b7a4-468c-a8cc-5318f7906eae |
| Jogador 2 | 4-2 | 210 | BUY | STABILIZE | 55.0 | 7 | 20 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3579524755477905 | 0.0 | 0.0 | +974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 / -— |
| Jogador 2 | 4-3 | 212 | SELL | STABILIZE | 55.0 | 7 | 27 | 2 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02199999988079071 | 0.0 | 0.0 | +— / -974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 |
| Jogador 2 | 4-3 | 213 | BUY | STABILIZE | 55.0 | 7 | 28 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30588093400001526 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 2 | 4-3 | 214 | SELL | STABILIZE | 55.0 | 7 | 25 | 2 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010441876947879791 | 0.0 | 0.0 | +— / -e0445166-70a5-4135-a45e-ff238a95b228 |
| Jogador 2 | 4-3 | 215 | BUY | STABILIZE | 55.0 | 7 | 29 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17186333239078522 | 0.0 | 0.0 | +26462e09-ab6e-4b87-85a8-6bda974b0c45 / -— |
| Jogador 2 | 4-3 | 216 | SELL | STABILIZE | 55.0 | 7 | 26 | 2 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0038999998942017555 | 0.0 | 0.0 | +— / -26462e09-ab6e-4b87-85a8-6bda974b0c45 |
| Jogador 2 | 4-3 | 217 | BUY | STABILIZE | 55.0 | 7 | 29 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27503618597984314 | 0.0 | 0.0 | +60138930-82d5-4f1c-a5fe-a22ea4b70d36 / -— |
| Jogador 2 | 4-3 | 218 | SELL | STABILIZE | 55.0 | 7 | 27 | 2 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -60138930-82d5-4f1c-a5fe-a22ea4b70d36 |
| Jogador 2 | 4-3 | 219 | BUY | STABILIZE | 55.0 | 7 | 29 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27722179889678955 | 0.0 | 0.0 | +7b3e8122-3b51-46b5-94a8-68fb77156e0e / -— |
| Jogador 2 | 4-3 | 220 | SELL | STABILIZE | 55.0 | 7 | 28 | 2 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02199999988079071 | 0.0 | 0.0 | +— / -7b3e8122-3b51-46b5-94a8-68fb77156e0e |
| Jogador 2 | 4-4 | 222 | BUY | STABILIZE | 43.0 | 7 | 36 | 3 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049195319414138794 | 0.0 | 0.0 | +b80a9778-b2ce-411b-8d08-24549c04367c / -— |
| Jogador 2 | 4-4 | 223 | SELL | STABILIZE | 43.0 | 7 | 33 | 3 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -b80a9778-b2ce-411b-8d08-24549c04367c |
| Jogador 2 | 4-4 | 224 | BUY | STABILIZE | 43.0 | 7 | 36 | 3 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.262760192155838 | 0.0 | 0.0 | +b26a039f-581c-4de2-8a75-f7e8a4ef0e4a / -— |
| Jogador 2 | 4-4 | 225 | SELL | STABILIZE | 43.0 | 7 | 33 | 3 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02446993626654148 | 0.0 | 0.0 | +— / -b26a039f-581c-4de2-8a75-f7e8a4ef0e4a |
| Jogador 2 | 4-4 | 226 | BUY | STABILIZE | 43.0 | 7 | 36 | 3 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1872512549161911 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -— |
| Jogador 2 | 4-4 | 227 | SELL | STABILIZE | 43.0 | 7 | 35 | 3 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0018333332845941186 | 0.0 | 0.0 | +— / -ad19ac66-9f86-4c29-8ae7-7222164aece1 |
| Jogador 2 | 4-4 | 228 | BUY | STABILIZE | 43.0 | 7 | 36 | 3 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2725129723548889 | 0.0 | 0.0 | +e4764e13-e26d-4358-980a-c7c625e26726 / -— |
| Jogador 2 | 4-4 | 229 | SELL | STABILIZE | 43.0 | 7 | 33 | 3 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -e4764e13-e26d-4358-980a-c7c625e26726 |
| Jogador 2 | 4-4 | 230 | MOVE_BENCH | STABILIZE | 43.0 | 7 | 36 | 3 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3993896245956421 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 232 | BUY | STABILIZE | 43.0 | 7 | 44 | 4 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8776144981384277 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -— |
| Jogador 2 | 4-5 | 233 | SELL | STABILIZE | 43.0 | 7 | 41 | 4 | 30.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12526458501815796 | 0.0 | 0.0 | +— / -729ccd5b-adc5-4bca-9523-dcb532e93ecb |
| Jogador 2 | 4-5 | 234 | BUY | STABILIZE | 43.0 | 7 | 45 | 4 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03912662714719772 | 0.0 | 0.0 | +262702a6-b710-4129-9dc6-0c1a04514ff9 / -— |
| Jogador 2 | 4-5 | 235 | SELL | STABILIZE | 43.0 | 7 | 43 | 4 | 30.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008933333680033684 | 0.0 | 0.0 | +— / -262702a6-b710-4129-9dc6-0c1a04514ff9 |
| Jogador 2 | 4-5 | 236 | BUY | STABILIZE | 43.0 | 7 | 45 | 4 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26175376772880554 | 0.0 | 0.0 | +84981e98-bfb7-4c49-a020-51cf6d864881 / -— |
| Jogador 2 | 4-5 | 237 | SELL | STABILIZE | 43.0 | 7 | 42 | 4 | 30.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007483221590518951 | 0.0 | 0.0 | +— / -84981e98-bfb7-4c49-a020-51cf6d864881 |
| Jogador 2 | 4-5 | 238 | BUY | STABILIZE | 43.0 | 7 | 45 | 4 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2734104096889496 | 0.0 | 0.0 | +715d5bfc-c8c3-4dec-a247-9e07ee2755e8 / -— |
| Jogador 2 | 4-5 | 239 | SELL | STABILIZE | 43.0 | 7 | 43 | 4 | 30.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -715d5bfc-c8c3-4dec-a247-9e07ee2755e8 |
| Jogador 2 | 4-5 | 240 | BUY | STABILIZE | 43.0 | 7 | 45 | 4 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27340805530548096 | 0.0 | 0.0 | +ac547bcb-d285-480d-b50e-3cfba572db5a / -— |
| Jogador 2 | 4-6 | 242 | SELL | STABILIZE | 43.0 | 7 | 53 | 5 | 30.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -ac547bcb-d285-480d-b50e-3cfba572db5a |
| Jogador 2 | 4-6 | 243 | BUY | STABILIZE | 43.0 | 7 | 55 | 5 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.904272735118866 | 0.0 | 0.0 | +68301141-c9f1-4303-9775-753520772836 / -— |
| Jogador 2 | 4-6 | 244 | SELL | STABILIZE | 43.0 | 7 | 54 | 5 | 30.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5501647591590881 | 0.0 | 0.0 | +— / -2ace989d-3e9e-483b-9b14-cd6b8f171f17 |
| Jogador 2 | 4-6 | 245 | BUY | STABILIZE | 43.0 | 7 | 57 | 5 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9612947106361389 | 0.0 | 0.0 | +b9b38183-663e-43a4-9f9d-02f1bd4d2d24 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-6 | 246 | BUY | STABILIZE | 43.0 | 7 | 56 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07421451807022095 | 0.0 | 0.0 | +d366508d-f33b-485a-8ff3-e5d0a248ae3e / -— |
| Jogador 2 | 4-6 | 247 | SELL | STABILIZE | 43.0 | 7 | 54 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -b9b38183-663e-43a4-9f9d-02f1bd4d2d24 |
| Jogador 2 | 4-6 | 248 | EQUIP_FROM_INVENTORY | STABILIZE | 43.0 | 7 | 57 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13177405297756195 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 249 | BUY | STABILIZE | 43.0 | 7 | 57 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09270142763853073 | 0.0 | 0.0 | +f8a93323-530e-4f9c-99d7-a5ec83b78992 / -— |
| Jogador 2 | 4-6 | 250 | SELL | STABILIZE | 43.0 | 7 | 56 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005191036034375429 | 0.0 | 0.0 | +— / -f8a93323-530e-4f9c-99d7-a5ec83b78992 |
| Jogador 2 | 4-7 | 252 | BUY | STABILIZE | 31.0 | 7 | 67 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19036416709423065 | 0.0 | 0.0 | +98b600a1-736b-437d-a69e-8a7f7235d9c3 / -— |
| Jogador 2 | 4-7 | 253 | SELL | STABILIZE | 31.0 | 7 | 65 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016389286145567894 | 0.0 | 0.0 | +— / -d366508d-f33b-485a-8ff3-e5d0a248ae3e |
| Jogador 2 | 4-7 | 254 | BUY | STABILIZE | 31.0 | 7 | 67 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1071183979511261 | 0.0 | 0.0 | +c7a7408a-e7bd-428d-9935-4d5a002d8d9f / -— |
| Jogador 2 | 4-7 | 255 | SELL | STABILIZE | 31.0 | 7 | 66 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029834378510713577 | 0.0 | 0.0 | +— / -c7a7408a-e7bd-428d-9935-4d5a002d8d9f |
| Jogador 2 | 4-7 | 256 | BUY | STABILIZE | 31.0 | 7 | 67 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04420088231563568 | 0.0 | 0.0 | +55cd39c0-65d5-410e-917e-501f584115fa / -— |
| Jogador 2 | 4-7 | 257 | SELL | STABILIZE | 31.0 | 7 | 66 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026666666381061077 | 0.0 | 0.0 | +— / -55cd39c0-65d5-410e-917e-501f584115fa |
| Jogador 2 | 4-7 | 258 | BUY | STABILIZE | 31.0 | 7 | 67 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2679705321788788 | 0.0 | 0.0 | +e5f38fbd-826a-4067-a33f-86cf7eb98f30 / -— |
| Jogador 2 | 4-7 | 259 | SELL | STABILIZE | 31.0 | 7 | 65 | 5 | 28.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003533333307132125 | 0.0 | 0.0 | +— / -e5f38fbd-826a-4067-a33f-86cf7eb98f30 |
| Jogador 2 | 4-7 | 260 | BUY | STABILIZE | 31.0 | 7 | 67 | 5 | 28.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21247905492782593 | 0.0 | 0.0 | +9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 / -— |
| Jogador 2 | 5-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 31.0 | 7 | 76 | 5 | 28.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08916714787483215 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 31.0 | 7 | 76 | 5 | 28.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14728902280330658 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 264 | SELL | STABILIZE | 31.0 | 7 | 76 | 5 | 28.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01133333332836628 | 0.0 | 0.0 | +— / -9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 |
| Jogador 2 | 5-1 | 265 | BUY | STABILIZE | 31.0 | 7 | 77 | 5 | 28.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3655109405517578 | 0.0 | 0.0 | +1c5a9322-14c8-4df9-937b-842dcaa1f372 / -— |
| Jogador 2 | 5-1 | 266 | SELL | STABILIZE | 31.0 | 7 | 74 | 5 | 28.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.470633327960968 | 0.0 | 0.0 | +— / -584e7960-a541-4d45-8ea1-8a75e288c387 |
| Jogador 2 | 5-1 | 267 | BUY | STABILIZE | 31.0 | 7 | 75 | 5 | 28.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37681013345718384 | 0.0 | 0.0 | +9a96b07c-5b37-4be7-855e-dc2d942e7171 / -— |
| Jogador 2 | 5-1 | 268 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 72 | 5 | 28.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4001026451587677 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 269 | BUY | STABILIZE | 31.0 | 7 | 72 | 5 | 34.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17423875629901886 | 0.0 | 0.0 | +aee0c45d-0178-4238-987f-5ee83dae7bce / -— |
| Jogador 2 | 5-1 | 270 | SELL | STABILIZE | 31.0 | 7 | 67 | 5 | 34.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -a0ebc646-2e71-4b07-9208-401aa0cda6bb |
| Jogador 2 | 5-2 | 272 | BUY | STABILIZE | 31.0 | 7 | 79 | 5 | 34.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0228005647659302 | 0.0 | 0.0 | +2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d / -3bbd7105-b508-437d-ac84-11e01a499779,8aa832ec-4c09-43bd-ae21-baf7268e468d |
| Jogador 2 | 5-2 | 273 | BUY | STABILIZE | 31.0 | 7 | 76 | 5 | 34.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05404436215758324 | 0.0 | 0.0 | +d2afd490-f89f-47c9-8279-a88acde5b1b6 / -— |
| Jogador 2 | 5-2 | 274 | BUY | STABILIZE | 31.0 | 7 | 73 | 5 | 34.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21837937831878662 | 0.0 | 0.0 | +a267d973-f857-4dda-89e1-209bff42ab6f / -— |
| Jogador 2 | 5-2 | 275 | SELL | STABILIZE | 31.0 | 7 | 69 | 5 | 34.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14640000462532043 | 0.0 | 0.0 | +— / -2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d |
| Jogador 2 | 5-2 | 276 | BUY | STABILIZE | 31.0 | 7 | 77 | 5 | 34.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26813510060310364 | 0.0 | 0.0 | +f00a538c-0607-4d8b-babe-7c13daf80c42 / -— |
| Jogador 2 | 5-2 | 277 | SELL | STABILIZE | 31.0 | 7 | 75 | 5 | 34.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -f00a538c-0607-4d8b-babe-7c13daf80c42 |
| Jogador 2 | 5-2 | 278 | BUY | STABILIZE | 31.0 | 7 | 77 | 5 | 34.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26813825964927673 | 0.0 | 0.0 | +76fcc4d0-4988-4e99-8ac0-c251f0b99dcd / -— |
| Jogador 2 | 5-2 | 279 | REROLL | STABILIZE | 31.0 | 7 | 75 | 5 | 34.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 280 | SELL | STABILIZE | 31.0 | 7 | 73 | 5 | 34.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -76fcc4d0-4988-4e99-8ac0-c251f0b99dcd |
| Jogador 2 | 5-3 | 282 | BUY | STABILIZE | 31.0 | 7 | 87 | 5 | 34.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0212970972061157 | 0.0 | 0.0 | +d3fddd9d-ee81-418d-9c58-0baa4ed99f61 / -68301141-c9f1-4303-9775-753520772836,f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 5-3 | 283 | BUY | STABILIZE | 31.0 | 7 | 86 | 5 | 32.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24212905764579773 | 0.0 | 0.0 | +08731924-b808-4070-8c85-2c747847d835 / -— |
| Jogador 2 | 5-3 | 284 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 81 | 5 | 32.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5500085949897766 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 285 | BUY | STABILIZE | 31.0 | 7 | 81 | 5 | 38.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12422060966491699 | 0.0 | 0.0 | +3c5f5211-f30d-44e7-ac68-0ce513a3d614 / -— |
| Jogador 2 | 5-3 | 286 | SELL | STABILIZE | 31.0 | 7 | 79 | 5 | 38.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8474000096321106 | 0.0 | 0.0 | +— / -d3fddd9d-ee81-418d-9c58-0baa4ed99f61 |
| Jogador 2 | 5-3 | 287 | BUY | STABILIZE | 31.0 | 7 | 82 | 5 | 38.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13349737226963043 | 0.0 | 0.0 | +551e9535-d584-4055-a544-ed78d65ecacb / -— |
| Jogador 2 | 5-3 | 288 | MOVE_BOARD | STABILIZE | 31.0 | 7 | 79 | 5 | 38.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.17180480225943e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 289 | MOVE_BOARD | STABILIZE | 31.0 | 7 | 79 | 5 | 38.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014988051727414131 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 290 | PASS | STABILIZE | 31.0 | 7 | 79 | 5 | 38.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14459846913814545 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 292 | SELL | STABILIZE | 31.0 | 7 | 91 | 5 | 38.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -3c5f5211-f30d-44e7-ac68-0ce513a3d614 |
| Jogador 2 | 5-4 | 293 | BUY | STABILIZE | 31.0 | 7 | 93 | 5 | 38.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8936998248100281 | 0.0 | 0.0 | +c93990ff-0a6f-46bc-8fc1-12623d55abc1 / -— |
| Jogador 2 | 5-4 | 294 | SELL | STABILIZE | 31.0 | 7 | 89 | 5 | 38.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -551e9535-d584-4055-a544-ed78d65ecacb |
| Jogador 2 | 5-4 | 295 | BUY | STABILIZE | 31.0 | 7 | 92 | 5 | 38.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15532512962818146 | 0.0 | 0.0 | +194da7dc-39b4-40e3-869d-326ace65137b / -— |
| Jogador 2 | 5-4 | 296 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 89 | 5 | 38.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09990783780813217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 297 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 89 | 5 | 40.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4133784770965576 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 298 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 89 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05475897341966629 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 299 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 89 | 5 | 38.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4147169888019562 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 300 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 89 | 5 | 40.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0850004181265831 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 302 | SELL | STABILIZE | 31.0 | 7 | 100 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -d2afd490-f89f-47c9-8279-a88acde5b1b6 |
| Jogador 2 | 5-5 | 303 | BUY | STABILIZE | 31.0 | 7 | 103 | 5 | 42.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9306617975234985 | 0.0 | 0.0 | +5098782d-1ec1-4a5b-a435-f3c84ab1be0d / -— |
| Jogador 2 | 5-5 | 304 | SELL | STABILIZE | 31.0 | 7 | 100 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.040361933410167694 | 0.0 | 0.0 | +— / -194da7dc-39b4-40e3-869d-326ace65137b |
| Jogador 2 | 5-5 | 305 | BUY | STABILIZE | 31.0 | 7 | 103 | 5 | 42.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.907489001750946 | 0.0 | 0.0 | +6b7f5603-ce44-4b91-8a3e-939c4fbb26ac / -— |
| Jogador 2 | 5-5 | 306 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 101 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06978446245193481 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 307 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 101 | 5 | 38.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41468802094459534 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 308 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 101 | 5 | 40.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08499989658594131 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 309 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 101 | 5 | 42.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05490155145525932 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 310 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 101 | 5 | 38.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4146784543991089 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 312 | SELL | STABILIZE | 31.0 | 7 | 113 | 5 | 40.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -a267d973-f857-4dda-89e1-209bff42ab6f |
| Jogador 2 | 5-6 | 313 | BUY | STABILIZE | 31.0 | 7 | 117 | 5 | 40.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0237746238708496 | 0.0 | 0.0 | +5e8a73b8-846a-49a9-be41-30c3baf2cb55 / -cce8de69-f877-4e86-b720-6aea91e68f47,e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 5-6 | 314 | BUY | STABILIZE | 31.0 | 7 | 114 | 5 | 34.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0237388610839844 | 0.0 | 0.0 | +5d95f8bc-0c01-4c67-8764-4410eb32ee93 / -5098782d-1ec1-4a5b-a435-f3c84ab1be0d,74b1cd6f-12f4-4287-a5f6-9d016663ccf5 |
| Jogador 2 | 5-6 | 315 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 111 | 5 | 28.0 | Vivaz/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10055094212293625 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 316 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 111 | 5 | 30.0 | Vivaz/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.053163424134254456 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 317 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 111 | 5 | 26.0 | Vivaz/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7232696413993835 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 318 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 111 | 5 | 28.0 | Vivaz/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08555220067501068 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 319 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 111 | 5 | 30.0 | Vivaz/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05346384271979332 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 320 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 111 | 5 | 26.0 | Vivaz/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15083572268486023 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 322 | BUY | STABILIZE | 31.0 | 7 | 124 | 5 | 36.0 | Vivaz/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025742435827851295 | 0.0 | 0.0 | +497fbcb9-9d15-43f0-ad71-96eeceeee99d / -— |
| Jogador 2 | 5-7 | 323 | BUY | STABILIZE | 31.0 | 7 | 121 | 5 | 36.0 | Vivaz/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1043967455625534 | 0.0 | 0.0 | +ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 / -— |
| Jogador 2 | 5-7 | 324 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 118 | 5 | 36.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04237937182188034 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 325 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 118 | 5 | 32.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008382449857890606 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 326 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 118 | 5 | 36.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057495951652526855 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 327 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 118 | 5 | 36.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030661460012197495 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 328 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 118 | 5 | 32.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004525991971604526 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 329 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 118 | 5 | 36.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7723355293273926 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 330 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 118 | 5 | 34.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10055267065763474 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 332 | EQUIP_FROM_INVENTORY | STABILIZE | 31.0 | 7 | 130 | 5 | 32.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07642421871423721 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 333 | SELL | STABILIZE | 31.0 | 7 | 130 | 5 | 32.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -5e8a73b8-846a-49a9-be41-30c3baf2cb55 |
| Jogador 2 | 6-1 | 334 | BUY | STABILIZE | 31.0 | 7 | 138 | 5 | 32.0 | Vivaz/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4420672357082367 | 0.0 | 0.0 | +051d83d1-972e-42b2-ab59-376c753ad24e / -— |
| Jogador 2 | 6-1 | 335 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 135 | 5 | 32.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476668171584606 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 336 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 135 | 5 | 36.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7678563594818115 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 337 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 135 | 5 | 34.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08526520431041718 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 338 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 135 | 5 | 32.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012928580865263939 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 339 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 135 | 5 | 36.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7678546905517578 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 340 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 135 | 5 | 34.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10022509098052979 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 342 | SELL | STABILIZE | 31.0 | 7 | 149 | 5 | 36.0 | Vivaz/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -5d95f8bc-0c01-4c67-8764-4410eb32ee93 |
| Jogador 2 | 6-2 | 343 | BUY | STABILIZE | 31.0 | 7 | 157 | 5 | 36.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4328828454017639 | 0.0 | 0.0 | +edd9f925-ac58-4285-a53c-ca70b782c682 / -— |
| Jogador 2 | 6-2 | 344 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 154 | 5 | 36.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08346813172101974 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 345 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 154 | 5 | 32.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012876984663307667 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 346 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 154 | 5 | 36.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00864807516336441 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 347 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 154 | 5 | 36.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06965082883834839 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 348 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 154 | 5 | 32.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012924648821353912 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 349 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 154 | 5 | 36.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7526814341545105 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 350 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 154 | 5 | 34.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1001061275601387 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 352 | SELL | ALL_IN | 14.0 | 7 | 164 | 5 | 32.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014887568540871143 | 0.0 | 0.0 | +— / -ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 |
| Jogador 2 | 6-3 | 353 | BUY | ALL_IN | 14.0 | 7 | 167 | 5 | 32.0 | Vivaz/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9933223128318787 | 0.0 | 0.0 | +e32f79ba-6ddd-4e40-8150-666105cb09b7 / -— |
| Jogador 2 | 6-3 | 354 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 164 | 5 | 32.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04784916341304779 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 355 | SELL | ALL_IN | 14.0 | 7 | 164 | 5 | 36.0 | Vivaz/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06233333423733711 | 0.0 | 0.0 | +— / -08731924-b808-4070-8c85-2c747847d835 |
| Jogador 2 | 6-3 | 356 | BUY | ALL_IN | 14.0 | 7 | 169 | 5 | 36.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4509425163269043 | 0.0 | 0.0 | +0d4bcb6c-af4b-4726-a600-d24420cb04bd / -— |
| Jogador 2 | 6-3 | 357 | SELL | ALL_IN | 14.0 | 7 | 166 | 5 | 36.0 | Vivaz/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1377333402633667 | 0.0 | 0.0 | +— / -0d4bcb6c-af4b-4726-a600-d24420cb04bd |
| Jogador 2 | 6-3 | 358 | BUY | ALL_IN | 14.0 | 7 | 169 | 5 | 36.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4113007187843323 | 0.0 | 0.0 | +28a07a1f-a937-42e3-b3c3-27738ce56c4f / -— |
| Jogador 2 | 6-3 | 359 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 165 | 5 | 36.0 | Vivaz/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7736096978187561 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 360 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 165 | 5 | 34.0 | Vivaz/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08515684306621552 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 362 | SELL | ALL_IN | 14.0 | 7 | 176 | 5 | 32.0 | Vivaz/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01252322643995285 | 0.0 | 0.0 | +— / -aee0c45d-0178-4238-987f-5ee83dae7bce |
| Jogador 2 | 6-4 | 363 | BUY | ALL_IN | 14.0 | 7 | 181 | 5 | 32.0 | Vivaz/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.955764889717102 | 0.0 | 0.0 | +29c2eb81-6c39-41ff-96eb-a3b28d6e4b99 / -— |
| Jogador 2 | 6-4 | 364 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 178 | 5 | 32.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09989780187606812 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 365 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 178 | 5 | 32.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7823334336280823 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 366 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 178 | 5 | 30.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29911038279533386 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 367 | PASS | ALL_IN | 14.0 | 7 | 178 | 5 | 32.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6434125304222107 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 372 | BUY | ALL_IN | 14.0 | 7 | 188 | 5 | 38.0 | Vivaz/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45093896985054016 | 0.0 | 0.0 | +84250843-db6c-4e91-9c6f-b12e36fc31cb / -— |
| Jogador 2 | 6-5 | 373 | SELL | ALL_IN | 14.0 | 7 | 185 | 5 | 38.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1377333402633667 | 0.0 | 0.0 | +— / -84250843-db6c-4e91-9c6f-b12e36fc31cb |
| Jogador 2 | 6-5 | 374 | BUY | ALL_IN | 14.0 | 7 | 188 | 5 | 38.0 | Vivaz/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16612161695957184 | 0.0 | 0.0 | +c06a964e-4ad5-444a-8800-0410c94f5c1f / -— |
| Jogador 2 | 6-5 | 375 | SELL | ALL_IN | 14.0 | 7 | 187 | 5 | 38.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02763725258409977 | 0.0 | 0.0 | +— / -c06a964e-4ad5-444a-8800-0410c94f5c1f |
| Jogador 2 | 6-5 | 376 | BUY | ALL_IN | 14.0 | 7 | 188 | 5 | 38.0 | Vivaz/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23737256228923798 | 0.0 | 0.0 | +1932532c-8c2d-45c1-bdcc-77fc7d6bb4a8 / -— |
| Jogador 2 | 6-5 | 377 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 185 | 5 | 38.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 378 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 185 | 5 | 38.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08489803224802017 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 379 | SELL | ALL_IN | 14.0 | 7 | 185 | 5 | 40.0 | Vivaz/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -1932532c-8c2d-45c1-bdcc-77fc7d6bb4a8 |
| Jogador 2 | 6-5 | 380 | BUY | ALL_IN | 14.0 | 7 | 188 | 5 | 40.0 | Vivaz/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25722411274909973 | 0.0 | 0.0 | +0e1790b6-c2ab-4f31-8cd4-13b505beb06f / -— |
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
| Jogador 3 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0396579504013062 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179773807525635 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009961719624698162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 32 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5894677639007568 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22681869566440582 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21195760369300842 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 46 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.264544814825058 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25187569856643677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23012398183345795 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3955864906311035 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21847811341285706 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007450772449374199 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012296375818550587 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9577486515045166 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 63 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3376089632511139 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 64 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3328060507774353 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26658305525779724 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 75 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8901233673095703 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39217498898506165 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41467806696891785 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 85 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15193122625350952 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 86 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034290023148059845 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 87 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 88 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.047020673984662e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 89 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8984463214874268 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 93 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 94 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 102 | SELL | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010222157463431358 | 0.0 | 0.0 | +— / -5ead8548-7453-4fa1-856e-674995576a48 |
| Jogador 3 | 2-6 | 103 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9474310278892517 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -c70251e8-af44-4466-808f-d49e9e5f57e9,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10645737498998642 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 105 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499595165252686 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 106 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15247750282287598 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 107 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 20.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 108 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2731267511844635 | 0.0 | 0.0 | +d97b6383-1870-48d1-a9b8-6a8ce153c9ce / -— |
| Jogador 3 | 2-6 | 109 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39864757657051086 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 24.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013072052039206028 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 112 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8915395140647888 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 113 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16402792930603027 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 3 | 2-7 | 114 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 24.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 2-7 | 115 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16315743327140808 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 5 | 0 | 24.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00030490270000882447 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 117 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 24.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 118 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5137274861335754 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 119 | BUY | STABILIZE | 100.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12366987019777298 | 0.0 | 0.0 | +432bc6b0-03a8-42f3-a147-d165f4172a8f / -— |
| Jogador 3 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.250615656375885 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 123 | SELL | STABILIZE | 100.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0026212804950773716 | 0.0 | 0.0 | +— / -432bc6b0-03a8-42f3-a147-d165f4172a8f |
| Jogador 3 | 3-1 | 124 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28319963812828064 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.077279858298425e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 127 | BUY_XP | STABILIZE | 100.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.4280583097133785e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 129 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014955910854041576 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 130 | PASS | STABILIZE | 100.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 132 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 133 | MOVE_BOARD | STABILIZE | 91.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023855626583099365 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 134 | PASS | STABILIZE | 91.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 142 | SELL | STABILIZE | 81.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -f19f9e7f-f189-47fe-b571-be5065c6eb39 |
| Jogador 3 | 3-3 | 143 | BUY | STABILIZE | 81.0 | 6 | 14 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8059886693954468 | 0.0 | 0.0 | +f0b6c16b-7610-454c-929d-7152f0a041d3 / -— |
| Jogador 3 | 3-3 | 144 | BUY_XP | STABILIZE | 81.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00885566882789135 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 147 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999785460531712 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 148 | PASS | STABILIZE | 81.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 152 | SELL | STABILIZE | 81.0 | 6 | 14 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022915394976735115 | 0.0 | 0.0 | +— / -41db1132-4e1c-48eb-8a9b-1b2c74cb22ce |
| Jogador 3 | 3-4 | 153 | BUY | STABILIZE | 81.0 | 6 | 16 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8031110167503357 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 3 | 3-4 | 154 | BUY_XP | STABILIZE | 81.0 | 6 | 13 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 155 | BUY_XP | STABILIZE | 81.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 156 | BUY_XP | STABILIZE | 81.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 158 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08482886850833893 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017046572640538216 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 160 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04207063466310501 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 162 | SELL | STABILIZE | 81.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -d97b6383-1870-48d1-a9b8-6a8ce153c9ce |
| Jogador 3 | 3-5 | 163 | BUY | STABILIZE | 81.0 | 6 | 8 | 0 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8335355520248413 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -c3f8419e-a450-4247-bb65-8de8dba1c8ee,d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 3 | 3-5 | 164 | BUY | STABILIZE | 81.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26521825790405273 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 3 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 167 | PASS | STABILIZE | 81.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 172 | BUY | STABILIZE | 68.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8359841704368591 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -bca8862c-5e5b-4a51-9173-79218fbfea3d,f0b6c16b-7610-454c-929d-7152f0a041d3 |
| Jogador 3 | 3-6 | 173 | BUY | STABILIZE | 68.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2230955809354782 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 3 | 3-6 | 174 | BUY | STABILIZE | 68.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011445424519479275 | 0.0 | 0.0 | +1489b596-9339-407a-b49f-d01ecfdd6f78 / -— |
| Jogador 3 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 68.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 68.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014651498757302761 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 177 | PASS | STABILIZE | 68.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 182 | SELL | STABILIZE | 68.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7534999847412109 | 0.0 | 0.0 | +— / -0e31b1ec-3ead-480e-8577-f59bb5486d00 |
| Jogador 3 | 3-7 | 183 | BUY | STABILIZE | 68.0 | 7 | 11 | 1 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20379739999771118 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-7 | 184 | SELL | STABILIZE | 68.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -a9c52953-4532-455b-851f-04079adfd354 |
| Jogador 3 | 3-7 | 185 | BUY | STABILIZE | 68.0 | 7 | 16 | 1 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37499889731407166 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 186 | BUY_XP | STABILIZE | 68.0 | 7 | 13 | 1 | 32.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 187 | BUY_XP | STABILIZE | 68.0 | 7 | 9 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 188 | BUY_XP | STABILIZE | 68.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 189 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 192 | BUY | FAST8 | 68.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7327374219894409 | 0.0 | 0.0 | +15d93457-0760-419e-87db-74223c1cb7f4 / -— |
| Jogador 3 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 68.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11159961670637131 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 194 | CRAFT_AND_EQUIP | FAST8 | 68.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09244579076766968 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 195 | SELL | FAST8 | 68.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016131043434143066 | 0.0 | 0.0 | +— / -1489b596-9339-407a-b49f-d01ecfdd6f78 |
| Jogador 3 | 4-1 | 196 | BUY | FAST8 | 68.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7313587069511414 | 0.0 | 0.0 | +f64919a5-eb2c-4e23-91ed-0067b3d90951 / -— |
| Jogador 3 | 4-1 | 197 | MOVE_BOARD | FAST8 | 68.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.207072434946895e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 198 | MOVE_BOARD | FAST8 | 68.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999953098595142 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 199 | MOVE_BOARD | FAST8 | 68.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999743551015854 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 200 | PASS | FAST8 | 68.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 202 | MOVE_BOARD | FAST8 | 68.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003734444035217166 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 203 | MOVE_BOARD | FAST8 | 68.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011265812441706657 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 204 | PASS | FAST8 | 68.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 212 | MOVE_BOARD | FAST8 | 68.0 | 7 | 15 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 213 | MOVE_BOARD | FAST8 | 68.0 | 7 | 15 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 214 | PASS | FAST8 | 68.0 | 7 | 15 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 222 | MOVE_BOARD | FAST8 | 68.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 223 | MOVE_BOARD | FAST8 | 68.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000098384916782 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 224 | PASS | FAST8 | 68.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030714286491274834 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 232 | SELL | FAST8 | 68.0 | 7 | 31 | 3 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027212878689169884 | 0.0 | 0.0 | +— / -ccdd8153-af58-4fe7-994c-d49f0a7a17f8 |
| Jogador 3 | 4-5 | 233 | BUY | FAST8 | 68.0 | 7 | 35 | 3 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8233214616775513 | 0.0 | 0.0 | +0f5471bd-1451-4979-adc9-aced6bb63610 / -15d93457-0760-419e-87db-74223c1cb7f4,bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed |
| Jogador 3 | 4-5 | 234 | BUY | FAST8 | 68.0 | 7 | 32 | 3 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1529284119606018 | 0.0 | 0.0 | +4c1dab77-0e6d-401b-a341-40117b445957 / -— |
| Jogador 3 | 4-5 | 235 | BUY | FAST8 | 68.0 | 7 | 29 | 2 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11756212264299393 | 0.0 | 0.0 | +fe12befc-b473-4f91-9e51-558a03efa3ad / -— |
| Jogador 3 | 4-5 | 236 | MOVE_BOARD | FAST8 | 68.0 | 7 | 26 | 2 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 237 | MOVE_BOARD | FAST8 | 68.0 | 7 | 26 | 2 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020121173933148384 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 238 | PASS | FAST8 | 68.0 | 7 | 26 | 2 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03285714238882065 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 242 | SELL | FAST8 | 68.0 | 7 | 36 | 3 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -0f5471bd-1451-4979-adc9-aced6bb63610 |
| Jogador 3 | 4-6 | 243 | BUY | FAST8 | 68.0 | 7 | 44 | 4 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.853298008441925 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -79786887-d318-4836-b2f0-c0f03e86cbe5,8a68772c-3f02-4f2e-882b-4fa69fbb6750 |
| Jogador 3 | 4-6 | 244 | MOVE_BENCH | STABILIZE | 68.0 | 7 | 41 | 4 | 24.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32933151721954346 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 245 | BUY | FAST8 | 68.0 | 7 | 41 | 4 | 36.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2704584002494812 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 3 | 4-6 | 246 | MOVE_BOARD | FAST8 | 68.0 | 7 | 40 | 4 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001249518827535212 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 247 | MOVE_BOARD | FAST8 | 68.0 | 7 | 40 | 4 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01218100730329752 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 248 | MOVE_BOARD | FAST8 | 68.0 | 7 | 40 | 4 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 249 | PASS | FAST8 | 68.0 | 7 | 40 | 4 | 36.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04285714402794838 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 252 | BUY | FAST8 | 68.0 | 7 | 53 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2964959740638733 | 0.0 | 0.0 | +50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de / -— |
| Jogador 3 | 4-7 | 253 | MOVE_BOARD | FAST8 | 68.0 | 7 | 50 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.0657563406275585e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 254 | MOVE_BOARD | FAST8 | 68.0 | 7 | 50 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 255 | MOVE_BOARD | FAST8 | 68.0 | 7 | 50 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 256 | PASS | FAST8 | 68.0 | 7 | 50 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 68.0 | 7 | 63 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1525946706533432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 68.0 | 7 | 63 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11757455766201019 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 264 | MOVE_BOARD | FAST8 | 68.0 | 7 | 63 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00012675650941673666 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 265 | MOVE_BOARD | FAST8 | 68.0 | 7 | 63 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017947377637028694 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 266 | PASS | FAST8 | 68.0 | 7 | 63 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09674564003944397 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 272 | SELL | FAST8 | 68.0 | 7 | 77 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03697780519723892 | 0.0 | 0.0 | +— / -fe12befc-b473-4f91-9e51-558a03efa3ad |
| Jogador 3 | 5-2 | 273 | BUY | FAST8 | 68.0 | 7 | 80 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8776038885116577 | 0.0 | 0.0 | +aea521ef-8511-4b98-9c6d-e83b814777df / -— |
| Jogador 3 | 5-2 | 274 | MOVE_BOARD | FAST8 | 68.0 | 7 | 79 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 275 | MOVE_BOARD | FAST8 | 68.0 | 7 | 79 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 276 | PASS | FAST8 | 68.0 | 7 | 79 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1091393530368805 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 282 | SELL | FAST8 | 53.0 | 7 | 89 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 3 | 5-3 | 283 | BUY | FAST8 | 53.0 | 7 | 90 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8418260812759399 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -— |
| Jogador 3 | 5-3 | 284 | SELL | FAST8 | 53.0 | 7 | 87 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42970386147499084 | 0.0 | 0.0 | +— / -9028d514-586b-4d0e-b042-07389323c8cf |
| Jogador 3 | 5-3 | 285 | BUY | FAST8 | 53.0 | 7 | 90 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6491087675094604 | 0.0 | 0.0 | +54574f38-262f-44ac-83da-03088b8bdea3 / -— |
| Jogador 3 | 5-3 | 286 | MOVE_BOARD | FAST8 | 53.0 | 7 | 88 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 287 | MOVE_BOARD | FAST8 | 53.0 | 7 | 88 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 288 | PASS | FAST8 | 53.0 | 7 | 88 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11645875871181488 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 292 | SELL | FAST8 | 53.0 | 7 | 99 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5087980031967163 | 0.0 | 0.0 | +— / -54574f38-262f-44ac-83da-03088b8bdea3 |
| Jogador 3 | 5-4 | 293 | BUY | FAST8 | 53.0 | 7 | 101 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9531795382499695 | 0.0 | 0.0 | +8538e488-6f36-433a-b261-73626f24bb07 / -b75c9bc5-9bc7-465a-a97c-59156e5c482d,f64919a5-eb2c-4e23-91ed-0067b3d90951 |
| Jogador 3 | 5-4 | 294 | BUY | FAST8 | 53.0 | 7 | 98 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3951278030872345 | 0.0 | 0.0 | +e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 / -— |
| Jogador 3 | 5-4 | 295 | BUY | FAST8 | 53.0 | 7 | 96 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2823124825954437 | 0.0 | 0.0 | +93581e04-3f00-4430-8e5b-c953196bc1de / -— |
| Jogador 3 | 5-4 | 296 | MOVE_BOARD | FAST8 | 53.0 | 7 | 94 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0030392538756132126 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 297 | MOVE_BOARD | FAST8 | 53.0 | 7 | 94 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012486644089221954 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 298 | MOVE_BOARD | FAST8 | 53.0 | 7 | 94 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 299 | PASS | FAST8 | 53.0 | 7 | 94 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1214388906955719 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 302 | SELL | FAST8 | 53.0 | 7 | 104 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -8538e488-6f36-433a-b261-73626f24bb07 |
| Jogador 3 | 5-5 | 303 | BUY | FAST8 | 53.0 | 7 | 112 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09865964949131012 | 0.0 | 0.0 | +dc423197-9320-4651-b71d-a62086416f9d / -— |
| Jogador 3 | 5-5 | 304 | SELL | FAST8 | 53.0 | 7 | 107 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04586666822433472 | 0.0 | 0.0 | +— / -dc423197-9320-4651-b71d-a62086416f9d |
| Jogador 3 | 5-5 | 305 | BUY | FAST8 | 53.0 | 7 | 112 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14872270822525024 | 0.0 | 0.0 | +92bac611-1820-42eb-8243-499f20058673 / -— |
| Jogador 3 | 5-5 | 306 | SELL | FAST8 | 53.0 | 7 | 109 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5925999879837036 | 0.0 | 0.0 | +— / -e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 |
| Jogador 3 | 5-5 | 307 | BUY | FAST8 | 53.0 | 7 | 111 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1477043330669403 | 0.0 | 0.0 | +aa803972-8af8-46d7-b430-079819730c36 / -— |
| Jogador 3 | 5-5 | 308 | SELL | FAST8 | 53.0 | 7 | 108 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.060404784977436066 | 0.0 | 0.0 | +— / -92bac611-1820-42eb-8243-499f20058673 |
| Jogador 3 | 5-5 | 309 | BUY | FAST8 | 53.0 | 7 | 111 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07718298584222794 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -— |
| Jogador 3 | 5-5 | 310 | MOVE_BOARD | FAST8 | 53.0 | 7 | 108 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 312 | SELL | FAST8 | 53.0 | 7 | 120 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -2b10436d-ccfe-4329-aef8-2769899b3787 |
| Jogador 3 | 5-6 | 313 | BUY | FAST8 | 53.0 | 7 | 123 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15445144474506378 | 0.0 | 0.0 | +04ebf9b8-7683-4270-b98a-a3bfb342dcf8 / -— |
| Jogador 3 | 5-6 | 314 | SELL | FAST8 | 53.0 | 7 | 120 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05771516263484955 | 0.0 | 0.0 | +— / -04ebf9b8-7683-4270-b98a-a3bfb342dcf8 |
| Jogador 3 | 5-6 | 315 | BUY | FAST8 | 53.0 | 7 | 123 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0781797394156456 | 0.0 | 0.0 | +0f186e00-6f9d-4a22-a1ed-5ccd1b14613d / -— |
| Jogador 3 | 5-6 | 316 | SELL | FAST8 | 53.0 | 7 | 120 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -0f186e00-6f9d-4a22-a1ed-5ccd1b14613d |
| Jogador 3 | 5-6 | 317 | BUY | FAST8 | 53.0 | 7 | 123 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24591001868247986 | 0.0 | 0.0 | +d4e5375b-6b8c-4492-b9cc-ded108270798 / -— |
| Jogador 3 | 5-6 | 318 | SELL | FAST8 | 53.0 | 7 | 119 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -d4e5375b-6b8c-4492-b9cc-ded108270798 |
| Jogador 3 | 5-6 | 319 | BUY | FAST8 | 53.0 | 7 | 123 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08876500278711319 | 0.0 | 0.0 | +4321582a-0b45-4666-a119-7b49e92d012a / -— |
| Jogador 3 | 5-6 | 320 | MOVE_BOARD | FAST8 | 53.0 | 7 | 121 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 322 | SELL | FAST8 | 53.0 | 7 | 133 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07286437600851059 | 0.0 | 0.0 | +— / -aa803972-8af8-46d7-b430-079819730c36 |
| Jogador 3 | 5-7 | 323 | BUY | FAST8 | 53.0 | 7 | 136 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8672500848770142 | 0.0 | 0.0 | +94e47e85-54f4-4546-af6a-3700e3c325a8 / -— |
| Jogador 3 | 5-7 | 324 | SELL | FAST8 | 53.0 | 7 | 135 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34842222929000854 | 0.0 | 0.0 | +— / -4321582a-0b45-4666-a119-7b49e92d012a |
| Jogador 3 | 5-7 | 325 | BUY | FAST8 | 53.0 | 7 | 137 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14587076008319855 | 0.0 | 0.0 | +13169f05-0cd0-4012-89a6-7b47246b475e / -— |
| Jogador 3 | 5-7 | 326 | SELL | FAST8 | 53.0 | 7 | 134 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05764913186430931 | 0.0 | 0.0 | +— / -13169f05-0cd0-4012-89a6-7b47246b475e |
| Jogador 3 | 5-7 | 327 | BUY | FAST8 | 53.0 | 7 | 137 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04899435490369797 | 0.0 | 0.0 | +158c7931-f8db-44bd-a279-53dd6e59b352 / -— |
| Jogador 3 | 5-7 | 328 | SELL | FAST8 | 53.0 | 7 | 134 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4624624252319336 | 0.0 | 0.0 | +— / -93581e04-3f00-4430-8e5b-c953196bc1de |
| Jogador 3 | 5-7 | 329 | BUY | FAST8 | 53.0 | 7 | 136 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03172619640827179 | 0.0 | 0.0 | +335c4988-791a-4579-a473-f387b986806c / -— |
| Jogador 3 | 5-7 | 330 | MOVE_BOARD | FAST8 | 53.0 | 7 | 134 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 332 | EQUIP_FROM_INVENTORY | FAST8 | 53.0 | 7 | 145 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.042388640344142914 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 333 | SELL | FAST8 | 53.0 | 7 | 145 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -335c4988-791a-4579-a473-f387b986806c |
| Jogador 3 | 6-1 | 334 | BUY | FAST8 | 53.0 | 7 | 147 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3383693993091583 | 0.0 | 0.0 | +b5e5c8e4-7fb5-4b4b-b284-f0794e78eadc / -— |
| Jogador 3 | 6-1 | 335 | SELL | FAST8 | 53.0 | 7 | 144 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42989152669906616 | 0.0 | 0.0 | +— / -b5e5c8e4-7fb5-4b4b-b284-f0794e78eadc |
| Jogador 3 | 6-1 | 336 | BUY | FAST8 | 53.0 | 7 | 147 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08111819624900818 | 0.0 | 0.0 | +49eaab97-475e-4663-a2b7-61d755bf19ca / -— |
| Jogador 3 | 6-1 | 337 | SELL | FAST8 | 53.0 | 7 | 144 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04138507321476936 | 0.0 | 0.0 | +— / -49eaab97-475e-4663-a2b7-61d755bf19ca |
| Jogador 3 | 6-1 | 338 | BUY | FAST8 | 53.0 | 7 | 147 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08717965334653854 | 0.0 | 0.0 | +ee093d10-ed4b-4e0e-8e0a-37247f9aa517 / -— |
| Jogador 3 | 6-1 | 339 | SELL | FAST8 | 53.0 | 7 | 144 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002968092914670706 | 0.0 | 0.0 | +— / -ee093d10-ed4b-4e0e-8e0a-37247f9aa517 |
| Jogador 3 | 6-1 | 340 | BUY | FAST8 | 53.0 | 7 | 147 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24756067991256714 | 0.0 | 0.0 | +52799e57-7b54-4dc5-b7f8-c39c8f57e7fa / -— |
| Jogador 3 | 6-2 | 342 | SELL | FAST8 | 53.0 | 7 | 154 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -52799e57-7b54-4dc5-b7f8-c39c8f57e7fa |
| Jogador 3 | 6-2 | 343 | BUY | FAST8 | 53.0 | 7 | 158 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08719795942306519 | 0.0 | 0.0 | +533790d1-aca6-417d-b163-b0bda70d1500 / -— |
| Jogador 3 | 6-2 | 344 | SELL | FAST8 | 53.0 | 7 | 155 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0029649464413523674 | 0.0 | 0.0 | +— / -533790d1-aca6-417d-b163-b0bda70d1500 |
| Jogador 3 | 6-2 | 345 | BUY | FAST8 | 53.0 | 7 | 158 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2022617757320404 | 0.0 | 0.0 | +1cd4d2ae-a25f-4a8d-93e5-42284161b055 / -— |
| Jogador 3 | 6-2 | 346 | SELL | FAST8 | 53.0 | 7 | 155 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -1cd4d2ae-a25f-4a8d-93e5-42284161b055 |
| Jogador 3 | 6-2 | 347 | BUY | FAST8 | 53.0 | 7 | 158 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09135656803846359 | 0.0 | 0.0 | +ff6d5b66-5b8f-49b1-bbad-4231b794c2f1 / -— |
| Jogador 3 | 6-2 | 348 | SELL | FAST8 | 53.0 | 7 | 156 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -ff6d5b66-5b8f-49b1-bbad-4231b794c2f1 |
| Jogador 3 | 6-2 | 349 | BUY | FAST8 | 53.0 | 7 | 158 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26683127880096436 | 0.0 | 0.0 | +14f6071d-5085-47a5-b657-04043b21adce / -— |
| Jogador 3 | 6-2 | 350 | MOVE_BOARD | FAST8 | 53.0 | 7 | 157 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.965929979836801e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 352 | SELL | FAST8 | 53.0 | 7 | 169 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -14f6071d-5085-47a5-b657-04043b21adce |
| Jogador 3 | 6-3 | 353 | BUY | FAST8 | 53.0 | 7 | 170 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9967524409294128 | 0.0 | 0.0 | +23191bf1-a03a-47ab-aa04-1a5b6d86b445 / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 6-3 | 354 | BUY | FAST8 | 53.0 | 7 | 169 | 5 | 40.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3171837031841278 | 0.0 | 0.0 | +f1c48e72-ce66-4b0d-ab88-5d965e06066b / -— |
| Jogador 3 | 6-3 | 355 | SELL | FAST8 | 53.0 | 7 | 167 | 5 | 40.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4256555438041687 | 0.0 | 0.0 | +— / -23191bf1-a03a-47ab-aa04-1a5b6d86b445 |
| Jogador 3 | 6-3 | 356 | BUY | FAST8 | 53.0 | 7 | 170 | 5 | 40.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.07847367227077484 | 0.0 | 0.0 | +7904ab26-de3f-4144-b70f-ed620b41c907 / -— |
| Jogador 3 | 6-3 | 357 | EQUIP_FROM_INVENTORY | FAST8 | 53.0 | 7 | 168 | 5 | 40.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0577334426343441 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 358 | EQUIP_FROM_INVENTORY | FAST8 | 53.0 | 7 | 168 | 5 | 40.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0573318786919117 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 359 | SELL | FAST8 | 53.0 | 7 | 168 | 5 | 40.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007569465320557356 | 0.0 | 0.0 | +— / -7904ab26-de3f-4144-b70f-ed620b41c907 |
| Jogador 3 | 6-3 | 360 | BUY | FAST8 | 53.0 | 7 | 170 | 5 | 40.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2682344913482666 | 0.0 | 0.0 | +c90020e9-0dbe-415a-8745-059dc5d8163f / -— |
| Jogador 3 | 6-4 | 362 | SELL | STABILIZE | 38.0 | 7 | 178 | 5 | 40.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -c90020e9-0dbe-415a-8745-059dc5d8163f |
| Jogador 3 | 6-4 | 363 | BUY | STABILIZE | 38.0 | 7 | 180 | 5 | 40.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6285337209701538 | 0.0 | 0.0 | +1505b8ee-8c59-40ae-b774-fdce1230b8ef / -— |
| Jogador 3 | 6-4 | 364 | SELL | STABILIZE | 38.0 | 7 | 178 | 5 | 40.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10119850933551788 | 0.0 | 0.0 | +— / -f1c48e72-ce66-4b0d-ab88-5d965e06066b |
| Jogador 3 | 6-4 | 365 | BUY | STABILIZE | 38.0 | 7 | 180 | 5 | 40.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20803844928741455 | 0.0 | 0.0 | +5f4811bf-2e06-4dc5-843b-3f0fef851c86 / -— |
| Jogador 3 | 6-4 | 366 | SELL | STABILIZE | 38.0 | 7 | 176 | 5 | 40.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07616817206144333 | 0.0 | 0.0 | +— / -5f4811bf-2e06-4dc5-843b-3f0fef851c86 |
| Jogador 3 | 6-4 | 367 | BUY | STABILIZE | 38.0 | 7 | 180 | 5 | 40.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028476428240537643 | 0.0 | 0.0 | +d14fd3f6-4cb4-4ffe-8f73-ba7946765a85 / -— |
| Jogador 3 | 6-4 | 368 | SELL | STABILIZE | 38.0 | 7 | 177 | 5 | 40.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -d14fd3f6-4cb4-4ffe-8f73-ba7946765a85 |
| Jogador 3 | 6-4 | 369 | BUY | STABILIZE | 38.0 | 7 | 180 | 5 | 40.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017880074679851532 | 0.0 | 0.0 | +fe772b41-d367-4385-b35f-eb5c07754a32 / -— |
| Jogador 3 | 6-4 | 370 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 178 | 5 | 40.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4156216084957123 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 372 | BUY | STABILIZE | 38.0 | 7 | 188 | 5 | 46.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17955833673477173 | 0.0 | 0.0 | +2ce6c216-8ffa-4f9b-b78a-aed96adfa47b / -— |
| Jogador 3 | 6-5 | 373 | SELL | STABILIZE | 38.0 | 7 | 185 | 5 | 46.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -fe772b41-d367-4385-b35f-eb5c07754a32 |
| Jogador 3 | 6-5 | 374 | BUY | STABILIZE | 38.0 | 7 | 187 | 5 | 46.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11542461812496185 | 0.0 | 0.0 | +b1e5b3b9-fda8-4d4a-9368-94fd558da4f7 / -— |
| Jogador 3 | 6-5 | 375 | SELL | STABILIZE | 38.0 | 7 | 186 | 5 | 46.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03200000151991844 | 0.0 | 0.0 | +— / -b1e5b3b9-fda8-4d4a-9368-94fd558da4f7 |
| Jogador 3 | 6-5 | 376 | BUY | STABILIZE | 38.0 | 7 | 187 | 5 | 46.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18033167719841003 | 0.0 | 0.0 | +c339a5f7-66d9-4d5f-b331-4bac23a83a4a / -— |
| Jogador 3 | 6-5 | 377 | SELL | STABILIZE | 38.0 | 7 | 185 | 5 | 46.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007442011963576078 | 0.0 | 0.0 | +— / -c339a5f7-66d9-4d5f-b331-4bac23a83a4a |
| Jogador 3 | 6-5 | 378 | BUY | STABILIZE | 38.0 | 7 | 187 | 5 | 46.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23778171837329865 | 0.0 | 0.0 | +5594beb6-a447-4be2-a6e0-ae5c4f94fe70 / -— |
| Jogador 3 | 6-5 | 379 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 186 | 5 | 46.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 380 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 186 | 5 | 46.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-6 | 382 | SELL | STABILIZE | 38.0 | 7 | 197 | 5 | 46.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -5594beb6-a447-4be2-a6e0-ae5c4f94fe70 |
| Jogador 3 | 6-6 | 383 | BUY | STABILIZE | 38.0 | 7 | 198 | 5 | 46.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3806774318218231 | 0.0 | 0.0 | +6e40ac88-b1d5-4294-b92e-5bc3902fc385 / -— |
| Jogador 3 | 6-6 | 384 | SELL | STABILIZE | 38.0 | 7 | 194 | 5 | 46.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05150216817855835 | 0.0 | 0.0 | +— / -2ce6c216-8ffa-4f9b-b78a-aed96adfa47b |
| Jogador 3 | 6-6 | 385 | BUY | STABILIZE | 38.0 | 7 | 197 | 5 | 46.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12713782489299774 | 0.0 | 0.0 | +8ec344bd-ba9a-47e6-ba65-a4c832038b18 / -— |
| Jogador 3 | 6-6 | 386 | SELL | STABILIZE | 38.0 | 7 | 195 | 5 | 46.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -8ec344bd-ba9a-47e6-ba65-a4c832038b18 |
| Jogador 3 | 6-6 | 387 | BUY | STABILIZE | 38.0 | 7 | 197 | 5 | 46.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0033800045493990183 | 0.0 | 0.0 | +472b4728-efd0-4853-a186-37811f40157a / -— |
| Jogador 3 | 6-6 | 388 | SELL | STABILIZE | 38.0 | 7 | 196 | 5 | 46.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013202567584812641 | 0.0 | 0.0 | +— / -472b4728-efd0-4853-a186-37811f40157a |
| Jogador 3 | 6-6 | 389 | BUY | STABILIZE | 38.0 | 7 | 197 | 5 | 46.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.046425458043813705 | 0.0 | 0.0 | +af23c553-04de-4813-87d0-bb7e4becafe4 / -— |
| Jogador 3 | 6-6 | 390 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 196 | 5 | 46.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
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
| Jogador 4 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16324324905872345 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06005147472023964 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 32 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0128024816513062 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33920297026634216 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.98021000623703 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18392053246498108 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21627572178840637 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 57 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 58 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9554665088653564 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 63 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 64 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 72 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.943898618221283 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 73 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0434507131576538 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 74 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30420637130737305 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 75 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Camille | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5619999766349792 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 76 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 77 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10035662353038788 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 79 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5416666865348816 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-3 | 80 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13736027479171753 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23763549327850342 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15833333134651184 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005146525800228119 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11433333158493042 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08100000023841858 | 0.0 | 0.0 | +— / -0b62545c-1de0-47d8-bb4c-119f7e1526b3 |
| Jogador 4 | 2-4 | 89 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25004059076309204 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 90 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9549951553344727 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 4 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0011781454086304 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -86c535a4-a22b-4667-bc0f-46b4843d97cc,8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37761878967285156 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 94 | SELL | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -4b07138d-44fd-4515-8b65-d7db84f4639c |
| Jogador 4 | 2-5 | 95 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38633617758750916 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 4 | 2-5 | 96 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 97 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6152037382125854 | 0.0 | 0.0 | +— / -c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 4 | 2-5 | 98 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 1 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14828930795192719 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 100 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04833975434303284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 102 | BUY | STABILIZE | 90.0 | 6 | 6 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0516248941421509 | 0.0 | 0.0 | +814d07bd-0296-44af-9626-26a8a224d86f / -— |
| Jogador 4 | 2-6 | 103 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31527045369148254 | 0.0 | 0.0 | +f84bb43d-db12-46dd-a15c-28ef8fdb7fa2 / -— |
| Jogador 4 | 2-6 | 104 | SELL | STABILIZE | 90.0 | 6 | 4 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4323016405105591 | 0.0 | 0.0 | +— / -f84bb43d-db12-46dd-a15c-28ef8fdb7fa2 |
| Jogador 4 | 2-6 | 105 | SELL | STABILIZE | 90.0 | 6 | 5 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5572042465209961 | 0.0 | 0.0 | +— / -a92eca5d-299f-4f4d-a16b-d23981ef719f |
| Jogador 4 | 2-6 | 106 | BUY | STABILIZE | 90.0 | 6 | 8 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11671146005392075 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 107 | BUY_XP | STABILIZE | 90.0 | 6 | 4 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 0 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017364321276545525 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 109 | SELL | STABILIZE | 90.0 | 6 | 0 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09833333641290665 | 0.0 | 0.0 | +— / -b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a |
| Jogador 4 | 2-6 | 110 | BUY | STABILIZE | 90.0 | 6 | 4 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13668185472488403 | 0.0 | 0.0 | +f71a7192-663d-46a0-93ef-b900c59c3bde / -— |
| Jogador 4 | 2-7 | 112 | BUY | STABILIZE | 82.0 | 6 | 8 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1178635358810425 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -814d07bd-0296-44af-9626-26a8a224d86f,9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 2-7 | 113 | BUY | STABILIZE | 82.0 | 6 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3874455392360687 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 4 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27780812978744507 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 115 | BUY_XP | STABILIZE | 82.0 | 6 | 4 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 116 | SELL | STABILIZE | 82.0 | 6 | 0 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -4a0403a3-c999-4d4c-83f0-7270e8576aed |
| Jogador 4 | 2-7 | 117 | BUY | STABILIZE | 82.0 | 6 | 3 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008732828311622143 | 0.0 | 0.0 | +53a27943-148b-4522-9826-3f2e0b8a7858 / -— |
| Jogador 4 | 2-7 | 118 | SELL | STABILIZE | 82.0 | 6 | 1 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06233333423733711 | 0.0 | 0.0 | +— / -53a27943-148b-4522-9826-3f2e0b8a7858 |
| Jogador 4 | 2-7 | 119 | BUY | STABILIZE | 82.0 | 6 | 3 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03959916532039642 | 0.0 | 0.0 | +764470bb-9820-4e49-98f9-5a5f0ce5ca8f / -— |
| Jogador 4 | 2-7 | 120 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 1 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3998219668865204 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 122 | BUY | STABILIZE | 82.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28409284353256226 | 0.0 | 0.0 | +8052731e-e34c-4de7-84b1-2b986cfeddaa / -— |
| Jogador 4 | 3-1 | 123 | BUY | STABILIZE | 82.0 | 6 | 5 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3128894567489624 | 0.0 | 0.0 | +6bbf1aa9-e129-45c6-8668-699425d97c5d / -— |
| Jogador 4 | 3-1 | 124 | BUY | STABILIZE | 82.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2748315632343292 | 0.0 | 0.0 | +cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 / -— |
| Jogador 4 | 3-1 | 125 | CRAFT_AND_EQUIP | STABILIZE | 82.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24370227754116058 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 126 | SELL | STABILIZE | 82.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4323333203792572 | 0.0 | 0.0 | +— / -764470bb-9820-4e49-98f9-5a5f0ce5ca8f |
| Jogador 4 | 3-1 | 127 | BUY | STABILIZE | 82.0 | 6 | 4 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02595176361501217 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.987828626530245e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 129 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01691921055316925 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 130 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013080788776278496 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 132 | BUY | STABILIZE | 82.0 | 6 | 8 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379969000816345 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 133 | BUY | STABILIZE | 82.0 | 6 | 7 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879977822303772 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 6 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33340680599212646 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 135 | BUY | STABILIZE | 82.0 | 6 | 6 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27763575315475464 | 0.0 | 0.0 | +421bcbcb-ecb2-4af8-88d4-7be6cd284d27 / -— |
| Jogador 4 | 3-2 | 136 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3846994638442993 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 137 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5240402817726135 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0021987371146678925 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 139 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09079261869192123 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 140 | PASS | STABILIZE | 82.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 142 | BUY | STABILIZE | 72.0 | 6 | 8 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8035656213760376 | 0.0 | 0.0 | +52018505-08c9-471f-83b9-fd5066efe55a / -— |
| Jogador 4 | 3-3 | 143 | BUY | STABILIZE | 72.0 | 6 | 6 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01921609602868557 | 0.0 | 0.0 | +58c38a13-23c5-4ac1-8601-f0636aeb33ab / -— |
| Jogador 4 | 3-3 | 144 | BUY | STABILIZE | 72.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11897145211696625 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11487174034118652 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17620691657066345 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 147 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014289360493421555 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 148 | PASS | STABILIZE | 72.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 152 | SELL | STABILIZE | 62.0 | 6 | 8 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 3-4 | 153 | BUY | STABILIZE | 62.0 | 6 | 11 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7236806750297546 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 154 | EQUIP_FROM_INVENTORY | STABILIZE | 62.0 | 6 | 8 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04482552781701088 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 155 | EQUIP_FROM_INVENTORY | STABILIZE | 62.0 | 6 | 8 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0606028214097023 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 156 | EQUIP_FROM_INVENTORY | STABILIZE | 62.0 | 6 | 8 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05986315757036209 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 157 | SELL | STABILIZE | 62.0 | 6 | 8 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10400000214576721 | 0.0 | 0.0 | +— / -6bbf1aa9-e129-45c6-8668-699425d97c5d |
| Jogador 4 | 3-4 | 158 | BUY | STABILIZE | 62.0 | 6 | 10 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7549480199813843 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -52018505-08c9-471f-83b9-fd5066efe55a,8052731e-e34c-4de7-84b1-2b986cfeddaa |
| Jogador 4 | 3-4 | 159 | BUY | STABILIZE | 62.0 | 6 | 8 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.678822934627533 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -— |
| Jogador 4 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.6356372043446754e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 162 | BUY | STABILIZE | 62.0 | 6 | 13 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2855207026004791 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -— |
| Jogador 4 | 3-5 | 163 | SELL | STABILIZE | 62.0 | 6 | 11 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -7fd03119-ac82-49e1-b3bb-3a0caa31011f |
| Jogador 4 | 3-5 | 164 | BUY | STABILIZE | 62.0 | 6 | 16 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.448277086019516 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 4 | 3-5 | 165 | SELL | STABILIZE | 62.0 | 6 | 14 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011960970237851143 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 3-5 | 166 | BUY | STABILIZE | 62.0 | 6 | 16 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21379436552524567 | 0.0 | 0.0 | +805375b9-df52-4342-b581-4b92fcd12033 / -— |
| Jogador 4 | 3-5 | 167 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 13 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6577719449996948 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 168 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 13 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3900009095668793 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 169 | PASS | STABILIZE | 62.0 | 6 | 13 | 1 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 172 | SELL | STABILIZE | 52.0 | 6 | 20 | 2 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -805375b9-df52-4342-b581-4b92fcd12033 |
| Jogador 4 | 3-6 | 173 | BUY | STABILIZE | 52.0 | 6 | 23 | 2 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8123083710670471 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 174 | SELL | STABILIZE | 52.0 | 6 | 20 | 2 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004607070237398148 | 0.0 | 0.0 | +— / -58c38a13-23c5-4ac1-8601-f0636aeb33ab |
| Jogador 4 | 3-6 | 175 | BUY | STABILIZE | 52.0 | 6 | 23 | 2 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8140141367912292 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -— |
| Jogador 4 | 3-6 | 176 | SELL | STABILIZE | 52.0 | 6 | 21 | 2 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4873333275318146 | 0.0 | 0.0 | +— / -d754fcfc-6d22-4bc0-8643-8f4bef9afda5 |
| Jogador 4 | 3-6 | 177 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 22 | 2 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039185039699077606 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 178 | SELL | STABILIZE | 52.0 | 6 | 22 | 2 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800427734851837 | 0.0 | 0.0 | +— / -ac8f2a7d-1627-4aa4-a35b-805bce651b0e |
| Jogador 4 | 3-6 | 179 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 23 | 2 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09861903637647629 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 180 | SELL | STABILIZE | 52.0 | 6 | 23 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4907524585723877 | 0.0 | 0.0 | +— / -40f2a32f-1ace-4700-8a79-e6b5d3212036 |
| Jogador 4 | 3-7 | 182 | BUY | STABILIZE | 43.0 | 6 | 33 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8737921714782715 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-7 | 183 | MOVE_BENCH | STABILIZE | 43.0 | 6 | 30 | 3 | 18.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4001396894454956 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 184 | BUY | STABILIZE | 43.0 | 6 | 30 | 3 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14053751528263092 | 0.0 | 0.0 | +59f588eb-e3f3-4907-ab23-af073a26bd6a / -— |
| Jogador 4 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 43.0 | 6 | 28 | 2 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11486612260341644 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 186 | BUY | STABILIZE | 43.0 | 6 | 28 | 2 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2425394356250763 | 0.0 | 0.0 | +eab06dbd-05d4-43b6-88f0-e6abb0e83d34 / -— |
| Jogador 4 | 3-7 | 187 | MOVE_BOARD | STABILIZE | 43.0 | 6 | 26 | 2 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11458025127649307 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 188 | MOVE_BOARD | STABILIZE | 43.0 | 6 | 26 | 2 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014992999844253063 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 189 | MOVE_BOARD | STABILIZE | 43.0 | 6 | 26 | 2 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015452248975634575 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 190 | PASS | STABILIZE | 43.0 | 6 | 26 | 2 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08032740652561188 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 192 | BUY | STABILIZE | 43.0 | 6 | 34 | 3 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8371080756187439 | 0.0 | 0.0 | +465ecc70-f5da-47f4-a7c0-2005a8ed24c1 / -— |
| Jogador 4 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 43.0 | 6 | 33 | 3 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1670372039079666 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 43.0 | 6 | 33 | 3 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20717065036296844 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 195 | BUY | STABILIZE | 43.0 | 6 | 33 | 3 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3198559582233429 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -— |
| Jogador 4 | 4-1 | 196 | MOVE_BENCH | STABILIZE | 43.0 | 6 | 31 | 3 | 22.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39966538548469543 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 197 | MOVE_BENCH | STABILIZE | 43.0 | 6 | 31 | 3 | 24.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6839750409126282 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 198 | PASS | STABILIZE | 43.0 | 6 | 31 | 3 | 20.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038917459547519684 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 202 | SELL | STABILIZE | 31.0 | 6 | 41 | 4 | 20.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5740000009536743 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 4 | 4-2 | 203 | BUY | STABILIZE | 31.0 | 6 | 49 | 4 | 20.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9256765246391296 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -23f4d10f-2614-47b2-bfb2-4fb276764b5e,fe6546c3-86ef-40e1-aa7e-ff7e400fe628 |
| Jogador 4 | 4-2 | 204 | MOVE_BENCH | STABILIZE | 31.0 | 6 | 47 | 4 | 20.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0999731495976448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 205 | BUY | STABILIZE | 31.0 | 6 | 47 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23517422378063202 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 4 | 4-2 | 206 | SELL | STABILIZE | 31.0 | 6 | 44 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -fff5cc22-5f1a-47a4-93e3-9772177b0910 |
| Jogador 4 | 4-2 | 207 | SELL | STABILIZE | 31.0 | 6 | 49 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03204777464270592 | 0.0 | 0.0 | +— / -59f588eb-e3f3-4907-ab23-af073a26bd6a |
| Jogador 4 | 4-2 | 208 | MOVE_BENCH | STABILIZE | 31.0 | 6 | 51 | 5 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3997214138507843 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 209 | MOVE_BENCH | STABILIZE | 31.0 | 6 | 51 | 5 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7182336449623108 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 210 | PASS | STABILIZE | 31.0 | 6 | 51 | 5 | 20.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24561543762683868 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 212 | BUY | ALL_IN | 17.0 | 6 | 64 | 5 | 20.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4567343294620514 | 0.0 | 0.0 | +840740a6-45be-4107-a4b7-b10cefe1a667 / -— |
| Jogador 4 | 4-3 | 213 | BUY | ALL_IN | 17.0 | 6 | 62 | 5 | 20.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41878387331962585 | 0.0 | 0.0 | +651884f1-8453-44cb-ac46-780eb9f7ac86 / -— |
| Jogador 4 | 4-3 | 214 | BUY | ALL_IN | 17.0 | 6 | 59 | 5 | 20.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37977877259254456 | 0.0 | 0.0 | +a9588010-57fa-4baf-b226-a30f519342e7 / -— |
| Jogador 4 | 4-3 | 215 | MOVE_BENCH | ALL_IN | 17.0 | 6 | 56 | 5 | 20.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09983862191438675 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 216 | REROLL | ALL_IN | 17.0 | 6 | 56 | 5 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 217 | SELL | ALL_IN | 17.0 | 6 | 54 | 5 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5163333415985107 | 0.0 | 0.0 | +— / -eab06dbd-05d4-43b6-88f0-e6abb0e83d34 |
| Jogador 4 | 4-3 | 218 | BUY | ALL_IN | 17.0 | 6 | 56 | 5 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9417619705200195 | 0.0 | 0.0 | +f4173576-aa2e-4a93-94ec-ecd49d90d2b7 / -— |
| Jogador 4 | 4-3 | 219 | SELL | ALL_IN | 17.0 | 6 | 54 | 5 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -210d2415-663d-4768-bbc2-238766c2b863 |
| Jogador 4 | 4-3 | 220 | BUY | ALL_IN | 17.0 | 6 | 56 | 5 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0362199544906616 | 0.0 | 0.0 | +bb2e33e3-fe6f-4344-b113-aeba7ace7a2d / -840740a6-45be-4107-a4b7-b10cefe1a667,f4173576-aa2e-4a93-94ec-ecd49d90d2b7 |
| Jogador 4 | 4-4 | 222 | BUY | ALL_IN | 17.0 | 7 | 65 | 5 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05711452662944794 | 0.0 | 0.0 | +84a3b0f5-c448-4fe1-b001-5ceff2ed306a / -— |
| Jogador 4 | 4-4 | 223 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 61 | 5 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39868342876434326 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 224 | BUY | ALL_IN | 17.0 | 7 | 61 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07645667344331741 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -— |
| Jogador 4 | 4-4 | 225 | BUY | ALL_IN | 17.0 | 7 | 58 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2123119831085205 | 0.0 | 0.0 | +1f7f2a48-1318-4fc6-87cc-03d557bf69ea / -— |
| Jogador 4 | 4-4 | 226 | SELL | ALL_IN | 17.0 | 7 | 55 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6988999843597412 | 0.0 | 0.0 | +— / -bb2e33e3-fe6f-4344-b113-aeba7ace7a2d |
| Jogador 4 | 4-4 | 227 | BUY | ALL_IN | 17.0 | 7 | 60 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4071091413497925 | 0.0 | 0.0 | +bb51728e-fcc5-4950-ad03-c864c51c2371 / -— |
| Jogador 4 | 4-4 | 228 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 57 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0010317492997273803 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 229 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 57 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015360035933554173 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 230 | PASS | ALL_IN | 17.0 | 7 | 57 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5968818664550781 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 232 | SELL | ALL_IN | 17.0 | 7 | 67 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 |
| Jogador 4 | 4-5 | 233 | BUY | ALL_IN | 17.0 | 7 | 70 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9376121759414673 | 0.0 | 0.0 | +ded275a3-9551-4816-8112-f0a25524412c / -— |
| Jogador 4 | 4-5 | 234 | SELL | ALL_IN | 17.0 | 7 | 67 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -84a3b0f5-c448-4fe1-b001-5ceff2ed306a |
| Jogador 4 | 4-5 | 235 | BUY | ALL_IN | 17.0 | 7 | 71 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26170167326927185 | 0.0 | 0.0 | +a11208a9-96bf-468e-ab92-2ead6308be26 / -— |
| Jogador 4 | 4-5 | 236 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 67 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0024116169661283493 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 237 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 67 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016055606305599213 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 238 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 67 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36192259192466736 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 239 | PASS | ALL_IN | 17.0 | 7 | 67 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4679373800754547 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 242 | SELL | ALL_IN | 5.0 | 7 | 77 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -a11208a9-96bf-468e-ab92-2ead6308be26 |
| Jogador 4 | 4-6 | 243 | BUY | ALL_IN | 5.0 | 7 | 81 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0874226093292236 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -465ecc70-f5da-47f4-a7c0-2005a8ed24c1,cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 |
| Jogador 4 | 4-6 | 244 | BUY | ALL_IN | 5.0 | 7 | 80 | 5 | 26.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13445447385311127 | 0.0 | 0.0 | +755060be-13bb-4686-9ee9-e53fef2d75b2 / -— |
| Jogador 4 | 4-6 | 245 | MOVE_BENCH | ALL_IN | 5.0 | 7 | 77 | 5 | 26.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7653292417526245 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 246 | MOVE_BENCH | ALL_IN | 5.0 | 7 | 77 | 5 | 26.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6288001537322998 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 247 | BUY | ALL_IN | 5.0 | 7 | 77 | 5 | 32.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11319100856781006 | 0.0 | 0.0 | +1388df2e-8cb4-4e29-8b30-776c29406917 / -— |
| Jogador 4 | 4-6 | 248 | MOVE_BOARD | ALL_IN | 5.0 | 7 | 74 | 5 | 32.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03432098776102066 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 249 | MOVE_BOARD | ALL_IN | 5.0 | 7 | 74 | 5 | 32.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032332733273506165 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 250 | PASS | ALL_IN | 5.0 | 7 | 74 | 5 | 32.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5011171698570251 | 0.0 | 0.0 | +— / -— |
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
| Jogador 5 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.21576929092407227 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3300795257091522 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2885046601295471 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0326727628707886 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19872020184993744 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21272173523902893 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4088628590106964 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22629974782466888 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 59 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9718018174171448 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 64 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0441266298294067 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12275619804859161 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 75 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2461276352405548 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43632903695106506 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 77 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16280856728553772 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03177344799041748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 79 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25779372453689575 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 80 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31068891286849976 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21855023503303528 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05810000002384186 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 85 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08824896812438965 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-4 | 86 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1673087775707245 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07833333313465118 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09786732494831085 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-4 | 89 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 90 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2902471721172333 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3394378125667572 | 0.0 | 0.0 | +2e4ab22c-62d7-425c-9528-2e1315655c24 / -— |
| Jogador 5 | 2-5 | 94 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06970000267028809 | 0.0 | 0.0 | +— / -486e92ad-4dcf-4c0e-a470-e0b87777d380 |
| Jogador 5 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1223333328962326 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 5 | 2-5 | 96 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3170258700847626 | 0.0 | 0.0 | +28f66ef1-93d6-4cc8-a0c9-e84e844dee28 / -— |
| Jogador 5 | 2-5 | 97 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 98 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3515999913215637 | 0.0 | 0.0 | +— / -28f66ef1-93d6-4cc8-a0c9-e84e844dee28 |
| Jogador 5 | 2-5 | 99 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39711591601371765 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36481964588165283 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09186519682407379 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06104522570967674 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 105 | BUY | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05930067598819733 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 106 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08731768280267715 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-6 | 107 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06522078812122345 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 108 | SELL | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43148890137672424 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-6 | 109 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005137316416949034 | 0.0 | 0.0 | +53312511-4e10-4904-82c0-8a8e69c039cd / -— |
| Jogador 5 | 2-6 | 110 | BUY | STABILIZE | 95.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0050762249156832695 | 0.0 | 0.0 | +b6a21130-c9dc-45ad-8ddb-9223b0ec8751 / -— |
| Jogador 5 | 2-7 | 112 | BUY | STABILIZE | 89.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0378309488296509 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -02c39b42-90d5-4e01-9380-460b6c1cb993,eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 2-7 | 113 | BUY | STABILIZE | 89.0 | 6 | 8 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3441135585308075 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 114 | BUY | STABILIZE | 89.0 | 6 | 6 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9609003067016602 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 115 | SELL | STABILIZE | 89.0 | 6 | 4 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 2-7 | 116 | SELL | STABILIZE | 89.0 | 6 | 7 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034699998795986176 | 0.0 | 0.0 | +— / -53312511-4e10-4904-82c0-8a8e69c039cd |
| Jogador 5 | 2-7 | 117 | BUY | STABILIZE | 89.0 | 6 | 8 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06982599198818207 | 0.0 | 0.0 | +6eee9a92-4235-46af-ae42-c38acd6847ef / -— |
| Jogador 5 | 2-7 | 118 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 6 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6024214625358582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 119 | BUY | STABILIZE | 89.0 | 6 | 6 | 0 | 18.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05561622604727745 | 0.0 | 0.0 | +c5593e47-f48a-4362-b230-dfa3d7d36ec9 / -— |
| Jogador 5 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 5 | 0 | 18.0 | Enfeitiçador/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14903807640075684 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 122 | BUY | STABILIZE | 89.0 | 6 | 10 | 1 | 18.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.750347375869751 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -46838f8d-8037-485c-8c34-9639f14ada19,837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-1 | 123 | BUY | STABILIZE | 89.0 | 6 | 8 | 0 | 18.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3534855842590332 | 0.0 | 0.0 | +f7526b6b-8c94-4229-bd3f-1e538c769fec / -— |
| Jogador 5 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 89.0 | 6 | 7 | 0 | 18.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18200376629829407 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 125 | BUY | STABILIZE | 89.0 | 6 | 7 | 0 | 18.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12518657743930817 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 126 | BUY | STABILIZE | 89.0 | 6 | 4 | 0 | 18.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10796134918928146 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 5 | 3-1 | 127 | SELL | STABILIZE | 89.0 | 6 | 2 | 0 | 18.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 7 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15052425861358643 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 129 | SELL | STABILIZE | 89.0 | 6 | 7 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03618874028325081 | 0.0 | 0.0 | +— / -c5593e47-f48a-4362-b230-dfa3d7d36ec9 |
| Jogador 5 | 3-1 | 130 | SELL | STABILIZE | 89.0 | 6 | 8 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011563440784811974 | 0.0 | 0.0 | +— / -a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 |
| Jogador 5 | 3-2 | 132 | BUY | STABILIZE | 79.0 | 6 | 17 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6924597024917603 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 133 | BUY | STABILIZE | 79.0 | 6 | 14 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2717350721359253 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -— |
| Jogador 5 | 3-2 | 134 | BUY | STABILIZE | 79.0 | 6 | 12 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23315779864788055 | 0.0 | 0.0 | +35a674f6-a230-480b-a93f-f7ec76d78658 / -— |
| Jogador 5 | 3-2 | 135 | SELL | STABILIZE | 79.0 | 6 | 10 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3356666564941406 | 0.0 | 0.0 | +— / -35a674f6-a230-480b-a93f-f7ec76d78658 |
| Jogador 5 | 3-2 | 136 | SELL | STABILIZE | 79.0 | 6 | 12 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4327336549758911 | 0.0 | 0.0 | +— / -b6a21130-c9dc-45ad-8ddb-9223b0ec8751 |
| Jogador 5 | 3-2 | 137 | BUY | STABILIZE | 79.0 | 6 | 13 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06330464780330658 | 0.0 | 0.0 | +d218597b-b641-4a4c-867a-41227b83fcff / -— |
| Jogador 5 | 3-2 | 138 | SELL | STABILIZE | 79.0 | 6 | 11 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -f7526b6b-8c94-4229-bd3f-1e538c769fec |
| Jogador 5 | 3-2 | 139 | SELL | STABILIZE | 79.0 | 6 | 12 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33739185333251953 | 0.0 | 0.0 | +— / -d218597b-b641-4a4c-867a-41227b83fcff |
| Jogador 5 | 3-2 | 140 | BUY | STABILIZE | 79.0 | 6 | 14 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06500856578350067 | 0.0 | 0.0 | +1662b43d-12f4-45d6-b1bf-3733d5214808 / -— |
| Jogador 5 | 3-3 | 142 | BUY | STABILIZE | 79.0 | 6 | 20 | 2 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7172430753707886 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -— |
| Jogador 5 | 3-3 | 143 | BUY | STABILIZE | 79.0 | 6 | 18 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28126588463783264 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 144 | BUY | STABILIZE | 79.0 | 6 | 14 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2815595269203186 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 145 | BUY | STABILIZE | 79.0 | 6 | 11 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.037313465029001236 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-3 | 146 | SELL | STABILIZE | 79.0 | 6 | 8 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01336186844855547 | 0.0 | 0.0 | +— / -1662b43d-12f4-45d6-b1bf-3733d5214808 |
| Jogador 5 | 3-3 | 147 | BUY | STABILIZE | 79.0 | 6 | 9 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10898730158805847 | 0.0 | 0.0 | +a29f1c5b-c2f0-48be-b39c-0aa0d57fb94a / -— |
| Jogador 5 | 3-3 | 148 | SELL | STABILIZE | 79.0 | 6 | 7 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024954741820693016 | 0.0 | 0.0 | +— / -a29f1c5b-c2f0-48be-b39c-0aa0d57fb94a |
| Jogador 5 | 3-3 | 149 | SELL | STABILIZE | 79.0 | 6 | 9 | 0 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31601524353027344 | 0.0 | 0.0 | +— / -a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 5 | 3-3 | 150 | SELL | STABILIZE | 79.0 | 6 | 12 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25699999928474426 | 0.0 | 0.0 | +— / -8a4d0946-b80f-4fbb-ab7c-d43c2697c34e |
| Jogador 5 | 3-4 | 152 | BUY | STABILIZE | 69.0 | 6 | 22 | 2 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8271151185035706 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 5 | 3-4 | 153 | BUY | STABILIZE | 69.0 | 6 | 21 | 2 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6972155570983887 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -— |
| Jogador 5 | 3-4 | 154 | BUY | STABILIZE | 69.0 | 6 | 20 | 2 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021839922294020653 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 155 | SELL | STABILIZE | 69.0 | 6 | 18 | 1 | 18.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05505772680044174 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 3-4 | 156 | SELL | STABILIZE | 69.0 | 6 | 20 | 2 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5433428883552551 | 0.0 | 0.0 | +— / -ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 3-4 | 157 | SELL | STABILIZE | 69.0 | 6 | 21 | 2 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5377026796340942 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-4 | 158 | BUY | STABILIZE | 69.0 | 6 | 24 | 2 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034168802201747894 | 0.0 | 0.0 | +46fc5f36-cf3e-422e-89f3-9501ec9d7d12 / -— |
| Jogador 5 | 3-4 | 159 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 22 | 2 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37937840819358826 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 160 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 22 | 2 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38412752747535706 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 162 | BUY | STABILIZE | 69.0 | 6 | 29 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19191959500312805 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-5 | 163 | BUY | STABILIZE | 69.0 | 6 | 26 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06084762141108513 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 164 | SELL | STABILIZE | 69.0 | 6 | 23 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -46fc5f36-cf3e-422e-89f3-9501ec9d7d12 |
| Jogador 5 | 3-5 | 165 | BUY | STABILIZE | 69.0 | 6 | 25 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1541610062122345 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -— |
| Jogador 5 | 3-5 | 166 | SELL | STABILIZE | 69.0 | 6 | 24 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03002181276679039 | 0.0 | 0.0 | +— / -ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 3-5 | 167 | BUY | STABILIZE | 69.0 | 6 | 25 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15262682735919952 | 0.0 | 0.0 | +6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 / -— |
| Jogador 5 | 3-5 | 168 | SELL | STABILIZE | 69.0 | 6 | 24 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0018333332845941186 | 0.0 | 0.0 | +— / -6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 |
| Jogador 5 | 3-5 | 169 | SELL | STABILIZE | 69.0 | 6 | 25 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37033334374427795 | 0.0 | 0.0 | +— / -9bbd1da9-6a26-472c-912e-165ea4031b90 |
| Jogador 5 | 3-5 | 170 | SELL | STABILIZE | 69.0 | 6 | 28 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017946774140000343 | 0.0 | 0.0 | +— / -e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 3-6 | 172 | BUY | STABILIZE | 60.0 | 6 | 40 | 4 | 20.0 | Enfeitiçador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15527866780757904 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-6 | 173 | BUY | STABILIZE | 60.0 | 6 | 38 | 3 | 20.0 | Enfeitiçador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05801970884203911 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-6 | 174 | BUY | STABILIZE | 60.0 | 6 | 36 | 3 | 20.0 | Enfeitiçador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02713809721171856 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -— |
| Jogador 5 | 3-6 | 175 | SELL | STABILIZE | 60.0 | 6 | 35 | 3 | 20.0 | Enfeitiçador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018891815096139908 | 0.0 | 0.0 | +— / -bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 |
| Jogador 5 | 3-6 | 176 | SELL | STABILIZE | 60.0 | 6 | 36 | 3 | 20.0 | Enfeitiçador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37107720971107483 | 0.0 | 0.0 | +— / -750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 5 | 3-6 | 177 | SELL | STABILIZE | 60.0 | 6 | 38 | 3 | 20.0 | Enfeitiçador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -4af85188-f11e-4aca-8165-ba8e7f535670 |
| Jogador 5 | 3-6 | 178 | SELL | STABILIZE | 60.0 | 6 | 41 | 4 | 20.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36409735679626465 | 0.0 | 0.0 | +— / -1457cd1e-c240-4ce5-9217-a91bddfc8807 |
| Jogador 5 | 3-6 | 179 | BUY | STABILIZE | 60.0 | 6 | 43 | 4 | 20.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2096317708492279 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 5 | 3-6 | 180 | SELL | STABILIZE | 60.0 | 6 | 42 | 4 | 20.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3396666646003723 | 0.0 | 0.0 | +— / -82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 |
| Jogador 5 | 3-7 | 182 | BUY | STABILIZE | 60.0 | 6 | 53 | 5 | 20.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9111383557319641 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -— |
| Jogador 5 | 3-7 | 183 | BUY | STABILIZE | 60.0 | 6 | 51 | 5 | 20.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32303857803344727 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 184 | BUY | STABILIZE | 60.0 | 6 | 49 | 4 | 20.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19178451597690582 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 5 | 3-7 | 185 | BUY | STABILIZE | 60.0 | 6 | 46 | 4 | 20.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034992847591638565 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 186 | SELL | STABILIZE | 60.0 | 6 | 43 | 4 | 20.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 5 | 3-7 | 187 | SELL | STABILIZE | 60.0 | 6 | 46 | 4 | 20.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3628294765949249 | 0.0 | 0.0 | +— / -8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 |
| Jogador 5 | 3-7 | 188 | SELL | STABILIZE | 60.0 | 6 | 49 | 4 | 20.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3791833221912384 | 0.0 | 0.0 | +— / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 5 | 3-7 | 189 | SELL | STABILIZE | 60.0 | 6 | 51 | 5 | 20.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6388999819755554 | 0.0 | 0.0 | +— / -1d7b6420-388f-4cb1-b25c-2e5a3dfec742 |
| Jogador 5 | 3-7 | 190 | BUY | STABILIZE | 60.0 | 6 | 54 | 5 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049138154834508896 | 0.0 | 0.0 | +9b509d0e-ae62-4bfa-a551-f46ea68c64f4 / -— |
| Jogador 5 | 4-1 | 192 | BUY | STABILIZE | 60.0 | 6 | 63 | 5 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.004051685333252 | 0.0 | 0.0 | +0c07379e-5dd1-42e9-aa7a-a764f949deee / -135065df-1ebc-413d-86f1-4df28bd3ee41,691cde76-cf1b-4a60-b818-65f790e312ec |
| Jogador 5 | 4-1 | 193 | BUY | STABILIZE | 60.0 | 6 | 61 | 5 | 20.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4169626533985138 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 60.0 | 6 | 58 | 5 | 20.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1249510645866394 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 195 | CRAFT_AND_EQUIP | STABILIZE | 60.0 | 6 | 58 | 5 | 20.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11491114646196365 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 196 | BUY | STABILIZE | 60.0 | 6 | 58 | 5 | 20.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15226848423480988 | 0.0 | 0.0 | +f6de9b7d-1373-459e-b34a-7b878d1a1268 / -— |
| Jogador 5 | 4-1 | 197 | BUY | STABILIZE | 60.0 | 6 | 57 | 5 | 20.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17869782447814941 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 5 | 4-1 | 198 | SELL | STABILIZE | 60.0 | 6 | 54 | 5 | 20.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6414999961853027 | 0.0 | 0.0 | +— / -0c07379e-5dd1-42e9-aa7a-a764f949deee |
| Jogador 5 | 4-1 | 199 | SELL | STABILIZE | 60.0 | 6 | 59 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03763333335518837 | 0.0 | 0.0 | +— / -9b509d0e-ae62-4bfa-a551-f46ea68c64f4 |
| Jogador 5 | 4-1 | 200 | MOVE_BENCH | STABILIZE | 60.0 | 6 | 60 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09471524506807327 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 202 | BUY | STABILIZE | 49.0 | 6 | 70 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9040724039077759 | 0.0 | 0.0 | +93f7279f-b03b-407b-b623-c0a2bd88f877 / -— |
| Jogador 5 | 4-2 | 203 | BUY | STABILIZE | 49.0 | 6 | 69 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04507376253604889 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 5 | 4-2 | 204 | BUY | STABILIZE | 49.0 | 6 | 65 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23892703652381897 | 0.0 | 0.0 | +ef54ddfd-f436-4813-9585-cb652488ffa3 / -— |
| Jogador 5 | 4-2 | 205 | SELL | STABILIZE | 49.0 | 6 | 63 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 |
| Jogador 5 | 4-2 | 206 | BUY | STABILIZE | 49.0 | 6 | 66 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7265165448188782 | 0.0 | 0.0 | +7fd8b302-97aa-4373-94f4-adfcad477ed2 / -— |
| Jogador 5 | 4-2 | 207 | SELL | STABILIZE | 49.0 | 6 | 64 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47382935881614685 | 0.0 | 0.0 | +— / -8a4e95ea-d35a-4690-9313-126b5d86773e |
| Jogador 5 | 4-2 | 208 | BUY | STABILIZE | 49.0 | 6 | 66 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9243789315223694 | 0.0 | 0.0 | +6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb / -7fd8b302-97aa-4373-94f4-adfcad477ed2,ef54ddfd-f436-4813-9585-cb652488ffa3 |
| Jogador 5 | 4-2 | 209 | REROLL | STABILIZE | 49.0 | 6 | 64 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 210 | BUY | STABILIZE | 49.0 | 6 | 62 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24439339339733124 | 0.0 | 0.0 | +63221f24-3b81-4594-8861-ff29651d2298 / -— |
| Jogador 5 | 4-3 | 212 | BUY | STABILIZE | 37.0 | 6 | 70 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9581561088562012 | 0.0 | 0.0 | +17d5d3f2-999d-4788-852b-bda84adb4350 / -93f7279f-b03b-407b-b623-c0a2bd88f877,f6de9b7d-1373-459e-b34a-7b878d1a1268 |
| Jogador 5 | 4-3 | 213 | BUY | STABILIZE | 37.0 | 6 | 69 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3218260407447815 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 5 | 4-3 | 214 | BUY | STABILIZE | 37.0 | 6 | 67 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32324454188346863 | 0.0 | 0.0 | +485dab1f-b3a1-4170-8ed6-c0035072ae9b / -— |
| Jogador 5 | 4-3 | 215 | MOVE_BENCH | STABILIZE | 37.0 | 6 | 65 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3941308856010437 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 216 | MOVE_BENCH | STABILIZE | 37.0 | 6 | 65 | 5 | 16.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.310302197933197 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 217 | PASS | STABILIZE | 37.0 | 6 | 65 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10612819343805313 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 222 | SELL | ALL_IN | 24.0 | 6 | 76 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5989000201225281 | 0.0 | 0.0 | +— / -6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb |
| Jogador 5 | 4-4 | 223 | BUY | ALL_IN | 24.0 | 6 | 81 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0055651664733887 | 0.0 | 0.0 | +8995f621-b355-44ec-816e-797184bdc266 / -2e4ab22c-62d7-425c-9528-2e1315655c24,6084e8d8-82f2-47e3-b8e1-4077ad70efe5 |
| Jogador 5 | 4-4 | 224 | BUY | ALL_IN | 24.0 | 6 | 80 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14652785658836365 | 0.0 | 0.0 | +bae633d7-8337-461a-9a84-9c9758392bb6 / -— |
| Jogador 5 | 4-4 | 225 | BUY | ALL_IN | 24.0 | 6 | 79 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20852844417095184 | 0.0 | 0.0 | +cc9b5fff-2223-4721-a8b2-4f70e196b851 / -— |
| Jogador 5 | 4-4 | 226 | SELL | ALL_IN | 24.0 | 6 | 77 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6766999959945679 | 0.0 | 0.0 | +— / -17d5d3f2-999d-4788-852b-bda84adb4350 |
| Jogador 5 | 4-4 | 227 | BUY | ALL_IN | 24.0 | 6 | 80 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2595100998878479 | 0.0 | 0.0 | +167110eb-b0d0-4873-9ffe-38286dcc5ca2 / -— |
| Jogador 5 | 4-4 | 228 | SELL | ALL_IN | 24.0 | 6 | 79 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6766999959945679 | 0.0 | 0.0 | +— / -8995f621-b355-44ec-816e-797184bdc266 |
| Jogador 5 | 4-4 | 229 | BUY | ALL_IN | 24.0 | 6 | 82 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.301990270614624 | 0.0 | 0.0 | +7b49fb38-6e0e-4a72-a2ce-0527827d36a6 / -— |
| Jogador 5 | 4-4 | 230 | REROLL | ALL_IN | 24.0 | 6 | 81 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 232 | SELL | ALL_IN | 24.0 | 6 | 90 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -bae633d7-8337-461a-9a84-9c9758392bb6 |
| Jogador 5 | 4-5 | 233 | BUY | ALL_IN | 24.0 | 6 | 91 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37821534276008606 | 0.0 | 0.0 | +98b72340-a402-45bc-9493-71263e3168d6 / -— |
| Jogador 5 | 4-5 | 234 | SELL | ALL_IN | 24.0 | 6 | 90 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -cc9b5fff-2223-4721-a8b2-4f70e196b851 |
| Jogador 5 | 4-5 | 235 | BUY | ALL_IN | 24.0 | 6 | 92 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18977037072181702 | 0.0 | 0.0 | +f3e882b5-333e-44e3-ae82-cacacc8b1137 / -— |
| Jogador 5 | 4-5 | 236 | SELL | ALL_IN | 24.0 | 6 | 88 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -f3e882b5-333e-44e3-ae82-cacacc8b1137 |
| Jogador 5 | 4-5 | 237 | BUY | ALL_IN | 24.0 | 6 | 92 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20808465778827667 | 0.0 | 0.0 | +cba152f4-af54-4d82-a35d-67aa165174be / -— |
| Jogador 5 | 4-5 | 238 | SELL | ALL_IN | 24.0 | 6 | 90 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -cba152f4-af54-4d82-a35d-67aa165174be |
| Jogador 5 | 4-5 | 239 | BUY | ALL_IN | 24.0 | 6 | 92 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20808464288711548 | 0.0 | 0.0 | +738fea60-6b44-40f1-9936-43accf852bd7 / -— |
| Jogador 5 | 4-5 | 240 | REROLL | ALL_IN | 24.0 | 6 | 90 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 242 | SELL | ALL_IN | 13.0 | 6 | 99 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -738fea60-6b44-40f1-9936-43accf852bd7 |
| Jogador 5 | 4-6 | 243 | BUY | ALL_IN | 13.0 | 6 | 101 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9762611985206604 | 0.0 | 0.0 | +943437ce-e190-4790-986b-4e66e49637a7 / -— |
| Jogador 5 | 4-6 | 244 | SELL | ALL_IN | 13.0 | 6 | 98 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.093154177069664 | 0.0 | 0.0 | +— / -63221f24-3b81-4594-8861-ff29651d2298 |
| Jogador 5 | 4-6 | 245 | BUY | ALL_IN | 13.0 | 6 | 101 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9224501252174377 | 0.0 | 0.0 | +57d86f23-f167-472f-9878-21dcddc0a5f7 / -— |
| Jogador 5 | 4-6 | 246 | SELL | ALL_IN | 13.0 | 6 | 100 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04371456801891327 | 0.0 | 0.0 | +— / -86530a1f-5325-45fa-bf43-86419ccfda54 |
| Jogador 5 | 4-6 | 247 | BUY | ALL_IN | 13.0 | 6 | 104 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14025701582431793 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -— |
| Jogador 5 | 4-6 | 248 | MOVE_BENCH | ALL_IN | 13.0 | 6 | 103 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07840320467948914 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 249 | SELL | ALL_IN | 13.0 | 6 | 103 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007155637256801128 | 0.0 | 0.0 | +— / -a3def045-2a10-4672-a6d6-255c40fd1c90 |
| Jogador 5 | 4-6 | 250 | BUY | ALL_IN | 13.0 | 6 | 104 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2574920356273651 | 0.0 | 0.0 | +d80c845d-24bc-4053-a60d-5d0122839b0c / -— |
| Jogador 5 | 4-7 | 252 | SELL | ALL_IN | 1.0 | 6 | 114 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -d80c845d-24bc-4053-a60d-5d0122839b0c |
| Jogador 5 | 4-7 | 253 | BUY | ALL_IN | 1.0 | 6 | 116 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9210575222969055 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 5 | 4-7 | 254 | SELL | ALL_IN | 1.0 | 6 | 114 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5924999713897705 | 0.0 | 0.0 | +— / -7b49fb38-6e0e-4a72-a2ce-0527827d36a6 |
| Jogador 5 | 4-7 | 255 | BUY | ALL_IN | 1.0 | 6 | 115 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6773829460144043 | 0.0 | 0.0 | +c69a2be1-356a-4576-9887-6d1790221a5e / -— |
| Jogador 5 | 4-7 | 256 | SELL | ALL_IN | 1.0 | 6 | 113 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -167110eb-b0d0-4873-9ffe-38286dcc5ca2 |
| Jogador 5 | 4-7 | 257 | BUY | ALL_IN | 1.0 | 6 | 114 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43387100100517273 | 0.0 | 0.0 | +2949d735-3c16-4a45-835b-e11a9c12b16a / -— |
| Jogador 5 | 4-7 | 258 | SELL | ALL_IN | 1.0 | 6 | 112 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6277999877929688 | 0.0 | 0.0 | +— / -c69a2be1-356a-4576-9887-6d1790221a5e |
| Jogador 5 | 4-7 | 259 | BUY | ALL_IN | 1.0 | 6 | 114 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2574912905693054 | 0.0 | 0.0 | +ff181737-4995-4a67-add2-4f55cebabbee / -— |
| Jogador 5 | 4-7 | 260 | SELL | ALL_IN | 1.0 | 6 | 112 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -ff181737-4995-4a67-add2-4f55cebabbee |
| Jogador 5 | 5-1 | 262 | BUY | ALL_IN | 1.0 | 7 | 126 | 5 | 20.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1069774627685547 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -60255a84-4f78-49f0-a4f1-d598704c7ee7,943437ce-e190-4790-986b-4e66e49637a7 |
| Jogador 5 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 1.0 | 7 | 123 | 5 | 14.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10789307951927185 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 264 | CRAFT_AND_EQUIP | ALL_IN | 1.0 | 7 | 123 | 5 | 14.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13545580208301544 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 265 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 123 | 5 | 14.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21110795438289642 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 266 | BUY | ALL_IN | 1.0 | 7 | 123 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9457505345344543 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -— |
| Jogador 5 | 5-1 | 267 | BUY | ALL_IN | 1.0 | 7 | 122 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11927163600921631 | 0.0 | 0.0 | +4b1f1146-d580-41e9-987f-c32b1eb98b75 / -— |
| Jogador 5 | 5-1 | 268 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 119 | 5 | 18.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5904959440231323 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 269 | BUY | ALL_IN | 1.0 | 7 | 119 | 5 | 24.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19360849261283875 | 0.0 | 0.0 | +f84cc827-410f-47eb-bd95-bd650acfdd4b / -— |
| Jogador 5 | 5-1 | 270 | MOVE_BOARD | ALL_IN | 1.0 | 7 | 116 | 5 | 24.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004806130658835173 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | -0.15334774553775787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Sentry | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17399217188358307 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2196885347366333 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0373339653015137 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039901405572891235 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012773334980010986 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011599136516451836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 32 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5754001140594482 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.024707317352295 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 43 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1284489929676056 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15215367078781128 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2895250618457794 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 57 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 58 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26265332102775574 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 63 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2473105639219284 | 0.0 | 0.0 | +048e9074-b134-49ed-a105-88dca63d1aa3 / -— |
| Jogador 6 | 2-2 | 64 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -6a01f661-884f-4c25-9dbe-384a6fe3a5e6 |
| Jogador 6 | 2-2 | 65 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07944674044847488 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 66 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 72 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28931790590286255 | 0.0 | 0.0 | +b1ecd1fa-793c-40ad-a9e3-9d35d5030339 / -— |
| Jogador 6 | 2-3 | 73 | BUY | STABILIZE | 89.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18003346025943756 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 74 | BUY | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23817680776119232 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 75 | SELL | STABILIZE | 89.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14501242339611053 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-3 | 76 | SELL | STABILIZE | 89.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1518818438053131 | 0.0 | 0.0 | +— / -b1ecd1fa-793c-40ad-a9e3-9d35d5030339 |
| Jogador 6 | 2-3 | 77 | PASS | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 82 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1829318255186081 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 83 | BUY | STABILIZE | 83.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24054789543151855 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 84 | BUY | STABILIZE | 83.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8068678379058838 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 85 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 86 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013266666792333126 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-4 | 87 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10964435338973999 | 0.0 | 0.0 | +— / -048e9074-b134-49ed-a105-88dca63d1aa3 |
| Jogador 6 | 2-4 | 88 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 89 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14379245042800903 | 0.0 | 0.0 | +— / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 |
| Jogador 6 | 2-4 | 90 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14378976821899414 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-5 | 92 | BUY | STABILIZE | 83.0 | 5 | 10 | 1 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8596822023391724 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 93 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3051208257675171 | 0.0 | 0.0 | +f957e607-dd51-492b-9186-252da4e0c12f / -— |
| Jogador 6 | 2-5 | 94 | BUY_XP | STABILIZE | 83.0 | 5 | 8 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 95 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 96 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.484942764043808 | 0.0 | 0.0 | +— / -f957e607-dd51-492b-9186-252da4e0c12f |
| Jogador 6 | 2-5 | 97 | SELL | STABILIZE | 83.0 | 5 | 1 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49316444993019104 | 0.0 | 0.0 | +— / -a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 2-5 | 98 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 0 | 0 | 8.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2116594761610031 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 100 | SELL | STABILIZE | 83.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-6 | 102 | BUY | STABILIZE | 78.0 | 6 | 9 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3171352446079254 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 103 | BUY_XP | STABILIZE | 78.0 | 6 | 6 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 104 | SELL | STABILIZE | 78.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18617022037506104 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 2-6 | 105 | BUY_XP | STABILIZE | 78.0 | 6 | 5 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006841098889708519 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 107 | SELL | STABILIZE | 78.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-6 | 108 | BUY | STABILIZE | 78.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15727941691875458 | 0.0 | 0.0 | +2a7dd07f-3b48-489c-8822-9ec2434a01cf / -— |
| Jogador 6 | 2-6 | 109 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6007081270217896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020107917487621307 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 112 | BUY | STABILIZE | 78.0 | 6 | 6 | 0 | 12.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3116063177585602 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 113 | BUY | STABILIZE | 78.0 | 6 | 3 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11564478278160095 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 2-7 | 114 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09657106548547745 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05070220306515694 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 117 | PASS | STABILIZE | 78.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 122 | BUY | STABILIZE | 78.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11679896712303162 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 78.0 | 6 | 2 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19527630507946014 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 124 | SELL | STABILIZE | 78.0 | 6 | 2 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07351678609848022 | 0.0 | 0.0 | +— / -2a7dd07f-3b48-489c-8822-9ec2434a01cf |
| Jogador 6 | 3-1 | 125 | BUY | STABILIZE | 78.0 | 6 | 4 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09677563607692719 | 0.0 | 0.0 | +91f05e8c-f467-4f22-9cb0-c814ffa93198 / -— |
| Jogador 6 | 3-1 | 126 | SELL | STABILIZE | 78.0 | 6 | 2 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09366331249475479 | 0.0 | 0.0 | +— / -91f05e8c-f467-4f22-9cb0-c814ffa93198 |
| Jogador 6 | 3-1 | 127 | BUY_XP | STABILIZE | 78.0 | 6 | 4 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 128 | SELL | STABILIZE | 78.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06684678047895432 | 0.0 | 0.0 | +— / -9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 3-1 | 129 | SELL | STABILIZE | 78.0 | 6 | 3 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09566666930913925 | 0.0 | 0.0 | +— / -a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 |
| Jogador 6 | 3-1 | 130 | BUY | STABILIZE | 78.0 | 6 | 6 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10052493959665298 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-2 | 132 | BUY | STABILIZE | 69.0 | 6 | 7 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379297852516174 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -18934be2-4988-4f62-9f62-07ba151231f2,53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 3-2 | 133 | BUY | STABILIZE | 69.0 | 6 | 6 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8251233100891113 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 5 | 0 | 6.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08603986352682114 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 135 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4494313895702362 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 136 | BUY | STABILIZE | 69.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2500462830066681 | 0.0 | 0.0 | +4278eb73-acda-419d-bf9e-53a29ff6900d / -— |
| Jogador 6 | 3-2 | 137 | BUY | STABILIZE | 69.0 | 6 | 4 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010324019938707352 | 0.0 | 0.0 | +9204a42c-6310-4b08-9bc7-8a2e786b077a / -— |
| Jogador 6 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 2 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037598222494125366 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 139 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 2 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13687263429164886 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 140 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 2 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05400014668703079 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 142 | BUY | STABILIZE | 57.0 | 6 | 8 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28242337703704834 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 143 | BUY | STABILIZE | 57.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09311366826295853 | 0.0 | 0.0 | +31c30451-3999-47b1-8bcf-77e137137b2a / -— |
| Jogador 6 | 3-3 | 144 | SELL | STABILIZE | 57.0 | 6 | 3 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4949144423007965 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 3-3 | 145 | EQUIP_FROM_INVENTORY | STABILIZE | 57.0 | 6 | 6 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15578892827033997 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 146 | EQUIP_FROM_INVENTORY | STABILIZE | 57.0 | 6 | 6 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.18792887032032013 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 147 | EQUIP_FROM_INVENTORY | STABILIZE | 57.0 | 6 | 6 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14461596310138702 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 148 | MOVE_BENCH | STABILIZE | 57.0 | 6 | 6 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.318057119846344 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 57.0 | 6 | 6 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 57.0 | 6 | 6 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 152 | BUY | STABILIZE | 57.0 | 6 | 12 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1963455229997635 | 0.0 | 0.0 | +ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c / -— |
| Jogador 6 | 3-4 | 153 | BUY | STABILIZE | 57.0 | 6 | 9 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2407197207212448 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -— |
| Jogador 6 | 3-4 | 154 | MOVE_BOARD | STABILIZE | 57.0 | 6 | 5 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0525372140109539 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 155 | BUY | STABILIZE | 57.0 | 6 | 5 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056123748421669006 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 6 | 3-4 | 156 | MOVE_BOARD | STABILIZE | 57.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12912872433662415 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 57.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 158 | PASS | STABILIZE | 57.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 162 | BUY | STABILIZE | 57.0 | 6 | 7 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04503481835126877 | 0.0 | 0.0 | +9443e3b5-f0a2-4ab7-8378-907a3d2bccaa / -— |
| Jogador 6 | 3-5 | 163 | BUY | STABILIZE | 57.0 | 6 | 5 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02240164577960968 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 164 | MOVE_BOARD | STABILIZE | 57.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 57.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0032129797618836164 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 166 | PASS | STABILIZE | 57.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 172 | SELL | STABILIZE | 57.0 | 6 | 9 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08579999953508377 | 0.0 | 0.0 | +— / -31c30451-3999-47b1-8bcf-77e137137b2a |
| Jogador 6 | 3-6 | 173 | BUY | STABILIZE | 57.0 | 6 | 11 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46458005905151367 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 174 | SELL | STABILIZE | 57.0 | 6 | 8 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056803133338689804 | 0.0 | 0.0 | +— / -9204a42c-6310-4b08-9bc7-8a2e786b077a |
| Jogador 6 | 3-6 | 175 | BUY | STABILIZE | 57.0 | 6 | 10 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03419565409421921 | 0.0 | 0.0 | +604cc5dc-6c20-4d5a-b3a7-8862adfe1930 / -— |
| Jogador 6 | 3-6 | 176 | SELL | STABILIZE | 57.0 | 6 | 8 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056809380650520325 | 0.0 | 0.0 | +— / -604cc5dc-6c20-4d5a-b3a7-8862adfe1930 |
| Jogador 6 | 3-6 | 177 | BUY | STABILIZE | 57.0 | 6 | 10 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15535585582256317 | 0.0 | 0.0 | +ab050f92-777b-429f-9ed8-9b6c63794641 / -— |
| Jogador 6 | 3-6 | 178 | SELL | STABILIZE | 57.0 | 6 | 8 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08579999953508377 | 0.0 | 0.0 | +— / -ab050f92-777b-429f-9ed8-9b6c63794641 |
| Jogador 6 | 3-6 | 179 | BUY | STABILIZE | 57.0 | 6 | 10 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15535449981689453 | 0.0 | 0.0 | +ab472080-6e4b-4b75-b37d-cf10da9a5a0d / -— |
| Jogador 6 | 3-6 | 180 | MOVE_BOARD | STABILIZE | 57.0 | 6 | 8 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20273222029209137 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 182 | SELL | STABILIZE | 46.0 | 6 | 13 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -ab472080-6e4b-4b75-b37d-cf10da9a5a0d |
| Jogador 6 | 3-7 | 183 | BUY | STABILIZE | 46.0 | 6 | 15 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10928434878587723 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 184 | SELL | STABILIZE | 46.0 | 6 | 11 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03797534480690956 | 0.0 | 0.0 | +— / -9443e3b5-f0a2-4ab7-8378-907a3d2bccaa |
| Jogador 6 | 3-7 | 185 | BUY | STABILIZE | 46.0 | 6 | 13 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03084256500005722 | 0.0 | 0.0 | +89cec488-9a0e-4838-b486-2504a0742476 / -— |
| Jogador 6 | 3-7 | 186 | SELL | STABILIZE | 46.0 | 6 | 11 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -89cec488-9a0e-4838-b486-2504a0742476 |
| Jogador 6 | 3-7 | 187 | BUY | STABILIZE | 46.0 | 6 | 13 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09214136004447937 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 6 | 3-7 | 188 | SELL | STABILIZE | 46.0 | 6 | 10 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012509957887232304 | 0.0 | 0.0 | +— / -665661af-7240-4a65-bf3d-f4ecf3532a85 |
| Jogador 6 | 3-7 | 189 | MOVE_BOARD | STABILIZE | 46.0 | 6 | 13 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 190 | SELL | STABILIZE | 46.0 | 6 | 13 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09300000220537186 | 0.0 | 0.0 | +— / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 |
| Jogador 6 | 4-1 | 192 | BUY | STABILIZE | 46.0 | 6 | 22 | 2 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04546370729804039 | 0.0 | 0.0 | +78525c90-c4d2-425d-ba90-a03664c60a28 / -— |
| Jogador 6 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 46.0 | 6 | 20 | 2 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2505341172218323 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 46.0 | 6 | 20 | 2 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20996415615081787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 195 | BUY | STABILIZE | 46.0 | 6 | 20 | 2 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.040966298431158066 | 0.0 | 0.0 | +45d53a67-4ed4-495d-8751-5ea0f72f91e9 / -— |
| Jogador 6 | 4-1 | 196 | SELL | STABILIZE | 46.0 | 6 | 19 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05649999901652336 | 0.0 | 0.0 | +— / -45d53a67-4ed4-495d-8751-5ea0f72f91e9 |
| Jogador 6 | 4-1 | 197 | BUY | STABILIZE | 46.0 | 6 | 20 | 2 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34490570425987244 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -— |
| Jogador 6 | 4-1 | 198 | REROLL | STABILIZE | 46.0 | 6 | 17 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20399999618530273 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 199 | SELL | STABILIZE | 46.0 | 6 | 15 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02324032410979271 | 0.0 | 0.0 | +— / -78525c90-c4d2-425d-ba90-a03664c60a28 |
| Jogador 6 | 4-1 | 200 | BUY | STABILIZE | 46.0 | 6 | 17 | 1 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.802488386631012 | 0.0 | 0.0 | +b750b244-a898-479e-9a8e-f30a3f4b0005 / -— |
| Jogador 6 | 4-2 | 202 | MOVE_BENCH | STABILIZE | 36.0 | 7 | 21 | 2 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36312317848205566 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 203 | BUY | STABILIZE | 36.0 | 7 | 21 | 2 | 24.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10294204950332642 | 0.0 | 0.0 | +00f38555-1887-4fe2-9930-934055269095 / -— |
| Jogador 6 | 4-2 | 204 | MOVE_BENCH | STABILIZE | 36.0 | 7 | 17 | 1 | 24.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2883048951625824 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 205 | SELL | STABILIZE | 36.0 | 7 | 17 | 1 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044767796993255615 | 0.0 | 0.0 | +— / -4278eb73-acda-419d-bf9e-53a29ff6900d |
| Jogador 6 | 4-2 | 206 | BUY | STABILIZE | 36.0 | 7 | 18 | 1 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01971396617591381 | 0.0 | 0.0 | +bf0751f0-8094-4441-adb3-e5f8b4158426 / -— |
| Jogador 6 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 16 | 1 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0022053357679396868 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 16 | 1 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02865147404372692 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 209 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 16 | 1 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 210 | PASS | STABILIZE | 36.0 | 7 | 16 | 1 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028914285823702812 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 212 | SELL | ALL_IN | 24.0 | 7 | 23 | 2 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010600225999951363 | 0.0 | 0.0 | +— / -bf0751f0-8094-4441-adb3-e5f8b4158426 |
| Jogador 6 | 4-3 | 213 | BUY | ALL_IN | 24.0 | 7 | 25 | 2 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35117825865745544 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 6 | 4-3 | 214 | SELL | ALL_IN | 24.0 | 7 | 24 | 2 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02324041910469532 | 0.0 | 0.0 | +— / -f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 6 | 4-3 | 215 | BUY | ALL_IN | 24.0 | 7 | 27 | 2 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005618272814899683 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 6 | 4-3 | 216 | SELL | ALL_IN | 24.0 | 7 | 24 | 2 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002105759223923087 | 0.0 | 0.0 | +— / -1fa69553-5270-4459-986b-600f748711b7 |
| Jogador 6 | 4-3 | 217 | BUY | ALL_IN | 24.0 | 7 | 27 | 2 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2447320818901062 | 0.0 | 0.0 | +579b987a-fedf-45d8-92fc-634a041d3d4f / -— |
| Jogador 6 | 4-3 | 218 | MOVE_BOARD | ALL_IN | 24.0 | 7 | 24 | 2 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 219 | MOVE_BOARD | ALL_IN | 24.0 | 7 | 24 | 2 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09654279798269272 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 220 | PASS | ALL_IN | 24.0 | 7 | 24 | 2 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36885079741477966 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 222 | SELL | ALL_IN | 24.0 | 7 | 32 | 3 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -579b987a-fedf-45d8-92fc-634a041d3d4f |
| Jogador 6 | 4-4 | 223 | BUY | ALL_IN | 24.0 | 7 | 35 | 3 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09530546516180038 | 0.0 | 0.0 | +42cf45df-f7dd-418d-a241-d89e69523352 / -— |
| Jogador 6 | 4-4 | 224 | SELL | ALL_IN | 24.0 | 7 | 32 | 3 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0141333332285285 | 0.0 | 0.0 | +— / -4eedd873-e4ec-41e5-9f5e-48e443e80f86 |
| Jogador 6 | 4-4 | 225 | BUY | ALL_IN | 24.0 | 7 | 36 | 3 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01029044296592474 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 6 | 4-4 | 226 | SELL | ALL_IN | 24.0 | 7 | 34 | 3 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023115547373890877 | 0.0 | 0.0 | +— / -d175e09c-3ed6-4fb3-8c97-0c167862e29e |
| Jogador 6 | 4-4 | 227 | BUY | ALL_IN | 24.0 | 7 | 36 | 3 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06367553770542145 | 0.0 | 0.0 | +d53646ff-bb49-4f82-b761-faa4657f01cc / -— |
| Jogador 6 | 4-4 | 228 | REROLL | ALL_IN | 24.0 | 7 | 35 | 3 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 229 | SELL | ALL_IN | 24.0 | 7 | 33 | 3 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -42cf45df-f7dd-418d-a241-d89e69523352 |
| Jogador 6 | 4-4 | 230 | BUY | ALL_IN | 24.0 | 7 | 36 | 3 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8735199570655823 | 0.0 | 0.0 | +fcc4f620-7b85-40ed-a42c-2eadd37a82fd / -— |
| Jogador 6 | 4-5 | 232 | SELL | ALL_IN | 24.0 | 7 | 40 | 4 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0022486650850623846 | 0.0 | 0.0 | +— / -00f38555-1887-4fe2-9930-934055269095 |
| Jogador 6 | 4-5 | 233 | BUY | ALL_IN | 24.0 | 7 | 44 | 4 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9687122702598572 | 0.0 | 0.0 | +6e1d8af0-7f7c-4ec1-967c-e871072bc4e3 / -ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b,b750b244-a898-479e-9a8e-f30a3f4b0005 |
| Jogador 6 | 4-5 | 234 | BUY | ALL_IN | 24.0 | 7 | 41 | 4 | 24.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006279562599956989 | 0.0 | 0.0 | +4a885bc0-41b4-43f1-94d3-8e755a10645c / -— |
| Jogador 6 | 4-5 | 235 | MOVE_BENCH | ALL_IN | 24.0 | 7 | 38 | 3 | 24.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.529268741607666 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 236 | BUY | ALL_IN | 24.0 | 7 | 38 | 3 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002552360761910677 | 0.0 | 0.0 | +99182042-c4b9-4801-b66a-1f4432d301f3 / -— |
| Jogador 6 | 4-5 | 237 | MOVE_BOARD | ALL_IN | 24.0 | 7 | 35 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16310185194015503 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 238 | MOVE_BOARD | ALL_IN | 24.0 | 7 | 35 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01856280490756035 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 239 | MOVE_BOARD | ALL_IN | 24.0 | 7 | 35 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005728311836719513 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 240 | MOVE_BOARD | ALL_IN | 24.0 | 7 | 35 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015824826434254646 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 242 | SELL | ALL_IN | 24.0 | 7 | 45 | 4 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5867000222206116 | 0.0 | 0.0 | +— / -6e1d8af0-7f7c-4ec1-967c-e871072bc4e3 |
| Jogador 6 | 4-6 | 243 | BUY | ALL_IN | 24.0 | 7 | 53 | 5 | 26.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0045233964920044 | 0.0 | 0.0 | +deb56311-9843-48be-9a22-3529305d04e5 / -333cdd27-0114-4d36-8ffa-e79b0f43b8e8,cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 4-6 | 244 | BUY | ALL_IN | 24.0 | 7 | 50 | 5 | 26.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055413618683815 | 0.0 | 0.0 | +d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 / -— |
| Jogador 6 | 4-6 | 245 | BUY | ALL_IN | 24.0 | 7 | 46 | 4 | 26.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21640367805957794 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -— |
| Jogador 6 | 4-6 | 246 | REROLL | ALL_IN | 24.0 | 7 | 43 | 4 | 26.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 247 | SELL | ALL_IN | 24.0 | 7 | 41 | 4 | 26.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6567999720573425 | 0.0 | 0.0 | +— / -deb56311-9843-48be-9a22-3529305d04e5 |
| Jogador 6 | 4-6 | 248 | BUY | ALL_IN | 24.0 | 7 | 49 | 4 | 26.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07752799242734909 | 0.0 | 0.0 | +91966802-adc2-46d2-9e7e-194283bca85c / -— |
| Jogador 6 | 4-6 | 249 | SELL | ALL_IN | 24.0 | 7 | 46 | 4 | 26.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00563333323225379 | 0.0 | 0.0 | +— / -4a885bc0-41b4-43f1-94d3-8e755a10645c |
| Jogador 6 | 4-6 | 250 | BUY | ALL_IN | 24.0 | 7 | 49 | 4 | 26.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045539405196905136 | 0.0 | 0.0 | +5416d773-cb2c-442a-8ee9-0d46d22c2087 / -— |
| Jogador 6 | 4-7 | 252 | SELL | ALL_IN | 14.0 | 7 | 56 | 5 | 26.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026744311675429344 | 0.0 | 0.0 | +— / -d53646ff-bb49-4f82-b761-faa4657f01cc |
| Jogador 6 | 4-7 | 253 | BUY | ALL_IN | 14.0 | 7 | 57 | 5 | 26.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0493226051330566 | 0.0 | 0.0 | +e270a6b1-23dd-49a0-8694-ba911eae4c71 / -3cb4d077-df9a-4fd2-9a68-7301aff1b657,3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 4-7 | 254 | SELL | ALL_IN | 14.0 | 7 | 56 | 5 | 22.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7046999931335449 | 0.0 | 0.0 | +— / -e270a6b1-23dd-49a0-8694-ba911eae4c71 |
| Jogador 6 | 4-7 | 255 | BUY | ALL_IN | 14.0 | 7 | 59 | 5 | 22.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.4559013545513153 | 0.0 | 0.0 | +678a6f43-ca48-46c9-8c5b-6790493f4841 / -— |
| Jogador 6 | 4-7 | 256 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 7 | 56 | 5 | 22.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1784326285123825 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 257 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 56 | 5 | 22.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.1573459655046463 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 258 | BUY | ALL_IN | 14.0 | 7 | 56 | 5 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8928738236427307 | 0.0 | 0.0 | +9af900db-c181-448a-9736-30f08f062a00 / -— |
| Jogador 6 | 4-7 | 259 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 7 | 53 | 5 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15272070467472076 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 260 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 7 | 53 | 5 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14019717276096344 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 14.0 | 7 | 63 | 5 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1897772252559662 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 14.0 | 7 | 63 | 5 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11025350540876389 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 264 | SELL | ALL_IN | 14.0 | 7 | 63 | 5 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02034616284072399 | 0.0 | 0.0 | +— / -5416d773-cb2c-442a-8ee9-0d46d22c2087 |
| Jogador 6 | 5-1 | 265 | BUY | ALL_IN | 14.0 | 7 | 65 | 5 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3998667299747467 | 0.0 | 0.0 | +af404167-469a-447e-b415-dcb52033ef9b / -— |
| Jogador 6 | 5-1 | 266 | SELL | ALL_IN | 14.0 | 7 | 61 | 5 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 |
| Jogador 6 | 5-1 | 267 | BUY | ALL_IN | 14.0 | 7 | 65 | 5 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05877617746591568 | 0.0 | 0.0 | +a1357716-abf4-4d4f-abb8-34f2681f16dd / -— |
| Jogador 6 | 5-1 | 268 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 61 | 5 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3992289900779724 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 269 | BUY | ALL_IN | 14.0 | 7 | 61 | 5 | 34.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030365701764822006 | 0.0 | 0.0 | +2f2b455f-7035-4948-9429-612018ae7063 / -— |
| Jogador 6 | 5-1 | 270 | MOVE_BOARD | ALL_IN | 14.0 | 7 | 58 | 5 | 34.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009701218223199248 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 272 | SELL | ALL_IN | 14.0 | 7 | 68 | 5 | 34.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00426666671410203 | 0.0 | 0.0 | +— / -2f2b455f-7035-4948-9429-612018ae7063 |
| Jogador 6 | 5-2 | 273 | BUY | ALL_IN | 14.0 | 7 | 71 | 5 | 34.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7014266848564148 | 0.0 | 0.0 | +3faf4ab2-44b3-4779-985b-658c64791c28 / -— |
| Jogador 6 | 5-2 | 274 | MOVE_BOARD | ALL_IN | 14.0 | 7 | 68 | 5 | 34.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002549595432356 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 275 | SELL | ALL_IN | 14.0 | 7 | 68 | 5 | 34.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -a1357716-abf4-4d4f-abb8-34f2681f16dd |
| Jogador 6 | 5-2 | 276 | BUY | ALL_IN | 14.0 | 7 | 72 | 5 | 34.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009594118222594261 | 0.0 | 0.0 | +8756c125-e3d6-4f40-80d2-a6bf20e7b1c7 / -— |
| Jogador 6 | 5-2 | 277 | MOVE_BOARD | ALL_IN | 14.0 | 7 | 70 | 5 | 34.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 278 | MOVE_BOARD | ALL_IN | 14.0 | 7 | 70 | 5 | 34.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014506912790238857 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 279 | PASS | ALL_IN | 14.0 | 7 | 70 | 5 | 34.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49322932958602905 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 282 | SELL | ALL_IN | 14.0 | 7 | 81 | 5 | 34.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -8756c125-e3d6-4f40-80d2-a6bf20e7b1c7 |
| Jogador 6 | 5-3 | 283 | BUY | ALL_IN | 14.0 | 7 | 83 | 5 | 34.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9857990145683289 | 0.0 | 0.0 | +3eccad10-cc50-4695-852e-0809356dd33b / -678a6f43-ca48-46c9-8c5b-6790493f4841,99182042-c4b9-4801-b66a-1f4432d301f3 |
| Jogador 6 | 5-3 | 284 | BUY | ALL_IN | 14.0 | 7 | 80 | 5 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4399867653846741 | 0.0 | 0.0 | +caeaaabc-213a-4018-97f3-8797a0711863 / -— |
| Jogador 6 | 5-3 | 285 | SELL | ALL_IN | 14.0 | 7 | 79 | 5 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0813969299197197 | 0.0 | 0.0 | +— / -3eccad10-cc50-4695-852e-0809356dd33b |
| Jogador 6 | 5-3 | 286 | BUY | ALL_IN | 14.0 | 7 | 87 | 5 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40042856335639954 | 0.0 | 0.0 | +b250e22d-7193-4ea5-879d-5c7b41145719 / -— |
| Jogador 6 | 5-3 | 287 | REROLL | ALL_IN | 14.0 | 7 | 84 | 5 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 288 | SELL | ALL_IN | 14.0 | 7 | 82 | 5 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042399998754262924 | 0.0 | 0.0 | +— / -af404167-469a-447e-b415-dcb52033ef9b |
| Jogador 6 | 5-3 | 289 | BUY | ALL_IN | 14.0 | 7 | 86 | 5 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0204542875289917 | 0.0 | 0.0 | +9c3b3b78-e99c-4947-b958-cce156ecccb1 / -— |
| Jogador 6 | 5-3 | 290 | SELL | ALL_IN | 14.0 | 7 | 85 | 5 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6193505525588989 | 0.0 | 0.0 | +— / -3faf4ab2-44b3-4779-985b-658c64791c28 |
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
| Jogador 7 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0483810901641846 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23139899969100952 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004352054558694363 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 32 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005867671221494675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 33 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0368893146514893 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2449742704629898 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007539904909208417 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1995791792869568 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 46 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8279597759246826 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19957666099071503 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24525947868824005 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 57 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30117878317832947 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 58 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475671291351318 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1544657051563263 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 65 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17889785766601562 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04722195118665695 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 68 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-2 | 69 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11031114310026169 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 70 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15399228036403656 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 72 | BUY | STABILIZE | 94.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475437641143799 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 73 | BUY | STABILIZE | 94.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6456554532051086 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 6 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17264145612716675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 75 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09768490493297577 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 76 | SELL | STABILIZE | 94.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6188852787017822 | 0.0 | 0.0 | +— / -3394d5fc-ee48-4a08-8669-05984c804b53 |
| Jogador 7 | 2-3 | 77 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1420535445213318 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 78 | BUY_XP | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 79 | PASS | STABILIZE | 94.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 82 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3149080276489258 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 83 | BUY | STABILIZE | 94.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25719553232192993 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 84 | PASS | STABILIZE | 94.0 | 5 | 1 | 0 | 16.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 92 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2889767587184906 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 93 | BUY | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.314052939414978 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 94 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005171899683773518 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 95 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0160977803170681 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 96 | PASS | STABILIZE | 94.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 102 | BUY | STABILIZE | 94.0 | 5 | 9 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9129268527030945 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 7 | 2-6 | 103 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8861379027366638 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 104 | BUY_XP | STABILIZE | 94.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 105 | SELL | STABILIZE | 94.0 | 5 | 1 | 0 | 22.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00286666676402092 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-6 | 106 | SELL | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48007455468177795 | 0.0 | 0.0 | +— / -dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 7 | 2-6 | 107 | BUY_XP | STABILIZE | 94.0 | 5 | 4 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0022987904958426952 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 109 | SELL | STABILIZE | 94.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06310796737670898 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 2-6 | 110 | SELL | STABILIZE | 94.0 | 5 | 1 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4826222360134125 | 0.0 | 0.0 | +— / -caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 7 | 2-7 | 112 | BUY | STABILIZE | 94.0 | 5 | 9 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.267196387052536 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 113 | BUY_XP | STABILIZE | 94.0 | 5 | 6 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03353499993681908 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46113550662994385 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015011870302259922 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01493695005774498 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 117 | PASS | STABILIZE | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 122 | BUY | STABILIZE | 94.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28450947999954224 | 0.0 | 0.0 | +033a84d9-70f6-46a8-a6eb-a2f03be70400 / -— |
| Jogador 7 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15356650948524475 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 124 | BUY_XP | STABILIZE | 94.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0004193209169898182 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014673740603029728 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 127 | PASS | STABILIZE | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 132 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28169578313827515 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -— |
| Jogador 7 | 3-2 | 133 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 134 | PASS | STABILIZE | 84.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 142 | BUY | STABILIZE | 84.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2722036838531494 | 0.0 | 0.0 | +652ff984-c3ac-48d7-9fb6-e95aed0a047d / -— |
| Jogador 7 | 3-3 | 143 | BUY | STABILIZE | 84.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19788485765457153 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 144 | SELL | STABILIZE | 84.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 3-3 | 145 | BUY | STABILIZE | 84.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09154576063156128 | 0.0 | 0.0 | +4d03897d-0113-4a29-a864-75305c142d97 / -— |
| Jogador 7 | 3-3 | 146 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -4d03897d-0113-4a29-a864-75305c142d97 |
| Jogador 7 | 3-3 | 147 | BUY_XP | STABILIZE | 84.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 148 | SELL | STABILIZE | 84.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1289999932050705 | 0.0 | 0.0 | +— / -f116ca4e-dbe8-457e-83a5-958525aa384a |
| Jogador 7 | 3-3 | 149 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00015958370931912214 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 152 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379950523376465 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -4e206e09-40e3-4699-81cb-8aaf01109dea,a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 7 | 3-4 | 153 | BUY | STABILIZE | 84.0 | 6 | 6 | 0 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8312201499938965 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -2c7e844d-925a-43bb-8be8-65a71d11f964,6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09919946640729904 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 155 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1375356763601303 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 156 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010323596186935902 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 157 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -1ff50c59-5133-459e-8bf1-d449c26efabf |
| Jogador 7 | 3-4 | 158 | EQUIP_FROM_INVENTORY | STABILIZE | 84.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08516765385866165 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 159 | EQUIP_FROM_INVENTORY | STABILIZE | 84.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06659651547670364 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 160 | BUY_XP | STABILIZE | 84.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 162 | BUY | STABILIZE | 84.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.769496500492096 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 7 | 3-5 | 163 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21083655953407288 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 164 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02827499993145466 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 165 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 0 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2002675086259842 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014806131832301617 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 168 | PASS | STABILIZE | 84.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 169 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.56974196434021 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 172 | BUY | STABILIZE | 84.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7971920371055603 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 173 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00024124332412611693 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 174 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016383826732635498 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013856018893420696 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 176 | PASS | STABILIZE | 84.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 182 | BUY | STABILIZE | 84.0 | 7 | 10 | 1 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7249711751937866 | 0.0 | 0.0 | +21135c93-ae87-47a0-899c-7eaa0c2c30b8 / -— |
| Jogador 7 | 3-7 | 183 | BUY | STABILIZE | 84.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8309869170188904 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -d69fa0dc-74b6-4ee7-90f7-aaca5405c59c,fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 3-7 | 184 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 4 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5792394876480103 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017585063353180885 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0115539925172925 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 187 | PASS | STABILIZE | 84.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 192 | BUY | STABILIZE | 84.0 | 7 | 10 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.08452071249485016 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 7 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09724638611078262 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.0780925527215004 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 195 | BUY | STABILIZE | 84.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22373920679092407 | 0.0 | 0.0 | +6a30a366-c631-429d-9523-af769cdf48a4 / -— |
| Jogador 7 | 4-1 | 196 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00048300501657649875 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 197 | BUY_XP | STABILIZE | 84.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.5196304957498796e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015112956054508686 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0195732731372118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 202 | BUY | STABILIZE | 84.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27484890818595886 | 0.0 | 0.0 | +08a36d54-bb5c-48a6-afb1-e0f9943bf069 / -— |
| Jogador 7 | 4-2 | 203 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008890945464372635 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 204 | BUY_XP | STABILIZE | 84.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 205 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014214289374649525 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014927150681614876 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999018050730228 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 208 | PASS | STABILIZE | 84.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 212 | SELL | STABILIZE | 84.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5740000009536743 | 0.0 | 0.0 | +— / -cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 4-3 | 213 | EQUIP_FROM_INVENTORY | STABILIZE | 84.0 | 7 | 19 | 1 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08449430763721466 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 214 | BUY | STABILIZE | 84.0 | 7 | 19 | 1 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14308124780654907 | 0.0 | 0.0 | +a7893c5d-2faa-4292-9240-f3cc5813151e / -— |
| Jogador 7 | 4-3 | 215 | BUY_XP | STABILIZE | 84.0 | 7 | 15 | 1 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017271999269723892 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 216 | BUY_XP | STABILIZE | 84.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 217 | BUY_XP | STABILIZE | 84.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 218 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 219 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01497677993029356 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 220 | PASS | STABILIZE | 84.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 222 | SELL | STABILIZE | 84.0 | 7 | 12 | 1 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4880000054836273 | 0.0 | 0.0 | +— / -8a52858d-da47-4de9-8e91-8612788cb8fd |
| Jogador 7 | 4-4 | 223 | BUY | STABILIZE | 84.0 | 7 | 23 | 2 | 30.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8216232061386108 | 0.0 | 0.0 | +e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 / -— |
| Jogador 7 | 4-4 | 224 | SELL | STABILIZE | 84.0 | 7 | 20 | 2 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -6a30a366-c631-429d-9523-af769cdf48a4 |
| Jogador 7 | 4-4 | 225 | BUY | STABILIZE | 84.0 | 7 | 23 | 2 | 30.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7811113595962524 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 7 | 4-4 | 226 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 20 | 2 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.043084234377602e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 227 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 20 | 2 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000204555690289 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 228 | PASS | STABILIZE | 84.0 | 7 | 20 | 2 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02857142873108387 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 232 | SELL | STABILIZE | 84.0 | 7 | 30 | 3 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04139738902449608 | 0.0 | 0.0 | +— / -97d52b06-365b-44ad-b4f9-63e0f9503c8a |
| Jogador 7 | 4-5 | 233 | BUY | STABILIZE | 84.0 | 7 | 33 | 3 | 30.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0037114396691322327 | 0.0 | 0.0 | +241a8a03-6e6f-4a9a-8550-e9154f3e1e76 / -— |
| Jogador 7 | 4-5 | 234 | SELL | STABILIZE | 84.0 | 7 | 29 | 2 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03449999913573265 | 0.0 | 0.0 | +— / -f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 4-5 | 235 | BUY | STABILIZE | 84.0 | 7 | 32 | 3 | 30.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16760262846946716 | 0.0 | 0.0 | +c65dacb1-5745-49d1-b7d4-e45d8e24aa84 / -— |
| Jogador 7 | 4-5 | 236 | SELL | STABILIZE | 84.0 | 7 | 30 | 3 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04496827349066734 | 0.0 | 0.0 | +— / -c65dacb1-5745-49d1-b7d4-e45d8e24aa84 |
| Jogador 7 | 4-5 | 237 | BUY | STABILIZE | 84.0 | 7 | 32 | 3 | 30.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16764593124389648 | 0.0 | 0.0 | +7e0d7932-1b83-4918-9292-6e60957e6022 / -— |
| Jogador 7 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 30 | 3 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.519367237458937e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 30 | 3 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015006028115749359 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 240 | PASS | STABILIZE | 84.0 | 7 | 30 | 3 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0357142873108387 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 242 | SELL | STABILIZE | 84.0 | 7 | 42 | 4 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04640429839491844 | 0.0 | 0.0 | +— / -7e0d7932-1b83-4918-9292-6e60957e6022 |
| Jogador 7 | 4-6 | 243 | BUY | STABILIZE | 84.0 | 7 | 44 | 4 | 30.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08948204666376114 | 0.0 | 0.0 | +3c59d736-011d-480c-a9af-1df7a3b4caab / -— |
| Jogador 7 | 4-6 | 244 | SELL | STABILIZE | 84.0 | 7 | 41 | 4 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -3c59d736-011d-480c-a9af-1df7a3b4caab |
| Jogador 7 | 4-6 | 245 | BUY | STABILIZE | 84.0 | 7 | 44 | 4 | 30.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06117831543087959 | 0.0 | 0.0 | +aaebedb3-18bf-4ae6-948e-7b326b573f1c / -— |
| Jogador 7 | 4-6 | 246 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 43 | 4 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.6879135475610383e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 247 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 43 | 4 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015009273774921894 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 248 | PASS | STABILIZE | 84.0 | 7 | 43 | 4 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 252 | SELL | STABILIZE | 84.0 | 7 | 56 | 5 | 30.0 | Colosso/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026974445208907127 | 0.0 | 0.0 | +— / -aaebedb3-18bf-4ae6-948e-7b326b573f1c |
| Jogador 7 | 4-7 | 253 | BUY | STABILIZE | 84.0 | 7 | 57 | 5 | 30.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9634782671928406 | 0.0 | 0.0 | +2f75fcd7-1405-49fd-8a0c-649c1f8a9f09 / -0cf5c315-d2f3-4854-a95b-07912b83ea81,5b96c8f7-bacb-47df-8666-30d30d49549d |
| Jogador 7 | 4-7 | 254 | BUY | STABILIZE | 84.0 | 7 | 54 | 5 | 24.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9623502492904663 | 0.0 | 0.0 | +a492f78e-91f0-48cb-891a-6518551da328 / -033a84d9-70f6-46a8-a6eb-a2f03be70400,21135c93-ae87-47a0-899c-7eaa0c2c30b8 |
| Jogador 7 | 4-7 | 255 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 52 | 5 | 16.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3370100259780884 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 256 | BUY | STABILIZE | 84.0 | 7 | 52 | 5 | 24.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14979039132595062 | 0.0 | 0.0 | +8d75ef64-e2c3-47b6-a336-c9e5867158e5 / -— |
| Jogador 7 | 4-7 | 257 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 48 | 4 | 24.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32316067814826965 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 258 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 48 | 4 | 26.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 259 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 48 | 4 | 26.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015057987533509731 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 260 | PASS | STABILIZE | 84.0 | 7 | 48 | 4 | 26.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18857142329216003 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 262 | BUY | STABILIZE | 84.0 | 7 | 60 | 5 | 34.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04676458239555359 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -— |
| Jogador 7 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 7 | 55 | 5 | 34.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14090357720851898 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 7 | 55 | 5 | 34.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14978758990764618 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 265 | BUY | STABILIZE | 84.0 | 7 | 55 | 5 | 34.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04097292199730873 | 0.0 | 0.0 | +ad363fca-33b7-4257-99d6-7093df66caf6 / -— |
| Jogador 7 | 5-1 | 266 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 52 | 5 | 34.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 267 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 52 | 5 | 34.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015029638074338436 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 268 | PASS | STABILIZE | 84.0 | 7 | 52 | 5 | 34.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08911579847335815 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 272 | SELL | STABILIZE | 71.0 | 7 | 62 | 5 | 34.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -2f75fcd7-1405-49fd-8a0c-649c1f8a9f09 |
| Jogador 7 | 5-2 | 273 | BUY | STABILIZE | 71.0 | 7 | 70 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.5058412551879883 | 0.0 | 0.0 | +6fb5e8f1-2656-486b-9478-161c1b430d5f / -— |
| Jogador 7 | 5-2 | 274 | EQUIP_FROM_INVENTORY | STABILIZE | 71.0 | 7 | 67 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09764814376831055 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 275 | EQUIP_FROM_INVENTORY | STABILIZE | 71.0 | 7 | 67 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15354543924331665 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 276 | SELL | STABILIZE | 71.0 | 7 | 67 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -8d75ef64-e2c3-47b6-a336-c9e5867158e5 |
| Jogador 7 | 5-2 | 277 | BUY | STABILIZE | 71.0 | 7 | 71 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022921131923794746 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -— |
| Jogador 7 | 5-2 | 278 | MOVE_BOARD | STABILIZE | 71.0 | 7 | 68 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00028380751609802246 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 279 | SELL | STABILIZE | 71.0 | 7 | 68 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 |
| Jogador 7 | 5-2 | 280 | BUY | STABILIZE | 71.0 | 7 | 71 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01855810172855854 | 0.0 | 0.0 | +8da82a9e-0746-43e1-81c3-fa22ec3bb863 / -— |
| Jogador 7 | 5-3 | 282 | SELL | STABILIZE | 71.0 | 7 | 80 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029879465699195862 | 0.0 | 0.0 | +— / -8da82a9e-0746-43e1-81c3-fa22ec3bb863 |
| Jogador 7 | 5-3 | 283 | BUY | STABILIZE | 71.0 | 7 | 82 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2159281224012375 | 0.0 | 0.0 | +85fb6db6-e1b0-4fa1-b99a-2f205305ef0b / -— |
| Jogador 7 | 5-3 | 284 | SELL | STABILIZE | 71.0 | 7 | 79 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -85fb6db6-e1b0-4fa1-b99a-2f205305ef0b |
| Jogador 7 | 5-3 | 285 | BUY | STABILIZE | 71.0 | 7 | 82 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017259914427995682 | 0.0 | 0.0 | +864f332a-0446-4995-b7fb-76d48d293501 / -— |
| Jogador 7 | 5-3 | 286 | SELL | STABILIZE | 71.0 | 7 | 81 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -864f332a-0446-4995-b7fb-76d48d293501 |
| Jogador 7 | 5-3 | 287 | BUY | STABILIZE | 71.0 | 7 | 82 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2410917431116104 | 0.0 | 0.0 | +1bf15a91-4832-4245-9b48-382a27410263 / -— |
| Jogador 7 | 5-3 | 288 | SELL | STABILIZE | 71.0 | 7 | 80 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -1bf15a91-4832-4245-9b48-382a27410263 |
| Jogador 7 | 5-3 | 289 | BUY | STABILIZE | 71.0 | 7 | 82 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24109172821044922 | 0.0 | 0.0 | +9f1c634e-13c7-4b59-838c-4b676fa059be / -— |
| Jogador 7 | 5-3 | 290 | MOVE_BOARD | STABILIZE | 71.0 | 7 | 80 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 292 | SELL | STABILIZE | 55.0 | 7 | 90 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -9f1c634e-13c7-4b59-838c-4b676fa059be |
| Jogador 7 | 5-4 | 293 | BUY | STABILIZE | 55.0 | 7 | 92 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06463904678821564 | 0.0 | 0.0 | +e89905aa-6564-4e15-bc3a-c281646446bc / -— |
| Jogador 7 | 5-4 | 294 | SELL | STABILIZE | 55.0 | 7 | 89 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -e89905aa-6564-4e15-bc3a-c281646446bc |
| Jogador 7 | 5-4 | 295 | BUY | STABILIZE | 55.0 | 7 | 92 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04123122617602348 | 0.0 | 0.0 | +920ec426-49cf-489f-aad8-3f5461b93be6 / -— |
| Jogador 7 | 5-4 | 296 | SELL | STABILIZE | 55.0 | 7 | 88 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03678521141409874 | 0.0 | 0.0 | +— / -920ec426-49cf-489f-aad8-3f5461b93be6 |
| Jogador 7 | 5-4 | 297 | BUY | STABILIZE | 55.0 | 7 | 92 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11897347122430801 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -— |
| Jogador 7 | 5-4 | 298 | MOVE_BOARD | STABILIZE | 55.0 | 7 | 90 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 299 | MOVE_BOARD | STABILIZE | 55.0 | 7 | 90 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 300 | PASS | STABILIZE | 55.0 | 7 | 90 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11811063438653946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 302 | SELL | STABILIZE | 55.0 | 7 | 100 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -4261ad99-2607-4d90-978c-9e9abffd6d95 |
| Jogador 7 | 5-5 | 303 | BUY | STABILIZE | 55.0 | 7 | 102 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9255668520927429 | 0.0 | 0.0 | +2ac6d717-87f1-4421-929e-1934a9317e72 / -— |
| Jogador 7 | 5-5 | 304 | SELL | STABILIZE | 55.0 | 7 | 99 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45723333954811096 | 0.0 | 0.0 | +— / -6fb5e8f1-2656-486b-9478-161c1b430d5f |
| Jogador 7 | 5-5 | 305 | BUY | STABILIZE | 55.0 | 7 | 102 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06346847862005234 | 0.0 | 0.0 | +ae9da355-52b7-402c-be6e-41fa1148a550 / -— |
| Jogador 7 | 5-5 | 306 | SELL | STABILIZE | 55.0 | 7 | 99 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -ad363fca-33b7-4257-99d6-7093df66caf6 |
| Jogador 7 | 5-5 | 307 | BUY | STABILIZE | 55.0 | 7 | 102 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12633618712425232 | 0.0 | 0.0 | +a810e10d-e7ef-4ece-8fb2-8b6471b557ec / -— |
| Jogador 7 | 5-5 | 308 | SELL | STABILIZE | 55.0 | 7 | 100 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036796338856220245 | 0.0 | 0.0 | +— / -a810e10d-e7ef-4ece-8fb2-8b6471b557ec |
| Jogador 7 | 5-5 | 309 | BUY | STABILIZE | 55.0 | 7 | 102 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19161848723888397 | 0.0 | 0.0 | +3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 / -— |
| Jogador 7 | 5-5 | 310 | MOVE_BOARD | STABILIZE | 55.0 | 7 | 101 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002759473631158471 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 312 | SELL | STABILIZE | 40.0 | 7 | 112 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 |
| Jogador 7 | 5-6 | 313 | BUY | STABILIZE | 40.0 | 7 | 113 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12527380883693695 | 0.0 | 0.0 | +9f271ee0-c506-40b7-b3f3-bac209974ba2 / -— |
| Jogador 7 | 5-6 | 314 | SELL | STABILIZE | 40.0 | 7 | 111 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.051511988043785095 | 0.0 | 0.0 | +— / -9f271ee0-c506-40b7-b3f3-bac209974ba2 |
| Jogador 7 | 5-6 | 315 | BUY | STABILIZE | 40.0 | 7 | 113 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039845213294029236 | 0.0 | 0.0 | +8c4772c9-83f1-4021-b83f-a9ff1773bea0 / -— |
| Jogador 7 | 5-6 | 316 | SELL | STABILIZE | 40.0 | 7 | 110 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -8c4772c9-83f1-4021-b83f-a9ff1773bea0 |
| Jogador 7 | 5-6 | 317 | BUY | STABILIZE | 40.0 | 7 | 113 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02924502082169056 | 0.0 | 0.0 | +87902519-e44a-4d4c-9956-ac5aedc9b0c6 / -— |
| Jogador 7 | 5-6 | 318 | SELL | STABILIZE | 40.0 | 7 | 110 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033311959356069565 | 0.0 | 0.0 | +— / -87902519-e44a-4d4c-9956-ac5aedc9b0c6 |
| Jogador 7 | 5-6 | 319 | BUY | STABILIZE | 40.0 | 7 | 113 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04070277139544487 | 0.0 | 0.0 | +de590b22-a48c-4c78-a2f3-6ef39ce948fe / -— |
| Jogador 7 | 5-6 | 320 | REROLL | STABILIZE | 40.0 | 7 | 111 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 322 | SELL | STABILIZE | 27.0 | 7 | 120 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -ae9da355-52b7-402c-be6e-41fa1148a550 |
| Jogador 7 | 5-7 | 323 | BUY | STABILIZE | 27.0 | 7 | 123 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.848419725894928 | 0.0 | 0.0 | +88eb7a9e-aada-4146-adaf-4d3e8a5bdd67 / -— |
| Jogador 7 | 5-7 | 324 | SELL | STABILIZE | 27.0 | 7 | 121 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5925999879837036 | 0.0 | 0.0 | +— / -08a36d54-bb5c-48a6-afb1-e0f9943bf069 |
| Jogador 7 | 5-7 | 325 | BUY | STABILIZE | 27.0 | 7 | 123 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.644654393196106 | 0.0 | 0.0 | +d1f4a2a4-f3cb-413d-8ed8-b373fa56f1f2 / -— |
| Jogador 7 | 5-7 | 326 | SELL | STABILIZE | 27.0 | 7 | 119 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4919150769710541 | 0.0 | 0.0 | +— / -d1f4a2a4-f3cb-413d-8ed8-b373fa56f1f2 |
| Jogador 7 | 5-7 | 327 | BUY | STABILIZE | 27.0 | 7 | 123 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11552153527736664 | 0.0 | 0.0 | +2328111b-018a-4ca1-a9e7-f7cd9627fd43 / -— |
| Jogador 7 | 5-7 | 328 | SELL | STABILIZE | 27.0 | 7 | 121 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050200000405311584 | 0.0 | 0.0 | +— / -2328111b-018a-4ca1-a9e7-f7cd9627fd43 |
| Jogador 7 | 5-7 | 329 | BUY | STABILIZE | 27.0 | 7 | 123 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036349255591630936 | 0.0 | 0.0 | +6875f839-cf68-443f-9776-887087b375d3 / -— |
| Jogador 7 | 5-7 | 330 | REROLL | STABILIZE | 27.0 | 7 | 120 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 332 | EQUIP_FROM_INVENTORY | STABILIZE | 27.0 | 7 | 129 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13823729753494263 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 333 | SELL | STABILIZE | 27.0 | 7 | 129 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -6875f839-cf68-443f-9776-887087b375d3 |
| Jogador 7 | 6-1 | 334 | BUY | STABILIZE | 27.0 | 7 | 132 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0833474397659302 | 0.0 | 0.0 | +c3596d89-03d2-4fc7-afaf-591f10423252 / -599caeca-96ef-4308-b6cd-f65b005879e2,e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 |
| Jogador 7 | 6-1 | 335 | BUY | STABILIZE | 27.0 | 7 | 129 | 5 | 28.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18988576531410217 | 0.0 | 0.0 | +7fd34ef6-a124-4d23-a166-9f7ad919c826 / -— |
| Jogador 7 | 6-1 | 336 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 126 | 5 | 28.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5193599462509155 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 337 | BUY | STABILIZE | 27.0 | 7 | 126 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09231723845005035 | 0.0 | 0.0 | +f5a067a8-3eba-4efb-a5cf-76571eb8516e / -— |
| Jogador 7 | 6-1 | 338 | SELL | STABILIZE | 27.0 | 7 | 123 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -c3596d89-03d2-4fc7-afaf-591f10423252 |
| Jogador 7 | 6-1 | 339 | BUY | STABILIZE | 27.0 | 7 | 131 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2441786229610443 | 0.0 | 0.0 | +24d03668-5dc4-4b40-9439-a1d67522d0a3 / -— |
| Jogador 7 | 6-1 | 340 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 129 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 342 | SELL | ALL_IN | 12.0 | 8 | 140 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -24d03668-5dc4-4b40-9439-a1d67522d0a3 |
| Jogador 7 | 6-2 | 343 | BUY | ALL_IN | 12.0 | 8 | 142 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21324840188026428 | 0.0 | 0.0 | +e99948bb-f38f-41e0-b1c4-1864c35ffe14 / -— |
| Jogador 7 | 6-2 | 344 | SELL | ALL_IN | 12.0 | 8 | 140 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.051540326327085495 | 0.0 | 0.0 | +— / -e99948bb-f38f-41e0-b1c4-1864c35ffe14 |
| Jogador 7 | 6-2 | 345 | BUY | ALL_IN | 12.0 | 8 | 142 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14267827570438385 | 0.0 | 0.0 | +f7f1b5db-dae6-4b1c-9a1f-94fefd1cf248 / -— |
| Jogador 7 | 6-2 | 346 | SELL | ALL_IN | 12.0 | 8 | 138 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03332245722413063 | 0.0 | 0.0 | +— / -f5a067a8-3eba-4efb-a5cf-76571eb8516e |
| Jogador 7 | 6-2 | 347 | BUY | ALL_IN | 12.0 | 8 | 141 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.031845126301050186 | 0.0 | 0.0 | +280265b0-7892-4e7e-b654-e2cc7b0ea97b / -— |
| Jogador 7 | 6-2 | 348 | SELL | ALL_IN | 12.0 | 8 | 137 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -280265b0-7892-4e7e-b654-e2cc7b0ea97b |
| Jogador 7 | 6-2 | 349 | BUY | ALL_IN | 12.0 | 8 | 141 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04149233549833298 | 0.0 | 0.0 | +115ae76a-bc1f-49a4-948e-9ced3d8258b7 / -— |
| Jogador 7 | 6-2 | 350 | SELL | ALL_IN | 12.0 | 8 | 139 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029843544587492943 | 0.0 | 0.0 | +— / -115ae76a-bc1f-49a4-948e-9ced3d8258b7 |
| Jogador 7 | 6-3 | 352 | BUY | ALL_IN | 12.0 | 8 | 152 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4636830687522888 | 0.0 | 0.0 | +19e8f3ef-c3a6-459e-bf05-a53f742ba05d / -— |
| Jogador 7 | 6-3 | 353 | SELL | ALL_IN | 12.0 | 8 | 149 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -7fd34ef6-a124-4d23-a166-9f7ad919c826 |
| Jogador 7 | 6-3 | 354 | BUY | ALL_IN | 12.0 | 8 | 152 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4344101548194885 | 0.0 | 0.0 | +3e1e33ef-4948-4ff2-bfb9-db16af507dd9 / -— |
| Jogador 7 | 6-3 | 355 | SELL | ALL_IN | 12.0 | 8 | 150 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -f7f1b5db-dae6-4b1c-9a1f-94fefd1cf248 |
| Jogador 7 | 6-3 | 356 | BUY | ALL_IN | 12.0 | 8 | 154 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12606112658977509 | 0.0 | 0.0 | +ac0e7aab-09c1-4762-8c74-09fedabcd769 / -— |
| Jogador 7 | 6-3 | 357 | SELL | ALL_IN | 12.0 | 8 | 151 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03330202028155327 | 0.0 | 0.0 | +— / -ac0e7aab-09c1-4762-8c74-09fedabcd769 |
| Jogador 7 | 6-3 | 358 | BUY | ALL_IN | 12.0 | 8 | 154 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0572875514626503 | 0.0 | 0.0 | +6fe382fd-86c3-42ec-abb7-fb52c7a19c62 / -— |
| Jogador 7 | 6-3 | 359 | SELL | ALL_IN | 12.0 | 8 | 150 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -6fe382fd-86c3-42ec-abb7-fb52c7a19c62 |
| Jogador 7 | 6-3 | 360 | BUY | ALL_IN | 12.0 | 8 | 154 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05218100920319557 | 0.0 | 0.0 | +699b59c7-1237-472b-a4d1-18a35e88b7c2 / -— |
| Jogador 7 | 6-4 | 362 | SELL | ALL_IN | 12.0 | 8 | 164 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01133333332836628 | 0.0 | 0.0 | +— / -699b59c7-1237-472b-a4d1-18a35e88b7c2 |
| Jogador 7 | 6-4 | 363 | BUY | ALL_IN | 12.0 | 8 | 165 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9836829304695129 | 0.0 | 0.0 | +e15f057a-185e-4f99-8417-2c2b059912af / -— |
| Jogador 7 | 6-4 | 364 | SELL | ALL_IN | 12.0 | 8 | 162 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6524222493171692 | 0.0 | 0.0 | +— / -3e1e33ef-4948-4ff2-bfb9-db16af507dd9 |
| Jogador 7 | 6-4 | 365 | BUY | ALL_IN | 12.0 | 8 | 164 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.110414981842041 | 0.0 | 0.0 | +47b7832a-ef8a-436e-9e2e-84a5160ff6d5 / -242805ca-f275-4e04-a2f5-81e0b6680dd1,7159421f-b5ea-4d10-9cc5-59186d62983d |
| Jogador 7 | 6-4 | 366 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 163 | 5 | 30.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.24042849242687225 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 367 | BUY | ALL_IN | 12.0 | 8 | 163 | 5 | 36.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.014392858371138573 | 0.0 | 0.0 | +df0a5d1f-d42d-43eb-b505-cfd00e3dcea8 / -— |
| Jogador 7 | 6-4 | 368 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 8 | 159 | 5 | 36.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13581348955631256 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 369 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 8 | 159 | 5 | 36.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07068030536174774 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 370 | SELL | ALL_IN | 12.0 | 8 | 159 | 5 | 36.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7103000283241272 | 0.0 | 0.0 | +— / -47b7832a-ef8a-436e-9e2e-84a5160ff6d5 |
| Jogador 7 | 6-5 | 372 | BUY | ALL_IN | 12.0 | 8 | 173 | 5 | 36.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.1109851598739624 | 0.0 | 0.0 | +beed40ed-5b69-45eb-a675-b18cf2c9eb69 / -2ac6d717-87f1-4421-929e-1934a9317e72,daa7f698-2fa2-43d7-ae73-ec616b006db4 |
| Jogador 7 | 6-5 | 373 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 170 | 5 | 30.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.747831404209137 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 374 | BUY | ALL_IN | 12.0 | 8 | 170 | 5 | 32.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.21845054626464844 | 0.0 | 0.0 | +4f487e34-c67d-489d-a21e-78b5642aefd4 / -— |
| Jogador 7 | 6-5 | 375 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 166 | 5 | 32.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.09804780036211014 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 376 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 166 | 5 | 30.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.014053930528461933 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 377 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 166 | 5 | 30.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.761809229850769 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 378 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 166 | 5 | 32.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.08300432562828064 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 379 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 166 | 5 | 30.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.011906265281140804 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 380 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 166 | 5 | 30.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.15062621235847473 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 382 | BUY | ALL_IN | 12.0 | 8 | 177 | 5 | 40.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7577540278434753 | 0.0 | 0.0 | +3f38fe46-2585-4a0d-8999-ab347f9cd398 / -— |
| Jogador 7 | 6-6 | 383 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 8 | 173 | 5 | 40.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14061933755874634 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 384 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 8 | 173 | 5 | 40.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08452731370925903 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 385 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 8 | 173 | 5 | 40.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.056253112852573395 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 386 | SELL | ALL_IN | 12.0 | 8 | 173 | 5 | 40.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7167999744415283 | 0.0 | 0.0 | +— / -beed40ed-5b69-45eb-a675-b18cf2c9eb69 |
| Jogador 7 | 6-6 | 387 | BUY | ALL_IN | 12.0 | 8 | 181 | 5 | 40.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7695806622505188 | 0.0 | 0.0 | +6559ddb9-ba21-4084-9a25-7c9179a347dd / -— |
| Jogador 7 | 6-6 | 388 | SELL | ALL_IN | 12.0 | 8 | 178 | 5 | 40.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03675707057118416 | 0.0 | 0.0 | +— / -df0a5d1f-d42d-43eb-b505-cfd00e3dcea8 |
| Jogador 7 | 6-6 | 389 | BUY | ALL_IN | 12.0 | 8 | 182 | 5 | 40.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0759509727358818 | 0.0 | 0.0 | +6426604f-2d8c-4300-a2d5-b068448a6eda / -— |
| Jogador 7 | 6-6 | 390 | MOVE_BENCH | ALL_IN | 12.0 | 8 | 178 | 5 | 40.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08561801165342331 | 0.0 | 0.0 | +— / -— |
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
| Jogador 8 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0147674083709717 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36017322540283203 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 30 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28106260299682617 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.976050078868866 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 44 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17337313294410706 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 45 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25139617919921875 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 46 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11593848466873169 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 47 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.114261269569397 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -88a02960-5ebe-4b20-b667-1a8ce2728578,dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20082084834575653 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17914557456970215 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05906843766570091 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1034035682678223 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1241607591509819 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.034071777015924454 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-2 | 62 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25733545422554016 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 63 | BUY | STABILIZE | 94.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21252666413784027 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 64 | BUY | STABILIZE | 94.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18140096962451935 | 0.0 | 0.0 | +ebe77c97-f249-4265-ae03-bc8115a4795f / -— |
| Jogador 8 | 2-2 | 65 | SELL | STABILIZE | 94.0 | 4 | 2 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045099999755620956 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-2 | 66 | BUY | STABILIZE | 94.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058700814843177795 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 0 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1110355481505394 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 68 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 0 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5153083801269531 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 69 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 0 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050088800489902496 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 70 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 0 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15066689252853394 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9806622266769409 | 0.0 | 0.0 | +01f4a73c-7202-4ee3-964e-d32370c3c547 / -— |
| Jogador 8 | 2-3 | 73 | BUY | STABILIZE | 90.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9497133493423462 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -01f4a73c-7202-4ee3-964e-d32370c3c547,64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 2-3 | 74 | BUY | STABILIZE | 90.0 | 4 | 4 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3304692208766937 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 75 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 3 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17664417624473572 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 76 | BUY | STABILIZE | 90.0 | 4 | 3 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26588431000709534 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 77 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 0 | 0 | 14.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43016475439071655 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 0 | 0 | 16.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2268577367067337 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 79 | SELL | STABILIZE | 90.0 | 4 | 0 | 0 | 14.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21799325942993164 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-3 | 80 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 3 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050091151148080826 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 82 | BUY | STABILIZE | 85.0 | 4 | 9 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8834568858146667 | 0.0 | 0.0 | +3644801e-2247-403d-8b81-d2d3f15c2f55 / -— |
| Jogador 8 | 2-4 | 83 | BUY | STABILIZE | 85.0 | 4 | 8 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13914866745471954 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 84 | BUY | STABILIZE | 85.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001591468695551157 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 85 | SELL | STABILIZE | 85.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-4 | 86 | BUY_XP | STABILIZE | 85.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 87 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057459618896245956 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 88 | BUY | STABILIZE | 85.0 | 5 | 2 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17010119557380676 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 8 | 2-4 | 89 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 1 | 0 | 14.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06199973449110985 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 1 | 0 | 14.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029512744396924973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 92 | BUY | STABILIZE | 85.0 | 5 | 7 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8997885584831238 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 93 | SELL | STABILIZE | 85.0 | 5 | 6 | 0 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011366666294634342 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 8 | 2-5 | 94 | BUY | STABILIZE | 85.0 | 5 | 7 | 0 | 14.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6029919385910034 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 95 | SELL | STABILIZE | 85.0 | 5 | 5 | 0 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019166667014360428 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-5 | 96 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 14.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12595923244953156 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 3 | 0 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3666679263114929 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 98 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 3 | 0 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11147920787334442 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 99 | SELL | STABILIZE | 85.0 | 5 | 3 | 0 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011533332988619804 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 2-5 | 100 | BUY | STABILIZE | 85.0 | 5 | 5 | 0 | 14.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10788935422897339 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-6 | 102 | SELL | STABILIZE | 80.0 | 5 | 9 | 0 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06735355406999588 | 0.0 | 0.0 | +— / -c0d8da9e-5ede-4a26-8c5c-e2a908318bfd |
| Jogador 8 | 2-6 | 103 | BUY | STABILIZE | 80.0 | 5 | 11 | 1 | 14.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8972200751304626 | 0.0 | 0.0 | +c737e99a-613e-4f1a-a50e-7a865169f90c / -— |
| Jogador 8 | 2-6 | 104 | SELL | STABILIZE | 80.0 | 5 | 10 | 1 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04312312602996826 | 0.0 | 0.0 | +— / -a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 8 | 2-6 | 105 | BUY | STABILIZE | 80.0 | 5 | 12 | 1 | 14.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05031295865774155 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 106 | SELL | STABILIZE | 80.0 | 5 | 9 | 0 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07176666706800461 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-6 | 107 | BUY | STABILIZE | 80.0 | 5 | 12 | 1 | 14.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02566521055996418 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 108 | MOVE_BENCH | STABILIZE | 80.0 | 5 | 9 | 0 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2941746413707733 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 109 | MOVE_BENCH | STABILIZE | 80.0 | 5 | 9 | 0 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40189066529273987 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 110 | PASS | STABILIZE | 80.0 | 5 | 9 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 112 | SELL | STABILIZE | 75.0 | 5 | 16 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058432985097169876 | 0.0 | 0.0 | +— / -87600495-fe90-4832-ab42-9a5cb0ebe3f4 |
| Jogador 8 | 2-7 | 113 | BUY | STABILIZE | 75.0 | 5 | 19 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08854255080223083 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 114 | SELL | STABILIZE | 75.0 | 5 | 16 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05770526081323624 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 2-7 | 115 | BUY | STABILIZE | 75.0 | 5 | 19 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08842076361179352 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 116 | SELL | STABILIZE | 75.0 | 5 | 18 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05791017413139343 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 2-7 | 117 | BUY | STABILIZE | 75.0 | 5 | 19 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03518353030085564 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 118 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 16 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39760294556617737 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 119 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 16 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0722336694598198 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 120 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 16 | 1 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41288191080093384 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 75.0 | 5 | 24 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1995876133441925 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 123 | SELL | STABILIZE | 75.0 | 5 | 24 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3212941586971283 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 3-1 | 124 | BUY | STABILIZE | 75.0 | 5 | 27 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05420559272170067 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 23 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0634109228849411 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 126 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 23 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07741683721542358 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 127 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 23 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4129121005535126 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 128 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 23 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07036514580249786 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 129 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 23 | 2 | 14.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4124232828617096 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 130 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 23 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7560194134712219 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 132 | SELL | STABILIZE | 75.0 | 5 | 31 | 3 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc |
| Jogador 8 | 3-2 | 133 | BUY | STABILIZE | 75.0 | 5 | 34 | 3 | 16.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1973361074924469 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 134 | SELL | STABILIZE | 75.0 | 5 | 33 | 3 | 16.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038233332335948944 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-2 | 135 | BUY | STABILIZE | 75.0 | 5 | 34 | 3 | 16.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057555846869945526 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 136 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 30 | 3 | 16.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.702987015247345 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 137 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 30 | 3 | 18.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0011677861912176013 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 138 | PASS | STABILIZE | 75.0 | 5 | 30 | 3 | 16.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 142 | MOVE_BENCH | STABILIZE | 66.0 | 5 | 38 | 3 | 16.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18898043036460876 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 143 | SELL | STABILIZE | 66.0 | 5 | 38 | 3 | 16.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09959576278924942 | 0.0 | 0.0 | +— / -4ac49c80-f0c3-47ae-a031-96928d244e13 |
| Jogador 8 | 3-3 | 144 | BUY | STABILIZE | 66.0 | 5 | 42 | 4 | 16.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26285839080810547 | 0.0 | 0.0 | +1af578c1-57cf-4752-93e7-d0eebc6e8ae5 / -— |
| Jogador 8 | 3-3 | 145 | SELL | STABILIZE | 66.0 | 5 | 40 | 4 | 16.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07608573883771896 | 0.0 | 0.0 | +— / -1af578c1-57cf-4752-93e7-d0eebc6e8ae5 |
| Jogador 8 | 3-3 | 146 | BUY | STABILIZE | 66.0 | 5 | 42 | 4 | 16.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19533932209014893 | 0.0 | 0.0 | +3bf8af53-85e7-4e5b-8cf8-b7198a955e8d / -— |
| Jogador 8 | 3-3 | 147 | SELL | STABILIZE | 66.0 | 5 | 41 | 4 | 16.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038233332335948944 | 0.0 | 0.0 | +— / -3bf8af53-85e7-4e5b-8cf8-b7198a955e8d |
| Jogador 8 | 3-3 | 148 | BUY | STABILIZE | 66.0 | 5 | 42 | 4 | 16.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2581031620502472 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 149 | MOVE_BENCH | STABILIZE | 66.0 | 5 | 39 | 3 | 16.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6283807158470154 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 150 | MOVE_BENCH | STABILIZE | 66.0 | 5 | 39 | 3 | 18.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015971533954143524 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 152 | SELL | STABILIZE | 56.0 | 5 | 48 | 4 | 16.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08579999953508377 | 0.0 | 0.0 | +— / -e4605ac7-0b51-4f1c-a658-f7d25f9a9dae |
| Jogador 8 | 3-4 | 153 | BUY | STABILIZE | 56.0 | 5 | 51 | 5 | 16.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9012086987495422 | 0.0 | 0.0 | +eb7e36f0-cef9-4a2e-979a-f8a357da73e8 / -5de56114-806a-4f58-8241-b3b8434a2154,b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 3-4 | 154 | BUY | STABILIZE | 56.0 | 5 | 50 | 5 | 16.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.81242835521698 | 0.0 | 0.0 | +e8355df5-8ee7-44a3-ab88-3708c14fd5dc / -3644801e-2247-403d-8b81-d2d3f15c2f55,ebe77c97-f249-4265-ae03-bc8115a4795f |
| Jogador 8 | 3-4 | 155 | MOVE_BENCH | STABILIZE | 56.0 | 5 | 49 | 4 | 12.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19575577974319458 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 156 | MOVE_BENCH | STABILIZE | 56.0 | 5 | 49 | 4 | 12.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7783112525939941 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 157 | PASS | STABILIZE | 56.0 | 5 | 49 | 4 | 14.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13249999284744263 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 162 | BUY | STABILIZE | 56.0 | 5 | 59 | 5 | 18.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8498380780220032 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 8 | 3-5 | 163 | MOVE_BENCH | STABILIZE | 56.0 | 5 | 56 | 5 | 18.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1382439136505127 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 56.0 | 5 | 56 | 5 | 16.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.215140238404274 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 165 | PASS | STABILIZE | 56.0 | 5 | 56 | 5 | 16.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15637752413749695 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 169 | MOVE_BENCH | STABILIZE | 56.0 | 5 | 56 | 5 | 16.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5758641958236694 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 172 | BUY | STABILIZE | 44.0 | 5 | 67 | 5 | 22.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8999499678611755 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,c737e99a-613e-4f1a-a50e-7a865169f90c |
| Jogador 8 | 3-6 | 173 | MOVE_BENCH | STABILIZE | 44.0 | 5 | 66 | 5 | 20.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37043118476867676 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 174 | MOVE_BENCH | STABILIZE | 44.0 | 5 | 66 | 5 | 22.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3627150356769562 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 175 | MOVE_BENCH | STABILIZE | 44.0 | 5 | 66 | 5 | 20.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24096447229385376 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 176 | MOVE_BENCH | STABILIZE | 44.0 | 5 | 66 | 5 | 20.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41383230686187744 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 177 | PASS | STABILIZE | 44.0 | 5 | 66 | 5 | 22.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1631338894367218 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 182 | BUY | STABILIZE | 44.0 | 6 | 77 | 5 | 26.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.135125532746315 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 183 | BUY | STABILIZE | 44.0 | 6 | 74 | 5 | 26.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05333127826452255 | 0.0 | 0.0 | +3625f791-4c9f-4b95-bdf7-4a322dcd55d3 / -— |
| Jogador 8 | 3-7 | 184 | MOVE_BENCH | STABILIZE | 44.0 | 6 | 72 | 5 | 26.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2566274404525757 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 185 | MOVE_BENCH | STABILIZE | 44.0 | 6 | 72 | 5 | 24.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22050945460796356 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 186 | MOVE_BENCH | STABILIZE | 44.0 | 6 | 72 | 5 | 24.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8421215415000916 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 187 | PASS | STABILIZE | 44.0 | 6 | 72 | 5 | 26.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16640359163284302 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 192 | BUY | STABILIZE | 44.0 | 6 | 82 | 5 | 32.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9602756500244141 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -35e1a0f6-207d-4df2-b096-fc07962d094a,a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 4-1 | 193 | BUY | STABILIZE | 44.0 | 6 | 80 | 5 | 28.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3781667649745941 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -— |
| Jogador 8 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 44.0 | 6 | 79 | 5 | 28.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1784396469593048 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 195 | CRAFT_AND_EQUIP | STABILIZE | 44.0 | 6 | 79 | 5 | 28.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1315956711769104 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 196 | BUY | STABILIZE | 44.0 | 6 | 79 | 5 | 28.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12130340933799744 | 0.0 | 0.0 | +b2a77bec-e150-4d98-847c-9f2cfb50cbe7 / -— |
| Jogador 8 | 4-1 | 197 | MOVE_BENCH | STABILIZE | 44.0 | 6 | 78 | 5 | 28.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24025483429431915 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 198 | MOVE_BENCH | STABILIZE | 44.0 | 6 | 78 | 5 | 26.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15787802636623383 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 199 | MOVE_BENCH | STABILIZE | 44.0 | 6 | 78 | 5 | 26.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.526256263256073 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 200 | PASS | STABILIZE | 44.0 | 6 | 78 | 5 | 28.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10250770300626755 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 202 | BUY | FAST8 | 44.0 | 6 | 90 | 5 | 36.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4681374132633209 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -— |
| Jogador 8 | 4-2 | 203 | SELL | FAST8 | 44.0 | 6 | 87 | 5 | 36.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5099574327468872 | 0.0 | 0.0 | +— / -e8355df5-8ee7-44a3-ab88-3708c14fd5dc |
| Jogador 8 | 4-2 | 204 | BUY | FAST8 | 44.0 | 6 | 90 | 5 | 36.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2813762426376343 | 0.0 | 0.0 | +ea460790-b046-451d-9174-8b613e476241 / -— |
| Jogador 8 | 4-2 | 205 | MOVE_BOARD | FAST8 | 44.0 | 6 | 89 | 5 | 36.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10630274564027786 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 206 | SELL | FAST8 | 44.0 | 6 | 89 | 5 | 36.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -eb7e36f0-cef9-4a2e-979a-f8a357da73e8 |
| Jogador 8 | 4-2 | 207 | BUY | FAST8 | 44.0 | 6 | 92 | 5 | 36.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030785424634814262 | 0.0 | 0.0 | +ba7f039a-929c-4537-9eb6-f1dc4563cca8 / -— |
| Jogador 8 | 4-2 | 208 | MOVE_BOARD | FAST8 | 44.0 | 6 | 88 | 5 | 36.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09596934169530869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 209 | MOVE_BOARD | FAST8 | 44.0 | 6 | 88 | 5 | 36.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08723800629377365 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 210 | MOVE_BENCH | FAST8 | 44.0 | 6 | 88 | 5 | 36.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27167370915412903 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 212 | SELL | FAST8 | 44.0 | 6 | 100 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00830487534403801 | 0.0 | 0.0 | +— / -b2a77bec-e150-4d98-847c-9f2cfb50cbe7 |
| Jogador 8 | 4-3 | 213 | BUY | FAST8 | 44.0 | 6 | 101 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31160402297973633 | 0.0 | 0.0 | +7dfeef88-7e1d-43b8-b012-017278ec61dc / -— |
| Jogador 8 | 4-3 | 214 | SELL | FAST8 | 44.0 | 6 | 98 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015179852023720741 | 0.0 | 0.0 | +— / -3625f791-4c9f-4b95-bdf7-4a322dcd55d3 |
| Jogador 8 | 4-3 | 215 | BUY | FAST8 | 44.0 | 6 | 100 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2856297791004181 | 0.0 | 0.0 | +696f53ae-1413-47cc-b491-9870b7bcba51 / -— |
| Jogador 8 | 4-3 | 216 | SELL | FAST8 | 44.0 | 6 | 98 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -4d995451-2e5c-43c2-93f0-22e074e35ab2 |
| Jogador 8 | 4-3 | 217 | BUY | FAST8 | 44.0 | 6 | 102 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10456391423940659 | 0.0 | 0.0 | +e1867f53-f97a-4c7a-bce3-24aa037ce27f / -— |
| Jogador 8 | 4-3 | 218 | REROLL | FAST8 | 44.0 | 6 | 99 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 219 | REROLL | FAST8 | 44.0 | 6 | 99 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 220 | REROLL | FAST8 | 44.0 | 6 | 99 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 222 | SELL | STABILIZE | 33.0 | 6 | 109 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -ea460790-b046-451d-9174-8b613e476241 |
| Jogador 8 | 4-4 | 223 | BUY | STABILIZE | 33.0 | 6 | 110 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9040489196777344 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -— |
| Jogador 8 | 4-4 | 224 | SELL | STABILIZE | 33.0 | 6 | 107 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45946773886680603 | 0.0 | 0.0 | +— / -5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 |
| Jogador 8 | 4-4 | 225 | BUY | STABILIZE | 33.0 | 6 | 110 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8788709044456482 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -— |
| Jogador 8 | 4-4 | 226 | SELL | STABILIZE | 33.0 | 6 | 108 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.333344429731369 | 0.0 | 0.0 | +— / -2e656a3d-eed0-40bb-a831-443d972d6588 |
| Jogador 8 | 4-4 | 227 | BUY | STABILIZE | 33.0 | 6 | 111 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06266685575246811 | 0.0 | 0.0 | +a58767a1-d7c1-48e9-94ae-df46a364ef92 / -— |
| Jogador 8 | 4-4 | 228 | REROLL | STABILIZE | 33.0 | 6 | 110 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 229 | SELL | STABILIZE | 33.0 | 6 | 108 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -a58767a1-d7c1-48e9-94ae-df46a364ef92 |
| Jogador 8 | 4-4 | 230 | BUY | STABILIZE | 33.0 | 6 | 109 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8686667680740356 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 8 | 4-5 | 232 | SELL | STABILIZE | 33.0 | 6 | 116 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -2faa526c-d29e-47a9-9eb3-5030750cb483 |
| Jogador 8 | 4-5 | 233 | BUY | STABILIZE | 33.0 | 6 | 117 | 5 | 38.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9636229276657104 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -9af097e2-729d-474a-9a7e-b266c665c606,b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 4-5 | 234 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 114 | 5 | 32.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5950329303741455 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 235 | BUY | STABILIZE | 33.0 | 6 | 114 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05003179609775543 | 0.0 | 0.0 | +20821a31-3317-4f82-bbb2-b70cdebdd893 / -— |
| Jogador 8 | 4-5 | 236 | MOVE_BOARD | STABILIZE | 33.0 | 6 | 112 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00015160611656028777 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 237 | BUY | STABILIZE | 33.0 | 6 | 112 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04657571017742157 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 8 | 4-5 | 238 | REROLL | STABILIZE | 33.0 | 6 | 111 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 239 | SELL | STABILIZE | 33.0 | 6 | 109 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -6fb9f857-4ee1-4b52-8825-57f514dc2d0f |
| Jogador 8 | 4-5 | 240 | BUY | STABILIZE | 33.0 | 6 | 110 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5091992616653442 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 8 | 4-6 | 242 | SELL | ALL_IN | 22.0 | 6 | 119 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5583333373069763 | 0.0 | 0.0 | +— / -20821a31-3317-4f82-bbb2-b70cdebdd893 |
| Jogador 8 | 4-6 | 243 | BUY | ALL_IN | 22.0 | 6 | 121 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6783189177513123 | 0.0 | 0.0 | +ee67f5c6-559f-492e-9cc0-6bc19a203d6a / -— |
| Jogador 8 | 4-6 | 244 | SELL | ALL_IN | 22.0 | 6 | 117 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -db6b2dca-4de1-420e-aadb-943e19b6121a |
| Jogador 8 | 4-6 | 245 | BUY | ALL_IN | 22.0 | 6 | 119 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5323581099510193 | 0.0 | 0.0 | +2f2ff445-f60a-4a05-b37a-41b8a6d6c7f9 / -— |
| Jogador 8 | 4-6 | 246 | SELL | ALL_IN | 22.0 | 6 | 116 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5428036451339722 | 0.0 | 0.0 | +— / -2f2ff445-f60a-4a05-b37a-41b8a6d6c7f9 |
| Jogador 8 | 4-6 | 247 | BUY | ALL_IN | 22.0 | 6 | 119 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06463096290826797 | 0.0 | 0.0 | +2f5d8cb8-8ba3-45e9-a345-00e931d34490 / -— |
| Jogador 8 | 4-6 | 248 | MOVE_BENCH | ALL_IN | 22.0 | 6 | 116 | 5 | 44.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22174105048179626 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 249 | REROLL | ALL_IN | 22.0 | 6 | 116 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 250 | SELL | ALL_IN | 22.0 | 6 | 114 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5722882151603699 | 0.0 | 0.0 | +— / -ee67f5c6-559f-492e-9cc0-6bc19a203d6a |
| Jogador 8 | 4-7 | 252 | BUY | ALL_IN | 22.0 | 6 | 129 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06155049428343773 | 0.0 | 0.0 | +79b461e3-2c4f-40a2-b967-e0b6d5248bf6 / -— |
| Jogador 8 | 4-7 | 253 | SELL | ALL_IN | 22.0 | 6 | 127 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -79b461e3-2c4f-40a2-b967-e0b6d5248bf6 |
| Jogador 8 | 4-7 | 254 | BUY | ALL_IN | 22.0 | 6 | 129 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061571720987558365 | 0.0 | 0.0 | +986fbe1e-1826-4be7-a5d6-410a4c0a3f2f / -— |
| Jogador 8 | 4-7 | 255 | REROLL | ALL_IN | 22.0 | 6 | 127 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 256 | SELL | ALL_IN | 22.0 | 6 | 125 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -986fbe1e-1826-4be7-a5d6-410a4c0a3f2f |
| Jogador 8 | 4-7 | 257 | BUY | ALL_IN | 22.0 | 6 | 127 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4290968179702759 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -— |
| Jogador 8 | 4-7 | 258 | REROLL | ALL_IN | 22.0 | 6 | 124 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 259 | SELL | ALL_IN | 22.0 | 6 | 122 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022262167185544968 | 0.0 | 0.0 | +— / -ba7f039a-929c-4537-9eb6-f1dc4563cca8 |
| Jogador 8 | 4-7 | 260 | BUY | ALL_IN | 22.0 | 6 | 126 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4298672378063202 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -— |
| Jogador 8 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 22.0 | 6 | 135 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.119281105697155 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 22.0 | 6 | 135 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18541496992111206 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 264 | SELL | ALL_IN | 22.0 | 6 | 135 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6797000169754028 | 0.0 | 0.0 | +— / -a5deb295-89d5-4573-8ace-e370a0718266 |
| Jogador 8 | 5-1 | 265 | BUY | ALL_IN | 22.0 | 6 | 136 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.050207495689392 | 0.0 | 0.0 | +a5e92183-8d5d-434c-9294-47c6b7bfb91b / -696f53ae-1413-47cc-b491-9870b7bcba51,734c25e1-eddf-4452-a04a-1b39db3b94d0 |
| Jogador 8 | 5-1 | 266 | BUY | ALL_IN | 22.0 | 6 | 134 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7927091121673584 | 0.0 | 0.0 | +987e61e4-0d34-49cf-b1ef-a95a7a5dfb21 / -— |
| Jogador 8 | 5-1 | 267 | BUY | ALL_IN | 22.0 | 6 | 131 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4601322114467621 | 0.0 | 0.0 | +d5c73756-6784-44e9-b521-5c61db813319 / -— |
| Jogador 8 | 5-1 | 268 | SELL | ALL_IN | 22.0 | 6 | 130 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6848999857902527 | 0.0 | 0.0 | +— / -a5e92183-8d5d-434c-9294-47c6b7bfb91b |
| Jogador 8 | 5-1 | 269 | BUY | ALL_IN | 22.0 | 6 | 135 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9813353419303894 | 0.0 | 0.0 | +d8392323-28e4-4e98-a466-5958bf400729 / -— |
| Jogador 8 | 5-1 | 270 | REROLL | ALL_IN | 22.0 | 6 | 134 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 272 | SELL | ALL_IN | 22.0 | 6 | 144 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6822999715805054 | 0.0 | 0.0 | +— / -217a3ebb-1953-4f1e-bfdd-a3c9438e791e |
| Jogador 8 | 5-2 | 273 | BUY | ALL_IN | 22.0 | 6 | 147 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4539848268032074 | 0.0 | 0.0 | +95a2e19e-619f-4497-ba52-e9bbf06b364f / -— |
| Jogador 8 | 5-2 | 274 | SELL | ALL_IN | 22.0 | 6 | 144 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6822999715805054 | 0.0 | 0.0 | +— / -95a2e19e-619f-4497-ba52-e9bbf06b364f |
| Jogador 8 | 5-2 | 275 | BUY | ALL_IN | 22.0 | 6 | 147 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4483213424682617 | 0.0 | 0.0 | +0b38218d-9c50-41ac-b761-115c054bf314 / -— |
| Jogador 8 | 5-2 | 276 | REROLL | ALL_IN | 22.0 | 6 | 145 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 277 | SELL | ALL_IN | 22.0 | 6 | 143 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6809999942779541 | 0.0 | 0.0 | +— / -0b38218d-9c50-41ac-b761-115c054bf314 |
| Jogador 8 | 5-2 | 278 | BUY | ALL_IN | 22.0 | 6 | 145 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4462299942970276 | 0.0 | 0.0 | +efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 / -— |
| Jogador 8 | 5-2 | 279 | SELL | ALL_IN | 22.0 | 6 | 143 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6809999942779541 | 0.0 | 0.0 | +— / -efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 |
| Jogador 8 | 5-2 | 280 | BUY | ALL_IN | 22.0 | 6 | 145 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4203164279460907 | 0.0 | 0.0 | +8486b8a9-20fe-4234-bbba-0efa031c3b76 / -— |
| Jogador 8 | 5-3 | 282 | SELL | ALL_IN | 6.0 | 6 | 154 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7221431136131287 | 0.0 | 0.0 | +— / -8486b8a9-20fe-4234-bbba-0efa031c3b76 |
| Jogador 8 | 5-3 | 283 | BUY | ALL_IN | 6.0 | 6 | 155 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4814032018184662 | 0.0 | 0.0 | +3365b4aa-125c-4f72-bcc5-01c5a205b9b0 / -— |
| Jogador 8 | 5-3 | 284 | SELL | ALL_IN | 6.0 | 6 | 152 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7271000146865845 | 0.0 | 0.0 | +— / -3365b4aa-125c-4f72-bcc5-01c5a205b9b0 |
| Jogador 8 | 5-3 | 285 | BUY | ALL_IN | 6.0 | 6 | 155 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03683924674987793 | 0.0 | 0.0 | +8068dc77-9528-4a1d-b4dc-5ac216e8684f / -— |
| Jogador 8 | 5-3 | 286 | REROLL | ALL_IN | 6.0 | 6 | 153 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 287 | SELL | ALL_IN | 6.0 | 6 | 151 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009301097132265568 | 0.0 | 0.0 | +— / -8068dc77-9528-4a1d-b4dc-5ac216e8684f |
| Jogador 8 | 5-3 | 288 | BUY | ALL_IN | 6.0 | 6 | 153 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.918119490146637 | 0.0 | 0.0 | +c2bf43be-e6e1-47ed-bcb4-606e37f26671 / -— |
| Jogador 8 | 5-3 | 289 | SELL | ALL_IN | 6.0 | 6 | 150 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6753937602043152 | 0.0 | 0.0 | +— / -987e61e4-0d34-49cf-b1ef-a95a7a5dfb21 |
| Jogador 8 | 5-3 | 290 | BUY | ALL_IN | 6.0 | 6 | 153 | 5 | 42.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4839792549610138 | 0.0 | 0.0 | +b58c0c0e-9c6f-4977-91d1-177b7113c439 / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 235 | 202 | 123 | 3 | 6 | 0 | 1 | 0 | 144 | 36.0 |
- Jogador 1 — gasto por ação: BUY: 168g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 47g, stage 3: 49g, stage 4: 61g, stage 5: 39g
| Jogador 2 | 298 | 293 | 197 | 8 | 9 | 2 | 1 | 0 | 185 | 40.0 |
- Jogador 2 — gasto por ação: BUY: 247g, BUY_XP: 44g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 60g, stage 3: 73g, stage 4: 62g, stage 5: 62g, stage 6: 29g
| Jogador 3 | 257 | 240 | 139 | 5 | 12 | 0 | 0 | 0 | 196 | 46.0 |
- Jogador 3 — gasto por ação: BUY: 188g, BUY_XP: 52g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 49g, stage 3: 59g, stage 4: 22g, stage 5: 48g, stage 6: 55g
| Jogador 4 | 182 | 167 | 89 | 4 | 6 | 1 | 1 | 0 | 74 | 32.0 |
- Jogador 4 — gasto por ação: BUY: 133g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 69g, stage 3: 43g, stage 4: 49g
| Jogador 5 | 201 | 203 | 135 | 6 | 4 | 0 | 3 | 0 | 116 | 24.0 |
- Jogador 5 — gasto por ação: BUY: 173g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 6g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 59g, stage 3: 63g, stage 4: 64g, stage 5: 10g
| Jogador 6 | 210 | 219 | 136 | 11 | 8 | 0 | 4 | 0 | 88 | 28.0 |
- Jogador 6 — gasto por ação: BUY: 175g, BUY_XP: 36g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 8g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 63g, stage 3: 56g, stage 4: 69g, stage 5: 26g
| Jogador 7 | 284 | 297 | 176 | 5 | 13 | 1 | 2 | 0 | 178 | 40.0 |
- Jogador 7 — gasto por ação: BUY: 229g, BUY_XP: 64g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 50g, stage 3: 53g, stage 4: 59g, stage 5: 67g, stage 6: 62g
| Jogador 8 | 218 | 179 | 111 | 4 | 0 | 0 | 11 | 0 | 152 | 42.0 |
- Jogador 8 — gasto por ação: BUY: 159g, BUY_XP: 4g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 16g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 51g, stage 3: 26g, stage 4: 65g, stage 5: 30g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 8 | 7 |
- Jogador 1 · 2-7 · step 116: PASS com 4g, HP 93, nível 6/8 (STABILIZE).
- Jogador 1 · 4-6 · step 248: PASS com 75g, HP 43, nível 7/8 (STABILIZE).
- Jogador 1 · 4-7 · step 259: PASS com 83g, HP 43, nível 7/8 (STABILIZE).
- Jogador 1 · 5-2 · step 278: PASS com 93g, HP 29, nível 7/8 (STABILIZE).
- Jogador 1 · 5-4 · step 299: PASS com 124g, HP 17, nível 7/8 (ALL_IN).
- Jogador 1 · 5-5 · step 306: PASS com 133g, HP 17, nível 7/8 (ALL_IN).
- Jogador 1 · 5-6 · step 319: REROLL com 144g, HP 2, nível 7/8 (ALL_IN).
| Jogador 2 | 11 | 3 |
- Jogador 2 · 5-2 · step 279: REROLL com 75g, HP 31, nível 7/8 (STABILIZE).
- Jogador 2 · 5-3 · step 290: PASS com 79g, HP 31, nível 7/8 (STABILIZE).
- Jogador 2 · 6-4 · step 367: PASS com 178g, HP 14, nível 7/8 (ALL_IN).
| Jogador 3 | 13 | 12 |
- Jogador 3 · 3-2 · step 134: PASS com 6g, HP 91, nível 6/8 (STABILIZE).
- Jogador 3 · 3-3 · step 148: PASS com 8g, HP 81, nível 6/8 (STABILIZE).
- Jogador 3 · 4-2 · step 204: PASS com 8g, HP 68, nível 7/8 (FAST8).
- Jogador 3 · 4-3 · step 214: PASS com 15g, HP 68, nível 7/8 (FAST8).
- Jogador 3 · 4-4 · step 224: PASS com 23g, HP 68, nível 7/8 (FAST8).
- Jogador 3 · 4-5 · step 238: PASS com 26g, HP 68, nível 7/8 (FAST8).
- Jogador 3 · 4-6 · step 249: PASS com 40g, HP 68, nível 7/8 (FAST8).
- Jogador 3 · 4-7 · step 256: PASS com 50g, HP 68, nível 7/8 (FAST8).
- Jogador 3 · 5-1 · step 266: PASS com 63g, HP 68, nível 7/8 (FAST8).
- Jogador 3 · 5-2 · step 276: PASS com 79g, HP 68, nível 7/8 (FAST8).
- Jogador 3 · 5-3 · step 288: PASS com 88g, HP 53, nível 7/8 (FAST8).
- Jogador 3 · 5-4 · step 299: PASS com 94g, HP 53, nível 7/8 (FAST8).
| Jogador 4 | 8 | 8 |
- Jogador 4 · 3-5 · step 169: PASS com 13g, HP 62, nível 6/8 (STABILIZE).
- Jogador 4 · 3-7 · step 190: PASS com 26g, HP 43, nível 6/8 (STABILIZE).
- Jogador 4 · 4-1 · step 198: PASS com 31g, HP 43, nível 6/8 (STABILIZE).
- Jogador 4 · 4-2 · step 210: PASS com 51g, HP 31, nível 6/8 (STABILIZE).
- Jogador 4 · 4-3 · step 216: REROLL com 56g, HP 17, nível 6/8 (ALL_IN).
- Jogador 4 · 4-4 · step 230: PASS com 57g, HP 17, nível 7/8 (ALL_IN).
- Jogador 4 · 4-5 · step 239: PASS com 67g, HP 17, nível 7/8 (ALL_IN).
- Jogador 4 · 4-6 · step 250: PASS com 74g, HP 5, nível 7/8 (ALL_IN).
| Jogador 5 | 6 | 4 |
- Jogador 5 · 4-2 · step 209: REROLL com 64g, HP 49, nível 6/8 (STABILIZE).
- Jogador 5 · 4-3 · step 217: PASS com 65g, HP 37, nível 6/8 (STABILIZE).
- Jogador 5 · 4-4 · step 230: REROLL com 81g, HP 24, nível 6/8 (ALL_IN).
- Jogador 5 · 4-5 · step 240: REROLL com 90g, HP 24, nível 6/8 (ALL_IN).
| Jogador 6 | 9 | 7 |
- Jogador 6 · 4-1 · step 198: REROLL com 17g, HP 46, nível 6/8 (STABILIZE).
- Jogador 6 · 4-2 · step 210: PASS com 16g, HP 36, nível 7/8 (STABILIZE).
- Jogador 6 · 4-3 · step 220: PASS com 24g, HP 24, nível 7/8 (ALL_IN).
- Jogador 6 · 4-4 · step 228: REROLL com 35g, HP 24, nível 7/8 (ALL_IN).
- Jogador 6 · 4-6 · step 246: REROLL com 43g, HP 24, nível 7/8 (ALL_IN).
- Jogador 6 · 5-2 · step 279: PASS com 70g, HP 14, nível 7/8 (ALL_IN).
- Jogador 6 · 5-3 · step 287: REROLL com 84g, HP 14, nível 7/8 (ALL_IN).
| Jogador 7 | 16 | 9 |
- Jogador 7 · 3-7 · step 187: PASS com 4g, HP 84, nível 7/8 (STABILIZE).
- Jogador 7 · 4-4 · step 228: PASS com 20g, HP 84, nível 7/8 (STABILIZE).
- Jogador 7 · 4-5 · step 240: PASS com 30g, HP 84, nível 7/8 (STABILIZE).
- Jogador 7 · 4-6 · step 248: PASS com 43g, HP 84, nível 7/8 (STABILIZE).
- Jogador 7 · 4-7 · step 260: PASS com 48g, HP 84, nível 7/8 (STABILIZE).
- Jogador 7 · 5-1 · step 268: PASS com 52g, HP 84, nível 7/8 (STABILIZE).
- Jogador 7 · 5-4 · step 300: PASS com 90g, HP 55, nível 7/8 (STABILIZE).
- Jogador 7 · 5-6 · step 320: REROLL com 111g, HP 40, nível 7/8 (STABILIZE).
- Jogador 7 · 5-7 · step 330: REROLL com 120g, HP 27, nível 7/8 (STABILIZE).
| Jogador 8 | 1 | 18 |
- Jogador 8 · 2-6 · step 110: PASS com 9g, HP 80, nível 5/8 (STABILIZE).
- Jogador 8 · 3-2 · step 138: PASS com 30g, HP 75, nível 5/8 (STABILIZE).
- Jogador 8 · 3-4 · step 157: PASS com 49g, HP 56, nível 5/8 (STABILIZE).
- Jogador 8 · 3-5 · step 165: PASS com 56g, HP 56, nível 5/8 (STABILIZE).
- Jogador 8 · 3-6 · step 177: PASS com 66g, HP 44, nível 5/8 (STABILIZE).
- Jogador 8 · 3-7 · step 187: PASS com 72g, HP 44, nível 6/8 (STABILIZE).
- Jogador 8 · 4-1 · step 200: PASS com 78g, HP 44, nível 6/8 (STABILIZE).
- Jogador 8 · 4-3 · step 218: REROLL com 99g, HP 44, nível 6/8 (FAST8).
- Jogador 8 · 4-3 · step 219: REROLL com 99g, HP 44, nível 6/8 (FAST8).
- Jogador 8 · 4-3 · step 220: REROLL com 99g, HP 44, nível 6/8 (FAST8).
- Jogador 8 · 4-4 · step 228: REROLL com 110g, HP 33, nível 6/8 (STABILIZE).
- Jogador 8 · 4-5 · step 238: REROLL com 111g, HP 33, nível 6/8 (STABILIZE).
- Jogador 8 · 4-6 · step 249: REROLL com 116g, HP 22, nível 6/8 (ALL_IN).
- Jogador 8 · 4-7 · step 255: REROLL com 127g, HP 22, nível 6/8 (ALL_IN).
- Jogador 8 · 4-7 · step 258: REROLL com 124g, HP 22, nível 6/8 (ALL_IN).
- Jogador 8 · 5-1 · step 270: REROLL com 134g, HP 22, nível 6/8 (ALL_IN).
- Jogador 8 · 5-2 · step 276: REROLL com 145g, HP 22, nível 6/8 (ALL_IN).
- Jogador 8 · 5-3 · step 286: REROLL com 153g, HP 6, nível 6/8 (ALL_IN).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 2 | 2 | 0 | 0.0% |
| Jogador 2 | 2 | 2 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 2 | 2 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 235 | 39 | 47 | 149 | -0.0003 | -0.0378 | -0.0011 | 0.2882 | 0.0008 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0162 (77 ações), BUY_XP: Δ 0.0115 (8 ações), CRAFT_AND_EQUIP: Δ 0.0020 (7 ações), MOVE_BENCH: Δ 0.0356 (19 ações), MOVE_BOARD: Δ 0.0024 (56 ações), PASS: Δ 0.0000 (18 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0051 (49 ações)
| Jogador 2 | 298 | 58 | 49 | 191 | 0.0021 | 0.4245 | 0.0009 | 0.4114 | 0.0012 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0003 (108 ações), BUY_XP: Δ 0.0089 (11 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0025 (58 ações), MOVE_BOARD: Δ -0.0032 (25 ações), PASS: Δ 0.0000 (11 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0065 (75 ações)
| Jogador 3 | 257 | 48 | 36 | 173 | 0.0048 | 0.5145 | 0.0035 | 0.3303 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0163 (82 ações), BUY_XP: Δ 0.0038 (13 ações), CRAFT_AND_EQUIP: Δ 0.0147 (7 ações), EQUIP_FROM_INVENTORY: Δ -0.0565 (3 ações), MOVE_BENCH: Δ 0.0280 (17 ações), MOVE_BOARD: Δ 0.0245 (62 ações), PASS: Δ 0.0000 (24 ações), SELL: Δ 0.0122 (49 ações)
| Jogador 4 | 182 | 42 | 40 | 100 | -0.0038 | 0.0699 | -0.0036 | 0.4184 | -0.0002 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0103 (65 ações), BUY_XP: Δ 0.0135 (8 ações), CRAFT_AND_EQUIP: Δ 0.0028 (5 ações), EQUIP_FROM_INVENTORY: Δ -0.1267 (3 ações), MOVE_BENCH: Δ 0.0142 (24 ações), MOVE_BOARD: Δ -0.0341 (28 ações), PASS: Δ 0.0238 (16 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0149 (32 ações)
| Jogador 5 | 201 | 35 | 27 | 139 | 0.0018 | -0.0943 | -0.0000 | 0.3436 | 0.0018 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0155 (92 ações), BUY_XP: Δ 0.0162 (6 ações), CRAFT_AND_EQUIP: Δ 0.0010 (7 ações), MOVE_BENCH: Δ 0.0218 (16 ações), MOVE_BOARD: Δ 0.0914 (8 ações), PASS: Δ 0.0000 (8 ações), REROLL: Δ 0.0000 (3 ações), SELL: Δ 0.0100 (61 ações)
| Jogador 6 | 210 | 40 | 45 | 125 | 0.0019 | -0.4488 | 0.0008 | 0.3988 | 0.0011 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0173 (75 ações), BUY_XP: Δ 0.0029 (9 ações), CRAFT_AND_EQUIP: Δ 0.0007 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (6 ações), MOVE_BENCH: Δ 0.0637 (13 ações), MOVE_BOARD: Δ -0.0055 (33 ações), PASS: Δ 0.0000 (13 ações), REROLL: Δ 0.0000 (4 ações), SELL: Δ 0.0204 (50 ações)
| Jogador 7 | 284 | 49 | 47 | 188 | 0.0039 | 0.2567 | 0.0026 | 0.3738 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0128 (91 ações), BUY_XP: Δ 0.0091 (16 ações), CRAFT_AND_EQUIP: Δ 0.0364 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0545 (14 ações), MOVE_BENCH: Δ 0.0070 (23 ações), MOVE_BOARD: Δ 0.0080 (52 ações), PASS: Δ 0.0000 (22 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0094 (57 ações)
| Jogador 8 | 218 | 45 | 45 | 128 | 0.0025 | 0.1617 | 0.0010 | 0.3272 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0140 (81 ações), BUY_XP: Δ 0.0477 (1 ações), CRAFT_AND_EQUIP: Δ 0.0030 (7 ações), MOVE_BENCH: Δ 0.0158 (48 ações), MOVE_BOARD: Δ 0.0392 (10 ações), PASS: Δ 0.0000 (11 ações), REROLL: Δ 0.0000 (11 ações), SELL: Δ 0.0094 (49 ações)
- Jogador 1 — rounds avaliados: 31; correlação estrutural/combate: 0.392; posicional/combate: 0.104.
- Jogador 1 — combate positive: score estrutural prévio 0.137
  score posicional prévio 0.309
- Jogador 1 — combate negative: score estrutural prévio -0.149
  score posicional prévio 0.287
- Jogador 2 — rounds avaliados: 37; correlação estrutural/combate: 0.068; posicional/combate: 0.007.
- Jogador 2 — combate positive: score estrutural prévio 0.474
  score posicional prévio 0.412
- Jogador 2 — combate negative: score estrutural prévio 0.431
  score posicional prévio 0.413
- Jogador 3 — rounds avaliados: 38; correlação estrutural/combate: 0.101; posicional/combate: 0.105.
- Jogador 3 — combate positive: score estrutural prévio 0.526
  score posicional prévio 0.339
- Jogador 3 — combate negative: score estrutural prévio 0.426
  score posicional prévio 0.347
- Jogador 4 — rounds avaliados: 24; correlação estrutural/combate: 0.180; posicional/combate: -0.093.
- Jogador 4 — combate positive: score estrutural prévio 0.141
  score posicional prévio 0.397
- Jogador 4 — combate negative: score estrutural prévio 0.013
  score posicional prévio 0.404
- Jogador 5 — rounds avaliados: 26; correlação estrutural/combate: -0.031; posicional/combate: -0.330.
- Jogador 5 — combate positive: score estrutural prévio -0.074
  score posicional prévio 0.326
- Jogador 5 — combate negative: score estrutural prévio -0.066
  score posicional prévio 0.355
- Jogador 6 — rounds avaliados: 28; correlação estrutural/combate: 0.164; posicional/combate: -0.305.
- Jogador 6 — combate positive: score estrutural prévio -0.259
  score posicional prévio 0.347
- Jogador 6 — combate negative: score estrutural prévio -0.527
  score posicional prévio 0.447
- Jogador 7 — rounds avaliados: 38; correlação estrutural/combate: 0.120; posicional/combate: 0.148.
- Jogador 7 — combate positive: score estrutural prévio 0.286
  score posicional prévio 0.402
- Jogador 7 — combate negative: score estrutural prévio 0.217
  score posicional prévio 0.374
- Jogador 8 — rounds avaliados: 28; correlação estrutural/combate: -0.054; posicional/combate: -0.150.
- Jogador 8 — combate positive: score estrutural prévio 0.122
  score posicional prévio 0.296
- Jogador 8 — combate negative: score estrutural prévio 0.172
  score posicional prévio 0.324

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 265 | OK (265) | 7 | 0 | 0 | 0 | 7 | 0 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Crownguard, TFT_Item_HextechGunblade, TFT_Item_InfinityEdge, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon, TFT_Item_SpectralGauntlet; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 334 | OK (334) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_Crownguard, TFT_Item_GargoyleStoneplate, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_RunaansHurricane; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 295 | OK (295) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_GuinsoosRageblade, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_Redemption, TFT_Item_SteraksGage, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 205 | OK (205) | 5 | 0 | 0 | 1 | 5 | 3 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 226 | OK (226) | 7 | 0 | 0 | 0 | 7 | 0 |
- Jogador 5 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_IonicSpark, TFT_Item_Leviathan, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_PowerGauntlet; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 237 | OK (237) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 6 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_JeweledGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 321 | OK (321) | 8 | 0 | 0 | 0 | 8 | 3 |
- Jogador 7 — IDs equipados observados: TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 245 | OK (245) | 6 | 1 | 0 | 0 | 7 | 0 |
- Jogador 8 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_DragonsClaw, TFT_Item_InfinityEdge, TFT_Item_LastWhisper, TFT_Item_Morellonomicon, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.110 | 0.000 |
| Jogador 1 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.001 | 0.000 |
| Jogador 1 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 1 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.012 | 0.000 |
| Jogador 1 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 6 | 5 | 4 → 4 | -0.014 | 0.427 |
| Jogador 1 | 2-2 | 10 | 2.000 | 0.000 | 0 → 0 | 3 → 3 | 14% → 18% | 6 → 8 | 9 | 4 → 5 | -0.027 | 0.264 |
| Jogador 1 | 2-3 | 8 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 18% → 18% | 8 → 5 | 11 | 5 → 5 | 0.000 | -0.323 |
| Jogador 1 | 2-4 | 7 | 2.000 | 4.000 | 0 → 0 | 3 → 2 | 18% → 18% | 5 → 6 | 4 | 5 → 5 | -0.002 | 0.000 |
| Jogador 1 | 2-5 | 10 | 0.000 | 4.000 | 0 → 0 | 2 → 3 | 18% → 18% | 6 → 7 | 8 | 5 → 6 | 0.073 | 0.256 |
| Jogador 1 | 2-6 | 9 | 6.000 | 6.000 | 0 → 1 | 3 → 2 | 18% → 21% | 7 → 7 | 7 | 6 → 6 | 0.007 | 0.324 |
| Jogador 1 | 2-7 | 7 | 2.000 | 2.000 | 1 → 2 | 2 → 2 | 21% → 18% | 7 → 10 | 3 | 6 → 6 | -0.062 | 0.000 |
| Jogador 1 | 3-1 | 10 | 4.000 | 0.000 | 2 → 2 | 2 → 2 | 18% → 21% | 10 → 7 | 10 | 6 → 6 | -0.006 | 0.286 |
| Jogador 1 | 3-2 | 8 | 0.000 | 14.000 | 2 → 2 | 2 → 2 | 21% → 21% | 7 → 7 | 7 | 6 → 6 | 0.009 | 0.351 |
| Jogador 1 | 3-3 | 9 | 0.000 | 14.000 | 2 → 2 | 2 → 2 | 21% → 21% | 7 → 5 | 9 | 6 → 6 | -0.049 | -0.287 |
| Jogador 1 | 3-4 | 10 | 0.000 | -6.000 | 2 → 2 | 2 → 2 | 21% → 21% | 5 → 13 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 3-5 | 10 | 4.000 | -8.000 | 2 → 2 | 2 → 2 | 21% → 21% | 13 → 21 | 4 | 6 → 6 | -0.006 | 0.286 |
| Jogador 1 | 3-6 | 10 | 0.000 | -2.000 | 2 → 2 | 2 → 4 | 21% → 21% | 21 → 29 | 5 | 6 → 6 | -0.007 | -0.259 |
| Jogador 1 | 3-7 | 10 | 0.000 | -4.000 | 2 → 2 | 4 → 4 | 21% → 21% | 29 → 39 | 8 | 6 → 6 | -0.006 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | 8.000 | 2 → 2 | 4 → 4 | 21% → 21% | 39 → 44 | 8 | 6 → 6 | 0.062 | 0.281 |
| Jogador 1 | 4-2 | 10 | 0.000 | -10.000 | 2 → 2 | 4 → 4 | 21% → 21% | 44 → 58 | 6 | 6 → 6 | -0.056 | -0.268 |
| Jogador 1 | 4-3 | 10 | 0.000 | -12.000 | 2 → 2 | 4 → 2 | 21% → 21% | 58 → 74 | 7 | 6 → 6 | 0.000 | -0.268 |
| Jogador 1 | 4-4 | 10 | 0.000 | -4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 74 → 87 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 4-5 | 10 | 6.000 | 14.000 | 2 → 2 | 2 → 2 | 21% → 25% | 87 → 84 | 17 | 6 → 7 | 0.097 | -0.263 |
| Jogador 1 | 4-6 | 8 | 0.000 | 18.000 | 2 → 2 | 2 → 3 | 25% → 25% | 84 → 86 | 9 | 7 → 7 | -0.001 | 0.345 |
| Jogador 1 | 4-7 | 9 | 0.000 | 6.000 | 2 → 2 | 3 → 4 | 25% → 25% | 86 → 93 | 6 | 7 → 7 | -0.001 | 0.000 |
| Jogador 1 | 5-1 | 10 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 25% → 25% | 93 → 100 | 9 | 7 → 7 | -0.006 | -0.273 |
| Jogador 1 | 5-2 | 8 | 2.000 | 10.000 | 2 → 3 | 4 → 4 | 25% → 25% | 100 → 104 | 7 | 7 → 7 | -0.051 | -0.333 |
| Jogador 1 | 5-3 | 10 | 0.000 | -12.000 | 3 → 3 | 4 → 4 | 25% → 25% | 104 → 123 | 7 | 7 → 7 | 0.017 | 0.294 |
| Jogador 1 | 5-4 | 9 | 0.000 | -2.000 | 3 → 3 | 4 → 4 | 25% → 25% | 123 → 134 | 1 | 7 → 7 | -0.035 | 0.000 |
| Jogador 1 | 5-5 | 6 | 0.000 | 2.000 | 3 → 3 | 4 → 4 | 25% → 25% | 134 → 143 | 5 | 7 → 7 | -0.070 | -0.500 |
| Jogador 1 | 5-6 | 10 | -36.000 | -50.000 | 3 → 0 | 4 → 0 | 25% → 0% | 143 → 144 | 10 | 7 → 7 | 0.021 | -0.285 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 33, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 14; mudanças de composição: 1; posicionamento melhorou em 43 ações e piorou em 49.
- Jogador 1 — estado final: ouro 144, nível 7, vida 2.0, colocação 4.
| Jogador 2 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.161 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.109 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 3 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 8 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 11% → 14% | 4 → 5 | 5 | 4 → 4 | -0.020 | -0.289 |
| Jogador 2 | 2-2 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 1 | 14% → 14% | 5 → 6 | 8 | 4 → 4 | 0.024 | -0.248 |
| Jogador 2 | 2-3 | 4 | 2.000 | 0.000 | 1 → 1 | 1 → 1 | 14% → 18% | 6 → 7 | 5 | 4 → 5 | 0.019 | 0.689 |
| Jogador 2 | 2-4 | 10 | 4.000 | 8.000 | 1 → 1 | 1 → 2 | 18% → 18% | 7 → 6 | 8 | 5 → 5 | 0.027 | 0.000 |
| Jogador 2 | 2-5 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 18% → 18% | 6 → 6 | 14 | 5 → 5 | 0.001 | -0.248 |
| Jogador 2 | 2-6 | 10 | 0.000 | -6.000 | 1 → 1 | 2 → 2 | 18% → 18% | 6 → 7 | 14 | 5 → 6 | 0.005 | -0.253 |
| Jogador 2 | 2-7 | 7 | 2.000 | 10.000 | 1 → 1 | 2 → 2 | 18% → 21% | 7 → 7 | 6 | 6 → 6 | -0.031 | 0.000 |
| Jogador 2 | 3-1 | 9 | 0.000 | 12.000 | 1 → 1 | 2 → 2 | 21% → 21% | 7 → 7 | 6 | 6 → 6 | -0.015 | 0.307 |
| Jogador 2 | 3-2 | 10 | 4.000 | -8.000 | 1 → 1 | 2 → 2 | 21% → 21% | 7 → 8 | 10 | 6 → 6 | 0.025 | 0.272 |
| Jogador 2 | 3-3 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 3 | 21% → 21% | 8 → 8 | 16 | 6 → 6 | 0.000 | 0.281 |
| Jogador 2 | 3-4 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 21% → 21% | 8 → 6 | 14 | 6 → 7 | 0.005 | 0.000 |
| Jogador 2 | 3-5 | 10 | 6.000 | 0.000 | 1 → 1 | 3 → 4 | 21% → 25% | 6 → 10 | 6 | 7 → 7 | -0.003 | 0.308 |
| Jogador 2 | 3-6 | 7 | 0.000 | 16.000 | 1 → 1 | 4 → 4 | 25% → 25% | 10 → 7 | 8 | 7 → 7 | 0.008 | -0.396 |
| Jogador 2 | 3-7 | 10 | -4.000 | 6.000 | 1 → 1 | 4 → 3 | 25% → 25% | 7 → 10 | 13 | 7 → 7 | 0.043 | 0.000 |
| Jogador 2 | 4-1 | 10 | 0.000 | -6.000 | 1 → 1 | 3 → 3 | 25% → 25% | 10 → 20 | 10 | 7 → 7 | 0.000 | -0.266 |
| Jogador 2 | 4-2 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 20 → 27 | 9 | 7 → 7 | 0.000 | 0.293 |
| Jogador 2 | 4-3 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 3 | 25% → 25% | 27 → 36 | 9 | 7 → 7 | -0.000 | -0.276 |
| Jogador 2 | 4-4 | 10 | 6.000 | -6.000 | 1 → 1 | 3 → 3 | 25% → 25% | 36 → 44 | 10 | 7 → 7 | 0.008 | 0.000 |
| Jogador 2 | 4-5 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 4 | 25% → 25% | 44 → 53 | 12 | 7 → 7 | 0.000 | 0.280 |
| Jogador 2 | 4-6 | 10 | -2.000 | -6.000 | 1 → 1 | 4 → 4 | 25% → 21% | 53 → 67 | 5 | 7 → 7 | 0.004 | -0.281 |
| Jogador 2 | 4-7 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 67 → 76 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 10 | 6.000 | 10.000 | 1 → 1 | 4 → 4 | 21% → 25% | 76 → 79 | 11 | 7 → 7 | 0.000 | 0.306 |
| Jogador 2 | 5-2 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 3 | 25% → 25% | 79 → 87 | 16 | 7 → 7 | 0.000 | 0.301 |
| Jogador 2 | 5-3 | 10 | 4.000 | 12.000 | 1 → 1 | 3 → 2 | 25% → 25% | 87 → 91 | 11 | 7 → 7 | -0.052 | 0.307 |
| Jogador 2 | 5-4 | 10 | 4.000 | 0.000 | 1 → 1 | 2 → 3 | 25% → 25% | 91 → 100 | 7 | 7 → 7 | 0.003 | 0.000 |
| Jogador 2 | 5-5 | 10 | -2.000 | 0.000 | 1 → 1 | 3 → 5 | 25% → 25% | 100 → 113 | 5 | 7 → 7 | -0.003 | 0.316 |
| Jogador 2 | 5-6 | 10 | -4.000 | -4.000 | 1 → 1 | 5 → 3 | 25% → 21% | 113 → 124 | 6 | 7 → 7 | -0.021 | 0.291 |
| Jogador 2 | 5-7 | 10 | -4.000 | 16.000 | 1 → 1 | 3 → 3 | 21% → 21% | 124 → 130 | 6 | 7 → 7 | -0.001 | 0.000 |
| Jogador 2 | 6-1 | 10 | 4.000 | -10.000 | 1 → 1 | 3 → 3 | 21% → 21% | 130 → 149 | 3 | 7 → 7 | 0.009 | 0.296 |
| Jogador 2 | 6-2 | 10 | -4.000 | -2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 149 → 164 | 3 | 7 → 7 | 0.003 | -0.285 |
| Jogador 2 | 6-3 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 4 | 21% → 21% | 164 → 176 | 10 | 7 → 7 | 0.000 | 0.291 |
| Jogador 2 | 6-4 | 7 | 6.000 | -10.000 | 1 → 1 | 4 → 5 | 21% → 25% | 176 → 188 | 3 | 7 → 7 | -0.006 | 0.000 |
| Jogador 2 | 6-5 | 10 | -38.000 | -48.000 | 1 → 0 | 5 → 0 | 25% → 0% | 188 → 185 | 10 | 7 → 7 | -0.071 | -0.275 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 49, COMPOSITION_COMPATIBILITY: 33, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 17; mudanças de composição: 1; posicionamento melhorou em 63 ações e piorou em 51.
- Jogador 2 — estado final: ouro 185, nível 7, vida 14.0, colocação 3.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.060 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 3 | 1-4 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.002 | 0.000 |
| Jogador 3 | 2-1 | 8 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.003 | 0.327 |
| Jogador 3 | 2-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.684 |
| Jogador 3 | 2-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 8 | 7 | 4 → 5 | 0.006 | 0.502 |
| Jogador 3 | 2-4 | 9 | 6.000 | 2.000 | 1 → 1 | 1 → 2 | 14% → 18% | 8 → 6 | 8 | 5 → 5 | 0.019 | 0.000 |
| Jogador 3 | 2-5 | 4 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 18% → 18% | 6 → 8 | 5 | 5 → 5 | -0.000 | 0.628 |
| Jogador 3 | 2-6 | 10 | 6.000 | -4.000 | 1 → 2 | 3 → 1 | 18% → 18% | 8 → 8 | 9 | 5 → 5 | 0.002 | 0.269 |
| Jogador 3 | 2-7 | 10 | 6.000 | 4.000 | 2 → 2 | 1 → 2 | 18% → 21% | 8 → 7 | 11 | 5 → 6 | 0.058 | 0.000 |
| Jogador 3 | 3-1 | 10 | 0.000 | 4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 7 → 6 | 7 | 6 → 6 | 0.006 | -0.254 |
| Jogador 3 | 3-2 | 4 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 21% → 21% | 6 → 12 | 0 | 6 → 6 | -0.230 | -0.658 |
| Jogador 3 | 3-3 | 8 | 0.000 | 0.000 | 2 → 2 | 2 → 3 | 21% → 21% | 12 → 14 | 6 | 6 → 6 | 0.119 | 0.345 |
| Jogador 3 | 3-4 | 10 | 2.000 | 0.000 | 2 → 2 | 3 → 4 | 21% → 21% | 14 → 6 | 15 | 6 → 6 | -0.058 | 0.000 |
| Jogador 3 | 3-5 | 7 | 0.000 | 4.000 | 2 → 2 | 4 → 3 | 21% → 21% | 6 → 6 | 7 | 6 → 6 | 0.000 | -0.407 |
| Jogador 3 | 3-6 | 7 | 0.000 | 8.000 | 2 → 2 | 3 → 2 | 21% → 21% | 6 → 6 | 6 | 6 → 7 | -0.006 | 0.414 |
| Jogador 3 | 3-7 | 10 | 4.000 | -12.000 | 2 → 2 | 2 → 3 | 21% → 25% | 6 → 6 | 18 | 7 → 7 | 0.010 | 0.000 |
| Jogador 3 | 4-1 | 10 | 0.000 | 10.000 | 2 → 2 | 3 → 5 | 25% → 25% | 6 → 8 | 6 | 7 → 7 | 0.059 | 0.283 |
| Jogador 3 | 4-2 | 4 | 0.000 | 0.000 | 2 → 2 | 5 → 5 | 25% → 25% | 8 → 15 | 0 | 7 → 7 | -0.015 | 0.759 |
| Jogador 3 | 4-3 | 4 | 0.000 | 0.000 | 2 → 2 | 5 → 5 | 25% → 25% | 15 → 23 | 0 | 7 → 7 | 0.000 | 0.740 |
| Jogador 3 | 4-4 | 4 | 0.000 | 0.000 | 2 → 2 | 5 → 5 | 25% → 25% | 23 → 31 | 0 | 7 → 7 | -0.004 | 0.000 |
| Jogador 3 | 4-5 | 8 | 0.000 | 4.000 | 2 → 2 | 5 → 4 | 25% → 25% | 31 → 36 | 9 | 7 → 7 | -0.112 | 0.360 |
| Jogador 3 | 4-6 | 9 | 6.000 | -16.000 | 2 → 3 | 4 → 3 | 25% → 25% | 36 → 53 | 4 | 7 → 7 | 0.051 | 0.320 |
| Jogador 3 | 4-7 | 6 | 0.000 | 6.000 | 3 → 3 | 3 → 3 | 25% → 25% | 53 → 63 | 3 | 7 → 7 | 0.080 | 0.000 |
| Jogador 3 | 5-1 | 6 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 25% → 25% | 63 → 77 | 0 | 7 → 7 | -0.148 | 0.481 |
| Jogador 3 | 5-2 | 6 | 0.000 | -4.000 | 3 → 3 | 3 → 4 | 25% → 25% | 77 → 89 | 1 | 7 → 7 | 0.000 | -0.475 |
| Jogador 3 | 5-3 | 8 | 0.000 | 2.000 | 3 → 3 | 4 → 5 | 25% → 25% | 89 → 99 | 5 | 7 → 7 | 0.000 | 0.369 |
| Jogador 3 | 5-4 | 9 | 0.000 | 4.000 | 3 → 3 | 5 → 3 | 25% → 25% | 99 → 104 | 7 | 7 → 7 | 0.063 | 0.000 |
| Jogador 3 | 5-5 | 10 | 0.000 | -4.000 | 3 → 3 | 3 → 3 | 25% → 25% | 104 → 120 | 14 | 7 → 7 | 0.006 | 0.296 |
| Jogador 3 | 5-6 | 10 | 0.000 | -2.000 | 3 → 3 | 3 → 3 | 25% → 25% | 120 → 133 | 12 | 7 → 7 | 0.000 | 0.301 |
| Jogador 3 | 5-7 | 10 | 0.000 | -2.000 | 3 → 3 | 3 → 4 | 25% → 25% | 133 → 145 | 9 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-1 | 10 | 0.000 | 4.000 | 3 → 3 | 4 → 4 | 25% → 25% | 145 → 154 | 13 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-2 | 10 | 0.000 | -6.000 | 3 → 3 | 4 → 4 | 25% → 25% | 154 → 169 | 9 | 7 → 7 | 0.007 | 0.304 |
| Jogador 3 | 6-3 | 10 | -2.000 | 4.000 | 3 → 3 | 4 → 3 | 25% → 21% | 169 → 178 | 7 | 7 → 7 | -0.018 | -0.275 |
| Jogador 3 | 6-4 | 10 | 6.000 | -6.000 | 3 → 3 | 3 → 4 | 21% → 25% | 178 → 188 | 11 | 7 → 7 | -0.010 | 0.000 |
| Jogador 3 | 6-5 | 10 | 0.000 | 4.000 | 3 → 3 | 4 → 4 | 25% → 25% | 188 → 197 | 7 | 7 → 7 | -0.006 | 0.291 |
| Jogador 3 | 6-6 | 10 | 0.000 | 2.000 | 3 → 3 | 4 → 4 | 25% → 25% | 197 → 197 | 8 | 7 → 7 | 0.000 | 0.310 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 23, COMPOSITION_COMPATIBILITY: 34, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 53 ações e piorou em 38.
- Jogador 3 — estado final: ouro 197, nível 7, vida 38.0, colocação 1.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 4 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.065 | 0.000 |
| Jogador 4 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 4 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.013 | 0.000 |
| Jogador 4 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 5 | 5 | 4 → 4 | -0.021 | -0.404 |
| Jogador 4 | 2-2 | 4 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 14% → 18% | 5 → 6 | 5 | 4 → 5 | 0.034 | 0.684 |
| Jogador 4 | 2-3 | 10 | 4.000 | -4.000 | 0 → 0 | 3 → 2 | 18% → 18% | 6 → 9 | 9 | 5 → 5 | 0.005 | 0.251 |
| Jogador 4 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 10 | 12 | 5 → 5 | -0.013 | 0.000 |
| Jogador 4 | 2-5 | 10 | 2.000 | 0.000 | 0 → 0 | 3 → 2 | 18% → 21% | 10 → 6 | 14 | 5 → 6 | -0.012 | -0.237 |
| Jogador 4 | 2-6 | 10 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 21% → 21% | 6 → 8 | 12 | 6 → 6 | 0.015 | -0.274 |
| Jogador 4 | 2-7 | 10 | 6.000 | 0.000 | 0 → 0 | 3 → 2 | 21% → 21% | 8 → 7 | 12 | 6 → 6 | 0.026 | 0.000 |
| Jogador 4 | 3-1 | 10 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 21% → 21% | 7 → 8 | 7 | 6 → 6 | 0.002 | 0.272 |
| Jogador 4 | 3-2 | 10 | 0.000 | 8.000 | 0 → 0 | 2 → 1 | 21% → 21% | 8 → 8 | 5 | 6 → 6 | -0.062 | -0.263 |
| Jogador 4 | 3-3 | 8 | 0.000 | 12.000 | 0 → 0 | 1 → 2 | 21% → 21% | 8 → 8 | 6 | 6 → 6 | 0.115 | -0.329 |
| Jogador 4 | 3-4 | 10 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 21% → 21% | 8 → 13 | 6 | 6 → 6 | -0.039 | 0.000 |
| Jogador 4 | 3-5 | 9 | 0.000 | 2.000 | 0 → 0 | 3 → 4 | 21% → 21% | 13 → 20 | 7 | 6 → 6 | 0.049 | -0.298 |
| Jogador 4 | 3-6 | 10 | 2.000 | -12.000 | 0 → 0 | 4 → 4 | 21% → 21% | 20 → 33 | 5 | 6 → 6 | 0.001 | -0.254 |
| Jogador 4 | 3-7 | 10 | -2.000 | 10.000 | 0 → 0 | 4 → 3 | 21% → 21% | 33 → 34 | 7 | 6 → 6 | -0.044 | 0.000 |
| Jogador 4 | 4-1 | 8 | -2.000 | 8.000 | 0 → 0 | 3 → 5 | 21% → 21% | 34 → 41 | 3 | 6 → 6 | -0.007 | -0.346 |
| Jogador 4 | 4-2 | 10 | 0.000 | -18.000 | 0 → 0 | 5 → 4 | 21% → 21% | 41 → 64 | 5 | 6 → 6 | 0.006 | -0.288 |
| Jogador 4 | 4-3 | 10 | 2.000 | 10.000 | 0 → 0 | 4 → 4 | 21% → 21% | 64 → 65 | 14 | 6 → 7 | 0.004 | 0.285 |
| Jogador 4 | 4-4 | 10 | 6.000 | 12.000 | 0 → 0 | 4 → 5 | 21% → 25% | 65 → 67 | 13 | 7 → 7 | -0.016 | 0.000 |
| Jogador 4 | 4-5 | 9 | 0.000 | 0.000 | 0 → 0 | 5 → 6 | 25% → 25% | 67 → 77 | 7 | 7 → 7 | -0.093 | -0.302 |
| Jogador 4 | 4-6 | 10 | -28.000 | -48.000 | 0 → 0 | 6 → 0 | 25% → 0% | 77 → 74 | 7 | 7 → 7 | 0.034 | -0.276 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 16, COMPOSITION_COMPATIBILITY: 21, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 19; mudanças de composição: 0; posicionamento melhorou em 48 ações e piorou em 41.
- Jogador 4 — estado final: ouro 74, nível 7, vida 5.0, colocação 8.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.112 | 0.000 |
| Jogador 5 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.003 | 0.000 |
| Jogador 5 | 2-1 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.000 | 0.347 |
| Jogador 5 | 2-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.607 |
| Jogador 5 | 2-3 | 10 | 6.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 5 | 11 | 4 → 5 | -0.007 | -0.237 |
| Jogador 5 | 2-4 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 5 → 6 | 11 | 5 → 5 | 0.000 | 0.000 |
| Jogador 5 | 2-5 | 10 | 2.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 6 → 6 | 13 | 5 → 6 | -0.006 | 0.264 |
| Jogador 5 | 2-6 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 9 | 7 | 6 → 6 | 0.019 | -0.253 |
| Jogador 5 | 2-7 | 10 | 2.000 | 6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 10 | 8 | 6 → 6 | -0.037 | 0.000 |
| Jogador 5 | 3-1 | 10 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 10 → 17 | 8 | 6 → 6 | 0.025 | -0.263 |
| Jogador 5 | 3-2 | 10 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 21% → 21% | 17 → 20 | 10 | 6 → 6 | 0.000 | 0.281 |
| Jogador 5 | 3-3 | 10 | 0.000 | 8.000 | 0 → 0 | 1 → 2 | 21% → 21% | 20 → 22 | 14 | 6 → 6 | 0.000 | -0.258 |
| Jogador 5 | 3-4 | 10 | 2.000 | -2.000 | 0 → 0 | 2 → 2 | 21% → 21% | 22 → 29 | 6 | 6 → 6 | 0.001 | 0.000 |
| Jogador 5 | 3-5 | 10 | 0.000 | -4.000 | 0 → 0 | 2 → 2 | 21% → 21% | 29 → 40 | 8 | 6 → 6 | 0.000 | -0.259 |
| Jogador 5 | 3-6 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 40 → 53 | 6 | 6 → 6 | 0.000 | 0.277 |
| Jogador 5 | 3-7 | 10 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 21% → 21% | 53 → 63 | 11 | 6 → 6 | -0.000 | 0.000 |
| Jogador 5 | 4-1 | 10 | -2.000 | 6.000 | 0 → 0 | 3 → 2 | 21% → 21% | 63 → 70 | 9 | 6 → 6 | -0.001 | -0.273 |
| Jogador 5 | 4-2 | 10 | 0.000 | 14.000 | 0 → 0 | 2 → 2 | 21% → 21% | 70 → 70 | 16 | 6 → 6 | -0.006 | -0.276 |
| Jogador 5 | 4-3 | 7 | 2.000 | 6.000 | 0 → 0 | 2 → 1 | 21% → 21% | 70 → 76 | 5 | 6 → 6 | -0.007 | -0.400 |
| Jogador 5 | 4-4 | 10 | 0.000 | -6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 76 → 90 | 8 | 6 → 6 | 0.012 | 0.000 |
| Jogador 5 | 4-5 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 90 → 99 | 11 | 6 → 6 | 0.000 | -0.268 |
| Jogador 5 | 4-6 | 10 | 0.000 | -6.000 | 0 → 0 | 1 → 3 | 21% → 21% | 99 → 114 | 7 | 6 → 6 | 0.027 | -0.271 |
| Jogador 5 | 4-7 | 10 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 114 → 126 | 8 | 6 → 7 | 0.005 | 0.000 |
| Jogador 5 | 5-1 | 10 | -20.000 | -32.000 | 0 → 0 | 3 → 0 | 21% → 0% | 126 → 116 | 10 | 7 → 7 | -0.058 | -0.290 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 35, COMPOSITION_COMPATIBILITY: 31, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 18; mudanças de composição: 1; posicionamento melhorou em 38 ações e piorou em 29.
- Jogador 5 — estado final: ouro 116, nível 7, vida 1.0, colocação 7.
| Jogador 6 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.163 | 0.000 |
| Jogador 6 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.039 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.021 | -0.412 |
| Jogador 6 | 2-2 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | -0.010 | -0.430 |
| Jogador 6 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 9 | 5 | 4 → 5 | -0.005 | -0.369 |
| Jogador 6 | 2-4 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 3 | 14% → 14% | 9 → 10 | 13 | 5 → 5 | 0.006 | 0.000 |
| Jogador 6 | 2-5 | 10 | 2.000 | -12.000 | 0 → 0 | 3 → 4 | 14% → 18% | 10 → 9 | 14 | 5 → 6 | 0.052 | -0.242 |
| Jogador 6 | 2-6 | 10 | 2.000 | 0.000 | 0 → 0 | 4 → 3 | 18% → 21% | 9 → 6 | 13 | 6 → 6 | 0.010 | 0.246 |
| Jogador 6 | 2-7 | 7 | 0.000 | 12.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 5 | 6 | 6 → 6 | 0.004 | 0.000 |
| Jogador 6 | 3-1 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 3 | 21% → 21% | 5 → 7 | 13 | 6 → 6 | 0.006 | -0.259 |
| Jogador 6 | 3-2 | 10 | 4.000 | 2.000 | 0 → 1 | 3 → 1 | 21% → 18% | 7 → 8 | 5 | 6 → 6 | 0.023 | -0.291 |
| Jogador 6 | 3-3 | 10 | 6.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 21% | 8 → 12 | 5 | 6 → 6 | -0.017 | 0.277 |
| Jogador 6 | 3-4 | 8 | 0.000 | 20.000 | 1 → 1 | 1 → 1 | 21% → 21% | 12 → 7 | 10 | 6 → 6 | -0.030 | 0.000 |
| Jogador 6 | 3-5 | 6 | 0.000 | 10.000 | 1 → 1 | 1 → 1 | 21% → 21% | 7 → 9 | 5 | 6 → 6 | -0.004 | 0.461 |
| Jogador 6 | 3-6 | 10 | 0.000 | 2.000 | 1 → 1 | 1 → 2 | 21% → 21% | 9 → 13 | 9 | 6 → 6 | 0.032 | -0.273 |
| Jogador 6 | 3-7 | 10 | 0.000 | -6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 13 → 22 | 9 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 10 | 0.000 | 12.000 | 1 → 1 | 2 → 3 | 21% → 21% | 22 → 21 | 11 | 6 → 7 | -0.002 | -0.263 |
| Jogador 6 | 4-2 | 10 | 8.000 | 2.000 | 1 → 1 | 3 → 3 | 21% → 25% | 21 → 23 | 6 | 7 → 7 | 0.021 | -0.281 |
| Jogador 6 | 4-3 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 23 → 32 | 7 | 7 → 7 | -0.021 | 0.293 |
| Jogador 6 | 4-4 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 4 | 25% → 25% | 32 → 40 | 12 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 10 | -4.000 | 8.000 | 1 → 1 | 4 → 3 | 25% → 25% | 40 → 45 | 9 | 7 → 7 | 0.022 | 0.285 |
| Jogador 6 | 4-6 | 10 | 0.000 | -6.000 | 1 → 1 | 3 → 2 | 25% → 25% | 45 → 56 | 17 | 7 → 7 | 0.006 | -0.258 |
| Jogador 6 | 4-7 | 10 | 2.000 | 4.000 | 1 → 1 | 2 → 3 | 25% → 21% | 56 → 63 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 10 | 6.000 | 4.000 | 1 → 1 | 3 → 3 | 21% → 25% | 63 → 68 | 11 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 5-2 | 9 | 0.000 | -4.000 | 1 → 1 | 3 → 4 | 25% → 25% | 68 → 81 | 5 | 7 → 7 | -0.003 | 0.336 |
| Jogador 6 | 5-3 | 10 | -34.000 | -58.000 | 1 → 0 | 4 → 0 | 25% → 0% | 81 → 88 | 10 | 7 → 7 | -0.036 | -0.280 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 22, COMPOSITION_COMPATIBILITY: 36, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 44 ações e piorou em 47.
- Jogador 6 — estado final: ouro 88, nível 7, vida 14.0, colocação 6.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.043 | 0.000 |
| Jogador 7 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.077 | 0.000 |
| Jogador 7 | 2-1 | 6 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.016 | 0.456 |
| Jogador 7 | 2-2 | 10 | -2.000 | 4.000 | 0 → 0 | 3 → 2 | 14% → 11% | 8 → 8 | 8 | 4 → 4 | 0.015 | -0.258 |
| Jogador 7 | 2-3 | 9 | 10.000 | -6.000 | 0 → 0 | 2 → 2 | 11% → 14% | 8 → 8 | 9 | 4 → 5 | 0.056 | 0.304 |
| Jogador 7 | 2-4 | 4 | 6.000 | 8.000 | 0 → 0 | 2 → 2 | 14% → 18% | 8 → 6 | 7 | 5 → 5 | -0.013 | 0.000 |
| Jogador 7 | 2-5 | 6 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 18% → 18% | 6 → 9 | 4 | 5 → 5 | -0.012 | 0.419 |
| Jogador 7 | 2-6 | 10 | 0.000 | -2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 9 | 12 | 5 → 5 | 0.013 | 0.269 |
| Jogador 7 | 2-7 | 7 | 8.000 | -2.000 | 0 → 0 | 3 → 3 | 18% → 21% | 9 → 8 | 7 | 5 → 6 | 0.028 | 0.000 |
| Jogador 7 | 3-1 | 7 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 8 → 7 | 6 | 6 → 6 | -0.009 | -0.383 |
| Jogador 7 | 3-2 | 4 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 7 → 6 | 7 | 6 → 6 | 0.000 | 0.771 |
| Jogador 7 | 3-3 | 10 | 0.000 | -4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 7 | 14 | 6 → 6 | -0.006 | 0.286 |
| Jogador 7 | 3-4 | 10 | -4.000 | 0.000 | 0 → 0 | 3 → 1 | 21% → 18% | 7 → 8 | 8 | 6 → 6 | -0.000 | 0.000 |
| Jogador 7 | 3-5 | 9 | 8.000 | 0.000 | 0 → 0 | 1 → 2 | 18% → 25% | 8 → 7 | 8 | 6 → 7 | -0.003 | 0.335 |
| Jogador 7 | 3-6 | 6 | 0.000 | 8.000 | 0 → 0 | 2 → 3 | 25% → 25% | 7 → 10 | 4 | 7 → 7 | 0.000 | 0.492 |
| Jogador 7 | 3-7 | 7 | -4.000 | 8.000 | 0 → 0 | 3 → 3 | 25% → 25% | 10 → 10 | 6 | 7 → 7 | -0.018 | 0.000 |
| Jogador 7 | 4-1 | 10 | 0.000 | 12.000 | 0 → 0 | 3 → 3 | 25% → 25% | 10 → 8 | 10 | 7 → 7 | -0.011 | 0.293 |
| Jogador 7 | 4-2 | 8 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 25% → 25% | 8 → 11 | 6 | 7 → 7 | 0.059 | 0.373 |
| Jogador 7 | 4-3 | 10 | 0.000 | -4.000 | 0 → 0 | 3 → 3 | 25% → 25% | 11 → 12 | 16 | 7 → 7 | 0.026 | 0.285 |
| Jogador 7 | 4-4 | 8 | 0.000 | -10.000 | 0 → 0 | 3 → 5 | 25% → 25% | 12 → 30 | 6 | 7 → 7 | -0.004 | 0.000 |
| Jogador 7 | 4-5 | 10 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 25% → 25% | 30 → 42 | 8 | 7 → 7 | -0.022 | 0.285 |
| Jogador 7 | 4-6 | 8 | 0.000 | -2.000 | 0 → 0 | 5 → 5 | 25% → 25% | 42 → 56 | 4 | 7 → 7 | -0.007 | 0.367 |
| Jogador 7 | 4-7 | 10 | 4.000 | 2.000 | 0 → 1 | 5 → 3 | 25% → 25% | 56 → 60 | 9 | 7 → 7 | -0.004 | 0.000 |
| Jogador 7 | 5-1 | 8 | 0.000 | 16.000 | 1 → 1 | 3 → 3 | 25% → 25% | 60 → 62 | 8 | 7 → 7 | -0.001 | -0.344 |
| Jogador 7 | 5-2 | 10 | 0.000 | -10.000 | 1 → 1 | 3 → 4 | 25% → 25% | 62 → 80 | 8 | 7 → 7 | -0.009 | 0.283 |
| Jogador 7 | 5-3 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 80 → 90 | 8 | 7 → 7 | 0.000 | -0.290 |
| Jogador 7 | 5-4 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 90 → 100 | 9 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-5 | 10 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 100 → 112 | 9 | 7 → 7 | -0.022 | -0.280 |
| Jogador 7 | 5-6 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 112 → 120 | 12 | 7 → 7 | 0.000 | -0.275 |
| Jogador 7 | 5-7 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 5 | 25% → 25% | 120 → 129 | 13 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 10 | 0.000 | -2.000 | 1 → 1 | 5 → 4 | 25% → 25% | 129 → 140 | 11 | 7 → 8 | 0.025 | -0.280 |
| Jogador 7 | 6-2 | 10 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 140 → 152 | 12 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 6-3 | 10 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 152 → 164 | 13 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 6-4 | 10 | 2.000 | 2.000 | 1 → 1 | 4 → 4 | 25% → 21% | 164 → 173 | 8 | 8 → 8 | 0.010 | 0.000 |
| Jogador 7 | 6-5 | 10 | 4.000 | 4.000 | 1 → 1 | 4 → 3 | 21% → 21% | 173 → 177 | 7 | 8 → 8 | -0.013 | 0.000 |
| Jogador 7 | 6-6 | 10 | -40.000 | -52.000 | 1 → 0 | 3 → 0 | 21% → 0% | 177 → 178 | 11 | 8 → 8 | -0.069 | -0.290 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 36, COMPOSITION_COMPATIBILITY: 27, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 18; mudanças de composição: 0; posicionamento melhorou em 52 ações e piorou em 52.
- Jogador 7 — estado final: ouro 178, nível 8, vida 12.0, colocação 2.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.113 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.074 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 3 | 3 → 4 | 0.007 | 0.000 |
| Jogador 8 | 2-1 | 8 | 6.000 | 0.000 | 0 → 2 | 2 → 0 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.003 | -0.322 |
| Jogador 8 | 2-2 | 10 | 0.000 | 12.000 | 2 → 2 | 0 → 0 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | 0.013 | -0.231 |
| Jogador 8 | 2-3 | 10 | 0.000 | 6.000 | 2 → 1 | 0 → 0 | 14% → 14% | 6 → 9 | 6 | 4 → 4 | 0.021 | -0.237 |
| Jogador 8 | 2-4 | 10 | 2.000 | 8.000 | 1 → 1 | 0 → 1 | 14% → 18% | 9 → 7 | 11 | 4 → 5 | -0.003 | 0.000 |
| Jogador 8 | 2-5 | 10 | 0.000 | 8.000 | 1 → 1 | 1 → 3 | 18% → 18% | 7 → 9 | 8 | 5 → 5 | 0.066 | -0.237 |
| Jogador 8 | 2-6 | 10 | 4.000 | -4.000 | 1 → 1 | 3 → 4 | 18% → 18% | 9 → 16 | 7 | 5 → 5 | -0.025 | -0.232 |
| Jogador 8 | 2-7 | 10 | -2.000 | 2.000 | 1 → 1 | 4 → 4 | 18% → 18% | 16 → 24 | 7 | 5 → 5 | 0.040 | 0.000 |
| Jogador 8 | 3-1 | 10 | 0.000 | 2.000 | 1 → 0 | 4 → 4 | 18% → 18% | 24 → 31 | 4 | 5 → 5 | -0.062 | 0.281 |
| Jogador 8 | 3-2 | 8 | 0.000 | 4.000 | 0 → 0 | 4 → 4 | 18% → 18% | 31 → 38 | 5 | 5 → 5 | -0.055 | -0.317 |
| Jogador 8 | 3-3 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 4 | 18% → 18% | 38 → 48 | 6 | 5 → 5 | 0.011 | -0.268 |
| Jogador 8 | 3-4 | 7 | 2.000 | -8.000 | 0 → 0 | 4 → 2 | 18% → 14% | 48 → 59 | 2 | 5 → 5 | -0.021 | 0.000 |
| Jogador 8 | 3-5 | 6 | 4.000 | 2.000 | 0 → 0 | 2 → 3 | 14% → 18% | 59 → 67 | 3 | 5 → 5 | -0.015 | -0.486 |
| Jogador 8 | 3-6 | 7 | 4.000 | -4.000 | 0 → 1 | 3 → 2 | 18% → 18% | 67 → 77 | 1 | 5 → 6 | -0.038 | 0.388 |
| Jogador 8 | 3-7 | 7 | 6.000 | 4.000 | 1 → 1 | 2 → 2 | 18% → 21% | 77 → 82 | 5 | 6 → 6 | 0.087 | 0.000 |
| Jogador 8 | 4-1 | 10 | 4.000 | 0.000 | 1 → 2 | 2 → 1 | 21% → 21% | 82 → 90 | 4 | 6 → 6 | -0.046 | 0.290 |
| Jogador 8 | 4-2 | 10 | 2.000 | 6.000 | 2 → 2 | 1 → 2 | 21% → 21% | 90 → 100 | 8 | 6 → 6 | 0.138 | 0.286 |
| Jogador 8 | 4-3 | 10 | 0.000 | 2.000 | 2 → 2 | 2 → 2 | 21% → 21% | 100 → 109 | 8 | 6 → 6 | 0.000 | -0.268 |
| Jogador 8 | 4-4 | 10 | 0.000 | 2.000 | 2 → 2 | 2 → 4 | 21% → 21% | 109 → 116 | 11 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 10 | 6.000 | 0.000 | 2 → 3 | 4 → 4 | 21% → 21% | 116 → 119 | 10 | 6 → 6 | 0.003 | -0.268 |
| Jogador 8 | 4-6 | 10 | -2.000 | 0.000 | 3 → 3 | 4 → 3 | 21% → 21% | 119 → 129 | 12 | 6 → 6 | -0.001 | 0.298 |
| Jogador 8 | 4-7 | 10 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 129 → 135 | 12 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 10 | 0.000 | 0.000 | 3 → 3 | 3 → 4 | 21% → 21% | 135 → 144 | 9 | 6 → 6 | -0.000 | 0.291 |
| Jogador 8 | 5-2 | 10 | 0.000 | -4.000 | 3 → 3 | 4 → 4 | 21% → 21% | 144 → 154 | 10 | 6 → 6 | -0.000 | -0.285 |
| Jogador 8 | 5-3 | 10 | -42.000 | -42.000 | 3 → 0 | 4 → 0 | 21% → 0% | 154 → 152 | 11 | 6 → 6 | -0.111 | -0.278 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 22, COMPOSITION_COMPATIBILITY: 32, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 18; mudanças de composição: 0; posicionamento melhorou em 50 ações e piorou em 48.
- Jogador 8 — estado final: ouro 152, nível 6, vida 6.0, colocação 5.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 77 | 49 | 5 | 5 | 7 | 1 | 0 | 0 | 11 | 0 | 1 | 0 |
| Jogador 2 | 108 | 75 | 2 | 2 | 4 | 0 | 0 | 0 | 36 | 3 | 2 | 0 |
| Jogador 3 | 82 | 49 | 0 | 0 | 0 | 0 | 0 | 0 | 28 | 0 | 0 | 0 |
| Jogador 4 | 65 | 32 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 6 | 1 | 0 |
| Jogador 5 | 92 | 61 | 4 | 5 | 8 | 2 | 1 | 1 | 13 | 1 | 1 | 0 |
| Jogador 6 | 75 | 50 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 2 | 2 | 0 |
| Jogador 7 | 91 | 57 | 0 | 0 | 0 | 0 | 0 | 0 | 27 | 1 | 0 | 0 |
| Jogador 8 | 81 | 49 | 0 | 0 | 0 | 0 | 0 | 0 | 21 | 0 | 1 | 0 |
- Jogador 1 — venda DA_18_Ornn (2-5, step 94): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Camille (4-1, step 196): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Gromp18_AP (4-3, step 220): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Kayle (3-3, step 146): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Warwick (3-4, step 157): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rakan (4-6, step 247): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Yorick (5-1, step 266): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 2 — venda DA_18_Veigar (5-3, step 286): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Yorick (2-7, step 114): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Scuttlecrab18 (3-7, step 182): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_KhaZix (5-3, step 284): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Gromp18_AP (5-4, step 292): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_18_KhaZix (6-1, step 335): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_RekSai (6-3, step 355): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Rakan (2-7, step 116): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Alistar (3-1, step 126): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Akali_AD (3-6, step 176): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_18_Sejuani (3-6, step 180): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_MasterYi_AD (4-2, step 202): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Warwick (4-3, step 217): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 5 — venda DA_18_RekSai (2-7, step 115): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 5 — venda DA_18_Ornn (3-2, step 136): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Kobuko (3-4, step 156): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 5 — venda DA_18_Tristana (3-4, step 157): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_Scuttlecrab18 (3-7, step 188): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Yunara (4-2, step 207): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Leona (4-7, step 254): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Yunara (4-7, step 258): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-6, step 107): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 6 — venda DA_18_Sentry (3-3, step 144): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Xayah (4-7, step 254): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 6 — venda DA_18_Diana (5-3, step 290): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Camille (2-6, step 106): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rakan (3-4, step 157): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_KogMaw18_AD (4-3, step 212): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_Sentinel18 (4-4, step 222): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Hecarim (5-2, step 272): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Tristana (5-5, step 304): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Ezreal (5-7, step 326): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Krug18 (3-1, step 123): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 8 — venda DA_Karma18 (4-2, step 206): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Vi18 (4-4, step 224): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Elise (4-6, step 242): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Vi18 (4-6, step 246): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Sivir (4-6, step 250): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Azir (5-3, step 289): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **6**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| LOW | Jogador 1 | 2-3 | 75 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 1 | 2-5 | 94 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-1 | 196 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-2 | 210 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rammus) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 4-3 | 216 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Karma18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 4-3 | 217 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rengar) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 4-3 | 219 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 4-3 | 220 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-4 | 225 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Alistar) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 4-4 | 226 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Elise) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 4-4 | 228 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 1 | 2-2 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 267 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 268 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 269 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 270 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 271 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 272 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 273 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 274 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 275 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 276 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 277 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 278 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 281 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 282 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 283 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 284 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 285 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 286 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 287 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 288 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 289 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 290 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 291 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 292 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 293 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 294 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 295 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 296 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 297 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 298 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 299 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 301 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 302 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 303 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 304 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 305 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 306 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 311 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 312 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 313 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 314 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 315 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 316 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 317 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 318 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 319 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 320 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 321 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 527 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-3 | 634 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 733 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-6 | 988 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 989 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1090 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1334 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-2 | 1335 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1462 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-3 | 1463 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1596 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-4 | 1597 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1737 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-6 | 1879 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-7 | 2018 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-1 | 2160 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 2301 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-3 | 2437 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-4 | 2576 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-5 | 2710 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-6 | 2824 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-7 | 2950 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-1 | 3090 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-2 | 3208 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-3 | 3351 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-4 | 3482 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-5 | 3570 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-6 | 3706 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 5-6 | 3707 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 4-5 | 2801 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-6 | 2927 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-1 | 3185 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 2 | 2-5 | 97 | PURCHASE_SALE_REVIEW | Compra de DA_18_Azir foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 2 | 2-5 | 99 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Ornn) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-6 | 104 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sejuani) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-6 | 107 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-3 | 146 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kayle' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-4 | 157 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-4 | 157 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Warwick) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 2 | 3-5 | 166 | PURCHASE_SALE_REVIEW | Compra de DA_18_Teemo foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 2 | 4-6 | 247 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-3 | 286 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Veigar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 314 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 315 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 316 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 317 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 318 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 319 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 320 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 321 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 322 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 323 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 324 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 325 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 326 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 327 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 328 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 329 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 330 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 331 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 332 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 333 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 334 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 335 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 336 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 337 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 338 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 339 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 340 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 341 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 342 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 343 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 344 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 345 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 346 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 347 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 348 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 349 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 350 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 351 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 352 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 353 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 354 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 355 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 356 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 357 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 358 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 359 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 360 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 361 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-1 | 1266 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-2 | 1402 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-3 | 1538 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-4 | 1674 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-5 | 1810 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-6 | 1911 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-7 | 2049 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-1 | 2185 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-2 | 2321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2458 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 2595 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2730 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 2875 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 3012 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 3150 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 3285 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-3 | 3424 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-4 | 3559 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-5 | 3695 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-6 | 3832 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-7 | 3967 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-1 | 4110 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-2 | 4255 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-3 | 4396 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-4 | 4497 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-5 | 4637 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 6-5 | 4638 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 5-2 | 3401 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 3 | 2-7 | 114 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 3-7 | 182 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 5-3 | 284 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 6-1 | 335 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 6-3 | 355 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 248 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 249 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-7 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-7 | 253 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-7 | 254 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-7 | 255 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-7 | 256 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-7 | 261 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-1 | 262 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-1 | 263 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-1 | 264 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-1 | 265 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-1 | 266 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-1 | 271 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-2 | 272 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-2 | 273 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-2 | 274 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-2 | 275 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-2 | 276 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-2 | 281 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-3 | 282 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-3 | 283 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-3 | 284 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-3 | 285 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-3 | 286 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-3 | 287 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-3 | 288 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-3 | 291 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-4 | 292 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-4 | 293 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-4 | 294 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-4 | 295 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-4 | 296 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-4 | 297 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-4 | 298 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-4 | 299 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-4 | 301 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 302 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 303 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 304 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 305 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 306 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 307 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 308 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 309 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 310 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 311 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-6 | 312 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-6 | 313 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-6 | 314 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-6 | 315 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-6 | 316 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-6 | 317 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-6 | 318 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-6 | 319 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-6 | 320 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-6 | 321 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 322 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 323 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 324 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 325 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 326 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 327 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 328 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 329 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 330 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 331 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 332 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 333 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 334 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 335 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 336 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 337 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 338 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 339 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 340 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 341 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-2 | 342 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-2 | 343 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-2 | 344 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-2 | 345 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-2 | 346 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-2 | 347 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-2 | 348 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-2 | 349 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-2 | 350 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-2 | 351 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-3 | 352 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-3 | 353 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-3 | 354 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-4 | 701 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-5 | 759 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-6 | 890 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 1022 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1155 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1218 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-2 | 1219 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-3 | 1326 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1455 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1553 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 1649 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 1783 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 1923 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 1985 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-5 | 2224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-1 | 2527 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-2 | 2618 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-2 | 2619 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-3 | 2734 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-3 | 2735 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-4 | 2863 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-4 | 2864 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-5 | 3008 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-5 | 3009 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-6 | 3148 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-6 | 3149 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-7 | 3291 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-7 | 3292 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-1 | 3430 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 6-1 | 3431 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-2 | 3574 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 6-2 | 3575 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-3 | 3719 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 6-3 | 3720 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-4 | 3857 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 6-4 | 3858 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-5 | 4001 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 6-5 | 4002 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-6 | 4142 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 6-6 | 4143 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 2-6 | 104 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 4 | 2-7 | 116 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 3-1 | 126 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 3-6 | 180 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 2-5 | 849 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-6 | 981 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-7 | 1112 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-1 | 1247 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-2 | 1383 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-2 | 1384 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 2021 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-1 | 2132 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 2269 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-3 | 2409 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-4 | 2549 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 2673 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-5 | 2674 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-6 | 2813 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-6 | 2814 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 3-4 | 1728 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-6 | 1998 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-7 | 2109 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-1 | 2246 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-4 | 87 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 107 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Elise) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-2 | 135 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-2 | 136 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Ornn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-2 | 139 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-3 | 149 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rammus) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-6 | 176 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-6 | 180 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 3-7 | 187 | PURCHASE_SALE_REVIEW | Compra de DA_Vi18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 3-7 | 188 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-7 | 254 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Leona' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-7 | 258 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 2-1 | 58 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 59 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 3-3 | 149 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 3-5 | 169 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 170 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 226 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 227 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 228 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 229 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 230 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 4-7 | 259 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 260 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 261 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 262 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 263 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 264 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 265 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 266 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 267 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 268 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 269 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 270 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 271 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-3 | 558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 690 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 823 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 957 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-7 | 1092 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-7 | 1093 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-1 | 1229 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-1 | 1230 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-2 | 1366 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1367 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-3 | 1502 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-3 | 1503 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-4 | 1637 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-4 | 1638 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-5 | 1780 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1781 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-6 | 1918 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1919 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-7 | 2055 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-7 | 2056 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-1 | 2193 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-1 | 2194 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-2 | 2334 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 2335 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-3 | 2434 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2435 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-4 | 2572 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-4 | 2573 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-5 | 2707 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-5 | 2708 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 2849 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-7 | 2987 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 3127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-1 | 3128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 4-2 | 2411 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 2-3 | 76 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 2-5 | 96 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 6 | 3-3 | 144 | SOLD_CORE_UNIT | Venda de 'DA_18_Sentry' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 5-3 | 290 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
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
| LOW | Jogador 6 | 2-7 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 148 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 149 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 3-7 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 4-2 | 208 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 209 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 210 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 4-4 | 229 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 230 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 2-6 | 937 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1033 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1167 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1304 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1441 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1550 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1635 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-6 | 1767 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1904 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 2040 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 2178 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 2179 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 2313 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 2314 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 2448 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 2449 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-5 | 2584 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 2720 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-7 | 2866 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 3006 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 3007 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 3135 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-2 | 3136 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-3 | 3277 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-3 | 3278 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 4-1 | 2155 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-6 | 106 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 3-4 | 157 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 4-3 | 212 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 4-4 | 222 | SOLD_CORE_UNIT | Venda de 'DA_Sentinel18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 5-2 | 272 | SOLD_CORE_UNIT | Venda de 'DA_18_Hecarim' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 5-5 | 304 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 5-7 | 326 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Ezreal' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 2-4 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 7 | 2-7 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 429 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 567 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-5 | 841 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-6 | 975 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-7 | 1071 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-5 | 1632 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-5 | 1633 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1723 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-6 | 1724 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 1822 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-7 | 1823 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 1959 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-1 | 1960 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2071 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-2 | 2072 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2209 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-3 | 2210 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2318 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-4 | 2319 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2454 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-5 | 2455 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2565 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-6 | 2566 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2703 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-7 | 2704 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 2819 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-1 | 2820 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-2 | 2961 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-2 | 2962 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-3 | 3098 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-3 | 3099 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-4 | 3237 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-4 | 3238 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-5 | 3378 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-5 | 3379 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-6 | 3515 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-6 | 3516 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-7 | 3659 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-7 | 3660 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-1 | 3799 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-1 | 3800 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-2 | 3936 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-2 | 3937 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-3 | 4077 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-3 | 4078 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-4 | 4227 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-4 | 4228 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-5 | 4370 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-5 | 4371 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-6 | 4512 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 6-6 | 4513 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 4-3 | 2295 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-4 | 2431 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-5 | 2542 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-6 | 2680 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-7 | 2796 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 5-3 | 3214 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 8 | 1-4 | 46 | PURCHASE_SALE_REVIEW | Compra de DA_18_RekSai foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 8 | 4-2 | 206 | SOLD_CORE_UNIT | Venda de 'DA_Karma18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-4 | 224 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-6 | 242 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-6 | 246 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-6 | 250 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sivir' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-3 | 289 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Azir' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 3-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 8 | 3-4 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 169 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-1 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-1 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-2 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-2 | 207 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-2 | 208 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-2 | 209 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-2 | 210 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-3 | 224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-4 | 321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 433 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-2 | 566 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-6 | 1104 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-2 | 1485 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1619 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-4 | 1716 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-5 | 1800 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-6 | 1900 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 1996 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 2132 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-2 | 2270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 2409 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-4 | 2557 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-5 | 2695 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-3 | 3408 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 5-3 | 3409 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 3-1 | 1462 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-3 | 1693 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-4 | 1765 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-5 | 1877 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-6 | 1973 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-7 | 2109 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-2 | 2361 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-2 | 2373 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-2 | 2385 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
