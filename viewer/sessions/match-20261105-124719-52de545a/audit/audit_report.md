# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4996**
- Achados: **370**
- CRITICAL: 0 | HIGH: 26 | MEDIUM: 63 | LOW: 281

## Metadados da sessão

- Match ID: 52de545a-9c6f-45b5-8095-22a9a9e426c7
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: c383ebab86eba153dfaa53718694bc39064eb5f59ae8ce5b419ba8b61e9e2a42
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4408**
- Entradas posteriores à eliminação ignoradas: **588**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 35 | 8 | 20 | 11 | 54 | 3 | 3 | não/inconclusivo | 0 |
| Jogador 6 | 97 | 7 | 5 | 18 | 53 | 3 | 2 | não/inconclusivo | 0 |
| Jogador 7 | 108 | 8 | 21 | 3 | 58 | 6 | 1 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 218 | 58 | 27 | 15 | 5 | 20 | 79 | 0.0733 | 14 | 37 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 15, ALL_IN::BUY_XP: 2, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 3, ALL_IN::REROLL: 5, ALL_IN::SELL: 9, FAST8::BUY: 7, FAST8::BUY_XP: 1, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 7, FAST8::MOVE_BOARD: 9, FAST8::PASS: 5, FAST8::SELL: 4, STABILIZE::BUY: 36, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 10, STABILIZE::MOVE_BENCH: 30, STABILIZE::MOVE_BOARD: 30, STABILIZE::PASS: 15, STABILIZE::SELL: 14
- Jogador 1 — recompensas por ação: BUY: média 0.4328 (n=58), BUY_XP: média 0.0053 (n=15), ITEM: média 0.1479 (n=14), MOVE_BENCH: média -0.0845 (n=40), MOVE_BOARD: média -0.0039 (n=39), PASS: média -0.0370 (n=20), REROLL: média -0.0700 (n=5), SELL: média -0.2459 (n=27)
| Jogador 2 | 210 | 45 | 17 | 21 | 9 | 27 | 83 | 0.0753 | 16 | 35 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 10, ALL_IN::ITEM: 1, ALL_IN::MOVE_BOARD: 1, ALL_IN::REROLL: 9, ALL_IN::SELL: 6, FAST8::BUY: 10, FAST8::BUY_XP: 16, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 28, FAST8::PASS: 10, FAST8::SELL: 3, LOSS_STREAK::BUY: 3, LOSS_STREAK::BUY_XP: 1, LOSS_STREAK::MOVE_BENCH: 2, LOSS_STREAK::MOVE_BOARD: 1, LOSS_STREAK::SELL: 3, STABILIZE::BUY: 22, STABILIZE::BUY_XP: 4, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 32, STABILIZE::PASS: 17, STABILIZE::SELL: 5
- Jogador 2 — recompensas por ação: BUY: média 0.5271 (n=45), BUY_XP: média -0.0286 (n=21), ITEM: média 0.1412 (n=8), MOVE_BENCH: média -0.0014 (n=21), MOVE_BOARD: média -0.0135 (n=62), PASS: média -0.0270 (n=27), REROLL: média -0.0700 (n=9), SELL: média -0.3647 (n=17)
| Jogador 3 | 138 | 33 | 9 | 0 | 5 | 14 | 70 | 0.0659 | 6 | 20 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 6, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 8, ALL_IN::PASS: 1, ALL_IN::REROLL: 5, ALL_IN::SELL: 5, LOSS_STREAK::BUY: 4, LOSS_STREAK::MOVE_BENCH: 5, LOSS_STREAK::PASS: 1, STABILIZE::BUY: 23, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 44, STABILIZE::MOVE_BOARD: 13, STABILIZE::PASS: 12, STABILIZE::SELL: 4
- Jogador 3 — recompensas por ação: BUY: média 0.6121 (n=33), ITEM: média 0.1557 (n=7), MOVE_BENCH: média -0.1321 (n=57), MOVE_BOARD: média -0.0115 (n=13), PASS: média -0.0536 (n=14), REROLL: média -0.0700 (n=5), SELL: média -0.3789 (n=9)
| Jogador 4 | 193 | 54 | 30 | 20 | 0 | 19 | 63 | 0.0750 | 11 | 41 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::MOVE_BOARD: 2, ALL_IN::PASS: 1, ALL_IN::SELL: 1, FAST8::BUY: 20, FAST8::BUY_XP: 5, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 5, FAST8::MOVE_BOARD: 24, FAST8::PASS: 12, FAST8::SELL: 10, STABILIZE::BUY: 32, STABILIZE::BUY_XP: 15, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 17, STABILIZE::MOVE_BOARD: 15, STABILIZE::PASS: 6, STABILIZE::SELL: 19
- Jogador 4 — recompensas por ação: BUY: média 0.3685 (n=54), BUY_XP: média -0.0120 (n=20), ITEM: média 0.1771 (n=7), MOVE_BENCH: média 0.1241 (n=22), MOVE_BOARD: média -0.0093 (n=41), PASS: média -0.0337 (n=19), SELL: média -0.2710 (n=30)
| Jogador 5 | 272 | 89 | 53 | 14 | 25 | 21 | 62 | 0.0925 | 15 | 36 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 25, ALL_IN::BUY_XP: 1, ALL_IN::ITEM: 1, ALL_IN::MOVE_BENCH: 1, ALL_IN::REROLL: 13, ALL_IN::SELL: 22, FAST8::BUY: 15, FAST8::ITEM: 2, FAST8::MOVE_BOARD: 12, FAST8::PASS: 6, FAST8::REROLL: 10, FAST8::SELL: 8, STABILIZE::BUY: 49, STABILIZE::BUY_XP: 13, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 38, STABILIZE::PASS: 15, STABILIZE::REROLL: 2, STABILIZE::SELL: 23
- Jogador 5 — recompensas por ação: BUY: média 0.4526 (n=89), BUY_XP: média 0.0300 (n=14), ITEM: média 0.1888 (n=8), MOVE_BENCH: média 0.2058 (n=12), MOVE_BOARD: média -0.0100 (n=50), PASS: média -0.0486 (n=21), REROLL: média -0.1508 (n=25), SELL: média -0.2683 (n=53)
| Jogador 6 | 198 | 53 | 20 | 5 | 7 | 20 | 82 | 0.1180 | 9 | 28 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 17, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 5, ALL_IN::MOVE_BOARD: 14, ALL_IN::PASS: 3, ALL_IN::REROLL: 7, ALL_IN::SELL: 9, FAST8::BUY: 5, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 4, FAST8::MOVE_BOARD: 14, FAST8::PASS: 6, FAST8::SELL: 3, STABILIZE::BUY: 31, STABILIZE::BUY_XP: 5, STABILIZE::ITEM: 6, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 30, STABILIZE::PASS: 11, STABILIZE::SELL: 8
- Jogador 6 — recompensas por ação: BUY: média 0.5096 (n=53), BUY_XP: média -0.0260 (n=5), ITEM: média 0.1773 (n=11), MOVE_BENCH: média 0.1138 (n=24), MOVE_BOARD: média -0.0088 (n=58), PASS: média -0.0770 (n=20), REROLL: média -0.0700 (n=7), SELL: média -0.2830 (n=20)
| Jogador 7 | 255 | 58 | 20 | 21 | 7 | 27 | 109 | 0.0982 | 29 | 54 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 11, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 3, ALL_IN::MOVE_BOARD: 4, ALL_IN::PASS: 2, ALL_IN::REROLL: 7, ALL_IN::SELL: 3, ECON::BUY: 10, ECON::BUY_XP: 1, ECON::ITEM: 5, ECON::MOVE_BENCH: 14, ECON::MOVE_BOARD: 10, ECON::PASS: 7, ECON::SELL: 5, FAST8::BUY: 18, FAST8::BUY_XP: 15, FAST8::ITEM: 3, FAST8::MOVE_BENCH: 7, FAST8::MOVE_BOARD: 39, FAST8::PASS: 14, FAST8::SELL: 5, STABILIZE::BUY: 19, STABILIZE::BUY_XP: 5, STABILIZE::ITEM: 2, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 18, STABILIZE::PASS: 4, STABILIZE::SELL: 7
- Jogador 7 — recompensas por ação: BUY: média 0.5565 (n=58), BUY_XP: média -0.0195 (n=21), ITEM: média 0.1292 (n=13), MOVE_BENCH: média 0.0497 (n=38), MOVE_BOARD: média -0.0103 (n=71), PASS: média -0.0867 (n=27), REROLL: média -0.0700 (n=7), SELL: média -0.3420 (n=20)
| Jogador 8 | 261 | 93 | 53 | 14 | 17 | 12 | 62 | 0.1072 | 16 | 26 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 60, ALL_IN::ITEM: 6, ALL_IN::MOVE_BENCH: 5, ALL_IN::MOVE_BOARD: 9, ALL_IN::OTHER: 1, ALL_IN::PASS: 2, ALL_IN::REROLL: 17, ALL_IN::SELL: 43, FAST8::BUY: 6, FAST8::BUY_XP: 6, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 8, FAST8::PASS: 3, FAST8::SELL: 4, LOSS_STREAK::BUY: 3, LOSS_STREAK::MOVE_BENCH: 5, LOSS_STREAK::PASS: 1, STABILIZE::BUY: 24, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 19, STABILIZE::PASS: 6, STABILIZE::SELL: 6
- Jogador 8 — recompensas por ação: BUY: média 0.5329 (n=93), BUY_XP: média -0.0329 (n=14), ITEM: média 0.1500 (n=9), MOVE_BENCH: média 0.0427 (n=26), MOVE_BOARD: média -0.0167 (n=36), OTHER: média 0.0000 (n=1), PASS: média -0.0642 (n=12), REROLL: média -0.0794 (n=17), SELL: média -0.3934 (n=53)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 12:47:30 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.5100 |  |
| Jogador 1 | ? | 12:47:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 12:47:37 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 1 | 1-1 | 12:47:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 1 | 1-1 | 12:47:38 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-1 | 12:47:39 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2100 |  |
| Jogador 1 | 1-1 | 12:47:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 1 | 1-1 | 12:47:40 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0200 |  |
| Jogador 1 | 1-1 | 12:47:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-1 | 12:47:42 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4300 |  |
| Jogador 1 | 1-2 | 12:47:44 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3500 |  |
| Jogador 1 | 1-2 | 12:47:45 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2600 |  |
| Jogador 1 | 1-2 | 12:47:45 | MOVE Board -> Board: Akali (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-2 | 12:47:45 | MOVE Board -> Board: Ornn (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 1 | 1-2 | 12:47:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-3 | 12:47:52 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 12:47:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 12:48:00 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 1.0200 |  |
| Jogador 1 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 1 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 1 | 1-4 | 12:48:02 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 1-4 | 12:48:02 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 1-4 | 12:48:03 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 12:48:04 | MOVE Board -> Board: Leona (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-1 | 12:48:10 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | 0.3700 |  |
| Jogador 1 | 2-1 | 12:48:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 12:48:11 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-1 | 12:48:11 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.5400 |  |
| Jogador 1 | 2-1 | 12:48:12 | MOVE Board -> Board: Diana (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 12:48:13 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 12:48:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-2 | 12:48:21 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Diana | 0.3600 |  |
| Jogador 1 | 2-2 | 12:48:22 | MOVE Bench -> Board: Shen (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Diana | 0.0900 |  |
| Jogador 1 | 2-2 | 12:48:22 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | 0.3100 |  |
| Jogador 1 | 2-2 | 12:48:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-2 | 12:48:23 | MOVE Board -> Board: Akali (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-2 | 12:48:24 | MOVE Board -> Board: Diana (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-2 | 12:48:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-3 | 12:48:33 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Diana | 1.0300 |  |
| Jogador 1 | 2-3 | 12:48:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-3 | 12:48:34 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3800 |  |
| Jogador 1 | 2-3 | 12:48:35 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Diana | 0.2200 |  |
| Jogador 1 | 2-3 | 12:48:36 | MOVE Board -> Board: Leona (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-3 | 12:48:36 | MOVE Board -> Board: Akali (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Diana | -0.0300 |  |
| Jogador 1 | 2-3 | 12:48:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-4 | 12:48:47 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Diana | 0.8800 |  |
| Jogador 1 | 2-4 | 12:48:48 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Diana | 0.0700 |  |
| Jogador 1 | 2-4 | 12:48:48 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Diana | -0.6300 |  |
| Jogador 1 | 2-4 | 12:48:49 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Shen (i:4.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Diana | 0.1200 |  |
| Jogador 1 | 2-4 | 12:48:49 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Shen (i:4.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Diana | 0.1300 |  |
| Jogador 1 | 2-4 | 12:48:49 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Diana | -0.7600 |  |
| Jogador 1 | 2-4 | 12:48:50 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-4 | 12:48:51 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-4 | 12:48:51 | MOVE Bench -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Diana | -0.4000 |  |
| Jogador 1 | 2-5 | 12:49:02 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | 0.9000 |  |
| Jogador 1 | 2-5 | 12:49:02 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | 0.9500 |  |
| Jogador 1 | 2-5 | 12:49:03 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | 0.1100 |  |
| Jogador 1 | 2-5 | 12:49:04 | MOVE Bench -> Board: Diana (i:6.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | -0.3500 |  |
| Jogador 1 | 2-5 | 12:49:04 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | -0.3500 |  |
| Jogador 1 | 2-5 | 12:49:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 12:49:18 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Akali_AD | -0.0700 |  |
| Jogador 1 | 2-6 | 12:49:19 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Inferno | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 1 | 2-6 | 12:49:20 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 1 | 2-6 | 12:49:20 | MOVE Bench -> Board: Varus (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.6500 |  |
| Jogador 1 | 2-6 | 12:49:20 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.6400 |  |
| Jogador 1 | 2-6 | 12:49:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 12:49:35 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Inferno | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 2-7 | 12:49:36 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Inferno | DA_KogMaw18_AD | 0.5600 |  |
| Jogador 1 | 2-7 | 12:49:36 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | 0.4700 |  |
| Jogador 1 | 2-7 | 12:49:37 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | -0.3800 |  |
| Jogador 1 | 2-7 | 12:49:37 | MOVE Bench -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 1 | 2-7 | 12:49:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-1 | 12:49:53 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 12:49:53 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Inferno | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 1 | 3-1 | 12:49:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 12:49:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 12:49:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 1 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 3-1 | 12:49:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 12:49:56 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 12:49:56 | MOVE Board -> Board: Leona (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 12:49:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-2 | 12:50:12 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 3-2 | 12:50:12 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.7000 |  |
| Jogador 1 | 3-2 | 12:50:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 12:50:13 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 12:50:13 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 1 | 3-2 | 12:50:14 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.5200 |  |
| Jogador 1 | 3-2 | 12:50:14 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.1300 |  |
| Jogador 1 | 3-2 | 12:50:15 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 1 | 3-2 | 12:50:15 | MOVE Bench -> Board: Varus (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 3-3 | 12:50:31 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 1 | 3-3 | 12:50:32 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 3-3 | 12:50:32 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-3 | 12:50:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 12:50:33 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 12:50:34 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 1 | 3-3 | 12:50:34 | MOVE Board -> Board: Rakan (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 12:50:35 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.2700 |  |
| Jogador 1 | 3-3 | 12:50:35 | MOVE Board -> Board: Varus (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 3-4 | 12:50:53 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 3-4 | 12:50:54 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Shen | 0.8400 |  |
| Jogador 1 | 3-4 | 12:50:54 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Shen | 0.1500 |  |
| Jogador 1 | 3-4 | 12:50:55 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Shen | 0.2900 |  |
| Jogador 1 | 3-4 | 12:50:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 3-4 | 12:50:56 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | 0.3500 |  |
| Jogador 1 | 3-4 | 12:50:57 | MOVE Board -> Board: Cascalho (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-4 | 12:50:57 | MOVE Board -> Board: Rakan (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | -0.0400 |  |
| Jogador 1 | 3-4 | 12:50:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-5 | 12:51:18 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Shen | 0.2900 |  |
| Jogador 1 | 3-5 | 12:51:18 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-5 | 12:51:19 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | 0.0800 |  |
| Jogador 1 | 3-5 | 12:51:20 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | 0.0200 |  |
| Jogador 1 | 3-5 | 12:51:20 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 3-5 | 12:51:20 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 3-5 | 12:51:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-6 | 12:51:44 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 1 | 3-6 | 12:51:44 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 1 | 3-6 | 12:51:45 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Varus (i:2.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 1 | 3-6 | 12:51:45 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Varus (i:2.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 1 | 3-6 | 12:51:46 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Varus (i:2.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 1 | 3-6 | 12:51:46 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | -0.3900 |  |
| Jogador 1 | 3-6 | 12:51:47 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.7200 |  |
| Jogador 1 | 3-6 | 12:51:47 | MOVE Bench -> Board: Akali (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-6 | 12:51:47 | MOVE Bench -> Board: Leona (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.4600 |  |
| Jogador 1 | 3-7 | 12:52:11 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 1 | 3-7 | 12:52:12 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 1 | 3-7 | 12:52:12 | MOVE Bench -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | -0.6400 |  |
| Jogador 1 | 3-7 | 12:52:13 | MOVE Bench -> Board: Akali (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 1 | 3-7 | 12:52:13 | MOVE Bench -> Board: Leona (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | -0.7600 |  |
| Jogador 1 | 3-7 | 12:52:14 | MOVE Bench -> Board: Rakan (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 3-7 | 12:52:14 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 1 | 3-7 | 12:52:15 | MOVE Bench -> Board: Leona (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | -0.7500 |  |
| Jogador 1 | 3-7 | 12:52:15 | MOVE Bench -> Board: Akali (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 4-1 | 12:52:43 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 12:52:44 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Inferno | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 1 | 4-1 | 12:52:44 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Inferno | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 1 | 4-1 | 12:52:45 | MOVE Board -> Board: Akali (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-1 | 12:52:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Inferno | DA_KogMaw18_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-2 | 12:53:13 | MOVE Bench -> Board: Rakan (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Inferno | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 1 | 4-2 | 12:53:13 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 4-2 | 12:53:14 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Inferno | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 1 | 4-2 | 12:53:14 | MOVE Board -> Board: Rakan (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-2 | 12:53:15 | MOVE Board -> Board: Leona (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-2 | 12:53:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Inferno | DA_KogMaw18_AD | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-3 | 12:53:46 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Inferno | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 4-3 | 12:53:46 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Inferno | DA_Fiddlesticks18 | 0.8400 |  |
| Jogador 1 | 4-3 | 12:53:47 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Inferno | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 1 | 4-3 | 12:53:47 | MOVE Bench -> Board: Fiddlesticks (i:12.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Inferno | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 1 | 4-3 | 12:53:48 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Inferno | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 1 | 4-3 | 12:53:48 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Inferno | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 1 | 4-3 | 12:53:49 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Inferno | DA_Fiddlesticks18 | -0.1900 |  |
| Jogador 1 | 4-4 | 12:54:19 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Inferno | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 1 | 4-4 | 12:54:20 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 4-4 | 12:54:20 | MOVE Board -> Board: Akali (i:2.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 4-4 | 12:54:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Inferno | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 1 | 4-5 | 12:54:52 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Inferno | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 1 | 4-5 | 12:54:53 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Inferno | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 1 | 4-5 | 12:54:53 | MOVE Bench -> Board: Rakan (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Inferno | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 1 | 4-5 | 12:54:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Inferno | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 1 | 4-6 | 12:55:30 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 4 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 4-6 | 12:55:30 | COMPROU: Leona (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Inferno | DA_Fiddlesticks18 | 0.3600 |  |
| Jogador 1 | 4-6 | 12:55:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 4-6 | 12:55:31 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 4-6 | 12:55:32 | MOVE Board -> Board: Leona (i:2.0) <-> Fiddlesticks (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 4-6 | 12:55:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Inferno | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 1 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Fiddlesticks (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Inferno | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 1 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Fiddlesticks (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Inferno | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 1 | 4-7 | 12:56:07 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 4-7 | 12:56:07 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Inferno | DA_Fiddlesticks18 | 0.9500 |  |
| Jogador 1 | 4-7 | 12:56:08 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_Fiddlesticks18 | 0.1500 |  |
| Jogador 1 | 4-7 | 12:56:08 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 4-7 | 12:56:08 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 1 | 4-7 | 12:56:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_Fiddlesticks18 | -0.2700 |  |
| Jogador 1 | 5-1 | 12:56:41 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Inferno | DA_Fiddlesticks18 | 0.8300 |  |
| Jogador 1 | 5-1 | 12:56:41 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Inferno | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 1 | 5-1 | 12:56:42 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 84 | 5 | Inferno | DA_Fiddlesticks18 | 0.8200 |  |
| Jogador 1 | 5-1 | 12:56:42 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 84 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 5-1 | 12:56:43 | VENDEU: Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Inferno | DA_Fiddlesticks18 | -0.4400 |  |
| Jogador 1 | 5-1 | 12:56:43 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Inferno | DA_Fiddlesticks18 | 0.3700 |  |
| Jogador 1 | 5-1 | 12:56:44 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Inferno | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 1 | 5-1 | 12:56:45 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Inferno | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 1 | 5-1 | 12:56:45 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Inferno | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 1 | 5-2 | 12:57:20 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Inferno | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 1 | 5-2 | 12:57:20 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Inferno | DA_Fiddlesticks18 | 1.0500 |  |
| Jogador 1 | 5-2 | 12:57:21 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Inferno | DA_Fiddlesticks18 | 0.4300 |  |
| Jogador 1 | 5-2 | 12:57:21 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Inferno | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 1 | 5-2 | 12:57:22 | MOVE Bench -> Board: Amumu (i:8.0) <-> Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Inferno | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 1 | 5-2 | 12:57:22 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Inferno | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 1 | 5-2 | 12:57:23 | VENDEU: Akali (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Inferno | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 1 | 5-2 | 12:57:23 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Inferno | DA_Fiddlesticks18 | 0.9600 |  |
| Jogador 1 | 5-2 | 12:57:23 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Leona (i:2.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Inferno | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 1 | 5-3 | 12:57:58 | EQUIP_FROM_INVENTORY: TFT_Item_RapidFireCannon -> Fiddlesticks (i:12.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Inferno | DA_Fiddlesticks18 | 0.1300 |  |
| Jogador 1 | 5-3 | 12:57:58 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 5-3 | 12:57:59 | COMPROU: Lux (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Inferno | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 1 | 5-3 | 12:57:59 | VENDEU: Nidalee (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 1 | 5-3 | 12:58:00 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Inferno | DA_Fiddlesticks18 | 0.1500 |  |
| Jogador 1 | 5-3 | 12:58:00 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Inferno | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 1 | 5-3 | 12:58:01 | VENDEU: Kayle (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Inferno | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 1 | 5-3 | 12:58:01 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Inferno | DA_Fiddlesticks18 | 1.0800 |  |
| Jogador 1 | 5-3 | 12:58:01 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Inferno | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 1 | 5-4 | 12:58:37 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Inferno | DA_18_Diana | 0.4700 |  |
| Jogador 1 | 5-4 | 12:58:38 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Inferno | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 1 | 5-4 | 12:58:38 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Inferno | DA_Fiddlesticks18 | 0.5000 |  |
| Jogador 1 | 5-4 | 12:58:39 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Inferno | DA_Fiddlesticks18 | 0.1500 |  |
| Jogador 1 | 5-4 | 12:58:39 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Inferno | DA_Fiddlesticks18 | 0.1500 |  |
| Jogador 1 | 5-4 | 12:58:39 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Inferno | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 1 | 5-4 | 12:58:40 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 1 | 5-4 | 12:58:41 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Inferno | DA_Fiddlesticks18 | 0.9600 |  |
| Jogador 1 | 5-4 | 12:58:41 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Inferno | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 1 | 5-5 | 12:59:18 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Inferno | DA_Fiddlesticks18 | -0.4400 |  |
| Jogador 1 | 5-5 | 12:59:19 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Inferno | DA_Fiddlesticks18 | 1.0900 |  |
| Jogador 1 | 5-5 | 12:59:19 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Inferno | DA_Fiddlesticks18 | 0.4700 |  |
| Jogador 1 | 5-5 | 12:59:20 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Inferno | DA_Fiddlesticks18 | 0.4800 |  |
| Jogador 1 | 5-5 | 12:59:20 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Inferno | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 1 | 5-5 | 12:59:21 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Inferno | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 1 | 5-5 | 12:59:21 | VENDEU: Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Inferno | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 1 | 5-5 | 12:59:21 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 99 | 5 | Inferno | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 1 | 5-5 | 12:59:22 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Inferno | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 2 | ? | 12:47:30 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | ? | 12:47:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 12:47:37 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 12:47:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 12:47:38 | MOVE Bench -> Board: Rakan (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 1-1 | 12:47:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 12:47:42 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 1-2 | 12:47:44 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 12:47:45 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 12:47:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 12:47:49 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 12:47:52 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 12:47:52 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 12:47:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 1-3 | 12:47:53 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.4900 |  |
| Jogador 2 | 1-3 | 12:47:54 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 12:47:54 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 12:47:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 12:48:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-4 | 12:48:02 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.4500 |  |
| Jogador 2 | 1-4 | 12:48:02 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 1-4 | 12:48:03 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 12:48:04 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-1 | 12:48:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 2-1 | 12:48:10 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 12:48:11 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Veigar | -0.4200 |  |
| Jogador 2 | 2-1 | 12:48:11 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 2-1 | 12:48:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 12:48:13 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 2-1 | 12:48:14 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-1 | 12:48:14 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-1 | 12:48:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 12:48:21 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.3400 |  |
| Jogador 2 | 2-2 | 12:48:22 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-2 | 12:48:22 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 2-2 | 12:48:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-2 | 12:48:23 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 2-2 | 12:48:24 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-2 | 12:48:24 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.3100 |  |
| Jogador 2 | 2-2 | 12:48:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 12:48:33 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 4 | 0 | — | DA_18_Veigar | 0.2800 |  |
| Jogador 2 | 2-3 | 12:48:34 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 1 | 0 | — | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 2-3 | 12:48:34 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 12:48:35 | VENDEU: LeBlanc (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 3 | 0 | — | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-3 | 12:48:36 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Veigar (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 3 | 0 | — | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 2-3 | 12:48:36 | VENDEU: Veigar (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 6 | 0 | — | DA_Fiddlesticks18 | -0.6300 |  |
| Jogador 2 | 2-3 | 12:48:37 | BUY XP | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 2 | 0 | — | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 2 | 2-3 | 12:48:37 | VENDEU: Veigar (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 3 | 0 | — | DA_Fiddlesticks18 | -0.6500 |  |
| Jogador 2 | 2-3 | 12:48:38 | MOVE Bench -> Board: Veigar (i:2.0) <-> Kha'Zix (i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 3 | 0 | — | DA_Fiddlesticks18 | -0.2500 |  |
| Jogador 2 | 2-4 | 12:48:47 | COMPROU: Tristana (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 6 | 0 | Feérico | DA_18_Tristana | 0.3100 |  |
| Jogador 2 | 2-4 | 12:48:48 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Tristana | -0.3900 |  |
| Jogador 2 | 2-4 | 12:48:48 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Tristana | -0.1300 |  |
| Jogador 2 | 2-4 | 12:48:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 2-5 | 12:49:02 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | 0.6300 |  |
| Jogador 2 | 2-5 | 12:49:02 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | -0.7800 |  |
| Jogador 2 | 2-5 | 12:49:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 2 | 2-5 | 12:49:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | 0.0300 |  |
| Jogador 2 | 2-5 | 12:49:04 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | 0.5400 |  |
| Jogador 2 | 2-5 | 12:49:05 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 2 | 2-5 | 12:49:05 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 2-5 | 12:49:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 2-6 | 12:49:18 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Lillia | 0.3600 |  |
| Jogador 2 | 2-6 | 12:49:19 | MOVE Bench -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Lillia | 0.1000 |  |
| Jogador 2 | 2-6 | 12:49:20 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Lillia | -0.1200 |  |
| Jogador 2 | 2-6 | 12:49:20 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Lillia | -0.7700 |  |
| Jogador 2 | 2-6 | 12:49:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 2-7 | 12:49:35 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Lillia | 0.1800 |  |
| Jogador 2 | 2-7 | 12:49:36 | MOVE Bench -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Lillia | 0.1100 |  |
| Jogador 2 | 2-7 | 12:49:36 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Lillia | -0.1200 |  |
| Jogador 2 | 2-7 | 12:49:37 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Feérico | DA_18_Lillia | -0.7500 |  |
| Jogador 2 | 2-7 | 12:49:37 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-1 | 12:49:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Feérico | DA_18_Lillia | 0.2200 |  |
| Jogador 2 | 3-1 | 12:49:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Feérico | DA_18_Lillia | 0.7400 |  |
| Jogador 2 | 3-1 | 12:49:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Feérico | DA_18_Lillia | -0.0900 |  |
| Jogador 2 | 3-1 | 12:49:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-1 | 12:49:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-1 | 12:49:56 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-1 | 12:49:56 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-1 | 12:49:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-2 | 12:50:12 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_Lillia | 0.7300 |  |
| Jogador 2 | 3-2 | 12:50:12 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-2 | 12:50:12 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-2 | 12:50:13 | MOVE Board -> Board: Lillia (i:8.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-2 | 12:50:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-3 | 12:50:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-3 | 12:50:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-3 | 12:50:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-3 | 12:50:33 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-3 | 12:50:33 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Lillia | -0.0200 |  |
| Jogador 2 | 3-3 | 12:50:34 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-3 | 12:50:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-4 | 12:50:53 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_Lillia | 0.0600 |  |
| Jogador 2 | 3-4 | 12:50:54 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Feérico | DA_18_Lillia | 0.0300 |  |
| Jogador 2 | 3-4 | 12:50:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 3-4 | 12:50:55 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-4 | 12:50:56 | MOVE Board -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-4 | 12:50:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-5 | 12:51:18 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Feérico | DA_18_Lillia | 0.6500 |  |
| Jogador 2 | 3-5 | 12:51:18 | MOVE Board -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-5 | 12:51:19 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Feérico | DA_18_Lillia | -0.0200 |  |
| Jogador 2 | 3-5 | 12:51:20 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-5 | 12:51:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-6 | 12:51:44 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Feérico | DA_18_Tristana | 0.7600 |  |
| Jogador 2 | 3-6 | 12:51:44 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Feérico | DA_18_Tristana | -0.1100 |  |
| Jogador 2 | 3-6 | 12:51:45 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 2 | 3-6 | 12:51:45 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 3-6 | 12:51:46 | VENDEU: Tristana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Feérico | DA_18_Lillia | -0.5400 |  |
| Jogador 2 | 3-6 | 12:51:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Feérico | DA_18_Lillia | -0.1100 |  |
| Jogador 2 | 3-6 | 12:51:47 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 3-6 | 12:51:47 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-6 | 12:51:47 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-7 | 12:52:11 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_Lillia | 0.7300 |  |
| Jogador 2 | 3-7 | 12:52:12 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_Lillia | 0.1300 |  |
| Jogador 2 | 3-7 | 12:52:12 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_Lillia | 0.1100 |  |
| Jogador 2 | 3-7 | 12:52:13 | MOVE Board -> Board: Veigar (i:2.0) <-> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 3-7 | 12:52:13 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-7 | 12:52:14 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-7 | 12:52:14 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-1 | 12:52:43 | MOVE Board -> Board: Rakan (i:2.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-1 | 12:52:44 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-1 | 12:52:44 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-2 | 12:53:13 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Feérico | DA_18_Lillia | 0.2100 |  |
| Jogador 2 | 4-2 | 12:53:13 | MOVE Board -> Board: Lillia (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-2 | 12:53:14 | MOVE Board -> Board: Lillia (i:8.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Feérico | DA_18_Lillia | -0.0200 |  |
| Jogador 2 | 4-2 | 12:53:14 | MOVE Board -> Board: Veigar (i:2.0) <-> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-2 | 12:53:15 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-3 | 12:53:46 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Feérico | DA_18_Lillia | -0.1600 |  |
| Jogador 2 | 4-3 | 12:53:46 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-3 | 12:53:47 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Feérico | DA_18_Lillia | -0.0200 |  |
| Jogador 2 | 4-3 | 12:53:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Feérico | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 4-4 | 12:54:19 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-4 | 12:54:20 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Feérico | DA_18_Lillia | 0.7600 |  |
| Jogador 2 | 4-4 | 12:54:20 | MOVE Board -> Board: Rakan (i:2.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-4 | 12:54:21 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Feérico | DA_18_Lillia | 0.0100 |  |
| Jogador 2 | 4-4 | 12:54:21 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Feérico | DA_18_Lillia | -0.0700 |  |
| Jogador 2 | 4-4 | 12:54:21 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Feérico | DA_18_Lillia | 0.0100 |  |
| Jogador 2 | 4-4 | 12:54:22 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 1 | Feérico | DA_18_Lillia | -0.0700 |  |
| Jogador 2 | 4-4 | 12:54:22 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 1 | Feérico | DA_18_Lillia | 0.0100 |  |
| Jogador 2 | 4-4 | 12:54:23 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 1 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-5 | 12:54:52 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Feérico | DA_18_Lillia | -0.5300 |  |
| Jogador 2 | 4-5 | 12:54:53 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Feérico | DA_18_Rakan | 0.8400 |  |
| Jogador 2 | 4-5 | 12:54:53 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Feérico | DA_18_Rakan | 0.3000 |  |
| Jogador 2 | 4-5 | 12:54:54 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Feérico | DA_18_Rakan | 0.8400 |  |
| Jogador 2 | 4-5 | 12:54:54 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Feérico | DA_18_Rakan | -0.2300 |  |
| Jogador 2 | 4-5 | 12:54:55 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Feérico | DA_18_Veigar | 0.3800 |  |
| Jogador 2 | 4-5 | 12:54:55 | MOVE Board -> Board: Veigar (i:4.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-5 | 12:54:56 | MOVE Board -> Board: Lillia (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-5 | 12:54:56 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Feérico | DA_18_Veigar | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-6 | 12:55:30 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Feérico | DA_18_Veigar | 0.2800 |  |
| Jogador 2 | 4-6 | 12:55:30 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-6 | 12:55:31 | MOVE Board -> Board: Veigar (i:4.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-6 | 12:55:31 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Feérico | DA_18_Veigar | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-7 | 12:56:06 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Feérico | DA_18_Veigar | 0.3500 |  |
| Jogador 2 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Feérico | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 4-7 | 12:56:07 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Feérico | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 4-7 | 12:56:07 | MOVE Board -> Board: Shen (i:4.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 2 | 4-7 | 12:56:08 | MOVE Board -> Board: Veigar (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-7 | 12:56:08 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Feérico | DA_18_Veigar | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-1 | 12:56:41 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 24 | 2 | Feérico | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 5-1 | 12:56:41 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 24 | 2 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-1 | 12:56:42 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 24 | 2 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-1 | 12:56:42 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 24 | 2 | Feérico | DA_18_Veigar | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-2 | 12:57:20 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-2 | 12:57:20 | MOVE Board -> Board: Lillia (i:8.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-2 | 12:57:21 | MOVE Board -> Board: Veigar (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-2 | 12:57:21 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Feérico | DA_18_Veigar | -0.0700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-3 | 12:57:58 | MOVE Board -> Board: Shen (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-3 | 12:57:58 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 5-3 | 12:57:59 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Feérico | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 5-3 | 12:57:59 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-3 | 12:58:00 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-3 | 12:58:00 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-3 | 12:58:01 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Feérico | DA_18_Veigar | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-4 | 12:58:37 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 56 | 4 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-4 | 12:58:38 | MOVE Board -> Board: Veigar (i:4.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 56 | 4 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-4 | 12:58:38 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 56 | 4 | Feérico | DA_18_Veigar | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-5 | 12:59:18 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Feérico | DA_18_Veigar | -0.4500 |  |
| Jogador 2 | 5-5 | 12:59:19 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Veigar | 0.3500 |  |
| Jogador 2 | 5-5 | 12:59:19 | MOVE Board -> Board: Rakan (i:4.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-5 | 12:59:20 | MOVE Board -> Board: Lillia (i:8.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-5 | 12:59:20 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_18_Veigar | -0.1400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-6 | 13:00:00 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-6 | 13:00:01 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Feérico | DA_18_Veigar | 0.9300 |  |
| Jogador 2 | 5-6 | 13:00:01 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 5-6 | 13:00:02 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 5-6 | 13:00:02 | MOVE Board -> Board: Shen (i:4.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-6 | 13:00:03 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 5-6 | 13:00:03 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 5-6 | 13:00:03 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 5-6 | 13:00:04 | VENDEU: Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Feérico | DA_18_Rakan | -0.5900 |  |
| Jogador 2 | 5-7 | 13:00:42 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Feérico | DA_18_Rakan | 0.4200 |  |
| Jogador 2 | 5-7 | 13:00:42 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Kha'Zix (i:6.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Feérico | DA_18_Rakan | 0.0700 |  |
| Jogador 2 | 5-7 | 13:00:43 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Feérico | DA_18_Rakan | -0.0700 |  |
| Jogador 2 | 5-7 | 13:00:43 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Feérico | DA_18_Rakan | -0.4200 |  |
| Jogador 2 | 5-7 | 13:00:44 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Feérico | DA_18_Rakan | 1.1100 |  |
| Jogador 2 | 5-7 | 13:00:44 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Feérico | DA_18_Xayah | 0.5200 |  |
| Jogador 2 | 5-7 | 13:00:44 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Feérico | DA_18_Xayah | -0.0700 |  |
| Jogador 2 | 5-7 | 13:00:45 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Feérico | DA_18_Xayah | 0.9900 |  |
| Jogador 2 | 5-7 | 13:00:45 | VENDEU: Xayah (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Feérico | DA_18_Rakan | -0.5900 |  |
| Jogador 2 | 6-1 | 13:01:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Feérico | DA_18_Rakan | 0.5600 |  |
| Jogador 2 | 6-1 | 13:01:25 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Feérico | DA_18_Rakan | -0.0700 |  |
| Jogador 2 | 6-1 | 13:01:25 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Feérico | DA_18_Rakan | -0.5900 |  |
| Jogador 2 | 6-1 | 13:01:26 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Feérico | DA_18_Tristana | 1.1100 |  |
| Jogador 2 | 6-1 | 13:01:26 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Feérico | DA_18_Tristana | 0.9700 |  |
| Jogador 2 | 6-1 | 13:01:26 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Feérico | DA_18_Tristana | 0.6900 |  |
| Jogador 2 | 6-1 | 13:01:27 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 69 | 5 | Feérico | DA_18_Tristana | -0.0700 |  |
| Jogador 2 | 6-1 | 13:01:27 | VENDEU: Tristana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Feérico | DA_18_Rakan | -0.6000 |  |
| Jogador 2 | 6-1 | 13:01:28 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Feérico | DA_18_Shen | 1.0500 |  |
| Jogador 3 | ? | 12:47:30 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | ? | 12:47:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 12:47:37 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 12:47:38 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 12:47:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 12:47:42 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 1-2 | 12:47:44 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 12:47:45 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 12:47:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 12:47:49 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 1-3 | 12:47:52 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | 1-3 | 12:47:52 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 1-3 | 12:47:53 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 12:47:53 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 12:47:54 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 12:47:54 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 12:47:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 12:48:00 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0200 |  |
| Jogador 3 | 1-4 | 12:48:01 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 12:48:02 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 12:48:02 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 12:48:03 | MOVE Board -> Board: Camille (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-4 | 12:48:04 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-1 | 12:48:10 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Scuttlecrab18 | 1.1100 |  |
| Jogador 3 | 2-1 | 12:48:10 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | 0.3400 |  |
| Jogador 3 | 2-1 | 12:48:11 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 3 | 2-1 | 12:48:11 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | -0.7300 |  |
| Jogador 3 | 2-1 | 12:48:12 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 2-1 | 12:48:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-2 | 12:48:21 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Scuttlecrab18 | 0.3200 |  |
| Jogador 3 | 2-2 | 12:48:22 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Scuttlecrab18 | 0.2400 |  |
| Jogador 3 | 2-2 | 12:48:22 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | 0.1400 |  |
| Jogador 3 | 2-2 | 12:48:23 | MOVE Board -> Board: Camille (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-2 | 12:48:23 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 2-2 | 12:48:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-3 | 12:48:33 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 5 | 0 | — | DA_Scuttlecrab18 | 0.6900 |  |
| Jogador 3 | 2-3 | 12:48:34 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 4 | 0 | — | DA_Scuttlecrab18 | 0.8600 |  |
| Jogador 3 | 2-3 | 12:48:34 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 4 | 0 | — | DA_Scuttlecrab18 | 0.6400 |  |
| Jogador 3 | 2-3 | 12:48:35 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 1 | 0 | — | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 2-3 | 12:48:36 | MOVE Bench -> Board: Rakan (i:2.0) <-> Akali (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 1 | 0 | — | DA_Scuttlecrab18 | -0.7500 |  |
| Jogador 3 | 2-3 | 12:48:36 | MOVE Bench -> Board: Akali (i:4.0) <-> Camille (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 1 | 0 | — | DA_Scuttlecrab18 | 0.1100 |  |
| Jogador 3 | 2-3 | 12:48:37 | MOVE Bench -> Board: Camille (i:2.0) <-> Rakan (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 1 | 0 | — | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 3 | 2-3 | 12:48:37 | MOVE Bench -> Board: Rakan (i:2.0) <-> Akali (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 1 | 0 | — | DA_Scuttlecrab18 | -0.7600 |  |
| Jogador 3 | 2-3 | 12:48:38 | PASSOU TURNO | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 1 | 0 | — | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-4 | 12:48:47 | COMPROU: Yorick (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 6 | 0 | Colosso | DA_Scuttlecrab18 | 0.8200 |  |
| Jogador 3 | 2-4 | 12:48:48 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_Scuttlecrab18 | -0.0600 |  |
| Jogador 3 | 2-4 | 12:48:48 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Scuttlecrab18 | 0.8100 |  |
| Jogador 3 | 2-4 | 12:48:49 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 2-4 | 12:48:49 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_Scuttlecrab18 | -0.5000 |  |
| Jogador 3 | 2-4 | 12:48:49 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Scuttlecrab18 | 0.9300 |  |
| Jogador 3 | 2-4 | 12:48:50 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Kha'Zix (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 2-4 | 12:48:51 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Kha'Zix (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 2-4 | 12:48:51 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_Scuttlecrab18 | 0.2100 |  |
| Jogador 3 | 2-5 | 12:49:02 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_Scuttlecrab18 | 0.9500 |  |
| Jogador 3 | 2-5 | 12:49:02 | MOVE Bench -> Board: Tristana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 2-5 | 12:49:03 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 2-5 | 12:49:04 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Scuttlecrab18 | 0.3300 |  |
| Jogador 3 | 2-5 | 12:49:04 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 3 | 2-5 | 12:49:05 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Scuttlecrab18 | -0.1800 |  |
| Jogador 3 | 2-5 | 12:49:05 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 2-5 | 12:49:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Scuttlecrab18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 2-6 | 12:49:18 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Colosso | DA_Scuttlecrab18 | 0.9000 |  |
| Jogador 3 | 2-6 | 12:49:19 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_Scuttlecrab18 | 0.1700 |  |
| Jogador 3 | 2-6 | 12:49:20 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 2-6 | 12:49:20 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 2-6 | 12:49:20 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 2-6 | 12:49:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_Scuttlecrab18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 2-7 | 12:49:35 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_Scuttlecrab18 | 0.1900 |  |
| Jogador 3 | 2-7 | 12:49:36 | MOVE Bench -> Board: Camille (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_Scuttlecrab18 | -0.4000 |  |
| Jogador 3 | 2-7 | 12:49:36 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_Scuttlecrab18 | -0.5400 |  |
| Jogador 3 | 2-7 | 12:49:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_Scuttlecrab18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-1 | 12:49:53 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_Scuttlecrab18 | 0.1000 |  |
| Jogador 3 | 3-1 | 12:49:53 | MOVE Bench -> Board: Camille (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_Scuttlecrab18 | -0.4100 |  |
| Jogador 3 | 3-1 | 12:49:54 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_Scuttlecrab18 | -0.5400 |  |
| Jogador 3 | 3-1 | 12:49:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_Scuttlecrab18 | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-2 | 12:50:12 | MOVE Bench -> Board: Tristana (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_Scuttlecrab18 | -0.6100 |  |
| Jogador 3 | 3-2 | 12:50:12 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_Scuttlecrab18 | 0.0400 |  |
| Jogador 3 | 3-2 | 12:50:12 | MOVE Bench -> Board: Camille (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_Scuttlecrab18 | 0.1300 |  |
| Jogador 3 | 3-2 | 12:50:13 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_Scuttlecrab18 | -0.2100 |  |
| Jogador 3 | 3-2 | 12:50:13 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_Scuttlecrab18 | 0.0900 |  |
| Jogador 3 | 3-2 | 12:50:14 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_Scuttlecrab18 | -0.4000 |  |
| Jogador 3 | 3-2 | 12:50:14 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_Scuttlecrab18 | -0.5200 |  |
| Jogador 3 | 3-2 | 12:50:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_Scuttlecrab18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-3 | 12:50:31 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_Scuttlecrab18 | 0.1000 |  |
| Jogador 3 | 3-3 | 12:50:32 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_Scuttlecrab18 | -0.4100 |  |
| Jogador 3 | 3-3 | 12:50:32 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_Scuttlecrab18 | 0.0400 |  |
| Jogador 3 | 3-3 | 12:50:33 | MOVE Bench -> Board: Rakan (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 3 | 3-3 | 12:50:33 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_Scuttlecrab18 | -0.4200 |  |
| Jogador 3 | 3-3 | 12:50:34 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 3 | 3-3 | 12:50:34 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 3-3 | 12:50:35 | MOVE Bench -> Board: Rakan (i:2.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 3-3 | 12:50:35 | MOVE Bench -> Board: Camille (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_Scuttlecrab18 | 0.1000 |  |
| Jogador 3 | 3-4 | 12:50:53 | MOVE Bench -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Scuttlecrab18 | -0.9400 |  |
| Jogador 3 | 3-4 | 12:50:54 | MOVE Bench -> Board: Rakan (i:2.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 3 | 3-4 | 12:50:54 | MOVE Bench -> Board: Camille (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Scuttlecrab18 | 0.2500 |  |
| Jogador 3 | 3-4 | 12:50:55 | MOVE Bench -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Scuttlecrab18 | -0.8300 |  |
| Jogador 3 | 3-4 | 12:50:56 | MOVE Bench -> Board: Rakan (i:2.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 3-4 | 12:50:56 | MOVE Bench -> Board: Camille (i:4.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Scuttlecrab18 | -0.4500 |  |
| Jogador 3 | 3-4 | 12:50:57 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Scuttlecrab18 | 0.1400 |  |
| Jogador 3 | 3-4 | 12:50:57 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Scuttlecrab18 | -0.4300 |  |
| Jogador 3 | 3-4 | 12:50:57 | MOVE Bench -> Board: Rakan (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 3 | 3-5 | 12:51:18 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Colosso | DA_18_Yorick | -0.6000 |  |
| Jogador 3 | 3-5 | 12:51:18 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Colosso | DA_18_Yorick | 0.3200 |  |
| Jogador 3 | 3-5 | 12:51:19 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Colosso | DA_18_Camille | -0.5900 |  |
| Jogador 3 | 3-5 | 12:51:20 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Colosso | DA_18_Camille | 0.8800 |  |
| Jogador 3 | 3-5 | 12:51:20 | MOVE Bench -> Board: Camille (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Colosso | DA_18_Camille | -0.3700 |  |
| Jogador 3 | 3-5 | 12:51:20 | MOVE Bench -> Board: Rakan (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Colosso | DA_18_Camille | 0.2100 |  |
| Jogador 3 | 3-5 | 12:51:21 | MOVE Bench -> Board: Tristana (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Colosso | DA_18_Camille | -0.5400 |  |
| Jogador 3 | 3-5 | 12:51:21 | MOVE Bench -> Board: Camille (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Colosso | DA_18_Camille | -0.3900 |  |
| Jogador 3 | 3-5 | 12:51:22 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Colosso | DA_18_Camille | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-6 | 12:51:44 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Colosso | DA_18_Camille | -0.1900 |  |
| Jogador 3 | 3-6 | 12:51:44 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Colosso | DA_18_Camille | 0.0200 |  |
| Jogador 3 | 3-6 | 12:51:45 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Colosso | DA_18_Camille | 0.4100 |  |
| Jogador 3 | 3-6 | 12:51:45 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Colosso | DA_18_Camille | -0.0700 |  |
| Jogador 3 | 3-6 | 12:51:46 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Colosso | DA_18_Camille | -0.0700 |  |
| Jogador 3 | 3-6 | 12:51:46 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Colosso | DA_18_Camille | -0.4700 |  |
| Jogador 3 | 3-6 | 12:51:47 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Colosso | DA_18_Camille | 0.8900 |  |
| Jogador 3 | 3-6 | 12:51:47 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Colosso | DA_18_Camille | -0.0700 |  |
| Jogador 3 | 3-6 | 12:51:47 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Colosso | DA_18_Camille | -0.0300 |  |
| Jogador 3 | 3-7 | 12:52:11 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Camille (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_18_Camille | 0.1700 |  |
| Jogador 3 | 3-7 | 12:52:12 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Camille (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_18_Camille | 0.1500 |  |
| Jogador 3 | 3-7 | 12:52:12 | MOVE Bench -> Board: Tristana (i:6.0) <-> Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_18_Camille | -0.4200 |  |
| Jogador 3 | 3-7 | 12:52:13 | MOVE Bench -> Board: Camille (i:2.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_18_Camille | 0.0300 |  |
| Jogador 3 | 3-7 | 12:52:13 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_18_Camille | -0.3300 |  |
| Jogador 3 | 3-7 | 12:52:14 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Colosso | DA_18_Camille | -0.0700 |  |
| Jogador 3 | 3-7 | 12:52:14 | MOVE Bench -> Board: Tristana (i:6.0) <-> Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Colosso | DA_18_Camille | -0.4900 |  |
| Jogador 3 | 3-7 | 12:52:15 | MOVE Bench -> Board: Camille (i:2.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Colosso | DA_18_Camille | -0.0200 |  |
| Jogador 3 | 3-7 | 12:52:15 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Colosso | DA_18_Camille | -0.6200 |  |
| Jogador 3 | 4-1 | 12:52:43 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Colosso | DA_18_Camille | 0.9600 |  |
| Jogador 3 | 4-1 | 12:52:44 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Colosso | DA_18_Camille | -0.2400 |  |
| Jogador 3 | 4-1 | 12:52:44 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Colosso | DA_18_Camille | 0.4000 |  |
| Jogador 3 | 4-1 | 12:52:45 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Colosso | DA_18_Camille | 0.9500 |  |
| Jogador 3 | 4-1 | 12:52:45 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Colosso | DA_18_Camille | -0.0700 |  |
| Jogador 3 | 4-1 | 12:52:46 | VENDEU: Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Colosso | DA_18_Camille | -0.5900 |  |
| Jogador 3 | 4-1 | 12:52:46 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Colosso | DA_18_Camille | 0.9600 |  |
| Jogador 3 | 4-1 | 12:52:46 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Colosso | DA_18_Camille | -0.5900 |  |
| Jogador 3 | 4-1 | 12:52:47 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Colosso | DA_18_Tristana | 1.0700 |  |
| Jogador 4 | ? | 12:47:30 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5900 |  |
| Jogador 4 | ? | 12:47:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:47:37 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 12:47:38 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:47:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:47:42 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1700 |  |
| Jogador 4 | 1-2 | 12:47:44 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1400 |  |
| Jogador 4 | 1-2 | 12:47:45 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 4 | 1-2 | 12:47:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 12:47:45 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 1-2 | 12:47:46 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 1-2 | 12:47:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 1-2 | 12:47:49 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4000 |  |
| Jogador 4 | 1-3 | 12:47:52 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.6300 |  |
| Jogador 4 | 1-3 | 12:47:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 4 | 1-3 | 12:47:53 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0100 |  |
| Jogador 4 | 1-3 | 12:47:53 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.0600 |  |
| Jogador 4 | 1-3 | 12:47:54 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 4 | 1-3 | 12:47:54 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 12:47:55 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1100 |  |
| Jogador 4 | 1-3 | 12:47:55 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | -0.5000 |  |
| Jogador 4 | 1-3 | 12:47:57 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | -0.0800 |  |
| Jogador 4 | 1-3 | 12:47:58 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 1.0000 |  |
| Jogador 4 | 1-4 | 12:48:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 4 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | 0.2400 |  |
| Jogador 4 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 4 | 1-4 | 12:48:02 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | 0.5900 |  |
| Jogador 4 | 1-4 | 12:48:02 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | 0.1000 |  |
| Jogador 4 | 1-4 | 12:48:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.0400 |  |
| Jogador 4 | 1-4 | 12:48:04 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 2-1 | 12:48:10 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | 0.9600 |  |
| Jogador 4 | 2-1 | 12:48:10 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.1500 |  |
| Jogador 4 | 2-1 | 12:48:11 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | -0.0700 |  |
| Jogador 4 | 2-1 | 12:48:11 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Krug18 | 0.0400 |  |
| Jogador 4 | 2-1 | 12:48:12 | MOVE Bench -> Board: Elise (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Krug18 | -0.1000 |  |
| Jogador 4 | 2-1 | 12:48:13 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | -0.2200 |  |
| Jogador 4 | 2-1 | 12:48:14 | MOVE Board -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 4 | 2-1 | 12:48:14 | MOVE Board -> Board: Karma (i:2.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | -0.1600 |  |
| Jogador 4 | 2-1 | 12:48:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 4 | 2-2 | 12:48:21 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 4 | 2-2 | 12:48:22 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3200 |  |
| Jogador 4 | 2-2 | 12:48:22 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 4 | 2-2 | 12:48:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 4 | 2-2 | 12:48:23 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5200 |  |
| Jogador 4 | 2-2 | 12:48:24 | MOVE Board -> Board: Krugue (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-2 | 12:48:24 | MOVE Board -> Board: Yorick (i:2.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 4 | 2-2 | 12:48:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 12:48:33 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 4 | 2-3 | 12:48:34 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1700 |  |
| Jogador 4 | 2-3 | 12:48:34 | MOVE Board -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 12:48:35 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Aphelios | -0.6100 |  |
| Jogador 4 | 2-3 | 12:48:36 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Aphelios | -0.1400 |  |
| Jogador 4 | 2-3 | 12:48:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-3 | 12:48:37 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Aphelios | -0.0600 |  |
| Jogador 4 | 2-3 | 12:48:37 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Aphelios | -0.1100 |  |
| Jogador 4 | 2-3 | 12:48:38 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Aphelios | 0.1800 |  |
| Jogador 4 | 2-4 | 12:48:47 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_18_Aphelios | 1.0200 |  |
| Jogador 4 | 2-4 | 12:48:48 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_Aphelios | 0.3600 |  |
| Jogador 4 | 2-4 | 12:48:48 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_18_Aphelios | 0.6100 |  |
| Jogador 4 | 2-4 | 12:48:49 | MOVE Bench -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_18_Aphelios | -0.5500 |  |
| Jogador 4 | 2-4 | 12:48:49 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_18_Aphelios | 0.3400 |  |
| Jogador 4 | 2-4 | 12:48:49 | MOVE Bench -> Board: Karma (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_18_Aphelios | 0.0800 |  |
| Jogador 4 | 2-4 | 12:48:50 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_Aphelios | -0.5100 |  |
| Jogador 4 | 2-4 | 12:48:51 | MOVE Bench -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_Aphelios | -0.6600 |  |
| Jogador 4 | 2-4 | 12:48:51 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_Aphelios | -0.2000 |  |
| Jogador 4 | 2-5 | 12:49:02 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_18_Aphelios | 0.2700 |  |
| Jogador 4 | 2-5 | 12:49:02 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_18_Aphelios | 0.3100 |  |
| Jogador 4 | 2-5 | 12:49:03 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_18_Aphelios | 0.3200 |  |
| Jogador 4 | 2-5 | 12:49:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-5 | 12:49:04 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_Aphelios | -0.2100 |  |
| Jogador 4 | 2-5 | 12:49:05 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_Aphelios | -0.4900 |  |
| Jogador 4 | 2-5 | 12:49:05 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_18_Aphelios | -0.6000 |  |
| Jogador 4 | 2-5 | 12:49:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_Aphelios | 0.0300 |  |
| Jogador 4 | 2-5 | 12:49:06 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_Aphelios | 0.5800 |  |
| Jogador 4 | 2-6 | 12:49:18 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_18_Aphelios | 0.3700 |  |
| Jogador 4 | 2-6 | 12:49:19 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_18_Aphelios | 0.3700 |  |
| Jogador 4 | 2-6 | 12:49:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Aphelios | -0.0400 |  |
| Jogador 4 | 2-6 | 12:49:20 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Aphelios | 0.0600 |  |
| Jogador 4 | 2-6 | 12:49:20 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Aphelios | -0.4000 |  |
| Jogador 4 | 2-6 | 12:49:21 | MOVE Bench -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Aphelios | 0.0900 |  |
| Jogador 4 | 2-6 | 12:49:21 | MOVE Board -> Board: Karma (i:2.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 2-6 | 12:49:22 | MOVE Board -> Board: Krugue (i:6.0) <-> Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 2-6 | 12:49:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-7 | 12:49:35 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_18_Aphelios | 0.2400 |  |
| Jogador 4 | 2-7 | 12:49:36 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_18_Aphelios | 0.2800 |  |
| Jogador 4 | 2-7 | 12:49:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Aphelios | -0.0100 |  |
| Jogador 4 | 2-7 | 12:49:37 | MOVE Board -> Board: Aphelios (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Aphelios | 0.0000 |  |
| Jogador 4 | 2-7 | 12:49:37 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Aphelios | 0.0800 |  |
| Jogador 4 | 2-7 | 12:49:38 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_18_Aphelios | -0.2000 |  |
| Jogador 4 | 2-7 | 12:49:38 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_Aphelios | -0.6300 |  |
| Jogador 4 | 2-7 | 12:49:38 | MOVE Bench -> Board: Krugue (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Aphelios | -0.3300 |  |
| Jogador 4 | 2-7 | 12:49:39 | VENDEU: Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Florescer | DA_18_Aphelios | -0.4900 |  |
| Jogador 4 | 3-1 | 12:49:53 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Florescer | DA_18_Yorick | 0.7700 |  |
| Jogador 4 | 3-1 | 12:49:53 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Florescer | DA_18_Yorick | 0.1400 |  |
| Jogador 4 | 3-1 | 12:49:54 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Florescer | DA_18_Yorick | 0.2100 |  |
| Jogador 4 | 3-1 | 12:49:54 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Florescer | DA_18_Yorick | 0.6000 |  |
| Jogador 4 | 3-1 | 12:49:55 | MOVE Board -> Board: Yorick (i:4.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Florescer | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-1 | 12:49:56 | MOVE Board -> Board: Elise (i:4.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Florescer | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-1 | 12:49:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Florescer | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-2 | 12:50:12 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Florescer | DA_18_Yorick | 0.1200 |  |
| Jogador 4 | 3-2 | 12:50:12 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | 0.0200 |  |
| Jogador 4 | 3-2 | 12:50:12 | MOVE Board -> Board: Krugue (i:6.0) <-> Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-2 | 12:50:13 | MOVE Board -> Board: Karma (i:2.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-2 | 12:50:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-3 | 12:50:31 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_18_Yorick | 0.7300 |  |
| Jogador 4 | 3-3 | 12:50:32 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Florescer | DA_18_Yorick | 0.6400 |  |
| Jogador 4 | 3-3 | 12:50:32 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Florescer | DA_18_Yorick | 0.0600 |  |
| Jogador 4 | 3-3 | 12:50:33 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | 0.3200 |  |
| Jogador 4 | 3-3 | 12:50:33 | MOVE Board -> Board: Master Yi (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-3 | 12:50:34 | MOVE Board -> Board: Aphelios (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-3 | 12:50:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-4 | 12:50:53 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Florescer | DA_18_Yorick | -0.4400 |  |
| Jogador 4 | 3-4 | 12:50:54 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Florescer | DA_18_Yorick | 0.7600 |  |
| Jogador 4 | 3-4 | 12:50:54 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_18_Yorick | 0.0300 |  |
| Jogador 4 | 3-4 | 12:50:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Florescer | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 3-4 | 12:50:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-4 | 12:50:56 | MOVE Board -> Board: Yorick (i:4.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-4 | 12:50:57 | MOVE Board -> Board: Krugue (i:6.0) <-> Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-4 | 12:50:57 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-5 | 12:51:18 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Florescer | DA_18_Yorick | 0.7300 |  |
| Jogador 4 | 3-5 | 12:51:18 | VENDEU: Yunara (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_18_Yorick | -0.5000 |  |
| Jogador 4 | 3-5 | 12:51:19 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | 0.4400 |  |
| Jogador 4 | 3-5 | 12:51:20 | MOVE Board -> Board: Karma (i:2.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-5 | 12:51:20 | MOVE Board -> Board: Master Yi (i:6.0) <-> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-5 | 12:51:20 | MOVE Board -> Board: Elise (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-5 | 12:51:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-6 | 12:51:44 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 0 | Florescer | DA_18_Yorick | -0.4700 |  |
| Jogador 4 | 3-6 | 12:51:44 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Florescer | DA_18_MasterYi_AD | 0.7600 |  |
| Jogador 4 | 3-6 | 12:51:45 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Florescer | DA_18_MasterYi_AD | 0.6000 |  |
| Jogador 4 | 3-6 | 12:51:45 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Florescer | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 4 | 3-6 | 12:51:46 | MOVE Board -> Board: Master Yi (i:12.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 12:51:46 | MOVE Board -> Board: Yorick (i:4.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 3-6 | 12:51:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 12:52:11 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Florescer | DA_18_MasterYi_AD | 0.1100 |  |
| Jogador 4 | 3-7 | 12:52:12 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Florescer | DA_18_MasterYi_AD | 0.1400 |  |
| Jogador 4 | 3-7 | 12:52:12 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Florescer | DA_18_MasterYi_AD | -0.3100 |  |
| Jogador 4 | 3-7 | 12:52:13 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 12:52:13 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Florescer | DA_18_MasterYi_AD | -0.7300 |  |
| Jogador 4 | 3-7 | 12:52:14 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Florescer | DA_18_MasterYi_AD | -0.0300 |  |
| Jogador 4 | 4-1 | 12:52:43 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Florescer | DA_18_MasterYi_AD | 0.6000 |  |
| Jogador 4 | 4-1 | 12:52:44 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Florescer | DA_18_MasterYi_AD | 0.2100 |  |
| Jogador 4 | 4-1 | 12:52:44 | MOVE Board -> Board: Yorick (i:4.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-1 | 12:52:45 | MOVE Board -> Board: Master Yi (i:12.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-1 | 12:52:45 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Florescer | DA_18_MasterYi_AD | -0.0300 |  |
| Jogador 4 | 4-2 | 12:53:13 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Florescer | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 4 | 4-2 | 12:53:13 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Florescer | DA_18_MasterYi_AD | 0.6900 |  |
| Jogador 4 | 4-2 | 12:53:14 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 12:53:14 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-2 | 12:53:15 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Florescer | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 4 | 4-3 | 12:53:46 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Florescer | DA_18_MasterYi_AD | 0.0600 |  |
| Jogador 4 | 4-3 | 12:53:46 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Florescer | DA_18_MasterYi_AD | 0.7500 |  |
| Jogador 4 | 4-3 | 12:53:47 | MOVE Board -> Board: Elise (i:4.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-3 | 12:53:47 | MOVE Board -> Board: Yorick (i:4.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-3 | 12:53:48 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Florescer | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 4 | 4-4 | 12:54:19 | VENDEU: Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Florescer | DA_18_MasterYi_AD | -0.5900 |  |
| Jogador 4 | 4-4 | 12:54:20 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Florescer | DA_18_MasterYi_AD | -0.2200 |  |
| Jogador 4 | 4-4 | 12:54:20 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 4 | Florescer | DA_18_MasterYi_AD | 0.0100 |  |
| Jogador 4 | 4-4 | 12:54:21 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 4 | Florescer | DA_18_MasterYi_AD | -0.0700 |  |
| Jogador 4 | 4-4 | 12:54:21 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 4 | Florescer | DA_18_MasterYi_AD | 0.0100 |  |
| Jogador 4 | 4-4 | 12:54:21 | MOVE Board -> Board: Master Yi (i:12.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 4 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-4 | 12:54:22 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 4 | Florescer | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 4 | 4-4 | 12:54:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 4 | Florescer | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 4 | 4-5 | 12:54:52 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 3 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-5 | 12:54:53 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Florescer | DA_18_MasterYi_AD | 0.4000 |  |
| Jogador 4 | 4-5 | 12:54:53 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 3 | Florescer | DA_18_MasterYi_AD | -0.4400 |  |
| Jogador 4 | 4-5 | 12:54:54 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Florescer | DA_18_MasterYi_AD | 0.2500 |  |
| Jogador 4 | 4-5 | 12:54:54 | MOVE Board -> Board: Karma (i:2.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-5 | 12:54:55 | MOVE Board -> Board: Krugue (i:6.0) <-> Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 4-5 | 12:54:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Florescer | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 4 | 4-6 | 12:55:30 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 56 | 4 | Florescer | DA_18_MasterYi_AD | -0.5700 |  |
| Jogador 4 | 4-6 | 12:55:30 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Florescer | DA_18_MasterYi_AD | 0.2000 |  |
| Jogador 4 | 4-6 | 12:55:31 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Florescer | DA_18_MasterYi_AD | -0.1000 |  |
| Jogador 4 | 4-6 | 12:55:31 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 52 | 4 | Florescer | DA_18_MasterYi_AD | 0.1100 |  |
| Jogador 4 | 4-6 | 12:55:32 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Florescer | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 4 | 4-6 | 12:55:32 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 44 | 4 | Florescer | DA_18_MasterYi_AD | 0.0300 |  |
| Jogador 4 | 4-6 | 12:55:32 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 40 | 4 | Florescer | DA_18_MasterYi_AD | 0.0300 |  |
| Jogador 4 | 4-6 | 12:55:33 | MOVE Board -> Board: Aphelios (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 40 | 4 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 4-6 | 12:55:34 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 36 | 4 | Florescer | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 4 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Florescer | DA_18_MasterYi_AD | 0.1800 |  |
| Jogador 4 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_TearOfTheGoddess -> Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Florescer | DA_18_MasterYi_AD | 0.1300 |  |
| Jogador 4 | 4-7 | 12:56:07 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 3 | Florescer | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 4 | 4-7 | 12:56:07 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Florescer | DA_18_MasterYi_AD | 0.4100 |  |
| Jogador 4 | 4-7 | 12:56:08 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 41 | 3 | Florescer | DA_18_MasterYi_AD | 0.0300 |  |
| Jogador 4 | 4-7 | 12:56:08 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 37 | 3 | Florescer | DA_18_MasterYi_AD | -0.0500 |  |
| Jogador 4 | 4-7 | 12:56:08 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 33 | 3 | Florescer | DA_18_MasterYi_AD | 0.0300 |  |
| Jogador 4 | 4-7 | 12:56:09 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 29 | 3 | Florescer | DA_18_MasterYi_AD | 0.0300 |  |
| Jogador 4 | 4-7 | 12:56:09 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 29 | 3 | Florescer | DA_18_MasterYi_AD | 0.4000 |  |
| Jogador 4 | 5-1 | 12:56:41 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Florescer | DA_18_MasterYi_AD | 0.3600 |  |
| Jogador 4 | 5-1 | 12:56:41 | VENDEU: Sett (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Florescer | DA_18_MasterYi_AD | -0.1100 |  |
| Jogador 4 | 5-1 | 12:56:42 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Florescer | DA_18_MasterYi_AD | 0.3700 |  |
| Jogador 4 | 5-1 | 12:56:42 | MOVE Board -> Board: Diana (i:6.0) <-> Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 5-1 | 12:56:43 | MOVE Board -> Board: Elise (i:4.0) <-> Yorick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 5-1 | 12:56:43 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Florescer | DA_18_MasterYi_AD | -0.4100 |  |
| Jogador 5 | ? | 12:47:30 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.5700 |  |
| Jogador 5 | ? | 12:47:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 12:47:37 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 12:47:38 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1300 |  |
| Jogador 5 | 1-1 | 12:47:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 12:47:42 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-2 | 12:47:44 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.2000 |  |
| Jogador 5 | 1-2 | 12:47:45 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0400 |  |
| Jogador 5 | 1-2 | 12:47:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | -0.0100 |  |
| Jogador 5 | 1-2 | 12:47:45 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | -0.0300 |  |
| Jogador 5 | 1-2 | 12:47:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 1-2 | 12:47:49 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.4400 |  |
| Jogador 5 | 1-3 | 12:47:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yunara | 0.3300 |  |
| Jogador 5 | 1-3 | 12:47:52 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.2900 |  |
| Jogador 5 | 1-3 | 12:47:53 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0400 |  |
| Jogador 5 | 1-3 | 12:47:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 1-4 | 12:48:00 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yunara | 1.0200 |  |
| Jogador 5 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yunara | 0.2400 |  |
| Jogador 5 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yunara | 0.2100 |  |
| Jogador 5 | 1-4 | 12:48:02 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yunara | 0.4000 |  |
| Jogador 5 | 1-4 | 12:48:02 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 1-4 | 12:48:03 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 1-4 | 12:48:04 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.2500 |  |
| Jogador 5 | 2-1 | 12:48:10 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9600 |  |
| Jogador 5 | 2-1 | 12:48:10 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-1 | 12:48:11 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.1300 |  |
| Jogador 5 | 2-1 | 12:48:11 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.1700 |  |
| Jogador 5 | 2-1 | 12:48:12 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 2-1 | 12:48:13 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1900 |  |
| Jogador 5 | 2-1 | 12:48:14 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.5900 |  |
| Jogador 5 | 2-1 | 12:48:14 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0600 |  |
| Jogador 5 | 2-1 | 12:48:15 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 5 | 2-2 | 12:48:21 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Rakan | 1.1100 |  |
| Jogador 5 | 2-2 | 12:48:22 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 12:48:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 5 | 2-2 | 12:48:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0500 |  |
| Jogador 5 | 2-2 | 12:48:23 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.5900 |  |
| Jogador 5 | 2-2 | 12:48:24 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 12:48:24 | MOVE Board -> Board: Rakan (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-2 | 12:48:25 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 2-2 | 12:48:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-3 | 12:48:33 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 5 | 2-3 | 12:48:34 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.2000 |  |
| Jogador 5 | 2-3 | 12:48:34 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 5 | 2-3 | 12:48:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0400 |  |
| Jogador 5 | 2-3 | 12:48:36 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-3 | 12:48:36 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 2-3 | 12:48:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-4 | 12:48:47 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | 0.3400 |  |
| Jogador 5 | 2-4 | 12:48:48 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.3000 |  |
| Jogador 5 | 2-4 | 12:48:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | -0.0400 |  |
| Jogador 5 | 2-4 | 12:48:49 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-4 | 12:48:49 | MOVE Board -> Board: Rakan (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 2-4 | 12:48:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-5 | 12:49:02 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | 0.0900 |  |
| Jogador 5 | 2-5 | 12:49:02 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | -0.0500 |  |
| Jogador 5 | 2-5 | 12:49:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | 0.0300 |  |
| Jogador 5 | 2-5 | 12:49:04 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Rakan | -0.0500 |  |
| Jogador 5 | 2-5 | 12:49:04 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | -0.0600 |  |
| Jogador 5 | 2-5 | 12:49:05 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | -0.0700 |  |
| Jogador 5 | 2-5 | 12:49:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | -0.0600 |  |
| Jogador 5 | 2-5 | 12:49:06 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | 0.4100 |  |
| Jogador 5 | 2-5 | 12:49:06 | MOVE Board -> Board: Leona (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 2-6 | 12:49:18 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.8200 |  |
| Jogador 5 | 2-6 | 12:49:19 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | 0.3500 |  |
| Jogador 5 | 2-6 | 12:49:20 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | 0.8900 |  |
| Jogador 5 | 2-6 | 12:49:20 | MOVE Board -> Board: Rakan (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-6 | 12:49:20 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 2-6 | 12:49:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-7 | 12:49:35 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Yunara | 0.8300 |  |
| Jogador 5 | 2-7 | 12:49:36 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yunara | 0.7500 |  |
| Jogador 5 | 2-7 | 12:49:36 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yunara | 0.2000 |  |
| Jogador 5 | 2-7 | 12:49:37 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 2-7 | 12:49:37 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yunara | -0.0100 |  |
| Jogador 5 | 2-7 | 12:49:38 | MOVE Board -> Board: Leona (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yunara | -0.0100 |  |
| Jogador 5 | 2-7 | 12:49:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 3-1 | 12:49:53 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Yunara | 0.2900 |  |
| Jogador 5 | 3-1 | 12:49:53 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Tristana | 0.8200 |  |
| Jogador 5 | 3-1 | 12:49:54 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Tristana | -0.2600 |  |
| Jogador 5 | 3-1 | 12:49:54 | MOVE Board -> Board: Rakan (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-1 | 12:49:55 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-1 | 12:49:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-2 | 12:50:12 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Tristana | 0.8100 |  |
| Jogador 5 | 3-2 | 12:50:12 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Tristana | -0.5000 |  |
| Jogador 5 | 3-2 | 12:50:12 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Tristana | 0.2000 |  |
| Jogador 5 | 3-2 | 12:50:13 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Colosso | DA_18_Rakan | -0.4300 |  |
| Jogador 5 | 3-2 | 12:50:13 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 3-2 | 12:50:14 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 3-2 | 12:50:14 | MOVE Board -> Board: Leona (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 5 | 3-2 | 12:50:15 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 3-2 | 12:50:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Rakan | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-3 | 12:50:31 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Rakan | 0.1000 |  |
| Jogador 5 | 3-3 | 12:50:32 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_18_Rakan | 0.7300 |  |
| Jogador 5 | 3-3 | 12:50:32 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Rakan | -0.4200 |  |
| Jogador 5 | 3-3 | 12:50:33 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_18_Rakan | 0.7700 |  |
| Jogador 5 | 3-3 | 12:50:33 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Rakan | 0.0700 |  |
| Jogador 5 | 3-3 | 12:50:34 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 3-3 | 12:50:34 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 3-3 | 12:50:35 | MOVE Board -> Board: Leona (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 5 | 3-3 | 12:50:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Rakan | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-4 | 12:50:53 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Rakan | 0.7900 |  |
| Jogador 5 | 3-4 | 12:50:54 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_18_Rakan | -0.5800 |  |
| Jogador 5 | 3-4 | 12:50:54 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Rakan | 0.7200 |  |
| Jogador 5 | 3-4 | 12:50:55 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 3-4 | 12:50:56 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 3-4 | 12:50:56 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 3-4 | 12:50:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Rakan | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-5 | 12:51:18 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 5 | 3-5 | 12:51:18 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Colosso | DA_18_Rakan | 0.3100 |  |
| Jogador 5 | 3-5 | 12:51:19 | MOVE Board -> Board: Leona (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 3-5 | 12:51:20 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 3-5 | 12:51:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Colosso | DA_18_Rakan | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-6 | 12:51:44 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Colosso | DA_18_Rakan | -0.5000 |  |
| Jogador 5 | 3-6 | 12:51:44 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Colosso | DA_18_Rakan | 0.8700 |  |
| Jogador 5 | 3-6 | 12:51:45 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_18_Rakan | 0.2900 |  |
| Jogador 5 | 3-6 | 12:51:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Rakan | -0.0800 |  |
| Jogador 5 | 3-6 | 12:51:46 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 3-6 | 12:51:46 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 3-6 | 12:51:47 | MOVE Board -> Board: Leona (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 5 | 3-6 | 12:51:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Rakan | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-7 | 12:52:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Colosso | DA_18_Rakan | 0.8900 |  |
| Jogador 5 | 3-7 | 12:52:12 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Colosso | DA_18_Rakan | 0.2300 |  |
| Jogador 5 | 3-7 | 12:52:12 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Colosso | DA_18_Rakan | 0.2200 |  |
| Jogador 5 | 3-7 | 12:52:13 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 3 | Colosso | DA_18_Rakan | -0.5000 |  |
| Jogador 5 | 3-7 | 12:52:13 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Colosso | DA_18_Rakan | 0.1800 |  |
| Jogador 5 | 3-7 | 12:52:14 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Colosso | DA_18_Rakan | -0.2000 |  |
| Jogador 5 | 3-7 | 12:52:14 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Colosso | DA_18_Rakan | -0.0500 |  |
| Jogador 5 | 3-7 | 12:52:15 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Colosso | DA_18_Rakan | 0.6500 |  |
| Jogador 5 | 3-7 | 12:52:15 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 4-1 | 12:52:43 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Colosso | DA_18_Rakan | -0.1000 |  |
| Jogador 5 | 4-1 | 12:52:44 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Colosso | DA_18_Rakan | 0.8800 |  |
| Jogador 5 | 4-1 | 12:52:44 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Colosso | DA_18_Rakan | -0.5900 |  |
| Jogador 5 | 4-1 | 12:52:45 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 4 | Colosso | DA_18_Rakan | 0.9600 |  |
| Jogador 5 | 4-1 | 12:52:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Colosso | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 4-1 | 12:52:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_18_Rakan | 0.3400 |  |
| Jogador 5 | 4-1 | 12:52:46 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 4-1 | 12:52:46 | MOVE Board -> Board: Yunara (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 4-1 | 12:52:47 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 4-2 | 12:53:13 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Colosso | DA_18_Rakan | 0.3200 |  |
| Jogador 5 | 4-2 | 12:53:13 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 4-2 | 12:53:14 | MOVE Board -> Board: Yunara (i:4.0) <-> Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 4-2 | 12:53:14 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Colosso | DA_18_Rakan | -0.2300 |  |
| Jogador 5 | 4-3 | 12:53:46 | COMPROU: Leona (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Colosso | DA_18_Rakan | 0.7100 |  |
| Jogador 5 | 4-3 | 12:53:46 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_18_Rakan | 0.2600 |  |
| Jogador 5 | 4-3 | 12:53:47 | MOVE Board -> Board: Leona (i:2.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 4-3 | 12:53:47 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 4-3 | 12:53:48 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_18_Rakan | -0.0900 |  |
| Jogador 5 | 4-4 | 12:54:19 | MOVE Board -> Board: Rakan (i:4.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 4-4 | 12:54:20 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 4-4 | 12:54:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Colosso | DA_18_Rakan | -0.1000 |  |
| Jogador 5 | 4-5 | 12:54:52 | VENDEU: Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Colosso | DA_18_Rakan | -0.1000 |  |
| Jogador 5 | 4-5 | 12:54:53 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Colosso | DA_18_Rakan | 0.8300 |  |
| Jogador 5 | 4-5 | 12:54:53 | MOVE Board -> Board: Leona (i:2.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 4-5 | 12:54:54 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 4-5 | 12:54:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Colosso | DA_18_Rakan | -0.1100 |  |
| Jogador 5 | 4-6 | 12:55:30 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 105 | 5 | Colosso | DA_18_Rakan | -0.9800 |  |
| Jogador 5 | 4-6 | 12:55:30 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_18_Rakan | 0.1400 |  |
| Jogador 5 | 4-6 | 12:55:31 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 105 | 5 | Colosso | DA_18_Rakan | -0.0600 |  |
| Jogador 5 | 4-6 | 12:55:31 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 4-6 | 12:55:32 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Colosso | DA_18_Rakan | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 5 | 4-6 | 12:55:32 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Colosso | DA_18_Rakan | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 5 | 4-6 | 12:55:32 | MOVE Board -> Board: Yunara (i:4.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 4-6 | 12:55:33 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 5 | 4-6 | 12:55:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Colosso | DA_18_Rakan | -0.1200 |  |
| Jogador 5 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Colosso | DA_18_Rakan | 0.1800 |  |
| Jogador 5 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Colosso | DA_18_Rakan | 0.1300 |  |
| Jogador 5 | 4-7 | 12:56:07 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Colosso | DA_18_Rakan | -0.5900 |  |
| Jogador 5 | 4-7 | 12:56:07 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Colosso | DA_18_Rakan | 0.9500 |  |
| Jogador 5 | 4-7 | 12:56:08 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 108 | 5 | Colosso | DA_18_Rakan | 0.1500 |  |
| Jogador 5 | 4-7 | 12:56:08 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 105 | 5 | Colosso | DA_18_Rakan | 0.0600 |  |
| Jogador 5 | 4-7 | 12:56:08 | MOVE Board -> Board: Rakan (i:4.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 105 | 5 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 4-7 | 12:56:09 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 105 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 4-7 | 12:56:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 105 | 5 | Colosso | DA_18_Rakan | -0.1300 |  |
| Jogador 5 | 5-1 | 12:56:41 | VENDEU: Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 118 | 5 | Colosso | DA_18_Rakan | -0.8500 |  |
| Jogador 5 | 5-1 | 12:56:41 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Colosso | DA_18_Rakan | 0.5500 |  |
| Jogador 5 | 5-1 | 12:56:42 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 118 | 5 | Colosso | DA_18_Rakan | -0.0600 |  |
| Jogador 5 | 5-1 | 12:56:42 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Colosso | DA_18_Rakan | 0.2800 |  |
| Jogador 5 | 5-1 | 12:56:43 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Colosso | DA_18_Rakan | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 5 | 5-1 | 12:56:43 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Colosso | DA_18_Rakan | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 5 | 5-1 | 12:56:44 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Colosso | DA_18_Rakan | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 5 | 5-1 | 12:56:45 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Colosso | DA_18_Rakan | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 5 | 5-1 | 12:56:45 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Colosso | DA_18_Rakan | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 5 | 5-2 | 12:57:20 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 129 | 5 | Colosso | DA_18_Rakan | -0.1000 |  |
| Jogador 5 | 5-2 | 12:57:20 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 128 | 5 | Colosso | DA_18_Rakan | 0.3300 |  |
| Jogador 5 | 5-2 | 12:57:21 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 129 | 5 | Colosso | DA_18_Rakan | -0.5900 |  |
| Jogador 5 | 5-2 | 12:57:21 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 126 | 5 | Colosso | DA_18_Diana | 0.9000 |  |
| Jogador 5 | 5-2 | 12:57:22 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 123 | 5 | Colosso | DA_18_Diana | 0.3000 |  |
| Jogador 5 | 5-2 | 12:57:22 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 120 | 5 | Colosso | DA_18_Diana | 0.2800 |  |
| Jogador 5 | 5-2 | 12:57:23 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 120 | 5 | Colosso | DA_18_Diana | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 5 | 5-2 | 12:57:23 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 120 | 5 | Colosso | DA_18_Diana | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 5 | 5-2 | 12:57:23 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 120 | 5 | Colosso | DA_18_Diana | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 5 | 5-3 | 12:57:58 | VENDEU: Diana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 139 | 5 | Colosso | DA_18_Rakan | -0.5800 |  |
| Jogador 5 | 5-3 | 12:57:58 | COMPROU: Ashe (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 134 | 5 | Colosso | DA_18_Ashe | 0.0700 |  |
| Jogador 5 | 5-3 | 12:57:59 | MOVE Bench -> Board: Ashe (i:10.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 134 | 5 | Colosso | DA_18_Ashe | -0.7100 |  |
| Jogador 5 | 5-3 | 12:57:59 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 137 | 5 | Colosso | DA_18_Ashe | -0.5500 |  |
| Jogador 5 | 5-3 | 12:58:00 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 134 | 5 | Colosso | DA_18_Ashe | 0.0700 |  |
| Jogador 5 | 5-3 | 12:58:00 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 130 | 5 | Colosso | DA_18_Ashe | 0.0400 |  |
| Jogador 5 | 5-3 | 12:58:01 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Colosso | DA_18_Ashe | 0.0400 |  |
| Jogador 5 | 5-3 | 12:58:01 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 122 | 5 | Colosso | DA_18_Ashe | 0.0400 |  |
| Jogador 5 | 5-3 | 12:58:01 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 118 | 5 | Colosso | DA_18_Ashe | 0.0400 |  |
| Jogador 5 | 5-4 | 12:58:37 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 132 | 5 | Colosso | DA_18_Ashe | -0.0400 |  |
| Jogador 5 | 5-4 | 12:58:38 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 130 | 5 | Colosso | DA_18_Ashe | 1.0200 |  |
| Jogador 5 | 5-4 | 12:58:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Colosso | DA_18_Ashe | 0.4700 |  |
| Jogador 5 | 5-4 | 12:58:39 | MOVE Bench -> Board: Yunara (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Colosso | DA_18_Ashe | 0.5900 |  |
| Jogador 5 | 5-4 | 12:58:39 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 127 | 5 | Colosso | DA_18_Ashe | 0.0200 |  |
| Jogador 5 | 5-4 | 12:58:39 | MOVE Board -> Board: Yunara (i:8.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 127 | 5 | Colosso | DA_18_Ashe | 0.0000 |  |
| Jogador 5 | 5-4 | 12:58:40 | REROLL | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Colosso | DA_18_Ashe | -0.1600 |  |
| Jogador 5 | 5-4 | 12:58:41 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 127 | 5 | Colosso | DA_18_Ashe | -0.0100 |  |
| Jogador 5 | 5-4 | 12:58:41 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Colosso | DA_18_Ashe | 0.3300 |  |
| Jogador 5 | 5-5 | 12:59:18 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_18_Ashe | -0.0800 |  |
| Jogador 5 | 5-5 | 12:59:19 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Colosso | DA_18_Ashe | 0.3800 |  |
| Jogador 5 | 5-5 | 12:59:19 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Colosso | DA_18_Ashe | -0.0500 |  |
| Jogador 5 | 5-5 | 12:59:20 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Colosso | DA_18_Ashe | 0.0500 |  |
| Jogador 5 | 5-5 | 12:59:20 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Colosso | DA_18_Ashe | 0.1600 |  |
| Jogador 5 | 5-5 | 12:59:21 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Colosso | DA_18_Ashe | -0.0700 |  |
| Jogador 5 | 5-5 | 12:59:21 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Colosso | DA_18_Ashe | -0.0100 |  |
| Jogador 5 | 5-5 | 12:59:21 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Colosso | DA_18_Ashe | -0.0600 |  |
| Jogador 5 | 5-5 | 12:59:22 | MOVE Bench -> Board: Amumu (i:8.0) <-> Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Colosso | DA_18_Ashe | -0.2900 |  |
| Jogador 5 | 5-6 | 13:00:00 | VENDEU: Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Colosso | DA_18_Ashe | -0.0300 |  |
| Jogador 5 | 5-6 | 13:00:01 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Colosso | DA_18_Azir | 1.0500 |  |
| Jogador 5 | 5-6 | 13:00:01 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Colosso | DA_18_Azir | 0.4300 |  |
| Jogador 5 | 5-6 | 13:00:02 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Colosso | DA_18_Azir | 0.1800 |  |
| Jogador 5 | 5-6 | 13:00:02 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Colosso | DA_18_Azir | -0.0700 |  |
| Jogador 5 | 5-6 | 13:00:03 | VENDEU: Azir (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Colosso | DA_18_Ashe | -0.6000 |  |
| Jogador 5 | 5-6 | 13:00:03 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Colosso | DA_18_Ashe | 0.4200 |  |
| Jogador 5 | 5-6 | 13:00:03 | VENDEU: Nidalee (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Colosso | DA_18_Ashe | -0.0200 |  |
| Jogador 5 | 5-6 | 13:00:04 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Colosso | DA_18_Ashe | 0.1300 |  |
| Jogador 5 | 5-7 | 13:00:42 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Master Yi (i:6.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Colosso | DA_18_Ashe | 0.1000 |  |
| Jogador 5 | 5-7 | 13:00:42 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Colosso | DA_18_Ashe | -0.0400 |  |
| Jogador 5 | 5-7 | 13:00:43 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 149 | 5 | Colosso | DA_18_Ashe | 0.5100 |  |
| Jogador 5 | 5-7 | 13:00:43 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Colosso | DA_18_Ashe | -0.0300 |  |
| Jogador 5 | 5-7 | 13:00:44 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Colosso | DA_18_Ashe | 0.4100 |  |
| Jogador 5 | 5-7 | 13:00:44 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Colosso | DA_18_Ashe | -0.0700 |  |
| Jogador 5 | 5-7 | 13:00:44 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Colosso | DA_18_Ashe | -0.1000 |  |
| Jogador 5 | 5-7 | 13:00:45 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Colosso | DA_18_Ashe | 0.9500 |  |
| Jogador 5 | 5-7 | 13:00:45 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Colosso | DA_18_Ashe | -0.4700 |  |
| Jogador 5 | 6-1 | 13:01:24 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Colosso | DA_18_Ashe | 0.4100 |  |
| Jogador 5 | 6-1 | 13:01:25 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Colosso | DA_18_Ashe | -0.0700 |  |
| Jogador 5 | 6-1 | 13:01:25 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Colosso | DA_18_Ashe | -0.1000 |  |
| Jogador 5 | 6-1 | 13:01:26 | COMPROU: Alune (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Colosso | DA_18_Alune | 0.2400 |  |
| Jogador 5 | 6-1 | 13:01:26 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Colosso | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-1 | 13:01:26 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Colosso | DA_18_Alune | -0.5900 |  |
| Jogador 5 | 6-1 | 13:01:27 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 151 | 5 | Colosso | DA_18_Alune | 1.0300 |  |
| Jogador 5 | 6-1 | 13:01:27 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Colosso | DA_18_Alune | -0.6100 |  |
| Jogador 5 | 6-1 | 13:01:28 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 151 | 5 | Colosso | DA_18_Alune | 0.4400 |  |
| Jogador 5 | 6-2 | 13:02:07 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Colosso | DA_18_Alune | -0.1200 |  |
| Jogador 5 | 6-2 | 13:02:07 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 162 | 5 | Colosso | DA_18_Alune | 0.1800 |  |
| Jogador 5 | 6-2 | 13:02:08 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 160 | 5 | Colosso | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-2 | 13:02:08 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 164 | 5 | Colosso | DA_18_Alune | -0.0400 |  |
| Jogador 5 | 6-2 | 13:02:08 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 160 | 5 | Colosso | DA_18_Alune | 0.1800 |  |
| Jogador 5 | 6-2 | 13:02:09 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 158 | 5 | Colosso | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-2 | 13:02:09 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 162 | 5 | Colosso | DA_18_Alune | -0.0400 |  |
| Jogador 5 | 6-2 | 13:02:09 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Colosso | DA_18_Alune | 0.9800 |  |
| Jogador 5 | 6-2 | 13:02:10 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Colosso | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-3 | 13:02:52 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 167 | 5 | Colosso | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-3 | 13:02:52 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 170 | 5 | Colosso | DA_18_Alune | -0.5900 |  |
| Jogador 5 | 6-3 | 13:02:53 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 167 | 5 | Colosso | DA_18_Alune | 0.6200 |  |
| Jogador 5 | 6-3 | 13:02:53 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 165 | 5 | Colosso | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-3 | 13:02:54 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 168 | 5 | Colosso | DA_18_Alune | -0.4800 |  |
| Jogador 5 | 6-3 | 13:02:54 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 165 | 5 | Colosso | DA_18_Alune | 0.4300 |  |
| Jogador 5 | 6-3 | 13:02:54 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 168 | 5 | Colosso | DA_18_Alune | -0.1200 |  |
| Jogador 5 | 6-3 | 13:02:55 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 165 | 5 | Colosso | DA_18_Alune | 0.4300 |  |
| Jogador 5 | 6-3 | 13:02:55 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Colosso | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-4 | 13:03:38 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 177 | 5 | Colosso | DA_18_Alune | -0.1200 |  |
| Jogador 5 | 6-4 | 13:03:38 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 174 | 5 | Colosso | DA_18_Alune | 0.4300 |  |
| Jogador 5 | 6-4 | 13:03:38 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 177 | 5 | Colosso | DA_18_Alune | -0.1200 |  |
| Jogador 5 | 6-4 | 13:03:39 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 176 | 5 | Colosso | DA_18_Alune | 1.0400 |  |
| Jogador 5 | 6-4 | 13:03:39 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Colosso | DA_18_Alune | 0.2700 |  |
| Jogador 5 | 6-4 | 13:03:40 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 173 | 5 | Colosso | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-4 | 13:03:40 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 170 | 5 | Colosso | DA_18_Alune | 0.7500 |  |
| Jogador 5 | 6-4 | 13:03:41 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 168 | 5 | Colosso | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-4 | 13:03:41 | VENDEU: Leona (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 171 | 5 | Colosso | DA_18_Alune | -0.4600 |  |
| Jogador 6 | ? | 12:47:30 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1600 |  |
| Jogador 6 | ? | 12:47:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 12:47:37 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 6 | 1-1 | 12:47:38 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.9900 |  |
| Jogador 6 | 1-1 | 12:47:38 | MOVE Bench -> Board: Yorick (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1000 |  |
| Jogador 6 | 1-1 | 12:47:39 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1500 |  |
| Jogador 6 | 1-1 | 12:47:40 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.2200 |  |
| Jogador 6 | 1-1 | 12:47:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-1 | 12:47:42 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.5000 |  |
| Jogador 6 | 1-2 | 12:47:44 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 6 | 1-2 | 12:47:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 6 | 1-2 | 12:47:45 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 6 | 1-2 | 12:47:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 6 | 1-2 | 12:47:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-3 | 12:47:52 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 1.0200 |  |
| Jogador 6 | 1-3 | 12:47:52 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 6 | 1-3 | 12:47:53 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.1400 |  |
| Jogador 6 | 1-3 | 12:47:53 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1400 |  |
| Jogador 6 | 1-3 | 12:47:54 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0100 |  |
| Jogador 6 | 1-3 | 12:47:54 | MOVE Board -> Board: Yorick (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0300 |  |
| Jogador 6 | 1-3 | 12:47:55 | MOVE Board -> Board: Cascalho (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.3500 |  |
| Jogador 6 | 1-3 | 12:47:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-4 | 12:48:00 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.2800 |  |
| Jogador 6 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.1900 |  |
| Jogador 6 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.1900 |  |
| Jogador 6 | 1-4 | 12:48:02 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.0900 |  |
| Jogador 6 | 1-4 | 12:48:02 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.3100 |  |
| Jogador 6 | 1-4 | 12:48:03 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.1400 |  |
| Jogador 6 | 1-4 | 12:48:04 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Murkwolf18 | 0.0500 |  |
| Jogador 6 | 2-1 | 12:48:10 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Vi18 | 0.2700 |  |
| Jogador 6 | 2-1 | 12:48:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | -0.0400 |  |
| Jogador 6 | 2-1 | 12:48:11 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Vi18 | -0.1300 |  |
| Jogador 6 | 2-1 | 12:48:11 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Vi18 | -0.1900 |  |
| Jogador 6 | 2-1 | 12:48:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | 0.0500 |  |
| Jogador 6 | 2-1 | 12:48:13 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | 0.4500 |  |
| Jogador 6 | 2-1 | 12:48:14 | MOVE Board -> Board: Vi (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 2-1 | 12:48:14 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | 0.0800 |  |
| Jogador 6 | 2-1 | 12:48:15 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 2-2 | 12:48:21 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Vi18 | 0.3800 |  |
| Jogador 6 | 2-2 | 12:48:22 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Vi18 | 0.2700 |  |
| Jogador 6 | 2-2 | 12:48:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Vi18 | -0.0400 |  |
| Jogador 6 | 2-2 | 12:48:23 | MOVE Board -> Board: Vi (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 2-2 | 12:48:23 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Vi18 | -0.0400 |  |
| Jogador 6 | 2-2 | 12:48:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 2-3 | 12:48:33 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Vi18 | 0.3600 |  |
| Jogador 6 | 2-3 | 12:48:34 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Vi18 | 0.9500 |  |
| Jogador 6 | 2-3 | 12:48:34 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Vi18 | -0.1200 |  |
| Jogador 6 | 2-3 | 12:48:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | -0.0400 |  |
| Jogador 6 | 2-3 | 12:48:36 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Vi18 | -0.2200 |  |
| Jogador 6 | 2-3 | 12:48:36 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Vi18 | 0.2900 |  |
| Jogador 6 | 2-3 | 12:48:37 | MOVE Board -> Board: Vi (i:6.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 2-3 | 12:48:37 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Vi18 | 0.0700 |  |
| Jogador 6 | 2-3 | 12:48:38 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 2-4 | 12:48:47 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Yorick | 1.0500 |  |
| Jogador 6 | 2-4 | 12:48:48 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Yorick | 0.3500 |  |
| Jogador 6 | 2-4 | 12:48:48 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Yorick | 0.1000 |  |
| Jogador 6 | 2-4 | 12:48:49 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Yorick | -0.0600 |  |
| Jogador 6 | 2-4 | 12:48:49 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-4 | 12:48:49 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Yorick | 0.4200 |  |
| Jogador 6 | 2-4 | 12:48:50 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 2-4 | 12:48:51 | MOVE Board -> Board: Vi (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 6 | 2-4 | 12:48:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-5 | 12:49:02 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Yorick | 0.3400 |  |
| Jogador 6 | 2-5 | 12:49:02 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | 0.2800 |  |
| Jogador 6 | 2-5 | 12:49:03 | MOVE Board -> Board: Yorick (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-5 | 12:49:04 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 6 | 2-5 | 12:49:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-6 | 12:49:18 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Yorick | 1.0000 |  |
| Jogador 6 | 2-6 | 12:49:19 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | 0.9000 |  |
| Jogador 6 | 2-6 | 12:49:20 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-6 | 12:49:20 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 2-6 | 12:49:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-7 | 12:49:35 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Yorick | 0.7900 |  |
| Jogador 6 | 2-7 | 12:49:36 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Yorick | 0.2000 |  |
| Jogador 6 | 2-7 | 12:49:36 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | -0.1200 |  |
| Jogador 6 | 2-7 | 12:49:37 | MOVE Board -> Board: Vi (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-7 | 12:49:37 | MOVE Board -> Board: Yorick (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 2-7 | 12:49:38 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | -0.0800 |  |
| Jogador 6 | 2-7 | 12:49:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 3-1 | 12:49:53 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Yorick | 0.0100 |  |
| Jogador 6 | 3-1 | 12:49:53 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Yorick | 0.8400 |  |
| Jogador 6 | 3-1 | 12:49:54 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Yorick | 0.8400 |  |
| Jogador 6 | 3-1 | 12:49:54 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | 0.3600 |  |
| Jogador 6 | 3-1 | 12:49:55 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | 0.3900 |  |
| Jogador 6 | 3-1 | 12:49:56 | MOVE Board -> Board: Sejuani (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 3-1 | 12:49:56 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 3-1 | 12:49:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 3-2 | 12:50:12 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Rakan | 0.0500 |  |
| Jogador 6 | 3-2 | 12:50:12 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | -0.1400 |  |
| Jogador 6 | 3-2 | 12:50:12 | MOVE Board -> Board: Rakan (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 3-2 | 12:50:13 | MOVE Board -> Board: Sejuani (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 3-2 | 12:50:13 | MOVE Board -> Board: Akali (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 3-2 | 12:50:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 3-3 | 12:50:31 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_Vi18 | 0.8300 |  |
| Jogador 6 | 3-3 | 12:50:32 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Vi18 | 0.1900 |  |
| Jogador 6 | 3-3 | 12:50:32 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Vi18 | 0.4100 |  |
| Jogador 6 | 3-3 | 12:50:33 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Vi18 | 0.7700 |  |
| Jogador 6 | 3-3 | 12:50:33 | MOVE Bench -> Board: Vi (i:12.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Vi18 | 0.1000 |  |
| Jogador 6 | 3-3 | 12:50:34 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Vi18 | 0.2800 |  |
| Jogador 6 | 3-3 | 12:50:34 | MOVE Board -> Board: Vi (i:12.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-3 | 12:50:35 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-3 | 12:50:35 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-4 | 12:50:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Vi18 | 0.4000 |  |
| Jogador 6 | 3-4 | 12:50:54 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Vi18 | 0.2000 |  |
| Jogador 6 | 3-4 | 12:50:54 | MOVE Board -> Board: Rakan (i:4.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-4 | 12:50:55 | MOVE Board -> Board: Akali (i:2.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-4 | 12:50:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-5 | 12:51:18 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_Vi18 | 0.0400 |  |
| Jogador 6 | 3-5 | 12:51:18 | VENDEU: Cascalho (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_Vi18 | -0.5500 |  |
| Jogador 6 | 3-5 | 12:51:19 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_Vi18 | 0.7300 |  |
| Jogador 6 | 3-5 | 12:51:20 | MOVE Board -> Board: Grompe (i:4.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_Vi18 | 0.0500 |  |
| Jogador 6 | 3-5 | 12:51:20 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-5 | 12:51:20 | MOVE Board -> Board: Vi (i:12.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_Vi18 | -0.0200 |  |
| Jogador 6 | 3-5 | 12:51:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-6 | 12:51:44 | MOVE Board -> Board: Rakan (i:4.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-6 | 12:51:44 | MOVE Board -> Board: Akali (i:2.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-6 | 12:51:45 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-7 | 12:52:11 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Colosso | DA_Vi18 | 0.2300 |  |
| Jogador 6 | 3-7 | 12:52:12 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Colosso | DA_Vi18 | 0.2400 |  |
| Jogador 6 | 3-7 | 12:52:12 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-7 | 12:52:13 | VENDEU: Lobo Trevoguari (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 1 | Colosso | DA_Vi18 | -0.4700 |  |
| Jogador 6 | 3-7 | 12:52:13 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 1 | Colosso | DA_Vi18 | 0.7000 |  |
| Jogador 6 | 3-7 | 12:52:14 | MOVE Board -> Board: Vi (i:12.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 1 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 3-7 | 12:52:14 | MOVE Board -> Board: Grompe (i:4.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 1 | Colosso | DA_Vi18 | -0.0200 |  |
| Jogador 6 | 3-7 | 12:52:15 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 1 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 3-7 | 12:52:15 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 1 | Colosso | DA_Vi18 | -0.0400 |  |
| Jogador 6 | 4-1 | 12:52:43 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Colosso | DA_Vi18 | -0.0200 |  |
| Jogador 6 | 4-1 | 12:52:44 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_Vi18 | -0.0200 |  |
| Jogador 6 | 4-1 | 12:52:44 | MOVE Bench -> Board: Akali (i:2.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_Vi18 | -0.4000 |  |
| Jogador 6 | 4-1 | 12:52:45 | MOVE Bench -> Board: Akali (i:2.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_Vi18 | -0.7800 |  |
| Jogador 6 | 4-1 | 12:52:45 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_Vi18 | -0.0400 |  |
| Jogador 6 | 4-2 | 12:53:13 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Colosso | DA_Vi18 | -0.5800 |  |
| Jogador 6 | 4-2 | 12:53:13 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Colosso | DA_Vi18 | 0.9300 |  |
| Jogador 6 | 4-2 | 12:53:14 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Colosso | DA_Vi18 | 0.5000 |  |
| Jogador 6 | 4-2 | 12:53:14 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Colosso | DA_Vi18 | 0.3300 |  |
| Jogador 6 | 4-2 | 12:53:15 | MOVE Bench -> Board: Amumu (i:8.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Colosso | DA_Vi18 | -0.6600 |  |
| Jogador 6 | 4-2 | 12:53:16 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Vi (i:12.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Colosso | DA_Vi18 | 0.1500 |  |
| Jogador 6 | 4-2 | 12:53:16 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Vi (i:12.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Colosso | DA_Vi18 | 0.1400 |  |
| Jogador 6 | 4-2 | 12:53:17 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Vi (i:12.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Colosso | DA_Vi18 | 0.1600 |  |
| Jogador 6 | 4-2 | 12:53:17 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Colosso | DA_Vi18 | -0.1500 |  |
| Jogador 6 | 4-3 | 12:53:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Colosso | DA_Vi18 | 0.4700 |  |
| Jogador 6 | 4-3 | 12:53:46 | MOVE Board -> Board: Grompe (i:4.0) <-> Vi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 4-3 | 12:53:47 | MOVE Board -> Board: Vi (i:12.0) <-> Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Colosso | DA_Vi18 | 0.0800 |  |
| Jogador 6 | 4-3 | 12:53:47 | MOVE Board -> Board: Grompe (i:4.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 4-3 | 12:53:48 | MOVE Board -> Board: Rakan (i:4.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Colosso | DA_Vi18 | -0.0200 |  |
| Jogador 6 | 4-3 | 12:53:48 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Colosso | DA_Vi18 | -0.4500 |  |
| Jogador 6 | 4-4 | 12:54:19 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 4-4 | 12:54:20 | VENDEU: Akali (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Colosso | DA_Vi18 | -0.5900 |  |
| Jogador 6 | 4-4 | 12:54:20 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Colosso | DA_Vi18 | 0.9100 |  |
| Jogador 6 | 4-4 | 12:54:21 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Rakan (i:4.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Colosso | DA_Vi18 | 0.1800 |  |
| Jogador 6 | 4-4 | 12:54:21 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Colosso | DA_Vi18 | -0.4800 |  |
| Jogador 6 | 4-4 | 12:54:21 | MOVE Bench -> Board: Amumu (i:8.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Colosso | DA_Vi18 | -0.3800 |  |
| Jogador 6 | 4-4 | 12:54:22 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Colosso | DA_Vi18 | -0.4600 |  |
| Jogador 6 | 4-5 | 12:54:52 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Colosso | DA_Vi18 | -0.0200 |  |
| Jogador 6 | 4-5 | 12:54:53 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Colosso | DA_Vi18 | 0.2700 |  |
| Jogador 6 | 4-5 | 12:54:53 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Colosso | DA_Vi18 | -0.0700 |  |
| Jogador 6 | 4-5 | 12:54:54 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Colosso | DA_Vi18 | -0.0300 |  |
| Jogador 6 | 4-5 | 12:54:54 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Colosso | DA_Vi18 | 0.9100 |  |
| Jogador 6 | 4-5 | 12:54:55 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Colosso | DA_Vi18 | -0.0700 |  |
| Jogador 6 | 4-5 | 12:54:55 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Colosso | DA_Vi18 | -0.0700 |  |
| Jogador 6 | 4-5 | 12:54:56 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Colosso | DA_Vi18 | -0.5900 |  |
| Jogador 6 | 4-5 | 12:54:56 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Colosso | DA_Vi18 | 1.0200 |  |
| Jogador 6 | 4-6 | 12:55:30 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Colosso | DA_Vi18 | 0.4600 |  |
| Jogador 6 | 4-6 | 12:55:30 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Colosso | DA_Vi18 | 0.2000 |  |
| Jogador 6 | 4-6 | 12:55:31 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Colosso | DA_Vi18 | 0.1700 |  |
| Jogador 6 | 4-6 | 12:55:31 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Colosso | DA_Vi18 | -0.0700 |  |
| Jogador 6 | 4-6 | 12:55:32 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Colosso | DA_Vi18 | -0.0700 |  |
| Jogador 6 | 4-6 | 12:55:32 | VENDEU: Aronguejo (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Colosso | DA_Vi18 | -0.6000 |  |
| Jogador 6 | 4-6 | 12:55:32 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Colosso | DA_Vi18 | 0.4000 |  |
| Jogador 6 | 4-6 | 12:55:33 | MOVE Board -> Board: Sejuani (i:4.0) <-> Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 4-6 | 12:55:34 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Colosso | DA_Vi18 | -0.0700 |  |
| Jogador 6 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Colosso | DA_Vi18 | 0.1700 |  |
| Jogador 6 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Colosso | DA_Vi18 | 0.1000 |  |
| Jogador 6 | 4-7 | 12:56:07 | VENDEU: Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Colosso | DA_Vi18 | -0.0400 |  |
| Jogador 6 | 4-7 | 12:56:07 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Colosso | DA_Vi18 | 0.9400 |  |
| Jogador 6 | 4-7 | 12:56:08 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Colosso | DA_Vi18 | -0.0500 |  |
| Jogador 6 | 4-7 | 12:56:08 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_Vi18 | 0.5000 |  |
| Jogador 6 | 4-7 | 12:56:08 | MOVE Board -> Board: Grompe (i:4.0) <-> Vi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_Vi18 | 0.0100 |  |
| Jogador 6 | 4-7 | 12:56:09 | MOVE Board -> Board: Vi (i:12.0) <-> Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_Vi18 | -0.0600 |  |
| Jogador 6 | 4-7 | 12:56:09 | MOVE Board -> Board: Grompe (i:4.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_Vi18 | 0.0300 |  |
| Jogador 6 | 5-1 | 12:56:41 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Colosso | DA_Vi18 | -0.5900 |  |
| Jogador 6 | 5-1 | 12:56:41 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Colosso | DA_Vi18 | 1.0800 |  |
| Jogador 6 | 5-1 | 12:56:42 | MOVE Bench -> Board: Sejuani (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Colosso | DA_Vi18 | 0.5900 |  |
| Jogador 6 | 5-1 | 12:56:42 | MOVE Board -> Board: Sejuani (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 5-1 | 12:56:43 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Colosso | DA_Vi18 | -0.2800 |  |
| Jogador 6 | 5-1 | 12:56:43 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 5-1 | 12:56:44 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Colosso | DA_Vi18 | -0.0700 |  |
| Jogador 6 | 5-1 | 12:56:45 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Colosso | DA_KogMaw18_AD | 1.0800 |  |
| Jogador 6 | 5-1 | 12:56:45 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Colosso | DA_KogMaw18_AD | 0.4300 |  |
| Jogador 6 | 5-2 | 12:57:20 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Colosso | DA_KogMaw18_AD | 0.5100 |  |
| Jogador 6 | 5-2 | 12:57:20 | VENDEU: Kog'Maw (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Colosso | DA_Vi18 | -0.6000 |  |
| Jogador 6 | 5-2 | 12:57:21 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Colosso | DA_Vi18 | 1.0400 |  |
| Jogador 6 | 5-2 | 12:57:21 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Colosso | DA_Vi18 | 0.4000 |  |
| Jogador 6 | 5-2 | 12:57:22 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_Vi18 | 0.4300 |  |
| Jogador 6 | 5-2 | 12:57:22 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 5-2 | 12:57:23 | MOVE Board -> Board: Sejuani (i:8.0) <-> Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_Vi18 | -0.0200 |  |
| Jogador 6 | 5-2 | 12:57:23 | MOVE Board -> Board: Grompe (i:4.0) <-> Vi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_Vi18 | -0.0200 |  |
| Jogador 6 | 5-2 | 12:57:23 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_Vi18 | -0.5500 |  |
| Jogador 7 | ? | 12:47:30 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 7 | ? | 12:47:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 12:47:37 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 12:47:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 12:47:38 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 12:47:39 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1500 |  |
| Jogador 7 | 1-1 | 12:47:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 12:47:40 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0200 |  |
| Jogador 7 | 1-1 | 12:47:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 1-1 | 12:47:42 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4100 |  |
| Jogador 7 | 1-2 | 12:47:44 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 12:47:45 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 12:47:45 | MOVE Board -> Board: Varus (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.3400 |  |
| Jogador 7 | 1-2 | 12:47:45 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 7 | 1-2 | 12:47:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 12:47:52 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0200 |  |
| Jogador 7 | 1-3 | 12:47:52 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 7 | 1-3 | 12:47:53 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1300 |  |
| Jogador 7 | 1-3 | 12:47:53 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.6400 |  |
| Jogador 7 | 1-3 | 12:47:54 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 7 | 1-3 | 12:47:54 | MOVE Board -> Board: Varus (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 7 | 1-3 | 12:47:55 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0800 |  |
| Jogador 7 | 1-3 | 12:47:55 | MOVE Board -> Board: Akali (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0300 |  |
| Jogador 7 | 1-3 | 12:47:57 | MOVE Board -> Board: Varus (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.3600 |  |
| Jogador 7 | 1-3 | 12:47:58 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0200 |  |
| Jogador 7 | 1-4 | 12:48:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 7 | 1-4 | 12:48:01 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.5800 |  |
| Jogador 7 | 1-4 | 12:48:01 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 7 | 1-4 | 12:48:02 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 7 | 1-4 | 12:48:02 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3500 |  |
| Jogador 7 | 1-4 | 12:48:03 | MOVE Bench -> Board: Shen (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Shen | -0.4000 |  |
| Jogador 7 | 1-4 | 12:48:04 | MOVE Board -> Board: Shen (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0300 |  |
| Jogador 7 | 2-1 | 12:48:10 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 12:48:10 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.6900 |  |
| Jogador 7 | 2-1 | 12:48:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 7 | 2-1 | 12:48:11 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | -0.6300 |  |
| Jogador 7 | 2-1 | 12:48:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.0500 |  |
| Jogador 7 | 2-1 | 12:48:13 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.4200 |  |
| Jogador 7 | 2-1 | 12:48:14 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 7 | 2-1 | 12:48:14 | MOVE Board -> Board: Elise (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 7 | 2-1 | 12:48:15 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0400 |  |
| Jogador 7 | 2-2 | 12:48:21 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Shen | 1.0400 |  |
| Jogador 7 | 2-2 | 12:48:22 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Shen | 0.7800 |  |
| Jogador 7 | 2-2 | 12:48:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Shen | -0.0400 |  |
| Jogador 7 | 2-2 | 12:48:23 | MOVE Board -> Board: Yorick (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-2 | 12:48:23 | MOVE Board -> Board: Shen (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Shen | -0.0100 |  |
| Jogador 7 | 2-2 | 12:48:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-3 | 12:48:33 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 7 | 2-3 | 12:48:34 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.2600 |  |
| Jogador 7 | 2-3 | 12:48:34 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 2-3 | 12:48:35 | MOVE Bench -> Board: Elise (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | -0.1000 |  |
| Jogador 7 | 2-3 | 12:48:36 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 2-3 | 12:48:36 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Sentinel18 | -0.4900 |  |
| Jogador 7 | 2-3 | 12:48:37 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 2-3 | 12:48:37 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 2-3 | 12:48:38 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.3300 |  |
| Jogador 7 | 2-4 | 12:48:47 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_Sentinel18 | 0.3100 |  |
| Jogador 7 | 2-4 | 12:48:48 | MOVE Bench -> Board: Shen (i:4.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 2-4 | 12:48:48 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_Sentinel18 | -0.3900 |  |
| Jogador 7 | 2-4 | 12:48:49 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 12:48:49 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 12:48:49 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 2-4 | 12:48:50 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 12:48:51 | MOVE Board -> Board: Shen (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 12:48:51 | MOVE Board -> Board: Shen (i:4.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-5 | 12:49:02 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_Sentinel18 | 0.9800 |  |
| Jogador 7 | 2-5 | 12:49:02 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_Sentinel18 | 1.0500 |  |
| Jogador 7 | 2-5 | 12:49:03 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_Sentinel18 | 0.2200 |  |
| Jogador 7 | 2-5 | 12:49:04 | MOVE Bench -> Board: Shen (i:8.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_18_Shen | 0.0900 |  |
| Jogador 7 | 2-5 | 12:49:04 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Shen | 0.1800 |  |
| Jogador 7 | 2-5 | 12:49:05 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 7 | 2-5 | 12:49:05 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Shen | 0.4100 |  |
| Jogador 7 | 2-5 | 12:49:06 | MOVE Board -> Board: Yorick (i:2.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-5 | 12:49:06 | MOVE Board -> Board: Varus (i:2.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-6 | 12:49:18 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-6 | 12:49:19 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_18_Shen | -0.1200 |  |
| Jogador 7 | 2-6 | 12:49:20 | MOVE Board -> Board: Shen (i:8.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-6 | 12:49:20 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Shen | -0.1000 |  |
| Jogador 7 | 2-6 | 12:49:20 | MOVE Board -> Board: Yorick (i:2.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-6 | 12:49:21 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 7 | 2-6 | 12:49:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-7 | 12:49:35 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Inferno | DA_18_Shen | 0.1500 |  |
| Jogador 7 | 2-7 | 12:49:36 | MOVE Bench -> Board: Rammus (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Inferno | DA_18_Shen | -0.4000 |  |
| Jogador 7 | 2-7 | 12:49:36 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_18_Shen | 0.1000 |  |
| Jogador 7 | 2-7 | 12:49:37 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 7 | 2-7 | 12:49:37 | MOVE Board -> Board: Azuporã (i:8.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-7 | 12:49:38 | MOVE Board -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 7 | 2-7 | 12:49:38 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 3-1 | 12:49:53 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_18_Shen | 0.3600 |  |
| Jogador 7 | 3-1 | 12:49:53 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Shen | 0.5500 |  |
| Jogador 7 | 3-1 | 12:49:54 | MOVE Board -> Board: Varus (i:2.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 3-1 | 12:49:54 | MOVE Board -> Board: Azuporã (i:8.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 7 | 3-1 | 12:49:55 | MOVE Board -> Board: Rammus (i:6.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-1 | 12:49:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-2 | 12:50:12 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_Sentinel18 | 0.2000 |  |
| Jogador 7 | 3-2 | 12:50:12 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-2 | 12:50:12 | MOVE Board -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-2 | 12:50:13 | MOVE Board -> Board: Shen (i:8.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-2 | 12:50:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-3 | 12:50:31 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 7 | 3-3 | 12:50:32 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.6800 |  |
| Jogador 7 | 3-3 | 12:50:32 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 7 | 3-3 | 12:50:33 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-3 | 12:50:33 | MOVE Board -> Board: Shen (i:8.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-3 | 12:50:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-4 | 12:50:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 3-4 | 12:50:54 | MOVE Board -> Board: Azuporã (i:8.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-4 | 12:50:54 | MOVE Board -> Board: Varus (i:2.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 7 | 3-4 | 12:50:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-5 | 12:51:18 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Inferno | DA_KogMaw18_AD | 0.7300 |  |
| Jogador 7 | 3-5 | 12:51:18 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-5 | 12:51:19 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 7 | 3-5 | 12:51:20 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-5 | 12:51:20 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-5 | 12:51:20 | MOVE Board -> Board: Azuporã (i:8.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-5 | 12:51:21 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-5 | 12:51:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-6 | 12:51:44 | VENDEU: Lobo Trevoguari (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Inferno | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 7 | 3-6 | 12:51:44 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.6500 |  |
| Jogador 7 | 3-6 | 12:51:45 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 7 | 3-6 | 12:51:45 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.6900 |  |
| Jogador 7 | 3-6 | 12:51:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-6 | 12:51:46 | MOVE Board -> Board: Yorick (i:2.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-6 | 12:51:47 | MOVE Board -> Board: Azuporã (i:8.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-6 | 12:51:47 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-7 | 12:52:11 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 7 | 3-7 | 12:52:12 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 3-7 | 12:52:12 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-7 | 12:52:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-7 | 12:52:13 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-7 | 12:52:14 | MOVE Board -> Board: Rammus (i:6.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-7 | 12:52:14 | MOVE Board -> Board: Varus (i:2.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-7 | 12:52:15 | MOVE Board -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-7 | 12:52:15 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-1 | 12:52:43 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-1 | 12:52:44 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-1 | 12:52:44 | MOVE Board -> Board: Varus (i:2.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-1 | 12:52:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-1 | 12:52:45 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-2 | 12:53:13 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Inferno | DA_Sentinel18 | -0.4900 |  |
| Jogador 7 | 4-2 | 12:53:13 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Inferno | DA_Sentinel18 | 0.3800 |  |
| Jogador 7 | 4-2 | 12:53:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Inferno | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 4-2 | 12:53:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Inferno | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 4-2 | 12:53:15 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-2 | 12:53:16 | MOVE Board -> Board: Azuporã (i:8.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-2 | 12:53:16 | MOVE Board -> Board: Rammus (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-2 | 12:53:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-3 | 12:53:46 | VENDEU: Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Inferno | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 4-3 | 12:53:46 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Inferno | DA_CrimsonRaptor18 | 0.6800 |  |
| Jogador 7 | 4-3 | 12:53:47 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Inferno | DA_CrimsonRaptor18 | -0.1000 |  |
| Jogador 7 | 4-3 | 12:53:47 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Inferno | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 7 | 4-3 | 12:53:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 7 | 4-3 | 12:53:48 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 7 | 4-3 | 12:53:49 | MOVE Board -> Board: Shen (i:8.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 7 | 4-3 | 12:53:49 | MOVE Board -> Board: Varus (i:2.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 7 | 4-3 | 12:53:50 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 7 | 4-4 | 12:54:19 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_CrimsonRaptor18 | 0.1400 |  |
| Jogador 7 | 4-4 | 12:54:20 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 7 | 4-4 | 12:54:20 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 7 | 4-4 | 12:54:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 7 | 4-5 | 12:54:52 | VENDEU: Mamãe Bicuda (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 0 | Inferno | DA_Sentinel18 | -0.4900 |  |
| Jogador 7 | 4-5 | 12:54:53 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 0 | Inferno | DA_Sentinel18 | 0.2200 |  |
| Jogador 7 | 4-5 | 12:54:53 | MOVE Board -> Board: Shen (i:8.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-5 | 12:54:54 | MOVE Board -> Board: Varus (i:2.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 0 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-5 | 12:54:54 | MOVE Board -> Board: Rammus (i:6.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 7 | 4-5 | 12:54:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 0 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 7 | 4-6 | 12:55:30 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Inferno | DA_18_Shen | 0.0900 |  |
| Jogador 7 | 4-6 | 12:55:30 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Inferno | DA_18_Shen | 0.7800 |  |
| Jogador 7 | 4-6 | 12:55:31 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Inferno | DA_18_Shen | 0.1500 |  |
| Jogador 7 | 4-6 | 12:55:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Inferno | DA_18_Shen | -0.1100 |  |
| Jogador 7 | 4-6 | 12:55:32 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 22 | 2 | Inferno | DA_18_Shen | 0.0900 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 7 | 4-6 | 12:55:32 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 22 | 2 | Inferno | DA_18_Shen | 0.2300 |  |
| Jogador 7 | 4-6 | 12:55:32 | COMPROU: Grompe (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 20 | 2 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 7 | 4-6 | 12:55:33 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 20 | 2 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 4-6 | 12:55:34 | MOVE Board -> Board: Yorick (i:2.0) <-> Aronguejo (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 20 | 2 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 7 | 4-7 | 12:56:06 | COMPROU: Grompe (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 25 | 2 | Inferno | DA_18_Shen | 0.5200 |  |
| Jogador 7 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Aronguejo (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 25 | 2 | Inferno | DA_18_Shen | 0.1000 |  |
| Jogador 7 | 4-7 | 12:56:07 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_NegatronCloak -> Aronguejo (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 25 | 2 | Inferno | DA_18_Shen | 0.1400 |  |
| Jogador 7 | 4-7 | 12:56:07 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Shen (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 25 | 2 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 4-7 | 12:56:08 | MOVE Board -> Board: Shen (i:8.0) <-> Azuporã (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 25 | 2 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-7 | 12:56:08 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 25 | 2 | Inferno | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 5-1 | 12:56:41 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 30 | 2 | Inferno | DA_Sentinel18 | 0.2700 |  |
| Jogador 7 | 5-1 | 12:56:41 | MOVE Board -> Board: Azuporã (i:8.0) <-> Varus (i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-1 | 12:56:42 | MOVE Board -> Board: Varus (i:2.0) <-> Rammus (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 30 | 2 | Inferno | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-1 | 12:56:42 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 30 | 2 | Inferno | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 5-2 | 12:57:20 | VENDEU: Grompe (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 41 | 3 | Inferno | DA_Sentinel18 | -0.3900 |  |
| Jogador 7 | 5-2 | 12:57:20 | COMPROU: Shen (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Inferno | DA_18_Shen | 0.7800 |  |
| Jogador 7 | 5-2 | 12:57:21 | MOVE Bench -> Board: Shen (i:4.0) <-> Rammus (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Inferno | DA_18_Shen | 0.1000 |  |
| Jogador 7 | 5-2 | 12:57:21 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 7 | 5-2 | 12:57:22 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 7 | 5-2 | 12:57:22 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Inferno | DA_18_Shen | -0.2000 |  |
| Jogador 7 | 5-3 | 12:57:58 | VENDEU: Grompe (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 52 | 4 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 7 | 5-3 | 12:57:58 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 49 | 4 | Inferno | DA_18_Shen | 0.7900 |  |
| Jogador 7 | 5-3 | 12:57:59 | MOVE Bench -> Board: Rammus (i:6.0) <-> Aronguejo (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 49 | 4 | Inferno | DA_18_Shen | -0.6500 |  |
| Jogador 7 | 5-3 | 12:57:59 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Varus (i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 49 | 4 | Inferno | DA_18_Shen | -0.3200 |  |
| Jogador 7 | 5-3 | 12:58:00 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 49 | 4 | Inferno | DA_18_Shen | -0.0500 |  |
| Jogador 7 | 5-4 | 12:58:37 | VENDEU: Yorick (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 60 | 4 | Inferno | DA_18_Shen | -0.5000 |  |
| Jogador 7 | 5-4 | 12:58:38 | COMPROU: Rammus (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 57 | 4 | Inferno | DA_18_Rammus | 0.9000 |  |
| Jogador 7 | 5-4 | 12:58:38 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 57 | 4 | Inferno | DA_18_Rammus | 0.4900 |  |
| Jogador 7 | 5-4 | 12:58:39 | MOVE Board -> Board: Varus (i:2.0) <-> Yorick (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 57 | 4 | Inferno | DA_18_Rammus | -0.0100 |  |
| Jogador 7 | 5-4 | 12:58:39 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 57 | 4 | Inferno | DA_18_Rammus | -0.0100 |  |
| Jogador 7 | 5-4 | 12:58:39 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 57 | 4 | Inferno | DA_18_Rammus | -0.2500 |  |
| Jogador 7 | 5-5 | 12:59:18 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 67 | 5 | Inferno | DA_18_Rammus | 0.1000 |  |
| Jogador 7 | 5-5 | 12:59:19 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 63 | 5 | Inferno | DA_18_Rammus | 0.0000 |  |
| Jogador 7 | 5-5 | 12:59:19 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Aronguejo (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 63 | 5 | Inferno | DA_18_Rammus | -0.3400 |  |
| Jogador 7 | 5-5 | 12:59:20 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Rakan (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 63 | 5 | Inferno | DA_18_Rammus | -0.0200 |  |
| Jogador 7 | 5-5 | 12:59:20 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 63 | 5 | Inferno | DA_18_Rammus | -0.2600 |  |
| Jogador 7 | 5-6 | 13:00:00 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 70 | 5 | Inferno | DA_18_Rammus | 0.6300 |  |
| Jogador 7 | 5-6 | 13:00:01 | VENDEU: Rammus (i:12.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 78 | 5 | Inferno | DA_18_Shen | -0.4600 |  |
| Jogador 7 | 5-6 | 13:00:01 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Inferno | DA_18_Shen | 0.3600 |  |
| Jogador 7 | 5-6 | 13:00:02 | MOVE Bench -> Board: Rakan (i:2.0) <-> Nidalee (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 7 | 5-6 | 13:00:02 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Aronguejo (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Inferno | DA_18_Shen | -0.6600 |  |
| Jogador 7 | 5-6 | 13:00:03 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Inferno | DA_18_Shen | -0.1200 |  |
| Jogador 7 | 5-7 | 13:00:42 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Shen (i:4.0) (tabuleiro slot 12) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 86 | 5 | Inferno | DA_18_Shen | 0.1200 |  |
| Jogador 7 | 5-7 | 13:00:42 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kog'Maw (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 86 | 5 | Inferno | DA_18_Shen | -0.3300 |  |
| Jogador 7 | 5-7 | 13:00:43 | VENDEU: Yorick (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 87 | 5 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 7 | 5-7 | 13:00:43 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Inferno | DA_KogMaw18_AD | 1.0600 |  |
| Jogador 7 | 5-7 | 13:00:44 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Shen (i:4.0) (tabuleiro slot 12) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Inferno | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 7 | 5-7 | 13:00:44 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Shen (i:4.0) (tabuleiro slot 12) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 7 | 5-7 | 13:00:44 | MOVE Bench -> Board: Kog'Maw (i:12.0) <-> Rakan (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 7 | 5-7 | 13:00:45 | MOVE Bench -> Board: Rakan (i:2.0) <-> Aronguejo (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Inferno | DA_KogMaw18_AD | -0.7600 |  |
| Jogador 7 | 5-7 | 13:00:45 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kog'Maw (i:12.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Inferno | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 7 | 6-1 | 13:01:24 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Inferno | DA_KogMaw18_AD | 0.9800 |  |
| Jogador 7 | 6-1 | 13:01:25 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Inferno | DA_KogMaw18_AD | 1.1100 |  |
| Jogador 7 | 6-1 | 13:01:25 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Inferno | DA_Nidalee18_AP | 1.0300 |  |
| Jogador 7 | 6-1 | 13:01:26 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Inferno | DA_Nidalee18_AP | 0.1600 |  |
| Jogador 7 | 6-1 | 13:01:26 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Inferno | DA_Nidalee18_AP | 0.4800 |  |
| Jogador 7 | 6-1 | 13:01:26 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Varus (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Inferno | DA_Nidalee18_AP | -0.0200 |  |
| Jogador 7 | 6-1 | 13:01:27 | MOVE Board -> Board: Varus (i:2.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Inferno | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 7 | 6-1 | 13:01:27 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Inferno | DA_Nidalee18_AP | -0.6700 |  |
| Jogador 7 | 6-2 | 13:02:07 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Inferno | DA_Sentinel18 | 1.1800 |  |
| Jogador 7 | 6-2 | 13:02:07 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Inferno | DA_Sentinel18 | 1.0400 |  |
| Jogador 7 | 6-2 | 13:02:08 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Inferno | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 6-2 | 13:02:08 | MOVE Bench -> Board: Azuporã (i:16.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Inferno | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 6-2 | 13:02:08 | MOVE Board -> Board: Azuporã (i:16.0) <-> Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-2 | 13:02:09 | MOVE Board -> Board: Shen (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-2 | 13:02:09 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Inferno | DA_Sentinel18 | -0.6800 |  |
| Jogador 7 | 6-3 | 13:02:52 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Inferno | DA_Sentinel18 | 1.1800 |  |
| Jogador 7 | 6-3 | 13:02:52 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Inferno | DA_Sentinel18 | 0.2900 |  |
| Jogador 7 | 6-3 | 13:02:53 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Inferno | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 6-3 | 13:02:53 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Inferno | DA_Sentinel18 | 0.5000 |  |
| Jogador 7 | 6-3 | 13:02:54 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Inferno | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 6-3 | 13:02:54 | COMPROU: Varus (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Inferno | DA_Sentinel18 | 1.0100 |  |
| Jogador 7 | 6-3 | 13:02:54 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Inferno | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 6-3 | 13:02:55 | VENDEU: Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Inferno | DA_Sentinel18 | -0.8500 |  |
| Jogador 7 | 6-3 | 13:02:55 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Inferno | DA_Sentinel18 | 0.8000 |  |
| Jogador 7 | 6-4 | 13:03:38 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Shen (i:8.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Inferno | DA_Sentinel18 | 0.1400 |  |
| Jogador 7 | 6-4 | 13:03:38 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Shen (i:8.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Inferno | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 6-4 | 13:03:38 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Shen (i:8.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Inferno | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 6-4 | 13:03:39 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Inferno | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 6-4 | 13:03:39 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Inferno | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 6-4 | 13:03:40 | VENDEU: Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Inferno | DA_Sentinel18 | -0.6000 |  |
| Jogador 7 | 6-4 | 13:03:40 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 99 | 5 | Inferno | DA_Sentinel18 | 0.5100 |  |
| Jogador 7 | 6-4 | 13:03:41 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Inferno | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 6-4 | 13:03:41 | VENDEU: Nidalee (i:16.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Inferno | DA_Sentinel18 | -0.4600 |  |
| Jogador 8 | ? | 12:47:30 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5900 |  |
| Jogador 8 | ? | 12:47:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 12:47:37 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 12:47:38 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0100 |  |
| Jogador 8 | 1-1 | 12:47:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 12:47:42 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-2 | 12:47:44 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | 1-2 | 12:47:45 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-2 | 12:47:45 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-2 | 12:47:45 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-2 | 12:47:46 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3900 |  |
| Jogador 8 | 1-2 | 12:47:46 | MOVE Board -> Board: Leona (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.2400 |  |
| Jogador 8 | 1-2 | 12:47:47 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2000 |  |
| Jogador 8 | 1-2 | 12:47:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-2 | 12:47:48 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-2 | 12:47:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 12:47:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0000 |  |
| Jogador 8 | 1-3 | 12:47:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.1200 |  |
| Jogador 8 | 1-3 | 12:47:53 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.9000 |  |
| Jogador 8 | 1-3 | 12:47:53 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 8 | 1-3 | 12:47:54 | MOVE Board -> Board: Rakan (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 8 | 1-3 | 12:47:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 1-4 | 12:48:00 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.4000 |  |
| Jogador 8 | 1-4 | 12:48:01 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0100 |  |
| Jogador 8 | 1-4 | 12:48:01 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0900 |  |
| Jogador 8 | 1-4 | 12:48:02 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.1600 |  |
| Jogador 8 | 1-4 | 12:48:02 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.1800 |  |
| Jogador 8 | 1-4 | 12:48:03 | MOVE Bench -> Board: Leona (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | -0.0900 |  |
| Jogador 8 | 1-4 | 12:48:04 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.1400 |  |
| Jogador 8 | 2-1 | 12:48:10 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 8 | 2-1 | 12:48:10 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.2200 |  |
| Jogador 8 | 2-1 | 12:48:11 | MOVE Bench -> Board: Xayah (i:2.0) <-> Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | -0.5500 |  |
| Jogador 8 | 2-1 | 12:48:11 | MOVE Bench -> Board: Leona (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | -0.0400 |  |
| Jogador 8 | 2-1 | 12:48:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 2-2 | 12:48:21 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Xayah | 0.9600 |  |
| Jogador 8 | 2-2 | 12:48:22 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.9500 |  |
| Jogador 8 | 2-2 | 12:48:22 | MOVE Bench -> Board: Teemo (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | -0.7500 |  |
| Jogador 8 | 2-2 | 12:48:23 | MOVE Bench -> Board: Rakan (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.4000 |  |
| Jogador 8 | 2-2 | 12:48:23 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.3700 |  |
| Jogador 8 | 2-2 | 12:48:24 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | -0.1000 |  |
| Jogador 8 | 2-2 | 12:48:24 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | -0.6300 |  |
| Jogador 8 | 2-2 | 12:48:25 | MOVE Board -> Board: Rakan (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | -0.2800 |  |
| Jogador 8 | 2-2 | 12:48:25 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | 0.2800 |  |
| Jogador 8 | 2-3 | 12:48:33 | COMPROU: Sejuani (Custo 2 \| i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 13 | 0 | — | DA_18_Veigar | 0.2100 |  |
| Jogador 8 | 2-3 | 12:48:34 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 10 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 8 | 2-3 | 12:48:34 | MOVE Bench -> Board: Xayah (i:2.0) <-> Teemo (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 10 | 0 | — | DA_18_Veigar | 0.0100 |  |
| Jogador 8 | 2-3 | 12:48:35 | MOVE Bench -> Board: Teemo (i:4.0) <-> Leona (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 10 | 0 | — | DA_18_Veigar | -1.0200 |  |
| Jogador 8 | 2-3 | 12:48:36 | MOVE Bench -> Board: Leona (i:4.0) <-> Xayah (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 10 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 8 | 2-3 | 12:48:36 | MOVE Bench -> Board: Xayah (i:2.0) <-> Teemo (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 10 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 8 | 2-3 | 12:48:37 | MOVE Bench -> Board: Teemo (i:4.0) <-> Leona (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 10 | 0 | — | DA_18_Veigar | -0.7000 |  |
| Jogador 8 | 2-3 | 12:48:37 | PASSOU TURNO | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 10 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 8 | 2-4 | 12:48:47 | COMPROU: Warwick (Custo 2 \| i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 15 | 1 | Colosso | DA_18_Veigar | 0.6600 |  |
| Jogador 8 | 2-4 | 12:48:48 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Colosso | DA_18_Veigar | 0.2300 |  |
| Jogador 8 | 2-4 | 12:48:48 | MOVE Bench -> Board: Leona (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Colosso | DA_18_Veigar | 0.3700 |  |
| Jogador 8 | 2-4 | 12:48:49 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_18_Veigar | 0.1100 |  |
| Jogador 8 | 2-4 | 12:48:49 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_18_Veigar | -0.3400 |  |
| Jogador 8 | 2-4 | 12:48:49 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Colosso | DA_18_Veigar | -0.0600 |  |
| Jogador 8 | 2-4 | 12:48:50 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Colosso | DA_18_Veigar | 0.4200 |  |
| Jogador 8 | 2-4 | 12:48:51 | MOVE Board -> Board: Warwick (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 8 | 2-4 | 12:48:51 | MOVE Board -> Board: Rakan (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 8 | 2-5 | 12:49:02 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Veigar | 0.9000 |  |
| Jogador 8 | 2-5 | 12:49:02 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Leona | -0.5800 |  |
| Jogador 8 | 2-5 | 12:49:03 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Leona | 0.1400 |  |
| Jogador 8 | 2-5 | 12:49:04 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Leona | 0.0100 |  |
| Jogador 8 | 2-5 | 12:49:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Leona | -0.1200 |  |
| Jogador 8 | 2-5 | 12:49:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Leona | -0.0400 |  |
| Jogador 8 | 2-5 | 12:49:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Leona | -0.0400 |  |
| Jogador 8 | 2-5 | 12:49:06 | MOVE Board -> Board: Yorick (i:2.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-5 | 12:49:06 | MOVE Board -> Board: Warwick (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 2-6 | 12:49:18 | VENDEU: Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Diana | -0.5000 |  |
| Jogador 8 | 2-6 | 12:49:19 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Diana | 0.8900 |  |
| Jogador 8 | 2-6 | 12:49:20 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 8 | 2-6 | 12:49:20 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Diana | 0.0600 |  |
| Jogador 8 | 2-6 | 12:49:20 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Diana | -0.4500 |  |
| Jogador 8 | 2-6 | 12:49:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Diana | -0.0700 |  |
| Jogador 8 | 2-6 | 12:49:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Diana | -0.0600 |  |
| Jogador 8 | 2-6 | 12:49:22 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Diana | -0.5600 |  |
| Jogador 8 | 2-6 | 12:49:22 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Tristana | 0.2800 |  |
| Jogador 8 | 2-7 | 12:49:35 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Lillia | 0.2200 |  |
| Jogador 8 | 2-7 | 12:49:36 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Lillia | 0.2200 |  |
| Jogador 8 | 2-7 | 12:49:36 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Lillia | 0.4600 |  |
| Jogador 8 | 2-7 | 12:49:37 | MOVE Bench -> Board: Lillia (i:8.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Lillia | -0.3500 |  |
| Jogador 8 | 2-7 | 12:49:37 | MOVE Board -> Board: Lillia (i:8.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 2-7 | 12:49:38 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-1 | 12:49:53 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Lillia | 0.6500 |  |
| Jogador 8 | 3-1 | 12:49:53 | MOVE Board -> Board: Yorick (i:2.0) <-> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-1 | 12:49:54 | MOVE Board -> Board: Warwick (i:4.0) <-> Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Lillia | -0.0700 |  |
| Jogador 8 | 3-1 | 12:49:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-2 | 12:50:12 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Colosso | DA_18_Lillia | -0.4100 |  |
| Jogador 8 | 3-2 | 12:50:12 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_18_Lillia | 0.6400 |  |
| Jogador 8 | 3-2 | 12:50:12 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Colosso | DA_18_Lillia | 0.0600 |  |
| Jogador 8 | 3-2 | 12:50:13 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Colosso | DA_18_Lillia | 0.3000 |  |
| Jogador 8 | 3-2 | 12:50:13 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Colosso | DA_18_Lillia | 0.0500 |  |
| Jogador 8 | 3-2 | 12:50:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Colosso | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-2 | 12:50:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 1 | Colosso | DA_18_Lillia | -0.0900 |  |
| Jogador 8 | 3-2 | 12:50:15 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 1 | Colosso | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-2 | 12:50:15 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 1 | Colosso | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-3 | 12:50:31 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_18_Lillia | -0.3400 |  |
| Jogador 8 | 3-3 | 12:50:32 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Lillia | 0.7300 |  |
| Jogador 8 | 3-3 | 12:50:32 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_18_Lillia | -0.5300 |  |
| Jogador 8 | 3-3 | 12:50:33 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Sejuani | 0.7600 |  |
| Jogador 8 | 3-3 | 12:50:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Sejuani | -0.0900 |  |
| Jogador 8 | 3-3 | 12:50:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Sejuani | 0.0800 |  |
| Jogador 8 | 3-3 | 12:50:34 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Sejuani | 0.6000 |  |
| Jogador 8 | 3-3 | 12:50:35 | MOVE Board -> Board: Rakan (i:2.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Sejuani | -0.0200 |  |
| Jogador 8 | 3-3 | 12:50:35 | MOVE Board -> Board: Lillia (i:8.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Sejuani | -0.0100 |  |
| Jogador 8 | 3-4 | 12:50:53 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Sejuani | 0.6500 |  |
| Jogador 8 | 3-4 | 12:50:54 | MOVE Board -> Board: Yorick (i:2.0) <-> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 8 | 3-4 | 12:50:54 | MOVE Board -> Board: Warwick (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Sejuani | -0.0200 |  |
| Jogador 8 | 3-4 | 12:50:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 8 | 3-5 | 12:51:18 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Colosso | DA_18_Sejuani | 0.2800 |  |
| Jogador 8 | 3-5 | 12:51:18 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 8 | 3-5 | 12:51:19 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Sejuani | 0.0900 |  |
| Jogador 8 | 3-5 | 12:51:20 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_Sejuani | 0.0300 |  |
| Jogador 8 | 3-5 | 12:51:20 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Sejuani | 0.0300 |  |
| Jogador 8 | 3-5 | 12:51:20 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 8 | 3-5 | 12:51:21 | MOVE Board -> Board: Rakan (i:2.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Sejuani | -0.0200 |  |
| Jogador 8 | 3-5 | 12:51:21 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 8 | 3-6 | 12:51:44 | VENDEU: Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 13 | 0 | Colosso | DA_18_Lillia | -0.5000 |  |
| Jogador 8 | 3-6 | 12:51:44 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Colosso | DA_18_Lillia | 0.2500 |  |
| Jogador 8 | 3-6 | 12:51:45 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 13 | 0 | Colosso | DA_18_Lillia | -0.0600 |  |
| Jogador 8 | 3-6 | 12:51:45 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 12 | 0 | Colosso | DA_18_Lillia | 0.1600 |  |
| Jogador 8 | 3-6 | 12:51:46 | MOVE Board -> Board: Lillia (i:8.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 12 | 0 | Colosso | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-6 | 12:51:46 | MOVE Board -> Board: Yorick (i:2.0) <-> Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 12 | 0 | Colosso | DA_18_Lillia | -0.0200 |  |
| Jogador 8 | 3-6 | 12:51:47 | MOVE Board -> Board: Teemo (i:4.0) <-> Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 12 | 0 | Colosso | DA_18_Lillia | -0.0300 |  |
| Jogador 8 | 3-6 | 12:51:47 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 12 | 0 | Colosso | DA_18_Lillia | -0.3200 |  |
| Jogador 8 | 3-7 | 12:52:11 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 21 | 1 | Colosso | DA_18_Lillia | 0.2000 |  |
| Jogador 8 | 3-7 | 12:52:12 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 21 | 1 | Colosso | DA_18_Lillia | 0.2200 |  |
| Jogador 8 | 3-7 | 12:52:12 | VENDEU: Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Colosso | DA_18_Lillia | -0.0400 |  |
| Jogador 8 | 3-7 | 12:52:13 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 19 | 1 | Colosso | DA_18_Lillia | 0.8200 |  |
| Jogador 8 | 3-7 | 12:52:13 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Colosso | DA_18_Lillia | 0.0400 |  |
| Jogador 8 | 3-7 | 12:52:14 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 19 | 1 | Colosso | DA_18_Lillia | 0.2900 |  |
| Jogador 8 | 3-7 | 12:52:14 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Colosso | DA_18_Lillia | -0.0700 |  |
| Jogador 8 | 3-7 | 12:52:15 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Colosso | DA_18_Lillia | -0.3200 |  |
| Jogador 8 | 3-7 | 12:52:15 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Colosso | DA_18_Lillia | 0.2100 |  |
| Jogador 8 | 4-1 | 12:52:43 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 27 | 1 | Colosso | DA_18_Lillia | -0.0400 |  |
| Jogador 8 | 4-1 | 12:52:44 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Colosso | DA_18_Diana | 0.9100 |  |
| Jogador 8 | 4-1 | 12:52:44 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Colosso | DA_18_Diana | -0.0700 |  |
| Jogador 8 | 4-1 | 12:52:45 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 19 | 1 | Colosso | DA_18_Diana | 0.8300 |  |
| Jogador 8 | 4-1 | 12:52:45 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 18 | 1 | Colosso | DA_18_Diana | 0.8700 |  |
| Jogador 8 | 4-1 | 12:52:46 | MOVE Board -> Board: Warwick (i:4.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 18 | 1 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 8 | 4-1 | 12:52:46 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 16 | 1 | Colosso | DA_18_Diana | -0.2600 |  |
| Jogador 8 | 4-1 | 12:52:46 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 16 | 1 | Colosso | DA_18_Diana | 0.0100 |  |
| Jogador 8 | 4-1 | 12:52:47 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 14 | 1 | Colosso | DA_18_Diana | -0.2600 |  |
| Jogador 8 | 4-2 | 12:53:13 | VENDEU: Xayah (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 25 | 1 | Colosso | DA_18_Diana | -0.5800 |  |
| Jogador 8 | 4-2 | 12:53:13 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Colosso | DA_18_Diana | 0.9100 |  |
| Jogador 8 | 4-2 | 12:53:14 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Colosso | DA_18_Diana | 0.1400 |  |
| Jogador 8 | 4-2 | 12:53:14 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Colosso | DA_18_Diana | 0.6100 |  |
| Jogador 8 | 4-2 | 12:53:15 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Kha'Zix (i:6.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Colosso | DA_18_Diana | 0.0800 |  |
| Jogador 8 | 4-2 | 12:53:16 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Kha'Zix (i:6.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Colosso | DA_18_Diana | 0.0500 |  |
| Jogador 8 | 4-2 | 12:53:16 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Colosso | DA_18_Diana | -0.0800 |  |
| Jogador 8 | 4-2 | 12:53:17 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 8 | 4-2 | 12:53:17 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Colosso | DA_18_Diana | -0.4500 |  |
| Jogador 8 | 4-3 | 12:53:46 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 27 | 2 | Colosso | DA_18_Diana | 0.9200 |  |
| Jogador 8 | 4-3 | 12:53:46 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 25 | 2 | Colosso | DA_18_Diana | 0.3400 |  |
| Jogador 8 | 4-3 | 12:53:47 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 23 | 2 | Colosso | DA_18_Diana | 0.8600 |  |
| Jogador 8 | 4-3 | 12:53:47 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 21 | 2 | Colosso | DA_18_Diana | -0.0700 |  |
| Jogador 8 | 4-3 | 12:53:48 | MOVE Bench -> Board: Fiddlesticks (i:12.0) <-> LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 21 | 2 | Colosso | DA_Fiddlesticks18 | 0.4100 |  |
| Jogador 8 | 4-3 | 12:53:48 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 21 | 2 | Colosso | DA_Fiddlesticks18 | -0.2700 |  |
| Jogador 8 | 4-3 | 12:53:49 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 21 | 2 | Colosso | DA_Fiddlesticks18 | 0.1300 |  |
| Jogador 8 | 4-3 | 12:53:49 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 19 | 2 | Colosso | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 8 | 4-3 | 12:53:50 | VENDEU: Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 22 | 2 | Colosso | DA_Fiddlesticks18 | -0.5000 |  |
| Jogador 8 | 4-4 | 12:54:19 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 27 | 2 | Colosso | DA_18_Diana | 0.3500 |  |
| Jogador 8 | 4-4 | 12:54:20 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 25 | 2 | Colosso | DA_18_Diana | -0.0700 |  |
| Jogador 8 | 4-4 | 12:54:20 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Colosso | DA_Fiddlesticks18 | -0.4900 |  |
| Jogador 8 | 4-4 | 12:54:21 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Colosso | DA_Fiddlesticks18 | 0.8600 |  |
| Jogador 8 | 4-4 | 12:54:21 | VENDEU: Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 34 | 2 | Colosso | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 8 | 4-4 | 12:54:21 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Colosso | DA_Fiddlesticks18 | 0.9400 |  |
| Jogador 8 | 4-4 | 12:54:22 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 29 | 2 | Colosso | DA_Fiddlesticks18 | -0.2700 |  |
| Jogador 8 | 4-4 | 12:54:22 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 27 | 2 | Colosso | DA_Fiddlesticks18 | -0.2000 |  |
| Jogador 8 | 4-4 | 12:54:23 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 27 | 2 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 8 | 4-5 | 12:54:52 | VENDEU: LeBlanc (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 39 | 2 | Colosso | DA_Fiddlesticks18 | -0.5800 |  |
| Jogador 8 | 4-5 | 12:54:53 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 36 | 2 | Colosso | DA_Fiddlesticks18 | 0.4100 |  |
| Jogador 8 | 4-5 | 12:54:53 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 2 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 8 | 4-5 | 12:54:54 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Colosso | DA_Fiddlesticks18 | 0.2900 |  |
| Jogador 8 | 4-5 | 12:54:54 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 4-5 | 12:54:55 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Colosso | DA_Fiddlesticks18 | -0.4400 |  |
| Jogador 8 | 4-5 | 12:54:55 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Colosso | DA_Fiddlesticks18 | 0.7600 |  |
| Jogador 8 | 4-5 | 12:54:56 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Colosso | DA_Fiddlesticks18 | -0.5000 |  |
| Jogador 8 | 4-5 | 12:54:56 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 36 | 2 | Colosso | DA_Fiddlesticks18 | 0.4200 |  |
| Jogador 8 | 4-6 | 12:55:30 | VENDEU: Cascalho (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Colosso | DA_Fiddlesticks18 | -0.3400 |  |
| Jogador 8 | 4-6 | 12:55:30 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Colosso | DA_Fiddlesticks18 | 0.7600 |  |
| Jogador 8 | 4-6 | 12:55:31 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Colosso | DA_Fiddlesticks18 | -0.5000 |  |
| Jogador 8 | 4-6 | 12:55:31 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Colosso | DA_Fiddlesticks18 | 0.5700 |  |
| Jogador 8 | 4-6 | 12:55:32 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 4-6 | 12:55:32 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Colosso | DA_Fiddlesticks18 | -0.4400 |  |
| Jogador 8 | 4-6 | 12:55:32 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Colosso | DA_Fiddlesticks18 | 0.5700 |  |
| Jogador 8 | 4-6 | 12:55:33 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Colosso | DA_Fiddlesticks18 | -0.4400 |  |
| Jogador 8 | 4-6 | 12:55:34 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Colosso | DA_Fiddlesticks18 | 0.5700 |  |
| Jogador 8 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Colosso | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 8 | 4-7 | 12:56:06 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NegatronCloak -> Fiddlesticks (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Colosso | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 8 | 4-7 | 12:56:07 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Colosso | DA_Fiddlesticks18 | -0.4500 |  |
| Jogador 8 | 4-7 | 12:56:07 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Colosso | DA_Fiddlesticks18 | 0.4200 |  |
| Jogador 8 | 4-7 | 12:56:08 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Colosso | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 8 | 4-7 | 12:56:08 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Colosso | DA_Fiddlesticks18 | 0.9400 |  |
| Jogador 8 | 4-7 | 12:56:08 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 48 | 4 | Colosso | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 8 | 4-7 | 12:56:09 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 4 | Colosso | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 8 | 4-7 | 12:56:09 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 48 | 4 | Colosso | DA_Fiddlesticks18 | 0.9700 |  |
| Jogador 8 | 5-1 | 12:56:41 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 4 | Colosso | DA_Fiddlesticks18 | -0.9800 |  |
| Jogador 8 | 5-1 | 12:56:41 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Colosso | DA_Fiddlesticks18 | 0.5700 |  |
| Jogador 8 | 5-1 | 12:56:42 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 5-1 | 12:56:42 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Colosso | DA_Fiddlesticks18 | -0.4700 |  |
| Jogador 8 | 5-1 | 12:56:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 4 | Colosso | DA_Fiddlesticks18 | 0.5300 |  |
| Jogador 8 | 5-1 | 12:56:43 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 60 | 4 | Colosso | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 8 | 5-1 | 12:56:44 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Colosso | DA_Fiddlesticks18 | 0.6900 |  |
| Jogador 8 | 5-1 | 12:56:45 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 60 | 4 | Colosso | DA_Fiddlesticks18 | -0.4800 |  |
| Jogador 8 | 5-1 | 12:56:45 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Colosso | DA_Fiddlesticks18 | 0.6900 |  |
| Jogador 8 | 5-2 | 12:57:20 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Colosso | DA_Fiddlesticks18 | -0.4800 |  |
| Jogador 8 | 5-2 | 12:57:20 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 69 | 5 | Colosso | DA_Fiddlesticks18 | 0.5000 |  |
| Jogador 8 | 5-2 | 12:57:21 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Colosso | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 8 | 5-2 | 12:57:21 | COMPROU: Morgana (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Colosso | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 8 | 5-2 | 12:57:22 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 5-2 | 12:57:22 | VENDEU: Morgana (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 8 | 5-2 | 12:57:23 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Colosso | DA_Fiddlesticks18 | 0.5700 |  |
| Jogador 8 | 5-2 | 12:57:23 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Colosso | DA_Fiddlesticks18 | -0.4700 |  |
| Jogador 8 | 5-2 | 12:57:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Colosso | DA_Fiddlesticks18 | 0.2700 |  |
| Jogador 8 | 5-3 | 12:57:58 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Colosso | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 8 | 5-3 | 12:57:58 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Colosso | DA_Fiddlesticks18 | 0.6900 |  |
| Jogador 8 | 5-3 | 12:57:59 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Colosso | DA_Fiddlesticks18 | -0.4800 |  |
| Jogador 8 | 5-3 | 12:57:59 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Colosso | DA_Fiddlesticks18 | 0.6900 |  |
| Jogador 8 | 5-3 | 12:58:00 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 5-3 | 12:58:00 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Colosso | DA_Fiddlesticks18 | -0.4800 |  |
| Jogador 8 | 5-3 | 12:58:01 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Colosso | DA_Fiddlesticks18 | 1.1000 |  |
| Jogador 8 | 5-3 | 12:58:01 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Colosso | DA_Fiddlesticks18 | 1.1000 |  |
| Jogador 8 | 5-3 | 12:58:01 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Colosso | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 8 | 5-4 | 12:58:37 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Colosso | DA_Fiddlesticks18 | 0.5100 |  |
| Jogador 8 | 5-4 | 12:58:38 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Colosso | DA_Fiddlesticks18 | 0.5900 |  |
| Jogador 8 | 5-4 | 12:58:38 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 5-4 | 12:58:39 | VENDEU: Vi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Colosso | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 8 | 5-4 | 12:58:39 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Colosso | DA_Fiddlesticks18 | 0.5900 |  |
| Jogador 8 | 5-4 | 12:58:39 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Colosso | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 8 | 5-4 | 12:58:40 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Colosso | DA_Fiddlesticks18 | 0.4400 |  |
| Jogador 8 | 5-4 | 12:58:41 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 5-4 | 12:58:41 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_Fiddlesticks18 | -0.4500 |  |
| Jogador 8 | 5-5 | 12:59:18 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 99 | 5 | Colosso | DA_Fiddlesticks18 | 1.0400 |  |
| Jogador 8 | 5-5 | 12:59:19 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Colosso | DA_Fiddlesticks18 | -0.4700 |  |
| Jogador 8 | 5-5 | 12:59:19 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Colosso | DA_Fiddlesticks18 | 0.4600 |  |
| Jogador 8 | 5-5 | 12:59:20 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 5-5 | 12:59:20 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_Fiddlesticks18 | -0.3300 |  |
| Jogador 8 | 5-5 | 12:59:21 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Colosso | DA_Fiddlesticks18 | 1.1000 |  |
| Jogador 8 | 5-5 | 12:59:21 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Colosso | DA_Fiddlesticks18 | 0.4700 |  |
| Jogador 8 | 5-5 | 12:59:21 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Colosso | DA_Fiddlesticks18 | 0.2700 |  |
| Jogador 8 | 5-5 | 12:59:22 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 5-6 | 13:00:00 | VENDEU: Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Colosso | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 8 | 5-6 | 13:00:01 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Colosso | DA_Fiddlesticks18 | 0.4500 |  |
| Jogador 8 | 5-6 | 13:00:01 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Colosso | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 8 | 5-6 | 13:00:02 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Colosso | DA_Fiddlesticks18 | 0.2700 |  |
| Jogador 8 | 5-6 | 13:00:02 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Colosso | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 8 | 5-6 | 13:00:03 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Colosso | DA_Fiddlesticks18 | 0.2900 |  |
| Jogador 8 | 5-6 | 13:00:03 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 8 | 5-6 | 13:00:03 | VENDEU: Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Colosso | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 8 | 5-6 | 13:00:04 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 99 | 5 | Colosso | DA_Fiddlesticks18 | 0.9800 |  |
| Jogador 8 | 5-7 | 13:00:42 | EQUIP_FROM_INVENTORY: DA_18_EmblemHunter -> Fiddlesticks (i:12.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 8 | 5-7 | 13:00:42 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Colosso | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 8 | 5-7 | 13:00:43 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Colosso | DA_Fiddlesticks18 | 0.9800 |  |
| Jogador 8 | 5-7 | 13:00:43 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Colosso | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 8 | 5-7 | 13:00:44 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Colosso | DA_Fiddlesticks18 | 1.1100 |  |
| Jogador 8 | 5-7 | 13:00:44 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Colosso | DA_Fiddlesticks18 | 1.1100 |  |
| Jogador 8 | 5-7 | 13:00:44 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Colosso | DA_Fiddlesticks18 | 0.6000 |  |
| Jogador 8 | 5-7 | 13:00:45 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 8 | 5-7 | 13:00:45 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 31 | 36 | 180 | 31 | 17 | 218 | 14 | 37 |
| Jogador 2 | 34 | 43 | 215 | 34 | 17 | 210 | 16 | 35 |
| Jogador 3 | 20 | 25 | 125 | 20 | 11 | 138 | 6 | 20 |
| Jogador 4 | 27 | 27 | 135 | 27 | 16 | 193 | 11 | 41 |
| Jogador 5 | 37 | 62 | 310 | 37 | 17 | 272 | 15 | 36 |
| Jogador 6 | 28 | 35 | 175 | 28 | 16 | 198 | 9 | 28 |
| Jogador 7 | 37 | 44 | 220 | 37 | 18 | 255 | 29 | 54 |
| Jogador 8 | 33 | 50 | 250 | 33 | 17 | 261 | 16 | 26 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 218 | 218 | 218 | 0 | 204 | 0 | 218 | 218 | 218 | 58/43 |
| Jogador 2 | 210 | 210 | 210 | 0 | 202 | 0 | 210 | 210 | 210 | 45/31 |
| Jogador 3 | 138 | 138 | 138 | 0 | 131 | 0 | 138 | 138 | 138 | 33/21 |
| Jogador 4 | 193 | 193 | 193 | 0 | 186 | 0 | 193 | 193 | 193 | 54/38 |
| Jogador 5 | 272 | 272 | 272 | 0 | 264 | 0 | 272 | 272 | 272 | 89/75 |
| Jogador 6 | 198 | 198 | 198 | 0 | 187 | 0 | 198 | 198 | 198 | 53/38 |
| Jogador 7 | 255 | 255 | 255 | 0 | 242 | 0 | 255 | 255 | 255 | 58/44 |
| Jogador 8 | 261 | 261 | 261 | 0 | 251 | 0 | 261 | 261 | 261 | 93/81 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.511091411113739 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23841141164302826 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21238641440868378 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 21 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 22 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017465045675635338 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 23 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.429159551858902 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3453805148601532 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 32 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2616947889328003 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 33 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 35 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0389976501464844 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.021589994430542 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15311625599861145 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13858550786972046 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40421178936958313 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 58 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004885591333732009 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3683207631111145 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0001388133823638782 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5431637167930603 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014911508187651634 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014816210605204105 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 68 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35860857367515564 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 73 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0935075506567955 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 74 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3086712658405304 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 75 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 76 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.386985892779194e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 77 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 78 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0281730890274048 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -ba82e61e-9068-4e02-b710-5419c194d2ff,c448b2c1-7854-4c8c-a51b-eca2791eb639 |
| Jogador 1 | 2-4 | 83 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34000736474990845 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37722671031951904 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 85 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21772412955760956 | 0.0 | 0.0 | +8c5a0cda-86da-4f36-bee3-c2eae934e263 / -— |
| Jogador 1 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 87 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029021887108683586 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 88 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8764728307723999 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 93 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 16.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06652667373418808 | 0.0 | 0.0 | +0c9ac713-08bd-4fa7-a94a-2ab70d7815ff / -— |
| Jogador 1 | 2-5 | 94 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 16.0 | Inferno/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 1 | 2-5 | 95 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 5 | 5 | 0 | 16.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11814960092306137 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 96 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 5 | 5 | 0 | 16.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13305744528770447 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 5 | 0 | 16.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7575307488441467 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 98 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 99 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | Inferno/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0015219066990539432 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | Inferno/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4014248847961426 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 102 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8954623937606812 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 103 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499350786209106 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 104 | BUY | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10903742164373398 | 0.0 | 0.0 | +b32c67a7-6903-403a-9ed6-519ac8487685 / -— |
| Jogador 1 | 2-6 | 105 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3482951819896698 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 106 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3485221266746521 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 107 | PASS | STABILIZE | 100.0 | 5 | 2 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 112 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 18.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07402991503477097 | 0.0 | 0.0 | +acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce / -— |
| Jogador 1 | 2-7 | 113 | SELL | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -af132466-c7bd-40ad-9848-b79d59a5915c |
| Jogador 1 | 2-7 | 114 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20477253198623657 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 1 | 2-7 | 115 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 7 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6511899828910828 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 116 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6374121308326721 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 117 | PASS | STABILIZE | 95.0 | 5 | 7 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 6 | 12 | 1 | 18.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16547586023807526 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 123 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 12 | 1 | 18.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.558829665184021 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 124 | BUY | STABILIZE | 95.0 | 6 | 12 | 1 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47436949610710144 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 1 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 10 | 1 | 20.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38280582427978516 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 126 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 10 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19497564435005188 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 127 | PASS | STABILIZE | 95.0 | 6 | 10 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 132 | SELL | STABILIZE | 95.0 | 6 | 17 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -b32c67a7-6903-403a-9ed6-519ac8487685 |
| Jogador 1 | 3-2 | 133 | BUY | STABILIZE | 95.0 | 6 | 19 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7588727474212646 | 0.0 | 0.0 | +1e504283-c5d1-4eb3-915e-20533ec3a756 / -— |
| Jogador 1 | 3-2 | 134 | BUY_XP | STABILIZE | 95.0 | 6 | 18 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 135 | BUY_XP | STABILIZE | 95.0 | 6 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 136 | BUY_XP | STABILIZE | 95.0 | 6 | 10 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 137 | BUY_XP | STABILIZE | 95.0 | 6 | 6 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006524430587887764 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 139 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 140 | PASS | STABILIZE | 95.0 | 6 | 2 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 142 | SELL | STABILIZE | 95.0 | 6 | 9 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05449003353714943 | 0.0 | 0.0 | +— / -3fc2815d-c456-47c3-bb27-783336b3cdfa |
| Jogador 1 | 3-3 | 143 | BUY | STABILIZE | 95.0 | 6 | 11 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6975045800209045 | 0.0 | 0.0 | +c30e7bdb-41d6-423c-9d7d-2e146472e724 / -— |
| Jogador 1 | 3-3 | 144 | BUY_XP | STABILIZE | 95.0 | 6 | 8 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 145 | BUY_XP | STABILIZE | 95.0 | 6 | 4 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12390176951885223 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 147 | SELL | STABILIZE | 95.0 | 6 | 0 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5218504667282104 | 0.0 | 0.0 | +— / -1e504283-c5d1-4eb3-915e-20533ec3a756 |
| Jogador 1 | 3-3 | 148 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12661924958229065 | 0.0 | 0.0 | +— / -acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce |
| Jogador 1 | 3-3 | 149 | BUY | STABILIZE | 95.0 | 6 | 2 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2551088035106659 | 0.0 | 0.0 | +66b5ed5e-7fdf-4135-a334-e693715e302d / -— |
| Jogador 1 | 3-3 | 150 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05801793187856674 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 152 | BUY | STABILIZE | 85.0 | 6 | 5 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.124105304479599 | 0.0 | 0.0 | +c07fa6e1-195e-4a06-ba8f-b75213704c8a / -— |
| Jogador 1 | 3-4 | 153 | SELL | STABILIZE | 85.0 | 6 | 4 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -66b5ed5e-7fdf-4135-a334-e693715e302d |
| Jogador 1 | 3-4 | 154 | BUY | STABILIZE | 85.0 | 6 | 6 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014683802612125874 | 0.0 | 0.0 | +7a60e1b2-fc20-4070-b163-2f9fb6f93264 / -— |
| Jogador 1 | 3-4 | 155 | BUY_XP | STABILIZE | 85.0 | 6 | 5 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 156 | SELL | STABILIZE | 85.0 | 6 | 1 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023153237998485565 | 0.0 | 0.0 | +— / -7a60e1b2-fc20-4070-b163-2f9fb6f93264 |
| Jogador 1 | 3-4 | 157 | BUY | STABILIZE | 85.0 | 6 | 2 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2746579945087433 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00857488065958023 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27300477027893066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04560345038771629 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 162 | SELL | STABILIZE | 85.0 | 7 | 5 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -bddefab1-7dd7-4954-816c-45dbd44b947b |
| Jogador 1 | 3-5 | 163 | BUY | STABILIZE | 85.0 | 7 | 7 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8359168171882629 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 85.0 | 7 | 5 | 0 | 18.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15043093264102936 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 165 | BUY | STABILIZE | 85.0 | 7 | 5 | 0 | 20.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.287901371717453 | 0.0 | 0.0 | +a9184317-58b7-4804-9aef-3e2c08c20935 / -— |
| Jogador 1 | 3-5 | 166 | BUY_XP | STABILIZE | 85.0 | 7 | 4 | 0 | 20.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 167 | MOVE_BENCH | STABILIZE | 85.0 | 7 | 0 | 0 | 20.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3519571125507355 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 85.0 | 7 | 0 | 0 | 22.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01776222698390484 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 169 | MOVE_BOARD | STABILIZE | 85.0 | 7 | 0 | 0 | 22.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0380372479557991 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 170 | PASS | STABILIZE | 85.0 | 7 | 0 | 0 | 22.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 172 | BUY | STABILIZE | 74.0 | 7 | 6 | 0 | 22.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28599199652671814 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 173 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 4 | 0 | 22.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023034757003188133 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 174 | BUY | STABILIZE | 74.0 | 7 | 4 | 0 | 22.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07726340740919113 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 1 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 0 | 0 | 22.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02327917329967022 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 0 | 0 | 22.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009412364102900028 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 0 | 0 | 22.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014764638617634773 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 178 | PASS | STABILIZE | 74.0 | 7 | 0 | 0 | 22.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 182 | SELL | STABILIZE | 64.0 | 7 | 6 | 0 | 22.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 |
| Jogador 1 | 3-7 | 183 | BUY | STABILIZE | 64.0 | 7 | 11 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.20113462209701538 | 0.0 | 0.0 | +c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 / -— |
| Jogador 1 | 3-7 | 184 | EQUIP_FROM_INVENTORY | STABILIZE | 64.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11189998686313629 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 185 | EQUIP_FROM_INVENTORY | STABILIZE | 64.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15458351373672485 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 186 | EQUIP_FROM_INVENTORY | STABILIZE | 64.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12454041838645935 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 187 | SELL | STABILIZE | 64.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39339616894721985 | 0.0 | 0.0 | +— / -0c9ac713-08bd-4fa7-a94a-2ab70d7815ff |
| Jogador 1 | 3-7 | 188 | BUY | STABILIZE | 64.0 | 7 | 11 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7235320210456848 | 0.0 | 0.0 | +0d8cf876-2884-4724-ab79-246f8e0406f0 / -— |
| Jogador 1 | 3-7 | 189 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10071513801813126 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 190 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45690175890922546 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 64.0 | 7 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23290476202964783 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 64.0 | 7 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2330314815044403 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 194 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6395797729492188 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 195 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08501536399126053 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 196 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7632120847702026 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 197 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07404082268476486 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 198 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 14 | 1 | 20.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03562583401799202 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 199 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7484509944915771 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 200 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 14 | 1 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09992910921573639 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 202 | SELL | STABILIZE | 64.0 | 7 | 21 | 2 | 20.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004942879546433687 | 0.0 | 0.0 | +— / -c30e7bdb-41d6-423c-9d7d-2e146472e724 |
| Jogador 1 | 4-2 | 203 | BUY | STABILIZE | 64.0 | 7 | 24 | 2 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8357636332511902 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -— |
| Jogador 1 | 4-2 | 204 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 23 | 2 | 20.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39616858959198 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 205 | MOVE_BOARD | STABILIZE | 64.0 | 7 | 23 | 2 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01511753723025322 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 206 | PASS | STABILIZE | 64.0 | 7 | 23 | 2 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030714286491274834 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 212 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 30 | 3 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08881638199090958 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 213 | SELL | STABILIZE | 51.0 | 7 | 30 | 3 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030713003128767014 | 0.0 | 0.0 | +— / -c07fa6e1-195e-4a06-ba8f-b75213704c8a |
| Jogador 1 | 4-3 | 214 | BUY | STABILIZE | 51.0 | 7 | 31 | 3 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1443573236465454 | 0.0 | 0.0 | +2357a4df-3c61-4957-83c3-572bbb99ac5a / -— |
| Jogador 1 | 4-3 | 215 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 30 | 3 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 216 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 30 | 3 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997979626059532 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 217 | PASS | STABILIZE | 51.0 | 7 | 30 | 3 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0357142873108387 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 222 | SELL | STABILIZE | 39.0 | 7 | 39 | 3 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05001857504248619 | 0.0 | 0.0 | +— / -2357a4df-3c61-4957-83c3-572bbb99ac5a |
| Jogador 1 | 4-4 | 223 | BUY | STABILIZE | 39.0 | 7 | 40 | 4 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8438761830329895 | 0.0 | 0.0 | +167110eb-b0d0-4873-9ffe-38286dcc5ca2 / -0d8cf876-2884-4724-ab79-246f8e0406f0,c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 |
| Jogador 1 | 4-4 | 224 | BUY | STABILIZE | 39.0 | 7 | 37 | 3 | 22.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05950909107923508 | 0.0 | 0.0 | +7b49fb38-6e0e-4a72-a2ce-0527827d36a6 / -— |
| Jogador 1 | 4-4 | 225 | MOVE_BENCH | STABILIZE | 39.0 | 7 | 34 | 3 | 22.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09982139617204666 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 226 | MOVE_BOARD | FAST8 | 39.0 | 7 | 34 | 3 | 30.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03037792630493641 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 227 | MOVE_BENCH | FAST8 | 39.0 | 7 | 34 | 3 | 30.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3995579183101654 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 228 | PASS | FAST8 | 39.0 | 7 | 34 | 3 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18710476160049438 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 232 | BUY | FAST8 | 39.0 | 7 | 43 | 4 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09542014449834824 | 0.0 | 0.0 | +4c1dab77-0e6d-401b-a341-40117b445957 / -— |
| Jogador 1 | 4-5 | 233 | MOVE_BOARD | FAST8 | 39.0 | 7 | 39 | 3 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.851490176515654e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 234 | MOVE_BOARD | FAST8 | 39.0 | 7 | 39 | 3 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015009153634309769 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 235 | PASS | FAST8 | 39.0 | 7 | 39 | 3 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05245396867394447 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 242 | MOVE_BENCH | FAST8 | 39.0 | 7 | 48 | 4 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08090182393789291 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 243 | MOVE_BENCH | FAST8 | 39.0 | 7 | 48 | 4 | 30.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41067302227020264 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 244 | MOVE_BENCH | FAST8 | 39.0 | 7 | 48 | 4 | 32.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39773181080818176 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 245 | PASS | FAST8 | 39.0 | 7 | 48 | 4 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059238094836473465 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 252 | SELL | FAST8 | 39.0 | 7 | 58 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02043333277106285 | 0.0 | 0.0 | +— / -7b49fb38-6e0e-4a72-a2ce-0527827d36a6 |
| Jogador 1 | 4-7 | 253 | BUY | FAST8 | 39.0 | 7 | 61 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3639562427997589 | 0.0 | 0.0 | +9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 / -— |
| Jogador 1 | 4-7 | 254 | MOVE_BOARD | FAST8 | 39.0 | 7 | 60 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.9422679997660452e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 255 | MOVE_BOARD | FAST8 | 39.0 | 7 | 60 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015026054345071316 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 256 | MOVE_BOARD | FAST8 | 39.0 | 7 | 60 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015034071169793606 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 257 | PASS | FAST8 | 39.0 | 7 | 60 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09794412553310394 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 39.0 | 7 | 71 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14100173115730286 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 39.0 | 7 | 71 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.135064035654068 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 264 | SELL | FAST8 | 39.0 | 7 | 71 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022364621981978416 | 0.0 | 0.0 | +— / -4c1dab77-0e6d-401b-a341-40117b445957 |
| Jogador 1 | 5-1 | 265 | BUY | FAST8 | 39.0 | 7 | 75 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9534791707992554 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 5-1 | 266 | BUY | FAST8 | 39.0 | 7 | 72 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14661046862602234 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -— |
| Jogador 1 | 5-1 | 267 | MOVE_BOARD | FAST8 | 39.0 | 7 | 69 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 268 | MOVE_BOARD | FAST8 | 39.0 | 7 | 69 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014972998760640621 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 269 | PASS | FAST8 | 39.0 | 7 | 69 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.269768625497818 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 272 | BUY | FAST8 | 39.0 | 7 | 80 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8271639943122864 | 0.0 | 0.0 | +3faf4ab2-44b3-4779-985b-658c64791c28 / -— |
| Jogador 1 | 5-2 | 273 | SELL | FAST8 | 39.0 | 7 | 77 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5996000170707703 | 0.0 | 0.0 | +— / -8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 |
| Jogador 1 | 5-2 | 274 | BUY | FAST8 | 39.0 | 7 | 85 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8208386301994324 | 0.0 | 0.0 | +95c9269d-881e-4c24-878b-d65e78fc7230 / -— |
| Jogador 1 | 5-2 | 275 | MOVE_BOARD | FAST8 | 39.0 | 7 | 84 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.5591356461518444e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 276 | SELL | FAST8 | 39.0 | 7 | 84 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4350365102291107 | 0.0 | 0.0 | +— / -9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 |
| Jogador 1 | 5-2 | 277 | BUY | FAST8 | 39.0 | 7 | 85 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3726903796195984 | 0.0 | 0.0 | +dcb61be2-9a58-49bc-9f11-2f5fce42e7ea / -— |
| Jogador 1 | 5-2 | 278 | MOVE_BENCH | FAST8 | 39.0 | 7 | 82 | 5 | 28.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09385049343109131 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 279 | MOVE_BENCH | FAST8 | 39.0 | 7 | 82 | 5 | 30.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4146689176559448 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 280 | BUY_XP | FAST8 | 39.0 | 7 | 82 | 5 | 32.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025599999353289604 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 282 | SELL | ALL_IN | 21.0 | 7 | 88 | 5 | 32.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5935999751091003 | 0.0 | 0.0 | +— / -dcb61be2-9a58-49bc-9f11-2f5fce42e7ea |
| Jogador 1 | 5-3 | 283 | BUY | ALL_IN | 21.0 | 7 | 91 | 5 | 32.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.050339937210083 | 0.0 | 0.0 | +9f1c634e-13c7-4b59-838c-4b676fa059be / -a9184317-58b7-4804-9aef-3e2c08c20935,f384fea6-9b6f-4f9c-81ec-a8284d5ba140 |
| Jogador 1 | 5-3 | 284 | BUY | ALL_IN | 21.0 | 7 | 90 | 5 | 32.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4296303391456604 | 0.0 | 0.0 | +864f332a-0446-4995-b7fb-76d48d293501 / -— |
| Jogador 1 | 5-3 | 285 | BUY | ALL_IN | 21.0 | 7 | 86 | 5 | 32.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17511163651943207 | 0.0 | 0.0 | +1bf15a91-4832-4245-9b48-382a27410263 / -— |
| Jogador 1 | 5-3 | 286 | MOVE_BENCH | ALL_IN | 21.0 | 7 | 84 | 5 | 32.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0876333937048912 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 287 | REROLL | ALL_IN | 21.0 | 7 | 84 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 288 | SELL | ALL_IN | 21.0 | 7 | 82 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5935999751091003 | 0.0 | 0.0 | +— / -9f1c634e-13c7-4b59-838c-4b676fa059be |
| Jogador 1 | 5-3 | 289 | BUY | ALL_IN | 21.0 | 7 | 85 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9607949256896973 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -— |
| Jogador 1 | 5-3 | 290 | EQUIP_FROM_INVENTORY | ALL_IN | 21.0 | 7 | 83 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10777664184570312 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 292 | EQUIP_FROM_INVENTORY | ALL_IN | 5.0 | 7 | 94 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12840574979782104 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 293 | SELL | ALL_IN | 5.0 | 7 | 94 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015490290708839893 | 0.0 | 0.0 | +— / -1bf15a91-4832-4245-9b48-382a27410263 |
| Jogador 1 | 5-4 | 294 | BUY | ALL_IN | 5.0 | 7 | 96 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1661345362663269 | 0.0 | 0.0 | +bfe7ca8a-6e89-4673-b142-262e012398a9 / -— |
| Jogador 1 | 5-4 | 295 | SELL | ALL_IN | 5.0 | 7 | 91 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013333333190530539 | 0.0 | 0.0 | +— / -4518ad1d-87e7-4110-830a-96183c533201 |
| Jogador 1 | 5-4 | 296 | BUY | ALL_IN | 5.0 | 7 | 95 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15425646305084229 | 0.0 | 0.0 | +b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 / -— |
| Jogador 1 | 5-4 | 297 | REROLL | ALL_IN | 5.0 | 7 | 93 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 298 | SELL | ALL_IN | 5.0 | 7 | 91 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030033020302653313 | 0.0 | 0.0 | +— / -b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 |
| Jogador 1 | 5-4 | 299 | BUY | ALL_IN | 5.0 | 7 | 93 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0848257541656494 | 0.0 | 0.0 | +4321582a-0b45-4666-a119-7b49e92d012a / -3a43ff36-dccd-49a7-92d8-0b01e739ea89,3faf4ab2-44b3-4779-985b-658c64791c28 |
| Jogador 1 | 5-4 | 300 | BUY | ALL_IN | 5.0 | 7 | 90 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08974776417016983 | 0.0 | 0.0 | +d47034a1-8b51-4b82-b1b4-5f2aee8f959a / -— |
| Jogador 1 | 5-5 | 302 | BUY | ALL_IN | 5.0 | 7 | 98 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47170811891555786 | 0.0 | 0.0 | +8c4772c9-83f1-4021-b83f-a9ff1773bea0 / -— |
| Jogador 1 | 5-5 | 303 | SELL | ALL_IN | 5.0 | 7 | 95 | 5 | 34.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5996000170707703 | 0.0 | 0.0 | +— / -4321582a-0b45-4666-a119-7b49e92d012a |
| Jogador 1 | 5-5 | 304 | BUY | ALL_IN | 5.0 | 7 | 103 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5013142824172974 | 0.0 | 0.0 | +87902519-e44a-4d4c-9956-ac5aedc9b0c6 / -— |
| Jogador 1 | 5-5 | 305 | BUY_XP | ALL_IN | 5.0 | 7 | 102 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15142999589443207 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 306 | BUY_XP | ALL_IN | 5.0 | 7 | 98 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15068000555038452 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 307 | REROLL | ALL_IN | 5.0 | 7 | 94 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 308 | SELL | ALL_IN | 5.0 | 7 | 92 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019062001258134842 | 0.0 | 0.0 | +— / -d47034a1-8b51-4b82-b1b4-5f2aee8f959a |
| Jogador 1 | 5-5 | 309 | BUY | ALL_IN | 5.0 | 7 | 95 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9570865631103516 | 0.0 | 0.0 | +9a2edb0f-a3cd-455c-8406-2a7ca80e3bc6 / -— |
| Jogador 1 | 5-5 | 310 | MOVE_BENCH | ALL_IN | 5.0 | 7 | 92 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07778608053922653 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 312 | SELL | ALL_IN | 5.0 | 7 | 103 | 5 | 38.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4364297091960907 | 0.0 | 0.0 | +— / -87902519-e44a-4d4c-9956-ac5aedc9b0c6 |
| Jogador 1 | 5-6 | 313 | BUY | ALL_IN | 5.0 | 7 | 104 | 5 | 38.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0890378952026367 | 0.0 | 0.0 | +7fd34ef6-a124-4d23-a166-9f7ad919c826 / -973ba75e-ffa8-41f5-a3fb-e238e34d0216,9a2edb0f-a3cd-455c-8406-2a7ca80e3bc6 |
| Jogador 1 | 5-6 | 314 | BUY | ALL_IN | 5.0 | 7 | 101 | 5 | 32.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4660608470439911 | 0.0 | 0.0 | +24d03668-5dc4-4b40-9439-a1d67522d0a3 / -— |
| Jogador 1 | 5-6 | 315 | MOVE_BENCH | ALL_IN | 5.0 | 7 | 100 | 5 | 32.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4770873188972473 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 316 | BUY | ALL_IN | 5.0 | 7 | 100 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12092264741659164 | 0.0 | 0.0 | +c3596d89-03d2-4fc7-afaf-591f10423252 / -— |
| Jogador 1 | 5-6 | 317 | REROLL | ALL_IN | 5.0 | 7 | 96 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 318 | SELL | ALL_IN | 5.0 | 7 | 94 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5996000170707703 | 0.0 | 0.0 | +— / -7fd34ef6-a124-4d23-a166-9f7ad919c826 |
| Jogador 1 | 5-6 | 319 | BUY | ALL_IN | 5.0 | 7 | 102 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09150940924882889 | 0.0 | 0.0 | +19e8f3ef-c3a6-459e-bf05-a53f742ba05d / -— |
| Jogador 1 | 5-6 | 320 | REROLL | ALL_IN | 5.0 | 7 | 99 | 5 | 34.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.21754200756549835 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03891495615243912 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30128535628318787 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.117924690246582 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 32 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12332182377576828 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 33 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 41 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3083007335662842 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4079068899154663 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 44 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0720279216766357 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1113184317946434 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.491264671087265 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017032800242304802 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 49 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.03777015209198 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18241870403289795 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19648005068302155 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4503774344921112 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2862265110015869 | 0.0 | 0.0 | +18082e05-51e8-4142-b541-c3d7d781b878 / -— |
| Jogador 2 | 2-1 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013835214078426361 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18256588280200958 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 63 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.040596287697553635 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 64 | SELL | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41714125871658325 | 0.0 | 0.0 | +— / -7ca9b803-76eb-4283-9648-7f98bfd81149 |
| Jogador 2 | 2-2 | 65 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1375054121017456 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 66 | BUY_XP | STABILIZE | 95.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.044765785336494446 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 68 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015033424831926823 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 70 | PASS | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33613473176956177 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 73 | SELL | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058266665786504745 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-3 | 74 | BUY | STABILIZE | 90.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05892259255051613 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 75 | BUY_XP | STABILIZE | 90.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.411219984292984 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 77 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020376037806272507 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30938994884490967 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 79 | PASS | STABILIZE | 90.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 82 | BUY | LOSS_STREAK | 84.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28300100564956665 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 83 | BUY | LOSS_STREAK | 84.0 | 5 | 4 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.137313112616539 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 84 | MOVE_BOARD | LOSS_STREAK | 84.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0012883832678198814 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 85 | SELL | LOSS_STREAK | 84.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12459573894739151 | 0.0 | 0.0 | +— / -18082e05-51e8-4142-b541-c3d7d781b878 |
| Jogador 2 | 2-4 | 86 | MOVE_BENCH | LOSS_STREAK | 84.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.294613242149353 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 87 | SELL | LOSS_STREAK | 84.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -11a1c814-5357-4f19-944f-aa11d6bf8384 |
| Jogador 2 | 2-4 | 88 | BUY_XP | LOSS_STREAK | 84.0 | 5 | 6 | 0 | 14.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 89 | SELL | LOSS_STREAK | 84.0 | 5 | 2 | 0 | 14.0 | —/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.652999997138977 | 0.0 | 0.0 | +— / -43759c90-bd65-4632-8aa4-56ab63ae84fe |
| Jogador 2 | 2-4 | 90 | MOVE_BENCH | LOSS_STREAK | 84.0 | 5 | 3 | 0 | 14.0 | —/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2482563555240631 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 92 | BUY | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 10.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3056701719760895 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 93 | MOVE_BENCH | LOSS_STREAK | 84.0 | 5 | 6 | 0 | 10.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38566118478775024 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 94 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 6 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12811166048049927 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 95 | PASS | STABILIZE | 84.0 | 5 | 6 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 102 | BUY | STABILIZE | 78.0 | 5 | 12 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6327764987945557 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 9 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7806544303894043 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 104 | BUY_XP | STABILIZE | 78.0 | 5 | 9 | 0 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 105 | BUY_XP | STABILIZE | 78.0 | 5 | 5 | 0 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 106 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5407987236976624 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 20.0 | Feérico/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017628036439418793 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 20.0 | Feérico/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0016454902943223715 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 109 | PASS | STABILIZE | 78.0 | 6 | 1 | 0 | 20.0 | Feérico/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 112 | BUY | STABILIZE | 78.0 | 6 | 7 | 0 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3621925711631775 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 113 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 3 | 0 | 20.0 | Feérico/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10499230027198792 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 3 | 0 | 22.0 | Feérico/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11500000208616257 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 115 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 3 | 0 | 22.0 | Feérico/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7745389938354492 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 116 | PASS | STABILIZE | 78.0 | 6 | 3 | 0 | 20.0 | Feérico/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 78.0 | 6 | 8 | 0 | 20.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17858447134494781 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 123 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 8 | 0 | 20.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10501084476709366 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 124 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 8 | 0 | 22.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11500000208616257 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 8 | 0 | 22.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7484955787658691 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 126 | PASS | FAST8 | 78.0 | 6 | 8 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 132 | BUY | FAST8 | 78.0 | 6 | 15 | 1 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2173822969198227 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 133 | BUY | FAST8 | 78.0 | 6 | 14 | 1 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7372836470603943 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -— |
| Jogador 2 | 3-2 | 134 | BUY_XP | FAST8 | 78.0 | 6 | 13 | 1 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 135 | BUY_XP | FAST8 | 78.0 | 6 | 9 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 136 | BUY_XP | FAST8 | 78.0 | 6 | 5 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 137 | MOVE_BOARD | FAST8 | 78.0 | 6 | 1 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 138 | MOVE_BOARD | FAST8 | 78.0 | 6 | 1 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 139 | PASS | FAST8 | 78.0 | 6 | 1 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 142 | BUY | FAST8 | 78.0 | 6 | 8 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7339779138565063 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 143 | BUY_XP | FAST8 | 78.0 | 6 | 5 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 144 | MOVE_BOARD | FAST8 | 78.0 | 6 | 1 | 0 | 26.0 | Feérico/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 145 | MOVE_BOARD | FAST8 | 78.0 | 6 | 1 | 0 | 26.0 | Feérico/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01410484779626131 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 146 | PASS | FAST8 | 78.0 | 6 | 1 | 0 | 26.0 | Feérico/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 152 | BUY_XP | FAST8 | 78.0 | 6 | 8 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 153 | BUY_XP | FAST8 | 78.0 | 6 | 4 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 154 | MOVE_BOARD | FAST8 | 78.0 | 6 | 0 | 0 | 26.0 | Feérico/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 155 | MOVE_BOARD | FAST8 | 78.0 | 6 | 0 | 0 | 26.0 | Feérico/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0021026141475886106 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 156 | MOVE_BOARD | FAST8 | 78.0 | 6 | 0 | 0 | 26.0 | Feérico/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015436292625963688 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 157 | MOVE_BOARD | FAST8 | 78.0 | 6 | 0 | 0 | 26.0 | Feérico/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 158 | PASS | FAST8 | 78.0 | 6 | 0 | 0 | 26.0 | Feérico/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 162 | BUY | FAST8 | 78.0 | 7 | 6 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06376467645168304 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 163 | SELL | FAST8 | 78.0 | 7 | 3 | 0 | 26.0 | Feérico/DA_18_Lillia | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 3-5 | 164 | BUY_XP | FAST8 | 78.0 | 7 | 6 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 165 | MOVE_BOARD | FAST8 | 78.0 | 7 | 2 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 166 | MOVE_BOARD | FAST8 | 78.0 | 7 | 2 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 167 | PASS | FAST8 | 78.0 | 7 | 2 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 172 | BUY | FAST8 | 78.0 | 7 | 10 | 1 | 32.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6513106822967529 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-6 | 173 | MOVE_BOARD | FAST8 | 78.0 | 7 | 9 | 0 | 32.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00048012001207098365 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 174 | MOVE_BOARD | FAST8 | 78.0 | 7 | 9 | 0 | 32.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015005126595497131 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 175 | MOVE_BOARD | FAST8 | 78.0 | 7 | 9 | 0 | 32.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 176 | PASS | FAST8 | 78.0 | 7 | 9 | 0 | 32.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 182 | BUY | FAST8 | 66.0 | 7 | 14 | 1 | 32.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7639929056167603 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -0c15e414-bc67-46de-a087-fb7708db0dfe,e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-7 | 183 | BUY_XP | FAST8 | 66.0 | 7 | 11 | 1 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 184 | BUY_XP | FAST8 | 66.0 | 7 | 7 | 0 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 185 | MOVE_BOARD | FAST8 | 66.0 | 7 | 3 | 0 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001856679329648614 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 186 | SELL | FAST8 | 66.0 | 7 | 3 | 0 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5389999747276306 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 3-7 | 187 | BUY_XP | FAST8 | 66.0 | 7 | 11 | 1 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 188 | BUY_XP | FAST8 | 66.0 | 7 | 7 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 189 | MOVE_BOARD | FAST8 | 66.0 | 7 | 3 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 190 | MOVE_BOARD | FAST8 | 66.0 | 7 | 3 | 0 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014605330303311348 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 192 | BUY | FAST8 | 66.0 | 7 | 8 | 0 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7272920608520508 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 2 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 66.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12620168924331665 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 194 | CRAFT_AND_EQUIP | FAST8 | 66.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11010857671499252 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 195 | MOVE_BOARD | FAST8 | 66.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00045494906953535974 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 196 | MOVE_BOARD | FAST8 | 66.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 197 | MOVE_BOARD | FAST8 | 66.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999940060079098 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 198 | PASS | FAST8 | 66.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 202 | MOVE_BOARD | FAST8 | 66.0 | 7 | 11 | 1 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.215588554259739e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 203 | MOVE_BOARD | FAST8 | 66.0 | 7 | 11 | 1 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 204 | PASS | FAST8 | 66.0 | 7 | 11 | 1 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 212 | BUY | FAST8 | 53.0 | 7 | 17 | 1 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21394476294517517 | 0.0 | 0.0 | +696f53ae-1413-47cc-b491-9870b7bcba51 / -— |
| Jogador 2 | 4-3 | 213 | MOVE_BOARD | FAST8 | 53.0 | 7 | 14 | 1 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.619887358283449e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 214 | MOVE_BOARD | FAST8 | 53.0 | 7 | 14 | 1 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015125161036849022 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 215 | MOVE_BOARD | FAST8 | 53.0 | 7 | 14 | 1 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014912835322320461 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 216 | PASS | FAST8 | 53.0 | 7 | 14 | 1 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 222 | BUY | FAST8 | 40.0 | 7 | 21 | 2 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16274309158325195 | 0.0 | 0.0 | +42cf45df-f7dd-418d-a241-d89e69523352 / -— |
| Jogador 2 | 4-4 | 223 | MOVE_BOARD | FAST8 | 40.0 | 7 | 18 | 1 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 224 | MOVE_BOARD | FAST8 | 40.0 | 7 | 18 | 1 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000810846686363 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 225 | PASS | FAST8 | 40.0 | 7 | 18 | 1 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029513226822018623 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 232 | SELL | FAST8 | 40.0 | 7 | 25 | 2 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009100000374019146 | 0.0 | 0.0 | +— / -42cf45df-f7dd-418d-a241-d89e69523352 |
| Jogador 2 | 4-5 | 233 | BUY | FAST8 | 40.0 | 7 | 28 | 2 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7633550763130188 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 2 | 4-5 | 234 | MOVE_BOARD | FAST8 | 40.0 | 7 | 25 | 2 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.238728332798928e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 235 | BUY_XP | FAST8 | 40.0 | 7 | 25 | 2 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 236 | BUY_XP | FAST8 | 40.0 | 7 | 21 | 2 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07395999878644943 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 237 | BUY_XP | FAST8 | 40.0 | 7 | 17 | 1 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 238 | BUY_XP | FAST8 | 40.0 | 7 | 13 | 1 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07395999878644943 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 239 | BUY_XP | FAST8 | 40.0 | 7 | 9 | 0 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 240 | MOVE_BOARD | FAST8 | 40.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.319795597344637e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 242 | SELL | STABILIZE | 27.0 | 8 | 11 | 1 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.525660514831543 | 0.0 | 0.0 | +— / -60255a84-4f78-49f0-a4f1-d598704c7ee7 |
| Jogador 2 | 4-6 | 243 | BUY | STABILIZE | 27.0 | 8 | 14 | 1 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.837851881980896 | 0.0 | 0.0 | +b9b38183-663e-43a4-9f9d-02f1bd4d2d24 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-6 | 244 | MOVE_BENCH | STABILIZE | 27.0 | 8 | 13 | 1 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3039737045764923 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 245 | BUY | STABILIZE | 27.0 | 8 | 13 | 1 | 26.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8376955986022949 | 0.0 | 0.0 | +68301141-c9f1-4303-9775-753520772836 / -9d9dd707-484b-47f6-ac7c-aff2e7e6f48d,f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 4-6 | 246 | BUY | STABILIZE | 27.0 | 8 | 12 | 1 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2266615480184555 | 0.0 | 0.0 | +d366508d-f33b-485a-8ff3-e5d0a248ae3e / -— |
| Jogador 2 | 4-6 | 247 | MOVE_BENCH | STABILIZE | 27.0 | 8 | 10 | 1 | 24.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38184526562690735 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 248 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 10 | 1 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014119051396846771 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 249 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 10 | 1 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014564022421836853 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 250 | PASS | STABILIZE | 27.0 | 8 | 10 | 1 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 252 | BUY | STABILIZE | 27.0 | 8 | 17 | 1 | 32.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2763158082962036 | 0.0 | 0.0 | +50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de / -— |
| Jogador 2 | 4-7 | 253 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 15 | 1 | 32.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003844271879643202 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 254 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 15 | 1 | 32.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011169168166816235 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 255 | PASS | STABILIZE | 27.0 | 8 | 15 | 1 | 32.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08533333241939545 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 262 | BUY | STABILIZE | 27.0 | 8 | 21 | 2 | 36.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3530377745628357 | 0.0 | 0.0 | +a899fe97-90e4-4ae3-941c-af3dee48fed3 / -— |
| Jogador 2 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 27.0 | 8 | 19 | 1 | 36.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15302275121212006 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 27.0 | 8 | 19 | 1 | 36.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11357703059911728 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 265 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 19 | 1 | 36.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.8435813368996605e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 266 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 19 | 1 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014936195686459541 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 267 | PASS | STABILIZE | 27.0 | 8 | 19 | 1 | 36.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12920285761356354 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 272 | BUY | STABILIZE | 27.0 | 8 | 28 | 2 | 36.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1862436980009079 | 0.0 | 0.0 | +6fb5e8f1-2656-486b-9478-161c1b430d5f / -— |
| Jogador 2 | 5-2 | 273 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 24 | 2 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 274 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 24 | 2 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 275 | PASS | STABILIZE | 27.0 | 8 | 24 | 2 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05099809542298317 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 282 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 33 | 3 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.156879865353403e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 283 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 33 | 3 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016837960109114647 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 284 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 33 | 3 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013168446719646454 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 285 | PASS | STABILIZE | 27.0 | 8 | 33 | 3 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06862952560186386 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 292 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 43 | 4 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.5881411172813387e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 293 | SELL | STABILIZE | 27.0 | 8 | 43 | 4 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029200000688433647 | 0.0 | 0.0 | +— / -6fb5e8f1-2656-486b-9478-161c1b430d5f |
| Jogador 2 | 5-4 | 294 | BUY | STABILIZE | 27.0 | 8 | 47 | 4 | 36.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4054701626300812 | 0.0 | 0.0 | +6b7f5603-ce44-4b91-8a3e-939c4fbb26ac / -— |
| Jogador 2 | 5-4 | 295 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 46 | 4 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.4680638287245529e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 296 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 46 | 4 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 297 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 46 | 4 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015003605745732784 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 298 | PASS | STABILIZE | 27.0 | 8 | 46 | 4 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08705714344978333 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 302 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 56 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.8568614652613178e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 303 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 56 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014961542561650276 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 304 | PASS | STABILIZE | 27.0 | 8 | 56 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12875771522521973 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 312 | SELL | STABILIZE | 27.0 | 8 | 69 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44973334670066833 | 0.0 | 0.0 | +— / -a899fe97-90e4-4ae3-941c-af3dee48fed3 |
| Jogador 2 | 5-6 | 313 | BUY | STABILIZE | 27.0 | 8 | 71 | 5 | 36.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34900256991386414 | 0.0 | 0.0 | +4f8541d3-b2a0-4b56-a409-492d4992c419 / -— |
| Jogador 2 | 5-6 | 314 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 67 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00012562175106722862 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 315 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 67 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 316 | PASS | STABILIZE | 27.0 | 8 | 67 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14010876417160034 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 322 | SELL | ALL_IN | 10.0 | 8 | 77 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0006000000284984708 | 0.0 | 0.0 | +— / -d366508d-f33b-485a-8ff3-e5d0a248ae3e |
| Jogador 2 | 5-7 | 323 | BUY | ALL_IN | 10.0 | 8 | 79 | 5 | 36.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9270270466804504 | 0.0 | 0.0 | +c06a964e-4ad5-444a-8800-0410c94f5c1f / -— |
| Jogador 2 | 5-7 | 324 | REROLL | ALL_IN | 10.0 | 8 | 76 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 325 | REROLL | ALL_IN | 10.0 | 8 | 74 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 326 | MOVE_BOARD | ALL_IN | 10.0 | 8 | 72 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 327 | REROLL | ALL_IN | 10.0 | 8 | 72 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 328 | REROLL | ALL_IN | 10.0 | 8 | 70 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 329 | REROLL | ALL_IN | 10.0 | 8 | 68 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 330 | SELL | ALL_IN | 10.0 | 8 | 66 | 5 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5911999940872192 | 0.0 | 0.0 | +— / -6b7f5603-ce44-4b91-8a3e-939c4fbb26ac |
| Jogador 2 | 6-1 | 332 | BUY | ALL_IN | 10.0 | 8 | 77 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.42139551043510437 | 0.0 | 0.0 | +40cd6861-e205-4eb7-900f-d5364fc3c439 / -— |
| Jogador 2 | 6-1 | 333 | EQUIP_FROM_INVENTORY | ALL_IN | 10.0 | 8 | 76 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07410232722759247 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 334 | REROLL | ALL_IN | 10.0 | 8 | 76 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 335 | SELL | ALL_IN | 10.0 | 8 | 74 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4157271683216095 | 0.0 | 0.0 | +— / -40cd6861-e205-4eb7-900f-d5364fc3c439 |
| Jogador 2 | 6-1 | 336 | BUY | ALL_IN | 10.0 | 8 | 75 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1098427772521973 | 0.0 | 0.0 | +e41f7d8d-7662-4445-a1b5-47ad14c9ecb9 / -5489a8f6-2466-4171-b91e-64c367875d3c,584e7960-a541-4d45-8ea1-8a75e288c387 |
| Jogador 2 | 6-1 | 337 | BUY | ALL_IN | 10.0 | 8 | 74 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5179252624511719 | 0.0 | 0.0 | +297d9911-9b62-421e-bb32-76d72c202f1a / -— |
| Jogador 2 | 6-1 | 338 | REROLL | ALL_IN | 10.0 | 8 | 73 | 5 | 36.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 339 | BUY | ALL_IN | 10.0 | 8 | 71 | 5 | 36.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9872450232505798 | 0.0 | 0.0 | +b899f6f0-495e-490e-a4c5-3c81f7d7c739 / -— |
| Jogador 2 | 6-1 | 340 | SELL | ALL_IN | 10.0 | 8 | 67 | 5 | 36.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5935999751091003 | 0.0 | 0.0 | +— / -e41f7d8d-7662-4445-a1b5-47ad14c9ecb9 |
| Jogador 2 | 6-2 | 342 | BUY | ALL_IN | 10.0 | 8 | 81 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5604172945022583 | 0.0 | 0.0 | +7b4ad70b-e8a9-49b1-b23b-318ffe86e226 / -— |
| Jogador 2 | 6-2 | 343 | REROLL | ALL_IN | 10.0 | 8 | 80 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 344 | SELL | ALL_IN | 10.0 | 8 | 78 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5911999940872192 | 0.0 | 0.0 | +— / -7b4ad70b-e8a9-49b1-b23b-318ffe86e226 |
| Jogador 2 | 6-2 | 345 | BUY | ALL_IN | 10.0 | 8 | 79 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1112148761749268 | 0.0 | 0.0 | +ca8383d2-dd2d-47e7-a83a-e79e63f31719 / -696f53ae-1413-47cc-b491-9870b7bcba51,7fb0217d-521c-42b5-995c-81e299b3b934 |
| Jogador 2 | 6-2 | 346 | BUY | ALL_IN | 10.0 | 8 | 76 | 5 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9737995862960815 | 0.0 | 0.0 | +2fce1824-a070-4c9f-aa4c-f834afc2974b / -— |
| Jogador 2 | 6-2 | 347 | BUY | ALL_IN | 10.0 | 8 | 73 | 5 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6936531066894531 | 0.0 | 0.0 | +deb2adfd-36b2-4d5b-a09d-77c8d2650aaf / -— |
| Jogador 2 | 6-2 | 348 | REROLL | ALL_IN | 10.0 | 8 | 71 | 5 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 349 | SELL | ALL_IN | 10.0 | 8 | 69 | 5 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5996000170707703 | 0.0 | 0.0 | +— / -ca8383d2-dd2d-47e7-a83a-e79e63f31719 |
| Jogador 2 | 6-2 | 350 | BUY | ALL_IN | 10.0 | 8 | 77 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0508126020431519 | 0.0 | 0.0 | +b3e5d552-7da1-42e6-9168-d054a829a1e9 / -50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de,deb2adfd-36b2-4d5b-a09d-77c8d2650aaf |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5923603177070618 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15811274945735931 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0395745038986206 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 32 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179677248001099 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 33 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 41 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27028757333755493 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23715084791183472 | 0.0 | 0.0 | +d15ca853-2585-49d0-9d7f-339dae104062 / -— |
| Jogador 3 | 1-4 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9035412669181824 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 45 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22796723246574402 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 46 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0033081681467592716 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013056711293756962 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 49 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0189142227172852 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9622392654418945 | 0.0 | 0.0 | +584812e9-d314-4de0-97e2-604c5c69466c / -— |
| Jogador 3 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2319197803735733 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21813178062438965 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3998023271560669 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01305101066827774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1103581190109253 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -c70251e8-af44-4466-808f-d49e9e5f57e9,d15ca853-2585-49d0-9d7f-339dae104062 |
| Jogador 3 | 2-2 | 63 | BUY | STABILIZE | 95.0 | 4 | 4 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3374418318271637 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 64 | BUY | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08116115629673004 | 0.0 | 0.0 | +39cd170c-5fd5-4fa5-9466-e5595299dbe8 / -— |
| Jogador 3 | 2-2 | 65 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 0 | 0 | 10.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7291963696479797 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 66 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 0 | 0 | 14.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015602880157530308 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 67 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 14.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 72 | BUY | STABILIZE | 88.0 | 4 | 6 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31798991560935974 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 73 | BUY | STABILIZE | 88.0 | 4 | 5 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23806338012218475 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 74 | BUY | STABILIZE | 88.0 | 4 | 3 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14255765080451965 | 0.0 | 0.0 | +475e5206-4f54-4bbb-9db9-99d1895f0887 / -— |
| Jogador 3 | 2-3 | 75 | MOVE_BOARD | STABILIZE | 88.0 | 4 | 1 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 76 | MOVE_BOARD | STABILIZE | 88.0 | 4 | 1 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044919345527887344 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 77 | PASS | STABILIZE | 88.0 | 4 | 1 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 82 | BUY | LOSS_STREAK | 82.0 | 4 | 7 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6880530118942261 | 0.0 | 0.0 | +669a8da1-dcc8-403b-a7af-7c96abdc464d / -— |
| Jogador 3 | 2-4 | 83 | BUY | LOSS_STREAK | 82.0 | 4 | 5 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8604456782341003 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -584812e9-d314-4de0-97e2-604c5c69466c,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 2-4 | 84 | MOVE_BENCH | LOSS_STREAK | 82.0 | 4 | 4 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.636536180973053 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 85 | BUY | LOSS_STREAK | 82.0 | 4 | 4 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07020619511604309 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 86 | MOVE_BENCH | LOSS_STREAK | 82.0 | 4 | 1 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7496781945228577 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 87 | MOVE_BENCH | LOSS_STREAK | 82.0 | 4 | 1 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1055365577340126 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 88 | MOVE_BENCH | LOSS_STREAK | 82.0 | 4 | 1 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10478617995977402 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 89 | MOVE_BENCH | LOSS_STREAK | 82.0 | 4 | 1 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7643527388572693 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 90 | PASS | LOSS_STREAK | 82.0 | 4 | 1 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 92 | BUY | LOSS_STREAK | 82.0 | 4 | 7 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8247595429420471 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 93 | SELL | LOSS_STREAK | 82.0 | 4 | 6 | 0 | 14.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05503333359956741 | 0.0 | 0.0 | +— / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63 |
| Jogador 3 | 2-5 | 94 | BUY | STABILIZE | 82.0 | 4 | 9 | 0 | 14.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8057833313941956 | 0.0 | 0.0 | +03a4a455-ebf6-4587-8ab3-acd2b1038822 / -— |
| Jogador 3 | 2-5 | 95 | MOVE_BENCH | STABILIZE | 82.0 | 4 | 8 | 0 | 14.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08891696482896805 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 96 | SELL | STABILIZE | 82.0 | 4 | 8 | 0 | 18.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -8a384047-bcc4-4d79-8896-30170e9313cd |
| Jogador 3 | 2-5 | 97 | BUY | STABILIZE | 82.0 | 4 | 11 | 1 | 18.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.928411066532135 | 0.0 | 0.0 | +492fa74a-22b8-4f7d-a4f9-346fdcf565be / -03a4a455-ebf6-4587-8ab3-acd2b1038822,5ead8548-7453-4fa1-856e-674995576a48 |
| Jogador 3 | 2-5 | 98 | EQUIP_FROM_INVENTORY | STABILIZE | 82.0 | 4 | 10 | 1 | 18.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06025766581296921 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 99 | EQUIP_FROM_INVENTORY | STABILIZE | 82.0 | 4 | 10 | 1 | 18.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07010608911514282 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 100 | BUY | STABILIZE | 82.0 | 4 | 10 | 1 | 18.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21075980365276337 | 0.0 | 0.0 | +cdb48eea-209d-4833-9a68-79df61990332 / -— |
| Jogador 3 | 2-6 | 102 | BUY | STABILIZE | 82.0 | 5 | 13 | 1 | 18.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9498885869979858 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 82.0 | 5 | 12 | 1 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03527313470840454 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 82.0 | 5 | 12 | 1 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06399083137512207 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 105 | BUY | STABILIZE | 82.0 | 5 | 12 | 1 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33438995480537415 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -— |
| Jogador 3 | 2-6 | 106 | MOVE_BENCH | STABILIZE | 82.0 | 5 | 10 | 1 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05354064702987671 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 107 | MOVE_BENCH | STABILIZE | 82.0 | 5 | 10 | 1 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18304790556430817 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 82.0 | 5 | 10 | 1 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01805875450372696 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 109 | PASS | STABILIZE | 82.0 | 5 | 10 | 1 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 112 | BUY | STABILIZE | 75.0 | 5 | 16 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8962494134902954 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 113 | BUY | STABILIZE | 75.0 | 5 | 13 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16800576448440552 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 114 | MOVE_BOARD | STABILIZE | 75.0 | 5 | 12 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0035383186768740416 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 75.0 | 5 | 12 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 75.0 | 5 | 12 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01646578498184681 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 117 | PASS | STABILIZE | 75.0 | 5 | 12 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 75.0 | 5 | 18 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19225849211215973 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 123 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 18 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3951307535171509 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 124 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 18 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5363505482673645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 125 | PASS | STABILIZE | 75.0 | 5 | 18 | 1 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 132 | MOVE_BENCH | STABILIZE | 65.0 | 5 | 25 | 2 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09822089225053787 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 133 | MOVE_BENCH | STABILIZE | 65.0 | 5 | 25 | 2 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4121324419975281 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 65.0 | 5 | 25 | 2 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5362606048583984 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 135 | PASS | STABILIZE | 65.0 | 5 | 25 | 2 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02250000089406967 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 142 | MOVE_BENCH | STABILIZE | 54.0 | 5 | 33 | 3 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6120816469192505 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 143 | MOVE_BENCH | STABILIZE | 54.0 | 5 | 33 | 3 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.040462199598550797 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 144 | MOVE_BENCH | STABILIZE | 54.0 | 5 | 33 | 3 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13060806691646576 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 145 | MOVE_BENCH | STABILIZE | 54.0 | 5 | 33 | 3 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20720618963241577 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 146 | MOVE_BENCH | STABILIZE | 54.0 | 5 | 33 | 3 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0873718112707138 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 147 | MOVE_BENCH | STABILIZE | 54.0 | 5 | 33 | 3 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39952290058135986 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 148 | MOVE_BENCH | STABILIZE | 54.0 | 5 | 33 | 3 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5208450555801392 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 149 | PASS | STABILIZE | 54.0 | 5 | 33 | 3 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026499999687075615 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 152 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 42 | 4 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10156521201133728 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 153 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 42 | 4 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41371628642082214 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 42 | 4 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03737940266728401 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 155 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 42 | 4 | 28.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08461374044418335 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 156 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 42 | 4 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4183111786842346 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 157 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 42 | 4 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08190431445837021 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 42.0 | 5 | 42 | 4 | 28.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005264488863758743 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 159 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 42 | 4 | 28.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07246582210063934 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 160 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 42 | 4 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1016470417380333 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 162 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 52 | 5 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.939288318157196 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 163 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 52 | 5 | 28.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.051403652876615524 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 52 | 5 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25435131788253784 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 165 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 52 | 5 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8278281688690186 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 52 | 5 | 28.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05654027685523033 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 167 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 52 | 5 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.448640912771225 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 168 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 52 | 5 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13862060010433197 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 169 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 52 | 5 | 28.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4277909994125366 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 170 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 52 | 5 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07015951722860336 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 172 | SELL | STABILIZE | 32.0 | 5 | 64 | 5 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5960000157356262 | 0.0 | 0.0 | +— / -e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 3-6 | 173 | BUY | STABILIZE | 32.0 | 5 | 69 | 5 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32492056488990784 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -— |
| Jogador 3 | 3-6 | 174 | SELL | STABILIZE | 32.0 | 5 | 68 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5935999751091003 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 3-6 | 175 | BUY | STABILIZE | 32.0 | 5 | 71 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.876822829246521 | 0.0 | 0.0 | +1489b596-9339-407a-b49f-d01ecfdd6f78 / -— |
| Jogador 3 | 3-6 | 176 | MOVE_BENCH | STABILIZE | 32.0 | 5 | 70 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3655480146408081 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 177 | MOVE_BENCH | STABILIZE | 32.0 | 5 | 70 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20578470826148987 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 178 | MOVE_BENCH | STABILIZE | 32.0 | 5 | 70 | 5 | 18.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5387604832649231 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 179 | MOVE_BENCH | STABILIZE | 32.0 | 5 | 70 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38725823163986206 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 180 | PASS | STABILIZE | 32.0 | 5 | 70 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.084140844643116 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 182 | MOVE_BENCH | ALL_IN | 21.0 | 5 | 83 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18519839644432068 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 183 | SELL | ALL_IN | 21.0 | 5 | 83 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018799999728798866 | 0.0 | 0.0 | +— / -39cd170c-5fd5-4fa5-9466-e5595299dbe8 |
| Jogador 3 | 3-7 | 184 | BUY | ALL_IN | 21.0 | 5 | 84 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4103439748287201 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-7 | 185 | REROLL | ALL_IN | 21.0 | 5 | 81 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 186 | REROLL | ALL_IN | 21.0 | 5 | 79 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 187 | SELL | ALL_IN | 21.0 | 5 | 77 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4737669825553894 | 0.0 | 0.0 | +— / -475e5206-4f54-4bbb-9db9-99d1895f0887 |
| Jogador 3 | 3-7 | 188 | BUY | ALL_IN | 21.0 | 5 | 79 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8945081830024719 | 0.0 | 0.0 | +a4188ec8-4188-4fdf-8d76-c559fc0c7daf / -— |
| Jogador 3 | 3-7 | 189 | REROLL | ALL_IN | 21.0 | 5 | 76 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 190 | SELL | ALL_IN | 21.0 | 5 | 74 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03173818066716194 | 0.0 | 0.0 | +— / -669a8da1-dcc8-403b-a7af-7c96abdc464d |
| Jogador 3 | 4-1 | 192 | CRAFT_AND_EQUIP | ALL_IN | 21.0 | 5 | 89 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1709197610616684 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 193 | CRAFT_AND_EQUIP | ALL_IN | 21.0 | 5 | 89 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1532994955778122 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 194 | MOVE_BENCH | ALL_IN | 21.0 | 5 | 89 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42362985014915466 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 195 | MOVE_BENCH | ALL_IN | 21.0 | 5 | 89 | 5 | 26.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026791954413056374 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 196 | MOVE_BENCH | ALL_IN | 21.0 | 5 | 89 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3294079303741455 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 197 | REROLL | ALL_IN | 21.0 | 5 | 89 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 198 | MOVE_BENCH | ALL_IN | 21.0 | 5 | 87 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4907837510108948 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 199 | MOVE_BENCH | ALL_IN | 21.0 | 5 | 87 | 5 | 26.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023123105987906456 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 200 | PASS | ALL_IN | 21.0 | 5 | 87 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6206663250923157 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 202 | BUY | ALL_IN | 9.0 | 6 | 100 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9609707593917847 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -— |
| Jogador 3 | 4-2 | 203 | MOVE_BENCH | ALL_IN | 9.0 | 6 | 98 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2429613322019577 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 204 | MOVE_BENCH | ALL_IN | 9.0 | 6 | 98 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40452924370765686 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 205 | BUY | ALL_IN | 9.0 | 6 | 98 | 5 | 28.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9531727433204651 | 0.0 | 0.0 | +cb30dcaa-bc26-4584-9b50-24e47e70fcb0 / -— |
| Jogador 3 | 4-2 | 206 | REROLL | ALL_IN | 9.0 | 6 | 96 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 207 | SELL | ALL_IN | 9.0 | 6 | 94 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5911999940872192 | 0.0 | 0.0 | +— / -e2f28d51-690c-476e-b097-e5c69258f933 |
| Jogador 3 | 4-2 | 208 | BUY | ALL_IN | 9.0 | 6 | 95 | 5 | 28.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9632866978645325 | 0.0 | 0.0 | +8455b875-27e0-4172-9311-5cbb3e2242b9 / -— |
| Jogador 3 | 4-2 | 209 | SELL | ALL_IN | 9.0 | 6 | 92 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5911999940872192 | 0.0 | 0.0 | +— / -99511886-d1a7-4910-b099-5072e5385c63 |
| Jogador 3 | 4-2 | 210 | BUY | ALL_IN | 9.0 | 6 | 93 | 5 | 28.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0715073347091675 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -a4188ec8-4188-4fdf-8d76-c559fc0c7daf,cdb48eea-209d-4833-9a68-79df61990332 |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5923603177070618 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16539067029953003 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1359414905309677 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 32 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032739195972681046 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 33 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004173798952251673 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 36 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 41 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3951285779476166 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.633777379989624 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 44 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2853133976459503 | 0.0 | 0.0 | +b29f76e2-456d-4abf-b9a2-a4a80b577187 / -— |
| Jogador 4 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013970951549708843 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 46 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 1-4 | 47 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20905360579490662 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00029346661176532507 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 49 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10604772716760635 | 0.0 | 0.0 | +— / -b29f76e2-456d-4abf-b9a2-a4a80b577187 |
| Jogador 4 | 1-4 | 50 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4963333308696747 | 0.0 | 0.0 | +— / -4fbb2e46-1524-47c6-85a1-79266fd4da28 |
| Jogador 4 | 1-4 | 51 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07966666668653488 | 0.0 | 0.0 | +— / -95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 1-4 | 52 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0034171342849731 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -— |
| Jogador 4 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0398086309432983 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24012206494808197 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19971008598804474 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.587586522102356 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09787862002849579 | 0.0 | 0.0 | +b166276e-305e-4945-8398-7c8b4b86ca9e / -— |
| Jogador 4 | 2-1 | 59 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.948525202053133e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9622445702552795 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 63 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15488101541996002 | 0.0 | 0.0 | +e989a0cc-848a-4c45-b153-315877aee8f7 / -— |
| Jogador 4 | 2-2 | 64 | SELL | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0728333368897438 | 0.0 | 0.0 | +— / -b166276e-305e-4945-8398-7c8b4b86ca9e |
| Jogador 4 | 2-2 | 65 | BUY | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042398665100336075 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -— |
| Jogador 4 | 2-2 | 66 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09941677749156952 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 67 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21781885623931885 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 2-2 | 68 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 2 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00033785635605454445 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 2 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15737420320510864 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 70 | PASS | STABILIZE | 95.0 | 4 | 2 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 72 | BUY | STABILIZE | 89.0 | 4 | 8 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.959809422492981 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -cd27dcd8-0a45-4196-be66-fbe6eb4a0793,eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-3 | 73 | BUY | STABILIZE | 89.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31909212470054626 | 0.0 | 0.0 | +89740fc1-ac0c-4a0b-9e85-1832d5c3acc4 / -— |
| Jogador 4 | 2-3 | 74 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24696342647075653 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 75 | BUY_XP | STABILIZE | 89.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5221822261810303 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 77 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0003769167815335095 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042034972459077835 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 79 | PASS | STABILIZE | 89.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 82 | BUY | STABILIZE | 89.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1643054187297821 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 83 | BUY | STABILIZE | 89.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16767214238643646 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 84 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 85 | SELL | STABILIZE | 89.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6126222014427185 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-4 | 86 | SELL | STABILIZE | 89.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13833333551883698 | 0.0 | 0.0 | +— / -89740fc1-ac0c-4a0b-9e85-1832d5c3acc4 |
| Jogador 4 | 2-4 | 87 | BUY_XP | STABILIZE | 89.0 | 5 | 4 | 0 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 88 | SELL | STABILIZE | 89.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058266665786504745 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 89 | SELL | STABILIZE | 89.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11433333158493042 | 0.0 | 0.0 | +— / -9db562a0-c8a9-4291-8623-b7b6afbf2606 |
| Jogador 4 | 2-4 | 90 | BUY | STABILIZE | 89.0 | 5 | 4 | 0 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18329653143882751 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-5 | 92 | BUY | STABILIZE | 89.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0166760683059692 | 0.0 | 0.0 | +3825a7ba-319f-48f8-ad2d-8c24eabbc1cc / -— |
| Jogador 4 | 2-5 | 93 | BUY | STABILIZE | 89.0 | 5 | 5 | 0 | 16.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3607882857322693 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 4 | 2-5 | 94 | BUY | STABILIZE | 89.0 | 5 | 3 | 0 | 16.0 | Florescer/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6143243908882141 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -— |
| Jogador 4 | 2-5 | 95 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 2 | 0 | 16.0 | Florescer/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5467044711112976 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 96 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 2 | 0 | 16.0 | Florescer/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3415433168411255 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 2 | 0 | 16.0 | Florescer/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0767173320055008 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 98 | SELL | STABILIZE | 89.0 | 5 | 2 | 0 | 16.0 | Florescer/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5092611908912659 | 0.0 | 0.0 | +— / -8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 3 | 0 | 16.0 | Florescer/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6624012589454651 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 3 | 0 | 16.0 | Florescer/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19861748814582825 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 102 | BUY | STABILIZE | 89.0 | 5 | 10 | 1 | 22.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27425631880760193 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 103 | BUY | STABILIZE | 89.0 | 5 | 7 | 0 | 22.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3149300217628479 | 0.0 | 0.0 | +814d07bd-0296-44af-9626-26a8a224d86f / -— |
| Jogador 4 | 2-6 | 104 | BUY | STABILIZE | 89.0 | 5 | 6 | 0 | 22.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3152706027030945 | 0.0 | 0.0 | +f71a7192-663d-46a0-93ef-b900c59c3bde / -— |
| Jogador 4 | 2-6 | 105 | BUY_XP | STABILIZE | 89.0 | 5 | 4 | 0 | 22.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 106 | SELL | STABILIZE | 89.0 | 5 | 0 | 0 | 22.0 | Florescer/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21301904320716858 | 0.0 | 0.0 | +— / -814d07bd-0296-44af-9626-26a8a224d86f |
| Jogador 4 | 2-6 | 107 | SELL | STABILIZE | 89.0 | 5 | 1 | 0 | 22.0 | Florescer/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.489642858505249 | 0.0 | 0.0 | +— / -f71a7192-663d-46a0-93ef-b900c59c3bde |
| Jogador 4 | 2-6 | 108 | SELL | STABILIZE | 89.0 | 5 | 3 | 0 | 22.0 | Florescer/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6005100011825562 | 0.0 | 0.0 | +— / -c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 4 | 2-6 | 109 | BUY_XP | STABILIZE | 89.0 | 5 | 5 | 0 | 22.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 110 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 1 | 0 | 22.0 | Florescer/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5827678442001343 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 112 | BUY | STABILIZE | 89.0 | 6 | 8 | 0 | 24.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36644431948661804 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 113 | BUY | STABILIZE | 89.0 | 6 | 5 | 0 | 24.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36736589670181274 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -— |
| Jogador 4 | 2-7 | 114 | BUY_XP | STABILIZE | 89.0 | 6 | 4 | 0 | 24.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 115 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 0 | 0 | 24.0 | Florescer/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05902447924017906 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 116 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 0 | 0 | 24.0 | Florescer/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3958600163459778 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 117 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 0 | 0 | 24.0 | Florescer/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08854866027832031 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 118 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 0 | 0 | 24.0 | Florescer/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005851816385984421 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 0 | 0 | 24.0 | Florescer/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 120 | PASS | STABILIZE | 89.0 | 6 | 0 | 0 | 24.0 | Florescer/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 89.0 | 6 | 6 | 0 | 24.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23625905811786652 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 123 | BUY | STABILIZE | 89.0 | 6 | 6 | 0 | 24.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2808052897453308 | 0.0 | 0.0 | +8052731e-e34c-4de7-84b1-2b986cfeddaa / -— |
| Jogador 4 | 3-1 | 124 | BUY_XP | STABILIZE | 89.0 | 6 | 4 | 0 | 24.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 0 | 0 | 24.0 | Florescer/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.584292582876515e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 126 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 0 | 0 | 24.0 | Florescer/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08034022897481918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 127 | SELL | STABILIZE | 89.0 | 6 | 0 | 0 | 24.0 | Florescer/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19566667079925537 | 0.0 | 0.0 | +— / -8052731e-e34c-4de7-84b1-2b986cfeddaa |
| Jogador 4 | 3-1 | 128 | SELL | STABILIZE | 89.0 | 6 | 2 | 0 | 24.0 | Florescer/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -4a0403a3-c999-4d4c-83f0-7270e8576aed |
| Jogador 4 | 3-1 | 129 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 3 | 0 | 24.0 | Florescer/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32590141892433167 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 130 | SELL | FAST8 | 89.0 | 6 | 3 | 0 | 28.0 | Florescer/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4901779890060425 | 0.0 | 0.0 | +— / -4b07138d-44fd-4515-8b65-d7db84f4639c |
| Jogador 4 | 3-2 | 132 | BUY | FAST8 | 89.0 | 6 | 11 | 1 | 28.0 | Florescer/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7679678201675415 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 133 | BUY | FAST8 | 89.0 | 6 | 10 | 1 | 26.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13799521327018738 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 134 | BUY | FAST8 | 89.0 | 6 | 9 | 0 | 26.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21048109233379364 | 0.0 | 0.0 | +421bcbcb-ecb2-4af8-88d4-7be6cd284d27 / -— |
| Jogador 4 | 3-2 | 135 | MOVE_BENCH | FAST8 | 89.0 | 6 | 6 | 0 | 26.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6001043319702148 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 136 | MOVE_BOARD | FAST8 | 89.0 | 6 | 6 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 137 | MOVE_BOARD | FAST8 | 89.0 | 6 | 6 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 138 | PASS | FAST8 | 89.0 | 6 | 6 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 142 | BUY | FAST8 | 78.0 | 6 | 11 | 1 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12137051671743393 | 0.0 | 0.0 | +52018505-08c9-471f-83b9-fd5066efe55a / -— |
| Jogador 4 | 3-3 | 143 | BUY | FAST8 | 78.0 | 6 | 9 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0232553631067276 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 144 | MOVE_BOARD | FAST8 | 78.0 | 6 | 8 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002103325678035617 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 145 | MOVE_BOARD | FAST8 | 78.0 | 6 | 8 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013167286291718483 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 146 | PASS | FAST8 | 78.0 | 6 | 8 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 152 | BUY | FAST8 | 68.0 | 6 | 14 | 1 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7330762147903442 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 153 | BUY | FAST8 | 68.0 | 6 | 11 | 1 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.639206051826477 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 4 | 3-4 | 154 | SELL | FAST8 | 68.0 | 6 | 9 | 0 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05649999901652336 | 0.0 | 0.0 | +— / -ac8f2a7d-1627-4aa4-a35b-805bce651b0e |
| Jogador 4 | 3-4 | 155 | BUY | FAST8 | 68.0 | 6 | 10 | 1 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3246411085128784 | 0.0 | 0.0 | +4cf7dfe2-9d2c-4d45-803e-503eda810357 / -— |
| Jogador 4 | 3-4 | 156 | MOVE_BOARD | FAST8 | 68.0 | 6 | 8 | 0 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 157 | MOVE_BOARD | FAST8 | 68.0 | 6 | 8 | 0 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014742020517587662 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 158 | PASS | FAST8 | 68.0 | 6 | 8 | 0 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 162 | SELL | FAST8 | 68.0 | 6 | 14 | 1 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44066667556762695 | 0.0 | 0.0 | +— / -4cf7dfe2-9d2c-4d45-803e-503eda810357 |
| Jogador 4 | 3-5 | 163 | BUY | FAST8 | 68.0 | 6 | 16 | 1 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.759086012840271 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -52018505-08c9-471f-83b9-fd5066efe55a,7fd03119-ac82-49e1-b3bb-3a0caa31011f |
| Jogador 4 | 3-5 | 164 | BUY | FAST8 | 68.0 | 6 | 14 | 1 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028552299365401268 | 0.0 | 0.0 | +62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 / -— |
| Jogador 4 | 3-5 | 165 | BUY_XP | FAST8 | 68.0 | 6 | 11 | 1 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 166 | BUY_XP | FAST8 | 68.0 | 6 | 7 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 167 | MOVE_BOARD | FAST8 | 68.0 | 6 | 3 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 168 | MOVE_BOARD | FAST8 | 68.0 | 6 | 3 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014949648641049862 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 169 | PASS | FAST8 | 68.0 | 6 | 3 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 172 | BUY | FAST8 | 68.0 | 6 | 9 | 0 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7312068939208984 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 173 | SELL | FAST8 | 68.0 | 6 | 6 | 0 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -fe6546c3-86ef-40e1-aa7e-ff7e400fe628 |
| Jogador 4 | 3-6 | 174 | BUY | FAST8 | 68.0 | 6 | 11 | 1 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43726563453674316 | 0.0 | 0.0 | +f722cd46-0c4e-42e7-80ff-4b910c28d572 / -— |
| Jogador 4 | 3-6 | 175 | MOVE_BOARD | FAST8 | 68.0 | 6 | 8 | 0 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.560703731864123e-08 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 176 | MOVE_BOARD | FAST8 | 68.0 | 6 | 8 | 0 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 177 | MOVE_BOARD | FAST8 | 68.0 | 6 | 8 | 0 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999871142208576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 178 | PASS | FAST8 | 68.0 | 6 | 8 | 0 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 182 | SELL | FAST8 | 68.0 | 6 | 15 | 1 | 30.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46930569410324097 | 0.0 | 0.0 | +— / -62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 |
| Jogador 4 | 3-7 | 183 | BUY | FAST8 | 68.0 | 6 | 18 | 1 | 30.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7636228203773499 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-7 | 184 | MOVE_BENCH | STABILIZE | 68.0 | 6 | 15 | 1 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5988335013389587 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 185 | BUY | FAST8 | 68.0 | 6 | 15 | 1 | 36.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20003093779087067 | 0.0 | 0.0 | +59f588eb-e3f3-4907-ab23-af073a26bd6a / -— |
| Jogador 4 | 3-7 | 186 | MOVE_BOARD | FAST8 | 68.0 | 6 | 13 | 1 | 36.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 187 | MOVE_BOARD | FAST8 | 68.0 | 6 | 13 | 1 | 36.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 188 | PASS | FAST8 | 68.0 | 6 | 13 | 1 | 36.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 68.0 | 6 | 20 | 2 | 36.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11010690033435822 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 68.0 | 6 | 20 | 2 | 36.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1437884122133255 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 194 | BUY | FAST8 | 68.0 | 6 | 20 | 2 | 36.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3084973692893982 | 0.0 | 0.0 | +ddf39480-6ce0-46d0-ac45-57114245ffba / -— |
| Jogador 4 | 4-1 | 195 | MOVE_BOARD | FAST8 | 68.0 | 6 | 17 | 1 | 36.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -6.87880515215511e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 196 | MOVE_BENCH | FAST8 | 68.0 | 6 | 17 | 1 | 36.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7293457388877869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 197 | PASS | FAST8 | 68.0 | 6 | 17 | 1 | 36.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026428570970892906 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 202 | MOVE_BENCH | FAST8 | 56.0 | 7 | 23 | 2 | 36.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5998647809028625 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 203 | BUY | FAST8 | 56.0 | 7 | 23 | 2 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21247051656246185 | 0.0 | 0.0 | +84886290-556f-45e9-805b-9ca86a80ba27 / -— |
| Jogador 4 | 4-2 | 204 | MOVE_BOARD | FAST8 | 56.0 | 7 | 21 | 2 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 205 | MOVE_BOARD | FAST8 | 56.0 | 7 | 21 | 2 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 206 | PASS | FAST8 | 56.0 | 7 | 21 | 2 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029285714030265808 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 212 | SELL | FAST8 | 56.0 | 7 | 29 | 2 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08910000324249268 | 0.0 | 0.0 | +— / -ddf39480-6ce0-46d0-ac45-57114245ffba |
| Jogador 4 | 4-3 | 213 | BUY | FAST8 | 56.0 | 7 | 32 | 3 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6908536553382874 | 0.0 | 0.0 | +bb2e33e3-fe6f-4344-b113-aeba7ace7a2d / -— |
| Jogador 4 | 4-3 | 214 | MOVE_BOARD | FAST8 | 56.0 | 7 | 29 | 2 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 215 | MOVE_BOARD | FAST8 | 56.0 | 7 | 29 | 2 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999563805758953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 216 | PASS | FAST8 | 56.0 | 7 | 29 | 2 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03500000014901161 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 222 | SELL | FAST8 | 56.0 | 7 | 39 | 3 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0565166138112545 | 0.0 | 0.0 | +— / -f722cd46-0c4e-42e7-80ff-4b910c28d572 |
| Jogador 4 | 4-4 | 223 | BUY | FAST8 | 56.0 | 7 | 42 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7546412348747253 | 0.0 | 0.0 | +d1f19609-8b5f-489d-a2cf-d015fe7ed27e / -— |
| Jogador 4 | 4-4 | 224 | MOVE_BOARD | FAST8 | 56.0 | 7 | 40 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 225 | MOVE_BOARD | FAST8 | 56.0 | 7 | 40 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 226 | PASS | FAST8 | 56.0 | 7 | 40 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04285714402794838 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 232 | SELL | FAST8 | 56.0 | 7 | 50 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5911999940872192 | 0.0 | 0.0 | +— / -d71a866d-0c5a-41c2-9996-0e179f062aa2 |
| Jogador 4 | 4-5 | 233 | BUY | FAST8 | 56.0 | 7 | 51 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21745175123214722 | 0.0 | 0.0 | +f3e882b5-333e-44e3-ae82-cacacc8b1137 / -— |
| Jogador 4 | 4-5 | 234 | BUY_XP | FAST8 | 56.0 | 7 | 47 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 235 | BUY_XP | FAST8 | 56.0 | 7 | 43 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07395999878644943 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 236 | BUY_XP | FAST8 | 56.0 | 7 | 39 | 3 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 237 | MOVE_BOARD | FAST8 | 56.0 | 7 | 35 | 3 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 238 | MOVE_BOARD | FAST8 | 56.0 | 7 | 35 | 3 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015018943697214127 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 239 | PASS | FAST8 | 56.0 | 7 | 35 | 3 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03928571566939354 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 242 | SELL | FAST8 | 44.0 | 7 | 43 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -f3e882b5-333e-44e3-ae82-cacacc8b1137 |
| Jogador 4 | 4-6 | 243 | BUY | FAST8 | 44.0 | 7 | 47 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4010879397392273 | 0.0 | 0.0 | +e60f0b7f-8510-4c67-9ebd-0d8be1b0ff2b / -— |
| Jogador 4 | 4-6 | 244 | SELL | FAST8 | 44.0 | 7 | 45 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44066667556762695 | 0.0 | 0.0 | +— / -e60f0b7f-8510-4c67-9ebd-0d8be1b0ff2b |
| Jogador 4 | 4-6 | 245 | BUY | FAST8 | 44.0 | 7 | 47 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2530524730682373 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -— |
| Jogador 4 | 4-6 | 246 | MOVE_BOARD | FAST8 | 44.0 | 7 | 44 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0038321984466165304 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 247 | MOVE_BOARD | FAST8 | 44.0 | 7 | 44 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 248 | PASS | FAST8 | 44.0 | 7 | 44 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04749206453561783 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 252 | SELL | STABILIZE | 32.0 | 7 | 54 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5737333297729492 | 0.0 | 0.0 | +— / -84886290-556f-45e9-805b-9ca86a80ba27 |
| Jogador 4 | 4-7 | 253 | BUY | STABILIZE | 32.0 | 7 | 56 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20381279289722443 | 0.0 | 0.0 | +c69a2be1-356a-4576-9887-6d1790221a5e / -— |
| Jogador 4 | 4-7 | 254 | SELL | STABILIZE | 32.0 | 7 | 53 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09593333303928375 | 0.0 | 0.0 | +— / -d1f19609-8b5f-489d-a2cf-d015fe7ed27e |
| Jogador 4 | 4-7 | 255 | BUY | STABILIZE | 32.0 | 7 | 55 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1105044037103653 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 4 | 4-7 | 256 | BUY_XP | STABILIZE | 32.0 | 7 | 52 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04659999907016754 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 257 | BUY_XP | STABILIZE | 32.0 | 7 | 48 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 258 | BUY_XP | STABILIZE | 32.0 | 7 | 44 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 259 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 40 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0014494066126644611 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 260 | BUY_XP | STABILIZE | 32.0 | 7 | 40 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 32.0 | 7 | 45 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18292950093746185 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 32.0 | 7 | 45 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13379760086536407 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 264 | SELL | STABILIZE | 32.0 | 7 | 45 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023481614887714386 | 0.0 | 0.0 | +— / -d78561b4-3dcc-42fb-9983-2ed5d62f8606 |
| Jogador 4 | 5-1 | 265 | BUY | STABILIZE | 32.0 | 7 | 48 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40588992834091187 | 0.0 | 0.0 | +64215569-2a69-410d-a2f9-172544bef858 / -— |
| Jogador 4 | 5-1 | 266 | BUY_XP | STABILIZE | 32.0 | 7 | 45 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 267 | BUY_XP | STABILIZE | 32.0 | 7 | 41 | 4 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 268 | BUY_XP | STABILIZE | 32.0 | 7 | 37 | 3 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 269 | BUY_XP | STABILIZE | 32.0 | 7 | 33 | 3 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031201250851154327 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 270 | MOVE_BENCH | STABILIZE | 32.0 | 8 | 29 | 2 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4017806053161621 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 272 | BUY | ALL_IN | 16.0 | 8 | 37 | 3 | 46.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3575233817100525 | 0.0 | 0.0 | +0e5921d4-a056-4f42-951e-93de5f2834bb / -— |
| Jogador 4 | 5-2 | 273 | SELL | ALL_IN | 16.0 | 8 | 33 | 3 | 46.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11153333634138107 | 0.0 | 0.0 | +— / -0e5921d4-a056-4f42-951e-93de5f2834bb |
| Jogador 4 | 5-2 | 274 | BUY | ALL_IN | 16.0 | 8 | 37 | 3 | 46.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37431782484054565 | 0.0 | 0.0 | +0b38218d-9c50-41ac-b761-115c054bf314 / -— |
| Jogador 4 | 5-2 | 275 | MOVE_BOARD | ALL_IN | 16.0 | 8 | 35 | 3 | 46.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 276 | MOVE_BOARD | ALL_IN | 16.0 | 8 | 35 | 3 | 46.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 277 | PASS | ALL_IN | 16.0 | 8 | 35 | 3 | 46.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4104735553264618 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5658670663833618 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.10612095892429352 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13031664490699768 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17401309311389923 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20017212629318237 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 32 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039355870336294174 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 33 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0343543216586113 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 35 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 41 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43657252192497253 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3327503204345703 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 44 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2927319407463074 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039752013981342316 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 46 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0192145109176636 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23672904074192047 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20601853728294373 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.402841717004776 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21565893292427063 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011052913032472134 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 14.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2490367442369461 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9570834636688232 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 63 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31671762466430664 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 64 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13096866011619568 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-2 | 65 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1725645512342453 | 0.0 | 0.0 | +0debca82-3a2a-44ba-af48-83211d5e5243 / -— |
| Jogador 5 | 2-2 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 14.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00817900337278843 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 67 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 14.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1882772147655487 | 0.0 | 0.0 | +— / -9c678a7f-3209-4d1b-addd-385f7d4b89fa |
| Jogador 5 | 2-2 | 68 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5874356627464294 | 0.0 | 0.0 | +— / -eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 2-2 | 69 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055078063160181046 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 70 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14971227943897247 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 12 | 1 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.113427758216858 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 4 | 11 | 1 | 16.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2544553577899933 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 75 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5944125056266785 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 77 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15741054713726044 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.35144089453388e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 79 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014995072968304157 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 80 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3610869348049164 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 83 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19861888885498047 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 84 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05810000002384186 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 85 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0028256650548428297 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 87 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012567846104502678 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 88 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.344232439994812 | 0.0 | 0.0 | +2e4ab22c-62d7-425c-9528-2e1315655c24 / -— |
| Jogador 5 | 2-5 | 93 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.299274206161499 | 0.0 | 0.0 | +28f66ef1-93d6-4cc8-a0c9-e84e844dee28 / -— |
| Jogador 5 | 2-5 | 94 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 95 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.133643571753055e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 97 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 102 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0889517143368721 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 103 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05053376033902168 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 104 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 105 | SELL | STABILIZE | 100.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04968453571200371 | 0.0 | 0.0 | +— / -5627d898-cff3-4664-87d1-40a8f3656ab3 |
| Jogador 5 | 2-6 | 106 | SELL | STABILIZE | 100.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-6 | 107 | SELL | STABILIZE | 100.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0689999982714653 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 108 | BUY_XP | STABILIZE | 100.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 109 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41207295656204224 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 112 | BUY | STABILIZE | 94.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.821526050567627 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -— |
| Jogador 5 | 2-7 | 113 | BUY | STABILIZE | 94.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35159537196159363 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 114 | BUY | STABILIZE | 94.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8869309425354004 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0009042004821822047 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013998620212078094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 117 | PASS | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 122 | BUY | STABILIZE | 94.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.831781268119812 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -46838f8d-8037-485c-8c34-9639f14ada19,837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-1 | 123 | BUY | STABILIZE | 94.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7538460493087769 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20155900716781616 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.538920385741221e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997726306319237 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 127 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 128 | PASS | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 132 | BUY | STABILIZE | 94.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2857232689857483 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -— |
| Jogador 5 | 3-2 | 133 | BUY | STABILIZE | 94.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8234482407569885 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -0debca82-3a2a-44ba-af48-83211d5e5243,e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 3-2 | 134 | BUY | STABILIZE | 94.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2592151165008545 | 0.0 | 0.0 | +1662b43d-12f4-45d6-b1bf-3733d5214808 / -— |
| Jogador 5 | 3-2 | 135 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500721275806427 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 137 | PASS | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 142 | BUY | STABILIZE | 94.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.805698812007904 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -— |
| Jogador 5 | 3-3 | 143 | SELL | STABILIZE | 94.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-3 | 144 | BUY | STABILIZE | 94.0 | 6 | 10 | 1 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20303601026535034 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 145 | SELL | STABILIZE | 94.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43137067556381226 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-3 | 146 | BUY | STABILIZE | 94.0 | 6 | 15 | 1 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.254202663898468 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 147 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 11 | 1 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.480053121369565e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 148 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 11 | 1 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015033355914056301 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 11 | 1 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014968606643378735 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 150 | PASS | STABILIZE | 94.0 | 6 | 11 | 1 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 152 | SELL | STABILIZE | 94.0 | 6 | 19 | 1 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10199999809265137 | 0.0 | 0.0 | +— / -1662b43d-12f4-45d6-b1bf-3733d5214808 |
| Jogador 5 | 3-4 | 153 | BUY | STABILIZE | 94.0 | 6 | 20 | 2 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.734199583530426 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 5 | 3-4 | 154 | SELL | STABILIZE | 94.0 | 6 | 19 | 1 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41734322905540466 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 3-4 | 155 | BUY | STABILIZE | 94.0 | 6 | 20 | 2 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7722846269607544 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -2e4ab22c-62d7-425c-9528-2e1315655c24,6084e8d8-82f2-47e3-b8e1-4077ad70efe5 |
| Jogador 5 | 3-4 | 156 | BUY | STABILIZE | 94.0 | 6 | 19 | 1 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06879913806915283 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 17 | 1 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.6441881598439068e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 17 | 1 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499806810170412 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 17 | 1 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015060772188007832 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 160 | PASS | STABILIZE | 94.0 | 6 | 17 | 1 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 162 | BUY | STABILIZE | 94.0 | 6 | 24 | 2 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7918863296508789 | 0.0 | 0.0 | +c3a766c4-2db6-4b3f-88e9-a855fef1e6f6 / -— |
| Jogador 5 | 3-5 | 163 | SELL | STABILIZE | 94.0 | 6 | 22 | 2 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 3-5 | 164 | BUY | STABILIZE | 94.0 | 6 | 25 | 2 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7185599207878113 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -— |
| Jogador 5 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 24 | 2 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.139307227684185e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 24 | 2 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499909721314907 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 24 | 2 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499893981963396 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 168 | PASS | STABILIZE | 94.0 | 6 | 24 | 2 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02199999988079071 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 172 | SELL | STABILIZE | 94.0 | 6 | 33 | 3 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02386626973748207 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 3-6 | 173 | BUY | STABILIZE | 94.0 | 6 | 35 | 3 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31292814016342163 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -— |
| Jogador 5 | 3-6 | 174 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 34 | 3 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.335555811645463e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 34 | 3 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014968606643378735 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 176 | PASS | STABILIZE | 94.0 | 6 | 34 | 3 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 182 | SELL | STABILIZE | 94.0 | 6 | 45 | 4 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49737727642059326 | 0.0 | 0.0 | +— / -ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 3-7 | 183 | BUY | STABILIZE | 94.0 | 6 | 46 | 4 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8727429509162903 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -b0190388-bc3b-43af-b782-94490de9d8b1,c3a766c4-2db6-4b3f-88e9-a855fef1e6f6 |
| Jogador 5 | 3-7 | 184 | BUY | STABILIZE | 94.0 | 6 | 44 | 4 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2929243743419647 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 185 | BUY_XP | STABILIZE | 94.0 | 6 | 41 | 4 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08445625007152557 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 37 | 3 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.6441881598439068e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 187 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 37 | 3 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499806810170412 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 188 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 37 | 3 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015060772188007832 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 189 | PASS | STABILIZE | 94.0 | 6 | 37 | 3 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1264999955892563 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 192 | BUY | STABILIZE | 94.0 | 6 | 47 | 4 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8875916004180908 | 0.0 | 0.0 | +b2a77bec-e150-4d98-847c-9f2cfb50cbe7 / -— |
| Jogador 5 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 46 | 4 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23237529397010803 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 46 | 4 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22224318981170654 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 195 | SELL | STABILIZE | 94.0 | 6 | 46 | 4 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5031999945640564 | 0.0 | 0.0 | +— / -691cde76-cf1b-4a60-b818-65f790e312ec |
| Jogador 5 | 4-1 | 196 | BUY | STABILIZE | 94.0 | 6 | 51 | 5 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18268117308616638 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 5 | 4-1 | 197 | REROLL | STABILIZE | 94.0 | 6 | 48 | 4 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20399999618530273 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 198 | SELL | STABILIZE | 94.0 | 6 | 46 | 4 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04671458527445793 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 5 | 4-1 | 199 | BUY | STABILIZE | 94.0 | 6 | 49 | 4 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6512417793273926 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 5 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 48 | 4 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.9972969059599563e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 202 | SELL | STABILIZE | 81.0 | 6 | 57 | 5 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09929999709129333 | 0.0 | 0.0 | +— / -8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 |
| Jogador 5 | 4-2 | 203 | BUY | STABILIZE | 81.0 | 6 | 60 | 5 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8770240545272827 | 0.0 | 0.0 | +395ae945-c8a2-4d80-98a4-5eb6887b8f78 / -— |
| Jogador 5 | 4-2 | 204 | SELL | STABILIZE | 81.0 | 6 | 57 | 5 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5935999751091003 | 0.0 | 0.0 | +— / -1e81ac95-667f-494d-89eb-2bcdcf887a7e |
| Jogador 5 | 4-2 | 205 | BUY | STABILIZE | 81.0 | 6 | 60 | 5 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9588929414749146 | 0.0 | 0.0 | +2001a193-3868-4a3f-8a71-3a9f95c04a02 / -02c39b42-90d5-4e01-9380-460b6c1cb993,9593a62e-442f-410a-8a0c-7d781e2487cc |
| Jogador 5 | 4-2 | 206 | BUY_XP | STABILIZE | 81.0 | 6 | 59 | 5 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016950000077486038 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 207 | BUY_XP | STABILIZE | 81.0 | 6 | 55 | 5 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3387812376022339 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 208 | MOVE_BENCH | STABILIZE | 81.0 | 7 | 51 | 5 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2481817603111267 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 209 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 51 | 5 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014309724792838097 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 210 | MOVE_BOARD | STABILIZE | 81.0 | 7 | 51 | 5 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014995601959526539 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 212 | BUY | FAST8 | 81.0 | 7 | 62 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3238973319530487 | 0.0 | 0.0 | +ea88d306-ae6b-4dbe-b559-3371ba39613a / -— |
| Jogador 5 | 4-3 | 213 | MOVE_BOARD | FAST8 | 81.0 | 7 | 61 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.000105735678516794 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 214 | MOVE_BOARD | FAST8 | 81.0 | 7 | 61 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014924094080924988 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 215 | PASS | FAST8 | 81.0 | 7 | 61 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22661596536636353 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 222 | BUY | FAST8 | 81.0 | 7 | 73 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7077955603599548 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -— |
| Jogador 5 | 4-4 | 223 | BUY | FAST8 | 81.0 | 7 | 72 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2569945454597473 | 0.0 | 0.0 | +a58767a1-d7c1-48e9-94ae-df46a364ef92 / -— |
| Jogador 5 | 4-4 | 224 | MOVE_BOARD | FAST8 | 81.0 | 7 | 70 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0001588488376000896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 225 | MOVE_BOARD | FAST8 | 81.0 | 7 | 70 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014840549789369106 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 226 | PASS | FAST8 | 81.0 | 7 | 70 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09277009963989258 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 232 | MOVE_BOARD | FAST8 | 81.0 | 7 | 81 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 233 | MOVE_BOARD | FAST8 | 81.0 | 7 | 81 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014973495155572891 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 234 | PASS | FAST8 | 81.0 | 7 | 81 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.100680410861969 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 242 | SELL | FAST8 | 81.0 | 7 | 93 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09593333303928375 | 0.0 | 0.0 | +— / -a58767a1-d7c1-48e9-94ae-df46a364ef92 |
| Jogador 5 | 4-6 | 243 | BUY | FAST8 | 81.0 | 7 | 95 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.830356240272522 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 5 | 4-6 | 244 | MOVE_BOARD | FAST8 | 81.0 | 7 | 94 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 245 | MOVE_BOARD | FAST8 | 81.0 | 7 | 94 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014996838755905628 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 246 | PASS | FAST8 | 81.0 | 7 | 94 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11039899289608002 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 252 | SELL | FAST8 | 68.0 | 7 | 104 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9811999797821045 | 0.0 | 0.0 | +— / -ea88d306-ae6b-4dbe-b559-3371ba39613a |
| Jogador 5 | 4-7 | 253 | BUY | FAST8 | 68.0 | 7 | 105 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14340578019618988 | 0.0 | 0.0 | +e270a6b1-23dd-49a0-8694-ba911eae4c71 / -— |
| Jogador 5 | 4-7 | 254 | SELL | FAST8 | 68.0 | 7 | 102 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05510000139474869 | 0.0 | 0.0 | +— / -e270a6b1-23dd-49a0-8694-ba911eae4c71 |
| Jogador 5 | 4-7 | 255 | BUY | FAST8 | 68.0 | 7 | 105 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01263887993991375 | 0.0 | 0.0 | +89ef75a2-6ac2-4c6c-b2b8-492aec985a01 / -— |
| Jogador 5 | 4-7 | 256 | REROLL | FAST8 | 68.0 | 7 | 101 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 257 | REROLL | FAST8 | 68.0 | 7 | 101 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 258 | MOVE_BOARD | FAST8 | 68.0 | 7 | 101 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 259 | MOVE_BOARD | FAST8 | 68.0 | 7 | 101 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015009241178631783 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 260 | PASS | FAST8 | 68.0 | 7 | 101 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11575925350189209 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 68.0 | 7 | 111 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1795116513967514 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 68.0 | 7 | 111 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13430026173591614 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 264 | SELL | FAST8 | 68.0 | 7 | 111 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5911999940872192 | 0.0 | 0.0 | +— / -04520fe5-4449-4632-b275-e5e28d642007 |
| Jogador 5 | 5-1 | 265 | BUY | FAST8 | 68.0 | 7 | 112 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9511960744857788 | 0.0 | 0.0 | +d5c73756-6784-44e9-b521-5c61db813319 / -b2a77bec-e150-4d98-847c-9f2cfb50cbe7,bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 |
| Jogador 5 | 5-1 | 266 | BUY | FAST8 | 68.0 | 7 | 111 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1466246247291565 | 0.0 | 0.0 | +d8392323-28e4-4e98-a466-5958bf400729 / -— |
| Jogador 5 | 5-1 | 267 | BUY | FAST8 | 68.0 | 7 | 108 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06203296780586243 | 0.0 | 0.0 | +a5e92183-8d5d-434c-9294-47c6b7bfb91b / -— |
| Jogador 5 | 5-1 | 268 | MOVE_BOARD | FAST8 | 68.0 | 7 | 105 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 269 | MOVE_BOARD | FAST8 | 68.0 | 7 | 105 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997442252933979 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 270 | PASS | FAST8 | 68.0 | 7 | 105 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13074180483818054 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 272 | SELL | FAST8 | 68.0 | 7 | 115 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.847100019454956 | 0.0 | 0.0 | +— / -d5c73756-6784-44e9-b521-5c61db813319 |
| Jogador 5 | 5-2 | 273 | BUY | FAST8 | 68.0 | 7 | 118 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5514665246009827 | 0.0 | 0.0 | +efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 / -— |
| Jogador 5 | 5-2 | 274 | SELL | FAST8 | 68.0 | 7 | 115 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.056191712617874146 | 0.0 | 0.0 | +— / -d8392323-28e4-4e98-a466-5958bf400729 |
| Jogador 5 | 5-2 | 275 | BUY | FAST8 | 68.0 | 7 | 118 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28340524435043335 | 0.0 | 0.0 | +c07a17cf-e9e7-42be-b925-cb4f699593de / -— |
| Jogador 5 | 5-2 | 276 | REROLL | FAST8 | 68.0 | 7 | 115 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 277 | REROLL | FAST8 | 68.0 | 7 | 115 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 278 | REROLL | FAST8 | 68.0 | 7 | 115 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 279 | REROLL | FAST8 | 68.0 | 7 | 115 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 280 | REROLL | FAST8 | 68.0 | 7 | 115 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 282 | SELL | FAST8 | 52.0 | 7 | 126 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09929999709129333 | 0.0 | 0.0 | +— / -c07a17cf-e9e7-42be-b925-cb4f699593de |
| Jogador 5 | 5-3 | 283 | BUY | FAST8 | 52.0 | 7 | 129 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3263416588306427 | 0.0 | 0.0 | +b58c0c0e-9c6f-4977-91d1-177b7113c439 / -— |
| Jogador 5 | 5-3 | 284 | SELL | FAST8 | 52.0 | 7 | 128 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5911999940872192 | 0.0 | 0.0 | +— / -b58c0c0e-9c6f-4977-91d1-177b7113c439 |
| Jogador 5 | 5-3 | 285 | BUY | FAST8 | 52.0 | 7 | 129 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9021521806716919 | 0.0 | 0.0 | +d58ebcea-d18b-42f8-a6ca-984d15656662 / -a5e92183-8d5d-434c-9294-47c6b7bfb91b,efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 |
| Jogador 5 | 5-3 | 286 | BUY | FAST8 | 52.0 | 7 | 126 | 5 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2983253002166748 | 0.0 | 0.0 | +7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 / -— |
| Jogador 5 | 5-3 | 287 | BUY | FAST8 | 52.0 | 7 | 123 | 5 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2835603356361389 | 0.0 | 0.0 | +40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b / -— |
| Jogador 5 | 5-3 | 288 | REROLL | FAST8 | 52.0 | 7 | 120 | 5 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 289 | REROLL | FAST8 | 52.0 | 7 | 120 | 5 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 290 | REROLL | FAST8 | 52.0 | 7 | 120 | 5 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 292 | SELL | STABILIZE | 37.0 | 7 | 131 | 5 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5772666931152344 | 0.0 | 0.0 | +— / -d58ebcea-d18b-42f8-a6ca-984d15656662 |
| Jogador 5 | 5-4 | 293 | BUY | STABILIZE | 37.0 | 7 | 139 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06849149614572525 | 0.0 | 0.0 | +92bac611-1820-42eb-8243-499f20058673 / -— |
| Jogador 5 | 5-4 | 294 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 134 | 5 | 28.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7053803205490112 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 295 | SELL | STABILIZE | 37.0 | 7 | 134 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5545855164527893 | 0.0 | 0.0 | +— / -2001a193-3868-4a3f-8a71-3a9f95c04a02 |
| Jogador 5 | 5-4 | 296 | BUY | STABILIZE | 37.0 | 7 | 137 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06970115005970001 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -— |
| Jogador 5 | 5-4 | 297 | BUY_XP | STABILIZE | 37.0 | 7 | 134 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035999998450279236 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 298 | BUY_XP | STABILIZE | 37.0 | 7 | 130 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035999998450279236 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 299 | BUY_XP | STABILIZE | 37.0 | 7 | 126 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035999998450279236 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 300 | BUY_XP | STABILIZE | 37.0 | 7 | 122 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035999998450279236 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 302 | SELL | STABILIZE | 37.0 | 7 | 129 | 5 | 34.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03767099231481552 | 0.0 | 0.0 | +— / -2b10436d-ccfe-4329-aef8-2769899b3787 |
| Jogador 5 | 5-5 | 303 | BUY | STABILIZE | 37.0 | 7 | 132 | 5 | 34.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0215048789978027 | 0.0 | 0.0 | +c71adf7d-8d74-439d-8863-dac0f4f20cd1 / -4d8c374c-264c-47d9-8cfc-78cbf64ceda0,8a4e95ea-d35a-4690-9313-126b5d86773e |
| Jogador 5 | 5-5 | 304 | BUY | STABILIZE | 37.0 | 7 | 130 | 5 | 30.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4711962938308716 | 0.0 | 0.0 | +e1be174a-f112-4e1b-8bf6-738af52f27e8 / -— |
| Jogador 5 | 5-5 | 305 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 129 | 5 | 30.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.590681791305542 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 306 | BUY | STABILIZE | 37.0 | 7 | 129 | 5 | 38.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023974156007170677 | 0.0 | 0.0 | +87726d3e-4b0d-41ae-bf43-893d4092bd5b / -— |
| Jogador 5 | 5-5 | 307 | MOVE_BOARD | STABILIZE | 37.0 | 7 | 127 | 5 | 38.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006863648304715753 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 308 | REROLL | STABILIZE | 37.0 | 7 | 127 | 5 | 38.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15760000050067902 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 309 | SELL | STABILIZE | 37.0 | 7 | 125 | 5 | 38.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01360000018030405 | 0.0 | 0.0 | +— / -87726d3e-4b0d-41ae-bf43-893d4092bd5b |
| Jogador 5 | 5-5 | 310 | BUY | STABILIZE | 37.0 | 7 | 127 | 5 | 38.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3302609920501709 | 0.0 | 0.0 | +25029b69-ee52-4788-840e-006ff9e57d5d / -— |
| Jogador 5 | 5-6 | 312 | SELL | ALL_IN | 23.0 | 7 | 136 | 5 | 38.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08293333649635315 | 0.0 | 0.0 | +— / -25029b69-ee52-4788-840e-006ff9e57d5d |
| Jogador 5 | 5-6 | 313 | BUY | ALL_IN | 23.0 | 7 | 138 | 5 | 38.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38474419713020325 | 0.0 | 0.0 | +0366f83c-b9d4-47c2-aa5e-4dc1021bd201 / -— |
| Jogador 5 | 5-6 | 314 | SELL | ALL_IN | 23.0 | 7 | 134 | 5 | 38.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0481666661798954 | 0.0 | 0.0 | +— / -7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 |
| Jogador 5 | 5-6 | 315 | BUY | ALL_IN | 23.0 | 7 | 137 | 5 | 38.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05243248492479324 | 0.0 | 0.0 | +533790d1-aca6-417d-b163-b0bda70d1500 / -— |
| Jogador 5 | 5-6 | 316 | BUY_XP | ALL_IN | 23.0 | 7 | 135 | 5 | 38.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1576174944639206 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 317 | REROLL | ALL_IN | 23.0 | 7 | 131 | 5 | 38.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 318 | SELL | ALL_IN | 23.0 | 7 | 129 | 5 | 38.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01360000018030405 | 0.0 | 0.0 | +— / -533790d1-aca6-417d-b163-b0bda70d1500 |
| Jogador 5 | 5-6 | 319 | BUY | ALL_IN | 23.0 | 7 | 131 | 5 | 38.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05992245301604271 | 0.0 | 0.0 | +12d02679-e950-433b-ad9e-679a89cf86d8 / -— |
| Jogador 5 | 5-6 | 320 | MOVE_BENCH | ALL_IN | 23.0 | 7 | 127 | 5 | 38.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28904348611831665 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 322 | SELL | ALL_IN | 23.0 | 7 | 138 | 5 | 44.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03333333507180214 | 0.0 | 0.0 | +— / -12d02679-e950-433b-ad9e-679a89cf86d8 |
| Jogador 5 | 5-7 | 323 | BUY | ALL_IN | 23.0 | 7 | 142 | 5 | 44.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0506324768066406 | 0.0 | 0.0 | +c339a5f7-66d9-4d5f-b331-4bac23a83a4a / -1d7b6420-388f-4cb1-b25c-2e5a3dfec742,395ae945-c8a2-4d80-98a4-5eb6887b8f78 |
| Jogador 5 | 5-7 | 324 | BUY | ALL_IN | 23.0 | 7 | 139 | 5 | 44.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4324108064174652 | 0.0 | 0.0 | +2ce6c216-8ffa-4f9b-b78a-aed96adfa47b / -— |
| Jogador 5 | 5-7 | 325 | BUY | ALL_IN | 23.0 | 7 | 137 | 5 | 44.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1800534576177597 | 0.0 | 0.0 | +b1e5b3b9-fda8-4d4a-9368-94fd558da4f7 / -— |
| Jogador 5 | 5-7 | 326 | REROLL | ALL_IN | 23.0 | 7 | 133 | 5 | 44.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 327 | SELL | ALL_IN | 23.0 | 7 | 131 | 5 | 44.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5996000170707703 | 0.0 | 0.0 | +— / -c339a5f7-66d9-4d5f-b331-4bac23a83a4a |
| Jogador 5 | 5-7 | 328 | BUY | ALL_IN | 23.0 | 7 | 139 | 5 | 44.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41671085357666016 | 0.0 | 0.0 | +16ccc1d8-1393-41a2-9f14-000d94c78bca / -— |
| Jogador 5 | 5-7 | 329 | SELL | ALL_IN | 23.0 | 7 | 136 | 5 | 44.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02151884324848652 | 0.0 | 0.0 | +— / -89ef75a2-6ac2-4c6c-b2b8-492aec985a01 |
| Jogador 5 | 5-7 | 330 | BUY | ALL_IN | 23.0 | 7 | 140 | 5 | 44.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12998628616333008 | 0.0 | 0.0 | +d925d9be-1d80-4347-93ba-4e5bc885dfc4 / -— |
| Jogador 5 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ALL_IN | 23.0 | 7 | 148 | 5 | 44.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10192663967609406 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 333 | SELL | ALL_IN | 23.0 | 7 | 148 | 5 | 44.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04326541721820831 | 0.0 | 0.0 | +— / -b1e5b3b9-fda8-4d4a-9368-94fd558da4f7 |
| Jogador 5 | 6-1 | 334 | BUY | ALL_IN | 23.0 | 7 | 152 | 5 | 44.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5127840042114258 | 0.0 | 0.0 | +3c65e9e8-ff81-499f-8145-953bbcd0531e / -— |
| Jogador 5 | 6-1 | 335 | SELL | ALL_IN | 23.0 | 7 | 149 | 5 | 44.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034694772213697433 | 0.0 | 0.0 | +— / -d925d9be-1d80-4347-93ba-4e5bc885dfc4 |
| Jogador 5 | 6-1 | 336 | BUY | ALL_IN | 23.0 | 7 | 152 | 5 | 44.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4131432771682739 | 0.0 | 0.0 | +9315c427-7094-4e56-adb5-70be515fddaa / -— |
| Jogador 5 | 6-1 | 337 | REROLL | ALL_IN | 23.0 | 7 | 150 | 5 | 44.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 338 | SELL | ALL_IN | 23.0 | 7 | 148 | 5 | 44.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10459999740123749 | 0.0 | 0.0 | +— / -9315c427-7094-4e56-adb5-70be515fddaa |
| Jogador 5 | 6-1 | 339 | BUY | ALL_IN | 23.0 | 7 | 150 | 5 | 44.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.95169997215271 | 0.0 | 0.0 | +3ba5e931-3f4c-410f-bf0b-d9d1a426efa3 / -— |
| Jogador 5 | 6-1 | 340 | SELL | ALL_IN | 23.0 | 7 | 147 | 5 | 44.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4742666780948639 | 0.0 | 0.0 | +— / -3c65e9e8-ff81-499f-8145-953bbcd0531e |
| Jogador 5 | 6-2 | 342 | BUY | ALL_IN | 23.0 | 7 | 161 | 5 | 44.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41329529881477356 | 0.0 | 0.0 | +a555195a-af05-4734-a909-5eadcfe58b24 / -— |
| Jogador 5 | 6-2 | 343 | REROLL | ALL_IN | 23.0 | 7 | 159 | 5 | 44.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 344 | SELL | ALL_IN | 23.0 | 7 | 157 | 5 | 44.0 | Colosso/DA_18_Ashe | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10459999740123749 | 0.0 | 0.0 | +— / -a555195a-af05-4734-a909-5eadcfe58b24 |
| Jogador 5 | 6-2 | 345 | BUY | ALL_IN | 23.0 | 7 | 159 | 5 | 44.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24043790996074677 | 0.0 | 0.0 | +42dcd971-9003-42c7-89f4-271ba5fe868d / -— |
| Jogador 5 | 6-2 | 346 | REROLL | ALL_IN | 23.0 | 7 | 154 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 347 | SELL | ALL_IN | 23.0 | 7 | 152 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5911999940872192 | 0.0 | 0.0 | +— / -e1be174a-f112-4e1b-8bf6-738af52f27e8 |
| Jogador 5 | 6-2 | 348 | BUY | ALL_IN | 23.0 | 7 | 153 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0277578830718994 | 0.0 | 0.0 | +d586f67f-487b-408e-b96d-21f5b8b6670e / -— |
| Jogador 5 | 6-2 | 349 | SELL | ALL_IN | 23.0 | 7 | 151 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6115999817848206 | 0.0 | 0.0 | +— / -3ba5e931-3f4c-410f-bf0b-d9d1a426efa3 |
| Jogador 5 | 6-2 | 350 | BUY | ALL_IN | 23.0 | 7 | 154 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43512478470802307 | 0.0 | 0.0 | +4aad2eba-6da2-4e1f-8350-7a645cf03109 / -— |
| Jogador 5 | 6-3 | 352 | SELL | ALL_IN | 23.0 | 7 | 163 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12096666544675827 | 0.0 | 0.0 | +— / -40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b |
| Jogador 5 | 6-3 | 353 | BUY | ALL_IN | 23.0 | 7 | 166 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17666736245155334 | 0.0 | 0.0 | +d63a72f0-dcab-454e-afad-17ddc66b5b3d / -— |
| Jogador 5 | 6-3 | 354 | REROLL | ALL_IN | 23.0 | 7 | 162 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 355 | SELL | ALL_IN | 23.0 | 7 | 160 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043269526213407516 | 0.0 | 0.0 | +— / -d63a72f0-dcab-454e-afad-17ddc66b5b3d |
| Jogador 5 | 6-3 | 356 | BUY | ALL_IN | 23.0 | 7 | 164 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17826521396636963 | 0.0 | 0.0 | +23181987-d0b2-4e8c-a1a7-48a1e28179f7 / -— |
| Jogador 5 | 6-3 | 357 | REROLL | ALL_IN | 23.0 | 7 | 160 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 358 | SELL | ALL_IN | 23.0 | 7 | 158 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043246544897556305 | 0.0 | 0.0 | +— / -23181987-d0b2-4e8c-a1a7-48a1e28179f7 |
| Jogador 5 | 6-3 | 359 | BUY | ALL_IN | 23.0 | 7 | 162 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9845158457756042 | 0.0 | 0.0 | +2ed60268-d2b1-4e41-bae7-43a89060e325 / -— |
| Jogador 5 | 6-3 | 360 | REROLL | ALL_IN | 23.0 | 7 | 159 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 362 | REROLL | ALL_IN | 23.0 | 7 | 169 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 363 | SELL | ALL_IN | 23.0 | 7 | 167 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5892850160598755 | 0.0 | 0.0 | +— / -4aad2eba-6da2-4e1f-8350-7a645cf03109 |
| Jogador 5 | 6-4 | 364 | BUY | ALL_IN | 23.0 | 7 | 170 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6249175071716309 | 0.0 | 0.0 | +559d1b79-d4c7-470c-912e-fe30541195ec / -— |
| Jogador 5 | 6-4 | 365 | REROLL | ALL_IN | 23.0 | 7 | 167 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 366 | SELL | ALL_IN | 23.0 | 7 | 165 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47788992524147034 | 0.0 | 0.0 | +— / -559d1b79-d4c7-470c-912e-fe30541195ec |
| Jogador 5 | 6-4 | 367 | BUY | ALL_IN | 23.0 | 7 | 168 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43087974190711975 | 0.0 | 0.0 | +91539d01-1b4f-442a-99b0-56b534ea8063 / -— |
| Jogador 5 | 6-4 | 368 | SELL | ALL_IN | 23.0 | 7 | 165 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12096666544675827 | 0.0 | 0.0 | +— / -91539d01-1b4f-442a-99b0-56b534ea8063 |
| Jogador 5 | 6-4 | 369 | BUY | ALL_IN | 23.0 | 7 | 168 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4308875799179077 | 0.0 | 0.0 | +74ac117f-47a6-4d94-b6f7-8d42714571e5 / -— |
| Jogador 5 | 6-4 | 370 | REROLL | ALL_IN | 23.0 | 7 | 165 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 372 | SELL | ALL_IN | 23.0 | 7 | 174 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12096666544675827 | 0.0 | 0.0 | +— / -74ac117f-47a6-4d94-b6f7-8d42714571e5 |
| Jogador 5 | 6-5 | 373 | BUY | ALL_IN | 23.0 | 7 | 177 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4307844340801239 | 0.0 | 0.0 | +41b1dead-685f-4b66-b9b1-cc504a711c98 / -— |
| Jogador 5 | 6-5 | 374 | SELL | ALL_IN | 23.0 | 7 | 174 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12096666544675827 | 0.0 | 0.0 | +— / -41b1dead-685f-4b66-b9b1-cc504a711c98 |
| Jogador 5 | 6-5 | 375 | BUY | ALL_IN | 23.0 | 7 | 177 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0385408401489258 | 0.0 | 0.0 | +09e28e26-f7f0-4d8a-acca-f768d9205f14 / -28f66ef1-93d6-4cc8-a0c9-e84e844dee28,45da6d00-829e-4e2e-a1a5-318498fd007b |
| Jogador 5 | 6-5 | 376 | BUY | ALL_IN | 23.0 | 7 | 176 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26653584837913513 | 0.0 | 0.0 | +94f20892-cf66-4256-9159-a295f6054b8f / -— |
| Jogador 5 | 6-5 | 377 | REROLL | ALL_IN | 23.0 | 7 | 175 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 378 | BUY | ALL_IN | 23.0 | 7 | 173 | 5 | 44.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7461925148963928 | 0.0 | 0.0 | +2900e5fd-1259-430c-ba65-d6a6122b6a08 / -— |
| Jogador 5 | 6-5 | 379 | REROLL | ALL_IN | 23.0 | 7 | 170 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 380 | SELL | ALL_IN | 23.0 | 7 | 168 | 5 | 44.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4610888957977295 | 0.0 | 0.0 | +— / -09e28e26-f7f0-4d8a-acca-f768d9205f14 |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.16343529522418976 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9946255087852478 | 0.0 | 0.0 | +425b1e77-5887-40b3-875e-c1f60dc6c513 / -— |
| Jogador 6 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1021408811211586 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15072090923786163 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 21 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21588344871997833 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4997868835926056 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.21719536185264587 | 0.0 | 0.0 | +c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 / -— |
| Jogador 6 | 1-3 | 32 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2727758288383484 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 33 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009247762151062489 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013545097783207893 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 35 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.021591067314148 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 44 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28995591402053833 | 0.0 | 0.0 | +72aa8420-8dc2-4e9b-a10a-bd2a36f26656 / -— |
| Jogador 6 | 1-4 | 45 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14078648388385773 | 0.0 | 0.0 | +— / -72aa8420-8dc2-4e9b-a10a-bd2a36f26656 |
| Jogador 6 | 1-4 | 46 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13791993260383606 | 0.0 | 0.0 | +c19cf6a8-c66e-4670-b0fc-fb83453f22e7 / -— |
| Jogador 6 | 1-4 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010088593699038029 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026310956105589867 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3491264581680298 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 50 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2840023636817932 | 0.0 | 0.0 | +c8b72b14-11a4-48e6-8135-41efdbc347cb / -— |
| Jogador 6 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1944529116153717 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19068704545497894 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09342395514249802 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31314510107040405 | 0.0 | 0.0 | +185ee377-0917-4209-905b-9486d5be0193 / -— |
| Jogador 6 | 2-1 | 59 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14385224878787994 | 0.0 | 0.0 | +— / -185ee377-0917-4209-905b-9486d5be0193 |
| Jogador 6 | 2-1 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.046593789011240005 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 10.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26815664768218994 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 64 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1266595721244812 | 0.0 | 0.0 | +— / -c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 |
| Jogador 6 | 2-2 | 65 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.188470259308815 | 0.0 | 0.0 | +— / -c8b72b14-11a4-48e6-8135-41efdbc347cb |
| Jogador 6 | 2-2 | 66 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 67 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44852539896965027 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 68 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 16.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00025023892521858215 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 16.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0760081335902214 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 70 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 16.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007254647556692362 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.382080614566803 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2677189111709595 | 0.0 | 0.0 | +2ef60eed-d073-41a6-adec-4466c673b313 / -— |
| Jogador 6 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 75 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001228958717547357 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 76 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03979475051164627 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 77 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3590308129787445 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9513565301895142 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12417469918727875 | 0.0 | 0.0 | +— / -2ef60eed-d073-41a6-adec-4466c673b313 |
| Jogador 6 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 86 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22494643926620483 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-4 | 87 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2905943691730499 | 0.0 | 0.0 | +2c497125-ca06-46b1-a3b3-9a59d904705b / -— |
| Jogador 6 | 2-4 | 88 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008745495229959488 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 89 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07023073732852936 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014443120919167995 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0478794574737549 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -425b1e77-5887-40b3-875e-c1f60dc6c513,908afab9-748c-4057-a2a9-d2686c5d52e0 |
| Jogador 6 | 2-5 | 93 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 6 | 0 | 12.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3482629656791687 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 94 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 16.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10123739391565323 | 0.0 | 0.0 | +0c6afd45-be8c-4f89-8fdc-938247537ab9 / -— |
| Jogador 6 | 2-5 | 95 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 16.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -6.5548174461582676e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4177583158016205 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 98 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015046876855194569 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 99 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014980083331465721 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 100 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 102 | BUY | STABILIZE | 90.0 | 6 | 7 | 0 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34070664644241333 | 0.0 | 0.0 | +2a7dd07f-3b48-489c-8822-9ec2434a01cf / -— |
| Jogador 6 | 2-6 | 103 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2770198881626129 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0039948029443621635 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011000051163136959 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 106 | PASS | STABILIZE | 90.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 112 | BUY | STABILIZE | 90.0 | 6 | 8 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9967613220214844 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 2-7 | 113 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8984922766685486 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 114 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500962395220995 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 116 | PASS | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 122 | BUY | STABILIZE | 90.0 | 6 | 7 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7942770719528198 | 0.0 | 0.0 | +ab127012-83d7-46f0-a16c-b20582d1179b / -— |
| Jogador 6 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 90.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1970425844192505 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 124 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12495273351669312 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.079838605430268e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020080827176570892 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 127 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0831904411315918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 128 | PASS | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 132 | SELL | STABILIZE | 80.0 | 6 | 7 | 0 | 20.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0126277981325984 | 0.0 | 0.0 | +— / -0c6afd45-be8c-4f89-8fdc-938247537ab9 |
| Jogador 6 | 3-2 | 133 | BUY | STABILIZE | 80.0 | 6 | 8 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379517793655396 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -18934be2-4988-4f62-9f62-07ba151231f2,53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 3-2 | 134 | BUY | STABILIZE | 80.0 | 6 | 7 | 0 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8362466096878052 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 135 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 6 | 0 | 16.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3628266751766205 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 136 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 6 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39382362365722656 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01449672132730484 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012627184391021729 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 139 | PASS | STABILIZE | 80.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 142 | BUY | STABILIZE | 70.0 | 6 | 12 | 1 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05258096382021904 | 0.0 | 0.0 | +25b16126-6e41-4649-a47f-42656ffc7a08 / -— |
| Jogador 6 | 3-3 | 143 | BUY | STABILIZE | 70.0 | 6 | 10 | 1 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13635294139385223 | 0.0 | 0.0 | +952adeb2-fe24-47af-9748-5131b91dcc06 / -— |
| Jogador 6 | 3-3 | 144 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00023949834576342255 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015037664212286472 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014600389637053013 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 147 | PASS | STABILIZE | 70.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 152 | BUY | STABILIZE | 70.0 | 6 | 14 | 1 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8334818482398987 | 0.0 | 0.0 | +2ed895f2-1e83-426c-88fc-b9fb6403835d / -43da0d73-facd-488b-b856-94e9496a97f9,9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 3-4 | 153 | BUY | STABILIZE | 70.0 | 6 | 11 | 1 | 18.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19398222863674164 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 6 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 70.0 | 6 | 8 | 0 | 18.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40667036175727844 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 155 | BUY | STABILIZE | 70.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7661017179489136 | 0.0 | 0.0 | +4698e3b3-0833-4895-a1f1-26b372b2f965 / -ab127012-83d7-46f0-a16c-b20582d1179b,c19cf6a8-c66e-4670-b0fc-fb83453f22e7 |
| Jogador 6 | 3-4 | 156 | MOVE_BENCH | STABILIZE | 70.0 | 6 | 6 | 0 | 18.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09522031992673874 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 157 | MOVE_BENCH | FAST8 | 70.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27934807538986206 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 158 | MOVE_BOARD | FAST8 | 70.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 159 | MOVE_BOARD | FAST8 | 70.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00348236714489758 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 160 | PASS | FAST8 | 70.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 162 | BUY | FAST8 | 70.0 | 6 | 11 | 1 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39697369933128357 | 0.0 | 0.0 | +506f7312-07d8-4165-bd67-f7a69cf9a19c / -— |
| Jogador 6 | 3-5 | 163 | BUY | FAST8 | 70.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20391811430454254 | 0.0 | 0.0 | +5b95b64a-b46a-4827-8613-307c8dadc072 / -— |
| Jogador 6 | 3-5 | 164 | MOVE_BOARD | FAST8 | 70.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1102230246251565e-16 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 165 | MOVE_BOARD | FAST8 | 70.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 166 | PASS | FAST8 | 70.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 172 | MOVE_BOARD | FAST8 | 60.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.044960469007492065 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 173 | SELL | FAST8 | 60.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5510873198509216 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 3-6 | 174 | BUY | FAST8 | 60.0 | 6 | 15 | 1 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7296803593635559 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 175 | MOVE_BOARD | FAST8 | 60.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048094745725393295 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 176 | MOVE_BOARD | FAST8 | 60.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 177 | MOVE_BOARD | FAST8 | 60.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015001095831394196 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 178 | PASS | FAST8 | 60.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 182 | MOVE_BOARD | FAST8 | 60.0 | 6 | 19 | 1 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 183 | MOVE_BOARD | FAST8 | 60.0 | 6 | 19 | 1 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 184 | PASS | FAST8 | 60.0 | 6 | 19 | 1 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 60.0 | 6 | 25 | 2 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22672857344150543 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 60.0 | 6 | 25 | 2 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2440195232629776 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 194 | MOVE_BOARD | FAST8 | 60.0 | 6 | 25 | 2 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.332904937764397e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 195 | SELL | FAST8 | 60.0 | 6 | 25 | 2 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4727681577205658 | 0.0 | 0.0 | +— / -4698e3b3-0833-4895-a1f1-26b372b2f965 |
| Jogador 6 | 4-1 | 196 | BUY | FAST8 | 60.0 | 6 | 30 | 3 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6970998644828796 | 0.0 | 0.0 | +b750b244-a898-479e-9a8e-f30a3f4b0005 / -— |
| Jogador 6 | 4-1 | 197 | MOVE_BOARD | FAST8 | 60.0 | 6 | 29 | 2 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.84527900982357e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 198 | MOVE_BOARD | FAST8 | 60.0 | 6 | 29 | 2 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015078467316925526 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 199 | MOVE_BOARD | FAST8 | 60.0 | 6 | 29 | 2 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998182654380798 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 200 | PASS | FAST8 | 60.0 | 6 | 29 | 2 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03500000014901161 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 202 | SELL | FAST8 | 48.0 | 6 | 36 | 3 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023160528391599655 | 0.0 | 0.0 | +— / -952adeb2-fe24-47af-9748-5131b91dcc06 |
| Jogador 6 | 4-2 | 203 | BUY | FAST8 | 48.0 | 6 | 38 | 3 | 30.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024085696786642075 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 6 | 4-2 | 204 | MOVE_BENCH | FAST8 | 48.0 | 6 | 35 | 3 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 205 | MOVE_BENCH | FAST8 | 48.0 | 6 | 35 | 3 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.779636561870575 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 206 | PASS | FAST8 | 48.0 | 6 | 35 | 3 | 28.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03928571566939354 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 212 | SELL | STABILIZE | 34.0 | 6 | 44 | 4 | 28.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 4-3 | 213 | BUY | STABILIZE | 34.0 | 6 | 47 | 4 | 28.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9273517727851868 | 0.0 | 0.0 | +b26a039f-581c-4de2-8a75-f7e8a4ef0e4a / -2c497125-ca06-46b1-a3b3-9a59d904705b,b750b244-a898-479e-9a8e-f30a3f4b0005 |
| Jogador 6 | 4-3 | 214 | MOVE_BENCH | STABILIZE | 34.0 | 6 | 46 | 4 | 24.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.5031762719154358 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 215 | BUY | STABILIZE | 34.0 | 6 | 46 | 4 | 28.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.33029162883758545 | 0.0 | 0.0 | +ed23d828-f4bc-4d6c-8cc1-c074047dac8a / -— |
| Jogador 6 | 4-3 | 216 | MOVE_BENCH | STABILIZE | 34.0 | 6 | 42 | 4 | 28.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.6625364422798157 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 217 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 6 | 42 | 4 | 32.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15105471014976501 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 218 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 6 | 42 | 4 | 32.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1385311782360077 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 219 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 6 | 42 | 4 | 32.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.16028298437595367 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 220 | MOVE_BENCH | STABILIZE | 34.0 | 6 | 42 | 4 | 32.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14740408957004547 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 222 | BUY | ALL_IN | 20.0 | 6 | 52 | 5 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4731415808200836 | 0.0 | 0.0 | +c49cf468-6fa4-4d94-bc3a-9dc8f7111626 / -— |
| Jogador 6 | 4-4 | 223 | MOVE_BOARD | ALL_IN | 20.0 | 6 | 51 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01175761129707098 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 224 | MOVE_BOARD | ALL_IN | 20.0 | 6 | 51 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07663680613040924 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 225 | MOVE_BOARD | ALL_IN | 20.0 | 6 | 51 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014978812076151371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 226 | MOVE_BOARD | ALL_IN | 20.0 | 6 | 51 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015003378503024578 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 227 | PASS | ALL_IN | 20.0 | 6 | 51 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4452776610851288 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 232 | MOVE_BOARD | ALL_IN | 20.0 | 6 | 62 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.607697858067695e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 233 | SELL | ALL_IN | 20.0 | 6 | 62 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5935999751091003 | 0.0 | 0.0 | +— / -b26a039f-581c-4de2-8a75-f7e8a4ef0e4a |
| Jogador 6 | 4-5 | 234 | BUY | ALL_IN | 20.0 | 6 | 65 | 5 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9073916673660278 | 0.0 | 0.0 | +7e0d7932-1b83-4918-9292-6e60957e6022 / -— |
| Jogador 6 | 4-5 | 235 | EQUIP_FROM_INVENTORY | ALL_IN | 20.0 | 6 | 63 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.17677892744541168 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 236 | MOVE_BENCH | ALL_IN | 20.0 | 6 | 63 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47785046696662903 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 237 | MOVE_BENCH | ALL_IN | 20.0 | 6 | 63 | 5 | 32.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38138943910598755 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 238 | PASS | ALL_IN | 20.0 | 6 | 63 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4570750296115875 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 242 | SELL | ALL_IN | 20.0 | 6 | 74 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020577069371938705 | 0.0 | 0.0 | +— / -3bbd7105-b508-437d-ac84-11e01a499779 |
| Jogador 6 | 4-6 | 243 | BUY | ALL_IN | 20.0 | 6 | 77 | 5 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2725098431110382 | 0.0 | 0.0 | +57d86f23-f167-472f-9878-21dcddc0a5f7 / -— |
| Jogador 6 | 4-6 | 244 | REROLL | ALL_IN | 20.0 | 6 | 76 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 245 | SELL | ALL_IN | 20.0 | 6 | 74 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03343333303928375 | 0.0 | 0.0 | +— / -a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 |
| Jogador 6 | 4-6 | 246 | BUY | ALL_IN | 20.0 | 6 | 77 | 5 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9104298949241638 | 0.0 | 0.0 | +d6a929d8-6d7c-4bcd-880d-d819daca2ae0 / -— |
| Jogador 6 | 4-6 | 247 | REROLL | ALL_IN | 20.0 | 6 | 75 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 248 | REROLL | ALL_IN | 20.0 | 6 | 73 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 249 | SELL | ALL_IN | 20.0 | 6 | 71 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5911999940872192 | 0.0 | 0.0 | +— / -c49cf468-6fa4-4d94-bc3a-9dc8f7111626 |
| Jogador 6 | 4-6 | 250 | BUY | ALL_IN | 20.0 | 6 | 72 | 5 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0197169780731201 | 0.0 | 0.0 | +b0c8ce74-5ce1-4ed0-82ac-f95013475f3c / -5b95b64a-b46a-4827-8613-307c8dadc072,7e0d7932-1b83-4918-9292-6e60957e6022 |
| Jogador 6 | 4-7 | 252 | MOVE_BENCH | ALL_IN | 20.0 | 6 | 82 | 5 | 32.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4551738500595093 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 253 | BUY | ALL_IN | 20.0 | 6 | 82 | 5 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19615837931632996 | 0.0 | 0.0 | +8d75ef64-e2c3-47b6-a336-c9e5867158e5 / -— |
| Jogador 6 | 4-7 | 254 | BUY | ALL_IN | 20.0 | 6 | 79 | 5 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17090870440006256 | 0.0 | 0.0 | +a492f78e-91f0-48cb-891a-6518551da328 / -— |
| Jogador 6 | 4-7 | 255 | REROLL | ALL_IN | 20.0 | 6 | 77 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 256 | REROLL | ALL_IN | 20.0 | 6 | 75 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 257 | SELL | ALL_IN | 20.0 | 6 | 73 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5960000157356262 | 0.0 | 0.0 | +— / -b0c8ce74-5ce1-4ed0-82ac-f95013475f3c |
| Jogador 6 | 4-7 | 258 | BUY | ALL_IN | 20.0 | 6 | 78 | 5 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40056687593460083 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -— |
| Jogador 6 | 4-7 | 259 | MOVE_BOARD | ALL_IN | 20.0 | 6 | 77 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013999642804265022 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 260 | REROLL | ALL_IN | 20.0 | 6 | 77 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 20.0 | 6 | 86 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17469331622123718 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 20.0 | 6 | 86 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09961548447608948 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 264 | SELL | ALL_IN | 20.0 | 6 | 86 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04267676919698715 | 0.0 | 0.0 | +— / -a492f78e-91f0-48cb-891a-6518551da328 |
| Jogador 6 | 5-1 | 265 | BUY | ALL_IN | 20.0 | 6 | 88 | 5 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9351986050605774 | 0.0 | 0.0 | +1512b230-15a6-405f-9b6b-4387a3091648 / -— |
| Jogador 6 | 5-1 | 266 | SELL | ALL_IN | 20.0 | 6 | 87 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049479544162750244 | 0.0 | 0.0 | +— / -8d75ef64-e2c3-47b6-a336-c9e5867158e5 |
| Jogador 6 | 5-1 | 267 | BUY | ALL_IN | 20.0 | 6 | 90 | 5 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5004136562347412 | 0.0 | 0.0 | +b2517873-8317-401b-8461-1d86969edbd7 / -— |
| Jogador 6 | 5-1 | 268 | MOVE_BOARD | ALL_IN | 20.0 | 6 | 89 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013375958427786827 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 269 | MOVE_BOARD | ALL_IN | 20.0 | 6 | 89 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06347520649433136 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 270 | MOVE_BOARD | ALL_IN | 20.0 | 6 | 89 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.033475909382104874 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 272 | SELL | ALL_IN | 6.0 | 6 | 99 | 5 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5911999940872192 | 0.0 | 0.0 | +— / -b2517873-8317-401b-8461-1d86969edbd7 |
| Jogador 6 | 5-2 | 273 | BUY | ALL_IN | 6.0 | 6 | 100 | 5 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0832148790359497 | 0.0 | 0.0 | +2b89bd83-8449-4c63-9da2-62a46c68bdf5 / -2a7dd07f-3b48-489c-8822-9ec2434a01cf,d6a929d8-6d7c-4bcd-880d-d819daca2ae0 |
| Jogador 6 | 5-2 | 274 | MOVE_BENCH | ALL_IN | 6.0 | 6 | 98 | 5 | 32.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5908926129341125 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 275 | MOVE_BOARD | ALL_IN | 6.0 | 6 | 98 | 5 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014987845905125141 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 276 | BUY | ALL_IN | 6.0 | 6 | 98 | 5 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2789558470249176 | 0.0 | 0.0 | +674bcfdb-fddd-498c-ba65-ef3a3b989f07 / -— |
| Jogador 6 | 5-2 | 277 | MOVE_BOARD | ALL_IN | 6.0 | 6 | 95 | 5 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.496762928989483e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 278 | REROLL | ALL_IN | 6.0 | 6 | 95 | 5 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 279 | BUY | ALL_IN | 6.0 | 6 | 93 | 5 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0836749076843262 | 0.0 | 0.0 | +b250e22d-7193-4ea5-879d-5c7b41145719 / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede,fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 5-2 | 280 | BUY | ALL_IN | 6.0 | 6 | 90 | 5 | 40.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43184521794319153 | 0.0 | 0.0 | +3ae84928-bc2a-4c1e-8663-b7ad05da4501 / -— |
| Jogador 6 | 5-3 | 282 | BUY | ALL_IN | 6.0 | 7 | 98 | 5 | 40.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5143221020698547 | 0.0 | 0.0 | +b311d350-7bab-48ee-9833-0883606b4a2f / -— |
| Jogador 6 | 5-3 | 283 | SELL | ALL_IN | 6.0 | 7 | 95 | 5 | 40.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5996000170707703 | 0.0 | 0.0 | +— / -b250e22d-7193-4ea5-879d-5c7b41145719 |
| Jogador 6 | 5-3 | 284 | BUY | ALL_IN | 6.0 | 7 | 103 | 5 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0351240634918213 | 0.0 | 0.0 | +6eff87be-d18f-4f46-a9c6-9ae977c887e0 / -— |
| Jogador 6 | 5-3 | 285 | MOVE_BENCH | ALL_IN | 6.0 | 7 | 100 | 5 | 40.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40001848340034485 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 286 | BUY | ALL_IN | 6.0 | 7 | 100 | 5 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4344724714756012 | 0.0 | 0.0 | +a37d8478-8a98-4099-bb18-3602d68764f5 / -— |
| Jogador 6 | 5-3 | 287 | MOVE_BOARD | ALL_IN | 6.0 | 7 | 97 | 5 | 46.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.2760497156705242e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 288 | MOVE_BOARD | ALL_IN | 6.0 | 7 | 97 | 5 | 46.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01506155263632536 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 289 | MOVE_BOARD | ALL_IN | 6.0 | 7 | 97 | 5 | 46.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015115310437977314 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 290 | PASS | ALL_IN | 6.0 | 7 | 97 | 5 | 46.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5475194454193115 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5923603177070618 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589178562164307 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15055713057518005 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 21 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 22 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01892075128853321 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 23 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40501677989959717 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0479782819747925 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 32 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23226182162761688 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 33 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3358203172683716 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011522081680595875 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 35 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0209136009216309 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 44 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19077573716640472 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 45 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12621930241584778 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 1-4 | 46 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6381460428237915 | 0.0 | 0.0 | +— / -d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 1-4 | 47 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16201309859752655 | 0.0 | 0.0 | +a179e7d4-31e2-4a74-9905-0daede16517e / -— |
| Jogador 7 | 1-4 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3396373391151428 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07905701547861099 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03088962659239769 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 51 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.355741411447525 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0218601506203413 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9638639092445374 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5841108560562134 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2015884816646576 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16966351866722107 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34573835134506226 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4026520848274231 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033463701605796814 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0478956699371338 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6876066327095032 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 64 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 65 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-2 | 66 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04550499841570854 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 67 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41804277896881104 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 68 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17488038539886475 | 0.0 | 0.0 | +98558a52-389f-46fc-b370-6345603f4103 / -— |
| Jogador 7 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 70 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0386943481862545 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0363892316818237 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -— |
| Jogador 7 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7809739708900452 | 0.0 | 0.0 | +0547b747-1e37-49ba-a447-67c526a8cd50 / -— |
| Jogador 7 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 75 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 76 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 77 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3100542426109314 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 83 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25775548815727234 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04642852768301964 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 85 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 1 | 0 | 16.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989396944642067 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09460029751062393 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 87 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4936666786670685 | 0.0 | 0.0 | +— / -98558a52-389f-46fc-b370-6345603f4103 |
| Jogador 7 | 2-4 | 88 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09329134970903397 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 89 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07699999958276749 | 0.0 | 0.0 | +— / -0547b747-1e37-49ba-a447-67c526a8cd50 |
| Jogador 7 | 2-4 | 90 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3250313103199005 | 0.0 | 0.0 | +3280b28e-bd8f-494b-a78d-111744e2178b / -— |
| Jogador 7 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3076799809932709 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 93 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 4 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0915377214550972 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 94 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 4 | 0 | 18.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3912971019744873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 95 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 24.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 96 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 24.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041315723210573196 | 0.0 | 0.0 | +— / -a179e7d4-31e2-4a74-9905-0daede16517e |
| Jogador 7 | 2-5 | 97 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 24.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0852893739938736 | 0.0 | 0.0 | +— / -3280b28e-bd8f-494b-a78d-111744e2178b |
| Jogador 7 | 2-5 | 98 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 24.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 99 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 24.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 100 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 24.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 102 | BUY | STABILIZE | 94.0 | 6 | 5 | 0 | 24.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.976452112197876 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 103 | BUY | STABILIZE | 94.0 | 6 | 2 | 0 | 24.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.045748233795166 | 0.0 | 0.0 | +a146f2d5-4da5-4c0e-bb09-de3177c72417 / -3394d5fc-ee48-4a08-8669-05984c804b53,5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 0 | 0 | 16.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21862371265888214 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 105 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 0 | 0 | 18.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08603416383266449 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 106 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1762682944536209 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 107 | MOVE_BOARD | FAST8 | 94.0 | 6 | 0 | 0 | 26.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014558399096131325 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 108 | MOVE_BENCH | FAST8 | 94.0 | 6 | 0 | 0 | 26.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40528878569602966 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 109 | MOVE_BOARD | FAST8 | 94.0 | 6 | 0 | 0 | 28.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00022603676188737154 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 110 | MOVE_BOARD | FAST8 | 94.0 | 6 | 0 | 0 | 28.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.977098898161785e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 112 | MOVE_BOARD | FAST8 | 94.0 | 6 | 6 | 0 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 113 | BUY | FAST8 | 94.0 | 6 | 6 | 0 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12387809157371521 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 114 | MOVE_BOARD | FAST8 | 94.0 | 6 | 3 | 0 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 115 | BUY | FAST8 | 94.0 | 6 | 3 | 0 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10491105914115906 | 0.0 | 0.0 | +ac02c0c4-a10d-497d-b6c1-d458ad7ae58c / -— |
| Jogador 7 | 2-7 | 116 | MOVE_BOARD | FAST8 | 94.0 | 6 | 1 | 0 | 28.0 | Inferno/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.989683348976541e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 117 | MOVE_BOARD | FAST8 | 94.0 | 6 | 1 | 0 | 28.0 | Inferno/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014992088079452515 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 118 | PASS | FAST8 | 94.0 | 6 | 1 | 0 | 28.0 | Inferno/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 122 | CRAFT_AND_EQUIP | FAST8 | 94.0 | 6 | 6 | 0 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14802779257297516 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 123 | MOVE_BENCH | FAST8 | 94.0 | 6 | 6 | 0 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39969807863235474 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 124 | BUY | FAST8 | 94.0 | 6 | 6 | 0 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09765968471765518 | 0.0 | 0.0 | +033a84d9-70f6-46a8-a6eb-a2f03be70400 / -— |
| Jogador 7 | 3-1 | 125 | BUY_XP | FAST8 | 94.0 | 6 | 4 | 0 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 126 | MOVE_BOARD | FAST8 | 94.0 | 6 | 0 | 0 | 32.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 127 | MOVE_BOARD | FAST8 | 94.0 | 6 | 0 | 0 | 32.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997709542512894 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 128 | PASS | FAST8 | 94.0 | 6 | 0 | 0 | 32.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 132 | BUY | FAST8 | 85.0 | 6 | 5 | 0 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35694071650505066 | 0.0 | 0.0 | +fa331d8d-1e0c-49b4-848e-8ad58859331c / -— |
| Jogador 7 | 3-2 | 133 | BUY | FAST8 | 85.0 | 6 | 3 | 0 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5533363819122314 | 0.0 | 0.0 | +96bf8f0a-9fe1-4182-95dc-903c1e623983 / -ac02c0c4-a10d-497d-b6c1-d458ad7ae58c,fa331d8d-1e0c-49b4-848e-8ad58859331c |
| Jogador 7 | 3-2 | 134 | MOVE_BOARD | FAST8 | 85.0 | 6 | 1 | 0 | 32.0 | Inferno/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00010421476326882839 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 135 | MOVE_BOARD | FAST8 | 85.0 | 6 | 1 | 0 | 32.0 | Inferno/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 136 | MOVE_BOARD | FAST8 | 85.0 | 6 | 1 | 0 | 32.0 | Inferno/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 137 | PASS | FAST8 | 85.0 | 6 | 1 | 0 | 32.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 142 | BUY | FAST8 | 85.0 | 6 | 7 | 0 | 32.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20238542556762695 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 143 | BUY_XP | FAST8 | 85.0 | 6 | 4 | 0 | 32.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 144 | MOVE_BOARD | FAST8 | 85.0 | 6 | 0 | 0 | 32.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.4985217805806315e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 145 | MOVE_BOARD | FAST8 | 85.0 | 6 | 0 | 0 | 32.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999122358858585 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 146 | PASS | FAST8 | 85.0 | 6 | 0 | 0 | 32.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 152 | BUY | FAST8 | 85.0 | 6 | 7 | 0 | 32.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7620481252670288 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -2c7e844d-925a-43bb-8be8-65a71d11f964,6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 3-4 | 153 | BUY | FAST8 | 85.0 | 6 | 4 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6816055774688721 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -— |
| Jogador 7 | 3-4 | 154 | MOVE_BENCH | FAST8 | 85.0 | 6 | 3 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40236029028892517 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 155 | MOVE_BOARD | FAST8 | 85.0 | 6 | 3 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 156 | MOVE_BOARD | FAST8 | 85.0 | 6 | 3 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 157 | PASS | FAST8 | 85.0 | 6 | 3 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 162 | BUY | FAST8 | 85.0 | 6 | 9 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08478350192308426 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 7 | 3-5 | 163 | MOVE_BOARD | FAST8 | 85.0 | 6 | 8 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0009966858197003603 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 164 | MOVE_BOARD | FAST8 | 85.0 | 6 | 8 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06528712064027786 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 165 | PASS | FAST8 | 85.0 | 6 | 8 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 172 | BUY | FAST8 | 85.0 | 6 | 15 | 1 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7329369187355042 | 0.0 | 0.0 | +6caec849-54f8-4ec1-90a4-fc0587510013 / -— |
| Jogador 7 | 3-6 | 173 | MOVE_BOARD | FAST8 | 85.0 | 6 | 12 | 1 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003939080983400345 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 174 | BUY_XP | FAST8 | 85.0 | 6 | 12 | 1 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 175 | BUY_XP | FAST8 | 85.0 | 6 | 8 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 176 | BUY_XP | FAST8 | 85.0 | 6 | 4 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 177 | MOVE_BOARD | FAST8 | 85.0 | 6 | 0 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 178 | MOVE_BOARD | FAST8 | 85.0 | 6 | 0 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 179 | PASS | FAST8 | 85.0 | 6 | 0 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 182 | SELL | FAST8 | 85.0 | 7 | 7 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -96bf8f0a-9fe1-4182-95dc-903c1e623983 |
| Jogador 7 | 3-7 | 183 | BUY | FAST8 | 85.0 | 7 | 12 | 1 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6517685651779175 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 184 | MOVE_BENCH | FAST8 | 85.0 | 7 | 8 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.399168998003006 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 185 | BUY | FAST8 | 85.0 | 7 | 8 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6920510530471802 | 0.0 | 0.0 | +21135c93-ae87-47a0-899c-7eaa0c2c30b8 / -— |
| Jogador 7 | 3-7 | 186 | BUY_XP | FAST8 | 85.0 | 7 | 6 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 187 | MOVE_BOARD | FAST8 | 85.0 | 7 | 2 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 188 | MOVE_BOARD | FAST8 | 85.0 | 7 | 2 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 189 | PASS | FAST8 | 85.0 | 7 | 2 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 85.0 | 7 | 8 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10940434038639069 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 85.0 | 7 | 8 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09164326637983322 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 194 | BUY_XP | FAST8 | 85.0 | 7 | 8 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 195 | BUY_XP | FAST8 | 85.0 | 7 | 4 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 196 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 197 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.000419601914472878 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 198 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014628434553742409 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 199 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999797567725182 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 200 | PASS | FAST8 | 85.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 202 | BUY_XP | FAST8 | 85.0 | 7 | 8 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 203 | BUY_XP | FAST8 | 85.0 | 7 | 4 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 204 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.581756330589997e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 205 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 206 | PASS | FAST8 | 85.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 212 | SELL | FAST8 | 85.0 | 7 | 9 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 4-3 | 213 | BUY | FAST8 | 85.0 | 7 | 17 | 1 | 32.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3844159245491028 | 0.0 | 0.0 | +677ea844-e1bf-4c68-a0b0-136abb86ba7b / -— |
| Jogador 7 | 4-3 | 214 | BUY_XP | FAST8 | 85.0 | 7 | 14 | 1 | 32.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006039999891072512 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 215 | BUY_XP | FAST8 | 85.0 | 7 | 10 | 1 | 32.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 216 | BUY_XP | FAST8 | 85.0 | 7 | 6 | 0 | 32.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 217 | MOVE_BOARD | FAST8 | 85.0 | 7 | 2 | 0 | 32.0 | Inferno/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 218 | MOVE_BOARD | FAST8 | 85.0 | 7 | 2 | 0 | 32.0 | Inferno/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 219 | PASS | FAST8 | 85.0 | 7 | 2 | 0 | 32.0 | Inferno/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 222 | SELL | FAST8 | 85.0 | 7 | 11 | 1 | 32.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03216666728258133 | 0.0 | 0.0 | +— / -42f739bb-e676-4a27-a96f-c09d09d592bb |
| Jogador 7 | 4-4 | 223 | BUY | FAST8 | 85.0 | 7 | 12 | 1 | 32.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6839540004730225 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -599caeca-96ef-4308-b6cd-f65b005879e2,6caec849-54f8-4ec1-90a4-fc0587510013 |
| Jogador 7 | 4-4 | 224 | BUY | FAST8 | 85.0 | 7 | 9 | 0 | 32.0 | Inferno/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10410334914922714 | 0.0 | 0.0 | +7643f027-a90f-4f3a-8b4c-7be4cba17f95 / -— |
| Jogador 7 | 4-4 | 225 | MOVE_BENCH | FAST8 | 85.0 | 7 | 6 | 0 | 32.0 | Inferno/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799707490950823 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 226 | BUY_XP | FAST8 | 85.0 | 7 | 6 | 0 | 34.0 | Inferno/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 227 | MOVE_BOARD | FAST8 | 85.0 | 7 | 2 | 0 | 34.0 | Inferno/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.3972419310448458e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 228 | MOVE_BOARD | FAST8 | 85.0 | 7 | 2 | 0 | 34.0 | Inferno/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015027765184640884 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 229 | MOVE_BOARD | FAST8 | 85.0 | 7 | 2 | 0 | 34.0 | Inferno/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01498577930033207 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 230 | PASS | FAST8 | 85.0 | 7 | 2 | 0 | 34.0 | Inferno/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 232 | BUY | FAST8 | 85.0 | 7 | 10 | 1 | 34.0 | Inferno/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13598857820034027 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 7 | 4-5 | 233 | MOVE_BOARD | FAST8 | 85.0 | 7 | 8 | 0 | 34.0 | Inferno/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.4808016405586386e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 234 | MOVE_BOARD | FAST8 | 85.0 | 7 | 8 | 0 | 34.0 | Inferno/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 235 | PASS | FAST8 | 85.0 | 7 | 8 | 0 | 34.0 | Inferno/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 242 | SELL | FAST8 | 85.0 | 7 | 17 | 1 | 34.0 | Inferno/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 |
| Jogador 7 | 4-6 | 243 | BUY | FAST8 | 85.0 | 7 | 25 | 2 | 34.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2247181385755539 | 0.0 | 0.0 | +de8de4b5-48ea-4947-ae08-2b90d94b0fc1 / -— |
| Jogador 7 | 4-6 | 244 | MOVE_BOARD | FAST8 | 85.0 | 7 | 22 | 2 | 34.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.965394044935238e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 245 | MOVE_BOARD | FAST8 | 85.0 | 7 | 22 | 2 | 34.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999987557530403 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 246 | MOVE_BOARD | FAST8 | 85.0 | 7 | 22 | 2 | 34.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 247 | PASS | FAST8 | 85.0 | 7 | 22 | 2 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 252 | SELL | FAST8 | 73.0 | 7 | 29 | 2 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08958975970745087 | 0.0 | 0.0 | +— / -7643f027-a90f-4f3a-8b4c-7be4cba17f95 |
| Jogador 7 | 4-7 | 253 | BUY | FAST8 | 73.0 | 7 | 32 | 3 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7846734523773193 | 0.0 | 0.0 | +986fbe1e-1826-4be7-a5d6-410a4c0a3f2f / -033a84d9-70f6-46a8-a6eb-a2f03be70400,21135c93-ae87-47a0-899c-7eaa0c2c30b8 |
| Jogador 7 | 4-7 | 254 | MOVE_BENCH | FAST8 | 73.0 | 7 | 30 | 3 | 26.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1515931636095047 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 255 | BUY_XP | FAST8 | 73.0 | 7 | 30 | 3 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10692500323057175 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 256 | BUY_XP | FAST8 | 73.0 | 7 | 26 | 2 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09459374845027924 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 257 | MOVE_BENCH | ECON | 73.0 | 8 | 22 | 2 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22516222298145294 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 258 | BUY | ECON | 73.0 | 8 | 22 | 2 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014996889978647232 | 0.0 | 0.0 | +45ae38c5-7e69-41bb-9a93-f14db3af3587 / -— |
| Jogador 7 | 4-7 | 259 | MOVE_BOARD | ECON | 73.0 | 8 | 20 | 2 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.5461549992323853e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 260 | MOVE_BOARD | ECON | 73.0 | 8 | 20 | 2 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 262 | BUY | ECON | 73.0 | 8 | 27 | 2 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5153213143348694 | 0.0 | 0.0 | +57ba484a-6228-4263-8171-00a8a5893bea / -— |
| Jogador 7 | 5-1 | 263 | CRAFT_AND_EQUIP | ECON | 73.0 | 8 | 25 | 2 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10101711004972458 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 264 | CRAFT_AND_EQUIP | ECON | 73.0 | 8 | 25 | 2 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13663850724697113 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 265 | MOVE_BOARD | ECON | 73.0 | 8 | 25 | 2 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 266 | MOVE_BOARD | ECON | 73.0 | 8 | 25 | 2 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 267 | PASS | ECON | 73.0 | 8 | 25 | 2 | 36.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035357143729925156 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 272 | BUY | ECON | 57.0 | 8 | 33 | 3 | 38.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26969605684280396 | 0.0 | 0.0 | +e5f61076-ec13-419b-a4e8-d91b9975cfd6 / -— |
| Jogador 7 | 5-2 | 273 | MOVE_BOARD | ECON | 57.0 | 8 | 30 | 3 | 38.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0022368377540260553 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 274 | MOVE_BOARD | ECON | 57.0 | 8 | 30 | 3 | 38.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015849636867642403 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 275 | PASS | ECON | 57.0 | 8 | 30 | 3 | 38.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03928571566939354 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 282 | SELL | ECON | 57.0 | 8 | 39 | 3 | 38.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38747304677963257 | 0.0 | 0.0 | +— / -45ae38c5-7e69-41bb-9a93-f14db3af3587 |
| Jogador 7 | 5-3 | 283 | BUY | ECON | 57.0 | 8 | 41 | 4 | 38.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7844836115837097 | 0.0 | 0.0 | +bdee5671-864a-47c9-9576-9e0d8d2a7c6a / -— |
| Jogador 7 | 5-3 | 284 | MOVE_BENCH | ECON | 57.0 | 8 | 39 | 3 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09812910854816437 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 285 | MOVE_BOARD | ECON | 57.0 | 8 | 39 | 3 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 286 | MOVE_BOARD | ECON | 57.0 | 8 | 39 | 3 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013812566176056862 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 287 | PASS | ECON | 57.0 | 8 | 39 | 3 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20035713911056519 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 292 | SELL | ECON | 57.0 | 8 | 50 | 5 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029927697032690048 | 0.0 | 0.0 | +— / -57ba484a-6228-4263-8171-00a8a5893bea |
| Jogador 7 | 5-4 | 293 | BUY | ECON | 57.0 | 8 | 52 | 5 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7927505373954773 | 0.0 | 0.0 | +2ac6d717-87f1-4421-929e-1934a9317e72 / -— |
| Jogador 7 | 5-4 | 294 | MOVE_BENCH | ECON | 57.0 | 8 | 49 | 4 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6500382423400879 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 295 | MOVE_BENCH | ECON | 57.0 | 8 | 49 | 4 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32368233799934387 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 296 | PASS | ECON | 57.0 | 8 | 49 | 4 | 40.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05421428754925728 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 302 | SELL | ECON | 57.0 | 8 | 59 | 5 | 40.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5031567811965942 | 0.0 | 0.0 | +— / -242805ca-f275-4e04-a2f5-81e0b6680dd1 |
| Jogador 7 | 5-5 | 303 | BUY | ECON | 57.0 | 8 | 60 | 5 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9022305011749268 | 0.0 | 0.0 | +ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 / -584991bb-37b3-4ac1-8e29-14e0d74c5e78,677ea844-e1bf-4c68-a0b0-136abb86ba7b |
| Jogador 7 | 5-5 | 304 | MOVE_BENCH | ECON | 57.0 | 8 | 57 | 5 | 34.0 | Inferno/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48540589213371277 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 305 | MOVE_BOARD | ECON | 57.0 | 8 | 57 | 5 | 36.0 | Inferno/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014882233925163746 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 306 | MOVE_BOARD | ECON | 57.0 | 8 | 57 | 5 | 36.0 | Inferno/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999236911535263 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 307 | PASS | ECON | 57.0 | 8 | 57 | 5 | 36.0 | Inferno/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2464265078306198 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 312 | MOVE_BENCH | ECON | 41.0 | 8 | 67 | 5 | 36.0 | Inferno/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09720047563314438 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 313 | BUY | ECON | 41.0 | 8 | 67 | 5 | 40.0 | Inferno/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004957981873303652 | 0.0 | 0.0 | +e99948bb-f38f-41e0-b1c4-1864c35ffe14 / -— |
| Jogador 7 | 5-6 | 314 | MOVE_BENCH | ECON | 41.0 | 8 | 63 | 5 | 40.0 | Inferno/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3445296287536621 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 315 | MOVE_BENCH | ECON | 41.0 | 8 | 63 | 5 | 40.0 | Inferno/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020179087296128273 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 316 | PASS | ECON | 41.0 | 8 | 63 | 5 | 46.0 | Inferno/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2601122558116913 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 322 | BUY | ECON | 41.0 | 8 | 74 | 5 | 46.0 | Inferno/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6332088112831116 | 0.0 | 0.0 | +41cebf65-3d00-41d3-bc56-d1d126a6e261 / -— |
| Jogador 7 | 5-7 | 323 | SELL | ECON | 41.0 | 8 | 70 | 5 | 46.0 | Inferno/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.460681676864624 | 0.0 | 0.0 | +— / -ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 |
| Jogador 7 | 5-7 | 324 | BUY | ECON | 41.0 | 8 | 78 | 5 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35725295543670654 | 0.0 | 0.0 | +586ccfc6-ee5a-4ca1-98c2-31dec4273deb / -— |
| Jogador 7 | 5-7 | 325 | MOVE_BENCH | ECON | 41.0 | 8 | 76 | 5 | 46.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023743418976664543 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 326 | MOVE_BENCH | ECON | 41.0 | 8 | 76 | 5 | 40.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6625996828079224 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 327 | PASS | ECON | 41.0 | 8 | 76 | 5 | 40.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11765771359205246 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ECON | 41.0 | 8 | 86 | 5 | 40.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12038761377334595 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 333 | MOVE_BENCH | ECON | 41.0 | 8 | 86 | 5 | 40.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3316541314125061 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 334 | SELL | ECON | 41.0 | 8 | 86 | 5 | 42.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0309169739484787 | 0.0 | 0.0 | +— / -7159421f-b5ea-4d10-9cc5-59186d62983d |
| Jogador 7 | 6-1 | 335 | BUY | ECON | 41.0 | 8 | 87 | 5 | 42.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.063161849975586 | 0.0 | 0.0 | +d7ce3b58-1354-4970-94e8-17db783b9353 / -2ac6d717-87f1-4421-929e-1934a9317e72,de8de4b5-48ea-4947-ae08-2b90d94b0fc1 |
| Jogador 7 | 6-1 | 336 | EQUIP_FROM_INVENTORY | ECON | 41.0 | 8 | 84 | 5 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14083237946033478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 337 | EQUIP_FROM_INVENTORY | ECON | 41.0 | 8 | 84 | 5 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09622335433959961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 338 | MOVE_BENCH | ECON | 41.0 | 8 | 84 | 5 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09757933765649796 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 339 | MOVE_BENCH | ECON | 41.0 | 8 | 84 | 5 | 52.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.762133002281189 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 340 | MOVE_BENCH | ECON | 41.0 | 8 | 84 | 5 | 46.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40891197323799133 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 342 | BUY | ALL_IN | 23.0 | 8 | 94 | 5 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9772518873214722 | 0.0 | 0.0 | +dca007d3-1486-416d-93f2-e353911c46c5 / -— |
| Jogador 7 | 6-2 | 343 | BUY | ALL_IN | 23.0 | 8 | 92 | 5 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1108027696609497 | 0.0 | 0.0 | +ed77113d-b6af-4207-92c3-c4b4e1fcda54 / -bdee5671-864a-47c9-9576-9e0d8d2a7c6a,ec9662c5-0734-41a3-9999-224d7716228b |
| Jogador 7 | 6-2 | 344 | BUY | ALL_IN | 23.0 | 8 | 90 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0260441303253174 | 0.0 | 0.0 | +d140c71c-0721-4d2e-97c7-3efd32bd59db / -41cebf65-3d00-41d3-bc56-d1d126a6e261,e99948bb-f38f-41e0-b1c4-1864c35ffe14 |
| Jogador 7 | 6-2 | 345 | MOVE_BENCH | ALL_IN | 23.0 | 8 | 86 | 5 | 30.0 | Inferno/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16114753484725952 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 346 | MOVE_BENCH | ALL_IN | 23.0 | 8 | 86 | 5 | 34.0 | Inferno/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47553104162216187 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 347 | MOVE_BOARD | ALL_IN | 23.0 | 8 | 86 | 5 | 40.0 | Inferno/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0153654795140028 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 348 | MOVE_BOARD | ALL_IN | 23.0 | 8 | 86 | 5 | 40.0 | Inferno/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014722147956490517 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 349 | PASS | ALL_IN | 23.0 | 8 | 86 | 5 | 40.0 | Inferno/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6741834878921509 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 352 | BUY | ALL_IN | 23.0 | 8 | 96 | 5 | 40.0 | Inferno/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1806625127792358 | 0.0 | 0.0 | +664aa5f5-1d67-4e4d-81a0-8c951da00a26 / -8a52858d-da47-4de9-8e91-8612788cb8fd,fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 6-3 | 353 | BUY | ALL_IN | 23.0 | 8 | 92 | 5 | 32.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0399768352508545 | 0.0 | 0.0 | +50aaff79-fc62-4d74-93f6-dcc85c9b8668 / -— |
| Jogador 7 | 6-3 | 354 | REROLL | ALL_IN | 23.0 | 8 | 89 | 5 | 32.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 355 | MOVE_BENCH | ALL_IN | 23.0 | 8 | 87 | 5 | 32.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10027148574590683 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 356 | MOVE_BOARD | ALL_IN | 23.0 | 8 | 87 | 5 | 46.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 357 | MOVE_BOARD | ALL_IN | 23.0 | 8 | 87 | 5 | 46.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014995510689914227 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 358 | PASS | ALL_IN | 23.0 | 8 | 87 | 5 | 46.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6754673719406128 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 362 | BUY | ALL_IN | 6.0 | 8 | 98 | 5 | 52.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1810904741287231 | 0.0 | 0.0 | +42a24672-dcd0-4f0c-839a-82327962d77e / -50aaff79-fc62-4d74-93f6-dcc85c9b8668,e5f61076-ec13-419b-a4e8-d91b9975cfd6 |
| Jogador 7 | 6-4 | 363 | BUY | ALL_IN | 6.0 | 8 | 95 | 5 | 46.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28569743037223816 | 0.0 | 0.0 | +6f89a47a-1ab1-48ed-ba66-bcbaa3e74231 / -— |
| Jogador 7 | 6-4 | 364 | REROLL | ALL_IN | 6.0 | 8 | 93 | 5 | 46.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 365 | BUY | ALL_IN | 6.0 | 8 | 91 | 5 | 46.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5022976994514465 | 0.0 | 0.0 | +32033311-58ac-4308-8248-bb92f2bb9372 / -— |
| Jogador 7 | 6-4 | 366 | REROLL | ALL_IN | 6.0 | 8 | 88 | 5 | 46.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 367 | BUY | ALL_IN | 6.0 | 8 | 86 | 5 | 46.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0050338506698608 | 0.0 | 0.0 | +ba681672-d9c2-4490-82fb-d915c9aaf122 / -— |
| Jogador 7 | 6-4 | 368 | REROLL | ALL_IN | 6.0 | 8 | 85 | 5 | 46.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 369 | SELL | ALL_IN | 6.0 | 8 | 83 | 5 | 46.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8495000004768372 | 0.0 | 0.0 | +— / -ed77113d-b6af-4207-92c3-c4b4e1fcda54 |
| Jogador 7 | 6-4 | 370 | BUY | ALL_IN | 6.0 | 8 | 88 | 5 | 46.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8029817938804626 | 0.0 | 0.0 | +fb7a5348-949c-42cf-9326-c4676d6b6960 / -— |
| Jogador 7 | 6-5 | 372 | EQUIP_FROM_INVENTORY | ALL_IN | 6.0 | 8 | 97 | 5 | 46.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14054135978221893 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 373 | EQUIP_FROM_INVENTORY | ALL_IN | 6.0 | 8 | 97 | 5 | 46.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09547936171293259 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 374 | EQUIP_FROM_INVENTORY | ALL_IN | 6.0 | 8 | 97 | 5 | 46.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12010066211223602 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 375 | REROLL | ALL_IN | 6.0 | 8 | 97 | 5 | 46.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 376 | REROLL | ALL_IN | 6.0 | 8 | 95 | 5 | 46.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 377 | SELL | ALL_IN | 6.0 | 8 | 93 | 5 | 46.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5996000170707703 | 0.0 | 0.0 | +— / -42a24672-dcd0-4f0c-839a-82327962d77e |
| Jogador 7 | 6-5 | 378 | BUY | ALL_IN | 6.0 | 8 | 101 | 5 | 46.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5097769498825073 | 0.0 | 0.0 | +c7e728cc-abbd-488d-b3bb-3368e9259d0b / -— |
| Jogador 7 | 6-5 | 379 | REROLL | ALL_IN | 6.0 | 8 | 99 | 5 | 46.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 380 | SELL | ALL_IN | 6.0 | 8 | 97 | 5 | 46.0 | Inferno/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4572888910770416 | 0.0 | 0.0 | +— / -d140c71c-0721-4d2e-97c7-3efd32bd59db |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5923603177070618 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01241401955485344 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15737822651863098 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29129207134246826 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 32 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2845601439476013 | 0.0 | 0.0 | +74c2d7f0-8d5d-460e-88fc-5407b717144a / -— |
| Jogador 8 | 1-3 | 33 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008642825298011303 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002817703876644373 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38599154353141785 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23529231548309326 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19578605890274048 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005615613888949156 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 40 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9973782896995544 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 44 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.116762399673462 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -4ea4d9af-5729-414b-a102-b7fc80667118,74c2d7f0-8d5d-460e-88fc-5407b717144a |
| Jogador 8 | 1-4 | 45 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8977746367454529 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -— |
| Jogador 8 | 1-4 | 46 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05960175395011902 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 48 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.39674943685531616 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -— |
| Jogador 8 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0090450048446655 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -64f24363-3325-4538-972e-a6d8260b3787,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 2-1 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 4.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09098771214485168 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16432160139083862 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 58 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17862661182880402 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09185907244682312 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1381426751613617 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2898940443992615 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 63 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22260397672653198 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 64 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5520585775375366 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 65 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03780275955796242 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 66 | PASS | STABILIZE | 95.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.961363673210144 | 0.0 | 0.0 | +01f4a73c-7202-4ee3-964e-d32370c3c547 / -— |
| Jogador 8 | 2-3 | 73 | BUY | STABILIZE | 90.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9496535062789917 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -01f4a73c-7202-4ee3-964e-d32370c3c547,64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7469103336334229 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 75 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4035838842391968 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3663800358772278 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 77 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10110309720039368 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 78 | SELL | STABILIZE | 90.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -322e9047-623a-4fec-a0f9-d21d2fbcd88a |
| Jogador 8 | 2-3 | 79 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2793120741844177 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 80 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2836993336677551 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 82 | BUY | LOSS_STREAK | 83.0 | 4 | 15 | 1 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20603841543197632 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 83 | BUY | LOSS_STREAK | 83.0 | 4 | 13 | 1 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11746236681938171 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 84 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 10 | 1 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012923413887619972 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 85 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0182452201843262 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 86 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.034638822078704834 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 87 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 10 | 1 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018986035138368607 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 88 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6973024010658264 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 89 | PASS | LOSS_STREAK | 83.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 92 | BUY | LOSS_STREAK | 83.0 | 4 | 17 | 1 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6572617292404175 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 93 | BUY | LOSS_STREAK | 83.0 | 4 | 15 | 1 | 10.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23209550976753235 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-5 | 94 | MOVE_BENCH | STABILIZE | 83.0 | 4 | 13 | 1 | 10.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37398913502693176 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 95 | BUY | STABILIZE | 83.0 | 4 | 13 | 1 | 12.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11055422574281693 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 96 | MOVE_BENCH | STABILIZE | 83.0 | 4 | 12 | 1 | 12.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34266188740730286 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 97 | BUY_XP | STABILIZE | 83.0 | 4 | 12 | 1 | 14.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05587000027298927 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 98 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 8 | 0 | 14.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41593652963638306 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 99 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 100 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028039151802659035 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 102 | BUY | STABILIZE | 78.0 | 5 | 14 | 1 | 18.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9000272750854492 | 0.0 | 0.0 | +c737e99a-613e-4f1a-a50e-7a865169f90c / -— |
| Jogador 8 | 2-6 | 103 | SELL | STABILIZE | 78.0 | 5 | 13 | 1 | 18.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-6 | 104 | BUY | STABILIZE | 78.0 | 5 | 16 | 1 | 18.0 | Colosso/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13865892589092255 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 78.0 | 5 | 13 | 1 | 18.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011235710233449936 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 106 | BUY_XP | STABILIZE | 78.0 | 5 | 13 | 1 | 18.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 107 | BUY_XP | STABILIZE | 78.0 | 5 | 9 | 0 | 18.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 108 | BUY_XP | STABILIZE | 78.0 | 5 | 5 | 0 | 18.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 109 | MOVE_BOARD | STABILIZE | 78.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 78.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 112 | SELL | STABILIZE | 72.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -630d9254-3856-4d88-b981-43a8270b4b3d |
| Jogador 8 | 2-7 | 113 | BUY | STABILIZE | 72.0 | 5 | 11 | 1 | 18.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8944268226623535 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 114 | SELL | STABILIZE | 72.0 | 5 | 10 | 1 | 18.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0027000000700354576 | 0.0 | 0.0 | +— / -b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 2-7 | 115 | BUY | STABILIZE | 72.0 | 5 | 11 | 1 | 18.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06349088251590729 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 116 | SELL | STABILIZE | 72.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4495813250541687 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 2-7 | 117 | BUY_XP | STABILIZE | 72.0 | 5 | 10 | 1 | 18.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07040499895811081 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 118 | BUY_XP | STABILIZE | 72.0 | 6 | 6 | 0 | 18.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 119 | SELL | STABILIZE | 72.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5645192861557007 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-7 | 120 | BUY | STABILIZE | 72.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28419727087020874 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 3-1 | 122 | BUY | STABILIZE | 72.0 | 6 | 7 | 0 | 18.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.22192668914794922 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 72.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_18_Lillia | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21777379512786865 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 124 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_18_Lillia | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4562838673591614 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3485056459903717 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 126 | MOVE_BOARD | FAST8 | 72.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997540041804314 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 127 | PASS | FAST8 | 72.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 132 | BUY | FAST8 | 61.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6465262174606323 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 133 | MOVE_BOARD | FAST8 | 61.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 134 | MOVE_BOARD | FAST8 | 61.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06978186219930649 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 135 | PASS | FAST8 | 61.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 142 | SELL | FAST8 | 50.0 | 6 | 19 | 1 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4093691110610962 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-3 | 143 | BUY | FAST8 | 50.0 | 6 | 20 | 2 | 26.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6368858814239502 | 0.0 | 0.0 | +8df39648-f588-452a-b234-32da76c43aff / -— |
| Jogador 8 | 3-3 | 144 | SELL | FAST8 | 50.0 | 6 | 19 | 1 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05521087348461151 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 3-3 | 145 | BUY | FAST8 | 50.0 | 6 | 20 | 2 | 26.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30021268129348755 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 146 | MOVE_BOARD | FAST8 | 50.0 | 6 | 17 | 1 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05477243289351463 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 147 | BUY_XP | FAST8 | 50.0 | 6 | 17 | 1 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 148 | BUY_XP | FAST8 | 50.0 | 6 | 13 | 1 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 149 | BUY_XP | FAST8 | 50.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 150 | BUY_XP | FAST8 | 50.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 152 | SELL | FAST8 | 39.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33950477838516235 | 0.0 | 0.0 | +— / -e4605ac7-0b51-4f1c-a658-f7d25f9a9dae |
| Jogador 8 | 3-4 | 153 | BUY | FAST8 | 39.0 | 6 | 12 | 1 | 26.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7331274151802063 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 154 | SELL | FAST8 | 39.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5294222235679626 | 0.0 | 0.0 | +— / -c0d8da9e-5ede-4a26-8c5c-e2a908318bfd |
| Jogador 8 | 3-4 | 155 | BUY | FAST8 | 39.0 | 6 | 12 | 1 | 26.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7647899985313416 | 0.0 | 0.0 | +41782483-877e-4dce-bef9-4f1f3d5757bd / -5f2c89f5-15c2-4a77-943e-4ba5492d925b,d5848998-33f3-4632-94c0-60388a7cc6b8 |
| Jogador 8 | 3-4 | 156 | BUY_XP | FAST8 | 39.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 157 | BUY_XP | FAST8 | 39.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0839499980211258 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 158 | MOVE_BENCH | FAST8 | 39.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5993390083312988 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 159 | MOVE_BOARD | FAST8 | 39.0 | 7 | 2 | 0 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01502542570233345 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 160 | MOVE_BOARD | FAST8 | 39.0 | 7 | 2 | 0 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014991706237196922 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 162 | BUY | FAST8 | 39.0 | 7 | 10 | 1 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6532063484191895 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 8 | 3-5 | 163 | MOVE_BOARD | FAST8 | 39.0 | 7 | 7 | 0 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 164 | MOVE_BOARD | FAST8 | 39.0 | 7 | 7 | 0 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015013639815151691 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 165 | PASS | FAST8 | 39.0 | 7 | 7 | 0 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 172 | BUY | STABILIZE | 28.0 | 7 | 15 | 1 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28041917085647583 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 173 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 12 | 1 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.262262129690498e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 174 | BUY | STABILIZE | 28.0 | 7 | 12 | 1 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08903630822896957 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 175 | BUY_XP | STABILIZE | 28.0 | 7 | 8 | 0 | 28.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 176 | BUY_XP | STABILIZE | 28.0 | 7 | 4 | 0 | 28.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015001860447227955 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 179 | PASS | STABILIZE | 28.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 182 | SELL | ALL_IN | 17.0 | 7 | 8 | 0 | 28.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -41782483-877e-4dce-bef9-4f1f3d5757bd |
| Jogador 8 | 3-7 | 183 | BUY | ALL_IN | 17.0 | 7 | 13 | 1 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25123828649520874 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 184 | SELL | ALL_IN | 17.0 | 7 | 10 | 1 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.060233332216739655 | 0.0 | 0.0 | +— / -849ea0fc-7f61-4907-8abb-b25c8cc82efc |
| Jogador 8 | 3-7 | 185 | BUY | ALL_IN | 17.0 | 7 | 13 | 1 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15552444756031036 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 8 | 3-7 | 186 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 12 | 1 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.467130013263159e-08 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 187 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 12 | 1 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01561814546585083 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 188 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 12 | 1 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032639194279909134 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 189 | PASS | ALL_IN | 17.0 | 7 | 12 | 1 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3199999928474426 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 192 | CRAFT_AND_EQUIP | ALL_IN | 17.0 | 7 | 21 | 2 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19712504744529724 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 193 | CRAFT_AND_EQUIP | ALL_IN | 17.0 | 7 | 21 | 2 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22020213305950165 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 194 | SELL | ALL_IN | 17.0 | 7 | 21 | 2 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038233332335948944 | 0.0 | 0.0 | +— / -a14e4b8f-77c5-4909-a9ee-0044b836a877 |
| Jogador 8 | 4-1 | 195 | BUY | ALL_IN | 17.0 | 7 | 22 | 2 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8247836828231812 | 0.0 | 0.0 | +0534477f-2ff8-47a7-b71b-1a1d5430589e / -— |
| Jogador 8 | 4-1 | 196 | SELL | ALL_IN | 17.0 | 7 | 19 | 1 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038137421011924744 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 4-1 | 197 | BUY | ALL_IN | 17.0 | 7 | 22 | 2 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28777676820755005 | 0.0 | 0.0 | +974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 / -— |
| Jogador 8 | 4-1 | 198 | REROLL | ALL_IN | 17.0 | 7 | 19 | 1 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 199 | SELL | ALL_IN | 17.0 | 7 | 17 | 1 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32384443283081055 | 0.0 | 0.0 | +— / -974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 |
| Jogador 8 | 4-1 | 200 | BUY | ALL_IN | 17.0 | 7 | 20 | 2 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2129649817943573 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 8 | 4-2 | 202 | SELL | ALL_IN | 17.0 | 7 | 24 | 2 | 28.0 | Colosso/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0439809113740921 | 0.0 | 0.0 | +— / -86530a1f-5325-45fa-bf43-86419ccfda54 |
| Jogador 8 | 4-2 | 203 | BUY | ALL_IN | 17.0 | 7 | 27 | 2 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9090933799743652 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -0534477f-2ff8-47a7-b71b-1a1d5430589e,6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 4-2 | 204 | REROLL | ALL_IN | 17.0 | 7 | 24 | 2 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 205 | BUY | ALL_IN | 17.0 | 7 | 22 | 2 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8261224031448364 | 0.0 | 0.0 | +17d5d3f2-999d-4788-852b-bda84adb4350 / -— |
| Jogador 8 | 4-2 | 206 | BUY | ALL_IN | 17.0 | 7 | 19 | 1 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8653971552848816 | 0.0 | 0.0 | +485dab1f-b3a1-4170-8ed6-c0035072ae9b / -8df39648-f588-452a-b234-32da76c43aff,f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 4-2 | 207 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 18 | 1 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019734393805265427 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 208 | BUY | ALL_IN | 17.0 | 7 | 18 | 1 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2561050057411194 | 0.0 | 0.0 | +c7841e00-91da-410b-b00f-62f4bf32f666 / -— |
| Jogador 8 | 4-2 | 209 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 16 | 1 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013020406477153301 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 210 | BUY | ALL_IN | 17.0 | 7 | 16 | 1 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25610047578811646 | 0.0 | 0.0 | +f5cca112-4fa0-4ee6-a863-20a5d49ab7ef / -— |
| Jogador 8 | 4-3 | 212 | SELL | ALL_IN | 17.0 | 7 | 22 | 2 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -485dab1f-b3a1-4170-8ed6-c0035072ae9b |
| Jogador 8 | 4-3 | 213 | BUY | ALL_IN | 17.0 | 7 | 25 | 2 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9107416272163391 | 0.0 | 0.0 | +bb51728e-fcc5-4950-ad03-c864c51c2371 / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,c737e99a-613e-4f1a-a50e-7a865169f90c |
| Jogador 8 | 4-3 | 214 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 24 | 2 | 24.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.14019624888896942 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 215 | BUY | ALL_IN | 17.0 | 7 | 24 | 2 | 28.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.6072588562965393 | 0.0 | 0.0 | +17170204-1921-4cf1-b92b-cc73bb0701ea / -— |
| Jogador 8 | 4-3 | 216 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 7 | 22 | 2 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07504991441965103 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 217 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 7 | 22 | 2 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05236385390162468 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 218 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 22 | 2 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07615914195775986 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 219 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 22 | 2 | 32.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009533688426017761 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 220 | PASS | ALL_IN | 17.0 | 7 | 22 | 2 | 32.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44991111755371094 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 222 | BUY | ALL_IN | 17.0 | 7 | 30 | 3 | 32.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.922722578048706 | 0.0 | 0.0 | +1ff42607-ccac-4d3f-8277-bccddf08862f / -17d5d3f2-999d-4788-852b-bda84adb4350,23366968-ed3f-43d0-9f24-bb7691bf5d45 |
| Jogador 8 | 4-4 | 223 | BUY | ALL_IN | 17.0 | 7 | 27 | 2 | 32.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34382766485214233 | 0.0 | 0.0 | +61362365-2cf7-40e4-95f9-98e28728fd39 / -— |
| Jogador 8 | 4-4 | 224 | BUY | ALL_IN | 17.0 | 7 | 25 | 2 | 32.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8637236952781677 | 0.0 | 0.0 | +9cc98c55-1b3a-4b31-ae06-f66098e86e8f / -— |
| Jogador 8 | 4-4 | 225 | REROLL | ALL_IN | 17.0 | 7 | 23 | 2 | 32.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 226 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 21 | 2 | 32.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40534907579421997 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 227 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 21 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27222129702568054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 228 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 21 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12559430301189423 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 229 | REROLL | ALL_IN | 17.0 | 7 | 21 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 230 | SELL | ALL_IN | 17.0 | 7 | 19 | 1 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -bb51728e-fcc5-4950-ad03-c864c51c2371 |
| Jogador 8 | 4-5 | 232 | BUY | ALL_IN | 17.0 | 7 | 30 | 3 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3469376564025879 | 0.0 | 0.0 | +673bda2e-1343-4894-8005-c3ee2c90f1b7 / -— |
| Jogador 8 | 4-5 | 233 | REROLL | ALL_IN | 17.0 | 7 | 27 | 2 | 40.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 234 | SELL | ALL_IN | 17.0 | 7 | 25 | 2 | 40.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 |
| Jogador 8 | 4-5 | 235 | BUY | ALL_IN | 17.0 | 7 | 33 | 3 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8623353838920593 | 0.0 | 0.0 | +84e865bc-366e-45cd-85e4-fa7314688368 / -— |
| Jogador 8 | 4-5 | 236 | SELL | ALL_IN | 17.0 | 7 | 30 | 3 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029200000688433647 | 0.0 | 0.0 | +— / -a23ee552-279e-4c6c-aa05-6197043e8f1d |
| Jogador 8 | 4-5 | 237 | BUY | ALL_IN | 17.0 | 7 | 34 | 3 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9432638883590698 | 0.0 | 0.0 | +0435182d-aea5-44fe-ba36-601627982b66 / -c7841e00-91da-410b-b00f-62f4bf32f666,f5cca112-4fa0-4ee6-a863-20a5d49ab7ef |
| Jogador 8 | 4-5 | 238 | BUY | ALL_IN | 17.0 | 7 | 32 | 3 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2727166414260864 | 0.0 | 0.0 | +b0c1aba5-b1bd-48df-abec-19efa8e49d6d / -— |
| Jogador 8 | 4-5 | 239 | BUY | ALL_IN | 17.0 | 7 | 29 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19592168927192688 | 0.0 | 0.0 | +4aa5d560-d9d3-45f9-802a-bdbe95788762 / -— |
| Jogador 8 | 4-5 | 240 | MOVE_BENCH | ALL_IN | 17.0 | 7 | 27 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008051274344325066 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 242 | SELL | ALL_IN | 3.0 | 7 | 34 | 3 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -0435182d-aea5-44fe-ba36-601627982b66 |
| Jogador 8 | 4-6 | 243 | BUY | ALL_IN | 3.0 | 7 | 39 | 3 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41202113032341003 | 0.0 | 0.0 | +bcd06176-e1d7-43fb-abd4-b6faea8c7927 / -— |
| Jogador 8 | 4-6 | 244 | SELL | ALL_IN | 3.0 | 7 | 36 | 3 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008933333680033684 | 0.0 | 0.0 | +— / -4aa5d560-d9d3-45f9-802a-bdbe95788762 |
| Jogador 8 | 4-6 | 245 | BUY | ALL_IN | 3.0 | 7 | 38 | 3 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2867109179496765 | 0.0 | 0.0 | +80130f72-2d7c-49db-8d6f-4c0a962260e8 / -— |
| Jogador 8 | 4-6 | 246 | REROLL | ALL_IN | 3.0 | 7 | 37 | 3 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 247 | SELL | ALL_IN | 3.0 | 7 | 35 | 3 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4428810775279999 | 0.0 | 0.0 | +— / -a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 8 | 4-6 | 248 | BUY | ALL_IN | 3.0 | 7 | 37 | 3 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.76190584897995 | 0.0 | 0.0 | +91966802-adc2-46d2-9e7e-194283bca85c / -— |
| Jogador 8 | 4-6 | 249 | SELL | ALL_IN | 3.0 | 7 | 35 | 3 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49666666984558105 | 0.0 | 0.0 | +— / -91966802-adc2-46d2-9e7e-194283bca85c |
| Jogador 8 | 4-6 | 250 | BUY | ALL_IN | 3.0 | 7 | 37 | 3 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42384225130081177 | 0.0 | 0.0 | +5416d773-cb2c-442a-8ee9-0d46d22c2087 / -— |
| Jogador 8 | 4-7 | 252 | SELL | ALL_IN | 3.0 | 7 | 45 | 4 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34112557768821716 | 0.0 | 0.0 | +— / -80130f72-2d7c-49db-8d6f-4c0a962260e8 |
| Jogador 8 | 4-7 | 253 | BUY | ALL_IN | 3.0 | 7 | 46 | 4 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7619354724884033 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -— |
| Jogador 8 | 4-7 | 254 | SELL | ALL_IN | 3.0 | 7 | 44 | 4 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49666666984558105 | 0.0 | 0.0 | +— / -217a3ebb-1953-4f1e-bfdd-a3c9438e791e |
| Jogador 8 | 4-7 | 255 | BUY | ALL_IN | 3.0 | 7 | 46 | 4 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5690377950668335 | 0.0 | 0.0 | +4432f76a-94cc-4a96-b72b-1cf35b310dca / -— |
| Jogador 8 | 4-7 | 256 | REROLL | ALL_IN | 3.0 | 7 | 44 | 4 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 257 | SELL | ALL_IN | 3.0 | 7 | 42 | 4 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44066667556762695 | 0.0 | 0.0 | +— / -4432f76a-94cc-4a96-b72b-1cf35b310dca |
| Jogador 8 | 4-7 | 258 | BUY | ALL_IN | 3.0 | 7 | 44 | 4 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5716104507446289 | 0.0 | 0.0 | +aee0c45d-0178-4238-987f-5ee83dae7bce / -— |
| Jogador 8 | 4-7 | 259 | SELL | ALL_IN | 3.0 | 7 | 42 | 4 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44066667556762695 | 0.0 | 0.0 | +— / -aee0c45d-0178-4238-987f-5ee83dae7bce |
| Jogador 8 | 4-7 | 260 | BUY | ALL_IN | 3.0 | 7 | 44 | 4 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5716057419776917 | 0.0 | 0.0 | +e9bb05f6-3838-423a-bfd2-3791379b479e / -— |
| Jogador 8 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 3.0 | 7 | 51 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.05801064521074295 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 3.0 | 7 | 51 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1814044564962387 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 264 | SELL | ALL_IN | 3.0 | 7 | 51 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44706666469573975 | 0.0 | 0.0 | +— / -e9bb05f6-3838-423a-bfd2-3791379b479e |
| Jogador 8 | 5-1 | 265 | BUY | ALL_IN | 3.0 | 7 | 53 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4214657247066498 | 0.0 | 0.0 | +a267d973-f857-4dda-89e1-209bff42ab6f / -— |
| Jogador 8 | 5-1 | 266 | SELL | ALL_IN | 3.0 | 7 | 50 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5935999751091003 | 0.0 | 0.0 | +— / -bcd06176-e1d7-43fb-abd4-b6faea8c7927 |
| Jogador 8 | 5-1 | 267 | BUY | ALL_IN | 3.0 | 7 | 53 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.940660834312439 | 0.0 | 0.0 | +76fcc4d0-4988-4e99-8ac0-c251f0b99dcd / -— |
| Jogador 8 | 5-1 | 268 | REROLL | ALL_IN | 3.0 | 7 | 50 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 269 | SELL | ALL_IN | 3.0 | 7 | 48 | 4 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5879999995231628 | 0.0 | 0.0 | +— / -5416d773-cb2c-442a-8ee9-0d46d22c2087 |
| Jogador 8 | 5-1 | 270 | BUY | ALL_IN | 3.0 | 7 | 49 | 4 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.966159999370575 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -— |
| Jogador 8 | 5-2 | 272 | SELL | ALL_IN | 3.0 | 7 | 59 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9824000000953674 | 0.0 | 0.0 | +— / -61362365-2cf7-40e4-95f9-98e28728fd39 |
| Jogador 8 | 5-2 | 273 | BUY | ALL_IN | 3.0 | 7 | 61 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5682351589202881 | 0.0 | 0.0 | +3c5f5211-f30d-44e7-ac68-0ce513a3d614 / -— |
| Jogador 8 | 5-2 | 274 | REROLL | ALL_IN | 3.0 | 7 | 59 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 275 | SELL | ALL_IN | 3.0 | 7 | 57 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.469733327627182 | 0.0 | 0.0 | +— / -3c5f5211-f30d-44e7-ac68-0ce513a3d614 |
| Jogador 8 | 5-2 | 276 | BUY | ALL_IN | 3.0 | 7 | 59 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5306882858276367 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -— |
| Jogador 8 | 5-2 | 277 | SELL | ALL_IN | 3.0 | 7 | 58 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5924000144004822 | 0.0 | 0.0 | +— / -9cc98c55-1b3a-4b31-ae06-f66098e86e8f |
| Jogador 8 | 5-2 | 278 | BUY | ALL_IN | 3.0 | 7 | 60 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6892208456993103 | 0.0 | 0.0 | +d4c27edc-9b7e-4a31-a967-3aa80766b470 / -— |
| Jogador 8 | 5-2 | 279 | SELL | ALL_IN | 3.0 | 7 | 57 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4791383147239685 | 0.0 | 0.0 | +— / -d4c27edc-9b7e-4a31-a967-3aa80766b470 |
| Jogador 8 | 5-2 | 280 | BUY | ALL_IN | 3.0 | 7 | 60 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6930291056632996 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 8 | 5-3 | 282 | SELL | ALL_IN | 3.0 | 7 | 69 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47998982667922974 | 0.0 | 0.0 | +— / -f078e755-d142-4dad-99d0-7e7599e3016d |
| Jogador 8 | 5-3 | 283 | BUY | ALL_IN | 3.0 | 7 | 72 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4989929497241974 | 0.0 | 0.0 | +194da7dc-39b4-40e3-869d-326ace65137b / -— |
| Jogador 8 | 5-3 | 284 | SELL | ALL_IN | 3.0 | 7 | 69 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5935999751091003 | 0.0 | 0.0 | +— / -194da7dc-39b4-40e3-869d-326ace65137b |
| Jogador 8 | 5-3 | 285 | BUY | ALL_IN | 3.0 | 7 | 72 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06912288069725037 | 0.0 | 0.0 | +c93990ff-0a6f-46bc-8fc1-12623d55abc1 / -— |
| Jogador 8 | 5-3 | 286 | REROLL | ALL_IN | 3.0 | 7 | 68 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 287 | SELL | ALL_IN | 3.0 | 7 | 66 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007333333138376474 | 0.0 | 0.0 | +— / -c93990ff-0a6f-46bc-8fc1-12623d55abc1 |
| Jogador 8 | 5-3 | 288 | BUY | ALL_IN | 3.0 | 7 | 70 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5705535411834717 | 0.0 | 0.0 | +8538e488-6f36-433a-b261-73626f24bb07 / -— |
| Jogador 8 | 5-3 | 289 | SELL | ALL_IN | 3.0 | 7 | 68 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.469733327627182 | 0.0 | 0.0 | +— / -8538e488-6f36-433a-b261-73626f24bb07 |
| Jogador 8 | 5-3 | 290 | BUY | ALL_IN | 3.0 | 7 | 70 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2669455409049988 | 0.0 | 0.0 | +f9820f05-e1b0-4953-a98d-3ae191b1249a / -— |
| Jogador 8 | 5-4 | 292 | SELL | ALL_IN | 3.0 | 7 | 79 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05510000139474869 | 0.0 | 0.0 | +— / -f9820f05-e1b0-4953-a98d-3ae191b1249a |
| Jogador 8 | 5-4 | 293 | BUY | ALL_IN | 3.0 | 7 | 82 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6899017095565796 | 0.0 | 0.0 | +c4ec99e0-d973-42e9-a20e-1a9e7f5bf89a / -— |
| Jogador 8 | 5-4 | 294 | SELL | ALL_IN | 3.0 | 7 | 79 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4766290485858917 | 0.0 | 0.0 | +— / -c4ec99e0-d973-42e9-a20e-1a9e7f5bf89a |
| Jogador 8 | 5-4 | 295 | BUY | ALL_IN | 3.0 | 7 | 82 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6899721026420593 | 0.0 | 0.0 | +8025eaf5-b02b-4f94-b381-b94321bca206 / -— |
| Jogador 8 | 5-4 | 296 | REROLL | ALL_IN | 3.0 | 7 | 79 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 297 | SELL | ALL_IN | 3.0 | 7 | 77 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47918280959129333 | 0.0 | 0.0 | +— / -8025eaf5-b02b-4f94-b381-b94321bca206 |
| Jogador 8 | 5-4 | 298 | BUY | ALL_IN | 3.0 | 7 | 80 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0980900526046753 | 0.0 | 0.0 | +5d95f8bc-0c01-4c67-8764-4410eb32ee93 / -673bda2e-1343-4894-8005-c3ee2c90f1b7,84e865bc-366e-45cd-85e4-fa7314688368 |
| Jogador 8 | 5-4 | 299 | BUY | ALL_IN | 3.0 | 7 | 77 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0979489088058472 | 0.0 | 0.0 | +e29db20a-6b71-4518-ac7d-1e5d9eb67582 / -57903c42-49ca-43e1-8f86-42429c189fb5,bd4236f8-c8ff-4536-934a-b12b71012724 |
| Jogador 8 | 5-4 | 300 | BUY | ALL_IN | 3.0 | 7 | 74 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015315602533519268 | 0.0 | 0.0 | +5e8a73b8-846a-49a9-be41-30c3baf2cb55 / -— |
| Jogador 8 | 5-5 | 302 | BUY | ALL_IN | 3.0 | 7 | 84 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5103557705879211 | 0.0 | 0.0 | +94e47e85-54f4-4546-af6a-3700e3c325a8 / -— |
| Jogador 8 | 5-5 | 303 | BUY | ALL_IN | 3.0 | 7 | 81 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5901282429695129 | 0.0 | 0.0 | +13169f05-0cd0-4012-89a6-7b47246b475e / -— |
| Jogador 8 | 5-5 | 304 | REROLL | ALL_IN | 3.0 | 7 | 79 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 305 | SELL | ALL_IN | 3.0 | 7 | 77 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5996000170707703 | 0.0 | 0.0 | +— / -e29db20a-6b71-4518-ac7d-1e5d9eb67582 |
| Jogador 8 | 5-5 | 306 | BUY | ALL_IN | 3.0 | 7 | 85 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5937520265579224 | 0.0 | 0.0 | +6875f839-cf68-443f-9776-887087b375d3 / -— |
| Jogador 8 | 5-5 | 307 | SELL | ALL_IN | 3.0 | 7 | 82 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5996000170707703 | 0.0 | 0.0 | +— / -5d95f8bc-0c01-4c67-8764-4410eb32ee93 |
| Jogador 8 | 5-5 | 308 | BUY | ALL_IN | 3.0 | 7 | 90 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44424521923065186 | 0.0 | 0.0 | +88eb7a9e-aada-4146-adaf-4d3e8a5bdd67 / -— |
| Jogador 8 | 5-5 | 309 | REROLL | ALL_IN | 3.0 | 7 | 88 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 310 | SELL | ALL_IN | 3.0 | 7 | 86 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45159998536109924 | 0.0 | 0.0 | +— / -6875f839-cf68-443f-9776-887087b375d3 |
| Jogador 8 | 5-6 | 312 | BUY | ALL_IN | 3.0 | 7 | 100 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0391781330108643 | 0.0 | 0.0 | +95113577-160e-425d-a355-0f82356246fc / -— |
| Jogador 8 | 5-6 | 313 | SELL | ALL_IN | 3.0 | 7 | 99 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47423607110977173 | 0.0 | 0.0 | +— / -13169f05-0cd0-4012-89a6-7b47246b475e |
| Jogador 8 | 5-6 | 314 | BUY | ALL_IN | 3.0 | 7 | 101 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46276935935020447 | 0.0 | 0.0 | +1b7347d3-3505-47d6-a324-bbf75b32db31 / -— |
| Jogador 8 | 5-6 | 315 | REROLL | ALL_IN | 3.0 | 7 | 98 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 316 | SELL | ALL_IN | 3.0 | 7 | 96 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3346414268016815 | 0.0 | 0.0 | +— / -5e8a73b8-846a-49a9-be41-30c3baf2cb55 |
| Jogador 8 | 5-6 | 317 | BUY | ALL_IN | 3.0 | 7 | 97 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0973246097564697 | 0.0 | 0.0 | +60290b49-92fb-48d4-a657-26afd1f3f662 / -2d5214b0-3e0c-4e71-8664-2459bf616650,95113577-160e-425d-a355-0f82356246fc |
| Jogador 8 | 5-6 | 318 | BUY | ALL_IN | 3.0 | 7 | 96 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46512219309806824 | 0.0 | 0.0 | +23191bf1-a03a-47ab-aa04-1a5b6d86b445 / -— |
| Jogador 8 | 5-6 | 319 | BUY | ALL_IN | 3.0 | 7 | 92 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2735762894153595 | 0.0 | 0.0 | +f1c48e72-ce66-4b0d-ab88-5d965e06066b / -— |
| Jogador 8 | 5-6 | 320 | REROLL | ALL_IN | 3.0 | 7 | 89 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 322 | SELL | ALL_IN | 3.0 | 7 | 100 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5935999751091003 | 0.0 | 0.0 | +— / -60290b49-92fb-48d4-a657-26afd1f3f662 |
| Jogador 8 | 5-7 | 323 | BUY | ALL_IN | 3.0 | 7 | 103 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44971567392349243 | 0.0 | 0.0 | +472b4728-efd0-4853-a186-37811f40157a / -— |
| Jogador 8 | 5-7 | 324 | SELL | ALL_IN | 3.0 | 7 | 101 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05510000139474869 | 0.0 | 0.0 | +— / -f1c48e72-ce66-4b0d-ab88-5d965e06066b |
| Jogador 8 | 5-7 | 325 | BUY | ALL_IN | 3.0 | 7 | 104 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2668740749359131 | 0.0 | 0.0 | +6d150146-2d96-4b53-a24b-05a486a348cf / -— |
| Jogador 8 | 5-7 | 326 | SELL | ALL_IN | 3.0 | 7 | 101 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05510000139474869 | 0.0 | 0.0 | +— / -6d150146-2d96-4b53-a24b-05a486a348cf |
| Jogador 8 | 5-7 | 327 | BUY | ALL_IN | 3.0 | 7 | 104 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28510475158691406 | 0.0 | 0.0 | +af23c553-04de-4813-87d0-bb7e4becafe4 / -— |
| Jogador 8 | 5-7 | 328 | REROLL | ALL_IN | 3.0 | 7 | 103 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 329 | SELL | ALL_IN | 3.0 | 7 | 101 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07783333212137222 | 0.0 | 0.0 | +— / -af23c553-04de-4813-87d0-bb7e4becafe4 |
| Jogador 8 | 5-7 | 330 | BUY | ALL_IN | 3.0 | 7 | 102 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9827554225921631 | 0.0 | 0.0 | +e22ad17a-827b-42f7-95a6-9e334471b0b9 / -— |
| Jogador 8 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ALL_IN | 3.0 | 7 | 111 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0013109628343954682 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 333 | SELL | ALL_IN | 3.0 | 7 | 111 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5935999751091003 | 0.0 | 0.0 | +— / -94e47e85-54f4-4546-af6a-3700e3c325a8 |
| Jogador 8 | 6-1 | 334 | BUY | ALL_IN | 3.0 | 7 | 114 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9770238399505615 | 0.0 | 0.0 | +99c9fbf5-b28f-4743-b04a-5299e9e116e5 / -— |
| Jogador 8 | 6-1 | 335 | SELL | ALL_IN | 3.0 | 7 | 112 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5924000144004822 | 0.0 | 0.0 | +— / -88eb7a9e-aada-4146-adaf-4d3e8a5bdd67 |
| Jogador 8 | 6-1 | 336 | BUY | ALL_IN | 3.0 | 7 | 114 | 5 | 42.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1103684902191162 | 0.0 | 0.0 | +7be7d9db-fa8f-421e-93d5-5910cc3e1bf2 / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc,f6000a82-1241-4220-9362-c8d788472db0 |
| Jogador 8 | 6-1 | 337 | BUY | ALL_IN | 3.0 | 7 | 113 | 5 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1097368001937866 | 0.0 | 0.0 | +517873a4-be8f-4704-bf0b-23a4dc39806c / -472b4728-efd0-4853-a186-37811f40157a,99c9fbf5-b28f-4743-b04a-5299e9e116e5 |
| Jogador 8 | 6-1 | 338 | MOVE_BENCH | ALL_IN | 3.0 | 7 | 111 | 5 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5996988415718079 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 339 | MOVE_BOARD | ALL_IN | 3.0 | 7 | 111 | 5 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01811106503009796 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 340 | REROLL | ALL_IN | 3.0 | 7 | 111 | 5 | 48.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759999692440033 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 218 | 195 | 80 | 6 | 14 | 0 | 5 | 0 | 97 | 34.0 |
- Jogador 1 — gasto por ação: BUY: 125g, BUY_XP: 60g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 10g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 5g, stage 2: 43g, stage 3: 59g, stage 4: 13g, stage 5: 75g
| Jogador 2 | 210 | 196 | 48 | 9 | 19 | 0 | 9 | 0 | 75 | 32.0 |
- Jogador 2 — gasto por ação: BUY: 94g, BUY_XP: 84g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 18g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 6g, stage 2: 46g, stage 3: 56g, stage 4: 38g, stage 5: 24g, stage 6: 26g
| Jogador 3 | 138 | 68 | 21 | 1 | 0 | 0 | 5 | 0 | 90 | 22.0 |
- Jogador 3 — gasto por ação: BUY: 58g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 10g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 33g, stage 3: 14g, stage 4: 14g
| Jogador 4 | 193 | 190 | 59 | 15 | 17 | 0 | 0 | 0 | 35 | 46.0 |
- Jogador 4 — gasto por ação: BUY: 110g, BUY_XP: 80g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 8g, stage 2: 59g, stage 3: 45g, stage 4: 53g, stage 5: 25g
| Jogador 5 | 272 | 287 | 149 | 6 | 11 | 0 | 25 | 0 | 171 | 44.0 |
- Jogador 5 — gasto por ação: BUY: 201g, BUY_XP: 56g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 30g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 53g, stage 3: 37g, stage 4: 31g, stage 5: 89g, stage 6: 70g
| Jogador 6 | 198 | 138 | 53 | 4 | 4 | 0 | 7 | 0 | 97 | 46.0 |
- Jogador 6 — gasto por ação: BUY: 104g, BUY_XP: 20g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 14g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 8g, stage 2: 46g, stage 3: 26g, stage 4: 35g, stage 5: 23g
| Jogador 7 | 255 | 231 | 74 | 8 | 19 | 0 | 7 | 0 | 108 | 46.0 |
- Jogador 7 — gasto por ação: BUY: 133g, BUY_XP: 84g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 14g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 8g, stage 2: 50g, stage 3: 47g, stage 4: 58g, stage 5: 23g, stage 6: 45g
| Jogador 8 | 261 | 289 | 147 | 19 | 11 | 1 | 17 | 0 | 109 | 48.0 |
- Jogador 8 — gasto por ação: BUY: 199g, BUY_XP: 56g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 34g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 54g, stage 3: 59g, stage 4: 72g, stage 5: 90g, stage 6: 7g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 15 | 14 |
- Jogador 1 · 2-7 · step 117: PASS com 7g, HP 95, nível 5/8 (STABILIZE).
- Jogador 1 · 3-1 · step 127: PASS com 10g, HP 95, nível 6/8 (STABILIZE).
- Jogador 1 · 4-2 · step 206: PASS com 23g, HP 64, nível 7/8 (STABILIZE).
- Jogador 1 · 4-3 · step 217: PASS com 30g, HP 51, nível 7/8 (STABILIZE).
- Jogador 1 · 4-4 · step 228: PASS com 34g, HP 39, nível 7/8 (FAST8).
- Jogador 1 · 4-5 · step 235: PASS com 39g, HP 39, nível 7/8 (FAST8).
- Jogador 1 · 4-6 · step 245: PASS com 48g, HP 39, nível 7/8 (FAST8).
- Jogador 1 · 4-7 · step 257: PASS com 60g, HP 39, nível 7/8 (FAST8).
- Jogador 1 · 5-1 · step 269: PASS com 69g, HP 39, nível 7/8 (FAST8).
- Jogador 1 · 5-3 · step 287: REROLL com 84g, HP 21, nível 7/8 (ALL_IN).
- Jogador 1 · 5-4 · step 297: REROLL com 93g, HP 5, nível 7/8 (ALL_IN).
- Jogador 1 · 5-5 · step 307: REROLL com 94g, HP 5, nível 7/8 (ALL_IN).
- Jogador 1 · 5-6 · step 317: REROLL com 96g, HP 5, nível 7/8 (ALL_IN).
- Jogador 1 · 5-6 · step 320: REROLL com 99g, HP 5, nível 7/8 (ALL_IN).
| Jogador 2 | 21 | 7 |
- Jogador 2 · 2-5 · step 95: PASS com 6g, HP 84, nível 5/8 (STABILIZE).
- Jogador 2 · 3-1 · step 126: PASS com 8g, HP 78, nível 6/8 (FAST8).
- Jogador 2 · 3-6 · step 176: PASS com 9g, HP 78, nível 7/8 (FAST8).
- Jogador 2 · 4-1 · step 198: PASS com 5g, HP 66, nível 7/8 (FAST8).
- Jogador 2 · 4-2 · step 204: PASS com 11g, HP 66, nível 7/8 (FAST8).
- Jogador 2 · 4-3 · step 216: PASS com 14g, HP 53, nível 7/8 (FAST8).
- Jogador 2 · 4-4 · step 225: PASS com 18g, HP 40, nível 7/8 (FAST8).
| Jogador 3 | 0 | 12 |
- Jogador 3 · 2-6 · step 109: PASS com 10g, HP 82, nível 5/8 (STABILIZE).
- Jogador 3 · 2-7 · step 117: PASS com 12g, HP 75, nível 5/8 (STABILIZE).
- Jogador 3 · 3-1 · step 125: PASS com 18g, HP 75, nível 5/8 (STABILIZE).
- Jogador 3 · 3-2 · step 135: PASS com 25g, HP 65, nível 5/8 (STABILIZE).
- Jogador 3 · 3-3 · step 149: PASS com 33g, HP 54, nível 5/8 (STABILIZE).
- Jogador 3 · 3-6 · step 180: PASS com 70g, HP 32, nível 5/8 (STABILIZE).
- Jogador 3 · 3-7 · step 185: REROLL com 81g, HP 21, nível 5/8 (ALL_IN).
- Jogador 3 · 3-7 · step 186: REROLL com 79g, HP 21, nível 5/8 (ALL_IN).
- Jogador 3 · 3-7 · step 189: REROLL com 76g, HP 21, nível 5/8 (ALL_IN).
- Jogador 3 · 4-1 · step 197: REROLL com 89g, HP 21, nível 5/8 (ALL_IN).
- Jogador 3 · 4-1 · step 200: PASS com 87g, HP 21, nível 5/8 (ALL_IN).
- Jogador 3 · 4-2 · step 206: REROLL com 96g, HP 9, nível 6/8 (ALL_IN).
| Jogador 4 | 20 | 11 |
- Jogador 4 · 3-2 · step 138: PASS com 6g, HP 89, nível 6/8 (FAST8).
- Jogador 4 · 3-3 · step 146: PASS com 8g, HP 78, nível 6/8 (FAST8).
- Jogador 4 · 3-4 · step 158: PASS com 8g, HP 68, nível 6/8 (FAST8).
- Jogador 4 · 3-6 · step 178: PASS com 8g, HP 68, nível 6/8 (FAST8).
- Jogador 4 · 3-7 · step 188: PASS com 13g, HP 68, nível 6/8 (FAST8).
- Jogador 4 · 4-1 · step 197: PASS com 17g, HP 68, nível 6/8 (FAST8).
- Jogador 4 · 4-2 · step 206: PASS com 21g, HP 56, nível 7/8 (FAST8).
- Jogador 4 · 4-3 · step 216: PASS com 29g, HP 56, nível 7/8 (FAST8).
- Jogador 4 · 4-4 · step 226: PASS com 40g, HP 56, nível 7/8 (FAST8).
- Jogador 4 · 4-5 · step 239: PASS com 35g, HP 56, nível 7/8 (FAST8).
- Jogador 4 · 4-6 · step 248: PASS com 44g, HP 44, nível 7/8 (FAST8).
| Jogador 5 | 14 | 36 |
- Jogador 5 · 3-3 · step 150: PASS com 11g, HP 94, nível 6/8 (STABILIZE).
- Jogador 5 · 3-4 · step 160: PASS com 17g, HP 94, nível 6/8 (STABILIZE).
- Jogador 5 · 3-5 · step 168: PASS com 24g, HP 94, nível 6/8 (STABILIZE).
- Jogador 5 · 3-6 · step 176: PASS com 34g, HP 94, nível 6/8 (STABILIZE).
- Jogador 5 · 3-7 · step 189: PASS com 37g, HP 94, nível 6/8 (STABILIZE).
- Jogador 5 · 4-1 · step 197: REROLL com 48g, HP 94, nível 6/8 (STABILIZE).
- Jogador 5 · 4-3 · step 215: PASS com 61g, HP 81, nível 7/8 (FAST8).
- Jogador 5 · 4-4 · step 226: PASS com 70g, HP 81, nível 7/8 (FAST8).
- Jogador 5 · 4-5 · step 234: PASS com 81g, HP 81, nível 7/8 (FAST8).
- Jogador 5 · 4-6 · step 246: PASS com 94g, HP 81, nível 7/8 (FAST8).
- Jogador 5 · 4-7 · step 256: REROLL com 101g, HP 68, nível 7/8 (FAST8).
- Jogador 5 · 4-7 · step 257: REROLL com 101g, HP 68, nível 7/8 (FAST8).
- Jogador 5 · 4-7 · step 260: PASS com 101g, HP 68, nível 7/8 (FAST8).
- Jogador 5 · 5-1 · step 270: PASS com 105g, HP 68, nível 7/8 (FAST8).
- Jogador 5 · 5-2 · step 276: REROLL com 115g, HP 68, nível 7/8 (FAST8).
- Jogador 5 · 5-2 · step 277: REROLL com 115g, HP 68, nível 7/8 (FAST8).
- Jogador 5 · 5-2 · step 278: REROLL com 115g, HP 68, nível 7/8 (FAST8).
- Jogador 5 · 5-2 · step 279: REROLL com 115g, HP 68, nível 7/8 (FAST8).
- Jogador 5 · 5-2 · step 280: REROLL com 115g, HP 68, nível 7/8 (FAST8).
- Jogador 5 · 5-3 · step 288: REROLL com 120g, HP 52, nível 7/8 (FAST8).
- Jogador 5 · 5-3 · step 289: REROLL com 120g, HP 52, nível 7/8 (FAST8).
- Jogador 5 · 5-3 · step 290: REROLL com 120g, HP 52, nível 7/8 (FAST8).
- Jogador 5 · 5-5 · step 308: REROLL com 127g, HP 37, nível 7/8 (STABILIZE).
- Jogador 5 · 5-6 · step 317: REROLL com 131g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 5-7 · step 326: REROLL com 133g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 6-1 · step 337: REROLL com 150g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 6-2 · step 343: REROLL com 159g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 6-2 · step 346: REROLL com 154g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 6-3 · step 354: REROLL com 162g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 6-3 · step 357: REROLL com 160g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 6-3 · step 360: REROLL com 159g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 6-4 · step 362: REROLL com 169g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 6-4 · step 365: REROLL com 167g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 6-4 · step 370: REROLL com 165g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 6-5 · step 377: REROLL com 175g, HP 23, nível 7/8 (ALL_IN).
- Jogador 5 · 6-5 · step 379: REROLL com 170g, HP 23, nível 7/8 (ALL_IN).
| Jogador 6 | 5 | 18 |
- Jogador 6 · 3-2 · step 139: PASS com 6g, HP 80, nível 6/8 (STABILIZE).
- Jogador 6 · 3-3 · step 147: PASS com 8g, HP 70, nível 6/8 (STABILIZE).
- Jogador 6 · 3-4 · step 160: PASS com 6g, HP 70, nível 6/8 (FAST8).
- Jogador 6 · 3-5 · step 166: PASS com 7g, HP 70, nível 6/8 (FAST8).
- Jogador 6 · 3-6 · step 178: PASS com 12g, HP 60, nível 6/8 (FAST8).
- Jogador 6 · 3-7 · step 184: PASS com 19g, HP 60, nível 6/8 (FAST8).
- Jogador 6 · 4-1 · step 200: PASS com 29g, HP 60, nível 6/8 (FAST8).
- Jogador 6 · 4-2 · step 206: PASS com 35g, HP 48, nível 6/8 (FAST8).
- Jogador 6 · 4-4 · step 227: PASS com 51g, HP 20, nível 6/8 (ALL_IN).
- Jogador 6 · 4-5 · step 238: PASS com 63g, HP 20, nível 6/8 (ALL_IN).
- Jogador 6 · 4-6 · step 244: REROLL com 76g, HP 20, nível 6/8 (ALL_IN).
- Jogador 6 · 4-6 · step 247: REROLL com 75g, HP 20, nível 6/8 (ALL_IN).
- Jogador 6 · 4-6 · step 248: REROLL com 73g, HP 20, nível 6/8 (ALL_IN).
- Jogador 6 · 4-7 · step 255: REROLL com 77g, HP 20, nível 6/8 (ALL_IN).
- Jogador 6 · 4-7 · step 256: REROLL com 75g, HP 20, nível 6/8 (ALL_IN).
- Jogador 6 · 4-7 · step 260: REROLL com 77g, HP 20, nível 6/8 (ALL_IN).
- Jogador 6 · 5-2 · step 278: REROLL com 95g, HP 6, nível 6/8 (ALL_IN).
- Jogador 6 · 5-3 · step 290: PASS com 97g, HP 6, nível 7/8 (ALL_IN).
| Jogador 7 | 21 | 3 |
- Jogador 7 · 3-5 · step 165: PASS com 8g, HP 85, nível 6/8 (FAST8).
- Jogador 7 · 4-5 · step 235: PASS com 8g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 4-6 · step 247: PASS com 22g, HP 85, nível 7/8 (FAST8).
| Jogador 8 | 14 | 21 |
- Jogador 8 · 3-2 · step 135: PASS com 10g, HP 61, nível 6/8 (FAST8).
- Jogador 8 · 3-5 · step 165: PASS com 7g, HP 39, nível 7/8 (FAST8).
- Jogador 8 · 3-7 · step 189: PASS com 12g, HP 17, nível 7/8 (ALL_IN).
- Jogador 8 · 4-1 · step 198: REROLL com 19g, HP 17, nível 7/8 (ALL_IN).
- Jogador 8 · 4-2 · step 204: REROLL com 24g, HP 17, nível 7/8 (ALL_IN).
- Jogador 8 · 4-3 · step 220: PASS com 22g, HP 17, nível 7/8 (ALL_IN).
- Jogador 8 · 4-4 · step 225: REROLL com 23g, HP 17, nível 7/8 (ALL_IN).
- Jogador 8 · 4-4 · step 229: REROLL com 21g, HP 17, nível 7/8 (ALL_IN).
- Jogador 8 · 4-5 · step 233: REROLL com 27g, HP 17, nível 7/8 (ALL_IN).
- Jogador 8 · 4-6 · step 246: REROLL com 37g, HP 3, nível 7/8 (ALL_IN).
- Jogador 8 · 4-7 · step 256: REROLL com 44g, HP 3, nível 7/8 (ALL_IN).
- Jogador 8 · 5-1 · step 268: REROLL com 50g, HP 3, nível 7/8 (ALL_IN).
- Jogador 8 · 5-2 · step 274: REROLL com 59g, HP 3, nível 7/8 (ALL_IN).
- Jogador 8 · 5-3 · step 286: REROLL com 68g, HP 3, nível 7/8 (ALL_IN).
- Jogador 8 · 5-4 · step 296: REROLL com 79g, HP 3, nível 7/8 (ALL_IN).
- Jogador 8 · 5-5 · step 304: REROLL com 79g, HP 3, nível 7/8 (ALL_IN).
- Jogador 8 · 5-5 · step 309: REROLL com 88g, HP 3, nível 7/8 (ALL_IN).
- Jogador 8 · 5-6 · step 315: REROLL com 98g, HP 3, nível 7/8 (ALL_IN).
- Jogador 8 · 5-6 · step 320: REROLL com 89g, HP 3, nível 7/8 (ALL_IN).
- Jogador 8 · 5-7 · step 328: REROLL com 103g, HP 3, nível 7/8 (ALL_IN).
- Jogador 8 · 6-1 · step 340: REROLL com 111g, HP 3, nível 7/8 (ALL_IN).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 218 | 54 | 44 | 120 | 0.0031 | 0.2168 | 0.0014 | 0.3169 | 0.0018 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0115 (58 ações), BUY_XP: Δ 0.0021 (15 ações), CRAFT_AND_EQUIP: Δ 0.0086 (7 ações), EQUIP_FROM_INVENTORY: Δ -0.0210 (7 ações), MOVE_BENCH: Δ 0.0457 (40 ações), MOVE_BOARD: Δ -0.0210 (39 ações), PASS: Δ -0.0110 (20 ações), REROLL: Δ 0.0000 (5 ações), SELL: Δ 0.0227 (27 ações)
| Jogador 2 | 210 | 47 | 39 | 124 | 0.0005 | 0.3089 | -0.0009 | 0.2884 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0429 (45 ações), BUY_XP: Δ 0.0020 (21 ações), CRAFT_AND_EQUIP: Δ 0.0046 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0613 (21 ações), MOVE_BOARD: Δ 0.0036 (62 ações), PASS: Δ 0.0000 (27 ações), REROLL: Δ 0.0000 (9 ações), SELL: Δ 0.0271 (17 ações)
| Jogador 3 | 138 | 42 | 49 | 47 | 0.0029 | 0.1384 | 0.0009 | 0.2182 | 0.0020 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0374 (33 ações), CRAFT_AND_EQUIP: Δ 0.0408 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0179 (57 ações), MOVE_BOARD: Δ 0.0032 (13 ações), PASS: Δ 0.0000 (14 ações), REROLL: Δ 0.0000 (5 ações), SELL: Δ 0.0414 (9 ações)
| Jogador 4 | 193 | 37 | 27 | 129 | 0.0022 | 0.3981 | 0.0008 | 0.3214 | 0.0014 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0195 (54 ações), BUY_XP: Δ 0.0060 (20 ações), CRAFT_AND_EQUIP: Δ 0.0043 (7 ações), MOVE_BENCH: Δ 0.0620 (22 ações), MOVE_BOARD: Δ -0.0076 (41 ações), PASS: Δ 0.0000 (19 ações), SELL: Δ 0.0090 (30 ações)
| Jogador 5 | 272 | 58 | 44 | 170 | 0.0038 | 0.6018 | 0.0023 | 0.3575 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0190 (89 ações), BUY_XP: Δ 0.0074 (14 ações), CRAFT_AND_EQUIP: Δ 0.0050 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0804 (12 ações), MOVE_BOARD: Δ 0.0203 (50 ações), PASS: Δ 0.0000 (21 ações), REROLL: Δ 0.0000 (25 ações), SELL: Δ 0.0116 (53 ações)
| Jogador 6 | 198 | 53 | 47 | 98 | 0.0032 | 0.2399 | 0.0002 | 0.3218 | 0.0030 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0353 (53 ações), BUY_XP: Δ 0.0095 (5 ações), CRAFT_AND_EQUIP: Δ 0.0007 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (4 ações), MOVE_BENCH: Δ 0.0358 (24 ações), MOVE_BOARD: Δ 0.0202 (58 ações), PASS: Δ 0.0001 (20 ações), REROLL: Δ 0.0000 (7 ações), SELL: Δ 0.0210 (20 ações)
| Jogador 7 | 255 | 61 | 52 | 142 | 0.0035 | 0.4514 | 0.0025 | 0.3353 | 0.0011 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0645 (58 ações), BUY_XP: Δ 0.0046 (21 ações), CRAFT_AND_EQUIP: Δ 0.0187 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (6 ações), MOVE_BENCH: Δ 0.0661 (38 ações), MOVE_BOARD: Δ 0.0200 (71 ações), PASS: Δ 0.0000 (27 ações), REROLL: Δ 0.0000 (7 ações), SELL: Δ 0.0241 (20 ações)
| Jogador 8 | 261 | 47 | 51 | 163 | 0.0018 | 0.2800 | 0.0001 | 0.2835 | 0.0017 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0228 (93 ações), BUY_XP: Δ 0.0094 (14 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0943 (26 ações), MOVE_BOARD: Δ -0.0386 (36 ações), PASS: Δ 0.0000 (12 ações), REROLL: Δ 0.0087 (17 ações), SELL: Δ 0.0235 (53 ações)
- Jogador 1 — rounds avaliados: 31; correlação estrutural/combate: 0.044; posicional/combate: -0.147.
- Jogador 1 — combate positive: score estrutural prévio 0.262
  score posicional prévio 0.309
- Jogador 1 — combate negative: score estrutural prévio 0.224
  score posicional prévio 0.349
- Jogador 2 — rounds avaliados: 34; correlação estrutural/combate: 0.179; posicional/combate: 0.143.
- Jogador 2 — combate positive: score estrutural prévio 0.544
  score posicional prévio 0.299
- Jogador 2 — combate negative: score estrutural prévio 0.386
  score posicional prévio 0.266
- Jogador 3 — rounds avaliados: 20; correlação estrutural/combate: 0.207; posicional/combate: 0.036.
- Jogador 3 — combate positive: score estrutural prévio 0.215
  score posicional prévio 0.274
- Jogador 3 — combate negative: score estrutural prévio 0.106
  score posicional prévio 0.215
- Jogador 4 — rounds avaliados: 27; correlação estrutural/combate: 0.159; posicional/combate: 0.210.
- Jogador 4 — combate positive: score estrutural prévio 0.516
  score posicional prévio 0.359
- Jogador 4 — combate negative: score estrutural prévio 0.389
  score posicional prévio 0.311
- Jogador 5 — rounds avaliados: 37; correlação estrutural/combate: 0.028; posicional/combate: -0.019.
- Jogador 5 — combate positive: score estrutural prévio 0.642
  score posicional prévio 0.363
- Jogador 5 — combate negative: score estrutural prévio 0.710
  score posicional prévio 0.384
- Jogador 6 — rounds avaliados: 28; correlação estrutural/combate: 0.099; posicional/combate: 0.159.
- Jogador 6 — combate positive: score estrutural prévio 0.362
  score posicional prévio 0.336
- Jogador 6 — combate negative: score estrutural prévio 0.233
  score posicional prévio 0.294
- Jogador 7 — rounds avaliados: 37; correlação estrutural/combate: -0.265; posicional/combate: -0.234.
- Jogador 7 — combate positive: score estrutural prévio 0.453
  score posicional prévio 0.326
- Jogador 7 — combate negative: score estrutural prévio 0.816
  score posicional prévio 0.402
- Jogador 8 — rounds avaliados: 33; correlação estrutural/combate: 0.141; posicional/combate: -0.308.
- Jogador 8 — combate positive: score estrutural prévio 0.520
  score posicional prévio 0.250
- Jogador 8 — combate negative: score estrutural prévio 0.266
  score posicional prévio 0.316

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 248 | OK (248) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Bloodthirster, TFT_Item_InfinityEdge, TFT_Item_Morellonomicon, TFT_Item_RabadonsDeathcap, TFT_Item_RapidFireCannon, TFT_Item_RedBuff; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 243 | OK (243) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_GargoyleStoneplate, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 157 | OK (157) | 5 | 0 | 0 | 1 | 5 | 2 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_InfinityEdge, TFT_Item_Redemption, TFT_Item_SteraksGage, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 219 | OK (219) | 7 | 0 | 0 | 0 | 7 | 0 |
- Jogador 4 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Bloodthirster, TFT_Item_BlueBuff, TFT_Item_JeweledGauntlet, TFT_Item_Leviathan, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 309 | OK (309) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 5 — IDs equipados observados: TFT_Item_GargoyleStoneplate, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_Leviathan, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 225 | OK (225) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 6 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_Crownguard, TFT_Item_HextechGunblade, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 291 | OK (291) | 5 | 3 | 0 | 0 | 8 | 3 |
- Jogador 7 — IDs equipados observados: TFT_Item_NightHarvester, TFT_Item_RabadonsDeathcap, TFT_Item_Redemption, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 293 | OK (293) | 5 | 3 | 0 | 0 | 8 | 2 |
- Jogador 8 — IDs equipados observados: DA_18_EmblemHunter, TFT_Item_AdaptiveHelm, TFT_Item_DragonsClaw, TFT_Item_HextechGunblade, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.147 | 0.000 |
| Jogador 1 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.001 | 0.000 |
| Jogador 1 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 1 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.016 | 0.000 |
| Jogador 1 | 2-1 | 8 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 6 → 7 | 5 | 4 → 4 | 0.024 | 0.314 |
| Jogador 1 | 2-2 | 8 | 6.000 | 0.000 | 0 → 0 | 2 → 2 | 14% → 18% | 7 → 7 | 7 | 4 → 5 | 0.013 | 0.308 |
| Jogador 1 | 2-3 | 8 | 2.000 | 4.000 | 0 → 0 | 2 → 2 | 18% → 18% | 7 → 7 | 7 | 5 → 5 | -0.004 | 0.323 |
| Jogador 1 | 2-4 | 8 | 0.000 | 10.000 | 0 → 0 | 2 → 1 | 18% → 18% | 7 → 7 | 6 | 5 → 5 | -0.065 | 0.000 |
| Jogador 1 | 2-5 | 10 | -2.000 | 8.000 | 0 → 0 | 1 → 2 | 18% → 18% | 7 → 8 | 9 | 5 → 5 | 0.033 | 0.251 |
| Jogador 1 | 2-6 | 7 | 4.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 18% | 8 → 7 | 6 | 5 → 5 | 0.001 | -0.339 |
| Jogador 1 | 2-7 | 7 | 0.000 | 2.000 | 0 → 0 | 2 → 2 | 18% → 18% | 7 → 12 | 3 | 5 → 6 | -0.119 | 0.000 |
| Jogador 1 | 3-1 | 7 | 4.000 | 0.000 | 0 → 0 | 2 → 3 | 18% → 21% | 12 → 17 | 2 | 6 → 6 | 0.073 | 0.395 |
| Jogador 1 | 3-2 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 4 | 21% → 21% | 17 → 9 | 17 | 6 → 6 | -0.001 | 0.295 |
| Jogador 1 | 3-3 | 10 | 0.000 | 2.000 | 0 → 0 | 4 → 4 | 21% → 21% | 9 → 5 | 13 | 6 → 6 | -0.045 | -0.263 |
| Jogador 1 | 3-4 | 10 | 0.000 | 2.000 | 0 → 0 | 4 → 4 | 21% → 21% | 5 → 5 | 8 | 6 → 7 | 0.049 | 0.000 |
| Jogador 1 | 3-5 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 3 | 21% → 25% | 5 → 6 | 7 | 7 → 7 | -0.003 | -0.273 |
| Jogador 1 | 3-6 | 8 | 0.000 | 12.000 | 0 → 0 | 3 → 3 | 25% → 25% | 6 → 6 | 6 | 7 → 7 | 0.062 | -0.335 |
| Jogador 1 | 3-7 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 3 | 25% → 25% | 6 → 14 | 6 | 7 → 7 | 0.006 | 0.000 |
| Jogador 1 | 4-1 | 10 | -2.000 | 2.000 | 0 → 0 | 3 → 3 | 25% → 25% | 14 → 21 | 0 | 7 → 7 | -0.001 | 0.293 |
| Jogador 1 | 4-2 | 6 | 2.000 | -6.000 | 0 → 0 | 3 → 4 | 25% → 25% | 21 → 30 | 1 | 7 → 7 | -0.006 | -0.475 |
| Jogador 1 | 4-3 | 7 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 30 → 39 | 1 | 7 → 7 | 0.054 | -0.395 |
| Jogador 1 | 4-4 | 8 | 6.000 | -2.000 | 0 → 1 | 4 → 3 | 25% → 25% | 39 → 43 | 6 | 7 → 7 | -0.029 | 0.000 |
| Jogador 1 | 4-5 | 5 | 0.000 | 8.000 | 1 → 1 | 3 → 3 | 25% → 25% | 43 → 48 | 4 | 7 → 7 | -0.004 | 0.000 |
| Jogador 1 | 4-6 | 5 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 48 → 58 | 0 | 7 → 7 | -0.000 | 0.000 |
| Jogador 1 | 4-7 | 7 | 0.000 | -4.000 | 1 → 1 | 3 → 4 | 25% → 25% | 58 → 71 | 1 | 7 → 7 | -0.007 | 0.000 |
| Jogador 1 | 5-1 | 9 | 0.000 | -2.000 | 1 → 1 | 4 → 3 | 25% → 25% | 71 → 80 | 6 | 7 → 7 | -0.006 | 0.321 |
| Jogador 1 | 5-2 | 10 | 4.000 | -4.000 | 1 → 1 | 3 → 4 | 25% → 25% | 80 → 88 | 11 | 7 → 7 | -0.012 | -0.300 |
| Jogador 1 | 5-3 | 10 | 2.000 | 4.000 | 1 → 1 | 4 → 4 | 25% → 25% | 88 → 94 | 11 | 7 → 7 | 0.026 | -0.280 |
| Jogador 1 | 5-4 | 10 | 0.000 | 4.000 | 1 → 1 | 4 → 3 | 25% → 25% | 94 → 98 | 15 | 7 → 7 | -0.008 | 0.000 |
| Jogador 1 | 5-5 | 10 | 4.000 | -8.000 | 1 → 1 | 3 → 5 | 25% → 25% | 98 → 103 | 17 | 7 → 7 | 0.009 | 0.289 |
| Jogador 1 | 5-6 | 10 | -38.000 | -38.000 | 1 → 0 | 5 → 0 | 25% → 0% | 103 → 97 | 15 | 7 → 7 | -0.086 | -0.280 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 14, COMPOSITION_COMPATIBILITY: 21, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 15; mudanças de composição: 0; posicionamento melhorou em 58 ações e piorou em 46.
- Jogador 1 — estado final: ouro 97, nível 7, vida 5.0, colocação 5.
| Jogador 2 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.214 | 0.000 |
| Jogador 2 | 1-2 | 6 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.168 | 0.000 |
| Jogador 2 | 1-3 | 5 | 2.000 | 0.000 | 0 → 1 | 1 → 0 | 7% → 7% | 2 → 3 | 2 | 3 → 3 | 0.006 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 2.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 5 | 2 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 8 | 2.000 | 4.000 | 1 → 1 | 1 → 2 | 11% → 14% | 5 → 7 | 3 | 4 → 4 | 0.009 | -0.303 |
| Jogador 2 | 2-2 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 14% → 14% | 7 → 7 | 7 | 4 → 4 | 0.017 | -0.232 |
| Jogador 2 | 2-3 | 9 | 2.000 | 2.000 | 1 → 1 | 2 → 2 | 14% → 18% | 7 → 7 | 8 | 4 → 5 | -0.083 | -0.270 |
| Jogador 2 | 2-4 | 10 | -2.000 | 4.000 | 1 → 0 | 2 → 1 | 18% → 18% | 7 → 9 | 10 | 5 → 5 | -0.032 | 0.000 |
| Jogador 2 | 2-5 | 5 | 4.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 9 → 12 | 3 | 5 → 5 | 0.147 | -0.506 |
| Jogador 2 | 2-6 | 9 | 6.000 | 0.000 | 0 → 0 | 1 → 2 | 18% → 21% | 12 → 7 | 11 | 5 → 6 | 0.013 | 0.300 |
| Jogador 2 | 2-7 | 6 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 21% → 21% | 7 → 8 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 3-1 | 6 | 6.000 | -6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 15 | 0 | 6 → 6 | 0.014 | 0.460 |
| Jogador 2 | 3-2 | 9 | 0.000 | 4.000 | 0 → 0 | 2 → 3 | 21% → 21% | 15 → 8 | 14 | 6 → 6 | -0.013 | 0.317 |
| Jogador 2 | 3-3 | 6 | 0.000 | 6.000 | 0 → 0 | 3 → 4 | 21% → 21% | 8 → 8 | 7 | 6 → 6 | -0.010 | 0.460 |
| Jogador 2 | 3-4 | 8 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 8 → 6 | 8 | 6 → 7 | 0.025 | 0.000 |
| Jogador 2 | 3-5 | 7 | 6.000 | -6.000 | 0 → 0 | 4 → 4 | 21% → 25% | 6 → 10 | 7 | 7 → 7 | 0.026 | 0.407 |
| Jogador 2 | 3-6 | 6 | 0.000 | 2.000 | 0 → 0 | 4 → 5 | 25% → 25% | 10 → 14 | 1 | 7 → 7 | 0.068 | -0.444 |
| Jogador 2 | 3-7 | 10 | -4.000 | -8.000 | 0 → 0 | 5 → 4 | 25% → 25% | 14 → 8 | 19 | 7 → 7 | -0.041 | 0.000 |
| Jogador 2 | 4-1 | 8 | 0.000 | 6.000 | 0 → 0 | 4 → 5 | 25% → 25% | 8 → 11 | 3 | 7 → 7 | 0.063 | 0.367 |
| Jogador 2 | 4-2 | 4 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 25% → 25% | 11 → 17 | 0 | 7 → 7 | -0.001 | -0.675 |
| Jogador 2 | 4-3 | 6 | 0.000 | 6.000 | 0 → 0 | 5 → 5 | 25% → 25% | 17 → 21 | 3 | 7 → 7 | -0.043 | -0.450 |
| Jogador 2 | 4-4 | 5 | 0.000 | 6.000 | 0 → 0 | 5 → 5 | 25% → 25% | 21 → 25 | 3 | 7 → 7 | -0.000 | 0.000 |
| Jogador 2 | 4-5 | 10 | 0.000 | 0.000 | 0 → 0 | 5 → 6 | 25% → 25% | 25 → 11 | 23 | 7 → 8 | 0.005 | -0.270 |
| Jogador 2 | 4-6 | 10 | 4.000 | -6.000 | 0 → 2 | 6 → 3 | 25% → 25% | 11 → 17 | 4 | 8 → 8 | 0.032 | 0.288 |
| Jogador 2 | 4-7 | 5 | 4.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 29% | 17 → 21 | 2 | 8 → 8 | -0.056 | 0.000 |
| Jogador 2 | 5-1 | 7 | 0.000 | 4.000 | 2 → 2 | 3 → 4 | 29% → 29% | 21 → 28 | 2 | 8 → 8 | 0.040 | 0.439 |
| Jogador 2 | 5-2 | 5 | 0.000 | 8.000 | 2 → 2 | 4 → 4 | 29% → 29% | 28 → 33 | 4 | 8 → 8 | 0.000 | 0.639 |
| Jogador 2 | 5-3 | 5 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 29% → 29% | 33 → 43 | 0 | 8 → 8 | -0.039 | 0.611 |
| Jogador 2 | 5-4 | 8 | 0.000 | -6.000 | 2 → 2 | 4 → 4 | 29% → 29% | 43 → 56 | 1 | 8 → 8 | -0.005 | 0.000 |
| Jogador 2 | 5-5 | 4 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 29% → 29% | 56 → 69 | 0 | 8 → 8 | 0.068 | 0.730 |
| Jogador 2 | 5-6 | 6 | 0.000 | 4.000 | 2 → 2 | 4 → 3 | 29% → 29% | 69 → 77 | 4 | 8 → 8 | -0.087 | -0.467 |
| Jogador 2 | 5-7 | 10 | 0.000 | 0.000 | 2 → 2 | 3 → 4 | 29% → 29% | 77 → 77 | 13 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 10 | 0.000 | 6.000 | 2 → 2 | 4 → 4 | 29% → 29% | 77 → 81 | 11 | 8 → 8 | 0.000 | 0.296 |
| Jogador 2 | 6-2 | 10 | -36.000 | -48.000 | 2 → 0 | 4 → 0 | 29% → 0% | 81 → 75 | 15 | 8 → 8 | -0.080 | -0.275 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 14, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 15; mudanças de composição: 0; posicionamento melhorou em 54 ações e piorou em 41.
- Jogador 2 — estado final: ouro 75, nível 8, vida 10.0, colocação 3.
| Jogador 3 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.150 | 0.000 |
| Jogador 3 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.007 | 0.000 |
| Jogador 3 | 1-3 | 5 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 7% → 7% | 2 → 3 | 2 | 3 → 3 | -0.092 | 0.000 |
| Jogador 3 | 1-4 | 8 | 4.000 | 2.000 | 0 → 1 | 0 → 0 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | 0.068 | 0.000 |
| Jogador 3 | 2-1 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 2 | 11% → 14% | 4 → 6 | 3 | 4 → 4 | 0.023 | -0.296 |
| Jogador 3 | 2-2 | 7 | 4.000 | 4.000 | 1 → 1 | 2 → 1 | 14% → 14% | 6 → 6 | 6 | 4 → 4 | -0.030 | -0.377 |
| Jogador 3 | 2-3 | 7 | 0.000 | 10.000 | 1 → 1 | 1 → 1 | 14% → 14% | 6 → 7 | 5 | 4 → 4 | -0.036 | -0.369 |
| Jogador 3 | 2-4 | 10 | 0.000 | 10.000 | 1 → 1 | 1 → 1 | 14% → 14% | 7 → 7 | 6 | 4 → 4 | 0.005 | 0.000 |
| Jogador 3 | 2-5 | 10 | 4.000 | -2.000 | 1 → 1 | 1 → 2 | 14% → 14% | 7 → 13 | 6 | 4 → 5 | 0.025 | 0.251 |
| Jogador 3 | 2-6 | 9 | 8.000 | -4.000 | 1 → 1 | 2 → 1 | 14% → 18% | 13 → 16 | 3 | 5 → 5 | -0.016 | -0.282 |
| Jogador 3 | 2-7 | 7 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 18% → 18% | 16 → 18 | 4 | 5 → 5 | 0.004 | 0.000 |
| Jogador 3 | 3-1 | 5 | -4.000 | 4.000 | 1 → 1 | 2 → 2 | 18% → 18% | 18 → 25 | 0 | 5 → 5 | 0.001 | -0.527 |
| Jogador 3 | 3-2 | 5 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 18% | 25 → 33 | 0 | 5 → 5 | 0.001 | -0.555 |
| Jogador 3 | 3-3 | 9 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 18% | 33 → 42 | 0 | 5 → 5 | 0.002 | -0.313 |
| Jogador 3 | 3-4 | 10 | 2.000 | -2.000 | 1 → 2 | 2 → 2 | 18% → 18% | 42 → 52 | 0 | 5 → 5 | 0.002 | 0.000 |
| Jogador 3 | 3-5 | 10 | -2.000 | 2.000 | 2 → 1 | 2 → 2 | 18% → 18% | 52 → 64 | 0 | 5 → 5 | -0.042 | -0.263 |
| Jogador 3 | 3-6 | 10 | 0.000 | -8.000 | 1 → 1 | 2 → 3 | 18% → 18% | 64 → 83 | 2 | 5 → 5 | -0.007 | -0.278 |
| Jogador 3 | 3-7 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 3 | 18% → 18% | 83 → 89 | 12 | 5 → 5 | 0.055 | 0.000 |
| Jogador 3 | 4-1 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 18% → 18% | 89 → 100 | 2 | 5 → 6 | -0.049 | -0.276 |
| Jogador 3 | 4-2 | 10 | -22.000 | -34.000 | 1 → 0 | 3 → 0 | 18% → 0% | 100 → 90 | 12 | 6 → 6 | -0.002 | -0.285 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 4, COMPOSITION_COMPATIBILITY: 11, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 12; mudanças de composição: 0; posicionamento melhorou em 47 ações e piorou em 50.
- Jogador 3 — estado final: ouro 90, nível 6, vida 9.0, colocação 8.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.150 | 0.000 |
| Jogador 4 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 4 | 1-3 | 8 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.016 | 0.000 |
| Jogador 4 | 1-4 | 11 | 0.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 7 | 4 | 3 → 4 | 0.054 | 0.000 |
| Jogador 4 | 2-1 | 8 | 2.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 14% | 7 → 6 | 6 | 4 → 4 | -0.004 | -0.296 |
| Jogador 4 | 2-2 | 10 | 2.000 | 6.000 | 0 → 0 | 2 → 3 | 14% → 14% | 6 → 8 | 6 | 4 → 4 | -0.084 | -0.253 |
| Jogador 4 | 2-3 | 9 | 6.000 | 0.000 | 0 → 0 | 3 → 2 | 14% → 18% | 8 → 6 | 8 | 4 → 5 | -0.004 | 0.306 |
| Jogador 4 | 2-4 | 10 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 6 → 8 | 11 | 5 → 5 | 0.006 | 0.000 |
| Jogador 4 | 2-5 | 10 | 6.000 | 4.000 | 0 → 0 | 2 → 3 | 18% → 18% | 8 → 10 | 6 | 5 → 5 | 0.012 | 0.259 |
| Jogador 4 | 2-6 | 10 | 2.000 | 0.000 | 0 → 0 | 3 → 3 | 18% → 21% | 10 → 8 | 14 | 5 → 6 | 0.018 | 0.251 |
| Jogador 4 | 2-7 | 10 | 0.000 | 8.000 | 0 → 0 | 3 → 3 | 21% → 21% | 8 → 6 | 8 | 6 → 6 | 0.049 | 0.000 |
| Jogador 4 | 3-1 | 10 | 4.000 | -8.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 11 | 6 | 6 → 6 | 0.031 | 0.281 |
| Jogador 4 | 3-2 | 8 | 2.000 | 6.000 | 0 → 1 | 3 → 2 | 21% → 21% | 11 → 11 | 5 | 6 → 6 | -0.020 | -0.328 |
| Jogador 4 | 3-3 | 6 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 11 → 14 | 3 | 6 → 6 | -0.048 | -0.430 |
| Jogador 4 | 3-4 | 8 | 0.000 | 12.000 | 1 → 1 | 2 → 5 | 21% → 21% | 14 → 14 | 7 | 6 → 6 | 0.029 | 0.000 |
| Jogador 4 | 3-5 | 9 | 0.000 | 2.000 | 1 → 1 | 5 → 3 | 21% → 21% | 14 → 9 | 13 | 6 → 6 | 0.033 | 0.322 |
| Jogador 4 | 3-6 | 8 | 0.000 | 4.000 | 1 → 1 | 3 → 5 | 21% → 21% | 9 → 15 | 6 | 6 → 6 | 0.010 | 0.350 |
| Jogador 4 | 3-7 | 8 | 6.000 | -8.000 | 1 → 2 | 5 → 3 | 21% → 21% | 15 → 20 | 5 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-1 | 7 | 0.000 | 6.000 | 2 → 1 | 3 → 3 | 21% → 21% | 20 → 23 | 3 | 6 → 7 | -0.021 | -0.381 |
| Jogador 4 | 4-2 | 6 | 4.000 | 0.000 | 1 → 2 | 3 → 3 | 21% → 25% | 23 → 29 | 2 | 7 → 7 | 0.022 | 0.502 |
| Jogador 4 | 4-3 | 6 | 0.000 | 0.000 | 2 → 2 | 3 → 4 | 25% → 25% | 29 → 39 | 3 | 7 → 7 | 0.015 | 0.489 |
| Jogador 4 | 4-4 | 6 | 0.000 | -2.000 | 2 → 2 | 4 → 5 | 25% → 25% | 39 → 50 | 2 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 4-5 | 9 | 0.000 | 6.000 | 2 → 2 | 5 → 5 | 25% → 25% | 50 → 43 | 16 | 7 → 7 | -0.046 | -0.302 |
| Jogador 4 | 4-6 | 8 | 0.000 | -2.000 | 2 → 2 | 5 → 5 | 25% → 25% | 43 → 54 | 5 | 7 → 7 | -0.066 | -0.339 |
| Jogador 4 | 4-7 | 10 | 0.000 | 4.000 | 2 → 2 | 5 → 4 | 25% → 25% | 54 → 45 | 22 | 7 → 7 | 0.005 | 0.000 |
| Jogador 4 | 5-1 | 10 | 6.000 | -6.000 | 2 → 2 | 4 → 4 | 25% → 29% | 45 → 37 | 19 | 7 → 8 | 0.004 | -0.290 |
| Jogador 4 | 5-2 | 7 | -46.000 | -44.000 | 2 → 0 | 4 → 0 | 29% → 0% | 37 → 35 | 6 | 8 → 8 | -0.077 | -0.393 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 16, COMPOSITION_COMPATIBILITY: 19, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 15; mudanças de composição: 0; posicionamento melhorou em 41 ações e piorou em 29.
- Jogador 4 — estado final: ouro 35, nível 8, vida 16.0, colocação 7.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.149 | 0.000 |
| Jogador 5 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.019 | 0.000 |
| Jogador 5 | 1-3 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.012 | 0.000 |
| Jogador 5 | 1-4 | 5 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | 0.084 | 0.000 |
| Jogador 5 | 2-1 | 8 | 6.000 | 2.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.095 | 0.320 |
| Jogador 5 | 2-2 | 10 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 6 → 12 | 7 | 4 → 4 | 0.101 | 0.256 |
| Jogador 5 | 2-3 | 10 | 4.000 | 0.000 | 0 → 1 | 1 → 0 | 14% → 18% | 12 → 8 | 11 | 4 → 5 | 0.009 | 0.274 |
| Jogador 5 | 2-4 | 8 | 0.000 | 8.000 | 1 → 1 | 0 → 0 | 18% → 18% | 8 → 6 | 9 | 5 → 5 | -0.045 | 0.000 |
| Jogador 5 | 2-5 | 7 | 0.000 | 4.000 | 1 → 1 | 0 → 0 | 18% → 18% | 6 → 7 | 6 | 5 → 5 | 0.004 | 0.384 |
| Jogador 5 | 2-6 | 10 | 2.000 | -4.000 | 1 → 1 | 0 → 0 | 18% → 21% | 7 → 5 | 11 | 5 → 6 | 0.012 | -0.243 |
| Jogador 5 | 2-7 | 7 | 0.000 | 10.000 | 1 → 1 | 0 → 2 | 21% → 21% | 5 → 5 | 5 | 6 → 6 | 0.036 | 0.000 |
| Jogador 5 | 3-1 | 8 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 5 → 6 | 5 | 6 → 6 | 0.000 | 0.369 |
| Jogador 5 | 3-2 | 7 | 0.000 | 6.000 | 1 → 1 | 2 → 1 | 21% → 21% | 6 → 7 | 6 | 6 → 6 | -0.014 | 0.400 |
| Jogador 5 | 3-3 | 10 | 0.000 | -2.000 | 1 → 1 | 1 → 2 | 21% → 21% | 7 → 19 | 9 | 6 → 6 | 0.017 | 0.298 |
| Jogador 5 | 3-4 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 1 | 21% → 21% | 19 → 24 | 4 | 6 → 6 | -0.027 | 0.000 |
| Jogador 5 | 3-5 | 8 | 0.000 | 2.000 | 1 → 1 | 1 → 3 | 21% → 21% | 24 → 33 | 3 | 6 → 6 | 0.042 | 0.351 |
| Jogador 5 | 3-6 | 6 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 33 → 45 | 1 | 6 → 6 | -0.011 | 0.477 |
| Jogador 5 | 3-7 | 9 | 0.000 | 4.000 | 1 → 1 | 3 → 1 | 21% → 21% | 45 → 47 | 9 | 6 → 6 | -0.031 | 0.000 |
| Jogador 5 | 4-1 | 10 | 0.000 | -4.000 | 1 → 1 | 1 → 3 | 21% → 21% | 47 → 57 | 7 | 6 → 6 | 0.028 | -0.275 |
| Jogador 5 | 4-2 | 10 | 6.000 | -12.000 | 1 → 2 | 3 → 3 | 21% → 25% | 57 → 62 | 12 | 6 → 7 | 0.017 | 0.286 |
| Jogador 5 | 4-3 | 5 | 0.000 | 2.000 | 2 → 2 | 3 → 3 | 25% → 25% | 62 → 73 | 1 | 7 → 7 | -0.074 | 0.587 |
| Jogador 5 | 4-4 | 6 | 0.000 | 6.000 | 2 → 2 | 3 → 4 | 25% → 25% | 73 → 81 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 4-5 | 4 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 25% → 25% | 81 → 93 | 0 | 7 → 7 | 0.054 | 0.715 |
| Jogador 5 | 4-6 | 6 | 0.000 | -2.000 | 2 → 2 | 4 → 5 | 25% → 25% | 93 → 104 | 1 | 7 → 7 | 0.040 | -0.450 |
| Jogador 5 | 4-7 | 10 | 0.000 | 6.000 | 2 → 2 | 5 → 4 | 25% → 25% | 104 → 111 | 7 | 7 → 7 | -0.034 | 0.000 |
| Jogador 5 | 5-1 | 10 | 0.000 | 10.000 | 2 → 2 | 4 → 3 | 25% → 25% | 111 → 115 | 7 | 7 → 7 | -0.004 | 0.000 |
| Jogador 5 | 5-2 | 10 | 0.000 | 2.000 | 2 → 2 | 3 → 4 | 25% → 25% | 115 → 126 | 6 | 7 → 7 | 0.006 | -0.275 |
| Jogador 5 | 5-3 | 10 | 0.000 | 6.000 | 2 → 2 | 4 → 3 | 25% → 25% | 126 → 131 | 10 | 7 → 7 | -0.006 | -0.290 |
| Jogador 5 | 5-4 | 10 | 6.000 | -6.000 | 2 → 1 | 3 → 3 | 25% → 25% | 131 → 129 | 24 | 7 → 7 | 0.008 | 0.000 |
| Jogador 5 | 5-5 | 10 | 4.000 | -4.000 | 1 → 2 | 3 → 2 | 25% → 25% | 129 → 136 | 9 | 7 → 7 | 0.005 | -0.273 |
| Jogador 5 | 5-6 | 10 | 6.000 | 0.000 | 2 → 2 | 2 → 2 | 25% → 25% | 136 → 138 | 16 | 7 → 7 | 0.001 | 0.000 |
| Jogador 5 | 5-7 | 10 | 0.000 | -4.000 | 2 → 2 | 2 → 1 | 25% → 25% | 138 → 148 | 17 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-1 | 10 | 0.000 | -8.000 | 2 → 2 | 1 → 2 | 25% → 25% | 148 → 161 | 10 | 7 → 7 | 0.000 | 0.305 |
| Jogador 5 | 6-2 | 10 | 0.000 | 12.000 | 2 → 2 | 2 → 2 | 25% → 25% | 161 → 163 | 16 | 7 → 7 | 0.000 | 0.292 |
| Jogador 5 | 6-3 | 10 | 0.000 | 0.000 | 2 → 2 | 2 → 3 | 25% → 25% | 163 → 169 | 17 | 7 → 7 | 0.000 | 0.304 |
| Jogador 5 | 6-4 | 10 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 169 → 174 | 15 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-5 | 10 | 0.000 | -2.000 | 2 → 2 | 3 → 3 | 25% → 25% | 174 → 172 | 12 | 7 → 7 | 0.000 | 0.310 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 13, COMPOSITION_COMPATIBILITY: 44, IMMEDIATE_UPGRADE: 11, PAIR_POTENTIAL: 21; mudanças de composição: 0; posicionamento melhorou em 61 ações e piorou em 44.
- Jogador 5 — estado final: ouro 172, nível 7, vida 23.0, colocação 1.
| Jogador 6 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.217 | 0.000 |
| Jogador 6 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.065 | 0.000 |
| Jogador 6 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.097 | 0.000 |
| Jogador 6 | 1-4 | 9 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 4 | 4 | 3 → 4 | -0.083 | 0.000 |
| Jogador 6 | 2-1 | 8 | 4.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 4 → 8 | 3 | 4 → 4 | 0.021 | 0.314 |
| Jogador 6 | 2-2 | 10 | 6.000 | -8.000 | 0 → 0 | 2 → 2 | 14% → 18% | 8 → 8 | 11 | 4 → 5 | 0.031 | 0.269 |
| Jogador 6 | 2-3 | 7 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 18% → 18% | 8 → 5 | 8 | 5 → 5 | -0.007 | -0.332 |
| Jogador 6 | 2-4 | 10 | 0.000 | -2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 5 → 7 | 7 | 5 → 5 | 0.090 | 0.000 |
| Jogador 6 | 2-5 | 10 | 2.000 | 0.000 | 0 → 1 | 3 → 2 | 18% → 18% | 7 → 7 | 6 | 5 → 6 | -0.011 | -0.237 |
| Jogador 6 | 2-6 | 6 | 2.000 | 8.000 | 1 → 1 | 2 → 2 | 18% → 21% | 7 → 8 | 5 | 6 → 6 | 0.002 | 0.423 |
| Jogador 6 | 2-7 | 6 | 0.000 | 12.000 | 1 → 1 | 2 → 4 | 21% → 21% | 8 → 7 | 6 | 6 → 6 | -0.005 | 0.000 |
| Jogador 6 | 3-1 | 8 | 0.000 | 10.000 | 1 → 1 | 4 → 5 | 21% → 21% | 7 → 7 | 5 | 6 → 6 | -0.097 | -0.323 |
| Jogador 6 | 3-2 | 9 | 4.000 | -6.000 | 1 → 2 | 5 → 3 | 21% → 21% | 7 → 12 | 2 | 6 → 6 | 0.050 | -0.287 |
| Jogador 6 | 3-3 | 7 | 0.000 | 8.000 | 2 → 2 | 3 → 3 | 21% → 21% | 12 → 14 | 4 | 6 → 6 | -0.003 | 0.402 |
| Jogador 6 | 3-4 | 10 | 6.000 | 0.000 | 2 → 3 | 3 → 1 | 21% → 21% | 14 → 11 | 8 | 6 → 6 | -0.050 | 0.000 |
| Jogador 6 | 3-5 | 6 | 0.000 | 8.000 | 3 → 3 | 1 → 2 | 21% → 21% | 11 → 12 | 4 | 6 → 6 | -0.000 | -0.439 |
| Jogador 6 | 3-6 | 8 | 0.000 | 2.000 | 3 → 3 | 2 → 3 | 21% → 21% | 12 → 19 | 3 | 6 → 6 | 0.133 | 0.369 |
| Jogador 6 | 3-7 | 4 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 19 → 25 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 10 | 0.000 | -6.000 | 3 → 3 | 3 → 4 | 21% → 21% | 25 → 36 | 1 | 6 → 6 | -0.028 | -0.276 |
| Jogador 6 | 4-2 | 6 | -2.000 | 4.000 | 3 → 2 | 4 → 4 | 21% → 21% | 36 → 44 | 3 | 6 → 6 | -0.018 | -0.472 |
| Jogador 6 | 4-3 | 10 | 8.000 | -4.000 | 2 → 2 | 4 → 3 | 21% → 21% | 44 → 52 | 5 | 6 → 6 | -0.061 | -0.278 |
| Jogador 6 | 4-4 | 7 | 0.000 | 2.000 | 2 → 2 | 3 → 3 | 21% → 21% | 52 → 62 | 1 | 6 → 6 | 0.134 | 0.000 |
| Jogador 6 | 4-5 | 8 | 0.000 | 0.000 | 2 → 2 | 3 → 4 | 21% → 21% | 62 → 74 | 2 | 6 → 6 | 0.020 | 0.360 |
| Jogador 6 | 4-6 | 10 | -4.000 | -4.000 | 2 → 2 | 4 → 4 | 21% → 18% | 74 → 82 | 11 | 6 → 6 | -0.025 | 0.288 |
| Jogador 6 | 4-7 | 10 | 4.000 | 0.000 | 2 → 2 | 4 → 4 | 18% → 21% | 82 → 86 | 12 | 6 → 6 | -0.065 | 0.000 |
| Jogador 6 | 5-1 | 10 | 0.000 | -6.000 | 2 → 2 | 4 → 5 | 21% → 21% | 86 → 99 | 2 | 6 → 6 | 0.069 | -0.273 |
| Jogador 6 | 5-2 | 10 | 4.000 | 4.000 | 2 → 3 | 5 → 3 | 21% → 21% | 99 → 98 | 12 | 6 → 7 | 0.005 | 0.000 |
| Jogador 6 | 5-3 | 10 | -40.000 | -40.000 | 3 → 0 | 3 → 0 | 21% → 0% | 98 → 97 | 9 | 7 → 7 | -0.106 | -0.275 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 2, COMPOSITION_COMPATIBILITY: 29, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 57 ações e piorou em 50.
- Jogador 6 — estado final: ouro 97, nível 7, vida 6.0, colocação 6.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.150 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.016 | 0.000 |
| Jogador 7 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.089 | 0.000 |
| Jogador 7 | 1-4 | 11 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 5 | 4 | 3 → 4 | 0.005 | 0.000 |
| Jogador 7 | 2-1 | 8 | 4.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | 0.022 | 0.320 |
| Jogador 7 | 2-2 | 10 | 4.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 8 | 10 | 4 → 5 | 0.029 | 0.280 |
| Jogador 7 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 1 → 3 | 18% → 18% | 8 → 8 | 7 | 5 → 5 | 0.000 | 0.352 |
| Jogador 7 | 2-4 | 10 | 8.000 | 6.000 | 0 → 0 | 3 → 2 | 18% → 18% | 8 → 7 | 9 | 5 → 5 | 0.068 | 0.000 |
| Jogador 7 | 2-5 | 10 | 2.000 | -4.000 | 0 → 0 | 2 → 2 | 18% → 18% | 7 → 5 | 11 | 5 → 6 | 0.033 | -0.243 |
| Jogador 7 | 2-6 | 10 | 4.000 | 2.000 | 0 → 1 | 2 → 2 | 18% → 21% | 5 → 6 | 5 | 6 → 6 | -0.010 | 0.259 |
| Jogador 7 | 2-7 | 8 | 0.000 | 10.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 6 | 5 | 6 → 6 | -0.009 | 0.000 |
| Jogador 7 | 3-1 | 8 | 4.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 5 | 6 | 6 → 6 | 0.014 | -0.323 |
| Jogador 7 | 3-2 | 7 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 5 → 7 | 4 | 6 → 6 | 0.001 | 0.395 |
| Jogador 7 | 3-3 | 6 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 7 → 7 | 7 | 6 → 6 | 0.012 | 0.483 |
| Jogador 7 | 3-4 | 7 | -2.000 | 4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | -0.026 | 0.000 |
| Jogador 7 | 3-5 | 5 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 9 → 15 | 1 | 6 → 6 | -0.194 | 0.562 |
| Jogador 7 | 3-6 | 9 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 21% → 21% | 15 → 7 | 15 | 6 → 7 | 0.006 | 0.315 |
| Jogador 7 | 3-7 | 9 | 2.000 | 2.000 | 1 → 1 | 3 → 5 | 21% → 25% | 7 → 8 | 10 | 7 → 7 | 0.005 | 0.000 |
| Jogador 7 | 4-1 | 10 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 25% → 25% | 8 → 8 | 8 | 7 → 7 | 0.098 | 0.283 |
| Jogador 7 | 4-2 | 6 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 25% → 25% | 8 → 9 | 8 | 7 → 7 | -0.010 | 0.498 |
| Jogador 7 | 4-3 | 9 | 0.000 | -6.000 | 1 → 1 | 5 → 6 | 25% → 25% | 9 → 11 | 15 | 7 → 7 | 0.007 | 0.318 |
| Jogador 7 | 4-4 | 10 | 2.000 | 2.000 | 1 → 1 | 6 → 5 | 25% → 25% | 11 → 10 | 10 | 7 → 7 | -0.025 | 0.000 |
| Jogador 7 | 4-5 | 5 | 0.000 | 4.000 | 1 → 1 | 5 → 5 | 25% → 25% | 10 → 17 | 2 | 7 → 7 | -0.003 | 0.577 |
| Jogador 7 | 4-6 | 7 | 0.000 | -6.000 | 1 → 1 | 5 → 5 | 25% → 25% | 17 → 29 | 3 | 7 → 7 | 0.058 | -0.388 |
| Jogador 7 | 4-7 | 10 | 2.000 | -4.000 | 1 → 2 | 5 → 4 | 25% → 25% | 29 → 27 | 12 | 7 → 8 | 0.005 | 0.000 |
| Jogador 7 | 5-1 | 7 | 2.000 | 2.000 | 2 → 2 | 4 → 5 | 25% → 29% | 27 → 33 | 2 | 8 → 8 | -0.008 | -0.393 |
| Jogador 7 | 5-2 | 5 | 0.000 | 6.000 | 2 → 2 | 5 → 5 | 29% → 29% | 33 → 39 | 3 | 8 → 8 | -0.184 | 0.584 |
| Jogador 7 | 5-3 | 7 | -2.000 | 2.000 | 2 → 2 | 5 → 5 | 29% → 29% | 39 → 50 | 2 | 8 → 8 | -0.003 | 0.419 |
| Jogador 7 | 5-4 | 6 | 4.000 | -2.000 | 2 → 2 | 5 → 6 | 29% → 29% | 50 → 59 | 3 | 8 → 8 | 0.035 | 0.000 |
| Jogador 7 | 5-5 | 7 | -4.000 | 2.000 | 2 → 2 | 6 → 4 | 29% → 29% | 59 → 67 | 3 | 8 → 8 | 0.085 | -0.393 |
| Jogador 7 | 5-6 | 6 | 10.000 | -2.000 | 2 → 2 | 4 → 4 | 29% → 29% | 67 → 74 | 4 | 8 → 8 | -0.004 | 0.495 |
| Jogador 7 | 5-7 | 7 | -6.000 | 6.000 | 2 → 1 | 4 → 5 | 29% → 29% | 74 → 86 | 6 | 8 → 8 | -0.006 | 0.000 |
| Jogador 7 | 6-1 | 10 | 2.000 | -4.000 | 1 → 2 | 5 → 4 | 29% → 29% | 86 → 94 | 3 | 8 → 8 | 0.005 | -0.285 |
| Jogador 7 | 6-2 | 9 | -2.000 | 6.000 | 2 → 2 | 4 → 3 | 29% → 29% | 94 → 96 | 8 | 8 → 8 | -0.047 | 0.000 |
| Jogador 7 | 6-3 | 8 | 12.000 | -6.000 | 2 → 3 | 3 → 3 | 29% → 29% | 96 → 98 | 9 | 8 → 8 | 0.005 | -0.356 |
| Jogador 7 | 6-4 | 10 | -6.000 | 14.000 | 3 → 3 | 3 → 4 | 29% → 25% | 98 → 97 | 17 | 8 → 8 | 0.001 | 0.000 |
| Jogador 7 | 6-5 | 10 | -46.000 | -62.000 | 3 → 0 | 4 → 0 | 25% → 0% | 97 → 108 | 8 | 8 → 8 | -0.088 | -0.290 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 17, IMMEDIATE_UPGRADE: 12, PAIR_POTENTIAL: 20; mudanças de composição: 0; posicionamento melhorou em 65 ações e piorou em 55.
- Jogador 7 — estado final: ouro 108, nível 8, vida 6.0, colocação 2.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.150 | 0.000 |
| Jogador 8 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 8 | 1-3 | 11 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.005 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.021 | 0.000 |
| Jogador 8 | 2-1 | 8 | 4.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 14% | 4 → 5 | 4 | 4 → 4 | -0.005 | -0.303 |
| Jogador 8 | 2-2 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 14% → 14% | 5 → 8 | 3 | 4 → 4 | -0.073 | -0.404 |
| Jogador 8 | 2-3 | 10 | 2.000 | -4.000 | 1 → 1 | 0 → 0 | 14% → 14% | 8 → 15 | 2 | 4 → 4 | 0.068 | -0.259 |
| Jogador 8 | 2-4 | 9 | -2.000 | 12.000 | 1 → 0 | 0 → 0 | 14% → 14% | 15 → 17 | 5 | 4 → 4 | -0.153 | 0.000 |
| Jogador 8 | 2-5 | 10 | 8.000 | 2.000 | 0 → 0 | 0 → 1 | 14% → 18% | 17 → 14 | 9 | 4 → 5 | 0.129 | -0.237 |
| Jogador 8 | 2-6 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 18% → 18% | 14 → 8 | 16 | 5 → 5 | 0.044 | -0.238 |
| Jogador 8 | 2-7 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 1 | 18% → 18% | 8 → 7 | 15 | 5 → 6 | 0.003 | 0.000 |
| Jogador 8 | 3-1 | 7 | 8.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 7 → 11 | 4 | 6 → 6 | 0.060 | -0.396 |
| Jogador 8 | 3-2 | 5 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 21% → 21% | 11 → 19 | 1 | 6 → 6 | -0.202 | -0.535 |
| Jogador 8 | 3-3 | 10 | 0.000 | 4.000 | 0 → 0 | 2 → 3 | 21% → 21% | 19 → 9 | 20 | 6 → 6 | 0.086 | -0.273 |
| Jogador 8 | 3-4 | 10 | 2.000 | -8.000 | 0 → 0 | 3 → 2 | 21% → 25% | 9 → 10 | 12 | 6 → 7 | -0.010 | 0.000 |
| Jogador 8 | 3-5 | 5 | 0.000 | 6.000 | 0 → 0 | 2 → 3 | 25% → 25% | 10 → 15 | 3 | 7 → 7 | -0.011 | -0.535 |
| Jogador 8 | 3-6 | 9 | 0.000 | 14.000 | 0 → 0 | 3 → 3 | 25% → 25% | 15 → 8 | 15 | 7 → 7 | 0.021 | -0.292 |
| Jogador 8 | 3-7 | 9 | 0.000 | -6.000 | 0 → 0 | 3 → 3 | 25% → 25% | 8 → 21 | 4 | 7 → 7 | -0.085 | 0.000 |
| Jogador 8 | 4-1 | 10 | 0.000 | 4.000 | 0 → 0 | 3 → 4 | 25% → 25% | 21 → 24 | 11 | 7 → 7 | 0.000 | 0.291 |
| Jogador 8 | 4-2 | 10 | 0.000 | 8.000 | 0 → 0 | 4 → 4 | 25% → 25% | 24 → 22 | 13 | 7 → 7 | -0.013 | 0.301 |
| Jogador 8 | 4-3 | 10 | 4.000 | -4.000 | 0 → 0 | 4 → 4 | 25% → 25% | 22 → 30 | 3 | 7 → 7 | -0.055 | 0.000 |
| Jogador 8 | 4-4 | 10 | 8.000 | -4.000 | 0 → 1 | 4 → 4 | 25% → 25% | 30 → 30 | 11 | 7 → 7 | 0.049 | 0.000 |
| Jogador 8 | 4-5 | 10 | 2.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 30 → 34 | 15 | 7 → 7 | 0.084 | -0.273 |
| Jogador 8 | 4-6 | 10 | 0.000 | -6.000 | 1 → 1 | 4 → 3 | 25% → 25% | 34 → 45 | 9 | 7 → 7 | 0.006 | 0.286 |
| Jogador 8 | 4-7 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 4 | 25% → 25% | 45 → 51 | 10 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 5 | 25% → 25% | 51 → 59 | 9 | 7 → 7 | 0.000 | 0.292 |
| Jogador 8 | 5-2 | 10 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 25% → 25% | 59 → 69 | 11 | 7 → 7 | 0.000 | 0.292 |
| Jogador 8 | 5-3 | 10 | 0.000 | 0.000 | 1 → 1 | 5 → 4 | 25% → 25% | 69 → 79 | 14 | 7 → 7 | 0.000 | 0.297 |
| Jogador 8 | 5-4 | 10 | 0.000 | -4.000 | 1 → 1 | 4 → 2 | 25% → 25% | 79 → 84 | 15 | 7 → 7 | -0.031 | 0.000 |
| Jogador 8 | 5-5 | 10 | 0.000 | -10.000 | 1 → 1 | 2 → 3 | 25% → 25% | 84 → 100 | 14 | 7 → 7 | 0.031 | 0.000 |
| Jogador 8 | 5-6 | 10 | 0.000 | 16.000 | 1 → 1 | 3 → 2 | 25% → 25% | 100 → 100 | 16 | 7 → 7 | -0.006 | 0.299 |
| Jogador 8 | 5-7 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 3 | 25% → 25% | 100 → 111 | 11 | 7 → 7 | 0.006 | 0.000 |
| Jogador 8 | 6-1 | 10 | -42.000 | -48.000 | 1 → 0 | 3 → 0 | 25% → 0% | 111 → 109 | 7 | 7 → 7 | -0.100 | -0.275 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 18, COMPOSITION_COMPATIBILITY: 26, IMMEDIATE_UPGRADE: 14, PAIR_POTENTIAL: 35; mudanças de composição: 0; posicionamento melhorou em 49 ações e piorou em 54.
- Jogador 8 — estado final: ouro 109, nível 7, vida 3.0, colocação 4.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 58 | 27 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 |
| Jogador 2 | 45 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 1 | 0 |
| Jogador 3 | 33 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 4 | 54 | 30 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Jogador 5 | 89 | 53 | 0 | 0 | 1 | 0 | 0 | 0 | 15 | 0 | 0 | 0 |
| Jogador 6 | 53 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| Jogador 7 | 58 | 20 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 |
| Jogador 8 | 93 | 53 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 0 |
- Jogador 1 — venda DA_18_Ornn (2-5, step 94): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Akali_AD (2-7, step 113): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Sentry (3-3, step 147): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 1 — venda DA_Vi18 (3-7, step 187): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 1 — venda DA_KogMaw18_AD (5-2, step 273): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Leona (5-2, step 276): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 1 — venda DA_18_Akali_AD (5-3, step 288): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Leona (5-6, step 312): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 1 — venda DA_CrimsonRaptor18 (5-6, step 318): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Tristana (3-7, step 186): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rammus (4-6, step 242): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_18_LeBlanc (5-6, step 312): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_RekSai (6-1, step 335): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_18_Tristana (6-2, step 349): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 3 — venda DA_18_Akali_AD (2-5, step 96): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_18_Caitlyn (3-7, step 187): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Xayah (2-5, step 98): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Elise (3-5, step 162): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Yunara (3-6, step 173): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Cassiopeia (3-7, step 182): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Elise (4-6, step 244): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Yunara (4-7, step 252): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (3-3, step 145): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (3-4, step 154): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_Karma18 (3-5, step 163): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (3-7, step 182): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_LeBlanc (4-1, step 195): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (4-7, step 252): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Rakan (5-2, step 272): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Azir (5-7, step 327): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Cassiopeia (6-1, step 340): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Vi18 (6-2, step 349): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Cassiopeia (6-4, step 366): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_Murkwolf18 (4-1, step 195): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (4-3, step 212): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 6 — venda DA_18_Akali_AD (4-5, step 233): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_Scuttlecrab18 (4-7, step 257): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_KogMaw18_AD (5-3, step 283): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 7 — venda DA_KogMaw18_AD (4-3, step 212): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_CrimsonRaptor18 (4-6, step 242): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_Gromp18_AP (5-3, step 282): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Yorick (5-5, step 302): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_18_Rammus (5-7, step 323): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Shen (6-4, step 369): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_Nidalee18_AP (6-5, step 380): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Veigar (2-6, step 103): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Leona (2-7, step 112): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Warwick (2-7, step 116): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Akali_AD (2-7, step 119): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Akali_AD (3-3, step 142): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_KhaZix (3-4, step 152): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 8 — venda DA_18_Sejuani (3-7, step 182): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Xayah (4-3, step 212): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Rakan (4-4, step 230): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_LeBlanc (4-6, step 242): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Teemo (4-6, step 247): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Warwick (4-6, step 249): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Warwick (4-7, step 254): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Teemo (4-7, step 257): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Teemo (4-7, step 259): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Teemo (5-1, step 264): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Sejuani (5-2, step 272): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Teemo (5-2, step 275): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Hecarim (5-2, step 279): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Hecarim (5-3, step 282): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Teemo (5-3, step 289): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Hecarim (5-4, step 294): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Hecarim (5-4, step 297): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_Vi18 (5-5, step 305): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=True, compensações posteriores=0.
- Jogador 8 — venda DA_18_Diana (5-5, step 307): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Hecarim (5-5, step 310): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Teemo (5-6, step 313): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rakan (5-7, step 322): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **9**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 2-5 | 94 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 2-7 | 113 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 5-2 | 273 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 5-3 | 288 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 5-6 | 318 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-3 | 618 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-4 | 729 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-5 | 865 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-5 | 866 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-6 | 963 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 964 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1062 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-7 | 1063 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1159 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1160 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1288 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-2 | 1289 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1421 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-3 | 1422 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1555 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-4 | 1556 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1692 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-5 | 1693 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1802 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 1942 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 2084 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 2171 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 2172 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 2383 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 2459 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-6 | 2531 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-7 | 2628 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-1 | 2756 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-2 | 2895 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-2 | 2896 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-3 | 3037 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-4 | 3173 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-5 | 3307 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-5 | 3308 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-6 | 3445 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 5-6 | 3446 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 2-7 | 1136 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-1 | 2148 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-2 | 2249 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 2 | 2-2 | 64 | PURCHASE_SALE_REVIEW | Compra de DA_18_Xayah foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 2 | 3-7 | 186 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-6 | 312 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_LeBlanc' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 45 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 2-3 | 675 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-4 | 809 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-5 | 882 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-1 | 1168 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-2 | 1288 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-3 | 1371 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-4 | 1481 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-5 | 1577 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-6 | 1668 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-7 | 1801 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-1 | 1915 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-2 | 1980 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2069 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-3 | 2070 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 2145 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-4 | 2146 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2279 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-5 | 2280 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 2420 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 2495 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-7 | 2496 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 2597 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 2675 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-3 | 2751 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-3 | 2752 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-4 | 2870 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-4 | 2871 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-5 | 2935 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-6 | 3023 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-7 | 3162 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-1 | 3303 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-2 | 3442 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 6-2 | 3443 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 4-5 | 2397 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-6 | 2472 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-7 | 2574 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-1 | 2652 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 2728 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-3 | 2847 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-4 | 2912 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-5 | 3000 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-7 | 187 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-3 | 186 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-2 | 503 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-3 | 599 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-4 | 739 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-5 | 877 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-6 | 1005 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 1105 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1182 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1259 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1539 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1676 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-5 | 1677 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 1810 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-6 | 1811 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 1950 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 2090 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-1 | 2091 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 2231 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 4-2 | 2232 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 2-5 | 982 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-6 | 1082 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-7 | 1159 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-1 | 1236 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-2 | 1371 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-5 | 1787 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 4 | 2-6 | 106 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 2-6 | 107 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sejuani) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 4 | 3-1 | 127 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yunara foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 4 | 3-6 | 173 | SOLD_CORE_UNIT | Venda de 'DA_18_Yunara' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 4-6 | 244 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 4-7 | 252 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 2-2 | 613 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-3 | 732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-3 | 733 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 2-4 | 865 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-4 | 866 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 2-5 | 1000 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-5 | 1001 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 2-6 | 1136 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-6 | 1137 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 2-7 | 1268 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-7 | 1269 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-1 | 1405 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-3 | 1605 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-3 | 1606 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-4 | 1715 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-4 | 1716 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-5 | 1835 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-5 | 1836 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-6 | 1945 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-6 | 1946 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 2061 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-7 | 2062 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-1 | 2161 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-1 | 2162 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 2251 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-2 | 2252 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-3 | 2337 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-3 | 2338 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-4 | 2426 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-4 | 2427 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 2547 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-5 | 2548 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-6 | 2658 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-6 | 2659 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-7 | 2789 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-7 | 2790 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-1 | 2922 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-1 | 2923 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-2 | 3030 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-2 | 3031 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 2-6 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 5 | 3-3 | 145 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 3-5 | 163 | SOLD_CORE_UNIT | Venda de 'DA_Karma18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 4-1 | 195 | SOLD_CORE_UNIT | Venda de 'DA_18_LeBlanc' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-7 | 252 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-2 | 272 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 5-7 | 327 | SOLD_CORE_UNIT | Venda de 'DA_18_Azir' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-1 | 340 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-2 | 349 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-4 | 366 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-1 | 393 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 766 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 862 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 994 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1294 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-4 | 1565 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-7 | 1876 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2220 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-4 | 2307 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-5 | 2369 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-7 | 2590 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-1 | 2730 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-1 | 2731 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-2 | 2870 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-2 | 2871 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 3009 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-3 | 3010 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-4 | 3143 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-4 | 3144 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-5 | 3288 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-5 | 3289 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-6 | 3426 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-6 | 3427 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-7 | 3572 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-7 | 3573 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-1 | 3715 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-1 | 3716 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-2 | 3856 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-2 | 3857 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-3 | 3997 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-3 | 3998 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-4 | 4134 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-4 | 4135 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-5 | 4271 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-5 | 4272 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| MEDIUM | Jogador 5 | 3-2 | 1409 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-3 | 1542 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-4 | 1650 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-5 | 1734 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-6 | 1853 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-6 | 2517 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-6 | 2529 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-1 | 2798 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-1 | 2810 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-1 | 2822 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-1 | 2834 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-1 | 2846 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-2 | 2961 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-2 | 2973 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-2 | 2985 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 2-1 | 59 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 6 | 4-1 | 195 | SOLD_CORE_UNIT | Venda de 'DA_Murkwolf18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 4-5 | 233 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 4-7 | 257 | SOLD_CORE_UNIT | Venda de 'DA_Scuttlecrab18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-1 | 45 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 152 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-4 | 358 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-1 | 469 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-2 | 600 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 695 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1251 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1376 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-4 | 1608 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1609 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-5 | 1697 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1698 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-1 | 2013 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 2014 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 2103 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 2104 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 2249 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 2250 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 2356 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 2742 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-7 | 2743 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-1 | 2887 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 2888 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 3025 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-2 | 3026 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-3 | 3168 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-3 | 3169 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| HIGH | Jogador 7 | 4-3 | 212 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 4-6 | 242 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 5-3 | 282 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 5-7 | 323 | SOLD_CORE_UNIT | Venda de 'DA_18_Rammus' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 6-4 | 369 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Shen' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 6-5 | 380 | SOLD_CORE_UNIT | Venda de 'DA_Nidalee18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 1-3 | 247 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 1-4 | 393 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 506 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 507 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-2 | 640 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 641 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-3 | 738 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-3 | 739 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-4 | 874 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-4 | 875 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-5 | 1009 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-6 | 1147 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-6 | 1148 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-7 | 1260 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1369 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1465 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1549 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1647 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1721 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-5 | 1722 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1839 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-6 | 1840 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 1966 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-7 | 1967 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 2099 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2185 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2303 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2439 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-4 | 2440 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2513 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-5 | 2514 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2612 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2748 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 2849 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-2 | 2924 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-2 | 2925 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-3 | 3029 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-3 | 3030 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-4 | 3119 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-5 | 3222 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-6 | 3314 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-6 | 3315 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-7 | 3416 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-7 | 3417 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-1 | 3564 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-2 | 3691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-2 | 3692 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-3 | 3807 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-3 | 3808 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-4 | 3949 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-4 | 3950 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-5 | 4088 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 6-5 | 4089 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 4-6 | 2675 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 7 | 1-3 | 333 | TEXT_MOVE_OSCILLATION | Possível alternância de duas unidades; confirme identidade/estado nos snapshots estruturados. |
| HIGH | Jogador 8 | 2-6 | 103 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 2-7 | 112 | SOLD_CORE_UNIT | Venda de 'DA_18_Leona' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 2-7 | 116 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 2-7 | 119 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-3 | 142 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 3-7 | 182 | SOLD_CORE_UNIT | Venda de 'DA_18_Sejuani' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-4 | 230 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-6 | 242 | SOLD_CORE_UNIT | Venda de 'DA_18_LeBlanc' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-6 | 247 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-6 | 249 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-7 | 254 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-7 | 257 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-7 | 259 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-1 | 264 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-2 | 272 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-2 | 275 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-2 | 279 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-3 | 282 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-3 | 289 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-4 | 294 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 5-5 | 307 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-5 | 310 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-6 | 313 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 5-7 | 322 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 2-2 | 553 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 818 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1318 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-2 | 1392 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-3 | 1523 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-5 | 1732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-6 | 1850 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-7 | 1979 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 2121 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2261 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2400 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 2401 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 2537 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 2675 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-6 | 2812 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-7 | 2945 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-1 | 3085 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-2 | 3222 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-3 | 3358 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-4 | 3494 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-5 | 3629 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-6 | 3769 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-7 | 3908 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-1 | 4048 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 6-1 | 4049 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
