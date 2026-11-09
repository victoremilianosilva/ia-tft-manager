# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4783**
- Achados: **783**
- CRITICAL: 0 | HIGH: 8 | MEDIUM: 65 | LOW: 710

## Metadados da sessão

- Match ID: ffc16893-4b4b-4e64-bc27-1ecf41a06a04
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 3d63262fb93d7504bfc05b4e6efd43b7d3bf9e722c0407b8e8b1bd7903bc856d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4273**
- Entradas posteriores à eliminação ignoradas: **510**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 59 | 7 | 8 | 5 | 61 | 2 | 3 | não/inconclusivo | 0 |
| Jogador 6 | 44 | 7 | 17 | 5 | 67 | 5 | 1 | não/inconclusivo | 0 |
| Jogador 7 | 87 | 8 | 26 | 1 | 58 | 3 | 1 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 197 | 63 | 30 | 11 | 2 | 19 | 65 | 0.1134 | 12 | 35 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 14, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 3, ALL_IN::MOVE_BOARD: 5, ALL_IN::PASS: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 6, FAST8::BUY: 9, FAST8::BUY_XP: 1, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 15, FAST8::PASS: 5, FAST8::SELL: 5, STABILIZE::BUY: 40, STABILIZE::BUY_XP: 10, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 12, STABILIZE::MOVE_BOARD: 28, STABILIZE::PASS: 13, STABILIZE::SELL: 19
- Jogador 1 — recompensas por ação: BUY: média 0.3917 (n=63), BUY_XP: média -0.0364 (n=11), ITEM: média 0.2071 (n=7), MOVE_BENCH: média 0.1500 (n=17), MOVE_BOARD: média -0.0042 (n=48), PASS: média -0.0311 (n=19), REROLL: média -0.1500 (n=2), SELL: média -0.1613 (n=30)
| Jogador 2 | 253 | 101 | 73 | 14 | 1 | 10 | 47 | 0.0420 | 7 | 23 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 41, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 2, ALL_IN::MOVE_BOARD: 13, ALL_IN::PASS: 2, ALL_IN::REROLL: 1, ALL_IN::SELL: 34, STABILIZE::BUY: 60, STABILIZE::BUY_XP: 14, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 18, STABILIZE::PASS: 8, STABILIZE::SELL: 39
- Jogador 2 — recompensas por ação: BUY: média 0.2179 (n=101), BUY_XP: média -0.0171 (n=14), ITEM: média 0.1800 (n=7), MOVE_BENCH: média 0.1650 (n=16), MOVE_BOARD: média -0.0100 (n=31), PASS: média -0.0640 (n=10), REROLL: média -0.0700 (n=1), SELL: média -0.1920 (n=73)
| Jogador 3 | 182 | 58 | 25 | 6 | 0 | 22 | 63 | 0.0990 | 4 | 17 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::MOVE_BOARD: 2, ALL_IN::PASS: 1, ALL_IN::SELL: 1, FAST8::BUY: 32, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 5, FAST8::MOVE_BOARD: 30, FAST8::PASS: 12, FAST8::SELL: 17, STABILIZE::BUY: 24, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 4, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 15, STABILIZE::PASS: 9, STABILIZE::SELL: 7
- Jogador 3 — recompensas por ação: BUY: média 0.3629 (n=58), BUY_XP: média -0.0250 (n=6), ITEM: média 0.1975 (n=8), MOVE_BENCH: média 0.1025 (n=16), MOVE_BOARD: média -0.0038 (n=47), PASS: média -0.0509 (n=22), SELL: média -0.1924 (n=25)
| Jogador 4 | 173 | 61 | 28 | 8 | 2 | 12 | 51 | 0.1105 | 6 | 19 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 15, ALL_IN::MOVE_BENCH: 5, ALL_IN::MOVE_BOARD: 4, ALL_IN::PASS: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 9, STABILIZE::BUY: 46, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 11, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 24, STABILIZE::PASS: 11, STABILIZE::SELL: 19
- Jogador 4 — recompensas por ação: BUY: média 0.4289 (n=61), BUY_XP: média -0.0288 (n=8), ITEM: média 0.1636 (n=11), MOVE_BENCH: média 0.0078 (n=23), MOVE_BOARD: média -0.0018 (n=28), PASS: média -0.0467 (n=12), REROLL: média -0.0700 (n=2), SELL: média -0.2875 (n=28)
| Jogador 5 | 231 | 85 | 55 | 18 | 1 | 15 | 48 | 0.0883 | 10 | 29 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 10, ALL_IN::ITEM: 2, ALL_IN::MOVE_BOARD: 2, ALL_IN::PASS: 1, ALL_IN::REROLL: 1, ALL_IN::SELL: 10, FAST8::BUY: 28, FAST8::BUY_XP: 6, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 3, FAST8::MOVE_BOARD: 20, FAST8::PASS: 7, FAST8::SELL: 20, STABILIZE::BUY: 47, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 9, STABILIZE::PASS: 7, STABILIZE::SELL: 25
- Jogador 5 — recompensas por ação: BUY: média 0.3165 (n=85), BUY_XP: média -0.0133 (n=18), ITEM: média 0.1256 (n=9), MOVE_BENCH: média 0.2553 (n=17), MOVE_BOARD: média 0.0010 (n=31), PASS: média -0.0407 (n=15), REROLL: média -0.0700 (n=1), SELL: média -0.2013 (n=55)
| Jogador 6 | 210 | 67 | 40 | 17 | 0 | 20 | 52 | 0.0343 | 8 | 47 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 6, ALL_IN::ITEM: 4, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 4, ALL_IN::PASS: 1, ALL_IN::SELL: 1, FAST8::BUY: 24, FAST8::BUY_XP: 5, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 3, FAST8::MOVE_BOARD: 20, FAST8::PASS: 7, FAST8::SELL: 14, LOSS_STREAK::BUY: 4, LOSS_STREAK::BUY_XP: 2, LOSS_STREAK::PASS: 1, LOSS_STREAK::SELL: 3, STABILIZE::BUY: 33, STABILIZE::BUY_XP: 10, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 8, STABILIZE::MOVE_BOARD: 16, STABILIZE::PASS: 11, STABILIZE::SELL: 22
- Jogador 6 — recompensas por ação: BUY: média 0.2510 (n=67), BUY_XP: média -0.0435 (n=17), ITEM: média 0.1329 (n=14), MOVE_BENCH: média 0.0967 (n=12), MOVE_BOARD: média -0.0177 (n=40), PASS: média -0.0235 (n=20), SELL: média -0.2680 (n=40)
| Jogador 7 | 239 | 58 | 28 | 26 | 0 | 25 | 85 | 0.0813 | 6 | 40 |
- Jogador 7 — ações por estratégia: ECON::BUY: 3, ECON::BUY_XP: 6, ECON::ITEM: 2, ECON::MOVE_BENCH: 2, ECON::MOVE_BOARD: 1, ECON::SELL: 1, FAST8::BUY: 27, FAST8::BUY_XP: 15, FAST8::ITEM: 6, FAST8::MOVE_BENCH: 6, FAST8::MOVE_BOARD: 29, FAST8::PASS: 9, FAST8::SELL: 16, STABILIZE::BUY: 22, STABILIZE::BUY_XP: 5, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 8, STABILIZE::MOVE_BOARD: 13, STABILIZE::PASS: 8, STABILIZE::SELL: 6, WINSTREAK::BUY: 6, WINSTREAK::ITEM: 1, WINSTREAK::MOVE_BENCH: 1, WINSTREAK::MOVE_BOARD: 25, WINSTREAK::PASS: 8, WINSTREAK::SELL: 5
- Jogador 7 — recompensas por ação: BUY: média 0.3481 (n=58), BUY_XP: média -0.0204 (n=26), ITEM: média 0.1318 (n=17), MOVE_BENCH: média 0.2276 (n=17), MOVE_BOARD: média -0.0037 (n=68), PASS: média -0.0148 (n=25), SELL: média -0.2046 (n=28)
| Jogador 8 | 272 | 104 | 71 | 22 | 0 | 16 | 51 | 0.0512 | 9 | 60 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 9, ALL_IN::MOVE_BOARD: 1, ALL_IN::SELL: 8, ECON::BUY: 27, ECON::BUY_XP: 1, ECON::ITEM: 2, ECON::MOVE_BENCH: 2, ECON::MOVE_BOARD: 23, ECON::OTHER: 1, ECON::PASS: 10, ECON::SELL: 16, FAST8::BUY: 34, FAST8::BUY_XP: 17, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 8, FAST8::PASS: 1, FAST8::SELL: 25, LOSS_STREAK::BUY: 5, LOSS_STREAK::MOVE_BENCH: 2, LOSS_STREAK::SELL: 3, STABILIZE::BUY: 29, STABILIZE::BUY_XP: 4, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 9, STABILIZE::MOVE_BOARD: 4, STABILIZE::PASS: 5, STABILIZE::SELL: 19
- Jogador 8 — recompensas por ação: BUY: média 0.2873 (n=104), BUY_XP: média -0.0364 (n=22), ITEM: média 0.1871 (n=7), MOVE_BENCH: média 0.1433 (n=15), MOVE_BOARD: média -0.0083 (n=36), OTHER: média -0.0200 (n=1), PASS: média -0.0725 (n=16), SELL: média -0.2414 (n=71)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 14:28:25 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | ? | 14:28:27 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | ? | 14:28:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 14:28:31 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 14:28:32 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 14:28:32 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-1 | 14:28:33 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 14:28:34 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 14:28:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 14:28:36 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 1-2 | 14:28:38 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-2 | 14:28:39 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 14:28:39 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 14:28:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-2 | 14:28:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 14:28:46 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 14:28:47 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 14:28:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 14:28:55 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 14:28:55 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 1-4 | 14:28:56 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 14:28:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-4 | 14:28:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-1 | 14:29:05 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 14:29:05 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.1300 |  |
| Jogador 1 | 2-1 | 14:29:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 14:29:06 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-1 | 14:29:07 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.2800 |  |
| Jogador 1 | 2-1 | 14:29:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 14:29:08 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1700 |  |
| Jogador 1 | 2-1 | 14:29:08 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-1 | 14:29:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-2 | 14:29:15 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 1 | 2-2 | 14:29:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 14:29:16 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-2 | 14:29:18 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1800 |  |
| Jogador 1 | 2-2 | 14:29:18 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 1 | 2-2 | 14:29:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 14:29:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 14:29:28 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 2-3 | 14:29:29 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3600 |  |
| Jogador 1 | 2-3 | 14:29:30 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 2-3 | 14:29:30 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 14:29:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 14:29:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-4 | 14:29:43 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Ornn | 1.0200 |  |
| Jogador 1 | 2-4 | 14:29:43 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Ornn | 0.3300 |  |
| Jogador 1 | 2-4 | 14:29:43 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 1 | 2-4 | 14:29:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 2-4 | 14:29:44 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 14:29:45 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 2-4 | 14:29:46 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 14:29:46 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 2-4 | 14:29:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 14:29:57 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 2-5 | 14:29:58 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 2-5 | 14:29:58 | MOVE Bench -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 1 | 2-5 | 14:29:59 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 1 | 2-5 | 14:29:59 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 2-5 | 14:30:00 | MOVE Board -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 14:30:00 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 14:30:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 14:30:14 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 2-6 | 14:30:14 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 1 | 2-6 | 14:30:15 | MOVE Bench -> Board: Shen (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 1 | 2-6 | 14:30:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 14:30:31 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Inferno | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 1 | 2-7 | 14:30:31 | MOVE Bench -> Board: Shen (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Inferno | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 1 | 2-7 | 14:30:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 1 | 2-7 | 14:30:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 2-7 | 14:30:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 2-7 | 14:30:33 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 14:30:34 | MOVE Board -> Board: Akali (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 2-7 | 14:30:34 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 2-7 | 14:30:35 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-1 | 14:30:51 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 3-1 | 14:30:52 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 3-1 | 14:30:53 | MOVE Board -> Board: Shen (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-1 | 14:30:54 | MOVE Board -> Board: Xayah (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 14:30:54 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 14:30:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-2 | 14:31:14 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-2 | 14:31:15 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 3-2 | 14:31:16 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 1 | 3-2 | 14:31:16 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 14:31:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-3 | 14:31:37 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 3-3 | 14:31:38 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 3-3 | 14:31:38 | VENDEU: Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 14:31:39 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 1 | 3-3 | 14:31:39 | VENDEU: Caitlyn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-3 | 14:31:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 14:31:40 | MOVE Board -> Board: Ezreal (i:8.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-3 | 14:31:41 | MOVE Board -> Board: Xayah (i:2.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 14:31:41 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-4 | 14:32:02 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.7700 |  |
| Jogador 1 | 3-4 | 14:32:02 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 3-4 | 14:32:03 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 1 | 3-4 | 14:32:04 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | 0.3700 |  |
| Jogador 1 | 3-4 | 14:32:04 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-4 | 14:32:05 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 3-4 | 14:32:05 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-4 | 14:32:06 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-4 | 14:32:06 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-5 | 14:32:28 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Inferno | DA_KogMaw18_AD | 0.7400 |  |
| Jogador 1 | 3-5 | 14:32:29 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 1 | 3-5 | 14:32:29 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 1 | 3-5 | 14:32:30 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-5 | 14:32:30 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 3-5 | 14:32:31 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 3-5 | 14:32:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 3-5 | 14:32:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 1 | Inferno | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 3-5 | 14:32:32 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 1 | Inferno | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 1 | 3-6 | 14:32:55 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Inferno | DA_KogMaw18_AD | 0.7300 |  |
| Jogador 1 | 3-6 | 14:32:56 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 1 | 3-6 | 14:32:57 | VENDEU: Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 3-6 | 14:32:57 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.6500 |  |
| Jogador 1 | 3-6 | 14:32:58 | MOVE Board -> Board: Xayah (i:2.0) <-> Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 3-6 | 14:32:58 | MOVE Board -> Board: Ezreal (i:8.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-6 | 14:32:59 | MOVE Board -> Board: Akali (i:4.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-6 | 14:32:59 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.2900 |  |
| Jogador 1 | 3-6 | 14:33:00 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-7 | 14:33:24 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 1 | 3-7 | 14:33:25 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 1 | 3-7 | 14:33:25 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 1 | 3-7 | 14:33:26 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-7 | 14:33:26 | MOVE Board -> Board: Xayah (i:2.0) <-> Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-7 | 14:33:27 | MOVE Board -> Board: Ezreal (i:8.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 1 | 3-7 | 14:33:28 | MOVE Board -> Board: Xayah (i:2.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-7 | 14:33:29 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-7 | 14:33:29 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 14:33:59 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 4-1 | 14:34:00 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Inferno | DA_KogMaw18_AD | 0.6700 |  |
| Jogador 1 | 4-1 | 14:34:00 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Inferno | DA_KogMaw18_AD | -0.3400 |  |
| Jogador 1 | 4-1 | 14:34:01 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Inferno | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 1 | 4-1 | 14:34:01 | MOVE Board -> Board: Xayah (i:2.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 4-1 | 14:34:02 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-1 | 14:34:02 | MOVE Board -> Board: Ezreal (i:8.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-1 | 14:34:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 4-2 | 14:34:33 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 4-2 | 14:34:33 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Inferno | DA_KogMaw18_AD | -0.3200 |  |
| Jogador 1 | 4-2 | 14:34:34 | VENDEU: Sivir (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Inferno | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 1 | 4-2 | 14:34:34 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Inferno | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 1 | 4-2 | 14:34:35 | MOVE Board -> Board: Xayah (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Inferno | DA_KogMaw18_AD | -0.3500 |  |
| Jogador 1 | 4-2 | 14:34:35 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-2 | 14:34:36 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Inferno | DA_KogMaw18_AD | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-3 | 14:35:06 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 41 | 3 | Inferno | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 1 | 4-3 | 14:35:06 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 3 | Inferno | DA_Fiddlesticks18 | 0.8400 |  |
| Jogador 1 | 4-3 | 14:35:07 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 3 | Inferno | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 1 | 4-3 | 14:35:08 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 3 | Inferno | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 1 | 4-3 | 14:35:08 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 40 | 3 | Inferno | DA_18_Akali_AD | -0.4900 |  |
| Jogador 1 | 4-3 | 14:35:09 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 3 | Inferno | DA_18_Akali_AD | -0.0300 |  |
| Jogador 1 | 4-3 | 14:35:09 | MOVE Board -> Board: Akali (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 3 | Inferno | DA_18_Akali_AD | 0.0300 |  |
| Jogador 1 | 4-3 | 14:35:10 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 38 | 3 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 4-3 | 14:35:10 | MOVE Board -> Board: Xayah (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 3 | Inferno | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 4-4 | 14:35:41 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 3 | Inferno | DA_18_Akali_AD | -0.0300 |  |
| Jogador 1 | 4-4 | 14:35:42 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Inferno | DA_18_Akali_AD | 0.3200 |  |
| Jogador 1 | 4-4 | 14:35:42 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 3 | Inferno | DA_18_Akali_AD | -0.0300 |  |
| Jogador 1 | 4-4 | 14:35:43 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Inferno | DA_18_Akali_AD | 0.1200 |  |
| Jogador 1 | 4-4 | 14:35:43 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Inferno | DA_18_Akali_AD | -0.0500 |  |
| Jogador 1 | 4-4 | 14:35:44 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Inferno | DA_18_Akali_AD | -0.1600 |  |
| Jogador 1 | 4-4 | 14:35:44 | MOVE Board -> Board: Akali (i:4.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Inferno | DA_18_Akali_AD | 0.2000 |  |
| Jogador 1 | 4-4 | 14:35:45 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Inferno | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 4-4 | 14:35:45 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 4-5 | 14:36:21 | VENDEU: Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 4-5 | 14:36:21 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Inferno | DA_CrimsonRaptor18 | 1.0200 |  |
| Jogador 1 | 4-5 | 14:36:22 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Inferno | DA_CrimsonRaptor18 | 0.1200 |  |
| Jogador 1 | 4-5 | 14:36:22 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 48 | 4 | Inferno | DA_CrimsonRaptor18 | -0.1500 |  |
| Jogador 1 | 4-5 | 14:36:23 | VENDEU: Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Inferno | DA_18_Akali_AD | -0.6100 |  |
| Jogador 1 | 4-5 | 14:36:24 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Inferno | DA_KogMaw18_AD | 1.0200 |  |
| Jogador 1 | 4-5 | 14:36:24 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Inferno | DA_KogMaw18_AD | 0.5000 |  |
| Jogador 1 | 4-5 | 14:36:25 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 48 | 4 | Inferno | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 1 | 4-5 | 14:36:25 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 45 | 4 | Inferno | DA_KogMaw18_AD | 0.4100 |  |
| Jogador 1 | 4-6 | 14:37:03 | VENDEU: Kog'Maw (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 4 | Inferno | DA_KogMaw18_AD | -0.7300 |  |
| Jogador 1 | 4-6 | 14:37:03 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 60 | 4 | Inferno | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 1 | 4-6 | 14:37:04 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 4 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 4-6 | 14:37:04 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 4 | Inferno | DA_KogMaw18_AD | 1.0800 |  |
| Jogador 1 | 4-6 | 14:37:05 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 62 | 4 | Inferno | DA_KogMaw18_AD | 0.4400 |  |
| Jogador 1 | 4-6 | 14:37:05 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 62 | 4 | Inferno | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 1 | 4-6 | 14:37:06 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Inferno | DA_KogMaw18_AD | 0.4200 |  |
| Jogador 1 | 4-6 | 14:37:06 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-6 | 14:37:07 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 55 | 4 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-7 | 14:37:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Inferno | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 4-7 | 14:37:43 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Inferno | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 4-7 | 14:37:44 | VENDEU: Xayah (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 69 | 5 | Inferno | DA_KogMaw18_AD | -0.7200 |  |
| Jogador 1 | 4-7 | 14:37:45 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Inferno | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 4-7 | 14:37:45 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-7 | 14:37:46 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Inferno | DA_KogMaw18_AD | 1.0800 |  |
| Jogador 1 | 4-7 | 14:37:46 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Inferno | DA_KogMaw18_AD | 0.4700 |  |
| Jogador 1 | 4-7 | 14:37:47 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Inferno | DA_KogMaw18_AD | 0.5600 |  |
| Jogador 1 | 4-7 | 14:37:47 | MOVE Board -> Board: Shen (i:8.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 5-1 | 14:38:24 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Inferno | DA_KogMaw18_AD | 0.4800 |  |
| Jogador 1 | 5-1 | 14:38:25 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Inferno | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 1 | 5-1 | 14:38:25 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 5-1 | 14:38:26 | MOVE Board -> Board: Akali (i:2.0) <-> Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 5-1 | 14:38:26 | MOVE Board -> Board: Shen (i:8.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 5-1 | 14:38:27 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Inferno | DA_KogMaw18_AD | -0.5100 |  |
| Jogador 2 | ? | 14:28:25 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | ? | 14:28:27 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | ? | 14:28:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 14:28:31 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 14:28:32 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 14:28:32 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 1-1 | 14:28:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 14:28:36 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 1-2 | 14:28:38 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 14:28:39 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 14:28:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 14:28:43 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 14:28:46 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 14:28:47 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 14:28:47 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-3 | 14:28:48 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-3 | 14:28:49 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 14:28:49 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 14:28:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 14:28:55 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 14:28:55 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 14:28:56 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 14:28:56 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 14:28:57 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 1-4 | 14:28:57 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 1-4 | 14:28:58 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-4 | 14:28:58 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 1-4 | 14:28:59 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 14:29:05 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 2-1 | 14:29:05 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 2-1 | 14:29:06 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-1 | 14:29:06 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-1 | 14:29:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 14:29:07 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 14:29:08 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-1 | 14:29:08 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-1 | 14:29:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 14:29:15 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-2 | 14:29:16 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 2-2 | 14:29:16 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-2 | 14:29:18 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-2 | 14:29:18 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-2 | 14:29:19 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-2 | 14:29:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-2 | 14:29:20 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 2-2 | 14:29:20 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 14:29:28 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 2-3 | 14:29:29 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 2-3 | 14:29:30 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 14:29:30 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 14:29:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-4 | 14:29:43 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.3400 |  |
| Jogador 2 | 2-4 | 14:29:43 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 2-4 | 14:29:43 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-4 | 14:29:44 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.3400 |  |
| Jogador 2 | 2-4 | 14:29:44 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 2-4 | 14:29:45 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 14:29:46 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.6400 |  |
| Jogador 2 | 2-4 | 14:29:46 | MOVE Bench -> Board: Vi (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 2-4 | 14:29:47 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.4100 |  |
| Jogador 2 | 2-5 | 14:29:57 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.9000 |  |
| Jogador 2 | 2-5 | 14:29:58 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 2-5 | 14:29:58 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-5 | 14:29:59 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 14:29:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 14:30:00 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-5 | 14:30:00 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 14:30:01 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 14:30:01 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.3400 |  |
| Jogador 2 | 2-6 | 14:30:14 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | 0.6300 |  |
| Jogador 2 | 2-6 | 14:30:14 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 2-6 | 14:30:15 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 2-6 | 14:30:15 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-6 | 14:30:16 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-6 | 14:30:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-6 | 14:30:17 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 2-6 | 14:30:17 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-6 | 14:30:17 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 14:30:31 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 2-7 | 14:30:31 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 2-7 | 14:30:31 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 2-7 | 14:30:32 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 2-7 | 14:30:33 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 2-7 | 14:30:33 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.4600 |  |
| Jogador 2 | 2-7 | 14:30:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 14:30:34 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 2-7 | 14:30:35 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 3-1 | 14:30:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 3-1 | 14:30:52 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 3-1 | 14:30:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-1 | 14:30:54 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 14:30:54 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.4300 |  |
| Jogador 2 | 3-1 | 14:30:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 14:30:55 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-1 | 14:30:55 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.2100 |  |
| Jogador 2 | 3-1 | 14:30:56 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 3-2 | 14:31:14 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-2 | 14:31:15 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-2 | 14:31:16 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-2 | 14:31:16 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 3-2 | 14:31:17 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-2 | 14:31:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 14:31:18 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 3-2 | 14:31:19 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.4900 |  |
| Jogador 2 | 3-2 | 14:31:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 14:31:37 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 14:31:38 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | 0.4500 |  |
| Jogador 2 | 3-3 | 14:31:38 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.2600 |  |
| Jogador 2 | 3-3 | 14:31:39 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-3 | 14:31:39 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.7900 |  |
| Jogador 2 | 3-3 | 14:31:40 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-3 | 14:31:40 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Veigar | -0.4900 |  |
| Jogador 2 | 3-3 | 14:31:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 3-3 | 14:31:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-4 | 14:32:02 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 3-4 | 14:32:02 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 3-4 | 14:32:03 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 3-4 | 14:32:04 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-4 | 14:32:04 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 3-4 | 14:32:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-4 | 14:32:05 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 3-4 | 14:32:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-4 | 14:32:06 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -1.0200 |  |
| Jogador 2 | 3-5 | 14:32:28 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-5 | 14:32:29 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 3-5 | 14:32:29 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-5 | 14:32:30 | VENDEU: Zyra (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-5 | 14:32:30 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 3-5 | 14:32:31 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 3-5 | 14:32:31 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.3700 |  |
| Jogador 2 | 3-5 | 14:32:31 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-5 | 14:32:32 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-6 | 14:32:55 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Tristana | 0.7500 |  |
| Jogador 2 | 3-6 | 14:32:56 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_18_Tristana | 0.2700 |  |
| Jogador 2 | 3-6 | 14:32:57 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Tristana | 0.1000 |  |
| Jogador 2 | 3-6 | 14:32:57 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_Veigar | -0.6200 |  |
| Jogador 2 | 3-6 | 14:32:58 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-6 | 14:32:58 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 3-6 | 14:32:59 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-6 | 14:32:59 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-6 | 14:33:00 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-7 | 14:33:24 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 3-7 | 14:33:25 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-7 | 14:33:25 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 3-7 | 14:33:26 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 3-7 | 14:33:26 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 3-7 | 14:33:27 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 3-7 | 14:33:28 | MOVE Board -> Board: Azir (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-7 | 14:33:29 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-7 | 14:33:29 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-1 | 14:33:59 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_Veigar | 0.8500 |  |
| Jogador 2 | 4-1 | 14:34:00 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_Veigar | 0.3500 |  |
| Jogador 2 | 4-1 | 14:34:00 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-1 | 14:34:01 | MOVE Board -> Board: Rakan (i:4.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-1 | 14:34:01 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 4-1 | 14:34:02 | MOVE Board -> Board: Azir (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-1 | 14:34:02 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-1 | 14:34:03 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-2 | 14:34:33 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_18_Veigar | 0.3200 |  |
| Jogador 2 | 4-2 | 14:34:33 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Colosso | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 4-2 | 14:34:34 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-2 | 14:34:34 | MOVE Board -> Board: Rakan (i:4.0) <-> Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 4-2 | 14:34:35 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Colosso | DA_18_Veigar | -0.3200 |  |
| Jogador 2 | 4-3 | 14:35:06 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-3 | 14:35:06 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Colosso | DA_18_Veigar | 0.3900 |  |
| Jogador 2 | 4-3 | 14:35:07 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-3 | 14:35:08 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-3 | 14:35:08 | MOVE Board -> Board: Azir (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-3 | 14:35:09 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-3 | 14:35:09 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Colosso | DA_18_Veigar | -0.2100 |  |
| Jogador 2 | 4-3 | 14:35:10 | MOVE Board -> Board: Rakan (i:4.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-3 | 14:35:10 | MOVE Board -> Board: Sejuani (i:4.0) <-> Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-4 | 14:35:41 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 14 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-4 | 14:35:42 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 11 | 0 | Colosso | DA_18_Veigar | 0.8400 |  |
| Jogador 2 | 4-4 | 14:35:42 | VENDEU: Ezreal (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 15 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-4 | 14:35:43 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 12 | 0 | Colosso | DA_18_Veigar | 0.8300 |  |
| Jogador 2 | 4-4 | 14:35:43 | VENDEU: Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 16 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-4 | 14:35:44 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 14 | 0 | Colosso | DA_18_Veigar | 0.3200 |  |
| Jogador 2 | 4-4 | 14:35:44 | MOVE Board -> Board: Azir (i:6.0) <-> Veigar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 14 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-4 | 14:35:45 | MOVE Board -> Board: Veigar (i:4.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 14 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 4-4 | 14:35:45 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 14 | 0 | Colosso | DA_18_Veigar | -0.3200 |  |
| Jogador 2 | 4-5 | 14:36:21 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Colosso | DA_18_Veigar | -0.5500 |  |
| Jogador 2 | 4-5 | 14:36:21 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 23 | 1 | Colosso | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 4-5 | 14:36:22 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 26 | 1 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-5 | 14:36:22 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 25 | 1 | Colosso | DA_18_Veigar | 0.3700 |  |
| Jogador 2 | 4-5 | 14:36:23 | VENDEU: Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 26 | 1 | Colosso | DA_18_Veigar | -0.7200 |  |
| Jogador 2 | 4-5 | 14:36:24 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-5 | 14:36:24 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 26 | 1 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-5 | 14:36:25 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 25 | 1 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-5 | 14:36:25 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 25 | 1 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-6 | 14:37:03 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-6 | 14:37:03 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 34 | 2 | Colosso | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-6 | 14:37:04 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 4-6 | 14:37:04 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Colosso | DA_18_Veigar | -0.2000 |  |
| Jogador 2 | 4-6 | 14:37:05 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-6 | 14:37:05 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Colosso | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 4-6 | 14:37:06 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Colosso | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-6 | 14:37:06 | COMPROU: Varus (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 34 | 2 | Colosso | DA_18_Veigar | -0.2600 |  |
| Jogador 2 | 4-6 | 14:37:07 | VENDEU: Varus (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 2 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-7 | 14:37:43 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Colosso | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 4-7 | 14:37:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Colosso | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-7 | 14:37:44 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 41 | 3 | Colosso | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 4-7 | 14:37:45 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Colosso | DA_18_Veigar | -0.7200 |  |
| Jogador 2 | 4-7 | 14:37:45 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 39 | 3 | Colosso | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 4-7 | 14:37:46 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Colosso | DA_18_Veigar | -0.4700 |  |
| Jogador 2 | 4-7 | 14:37:46 | COMPROU: Lux (Sabugueiro) (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 3 | Colosso | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 4-7 | 14:37:47 | VENDEU: Lux (Sabugueiro) (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Colosso | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-7 | 14:37:47 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 40 | 3 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 5-1 | 14:38:24 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-1 | 14:38:25 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 4 | Colosso | DA_18_Veigar | 0.4200 |  |
| Jogador 2 | 5-1 | 14:38:25 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 5-1 | 14:38:26 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 4 | Colosso | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 5-1 | 14:38:26 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Colosso | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 5-1 | 14:38:27 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 4 | Colosso | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 5-1 | 14:38:27 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Colosso | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 5-1 | 14:38:28 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Colosso | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 5-1 | 14:38:28 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 5-2 | 14:39:12 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Colosso | DA_18_Azir | 1.0800 |  |
| Jogador 2 | 5-2 | 14:39:12 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 5 | Colosso | DA_18_Azir | 1.0800 |  |
| Jogador 2 | 5-2 | 14:39:13 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 5 | Colosso | DA_18_Azir | 0.4500 |  |
| Jogador 2 | 5-2 | 14:39:13 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 57 | 5 | Colosso | DA_18_Azir | 0.1000 |  |
| Jogador 2 | 5-2 | 14:39:14 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 54 | 5 | Colosso | DA_18_Azir | 0.8500 |  |
| Jogador 2 | 5-2 | 14:39:14 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 5 | Colosso | DA_18_Azir | 0.1500 |  |
| Jogador 2 | 5-2 | 14:39:14 | MOVE Bench -> Board: Amumu (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 51 | 5 | Colosso | DA_18_Azir | 0.4600 |  |
| Jogador 2 | 5-2 | 14:39:15 | MOVE Board -> Board: Amumu (i:8.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 5 | Colosso | DA_18_Azir | -0.0100 |  |
| Jogador 2 | 5-2 | 14:39:15 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 51 | 5 | Colosso | DA_18_Azir | -0.0100 |  |
| Jogador 2 | 5-3 | 14:39:58 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Colosso | DA_18_Azir | 0.5000 |  |
| Jogador 2 | 5-3 | 14:39:59 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Colosso | DA_18_Azir | 0.6200 |  |
| Jogador 2 | 5-3 | 14:39:59 | VENDEU: Krugue (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Colosso | DA_18_Azir | -0.0700 |  |
| Jogador 2 | 5-3 | 14:40:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Colosso | DA_18_Azir | 0.4500 |  |
| Jogador 2 | 5-3 | 14:40:00 | VENDEU: Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Colosso | DA_18_Azir | -0.7300 |  |
| Jogador 2 | 5-3 | 14:40:01 | COMPROU: Alune (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Colosso | DA_18_Azir | 0.2500 |  |
| Jogador 2 | 5-3 | 14:40:01 | MOVE Board -> Board: Tristana (i:6.0) <-> Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Colosso | DA_18_Azir | 0.0400 |  |
| Jogador 2 | 5-3 | 14:40:02 | MOVE Board -> Board: Amumu (i:8.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Colosso | DA_18_Azir | -0.0100 |  |
| Jogador 2 | 5-3 | 14:40:02 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Colosso | DA_18_Azir | -0.0100 |  |
| Jogador 2 | 5-4 | 14:40:45 | VENDEU: Azir (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Colosso | DA_18_Alune | -0.7300 |  |
| Jogador 2 | 5-4 | 14:40:45 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Colosso | DA_18_Alune | -0.0700 |  |
| Jogador 2 | 5-4 | 14:40:45 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Colosso | DA_18_Alune | -0.0300 |  |
| Jogador 2 | 5-4 | 14:40:46 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Colosso | DA_18_Alune | -0.1700 |  |
| Jogador 2 | 5-4 | 14:40:48 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Colosso | DA_18_Alune | -0.0100 |  |
| Jogador 2 | 5-4 | 14:40:48 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Colosso | DA_18_Alune | -0.2700 |  |
| Jogador 2 | 5-4 | 14:40:48 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Colosso | DA_18_Alune | 0.0200 |  |
| Jogador 2 | 5-4 | 14:40:49 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Colosso | DA_18_Alune | -0.2700 |  |
| Jogador 2 | 5-4 | 14:40:49 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Colosso | DA_18_Alune | -0.0700 |  |
| Jogador 2 | 5-5 | 14:41:33 | VENDEU: Kayle (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Colosso | DA_18_Alune | 0.0200 |  |
| Jogador 2 | 5-5 | 14:41:33 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Colosso | DA_18_Alune | 0.4200 |  |
| Jogador 2 | 5-5 | 14:41:34 | VENDEU: Alune (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 5-5 | 14:41:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Colosso | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 5-5 | 14:41:35 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 5-5 | 14:41:35 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 5-5 | 14:41:36 | VENDEU: Sett (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-5 | 14:41:36 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Colosso | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 5-5 | 14:41:36 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 3 | ? | 14:28:25 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | ? | 14:28:27 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | ? | 14:28:27 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | ? | 14:28:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 14:28:31 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 14:28:32 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 14:28:32 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-1 | 14:28:33 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 1-1 | 14:28:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 14:28:36 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-2 | 14:28:38 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 14:28:39 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 14:28:39 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 14:28:40 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-2 | 14:28:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 14:28:43 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 1-3 | 14:28:46 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 14:28:47 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 14:28:47 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 14:28:48 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 14:28:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 14:28:55 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 1-4 | 14:28:55 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 1-4 | 14:28:56 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 14:28:56 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 14:28:57 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 14:28:57 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 1-4 | 14:28:58 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-4 | 14:28:58 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 1-4 | 14:28:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-1 | 14:29:05 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-1 | 14:29:05 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 14:29:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 14:29:15 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-2 | 14:29:16 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 2-2 | 14:29:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-2 | 14:29:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 14:29:28 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-3 | 14:29:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 2-3 | 14:29:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 14:29:43 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 2-4 | 14:29:43 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-4 | 14:29:43 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 14:29:44 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 2-4 | 14:29:44 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 2-4 | 14:29:45 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 2-4 | 14:29:46 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 2-4 | 14:29:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-4 | 14:29:47 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.1800 |  |
| Jogador 3 | 2-5 | 14:29:57 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 1.0500 |  |
| Jogador 3 | 2-5 | 14:29:58 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 1.0500 |  |
| Jogador 3 | 2-5 | 14:29:58 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 2-5 | 14:29:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 2-5 | 14:29:59 | MOVE Bench -> Board: Diana (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.4000 |  |
| Jogador 3 | 2-5 | 14:30:00 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.3200 |  |
| Jogador 3 | 2-5 | 14:30:00 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-5 | 14:30:01 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-5 | 14:30:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 14:30:14 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-6 | 14:30:14 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-6 | 14:30:15 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | 0.3100 |  |
| Jogador 3 | 2-6 | 14:30:15 | MOVE Board -> Board: Yorick (i:4.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 14:30:16 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 14:30:16 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 14:30:31 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_SparringGloves -> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 2-7 | 14:30:31 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Akali_AD | 0.1900 |  |
| Jogador 3 | 2-7 | 14:30:31 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 14:30:32 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-7 | 14:30:33 | MOVE Board -> Board: Yorick (i:4.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 14:30:33 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-7 | 14:30:34 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-7 | 14:30:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 14:30:51 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Akali_AD | 0.7400 |  |
| Jogador 3 | 3-1 | 14:30:52 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 3-1 | 14:30:53 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Akali_AD | -0.2500 |  |
| Jogador 3 | 3-1 | 14:30:54 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 14:30:54 | MOVE Board -> Board: Akali (i:4.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-1 | 14:30:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-2 | 14:31:14 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Akali_AD | 0.6600 |  |
| Jogador 3 | 3-2 | 14:31:15 | COMPROU: Sivir (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Akali_AD | -0.2600 |  |
| Jogador 3 | 3-2 | 14:31:16 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-2 | 14:31:16 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 14:31:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 14:31:37 | VENDEU: Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_18_Akali_AD | -0.4200 |  |
| Jogador 3 | 3-3 | 14:31:38 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Akali_AD | 0.7100 |  |
| Jogador 3 | 3-3 | 14:31:38 | MOVE Board -> Board: Akali (i:4.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 14:31:39 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 14:31:39 | MOVE Board -> Board: Yorick (i:4.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-3 | 14:31:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 14:32:02 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-4 | 14:32:02 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Colosso | DA_18_Akali_AD | 0.7500 |  |
| Jogador 3 | 3-4 | 14:32:03 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Colosso | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 3-4 | 14:32:04 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 14:32:04 | MOVE Board -> Board: Diana (i:6.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 14:32:05 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-4 | 14:32:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 14:32:28 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_18_Akali_AD | 0.7000 |  |
| Jogador 3 | 3-5 | 14:32:29 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Colosso | DA_18_Akali_AD | -0.2500 |  |
| Jogador 3 | 3-5 | 14:32:29 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Colosso | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-5 | 14:32:30 | MOVE Board -> Board: Akali (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 14:32:30 | MOVE Board -> Board: Diana (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-5 | 14:32:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 14:32:55 | VENDEU: Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Colosso | DA_18_Akali_AD | -0.1200 |  |
| Jogador 3 | 3-6 | 14:32:56 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Colosso | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 3-6 | 14:32:57 | VENDEU: Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 1 | Colosso | DA_18_Akali_AD | -0.7500 |  |
| Jogador 3 | 3-6 | 14:32:57 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Colosso | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 3-6 | 14:32:58 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 14:32:58 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Colosso | DA_18_Akali_AD | -0.6600 |  |
| Jogador 3 | 3-6 | 14:32:59 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-7 | 14:33:24 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Colosso | DA_18_Akali_AD | 0.1800 |  |
| Jogador 3 | 3-7 | 14:33:25 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Colosso | DA_18_Akali_AD | 0.1300 |  |
| Jogador 3 | 3-7 | 14:33:25 | VENDEU: Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Colosso | DA_18_Akali_AD | -0.5800 |  |
| Jogador 3 | 3-7 | 14:33:26 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Colosso | DA_18_Akali_AD | 0.7700 |  |
| Jogador 3 | 3-7 | 14:33:26 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Diana (i:6.0) (tabuleiro slot 25) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Colosso | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 3-7 | 14:33:27 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Colosso | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 3-7 | 14:33:28 | VENDEU: Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-7 | 14:33:29 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Colosso | DA_18_Akali_AD | 0.7700 |  |
| Jogador 3 | 3-7 | 14:33:29 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 14:33:59 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-1 | 14:34:00 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Colosso | DA_18_Akali_AD | 0.7800 |  |
| Jogador 3 | 4-1 | 14:34:00 | VENDEU: Sivir (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 4-1 | 14:34:01 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Colosso | DA_18_Akali_AD | 0.0300 |  |
| Jogador 3 | 4-1 | 14:34:01 | VENDEU: Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-1 | 14:34:02 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 4-1 | 14:34:02 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 14:34:03 | MOVE Bench -> Board: Vi (i:6.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_18_Akali_AD | -0.6600 |  |
| Jogador 3 | 4-1 | 14:34:03 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 4-2 | 14:34:33 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 4 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-2 | 14:34:33 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-2 | 14:34:34 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 4 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-2 | 14:34:34 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-2 | 14:34:35 | VENDEU: Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 4 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-2 | 14:34:35 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_18_Akali_AD | -0.1200 |  |
| Jogador 3 | 4-2 | 14:34:36 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 14:34:36 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-2 | 14:34:37 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_18_Akali_AD | -0.0800 |  |
| Jogador 3 | 4-3 | 14:35:06 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-3 | 14:35:06 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Colosso | DA_18_Akali_AD | -0.2700 |  |
| Jogador 3 | 4-3 | 14:35:07 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-3 | 14:35:08 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Colosso | DA_18_Akali_AD | -0.2800 |  |
| Jogador 3 | 4-3 | 14:35:08 | MOVE Board -> Board: Akali (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 14:35:09 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-3 | 14:35:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Colosso | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 4-4 | 14:35:41 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-4 | 14:35:42 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Colosso | DA_KogMaw18_AD | 0.8900 |  |
| Jogador 3 | 4-4 | 14:35:42 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 3 | 4-4 | 14:35:43 | MOVE Board -> Board: Diana (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 4-4 | 14:35:43 | MOVE Board -> Board: Vi (i:6.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 14:35:44 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_KogMaw18_AD | -0.2400 |  |
| Jogador 3 | 4-5 | 14:36:21 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Colosso | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 3 | 4-5 | 14:36:21 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 87 | 5 | Colosso | DA_Scuttlecrab18 | -0.6000 |  |
| Jogador 3 | 4-5 | 14:36:22 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_Scuttlecrab18 | 0.3300 |  |
| Jogador 3 | 4-5 | 14:36:22 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_Scuttlecrab18 | -0.0500 |  |
| Jogador 3 | 4-5 | 14:36:23 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_Scuttlecrab18 | 0.2800 |  |
| Jogador 3 | 4-5 | 14:36:24 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-5 | 14:36:24 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-5 | 14:36:25 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 4-5 | 14:36:25 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_Scuttlecrab18 | -0.1200 |  |
| Jogador 3 | 4-6 | 14:37:03 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Colosso | DA_Scuttlecrab18 | -0.5900 |  |
| Jogador 3 | 4-6 | 14:37:03 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 94 | 5 | Colosso | DA_Scuttlecrab18 | 0.9700 |  |
| Jogador 3 | 4-6 | 14:37:04 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Colosso | DA_Scuttlecrab18 | 0.9600 |  |
| Jogador 3 | 4-6 | 14:37:04 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Colosso | DA_Scuttlecrab18 | 0.1500 |  |
| Jogador 3 | 4-6 | 14:37:05 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Colosso | DA_Scuttlecrab18 | 0.1000 |  |
| Jogador 3 | 4-6 | 14:37:05 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Colosso | DA_Scuttlecrab18 | -0.1900 |  |
| Jogador 3 | 4-6 | 14:37:06 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Colosso | DA_Scuttlecrab18 | -0.6000 |  |
| Jogador 3 | 4-6 | 14:37:06 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Colosso | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 4-6 | 14:37:07 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-7 | 14:37:43 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Colosso | DA_Scuttlecrab18 | 0.6200 |  |
| Jogador 3 | 4-7 | 14:37:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Colosso | DA_Scuttlecrab18 | 0.2200 |  |
| Jogador 3 | 4-7 | 14:37:44 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Colosso | DA_Scuttlecrab18 | 0.1600 |  |
| Jogador 3 | 4-7 | 14:37:45 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Colosso | DA_Scuttlecrab18 | -0.6000 |  |
| Jogador 3 | 4-7 | 14:37:45 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Colosso | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 4-7 | 14:37:46 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Colosso | DA_Scuttlecrab18 | 0.1500 |  |
| Jogador 3 | 4-7 | 14:37:46 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Colosso | DA_Scuttlecrab18 | -0.2200 |  |
| Jogador 3 | 4-7 | 14:37:47 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-7 | 14:37:47 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-1 | 14:38:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Colosso | DA_Scuttlecrab18 | 0.9700 |  |
| Jogador 3 | 5-1 | 14:38:25 | VENDEU: Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Colosso | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 5-1 | 14:38:25 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_Scuttlecrab18 | 0.4200 |  |
| Jogador 3 | 5-1 | 14:38:26 | MOVE Board -> Board: Akali (i:4.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-1 | 14:38:26 | MOVE Board -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-1 | 14:38:27 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_Scuttlecrab18 | -0.5600 |  |
| Jogador 4 | ? | 14:28:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | ? | 14:28:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | ? | 14:28:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | ? | 14:28:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 14:28:31 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 14:28:32 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 14:28:32 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-1 | 14:28:33 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 1-1 | 14:28:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 14:28:36 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4600 |  |
| Jogador 4 | 1-2 | 14:28:38 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 14:28:39 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 14:28:39 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 14:28:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-2 | 14:28:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 14:28:46 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 14:28:47 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 14:28:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 14:28:55 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 4 | 1-4 | 14:28:55 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 1-4 | 14:28:56 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-4 | 14:28:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 1-4 | 14:28:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-1 | 14:29:05 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 2-1 | 14:29:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 2-1 | 14:29:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-2 | 14:29:15 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 4 | 2-2 | 14:29:16 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-2 | 14:29:16 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-2 | 14:29:18 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-2 | 14:29:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 14:29:19 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 14:29:19 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 14:29:20 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 4 | 2-2 | 14:29:20 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.4100 |  |
| Jogador 4 | 2-3 | 14:29:28 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-3 | 14:29:29 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-3 | 14:29:30 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 4 | 2-3 | 14:29:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-3 | 14:29:31 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-3 | 14:29:32 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 2-3 | 14:29:32 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 2-3 | 14:29:33 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 4 | 2-3 | 14:29:33 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.9500 |  |
| Jogador 4 | 2-4 | 14:29:43 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 1.0000 |  |
| Jogador 4 | 2-4 | 14:29:43 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 2-4 | 14:29:43 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 4 | 2-4 | 14:29:44 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 4 | 2-4 | 14:29:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-4 | 14:29:45 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.6200 |  |
| Jogador 4 | 2-4 | 14:29:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 2-4 | 14:29:46 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 4 | 2-4 | 14:29:47 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 4 | 2-5 | 14:29:57 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 4 | 2-5 | 14:29:58 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 4 | 2-5 | 14:29:58 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.4300 |  |
| Jogador 4 | 2-5 | 14:29:59 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-5 | 14:29:59 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 4 | 2-5 | 14:30:00 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-5 | 14:30:00 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 4 | 2-5 | 14:30:01 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 4 | 2-5 | 14:30:01 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-6 | 14:30:14 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 1.1200 |  |
| Jogador 4 | 2-6 | 14:30:14 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 4 | 2-6 | 14:30:15 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 4 | 2-6 | 14:30:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-6 | 14:30:16 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 4 | 2-6 | 14:30:16 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 2-6 | 14:30:17 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-6 | 14:30:17 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-6 | 14:30:17 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-7 | 14:30:31 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 2-7 | 14:30:31 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 4 | 2-7 | 14:30:31 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 4 | 2-7 | 14:30:32 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-7 | 14:30:33 | MOVE Board -> Board: Karma (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-7 | 14:30:33 | MOVE Board -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 2-7 | 14:30:34 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 14:30:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-1 | 14:30:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 4 | 3-1 | 14:30:52 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-1 | 14:30:53 | MOVE Bench -> Board: Yunara (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | -1.0200 |  |
| Jogador 4 | 3-1 | 14:30:54 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.4600 |  |
| Jogador 4 | 3-1 | 14:30:54 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.4400 |  |
| Jogador 4 | 3-1 | 14:30:55 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.2700 |  |
| Jogador 4 | 3-1 | 14:30:55 | MOVE Board -> Board: Rakan (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-1 | 14:30:55 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-1 | 14:30:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-2 | 14:31:14 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 4 | 3-2 | 14:31:15 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 4 | 3-2 | 14:31:16 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 4 | 3-2 | 14:31:16 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 4 | 3-2 | 14:31:17 | MOVE Bench -> Board: Yunara (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.9400 |  |
| Jogador 4 | 3-2 | 14:31:18 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 3-2 | 14:31:18 | MOVE Bench -> Board: Yunara (i:4.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 4 | 3-2 | 14:31:19 | MOVE Bench -> Board: Yunara (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.9400 |  |
| Jogador 4 | 3-2 | 14:31:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-3 | 14:31:37 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Florescer | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 4 | 3-3 | 14:31:38 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-3 | 14:31:38 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Yunara (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 4 | 3-3 | 14:31:39 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Yunara (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 4 | 3-3 | 14:31:39 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Yunara (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 4 | 3-3 | 14:31:40 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 3-3 | 14:31:40 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 4 | 3-3 | 14:31:41 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 0.5100 |  |
| Jogador 4 | 3-3 | 14:31:41 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 0.5400 |  |
| Jogador 4 | 3-4 | 14:32:02 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-4 | 14:32:02 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Florescer | DA_KogMaw18_AD | 0.4500 |  |
| Jogador 4 | 3-4 | 14:32:03 | MOVE Board -> Board: Master Yi (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-4 | 14:32:04 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 14:32:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-5 | 14:32:28 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 4 | 3-5 | 14:32:29 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Florescer | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 4 | 3-5 | 14:32:29 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Rakan (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Florescer | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 4 | 3-5 | 14:32:30 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Rakan (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Florescer | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 4 | 3-5 | 14:32:30 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Rakan (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Florescer | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 3-5 | 14:32:31 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 3-5 | 14:32:31 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Florescer | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 4 | 3-5 | 14:32:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Florescer | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 3-5 | 14:32:32 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 3-6 | 14:32:55 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 31 | 2 | Florescer | DA_KogMaw18_AD | -0.3100 |  |
| Jogador 4 | 3-6 | 14:32:56 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Florescer | DA_18_MasterYi_AD | 0.7900 |  |
| Jogador 4 | 3-6 | 14:32:57 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Florescer | DA_18_MasterYi_AD | 0.4400 |  |
| Jogador 4 | 3-6 | 14:32:57 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Florescer | DA_18_MasterYi_AD | 0.2500 |  |
| Jogador 4 | 3-6 | 14:32:58 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Florescer | DA_18_MasterYi_AD | 0.0300 |  |
| Jogador 4 | 3-6 | 14:32:58 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 4 | 3-6 | 14:32:59 | MOVE Board -> Board: Sejuani (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Florescer | DA_18_MasterYi_AD | -0.2500 |  |
| Jogador 4 | 3-6 | 14:32:59 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Florescer | DA_18_MasterYi_AD | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-7 | 14:33:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Florescer | DA_18_MasterYi_AD | 0.8400 |  |
| Jogador 4 | 3-7 | 14:33:25 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Florescer | DA_18_MasterYi_AD | 0.1800 |  |
| Jogador 4 | 3-7 | 14:33:25 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Florescer | DA_18_MasterYi_AD | 0.2100 |  |
| Jogador 4 | 3-7 | 14:33:26 | VENDEU: Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 40 | 2 | Florescer | DA_Fiddlesticks18 | -0.4900 |  |
| Jogador 4 | 3-7 | 14:33:26 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 2 | Florescer | DA_Fiddlesticks18 | 0.4900 |  |
| Jogador 4 | 3-7 | 14:33:27 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Florescer | DA_Fiddlesticks18 | -0.2300 |  |
| Jogador 4 | 3-7 | 14:33:28 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Florescer | DA_Fiddlesticks18 | 0.2400 |  |
| Jogador 4 | 3-7 | 14:33:29 | MOVE Board -> Board: Rakan (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Florescer | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 4 | 3-7 | 14:33:29 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Florescer | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 4 | 4-1 | 14:33:59 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Florescer | DA_Fiddlesticks18 | 0.9700 |  |
| Jogador 4 | 4-1 | 14:34:00 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 39 | 3 | Florescer | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 4 | 4-1 | 14:34:00 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 37 | 3 | Florescer | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 4 | 4-1 | 14:34:01 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Florescer | DA_Fiddlesticks18 | 0.3700 |  |
| Jogador 4 | 4-1 | 14:34:01 | VENDEU: Alistar (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 40 | 3 | Florescer | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 4 | 4-1 | 14:34:02 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 3 | Florescer | DA_Fiddlesticks18 | 0.3500 |  |
| Jogador 4 | 4-1 | 14:34:02 | VENDEU: Yunara (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Florescer | DA_Fiddlesticks18 | -0.5800 |  |
| Jogador 4 | 4-1 | 14:34:03 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 39 | 3 | Florescer | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 4 | 4-1 | 14:34:03 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 37 | 3 | Florescer | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 4 | 4-2 | 14:34:33 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Florescer | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 4 | 4-2 | 14:34:33 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 47 | 3 | Florescer | DA_Fiddlesticks18 | 0.9200 |  |
| Jogador 4 | 4-2 | 14:34:34 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Florescer | DA_Fiddlesticks18 | -0.5500 |  |
| Jogador 4 | 4-2 | 14:34:34 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 4 | 4-2 | 14:34:35 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Florescer | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 4 | 4-2 | 14:34:35 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 3 | Florescer | DA_Fiddlesticks18 | -0.5000 |  |
| Jogador 4 | 4-2 | 14:34:36 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Florescer | DA_Fiddlesticks18 | -0.2500 |  |
| Jogador 4 | 4-2 | 14:34:36 | MOVE Bench -> Board: Azir (i:6.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Florescer | DA_Fiddlesticks18 | -0.8800 |  |
| Jogador 4 | 4-2 | 14:34:37 | MOVE Bench -> Board: Rakan (i:2.0) <-> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Florescer | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 4 | 4-3 | 14:35:06 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Florescer | DA_Fiddlesticks18 | 0.9800 |  |
| Jogador 4 | 4-3 | 14:35:06 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Florescer | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 4 | 4-3 | 14:35:07 | COMPROU: Ezreal (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 55 | 4 | Florescer | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 4 | 4-3 | 14:35:08 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 55 | 4 | Florescer | DA_Fiddlesticks18 | 0.5500 |  |
| Jogador 4 | 4-3 | 14:35:08 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Florescer | DA_Fiddlesticks18 | -0.2200 |  |
| Jogador 4 | 4-3 | 14:35:09 | MOVE Board -> Board: Karma (i:2.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Florescer | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 4 | 4-3 | 14:35:09 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Florescer | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 4 | 4-3 | 14:35:10 | MOVE Board -> Board: Sejuani (i:4.0) <-> Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Florescer | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 4 | 4-3 | 14:35:10 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Florescer | DA_Fiddlesticks18 | -0.4800 |  |
| Jogador 4 | 4-4 | 14:35:41 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Florescer | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 4 | 4-4 | 14:35:42 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Florescer | DA_Fiddlesticks18 | 1.1000 |  |
| Jogador 4 | 4-4 | 14:35:42 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 4 | 4-4 | 14:35:43 | MOVE Bench -> Board: Rakan (i:4.0) <-> Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 4 | 4-4 | 14:35:43 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Florescer | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 4 | 4-4 | 14:35:44 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 4 | 4-4 | 14:35:44 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_Fiddlesticks18 | 0.4000 |  |
| Jogador 4 | 4-4 | 14:35:45 | MOVE Board -> Board: Rakan (i:4.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 4 | 4-4 | 14:35:45 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 5 | Florescer | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 5 | ? | 14:28:25 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | ? | 14:28:27 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 5 | ? | 14:28:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 14:28:31 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 14:28:32 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 14:28:32 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-1 | 14:28:33 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 14:28:34 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 14:28:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 14:28:36 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4300 |  |
| Jogador 5 | 1-2 | 14:28:38 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 1-2 | 14:28:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 14:28:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 14:28:47 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 14:28:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 14:28:55 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 14:28:55 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 5 | 1-4 | 14:28:56 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 5 | 1-4 | 14:28:56 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 5 | 1-4 | 14:28:57 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 14:28:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 14:29:05 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-1 | 14:29:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 14:29:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 14:29:15 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 5 | 2-2 | 14:29:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 2-2 | 14:29:16 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 5 | 2-2 | 14:29:18 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 14:29:18 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 5 | 2-2 | 14:29:19 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 14:29:19 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0300 |  |
| Jogador 5 | 2-2 | 14:29:20 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-2 | 14:29:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 14:29:28 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | 0.3100 |  |
| Jogador 5 | 2-3 | 14:29:29 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-3 | 14:29:30 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-3 | 14:29:30 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-3 | 14:29:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 14:29:32 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 14:29:32 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 14:29:33 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | 0.1900 |  |
| Jogador 5 | 2-3 | 14:29:33 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.1800 |  |
| Jogador 5 | 2-4 | 14:29:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2700 |  |
| Jogador 5 | 2-4 | 14:29:43 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-4 | 14:29:43 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-4 | 14:29:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 14:29:44 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-4 | 14:29:45 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.4100 |  |
| Jogador 5 | 2-4 | 14:29:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-4 | 14:29:46 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1000 |  |
| Jogador 5 | 2-4 | 14:29:47 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3600 |  |
| Jogador 5 | 2-5 | 14:29:57 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0200 |  |
| Jogador 5 | 2-5 | 14:29:58 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0200 |  |
| Jogador 5 | 2-5 | 14:29:58 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 14:29:59 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-5 | 14:29:59 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3500 |  |
| Jogador 5 | 2-5 | 14:30:00 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-5 | 14:30:00 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-5 | 14:30:01 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3300 |  |
| Jogador 5 | 2-5 | 14:30:01 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.4900 |  |
| Jogador 5 | 2-6 | 14:30:14 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Cassiopeia | 1.1200 |  |
| Jogador 5 | 2-6 | 14:30:14 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-6 | 14:30:15 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0200 |  |
| Jogador 5 | 2-6 | 14:30:15 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.6000 |  |
| Jogador 5 | 2-6 | 14:30:16 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1700 |  |
| Jogador 5 | 2-6 | 14:30:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-6 | 14:30:17 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.6300 |  |
| Jogador 5 | 2-6 | 14:30:17 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.5700 |  |
| Jogador 5 | 2-6 | 14:30:17 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.1400 |  |
| Jogador 5 | 2-7 | 14:30:31 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2800 |  |
| Jogador 5 | 2-7 | 14:30:31 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Yunara | 0.6800 |  |
| Jogador 5 | 2-7 | 14:30:31 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Yunara | 0.2100 |  |
| Jogador 5 | 2-7 | 14:30:32 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Yunara | 0.1200 |  |
| Jogador 5 | 2-7 | 14:30:33 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Yunara | 0.0100 |  |
| Jogador 5 | 2-7 | 14:30:33 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Yunara | -0.0100 |  |
| Jogador 5 | 2-7 | 14:30:34 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 5 | 2-7 | 14:30:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 2-7 | 14:30:35 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.2500 |  |
| Jogador 5 | 3-1 | 14:30:51 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.7200 |  |
| Jogador 5 | 3-1 | 14:30:52 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.7000 |  |
| Jogador 5 | 3-1 | 14:30:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 5 | 3-1 | 14:30:54 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 3-1 | 14:30:54 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 5 | 3-1 | 14:30:55 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.5300 |  |
| Jogador 5 | 3-1 | 14:30:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-1 | 14:30:55 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 5 | 3-1 | 14:30:56 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 5 | 3-2 | 14:31:14 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 5 | 3-2 | 14:31:15 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 5 | 3-2 | 14:31:16 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 5 | 3-2 | 14:31:16 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 5 | 3-2 | 14:31:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-2 | 14:31:18 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 5 | 3-2 | 14:31:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 5 | 3-2 | 14:31:19 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.5300 |  |
| Jogador 5 | 3-2 | 14:31:19 | MOVE Board -> Board: Teemo (i:4.0) <-> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-3 | 14:31:37 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 3-3 | 14:31:38 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 5 | 3-3 | 14:31:38 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 5 | 3-3 | 14:31:39 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-3 | 14:31:39 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-3 | 14:31:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-4 | 14:32:02 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 5 | 3-4 | 14:32:02 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.4800 |  |
| Jogador 5 | 3-4 | 14:32:03 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 5 | 3-4 | 14:32:04 | MOVE Board -> Board: Yorick (i:2.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-4 | 14:32:04 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 5 | 3-4 | 14:32:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-5 | 14:32:28 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.5900 |  |
| Jogador 5 | 3-5 | 14:32:29 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 3-5 | 14:32:29 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 3-5 | 14:32:30 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 3-5 | 14:32:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-5 | 14:32:31 | VENDEU: Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 5 | 3-5 | 14:32:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-5 | 14:32:31 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.4900 |  |
| Jogador 5 | 3-5 | 14:32:32 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 5 | 3-6 | 14:32:55 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 5 | 3-6 | 14:32:56 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.1700 |  |
| Jogador 5 | 3-6 | 14:32:57 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.3400 |  |
| Jogador 5 | 3-6 | 14:32:57 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 5 | 3-6 | 14:32:58 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 5 | 3-6 | 14:32:58 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-6 | 14:32:59 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-6 | 14:32:59 | MOVE Board -> Board: Veigar (i:2.0) <-> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 5 | 3-6 | 14:33:00 | MOVE Board -> Board: Kobuko (i:2.0) <-> Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-7 | 14:33:24 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.4400 |  |
| Jogador 5 | 3-7 | 14:33:25 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 5 | 3-7 | 14:33:25 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 5 | 3-7 | 14:33:26 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 5 | 3-7 | 14:33:26 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 5 | 3-7 | 14:33:27 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 5 | 3-7 | 14:33:28 | MOVE Bench -> Board: Krugue (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 3-7 | 14:33:29 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.5100 |  |
| Jogador 5 | 3-7 | 14:33:29 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 4-1 | 14:33:59 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.7400 |  |
| Jogador 5 | 4-1 | 14:34:00 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 5 | 4-1 | 14:34:00 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 5 | 4-1 | 14:34:01 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 5 | 4-1 | 14:34:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 4-1 | 14:34:02 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 5 | 4-1 | 14:34:02 | MOVE Bench -> Board: Krugue (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 4-1 | 14:34:03 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 5 | 4-1 | 14:34:03 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 5 | 4-2 | 14:34:33 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 5 | 4-2 | 14:34:33 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 5 | 4-2 | 14:34:34 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-2 | 14:34:34 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 5 | 4-2 | 14:34:35 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 4-2 | 14:34:35 | MOVE Board -> Board: Rammus (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 4-2 | 14:34:36 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-3 | 14:35:06 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.7300 |  |
| Jogador 5 | 4-3 | 14:35:06 | VENDEU: Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 5 | 4-3 | 14:35:07 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.6800 |  |
| Jogador 5 | 4-3 | 14:35:08 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-3 | 14:35:08 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 4-3 | 14:35:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-4 | 14:35:41 | VENDEU: Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 5 | 4-4 | 14:35:42 | COMPROU: Kobuko (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.7300 |  |
| Jogador 5 | 4-4 | 14:35:42 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 5 | 4-4 | 14:35:43 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 4-4 | 14:35:43 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 5 | 4-4 | 14:35:44 | MOVE Board -> Board: Teemo (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-4 | 14:35:44 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 4-4 | 14:35:45 | MOVE Board -> Board: Rammus (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 4-4 | 14:35:45 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Espinhos Negros | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 4-5 | 14:36:21 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Espinhos Negros | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 4-5 | 14:36:21 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.7100 |  |
| Jogador 5 | 4-5 | 14:36:22 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 5 | 4-5 | 14:36:22 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0600 |  |
| Jogador 5 | 4-5 | 14:36:23 | MOVE Board -> Board: Yorick (i:2.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 4-5 | 14:36:24 | MOVE Board -> Board: Krugue (i:6.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 5 | 4-5 | 14:36:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 5 | 4-6 | 14:37:03 | VENDEU: Mamãe Bicuda (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 1 | Espinhos Negros | DA_Sentinel18 | -0.5700 |  |
| Jogador 5 | 4-6 | 14:37:03 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Espinhos Negros | DA_Sentinel18 | 0.2300 |  |
| Jogador 5 | 4-6 | 14:37:04 | VENDEU: Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 1 | Espinhos Negros | DA_Sentinel18 | -0.0300 |  |
| Jogador 5 | 4-6 | 14:37:04 | COMPROU: Aphelios (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Espinhos Negros | DA_Sentinel18 | -0.2100 |  |
| Jogador 5 | 4-6 | 14:37:05 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Espinhos Negros | DA_Sentinel18 | 0.0000 |  |
| Jogador 5 | 4-6 | 14:37:05 | MOVE Board -> Board: Veigar (i:2.0) <-> Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Espinhos Negros | DA_Sentinel18 | -0.0100 |  |
| Jogador 5 | 4-6 | 14:37:06 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Espinhos Negros | DA_Sentinel18 | -0.0300 |  |
| Jogador 5 | 4-7 | 14:37:43 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NeedlesslyLargeRod -> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Espinhos Negros | DA_Sentinel18 | 0.1000 |  |
| Jogador 5 | 4-7 | 14:37:43 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Espinhos Negros | DA_Sentinel18 | 0.1300 |  |
| Jogador 5 | 4-7 | 14:37:44 | VENDEU: Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Espinhos Negros | DA_Sentinel18 | 0.0100 |  |
| Jogador 5 | 4-7 | 14:37:45 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Espinhos Negros | DA_Sentinel18 | 0.7600 |  |
| Jogador 5 | 4-7 | 14:37:45 | VENDEU: Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Espinhos Negros | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 5 | 4-7 | 14:37:46 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Espinhos Negros | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 5 | 4-7 | 14:37:46 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Espinhos Negros | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 5 | 4-7 | 14:37:47 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 4-7 | 14:37:47 | MOVE Board -> Board: Teemo (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-1 | 14:38:24 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 5-1 | 14:38:25 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.8900 |  |
| Jogador 5 | 5-1 | 14:38:25 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Espinhos Negros | DA_KogMaw18_AD | -0.5100 |  |
| Jogador 5 | 5-1 | 14:38:26 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.9700 |  |
| Jogador 5 | 5-1 | 14:38:26 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 5 | 5-1 | 14:38:27 | MOVE Bench -> Board: Kog'Maw (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 5 | 5-1 | 14:38:27 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 41 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.9700 |  |
| Jogador 5 | 5-1 | 14:38:28 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 41 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 5 | 5-1 | 14:38:28 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 40 | 3 | Espinhos Negros | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 5 | 5-2 | 14:39:12 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Espinhos Negros | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 5 | 5-2 | 14:39:12 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 4 | Espinhos Negros | DA_KogMaw18_AD | 0.5300 |  |
| Jogador 5 | 5-2 | 14:39:13 | VENDEU: Teemo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Espinhos Negros | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 5 | 5-2 | 14:39:13 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 4 | Espinhos Negros | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 5-2 | 14:39:14 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 4 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-2 | 14:39:14 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 47 | 4 | Espinhos Negros | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 5-2 | 14:39:14 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 47 | 4 | Espinhos Negros | DA_KogMaw18_AD | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 5-3 | 14:39:58 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Espinhos Negros | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 5 | 5-3 | 14:39:59 | VENDEU: Kobuko (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Espinhos Negros | DA_KogMaw18_AD | -0.7000 |  |
| Jogador 5 | 5-3 | 14:39:59 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Espinhos Negros | DA_KogMaw18_AD | 0.6400 |  |
| Jogador 5 | 5-3 | 14:40:00 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Kog'Maw (i:12.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Espinhos Negros | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 5 | 5-3 | 14:40:00 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Fiddlesticks (i:6.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Espinhos Negros | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 5 | 5-3 | 14:40:01 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-3 | 14:40:01 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Espinhos Negros | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 5 | 5-3 | 14:40:02 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Espinhos Negros | DA_KogMaw18_AD | -0.4700 |  |
| Jogador 5 | 5-4 | 14:40:45 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Espinhos Negros | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 5-4 | 14:40:45 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Espinhos Negros | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 5 | 5-4 | 14:40:45 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Espinhos Negros | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 5-4 | 14:40:46 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Espinhos Negros | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 5 | 5-4 | 14:40:48 | VENDEU: Nidalee (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Espinhos Negros | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 5-4 | 14:40:48 | COMPROU: Ashe (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-4 | 14:40:48 | VENDEU: Ashe (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-4 | 14:40:49 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 65 | 5 | Espinhos Negros | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 5 | 5-4 | 14:40:49 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Espinhos Negros | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 5 | 5-5 | 14:41:33 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Espinhos Negros | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-5 | 14:41:33 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Espinhos Negros | DA_KogMaw18_AD | 0.4500 |  |
| Jogador 5 | 5-5 | 14:41:34 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Espinhos Negros | DA_KogMaw18_AD | -0.6200 |  |
| Jogador 5 | 5-5 | 14:41:34 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Espinhos Negros | DA_KogMaw18_AD | 0.4300 |  |
| Jogador 5 | 5-5 | 14:41:35 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Espinhos Negros | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 5-5 | 14:41:35 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Espinhos Negros | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 5 | 5-5 | 14:41:36 | VENDEU: Nidalee (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Espinhos Negros | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 5-5 | 14:41:36 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Espinhos Negros | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 5 | 5-5 | 14:41:36 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Espinhos Negros | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 6 | ? | 14:28:25 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 14:28:27 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | -0.1500 |  |
| Jogador 6 | ? | 14:28:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 14:28:31 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 14:28:32 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 14:28:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 14:28:36 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2200 |  |
| Jogador 6 | 1-2 | 14:28:38 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 6 | 1-2 | 14:28:39 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 6 | 1-2 | 14:28:39 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 14:28:40 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 14:28:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-2 | 14:28:43 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.5700 |  |
| Jogador 6 | 1-3 | 14:28:46 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0200 |  |
| Jogador 6 | 1-3 | 14:28:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 14:28:55 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 1-4 | 14:28:55 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 6 | 1-4 | 14:28:56 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 6 | 1-4 | 14:28:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 6 | 1-4 | 14:28:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 2-1 | 14:29:05 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-1 | 14:29:05 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-1 | 14:29:06 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-1 | 14:29:06 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-1 | 14:29:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 14:29:15 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-2 | 14:29:16 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-2 | 14:29:16 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-2 | 14:29:18 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 14:29:18 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 14:29:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 14:29:28 | COMPROU: Hecarim (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 6 | 0 | — | DA_18_Tristana | 0.1100 |  |
| Jogador 6 | 2-3 | 14:29:29 | COMPROU: Rakan (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 5 | 0 | — | DA_18_Tristana | 0.1700 |  |
| Jogador 6 | 2-3 | 14:29:30 | COMPROU: Rakan (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 4 | 0 | — | DA_18_Tristana | 0.7400 |  |
| Jogador 6 | 2-3 | 14:29:30 | BUY XP | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 14:29:31 | VENDEU: Shen (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 2 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-3 | 14:29:32 | VENDEU: Kayle (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 4 | 0 | — | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-3 | 14:29:32 | BUY XP | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 14:29:33 | VENDEU: Grompe (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-3 | 14:29:33 | PASSOU TURNO | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 2 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-4 | 14:29:43 | COMPROU: Yorick (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 7 | 0 | Feérico | DA_18_Tristana | 0.8700 |  |
| Jogador 6 | 2-4 | 14:29:43 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | 0.2200 |  |
| Jogador 6 | 2-4 | 14:29:43 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Tristana | -0.1200 |  |
| Jogador 6 | 2-4 | 14:29:44 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | -0.4500 |  |
| Jogador 6 | 2-4 | 14:29:44 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_Tristana | -0.4100 |  |
| Jogador 6 | 2-4 | 14:29:45 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_Tristana | -1.0200 |  |
| Jogador 6 | 2-4 | 14:29:46 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_Tristana | 0.3600 |  |
| Jogador 6 | 2-4 | 14:29:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Tristana | -0.1200 |  |
| Jogador 6 | 2-4 | 14:29:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-5 | 14:29:57 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Tristana | 0.2100 |  |
| Jogador 6 | 2-5 | 14:29:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-5 | 14:29:58 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | -0.4900 |  |
| Jogador 6 | 2-5 | 14:29:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-5 | 14:29:59 | MOVE Bench -> Board: Yorick (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | -0.3000 |  |
| Jogador 6 | 2-5 | 14:30:00 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-5 | 14:30:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-6 | 14:30:14 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | 1.0300 |  |
| Jogador 6 | 2-6 | 14:30:14 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | -1.0200 |  |
| Jogador 6 | 2-6 | 14:30:15 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Tristana | -0.6300 |  |
| Jogador 6 | 2-6 | 14:30:15 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | 0.3600 |  |
| Jogador 6 | 2-6 | 14:30:16 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-6 | 14:30:16 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Tristana | -0.4900 |  |
| Jogador 6 | 2-6 | 14:30:17 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | -1.0200 |  |
| Jogador 6 | 2-6 | 14:30:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-6 | 14:30:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-7 | 14:30:31 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | 0.1000 |  |
| Jogador 6 | 2-7 | 14:30:31 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | 0.2300 |  |
| Jogador 6 | 2-7 | 14:30:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-7 | 14:30:32 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | -0.1000 |  |
| Jogador 6 | 2-7 | 14:30:33 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Tristana | -0.6300 |  |
| Jogador 6 | 2-7 | 14:30:33 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | 0.0100 |  |
| Jogador 6 | 2-7 | 14:30:34 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-7 | 14:30:34 | MOVE Bench -> Board: Ahri (i:8.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | -0.2000 |  |
| Jogador 6 | 2-7 | 14:30:35 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 3-1 | 14:30:51 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Tristana | 0.8400 |  |
| Jogador 6 | 3-1 | 14:30:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 3-1 | 14:30:53 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Tristana | -0.5500 |  |
| Jogador 6 | 3-1 | 14:30:54 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Yorick (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Tristana | 0.1300 |  |
| Jogador 6 | 3-1 | 14:30:54 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Yorick (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Tristana | 0.1600 |  |
| Jogador 6 | 3-1 | 14:30:55 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Yorick (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Tristana | 0.1400 |  |
| Jogador 6 | 3-1 | 14:30:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 3-1 | 14:30:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 3-1 | 14:30:56 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Tristana | -0.6300 |  |
| Jogador 6 | 3-2 | 14:31:14 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | 0.8000 |  |
| Jogador 6 | 3-2 | 14:31:15 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 3-2 | 14:31:16 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_Tristana | 0.0700 |  |
| Jogador 6 | 3-2 | 14:31:16 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_Tristana | 0.0900 |  |
| Jogador 6 | 3-2 | 14:31:17 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_Tristana | 0.4300 |  |
| Jogador 6 | 3-2 | 14:31:18 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | -0.2600 |  |
| Jogador 6 | 3-2 | 14:31:18 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | -0.1200 |  |
| Jogador 6 | 3-2 | 14:31:19 | MOVE Board -> Board: Tristana (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | 0.0900 |  |
| Jogador 6 | 3-2 | 14:31:19 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | -0.0800 |  |
| Jogador 6 | 3-3 | 14:31:37 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_Tristana | 0.2000 |  |
| Jogador 6 | 3-3 | 14:31:38 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | -0.2600 |  |
| Jogador 6 | 3-3 | 14:31:38 | MOVE Board -> Board: Xayah (i:2.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | 0.0500 |  |
| Jogador 6 | 3-3 | 14:31:39 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | 0.0100 |  |
| Jogador 6 | 3-3 | 14:31:39 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-3 | 14:31:40 | MOVE Board -> Board: Tristana (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-3 | 14:31:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-4 | 14:32:02 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_Tristana | 0.2100 |  |
| Jogador 6 | 3-4 | 14:32:02 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | -0.2600 |  |
| Jogador 6 | 3-4 | 14:32:03 | MOVE Board -> Board: Xayah (i:2.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-4 | 14:32:04 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-4 | 14:32:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-5 | 14:32:28 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_Tristana | 0.0100 |  |
| Jogador 6 | 3-5 | 14:32:29 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_Tristana | -0.1300 |  |
| Jogador 6 | 3-5 | 14:32:29 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 3-5 | 14:32:30 | COMPROU: Kobuko (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Tristana | -0.0900 |  |
| Jogador 6 | 3-5 | 14:32:30 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Tristana | -0.1000 |  |
| Jogador 6 | 3-5 | 14:32:31 | MOVE Board -> Board: Ahri (i:8.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Tristana | -0.2700 |  |
| Jogador 6 | 3-5 | 14:32:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-6 | 14:32:55 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_Tristana | 0.4000 |  |
| Jogador 6 | 3-6 | 14:32:56 | COMPROU: Gnar (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | 0.1100 |  |
| Jogador 6 | 3-6 | 14:32:57 | VENDEU: Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 3-6 | 14:32:57 | COMPROU: Leona (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | -0.1400 |  |
| Jogador 6 | 3-6 | 14:32:58 | VENDEU: Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_GnarSmall | 0.0100 |  |
| Jogador 6 | 3-6 | 14:32:58 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_GnarSmall | -0.0400 |  |
| Jogador 6 | 3-6 | 14:32:59 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 3-6 | 14:32:59 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_GnarSmall | -0.0400 |  |
| Jogador 6 | 3-6 | 14:33:00 | VENDEU: Teemo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 3-7 | 14:33:24 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Feérico | DA_18_GnarSmall | -0.0600 |  |
| Jogador 6 | 3-7 | 14:33:25 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Feérico | DA_18_GnarSmall | -0.0800 |  |
| Jogador 6 | 3-7 | 14:33:25 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Feérico | DA_18_GnarSmall | 0.1200 |  |
| Jogador 6 | 3-7 | 14:33:26 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Feérico | DA_18_GnarSmall | 0.1100 |  |
| Jogador 6 | 3-7 | 14:33:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-7 | 14:33:27 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 3-7 | 14:33:28 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 3-7 | 14:33:29 | VENDEU: Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_GnarSmall | -0.3900 |  |
| Jogador 6 | 3-7 | 14:33:29 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_GnarSmall | -0.0800 |  |
| Jogador 6 | 4-1 | 14:33:59 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Feérico | DA_18_GnarSmall | 0.5200 |  |
| Jogador 6 | 4-1 | 14:34:00 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 4-1 | 14:34:00 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Feérico | DA_18_GnarSmall | -0.1000 |  |
| Jogador 6 | 4-1 | 14:34:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-1 | 14:34:01 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 4-1 | 14:34:02 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | -0.0800 |  |
| Jogador 6 | 4-1 | 14:34:02 | MOVE Bench -> Board: Lillia (i:8.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | -0.1700 |  |
| Jogador 6 | 4-1 | 14:34:03 | MOVE Board -> Board: Lillia (i:8.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | -0.2000 |  |
| Jogador 6 | 4-1 | 14:34:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-2 | 14:34:33 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 14:34:33 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Feérico | DA_18_GnarSmall | -0.0400 |  |
| Jogador 6 | 4-2 | 14:34:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 14:34:34 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 4-2 | 14:34:35 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_GnarSmall | -0.0500 |  |
| Jogador 6 | 4-2 | 14:34:35 | MOVE Board -> Board: Tristana (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-2 | 14:34:36 | MOVE Board -> Board: Xayah (i:2.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 14:34:36 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-3 | 14:35:06 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-3 | 14:35:06 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Feérico | DA_18_GnarSmall | 0.2200 |  |
| Jogador 6 | 4-3 | 14:35:07 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-3 | 14:35:08 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-3 | 14:35:08 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | 0.2100 |  |
| Jogador 6 | 4-3 | 14:35:09 | MOVE Board -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-3 | 14:35:09 | MOVE Board -> Board: Yorick (i:2.0) <-> Ahri (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-3 | 14:35:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-4 | 14:35:41 | VENDEU: Amumu (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-4 | 14:35:42 | COMPROU: Varus (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 4-4 | 14:35:42 | MOVE Board -> Board: Ahri (i:8.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-4 | 14:35:43 | MOVE Board -> Board: Lillia (i:8.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Feérico | DA_18_GnarSmall | -0.0700 |  |
| Jogador 6 | 4-4 | 14:35:43 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-5 | 14:36:21 | VENDEU: Gnar (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 0 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 4-5 | 14:36:21 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Feérico | DA_18_Tristana | -0.1600 |  |
| Jogador 6 | 4-5 | 14:36:22 | MOVE Board -> Board: Xayah (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 4-5 | 14:36:22 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Feérico | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 4-5 | 14:36:23 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Feérico | DA_18_Tristana | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-6 | 14:37:03 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 22 | 1 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 4-6 | 14:37:03 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Feérico | DA_18_Tristana | 0.7800 |  |
| Jogador 6 | 4-6 | 14:37:04 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Feérico | DA_18_Tristana | 0.5200 |  |
| Jogador 6 | 4-6 | 14:37:04 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 4-6 | 14:37:05 | MOVE Board -> Board: Xayah (i:2.0) <-> Ahri (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Feérico | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 4-6 | 14:37:05 | MOVE Board -> Board: Ahri (i:8.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 4-6 | 14:37:06 | MOVE Board -> Board: Lillia (i:8.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 4-6 | 14:37:06 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Feérico | DA_18_Tristana | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-7 | 14:37:43 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Feérico | DA_18_Tristana | 0.8000 |  |
| Jogador 6 | 4-7 | 14:37:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Feérico | DA_18_Tristana | 0.1500 |  |
| Jogador 6 | 4-7 | 14:37:44 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Feérico | DA_18_Tristana | 0.1600 |  |
| Jogador 6 | 4-7 | 14:37:45 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Feérico | DA_18_Tristana | 0.1000 |  |
| Jogador 6 | 4-7 | 14:37:45 | MOVE Board -> Board: Master Yi (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Feérico | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 4-7 | 14:37:46 | MOVE Board -> Board: Xayah (i:2.0) <-> Ahri (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Feérico | DA_18_Tristana | 0.1300 |  |
| Jogador 6 | 4-7 | 14:37:46 | MOVE Board -> Board: Ahri (i:8.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 4-7 | 14:37:47 | MOVE Board -> Board: Lillia (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Feérico | DA_18_Tristana | 0.0500 |  |
| Jogador 6 | 4-7 | 14:37:47 | MOVE Board -> Board: Yorick (i:2.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 5-1 | 14:38:24 | MOVE Board -> Board: Lillia (i:8.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 5-1 | 14:38:25 | MOVE Board -> Board: Master Yi (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Feérico | DA_18_Tristana | -0.1800 |  |
| Jogador 6 | 5-1 | 14:38:25 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Feérico | DA_18_Tristana | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 5-2 | 14:39:12 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Feérico | DA_18_Tristana | 0.0400 |  |
| Jogador 6 | 5-2 | 14:39:12 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 34 | 2 | Feérico | DA_18_Tristana | 0.8400 |  |
| Jogador 6 | 5-2 | 14:39:13 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 2 | Feérico | DA_Fiddlesticks18 | -0.4900 |  |
| Jogador 6 | 5-2 | 14:39:13 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 41 | 2 | Feérico | DA_Fiddlesticks18 | 0.9700 |  |
| Jogador 6 | 5-2 | 14:39:14 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 2 | Feérico | DA_Fiddlesticks18 | -0.5800 |  |
| Jogador 6 | 5-2 | 14:39:14 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 41 | 2 | Feérico | DA_Fiddlesticks18 | 0.9700 |  |
| Jogador 6 | 5-2 | 14:39:14 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 41 | 2 | Feérico | DA_Fiddlesticks18 | 0.2100 |  |
| Jogador 6 | 5-2 | 14:39:15 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 38 | 2 | Feérico | DA_Fiddlesticks18 | 0.8900 |  |
| Jogador 6 | 5-2 | 14:39:15 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 38 | 2 | Feérico | DA_Fiddlesticks18 | 0.1600 |  |
| Jogador 6 | 5-3 | 14:39:58 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Feérico | DA_Fiddlesticks18 | 0.8900 |  |
| Jogador 6 | 5-3 | 14:39:59 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Feérico | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 6 | 5-3 | 14:39:59 | MOVE Bench -> Board: Ahri (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Feérico | DA_Fiddlesticks18 | 0.2500 |  |
| Jogador 6 | 5-3 | 14:40:00 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Feérico | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 6 | 5-3 | 14:40:00 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Lillia (i:8.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Feérico | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 6 | 5-3 | 14:40:01 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Lillia (i:8.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Feérico | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 6 | 5-3 | 14:40:01 | COMPROU: Alistar (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 3 | Feérico | DA_Fiddlesticks18 | -0.2600 |  |
| Jogador 6 | 5-3 | 14:40:02 | MOVE Board -> Board: Ahri (i:8.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 3 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 5-3 | 14:40:02 | MOVE Board -> Board: Lillia (i:8.0) <-> Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 3 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 5-4 | 14:40:45 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Feérico | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 6 | 5-4 | 14:40:45 | VENDEU: Fiddlesticks (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Feérico | DA_CrimsonRaptor18 | -0.6000 |  |
| Jogador 6 | 5-4 | 14:40:45 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Feérico | DA_CrimsonRaptor18 | 0.1700 |  |
| Jogador 6 | 5-4 | 14:40:46 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Master Yi (i:6.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Feérico | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 6 | 5-4 | 14:40:48 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Master Yi (i:6.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Feérico | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 6 | 5-4 | 14:40:48 | MOVE Board -> Board: Master Yi (i:6.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Feérico | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 6 | 5-4 | 14:40:48 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Feérico | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 6 | 5-4 | 14:40:49 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Feérico | DA_CrimsonRaptor18 | -0.4300 |  |
| Jogador 7 | ? | 14:28:25 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 14:28:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 14:28:31 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 14:28:32 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 14:28:32 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-1 | 14:28:33 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-1 | 14:28:34 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 14:28:34 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 14:28:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 14:28:36 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 7 | 1-2 | 14:28:38 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 14:28:39 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 14:28:39 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 14:28:40 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 14:28:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 14:28:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 14:28:46 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-3 | 14:28:47 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 7 | 1-3 | 14:28:47 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 14:28:48 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2000 |  |
| Jogador 7 | 1-3 | 14:28:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 14:28:55 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8300 |  |
| Jogador 7 | 1-4 | 14:28:55 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-4 | 14:28:56 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-4 | 14:28:56 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 7 | 1-4 | 14:28:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 14:29:05 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 14:29:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-1 | 14:29:06 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 14:29:06 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 14:29:07 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 14:29:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-1 | 14:29:08 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | -0.6300 |  |
| Jogador 7 | 2-1 | 14:29:08 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 2-1 | 14:29:09 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Varus (i:2.0) (tabuleiro slot 9) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1500 |  |
| Jogador 7 | 2-2 | 14:29:15 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 1.0500 |  |
| Jogador 7 | 2-2 | 14:29:16 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.6500 |  |
| Jogador 7 | 2-2 | 14:29:16 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1700 |  |
| Jogador 7 | 2-2 | 14:29:18 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 14:29:18 | VENDEU: Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | -0.6200 |  |
| Jogador 7 | 2-2 | 14:29:19 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1400 |  |
| Jogador 7 | 2-2 | 14:29:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Hecarim | 0.0200 |  |
| Jogador 7 | 2-2 | 14:29:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-2 | 14:29:20 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Hecarim | 0.1700 |  |
| Jogador 7 | 2-3 | 14:29:28 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Hecarim | 0.3100 |  |
| Jogador 7 | 2-3 | 14:29:29 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.2600 |  |
| Jogador 7 | 2-3 | 14:29:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 14:29:43 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.2900 |  |
| Jogador 7 | 2-4 | 14:29:43 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.3100 |  |
| Jogador 7 | 2-4 | 14:29:43 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 14:29:44 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-4 | 14:29:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 14:29:57 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 0.9100 |  |
| Jogador 7 | 2-5 | 14:29:58 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.8900 |  |
| Jogador 7 | 2-5 | 14:29:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 14:29:59 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 14:29:59 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.4800 |  |
| Jogador 7 | 2-5 | 14:30:00 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 14:30:00 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 14:30:01 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-5 | 14:30:01 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.4800 |  |
| Jogador 7 | 2-6 | 14:30:14 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Sentinel18 | -0.2700 |  |
| Jogador 7 | 2-6 | 14:30:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 2-6 | 14:30:15 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | 0.4600 |  |
| Jogador 7 | 2-6 | 14:30:15 | MOVE Board -> Board: Azuporã (i:8.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-6 | 14:30:16 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-6 | 14:30:16 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-7 | 14:30:31 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 2-7 | 14:30:31 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 2-7 | 14:30:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-7 | 14:30:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-7 | 14:30:33 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-7 | 14:30:33 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-1 | 14:30:51 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | 0.7300 |  |
| Jogador 7 | 3-1 | 14:30:52 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 3-1 | 14:30:53 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-2 | 14:31:14 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Sentinel18 | 0.2000 |  |
| Jogador 7 | 3-2 | 14:31:15 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-2 | 14:31:16 | VENDEU: Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 3-2 | 14:31:16 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | 0.1300 |  |
| Jogador 7 | 3-2 | 14:31:17 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 3-2 | 14:31:18 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-2 | 14:31:18 | VENDEU: Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | -0.4800 |  |
| Jogador 7 | 3-2 | 14:31:19 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Sentinel18 | 0.2000 |  |
| Jogador 7 | 3-2 | 14:31:19 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-3 | 14:31:37 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | 0.7700 |  |
| Jogador 7 | 3-3 | 14:31:38 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 7 | 3-3 | 14:31:38 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 7 | 3-3 | 14:31:39 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 7 | 3-3 | 14:31:39 | VENDEU: Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 3-3 | 14:31:40 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Hecarim (i:6.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 3-3 | 14:31:40 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Hecarim (i:6.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 7 | 3-3 | 14:31:41 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-3 | 14:31:41 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-4 | 14:32:02 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 7 | 3-4 | 14:32:02 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 7 | 3-4 | 14:32:03 | MOVE Board -> Board: Hecarim (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-4 | 14:32:04 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Sentinel18 | -0.6200 |  |
| Jogador 7 | 3-4 | 14:32:04 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Yorick (i:2.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Sentinel18 | 0.1400 |  |
| Jogador 7 | 3-4 | 14:32:05 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 3-4 | 14:32:05 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 3-4 | 14:32:06 | MOVE Board -> Board: Yorick (i:2.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 3-4 | 14:32:06 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-5 | 14:32:28 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-5 | 14:32:29 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_Sentinel18 | 0.5900 |  |
| Jogador 7 | 3-5 | 14:32:29 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 3-5 | 14:32:30 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 3-5 | 14:32:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 3-5 | 14:32:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 3-5 | 14:32:31 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.1700 |  |
| Jogador 7 | 3-5 | 14:32:31 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-5 | 14:32:32 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-6 | 14:32:55 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Sentinel18 | 0.7300 |  |
| Jogador 7 | 3-6 | 14:32:56 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.7300 |  |
| Jogador 7 | 3-6 | 14:32:57 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-6 | 14:32:57 | MOVE Board -> Board: Xayah (i:2.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 3-6 | 14:32:58 | MOVE Board -> Board: Hecarim (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-6 | 14:32:58 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-7 | 14:33:24 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 3-7 | 14:33:25 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Sentinel18 | 0.1600 |  |
| Jogador 7 | 3-7 | 14:33:25 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-7 | 14:33:26 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 3-7 | 14:33:26 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-7 | 14:33:27 | MOVE Board -> Board: Yorick (i:2.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-7 | 14:33:28 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 3-7 | 14:33:29 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-7 | 14:33:29 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-1 | 14:33:59 | VENDEU: Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_Sentinel18 | 0.0700 |  |
| Jogador 7 | 4-1 | 14:34:00 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Sentinel18 | 0.1300 |  |
| Jogador 7 | 4-1 | 14:34:00 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Colosso | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 4-1 | 14:34:01 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_Sentinel18 | 0.7300 |  |
| Jogador 7 | 4-1 | 14:34:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 4-1 | 14:34:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-1 | 14:34:02 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 4-1 | 14:34:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-1 | 14:34:03 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 4-2 | 14:34:33 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | -0.1300 |  |
| Jogador 7 | 4-2 | 14:34:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-2 | 14:34:34 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-2 | 14:34:34 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 4-2 | 14:34:35 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 4-2 | 14:34:35 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-2 | 14:34:36 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 4-2 | 14:34:36 | MOVE Board -> Board: Hecarim (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Sentinel18 | -0.2000 |  |
| Jogador 7 | 4-2 | 14:34:37 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-3 | 14:35:06 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | 0.7600 |  |
| Jogador 7 | 4-3 | 14:35:06 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | 0.5700 |  |
| Jogador 7 | 4-3 | 14:35:07 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 4-3 | 14:35:08 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-3 | 14:35:08 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.2400 |  |
| Jogador 7 | 4-3 | 14:35:09 | MOVE Board -> Board: Xayah (i:2.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 4-3 | 14:35:09 | MOVE Board -> Board: Xayah (i:2.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-3 | 14:35:10 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-3 | 14:35:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-4 | 14:35:41 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 4-4 | 14:35:42 | VENDEU: Mamãe Bicuda (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_Sentinel18 | -0.4900 |  |
| Jogador 7 | 4-4 | 14:35:42 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 4-4 | 14:35:43 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-4 | 14:35:43 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-4 | 14:35:44 | MOVE Board -> Board: Azuporã (i:8.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 4-4 | 14:35:44 | MOVE Board -> Board: Xayah (i:2.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Sentinel18 | -0.1000 |  |
| Jogador 7 | 4-4 | 14:35:45 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-5 | 14:36:21 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 4-5 | 14:36:21 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_Sentinel18 | 0.6700 |  |
| Jogador 7 | 4-5 | 14:36:22 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Sentinel18 | 0.2200 |  |
| Jogador 7 | 4-5 | 14:36:22 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Sentinel18 | 0.4400 |  |
| Jogador 7 | 4-5 | 14:36:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 4-5 | 14:36:24 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-5 | 14:36:24 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-5 | 14:36:25 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-6 | 14:37:03 | VENDEU: Hecarim (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 0 | Colosso | DA_Sentinel18 | -0.5500 |  |
| Jogador 7 | 4-6 | 14:37:03 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Colosso | DA_Sentinel18 | 0.7700 |  |
| Jogador 7 | 4-6 | 14:37:04 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Yorick (i:2.0) (tabuleiro slot 26) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Colosso | DA_Sentinel18 | 0.1100 |  |
| Jogador 7 | 4-6 | 14:37:04 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Yorick (i:2.0) (tabuleiro slot 26) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Colosso | DA_Sentinel18 | 0.1100 |  |
| Jogador 7 | 4-6 | 14:37:05 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Colosso | DA_Sentinel18 | 0.1300 |  |
| Jogador 7 | 4-6 | 14:37:05 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Colosso | DA_Sentinel18 | -0.4100 |  |
| Jogador 7 | 4-6 | 14:37:06 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Colosso | DA_Sentinel18 | 0.4100 |  |
| Jogador 7 | 4-6 | 14:37:06 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 4-6 | 14:37:07 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 9 | 0 | Colosso | DA_Sentinel18 | -0.0500 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 7 | 4-7 | 14:37:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Fiddlesticks (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 16 | 0 | Colosso | DA_Sentinel18 | 0.0800 |  |
| Jogador 7 | 4-7 | 14:37:43 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_TearOfTheGoddess -> Fiddlesticks (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 16 | 0 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 4-7 | 14:37:44 | MOVE Bench -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 16 | 0 | Colosso | DA_Sentinel18 | 0.1800 |  |
| Jogador 7 | 4-7 | 14:37:45 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 16 | 0 | Colosso | DA_Sentinel18 | 0.0800 |  |
| Jogador 7 | 4-7 | 14:37:45 | COMPROU: Ashe (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 11 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 4-7 | 14:37:46 | COMPROU: Grompe (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 9 | 0 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 4-7 | 14:37:46 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Colosso | DA_Sentinel18 | 0.0000 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 7 | 4-7 | 14:37:47 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_Sentinel18 | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 7 | 4-7 | 14:37:47 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-1 | 14:38:24 | VENDEU: Aronguejo (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 15 | 0 | Colosso | DA_Sentinel18 | -0.5800 |  |
| Jogador 7 | 5-1 | 14:38:25 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 12 | 0 | Colosso | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 5-1 | 14:38:25 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 8 | 0 | Colosso | DA_Sentinel18 | -0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 7 | 5-1 | 14:38:26 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_Sentinel18 | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 7 | 5-1 | 14:38:26 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Colosso | DA_Sentinel18 | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 7 | 5-1 | 14:38:27 | MOVE Bench -> Board: Ashe (i:10.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_Sentinel18 | 0.4100 |  |
| Jogador 7 | 5-1 | 14:38:27 | MOVE Board -> Board: Ashe (i:10.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-1 | 14:38:28 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Yorick (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-1 | 14:38:28 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 14:39:12 | COMPROU: Shen (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 5-2 | 14:39:12 | MOVE Board -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 14:39:13 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Colosso | DA_Sentinel18 | 0.1800 |  |
| Jogador 7 | 5-2 | 14:39:13 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 5-2 | 14:39:14 | MOVE Board -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-2 | 14:39:14 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Ashe (i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-2 | 14:39:14 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-3 | 14:39:58 | MOVE Board -> Board: Ashe (i:10.0) <-> Xayah (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-3 | 14:39:59 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-3 | 14:39:59 | MOVE Board -> Board: Yorick (i:2.0) <-> Cassiopeia (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-3 | 14:40:00 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 0 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-4 | 14:40:45 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 1 | Colosso | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 5-4 | 14:40:45 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Yorick (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 1 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-4 | 14:40:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Ashe (i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 1 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-4 | 14:40:46 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 1 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 5-5 | 14:41:33 | MOVE Board -> Board: Ashe (i:10.0) <-> Xayah (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 35 | 2 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-5 | 14:41:33 | MOVE Board -> Board: Xayah (i:2.0) <-> Kog'Maw (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 35 | 2 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-5 | 14:41:34 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 35 | 2 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-5 | 14:41:34 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 35 | 2 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 5-6 | 14:42:19 | MOVE Board -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 47 | 3 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-6 | 14:42:19 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 47 | 3 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-6 | 14:42:20 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 47 | 3 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 5-7 | 14:43:06 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Yorick (i:2.0) (tabuleiro slot 19) | WINSTREAK | WINSTREAK: preservar vantagem atual | 59 | 4 | Colosso | DA_Sentinel18 | 0.1300 |  |
| Jogador 7 | 5-7 | 14:43:07 | MOVE Board -> Board: Ashe (i:10.0) <-> Cassiopeia (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 59 | 4 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-7 | 14:43:07 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Yorick (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 59 | 4 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-7 | 14:43:08 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 59 | 4 | Colosso | DA_Sentinel18 | -0.1000 |  |
| Jogador 7 | 6-1 | 14:43:54 | VENDEU: Shen (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 75 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-1 | 14:43:54 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 73 | 5 | Colosso | DA_Sentinel18 | 0.4100 |  |
| Jogador 7 | 6-1 | 14:43:55 | MOVE Board -> Board: Yorick (i:2.0) <-> Xayah (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 73 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 6-1 | 14:43:55 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 73 | 5 | Colosso | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 6-1 | 14:43:56 | MOVE Board -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 73 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-1 | 14:43:56 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 73 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 6-1 | 14:43:57 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 73 | 5 | Colosso | DA_Sentinel18 | -0.1100 |  |
| Jogador 7 | 6-2 | 14:44:46 | VENDEU: Grompe (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 89 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 6-2 | 14:44:47 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 86 | 5 | Colosso | DA_Sentinel18 | 0.9200 |  |
| Jogador 7 | 6-2 | 14:44:47 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 86 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-2 | 14:44:48 | VENDEU: Vi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 89 | 5 | Colosso | DA_Sentinel18 | -0.1000 |  |
| Jogador 7 | 6-2 | 14:44:48 | COMPROU: Master Yi (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 86 | 5 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 6-2 | 14:44:49 | VENDEU: Master Yi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 89 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 6-2 | 14:44:49 | COMPROU: Ezreal (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 85 | 5 | Colosso | DA_Sentinel18 | -0.1900 |  |
| Jogador 7 | 6-2 | 14:44:50 | VENDEU: Ezreal (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 89 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-2 | 14:44:50 | COMPROU: Rammus (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 86 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 8 | ? | 14:28:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | ? | 14:28:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | ? | 14:28:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 14:28:31 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 14:28:32 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-1 | 14:28:32 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-1 | 14:28:33 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3600 |  |
| Jogador 8 | 1-1 | 14:28:34 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-1 | 14:28:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 14:28:36 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5000 |  |
| Jogador 8 | 1-2 | 14:28:38 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 8 | 1-2 | 14:28:39 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 8 | 1-2 | 14:28:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 14:28:46 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-3 | 14:28:47 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 8 | 1-3 | 14:28:47 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1700 |  |
| Jogador 8 | 1-3 | 14:28:48 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 8 | 1-3 | 14:28:49 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 8 | 1-3 | 14:28:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 14:28:55 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.1100 |  |
| Jogador 8 | 1-4 | 14:28:55 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 1-4 | 14:28:56 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 1-4 | 14:28:56 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 1-4 | 14:28:57 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 1.1000 |  |
| Jogador 8 | 1-4 | 14:28:57 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 1-4 | 14:28:58 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 1-4 | 14:28:58 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.3200 |  |
| Jogador 8 | 1-4 | 14:28:59 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 2-1 | 14:29:05 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-1 | 14:29:05 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.3000 |  |
| Jogador 8 | 2-1 | 14:29:06 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | -0.2100 |  |
| Jogador 8 | 2-1 | 14:29:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-1 | 14:29:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-2 | 14:29:15 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | 1.0500 |  |
| Jogador 8 | 2-2 | 14:29:16 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | 0.3600 |  |
| Jogador 8 | 2-2 | 14:29:16 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-2 | 14:29:18 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2300 |  |
| Jogador 8 | 2-2 | 14:29:18 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | -0.1300 |  |
| Jogador 8 | 2-2 | 14:29:19 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | -0.1500 |  |
| Jogador 8 | 2-2 | 14:29:19 | MOVE Bench -> Board: Karma (i:2.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | -0.5300 |  |
| Jogador 8 | 2-2 | 14:29:20 | MOVE Bench -> Board: Karma (i:4.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-2 | 14:29:20 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 2-3 | 14:29:28 | COMPROU: Master Yi (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 12 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 2-3 | 14:29:29 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Karma (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 12 | 0 | — | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 2-3 | 14:29:30 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 9 | 0 | — | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 2-3 | 14:29:30 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 9 | 0 | — | DA_Karma18 | 0.4800 |  |
| Jogador 8 | 2-3 | 14:29:31 | COMPROU: Kobuko (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 8 | 0 | — | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-3 | 14:29:32 | VENDEU: Kobuko (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 9 | 0 | — | DA_Karma18 | -0.4000 |  |
| Jogador 8 | 2-3 | 14:29:32 | VENDEU: Kha'Zix (i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 12 | 0 | — | DA_Karma18 | -0.3100 |  |
| Jogador 8 | 2-3 | 14:29:33 | COMPROU: Cascalho (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 11 | 0 | — | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 2-3 | 14:29:33 | VENDEU: Cascalho (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 12 | 0 | — | DA_Karma18 | -0.3600 |  |
| Jogador 8 | 2-4 | 14:29:43 | COMPROU: Karma (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 18 | 1 | Enfeitiçador | DA_Karma18 | 0.9700 |  |
| Jogador 8 | 2-4 | 14:29:43 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_Karma18 | 0.3000 |  |
| Jogador 8 | 2-4 | 14:29:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_Karma18 | 0.2900 |  |
| Jogador 8 | 2-4 | 14:29:44 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_Karma18 | -0.4900 |  |
| Jogador 8 | 2-4 | 14:29:44 | MOVE Bench -> Board: Rammus (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_Karma18 | -0.3100 |  |
| Jogador 8 | 2-4 | 14:29:45 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_Karma18 | -0.5800 |  |
| Jogador 8 | 2-4 | 14:29:46 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-4 | 14:29:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-4 | 14:29:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Enfeitiçador | DA_Karma18 | -0.1200 |  |
| Jogador 8 | 2-5 | 14:29:57 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_Karma18 | 0.9800 |  |
| Jogador 8 | 2-5 | 14:29:58 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_Karma18 | 0.3300 |  |
| Jogador 8 | 2-5 | 14:29:58 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-5 | 14:29:59 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-5 | 14:29:59 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | -0.3400 |  |
| Jogador 8 | 2-5 | 14:30:00 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Enfeitiçador | DA_Karma18 | -0.1900 |  |
| Jogador 8 | 2-5 | 14:30:00 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_Karma18 | -1.0200 |  |
| Jogador 8 | 2-5 | 14:30:01 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-5 | 14:30:01 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_Karma18 | -0.3800 |  |
| Jogador 8 | 2-6 | 14:30:14 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_Karma18 | 0.3600 |  |
| Jogador 8 | 2-6 | 14:30:14 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 2-6 | 14:30:15 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_Karma18 | -0.3200 |  |
| Jogador 8 | 2-6 | 14:30:15 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 2-6 | 14:30:16 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_Karma18 | -0.4200 |  |
| Jogador 8 | 2-6 | 14:30:16 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 2-6 | 14:30:17 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 2-6 | 14:30:17 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Enfeitiçador | DA_Karma18 | -0.1900 |  |
| Jogador 8 | 2-6 | 14:30:17 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Enfeitiçador | DA_Karma18 | -0.6300 |  |
| Jogador 8 | 2-7 | 14:30:31 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-7 | 14:30:31 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-7 | 14:30:31 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Enfeitiçador | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-7 | 14:30:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Enfeitiçador | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 2-7 | 14:30:33 | MOVE Bench -> Board: Lillia (i:8.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 2-7 | 14:30:33 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Enfeitiçador | DA_Karma18 | 0.3900 |  |
| Jogador 8 | 2-7 | 14:30:34 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 2-7 | 14:30:34 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 2 | Enfeitiçador | DA_Karma18 | -0.2700 |  |
| Jogador 8 | 2-7 | 14:30:35 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 2 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-1 | 14:30:51 | COMPROU: Sett (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Enfeitiçador | DA_Karma18 | -0.1200 |  |
| Jogador 8 | 3-1 | 14:30:52 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 2 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-1 | 14:30:53 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Enfeitiçador | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 3-1 | 14:30:54 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 2 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-1 | 14:30:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 2 | Enfeitiçador | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 3-1 | 14:30:55 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 2 | Enfeitiçador | DA_Karma18 | -0.3100 |  |
| Jogador 8 | 3-1 | 14:30:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 2 | Enfeitiçador | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 3-1 | 14:30:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 2 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-1 | 14:30:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 2 | Enfeitiçador | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 3-2 | 14:31:14 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Enfeitiçador | DA_Karma18 | 0.2100 |  |
| Jogador 8 | 3-2 | 14:31:15 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 3-2 | 14:31:16 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Enfeitiçador | DA_Karma18 | -0.3000 |  |
| Jogador 8 | 3-2 | 14:31:16 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 3-2 | 14:31:17 | VENDEU: Caitlyn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 3-2 | 14:31:18 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Enfeitiçador | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 3-2 | 14:31:18 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Enfeitiçador | DA_Karma18 | -0.0700 |  |
| Jogador 8 | 3-2 | 14:31:19 | VENDEU: Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Enfeitiçador | DA_Karma18 | -0.3700 |  |
| Jogador 8 | 3-2 | 14:31:19 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Enfeitiçador | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 3-3 | 14:31:37 | COMPROU: Karma (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Enfeitiçador | DA_Karma18 | 0.2500 |  |
| Jogador 8 | 3-3 | 14:31:38 | COMPROU: Kobuko (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-3 | 14:31:38 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Enfeitiçador | DA_Karma18 | -0.2300 |  |
| Jogador 8 | 3-3 | 14:31:39 | VENDEU: Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Enfeitiçador | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 3-3 | 14:31:39 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Enfeitiçador | DA_Karma18 | -0.2000 |  |
| Jogador 8 | 3-3 | 14:31:40 | VENDEU: Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Enfeitiçador | DA_Karma18 | -0.2700 |  |
| Jogador 8 | 3-3 | 14:31:40 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Enfeitiçador | DA_Karma18 | -0.3400 |  |
| Jogador 8 | 3-3 | 14:31:41 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Enfeitiçador | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 3-3 | 14:31:41 | VENDEU: Sett (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 1 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-4 | 14:32:02 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Enfeitiçador | DA_Karma18 | 0.6900 |  |
| Jogador 8 | 3-4 | 14:32:02 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Enfeitiçador | DA_Karma18 | 0.8100 |  |
| Jogador 8 | 3-4 | 14:32:03 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Enfeitiçador | DA_Karma18 | 0.2400 |  |
| Jogador 8 | 3-4 | 14:32:04 | VENDEU: LeBlanc (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Enfeitiçador | DA_Karma18 | -0.6200 |  |
| Jogador 8 | 3-4 | 14:32:04 | VENDEU: Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Enfeitiçador | DA_Karma18 | -0.5500 |  |
| Jogador 8 | 3-4 | 14:32:05 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Enfeitiçador | DA_Karma18 | -0.1300 |  |
| Jogador 8 | 3-4 | 14:32:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 3 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-4 | 14:32:06 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 3 | Enfeitiçador | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 3-4 | 14:32:06 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 3 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 3-5 | 14:32:28 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Enfeitiçador | DA_Karma18 | 0.7600 |  |
| Jogador 8 | 3-5 | 14:32:29 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Enfeitiçador | DA_Karma18 | 0.2500 |  |
| Jogador 8 | 3-5 | 14:32:29 | COMPROU: Malphite (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Enfeitiçador | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 3-5 | 14:32:30 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Enfeitiçador | DA_Karma18 | 0.4000 |  |
| Jogador 8 | 3-5 | 14:32:30 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 2 | Enfeitiçador | DA_Karma18 | 0.2300 |  |
| Jogador 8 | 3-5 | 14:32:31 | MOVE Board -> Board: Vi (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 2 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-5 | 14:32:31 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 2 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-5 | 14:32:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 2 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 3-6 | 14:32:55 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 3-6 | 14:32:56 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Enfeitiçador | DA_Karma18 | -0.2700 |  |
| Jogador 8 | 3-6 | 14:32:57 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-6 | 14:32:57 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 3-6 | 14:32:58 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 3-6 | 14:32:58 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-6 | 14:32:59 | VENDEU: Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-6 | 14:32:59 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Enfeitiçador | DA_Karma18 | -0.4200 |  |
| Jogador 8 | 3-6 | 14:33:00 | MOVE Board -> Board: Vi (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 2 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-7 | 14:33:24 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Enfeitiçador | DA_Karma18 | 0.8600 |  |
| Jogador 8 | 3-7 | 14:33:25 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Enfeitiçador | DA_Karma18 | 0.6100 |  |
| Jogador 8 | 3-7 | 14:33:25 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Karma (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Enfeitiçador | DA_Karma18 | 0.2300 |  |
| Jogador 8 | 3-7 | 14:33:26 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Karma (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Enfeitiçador | DA_Karma18 | 0.2500 |  |
| Jogador 8 | 3-7 | 14:33:26 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Enfeitiçador | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 3-7 | 14:33:27 | VENDEU: Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Enfeitiçador | DA_Karma18 | -0.5000 |  |
| Jogador 8 | 3-7 | 14:33:28 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Enfeitiçador | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 3-7 | 14:33:29 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 3-7 | 14:33:29 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 3 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 4-1 | 14:33:59 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Enfeitiçador | DA_Karma18 | 0.4100 |  |
| Jogador 8 | 4-1 | 14:34:00 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Enfeitiçador | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 4-1 | 14:34:00 | COMPROU: Sivir (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Enfeitiçador | DA_Karma18 | -0.0700 |  |
| Jogador 8 | 4-1 | 14:34:01 | VENDEU: Sivir (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 4-1 | 14:34:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Enfeitiçador | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 4-1 | 14:34:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 4-1 | 14:34:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 3 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 4-1 | 14:34:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 3 | Enfeitiçador | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 4-1 | 14:34:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 3 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 4-2 | 14:34:33 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Enfeitiçador | DA_Karma18 | 0.7700 |  |
| Jogador 8 | 4-2 | 14:34:33 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Enfeitiçador | DA_Karma18 | -0.4700 |  |
| Jogador 8 | 4-2 | 14:34:34 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 4-2 | 14:34:34 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 4-2 | 14:34:35 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Enfeitiçador | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 4-2 | 14:34:35 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-2 | 14:34:36 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Enfeitiçador | DA_Karma18 | -0.5200 |  |
| Jogador 8 | 4-2 | 14:34:36 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 4-2 | 14:34:37 | VENDEU: Malphite (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Enfeitiçador | DA_Karma18 | -0.4400 |  |
| Jogador 8 | 4-3 | 14:35:06 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Enfeitiçador | DA_Karma18 | 0.8300 |  |
| Jogador 8 | 4-3 | 14:35:06 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Enfeitiçador | DA_Karma18 | 0.8600 |  |
| Jogador 8 | 4-3 | 14:35:07 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Enfeitiçador | DA_Karma18 | 0.2200 |  |
| Jogador 8 | 4-3 | 14:35:08 | VENDEU: LeBlanc (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Enfeitiçador | DA_Karma18 | -0.5500 |  |
| Jogador 8 | 4-3 | 14:35:08 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Enfeitiçador | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 4-3 | 14:35:09 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 35 | 3 | Enfeitiçador | DA_Karma18 | 0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 8 | 4-3 | 14:35:09 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Lillia (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 35 | 3 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 4-3 | 14:35:10 | MOVE Bench -> Board: Lillia (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 35 | 3 | Enfeitiçador | DA_Karma18 | 0.2700 |  |
| Jogador 8 | 4-3 | 14:35:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 34 | 3 | Enfeitiçador | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 4-4 | 14:35:41 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Enfeitiçador | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 4-4 | 14:35:42 | COMPROU: Soraka (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 35 | 3 | Enfeitiçador | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 4-4 | 14:35:42 | COMPROU: Teemo (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 33 | 3 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 4-4 | 14:35:43 | MOVE Board -> Board: Rammus (i:6.0) <-> Master Yi (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 33 | 3 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-4 | 14:35:43 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 33 | 3 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-4 | 14:35:44 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 33 | 3 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-5 | 14:36:21 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 40 | 3 | Enfeitiçador | DA_Karma18 | 0.7900 |  |
| Jogador 8 | 4-5 | 14:36:21 | MOVE Board -> Board: Lillia (i:8.0) <-> Vi (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 40 | 3 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-5 | 14:36:22 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 40 | 3 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-5 | 14:36:22 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 40 | 3 | Enfeitiçador | DA_Karma18 | -0.1600 |  |
| Jogador 8 | 4-6 | 14:37:03 | MOVE Board -> Board: Rakan (i:2.0) <-> Rammus (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 51 | 4 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-6 | 14:37:03 | MOVE Board -> Board: Rammus (i:6.0) <-> Master Yi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 51 | 4 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-6 | 14:37:04 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 51 | 4 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 4-7 | 14:37:43 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Master Yi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 62 | 5 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 4-7 | 14:37:43 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NegatronCloak -> Master Yi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 62 | 5 | Enfeitiçador | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 4-7 | 14:37:44 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 62 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-7 | 14:37:45 | VENDEU: Xayah (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 63 | 5 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 4-7 | 14:37:45 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 59 | 5 | Enfeitiçador | DA_Karma18 | 0.1500 |  |
| Jogador 8 | 4-7 | 14:37:46 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Lillia (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 59 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-7 | 14:37:46 | MOVE Board -> Board: Lillia (i:8.0) <-> Vi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 59 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-7 | 14:37:47 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 59 | 5 | Enfeitiçador | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 5-1 | 14:38:24 | VENDEU: Teemo (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 71 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 5-1 | 14:38:25 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 68 | 5 | Enfeitiçador | DA_Karma18 | 0.7500 |  |
| Jogador 8 | 5-1 | 14:38:25 | VENDEU: Soraka (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 72 | 5 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 5-1 | 14:38:26 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 69 | 5 | Enfeitiçador | DA_Karma18 | 0.3400 |  |
| Jogador 8 | 5-1 | 14:38:26 | MOVE Board -> Board: Vi (i:6.0) <-> Master Yi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 69 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 5-1 | 14:38:27 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rakan (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 69 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 5-1 | 14:38:27 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 69 | 5 | Enfeitiçador | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 5-2 | 14:39:12 | VENDEU: Nidalee (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Enfeitiçador | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 5-2 | 14:39:12 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 82 | 5 | Enfeitiçador | DA_Karma18 | 1.0000 |  |
| Jogador 8 | 5-2 | 14:39:13 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 79 | 5 | Enfeitiçador | DA_Karma18 | 0.8600 |  |
| Jogador 8 | 5-2 | 14:39:13 | VENDEU: LeBlanc (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Enfeitiçador | DA_Karma18 | -0.6000 |  |
| Jogador 8 | 5-2 | 14:39:14 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 81 | 5 | Enfeitiçador | DA_18_Diana | 1.0000 |  |
| Jogador 8 | 5-2 | 14:39:14 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 78 | 5 | Enfeitiçador | DA_18_Diana | -0.0200 |  |
| Jogador 8 | 5-2 | 14:39:14 | COMPROU: Elise (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Enfeitiçador | DA_18_Diana | 0.0400 |  |
| Jogador 8 | 5-2 | 14:39:15 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Enfeitiçador | DA_18_Diana | 0.0000 |  |
| Jogador 8 | 5-2 | 14:39:15 | MOVE Board -> Board: Rammus (i:6.0) <-> Lillia (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Enfeitiçador | DA_18_Diana | -0.0100 |  |
| Jogador 8 | 5-3 | 14:39:58 | VENDEU: Diana (i:12.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 95 | 5 | Enfeitiçador | DA_18_Lillia | -0.6000 |  |
| Jogador 8 | 5-3 | 14:39:59 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 92 | 5 | Enfeitiçador | DA_18_Lillia | 0.5200 |  |
| Jogador 8 | 5-3 | 14:39:59 | VENDEU: Elise (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 94 | 5 | Enfeitiçador | DA_18_Lillia | -0.0200 |  |
| Jogador 8 | 5-3 | 14:40:00 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 91 | 5 | Enfeitiçador | DA_18_Lillia | 0.3500 |  |
| Jogador 8 | 5-3 | 14:40:00 | VENDEU: Hecarim (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 94 | 5 | Enfeitiçador | DA_18_Lillia | -0.4500 |  |
| Jogador 8 | 5-3 | 14:40:01 | COMPROU: Amumu (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 90 | 5 | Enfeitiçador | DA_18_Lillia | -0.0400 |  |
| Jogador 8 | 5-3 | 14:40:01 | MOVE Board -> Board: Lillia (i:8.0) <-> Fiddlesticks (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 90 | 5 | Enfeitiçador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 5-3 | 14:40:02 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Master Yi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 90 | 5 | Enfeitiçador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 5-3 | 14:40:02 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 90 | 5 | Enfeitiçador | DA_18_Lillia | -0.1300 |  |
| Jogador 8 | 5-4 | 14:40:45 | COMPROU: Vi (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 97 | 5 | Enfeitiçador | DA_18_Lillia | 0.7200 |  |
| Jogador 8 | 5-4 | 14:40:45 | VENDEU: Hecarim (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 100 | 5 | Enfeitiçador | DA_18_Lillia | -0.0200 |  |
| Jogador 8 | 5-4 | 14:40:45 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 97 | 5 | Enfeitiçador | DA_18_Lillia | 0.7000 |  |
| Jogador 8 | 5-4 | 14:40:46 | MOVE Board -> Board: Amumu (i:8.0) <-> Lillia (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 97 | 5 | Enfeitiçador | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 5-4 | 14:40:48 | MOVE Board -> Board: Lillia (i:8.0) <-> Rammus (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 97 | 5 | Enfeitiçador | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 5-4 | 14:40:48 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 97 | 5 | Enfeitiçador | DA_18_Lillia | -0.1400 |  |
| Jogador 8 | 5-5 | 14:41:33 | VENDEU: Vi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 112 | 5 | Enfeitiçador | DA_18_Lillia | -0.5100 |  |
| Jogador 8 | 5-5 | 14:41:33 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 108 | 5 | Enfeitiçador | DA_18_Lillia | 0.4000 |  |
| Jogador 8 | 5-5 | 14:41:34 | VENDEU: Master Yi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 111 | 5 | Enfeitiçador | DA_18_Lillia | -0.5100 |  |
| Jogador 8 | 5-5 | 14:41:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 108 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.9700 |  |
| Jogador 8 | 5-5 | 14:41:35 | COMPROU: Veigar (Custo 1 \| i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 107 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 8 | 5-5 | 14:41:35 | COMPROU: Yunara (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 105 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 8 | 5-5 | 14:41:36 | MOVE Board -> Board: Rammus (i:6.0) <-> Fiddlesticks (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 105 | 5 | Enfeitiçador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 8 | 5-5 | 14:41:36 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 105 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 8 | 5-5 | 14:41:36 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 105 | 5 | Enfeitiçador | DA_KogMaw18_AD | -0.1400 |  |
| Jogador 8 | 5-6 | 14:42:19 | VENDEU: Kog'Maw (i:12.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 125 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 8 | 5-6 | 14:42:19 | COMPROU: Rammus (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 122 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.8700 |  |
| Jogador 8 | 5-6 | 14:42:20 | VENDEU: Yunara (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 124 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 8 | 5-6 | 14:42:20 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 120 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1900 |  |
| Jogador 8 | 5-6 | 14:42:21 | VENDEU: Aphelios (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 124 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 8 | 5-6 | 14:42:21 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 120 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1900 |  |
| Jogador 8 | 5-6 | 14:42:21 | MOVE Board -> Board: Vi (i:6.0) <-> Master Yi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 120 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 8 | 5-6 | 14:42:22 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rakan (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 120 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 8 | 5-6 | 14:42:22 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 120 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 8 | 5-7 | 14:43:06 | EQUIP_FROM_INVENTORY: DA_18_EmblemHunter -> Rammus (i:6.0) (tabuleiro slot 25) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 131 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 8 | 5-7 | 14:43:07 | VENDEU: Aphelios (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 135 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 8 | 5-7 | 14:43:07 | COMPROU: Amumu (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 131 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.7200 |  |
| Jogador 8 | 5-7 | 14:43:08 | VENDEU: Veigar (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 132 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 8 | 5-7 | 14:43:08 | COMPROU: Soraka (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 128 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 8 | 5-7 | 14:43:08 | MOVE Board -> Board: Rakan (i:2.0) <-> Karma (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 128 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 8 | 5-7 | 14:43:09 | MOVE Board -> Board: Karma (i:4.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 128 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 8 | 5-7 | 14:43:09 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 128 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.1800 |  |
| Jogador 8 | 6-1 | 14:43:54 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 8 | 6-1 | 14:43:54 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.5400 |  |
| Jogador 8 | 6-1 | 14:43:55 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.6800 |  |
| Jogador 8 | 6-1 | 14:43:55 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.2900 |  |
| Jogador 8 | 6-1 | 14:43:56 | VENDEU: Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 8 | 6-1 | 14:43:56 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 8 | 6-1 | 14:43:57 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 8 | 6-1 | 14:43:57 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 8 | 6-1 | 14:43:57 | MOVE Board -> Board: Karma (i:4.0) <-> Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 8 | 6-2 | 14:44:46 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 8 | 6-2 | 14:44:47 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 149 | 5 | Enfeitiçador | DA_Amumu18 | 1.0800 |  |
| Jogador 8 | 6-2 | 14:44:47 | COMPROU: Morgana (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Enfeitiçador | DA_Amumu18 | -0.2500 |  |
| Jogador 8 | 6-2 | 14:44:48 | VENDEU: Amumu (i:16.0) | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 8 | 6-2 | 14:44:48 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 8 | 6-2 | 14:44:49 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 8 | 6-2 | 14:44:49 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.2300 |  |
| Jogador 8 | 6-2 | 14:44:50 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Enfeitiçador | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 8 | 6-2 | 14:44:50 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Enfeitiçador | DA_Fiddlesticks18 | -0.2700 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 27 | 29 | 145 | 27 | 16 | 197 | 12 | 35 |
| Jogador 2 | 31 | 32 | 160 | 31 | 16 | 253 | 7 | 23 |
| Jogador 3 | 27 | 27 | 135 | 27 | 16 | 182 | 4 | 17 |
| Jogador 4 | 23 | 25 | 125 | 23 | 14 | 173 | 6 | 19 |
| Jogador 5 | 31 | 32 | 160 | 31 | 16 | 231 | 10 | 29 |
| Jogador 6 | 30 | 30 | 150 | 30 | 17 | 210 | 8 | 47 |
| Jogador 7 | 35 | 35 | 175 | 35 | 17 | 239 | 6 | 40 |
| Jogador 8 | 35 | 35 | 175 | 35 | 17 | 272 | 9 | 60 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 197 | 197 | 197 | 0 | 190 | 0 | 197 | 197 | 197 | 63/48 |
| Jogador 2 | 253 | 253 | 253 | 0 | 246 | 0 | 253 | 253 | 253 | 101/87 |
| Jogador 3 | 182 | 182 | 182 | 0 | 174 | 0 | 182 | 182 | 182 | 58/43 |
| Jogador 4 | 173 | 173 | 173 | 0 | 162 | 0 | 173 | 173 | 173 | 61/46 |
| Jogador 5 | 231 | 231 | 231 | 0 | 222 | 0 | 231 | 231 | 231 | 85/71 |
| Jogador 6 | 210 | 210 | 210 | 0 | 196 | 0 | 210 | 210 | 210 | 67/52 |
| Jogador 7 | 239 | 239 | 239 | 0 | 222 | 0 | 239 | 239 | 239 | 58/42 |
| Jogador 8 | 272 | 272 | 272 | 0 | 264 | 0 | 272 | 272 | 272 | 104/89 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.20922301709651947 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.25060486793518066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23841141164302826 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22248587012290955 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013312771916389465 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42622989416122437 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3469875156879425 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25063249468803406 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 30 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 41 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0387866497039795 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.031377911567688 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 43 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9796043038368225 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19132192432880402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17696425318717957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 55 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 56 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33582380414009094 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 63 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12967589497566223 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 2-2 | 64 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06041593849658966 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2756381332874298 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00807955488562584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 68 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1727156937122345 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 2-2 | 69 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32726773619651794 | 0.0 | 0.0 | +e76c0caf-1c3d-493f-9a21-659dd8587fc2 / -— |
| Jogador 1 | 2-2 | 70 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3527817726135254 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 74 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3344882130622864 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 75 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17824050784111023 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 1 | 2-3 | 76 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15105079114437103 | 0.0 | 0.0 | +— / -e76c0caf-1c3d-493f-9a21-659dd8587fc2 |
| Jogador 1 | 2-3 | 77 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 78 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1169836521148682 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36419224739074707 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 84 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4286743998527527 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 85 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012633305042982101 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 87 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0242490768432617 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32583022117614746 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 94 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 1 | 2-5 | 95 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0037288148887455463 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 97 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06561169028282166 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 98 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004718039184808731 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 99 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015006372705101967 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 100 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479967594146729 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 10.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07185867428779602 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 3 | 0 | 10.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27010679244995117 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 105 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 3 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2985334098339081 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 106 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06937354803085327 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.690438698977232e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014103122986853123 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 109 | PASS | STABILIZE | 95.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 112 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0474052429199219 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-7 | 113 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 6 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35878920555114746 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 115 | PASS | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 6 | 12 | 1 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2475089579820633 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 123 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 12 | 1 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08159380406141281 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 124 | BUY_XP | STABILIZE | 95.0 | 6 | 12 | 1 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 125 | BUY_XP | STABILIZE | 95.0 | 6 | 8 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 126 | BUY_XP | STABILIZE | 95.0 | 6 | 4 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 127 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0023640748113393784 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016153350472450256 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 129 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3994933068752289 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 130 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016480665653944016 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 132 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022597791627049446 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 1 | 3-2 | 133 | BUY | STABILIZE | 95.0 | 6 | 4 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07508297264575958 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 134 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009105635806918144 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 135 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0146073829382658 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998000115156174 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 137 | PASS | STABILIZE | 95.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 142 | BUY | STABILIZE | 83.0 | 6 | 5 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00392879405990243 | 0.0 | 0.0 | +e6ee6b15-d413-4678-8ffb-29272199a53d / -— |
| Jogador 1 | 3-3 | 143 | BUY | STABILIZE | 83.0 | 6 | 2 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03628426417708397 | 0.0 | 0.0 | +66b5ed5e-7fdf-4135-a334-e693715e302d / -— |
| Jogador 1 | 3-3 | 144 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39972448348999023 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 145 | MOVE_BOARD | FAST8 | 83.0 | 6 | 0 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014996782876551151 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 146 | PASS | FAST8 | 83.0 | 6 | 0 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 152 | BUY | FAST8 | 72.0 | 6 | 6 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06937848031520844 | 0.0 | 0.0 | +0450963e-c7e2-4ff5-a2f5-09e65fa63527 / -— |
| Jogador 1 | 3-4 | 153 | BUY | FAST8 | 72.0 | 6 | 4 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07739397138357162 | 0.0 | 0.0 | +54b47885-6cb9-42e7-a9bb-049e0e2d2956 / -— |
| Jogador 1 | 3-4 | 154 | SELL | FAST8 | 72.0 | 6 | 3 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02176666632294655 | 0.0 | 0.0 | +— / -54b47885-6cb9-42e7-a9bb-049e0e2d2956 |
| Jogador 1 | 3-4 | 155 | BUY | FAST8 | 72.0 | 6 | 4 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15096314251422882 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 156 | SELL | FAST8 | 72.0 | 6 | 2 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -bddefab1-7dd7-4954-816c-45dbd44b947b |
| Jogador 1 | 3-4 | 157 | BUY_XP | FAST8 | 72.0 | 6 | 4 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 158 | MOVE_BOARD | FAST8 | 72.0 | 6 | 0 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0022687572054564953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 159 | MOVE_BOARD | FAST8 | 72.0 | 6 | 0 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012735165655612946 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 160 | PASS | FAST8 | 72.0 | 6 | 0 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 162 | BUY | FAST8 | 72.0 | 6 | 6 | 0 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7658191919326782 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 163 | BUY | STABILIZE | 72.0 | 6 | 4 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05151711776852608 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 1 | 3-5 | 164 | SELL | STABILIZE | 72.0 | 6 | 2 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 |
| Jogador 1 | 3-5 | 165 | BUY | STABILIZE | 72.0 | 6 | 7 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3712957799434662 | 0.0 | 0.0 | +c5557e24-8174-4d79-9e22-c2cbbb8225a8 / -— |
| Jogador 1 | 3-5 | 166 | SELL | STABILIZE | 72.0 | 6 | 5 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -0450963e-c7e2-4ff5-a2f5-09e65fa63527 |
| Jogador 1 | 3-5 | 167 | SELL | STABILIZE | 72.0 | 6 | 7 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07522574812173843 | 0.0 | 0.0 | +— / -760d5bee-7d64-4f03-abf0-6357c914a1ed |
| Jogador 1 | 3-5 | 168 | SELL | STABILIZE | 72.0 | 6 | 9 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018150215968489647 | 0.0 | 0.0 | +— / -66b5ed5e-7fdf-4135-a334-e693715e302d |
| Jogador 1 | 3-5 | 169 | SELL | STABILIZE | 72.0 | 6 | 11 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 3-5 | 170 | BUY | STABILIZE | 72.0 | 6 | 14 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00937527697533369 | 0.0 | 0.0 | +a9184317-58b7-4804-9aef-3e2c08c20935 / -— |
| Jogador 1 | 3-6 | 172 | BUY | STABILIZE | 63.0 | 6 | 20 | 2 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7369745969772339 | 0.0 | 0.0 | +600071dd-5c17-4f03-903f-d1cd6c20bb28 / -— |
| Jogador 1 | 3-6 | 173 | BUY | STABILIZE | 63.0 | 6 | 19 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28431278467178345 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -— |
| Jogador 1 | 3-6 | 174 | BUY | STABILIZE | 63.0 | 6 | 17 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8045675158500671 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 175 | SELL | STABILIZE | 63.0 | 6 | 15 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0070333331823349 | 0.0 | 0.0 | +— / -a9184317-58b7-4804-9aef-3e2c08c20935 |
| Jogador 1 | 3-6 | 176 | BUY | STABILIZE | 63.0 | 6 | 16 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018481243401765823 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 1 | 3-6 | 177 | SELL | STABILIZE | 63.0 | 6 | 12 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04730954021215439 | 0.0 | 0.0 | +— / -e6ee6b15-d413-4678-8ffb-29272199a53d |
| Jogador 1 | 3-6 | 178 | BUY_XP | STABILIZE | 63.0 | 6 | 15 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 179 | BUY_XP | STABILIZE | 63.0 | 6 | 11 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0645499974489212 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 180 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 7 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2888900935649872 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 182 | BUY | FAST8 | 51.0 | 7 | 13 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7331070899963379 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 1 | 3-7 | 183 | BUY | FAST8 | 51.0 | 7 | 10 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12755753099918365 | 0.0 | 0.0 | +c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 / -— |
| Jogador 1 | 3-7 | 184 | SELL | FAST8 | 51.0 | 7 | 7 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05524630472064018 | 0.0 | 0.0 | +— / -4518ad1d-87e7-4110-830a-96183c533201 |
| Jogador 1 | 3-7 | 185 | BUY | FAST8 | 51.0 | 7 | 11 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6471487283706665 | 0.0 | 0.0 | +0d8cf876-2884-4724-ab79-246f8e0406f0 / -— |
| Jogador 1 | 3-7 | 186 | MOVE_BOARD | FAST8 | 51.0 | 7 | 8 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0410819947719574 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 187 | MOVE_BOARD | FAST8 | 51.0 | 7 | 8 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010231753811240196 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 188 | MOVE_BOARD | FAST8 | 51.0 | 7 | 8 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018329741433262825 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 189 | MOVE_BOARD | FAST8 | 51.0 | 7 | 8 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28759634494781494 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 190 | PASS | FAST8 | 51.0 | 7 | 8 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 51.0 | 7 | 14 | 1 | 32.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2415591925382614 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 51.0 | 7 | 14 | 1 | 32.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24980567395687103 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 194 | BUY | FAST8 | 51.0 | 7 | 14 | 1 | 32.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11186732351779938 | 0.0 | 0.0 | +e7c8751e-5d30-4953-9508-35488b6c45db / -— |
| Jogador 1 | 4-1 | 195 | MOVE_BOARD | FAST8 | 51.0 | 7 | 11 | 1 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 196 | MOVE_BOARD | FAST8 | 51.0 | 7 | 11 | 1 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013492658734321594 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 197 | MOVE_BOARD | FAST8 | 51.0 | 7 | 11 | 1 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2783093750476837 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 198 | MOVE_BOARD | FAST8 | 51.0 | 7 | 11 | 1 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019793180748820305 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 199 | MOVE_BOARD | FAST8 | 51.0 | 7 | 11 | 1 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00883484911173582 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 200 | PASS | FAST8 | 51.0 | 7 | 11 | 1 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 202 | SELL | FAST8 | 41.0 | 7 | 19 | 1 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019766665995121002 | 0.0 | 0.0 | +— / -e7c8751e-5d30-4953-9508-35488b6c45db |
| Jogador 1 | 4-2 | 203 | BUY | FAST8 | 41.0 | 7 | 22 | 2 | 32.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6688462495803833 | 0.0 | 0.0 | +301afc05-ad23-4ed2-a835-108235c399e0 / -— |
| Jogador 1 | 4-2 | 204 | SELL | FAST8 | 41.0 | 7 | 19 | 1 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34066668152809143 | 0.0 | 0.0 | +— / -727765c8-7f02-491e-a6da-12b0dab59f6d |
| Jogador 1 | 4-2 | 205 | BUY | FAST8 | 41.0 | 7 | 21 | 2 | 32.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2479974329471588 | 0.0 | 0.0 | +6fa83356-562b-4a26-a77d-3e989089e70a / -— |
| Jogador 1 | 4-2 | 206 | MOVE_BOARD | FAST8 | 41.0 | 7 | 20 | 2 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007706447504460812 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 207 | MOVE_BOARD | FAST8 | 41.0 | 7 | 20 | 2 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016468502581119537 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 208 | MOVE_BOARD | FAST8 | 41.0 | 7 | 20 | 2 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015066426247358322 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 209 | PASS | FAST8 | 41.0 | 7 | 20 | 2 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03094179928302765 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 212 | SELL | STABILIZE | 30.0 | 7 | 30 | 3 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -c5557e24-8174-4d79-9e22-c2cbbb8225a8 |
| Jogador 1 | 4-3 | 213 | BUY | STABILIZE | 30.0 | 7 | 32 | 3 | 32.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3240160644054413 | 0.0 | 0.0 | +235510e3-df54-4de9-9bcf-bff6d47e364a / -— |
| Jogador 1 | 4-3 | 214 | SELL | STABILIZE | 30.0 | 7 | 28 | 2 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09413333237171173 | 0.0 | 0.0 | +— / -235510e3-df54-4de9-9bcf-bff6d47e364a |
| Jogador 1 | 4-3 | 215 | BUY | STABILIZE | 30.0 | 7 | 32 | 3 | 32.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35986146330833435 | 0.0 | 0.0 | +3f488391-7117-4e28-b6cc-7416722351d4 / -— |
| Jogador 1 | 4-3 | 216 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 29 | 2 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3544905483722687 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 217 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 29 | 2 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01473755482584238 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 218 | PASS | STABILIZE | 30.0 | 7 | 29 | 2 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05188889056444168 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 222 | SELL | STABILIZE | 30.0 | 7 | 38 | 3 | 32.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09256666898727417 | 0.0 | 0.0 | +— / -3f488391-7117-4e28-b6cc-7416722351d4 |
| Jogador 1 | 4-4 | 223 | BUY | STABILIZE | 30.0 | 7 | 41 | 4 | 32.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8413582444190979 | 0.0 | 0.0 | +30d2995a-d9b8-4424-af46-8766734e440c / -0d8cf876-2884-4724-ab79-246f8e0406f0,c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 |
| Jogador 1 | 4-4 | 224 | BUY | STABILIZE | 30.0 | 7 | 38 | 3 | 32.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1833707094192505 | 0.0 | 0.0 | +a2b57772-7a23-4ffd-ace1-d2a7a3f5a7cd / -— |
| Jogador 1 | 4-4 | 225 | BUY | STABILIZE | 30.0 | 7 | 35 | 3 | 32.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10556595772504807 | 0.0 | 0.0 | +d974e68a-e978-4335-8827-a94a9219be58 / -— |
| Jogador 1 | 4-4 | 226 | SELL | STABILIZE | 30.0 | 7 | 32 | 3 | 32.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -30d2995a-d9b8-4424-af46-8766734e440c |
| Jogador 1 | 4-4 | 227 | BUY | STABILIZE | 30.0 | 7 | 40 | 4 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025630075484514236 | 0.0 | 0.0 | +bb2e33e3-fe6f-4344-b113-aeba7ace7a2d / -— |
| Jogador 1 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 38 | 3 | 32.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03243882209062576 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 229 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 38 | 3 | 32.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022101029753684998 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 230 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 38 | 3 | 32.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.040600236505270004 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 232 | SELL | STABILIZE | 30.0 | 7 | 46 | 4 | 32.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030726086348295212 | 0.0 | 0.0 | +— / -bb2e33e3-fe6f-4344-b113-aeba7ace7a2d |
| Jogador 1 | 4-5 | 233 | BUY | STABILIZE | 30.0 | 7 | 48 | 4 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32203906774520874 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -— |
| Jogador 1 | 4-5 | 234 | SELL | STABILIZE | 30.0 | 7 | 45 | 4 | 32.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02999865449965 | 0.0 | 0.0 | +— / -d974e68a-e978-4335-8827-a94a9219be58 |
| Jogador 1 | 4-5 | 235 | BUY | STABILIZE | 30.0 | 7 | 48 | 4 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11625919491052628 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -— |
| Jogador 1 | 4-5 | 236 | SELL | STABILIZE | 30.0 | 7 | 44 | 4 | 32.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045499999076128006 | 0.0 | 0.0 | +— / -a2b57772-7a23-4ffd-ace1-d2a7a3f5a7cd |
| Jogador 1 | 4-5 | 237 | BUY | STABILIZE | 30.0 | 7 | 47 | 4 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1614965796470642 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -— |
| Jogador 1 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 43 | 4 | 32.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19794555008411407 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 43 | 4 | 32.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022731667384505272 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 240 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 43 | 4 | 32.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 242 | SELL | ALL_IN | 20.0 | 7 | 52 | 5 | 32.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -5f9e16e2-0766-403f-a85a-f6a735c04261 |
| Jogador 1 | 4-6 | 243 | BUY | ALL_IN | 20.0 | 7 | 56 | 5 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0235929489135742 | 0.0 | 0.0 | +98b72340-a402-45bc-9493-71263e3168d6 / -301afc05-ad23-4ed2-a835-108235c399e0,9fe58106-e0c4-4ecc-b152-13c8c0eb564e |
| Jogador 1 | 4-6 | 244 | BUY | ALL_IN | 20.0 | 7 | 53 | 5 | 26.0 | Inferno/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11566542834043503 | 0.0 | 0.0 | +20a4e507-09d3-42d7-b748-4dde14e82ddf / -— |
| Jogador 1 | 4-6 | 245 | REROLL | ALL_IN | 20.0 | 7 | 50 | 5 | 26.0 | Inferno/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 246 | SELL | ALL_IN | 20.0 | 7 | 48 | 4 | 26.0 | Inferno/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6078000068664551 | 0.0 | 0.0 | +— / -98b72340-a402-45bc-9493-71263e3168d6 |
| Jogador 1 | 4-6 | 247 | BUY | ALL_IN | 20.0 | 7 | 56 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0239049196243286 | 0.0 | 0.0 | +d1bc6c5b-74a5-46db-b00f-e91265546f5d / -227dbcdb-af5c-4318-94d1-f01a7847d100,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 4-6 | 248 | BUY | ALL_IN | 20.0 | 7 | 53 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5000331401824951 | 0.0 | 0.0 | +68301141-c9f1-4303-9775-753520772836 / -— |
| Jogador 1 | 4-6 | 249 | REROLL | ALL_IN | 20.0 | 7 | 50 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 250 | BUY | ALL_IN | 20.0 | 7 | 48 | 4 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4061914086341858 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -— |
| Jogador 1 | 4-7 | 252 | SELL | ALL_IN | 7.0 | 7 | 55 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7307999730110168 | 0.0 | 0.0 | +— / -d1bc6c5b-74a5-46db-b00f-e91265546f5d |
| Jogador 1 | 4-7 | 253 | BUY | ALL_IN | 7.0 | 7 | 63 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9371359944343567 | 0.0 | 0.0 | +6722b147-c2a7-4fd0-a943-5036adb3e3a1 / -— |
| Jogador 1 | 4-7 | 254 | SELL | ALL_IN | 7.0 | 7 | 60 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03767075389623642 | 0.0 | 0.0 | +— / -20a4e507-09d3-42d7-b748-4dde14e82ddf |
| Jogador 1 | 4-7 | 255 | BUY | ALL_IN | 7.0 | 7 | 63 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0796359777450562 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -600071dd-5c17-4f03-903f-d1cd6c20bb28,cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 4-7 | 256 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 62 | 5 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43513351678848267 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 257 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 62 | 5 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2897426187992096 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 258 | BUY | ALL_IN | 7.0 | 7 | 62 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41688433289527893 | 0.0 | 0.0 | +755060be-13bb-4686-9ee9-e53fef2d75b2 / -— |
| Jogador 1 | 4-7 | 259 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 59 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001354957465082407 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 260 | BUY | ALL_IN | 7.0 | 7 | 59 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02112375944852829 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -— |
| Jogador 1 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 7.0 | 7 | 66 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17469331622123718 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 7.0 | 7 | 66 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16656650602817535 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 264 | SELL | ALL_IN | 7.0 | 7 | 66 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7243000268936157 | 0.0 | 0.0 | +— / -04520fe5-4449-4632-b275-e5e28d642007 |
| Jogador 1 | 5-1 | 265 | BUY | ALL_IN | 7.0 | 7 | 69 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.049907922744751 | 0.0 | 0.0 | +ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 / -— |
| Jogador 1 | 5-1 | 266 | SELL | ALL_IN | 7.0 | 7 | 68 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010028937831521034 | 0.0 | 0.0 | +— / -3b934078-806c-40f0-b102-e9131220f70e |
| Jogador 1 | 5-1 | 267 | BUY | ALL_IN | 7.0 | 7 | 72 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0797263383865356 | 0.0 | 0.0 | +b0c8ce74-5ce1-4ed0-82ac-f95013475f3c / -9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8,d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 5-1 | 268 | BUY | ALL_IN | 7.0 | 7 | 70 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46759673953056335 | 0.0 | 0.0 | +58cbdbde-2151-438c-8897-902bef9bcd92 / -— |
| Jogador 1 | 5-1 | 269 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 66 | 5 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5605860352516174 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 270 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 66 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015073024667799473 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 272 | BUY | ALL_IN | 7.0 | 7 | 77 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4759495258331299 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -— |
| Jogador 1 | 5-2 | 273 | BUY | ALL_IN | 7.0 | 7 | 75 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07980978488922119 | 0.0 | 0.0 | +3658b5d8-450f-451a-8487-5b3bdd7c385b / -— |
| Jogador 1 | 5-2 | 274 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 74 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.310343011748046e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 275 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 74 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999630860984325 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 276 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 74 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04226560518145561 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 277 | PASS | ALL_IN | 7.0 | 7 | 74 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5146138072013855 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29996994137763977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.16027452051639557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43195363879203796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5009031295776367 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1178059577941895 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11989116668701172 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 28 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3088749945163727 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 41 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4079098701477051 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0720369815826416 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20235595107078552 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40033191442489624 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024478765204548836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 46 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012103810906410217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 47 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.037959098815918 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18197010457515717 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2734133303165436 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26543864607810974 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 56 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14788657426834106 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047933466732501984 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1965295523405075 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 2 | 2-1 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028999745845794678 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004016788676381111 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 62 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479689836502075 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 63 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23485329747200012 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 64 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15269938111305237 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 65 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8824999928474426 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-2 | 66 | BUY_XP | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.000639524485450238 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 68 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999117702245712 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 70 | PASS | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29644280672073364 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 73 | BUY | STABILIZE | 90.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03773828223347664 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 74 | SELL | STABILIZE | 90.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 |
| Jogador 2 | 2-3 | 75 | BUY | STABILIZE | 90.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030426939949393272 | 0.0 | 0.0 | +e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 / -— |
| Jogador 2 | 2-3 | 76 | SELL | STABILIZE | 90.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12440727651119232 | 0.0 | 0.0 | +— / -7ca9b803-76eb-4283-9648-7f98bfd81149 |
| Jogador 2 | 2-3 | 77 | SELL | STABILIZE | 90.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05833333358168602 | 0.0 | 0.0 | +— / -e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 |
| Jogador 2 | 2-3 | 78 | BUY_XP | STABILIZE | 90.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 79 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4014284610748291 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 80 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014995808713138103 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 82 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35677963495254517 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 83 | BUY | STABILIZE | 90.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1367374211549759 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 84 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 85 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998373575508595 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 86 | PASS | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 92 | BUY | STABILIZE | 90.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3384930193424225 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 93 | BUY | STABILIZE | 90.0 | 5 | 2 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07552637159824371 | 0.0 | 0.0 | +eb214f08-2367-4b33-af94-8aa504781450 / -— |
| Jogador 2 | 2-5 | 94 | BUY | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10363151878118515 | 0.0 | 0.0 | +be53a299-cc3e-4af3-94f6-343f9de1e0a0 / -— |
| Jogador 2 | 2-5 | 95 | SELL | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3409999907016754 | 0.0 | 0.0 | +— / -eb214f08-2367-4b33-af94-8aa504781450 |
| Jogador 2 | 2-5 | 96 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3974502682685852 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 97 | SELL | STABILIZE | 90.0 | 5 | 1 | 0 | 20.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04100000113248825 | 0.0 | 0.0 | +— / -be53a299-cc3e-4af3-94f6-343f9de1e0a0 |
| Jogador 2 | 2-5 | 98 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6411147117614746 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 16.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08416303247213364 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 16.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41244789958000183 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 102 | BUY | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.895645797252655 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 103 | BUY | STABILIZE | 84.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1784849315881729 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 104 | SELL | STABILIZE | 84.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.096413254737854 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 2-6 | 105 | SELL | STABILIZE | 84.0 | 5 | 3 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043666668236255646 | 0.0 | 0.0 | +— / -8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 2-6 | 106 | BUY_XP | STABILIZE | 84.0 | 5 | 6 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 107 | SELL | STABILIZE | 84.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1223333328962326 | 0.0 | 0.0 | +— / -97fc5647-5995-4f21-aa03-13454546919a |
| Jogador 2 | 2-6 | 108 | BUY_XP | STABILIZE | 84.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 109 | BUY | STABILIZE | 84.0 | 5 | 1 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039742015302181244 | 0.0 | 0.0 | +8ea1c095-e10b-46d0-8097-a70a211e2881 / -— |
| Jogador 2 | 2-6 | 110 | SELL | STABILIZE | 84.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3409999907016754 | 0.0 | 0.0 | +— / -8ea1c095-e10b-46d0-8097-a70a211e2881 |
| Jogador 2 | 2-7 | 112 | BUY | STABILIZE | 77.0 | 5 | 7 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6318197846412659 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 113 | BUY | STABILIZE | 77.0 | 5 | 4 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08345139026641846 | 0.0 | 0.0 | +6340ebaf-bd41-4f47-bdce-50e06faa4044 / -— |
| Jogador 2 | 2-7 | 114 | BUY | STABILIZE | 77.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07461805641651154 | 0.0 | 0.0 | +0067f61f-504d-440a-b071-de7f18886e3d / -— |
| Jogador 2 | 2-7 | 115 | SELL | STABILIZE | 77.0 | 5 | 1 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12057773023843765 | 0.0 | 0.0 | +— / -0067f61f-504d-440a-b071-de7f18886e3d |
| Jogador 2 | 2-7 | 116 | SELL | STABILIZE | 77.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09846474230289459 | 0.0 | 0.0 | +— / -6340ebaf-bd41-4f47-bdce-50e06faa4044 |
| Jogador 2 | 2-7 | 117 | BUY_XP | STABILIZE | 77.0 | 5 | 4 | 0 | 20.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 118 | MOVE_BENCH | STABILIZE | 77.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40069007873535156 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014996920712292194 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 122 | BUY | STABILIZE | 77.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28655314445495605 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 123 | BUY | STABILIZE | 77.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26519086956977844 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 77.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2582992613315582 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 125 | BUY | STABILIZE | 77.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0630786344408989 | 0.0 | 0.0 | +4312fba1-1471-4fb3-af6f-257248fa1437 / -— |
| Jogador 2 | 3-1 | 126 | SELL | STABILIZE | 77.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0940198302268982 | 0.0 | 0.0 | +— / -4312fba1-1471-4fb3-af6f-257248fa1437 |
| Jogador 2 | 3-1 | 127 | SELL | STABILIZE | 77.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4644455015659332 | 0.0 | 0.0 | +— / -729ccd5b-adc5-4bca-9523-dcb532e93ecb |
| Jogador 2 | 3-1 | 128 | BUY_XP | STABILIZE | 77.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 129 | SELL | STABILIZE | 77.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -a0ebc646-2e71-4b07-9208-401aa0cda6bb |
| Jogador 2 | 3-1 | 130 | BUY | STABILIZE | 77.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28540101647377014 | 0.0 | 0.0 | +bbdd0918-bfda-49bc-9ae0-8894eaf11a5c / -— |
| Jogador 2 | 3-2 | 132 | BUY | STABILIZE | 66.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28682228922843933 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 133 | BUY | STABILIZE | 66.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24460309743881226 | 0.0 | 0.0 | +f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 / -— |
| Jogador 2 | 3-2 | 134 | BUY | STABILIZE | 66.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025663085281848907 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -— |
| Jogador 2 | 3-2 | 135 | SELL | STABILIZE | 66.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005759625229984522 | 0.0 | 0.0 | +— / -5489a8f6-2466-4171-b91e-64c367875d3c |
| Jogador 2 | 3-2 | 136 | SELL | STABILIZE | 66.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4323333203792572 | 0.0 | 0.0 | +— / -bbdd0918-bfda-49bc-9ae0-8894eaf11a5c |
| Jogador 2 | 3-2 | 137 | BUY_XP | STABILIZE | 66.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 138 | SELL | STABILIZE | 66.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020999999716877937 | 0.0 | 0.0 | +— / -f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 |
| Jogador 2 | 3-2 | 139 | BUY | STABILIZE | 66.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21058619022369385 | 0.0 | 0.0 | +e86a4466-cd1f-48a3-a825-cab2e361b72a / -— |
| Jogador 2 | 3-2 | 140 | SELL | STABILIZE | 66.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3596666753292084 | 0.0 | 0.0 | +— / -e86a4466-cd1f-48a3-a825-cab2e361b72a |
| Jogador 2 | 3-3 | 142 | BUY | STABILIZE | 55.0 | 6 | 9 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7998140454292297 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 143 | BUY | STABILIZE | 55.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004060382954776287 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 144 | SELL | STABILIZE | 55.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 3-3 | 145 | BUY | STABILIZE | 55.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05734553188085556 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 146 | SELL | STABILIZE | 55.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050333332270383835 | 0.0 | 0.0 | +— / -3880fbd9-322b-4375-b855-fbb779a0cb47 |
| Jogador 2 | 3-3 | 147 | BUY_XP | STABILIZE | 55.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 148 | SELL | STABILIZE | 55.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -584e7960-a541-4d45-8ea1-8a75e288c387 |
| Jogador 2 | 3-3 | 149 | SELL | STABILIZE | 55.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49426746368408203 | 0.0 | 0.0 | +— / -e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 3-3 | 150 | BUY_XP | STABILIZE | 55.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 152 | BUY | STABILIZE | 55.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011844784952700138 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -— |
| Jogador 2 | 3-4 | 153 | BUY | STABILIZE | 55.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4466414153575897 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 2 | 3-4 | 154 | BUY | STABILIZE | 55.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25828051567077637 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 155 | SELL | STABILIZE | 55.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 3-4 | 156 | SELL | STABILIZE | 55.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7856666445732117 | 0.0 | 0.0 | +— / -c4c0b136-020d-4c1e-9517-8e0bf4c5a628 |
| Jogador 2 | 3-4 | 157 | SELL | STABILIZE | 55.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0689999982714653 | 0.0 | 0.0 | +— / -c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 2 | 3-4 | 158 | SELL | STABILIZE | 55.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48795557022094727 | 0.0 | 0.0 | +— / -2ace989d-3e9e-483b-9b14-cd6b8f171f17 |
| Jogador 2 | 3-4 | 159 | BUY_XP | STABILIZE | 55.0 | 6 | 11 | 1 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 160 | BUY_XP | STABILIZE | 55.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 162 | BUY | STABILIZE | 55.0 | 7 | 8 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07561925798654556 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 163 | BUY | STABILIZE | 55.0 | 7 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0664554014801979 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 164 | BUY | STABILIZE | 55.0 | 7 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28559184074401855 | 0.0 | 0.0 | +b5cec20a-0619-4060-9f1b-e72942ac34dd / -— |
| Jogador 2 | 3-5 | 165 | SELL | STABILIZE | 55.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020999999716877937 | 0.0 | 0.0 | +— / -b5cec20a-0619-4060-9f1b-e72942ac34dd |
| Jogador 2 | 3-5 | 166 | SELL | STABILIZE | 55.0 | 7 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09655903279781342 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 3-5 | 167 | BUY_XP | STABILIZE | 55.0 | 7 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 168 | SELL | STABILIZE | 55.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09774290025234222 | 0.0 | 0.0 | +— / -cce8de69-f877-4e86-b720-6aea91e68f47 |
| Jogador 2 | 3-5 | 169 | BUY_XP | STABILIZE | 55.0 | 7 | 4 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 170 | SELL | STABILIZE | 55.0 | 7 | 0 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0210000276565552 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 3-6 | 172 | BUY | STABILIZE | 44.0 | 7 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8032166957855225 | 0.0 | 0.0 | +63304cf5-4aa7-473e-9bfb-ec04cd68ebbd / -— |
| Jogador 2 | 3-6 | 173 | BUY | STABILIZE | 44.0 | 7 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879561483860016 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-6 | 174 | BUY | STABILIZE | 44.0 | 7 | 4 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009245792403817177 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 175 | SELL | STABILIZE | 44.0 | 7 | 0 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -23157bd6-5e8f-4416-bb7f-2e5d71a06543 |
| Jogador 2 | 3-6 | 176 | BUY | STABILIZE | 44.0 | 7 | 4 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23991107940673828 | 0.0 | 0.0 | +33a860e2-992f-4355-ab24-85b4a2576f90 / -— |
| Jogador 2 | 3-6 | 177 | SELL | STABILIZE | 44.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 3-6 | 178 | SELL | STABILIZE | 44.0 | 7 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37439998984336853 | 0.0 | 0.0 | +— / -33a860e2-992f-4355-ab24-85b4a2576f90 |
| Jogador 2 | 3-6 | 179 | BUY | STABILIZE | 44.0 | 7 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06759399175643921 | 0.0 | 0.0 | +8fb80cc8-4120-41a0-bc96-35f81a466ed9 / -— |
| Jogador 2 | 3-6 | 180 | SELL | STABILIZE | 44.0 | 7 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050333332270383835 | 0.0 | 0.0 | +— / -8fb80cc8-4120-41a0-bc96-35f81a466ed9 |
| Jogador 2 | 3-7 | 182 | BUY | STABILIZE | 32.0 | 7 | 11 | 1 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7522304058074951 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -0c15e414-bc67-46de-a087-fb7708db0dfe,e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-7 | 183 | BUY | STABILIZE | 32.0 | 7 | 8 | 0 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26671457290649414 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 2 | 3-7 | 184 | BUY | STABILIZE | 32.0 | 7 | 5 | 0 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09781061857938766 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 185 | SELL | STABILIZE | 32.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6190000176429749 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 3-7 | 186 | BUY | STABILIZE | 32.0 | 7 | 9 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06832493841648102 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 2 | 3-7 | 187 | BUY | STABILIZE | 32.0 | 7 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2690102458000183 | 0.0 | 0.0 | +813260b6-a1b8-4a5c-978e-acd60b6b1082 / -— |
| Jogador 2 | 3-7 | 188 | BUY_XP | STABILIZE | 32.0 | 7 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 189 | SELL | STABILIZE | 32.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03433333337306976 | 0.0 | 0.0 | +— / -813260b6-a1b8-4a5c-978e-acd60b6b1082 |
| Jogador 2 | 3-7 | 190 | SELL | STABILIZE | 32.0 | 7 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050333332270383835 | 0.0 | 0.0 | +— / -ed0dab77-fd87-4677-8428-7505ccd34b86 |
| Jogador 2 | 4-1 | 192 | BUY | STABILIZE | 32.0 | 7 | 11 | 1 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.14812366664409637 | 0.0 | 0.0 | +a4188ec8-4188-4fdf-8d76-c559fc0c7daf / -— |
| Jogador 2 | 4-1 | 193 | BUY | STABILIZE | 32.0 | 7 | 8 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07350358366966248 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 2 | 4-1 | 194 | BUY | STABILIZE | 32.0 | 7 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2882620394229889 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 2 | 4-1 | 195 | CRAFT_AND_EQUIP | STABILIZE | 32.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1756727248430252 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 196 | CRAFT_AND_EQUIP | STABILIZE | 32.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22012890875339508 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 197 | MOVE_BENCH | STABILIZE | 32.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40679213404655457 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 1 | 0 | 28.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015130309388041496 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 1 | 0 | 28.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014909714460372925 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 200 | PASS | STABILIZE | 32.0 | 7 | 1 | 0 | 28.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 202 | BUY | STABILIZE | 32.0 | 7 | 7 | 0 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8542308807373047 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-2 | 203 | MOVE_BENCH | STABILIZE | 32.0 | 7 | 6 | 0 | 24.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34972721338272095 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 204 | BUY | STABILIZE | 32.0 | 7 | 6 | 0 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012333536520600319 | 0.0 | 0.0 | +3fdd5708-2e07-4636-a598-d872f57e1c16 / -— |
| Jogador 2 | 4-2 | 205 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 3 | 0 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.5519782866467722e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 206 | BUY | STABILIZE | 32.0 | 7 | 3 | 0 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06264067441225052 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -— |
| Jogador 2 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 1 | 0 | 28.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005656015709973872 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 1 | 0 | 28.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014433097094297409 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 209 | PASS | STABILIZE | 32.0 | 7 | 1 | 0 | 28.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 212 | BUY | ALL_IN | 20.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3157823383808136 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 2 | 4-3 | 213 | BUY | ALL_IN | 20.0 | 7 | 3 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4025171995162964 | 0.0 | 0.0 | +26462e09-ab6e-4b87-85a8-6bda974b0c45 / -— |
| Jogador 2 | 4-3 | 214 | MOVE_BOARD | ALL_IN | 20.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 215 | MOVE_BOARD | ALL_IN | 20.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015001068823039532 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 216 | PASS | ALL_IN | 20.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3199999928474426 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 222 | SELL | ALL_IN | 7.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -23793b7b-2dab-48f0-a8ba-db85fc14c1c5 |
| Jogador 2 | 4-4 | 223 | BUY | ALL_IN | 7.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3942619562149048 | 0.0 | 0.0 | +b5b3098f-d48c-42b8-8022-639a25225980 / -— |
| Jogador 2 | 4-4 | 224 | SELL | ALL_IN | 7.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012071716599166393 | 0.0 | 0.0 | +— / -3fdd5708-2e07-4636-a598-d872f57e1c16 |
| Jogador 2 | 4-4 | 225 | BUY | ALL_IN | 7.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025418581441044807 | 0.0 | 0.0 | +fb551efa-6ad5-4f97-aa05-bc5eb70943d4 / -— |
| Jogador 2 | 4-4 | 226 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.107849336942309e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 227 | SELL | ALL_IN | 7.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00563333323225379 | 0.0 | 0.0 | +— / -fb551efa-6ad5-4f97-aa05-bc5eb70943d4 |
| Jogador 2 | 4-4 | 228 | BUY | ALL_IN | 7.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21200525760650635 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 2 | 4-4 | 229 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 7 | 0 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 230 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 7 | 0 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499974261969328 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 232 | SELL | ALL_IN | 7.0 | 7 | 13 | 1 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0018333332845941186 | 0.0 | 0.0 | +— / -29a44465-8a09-49e7-abfc-a27e987543f1 |
| Jogador 2 | 4-5 | 233 | BUY | ALL_IN | 7.0 | 7 | 14 | 1 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8359854817390442 | 0.0 | 0.0 | +c49cf468-6fa4-4d94-bc3a-9dc8f7111626 / -— |
| Jogador 2 | 4-5 | 234 | SELL | ALL_IN | 7.0 | 7 | 11 | 1 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0042778560891747475 | 0.0 | 0.0 | +— / -59304448-26ee-4e38-a52e-014e22ece127 |
| Jogador 2 | 4-5 | 235 | BUY | ALL_IN | 7.0 | 7 | 15 | 1 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8320786952972412 | 0.0 | 0.0 | +9d2d95f2-c079-43eb-a4cd-37b224a473a8 / -— |
| Jogador 2 | 4-5 | 236 | SELL | ALL_IN | 7.0 | 7 | 12 | 1 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025279102846980095 | 0.0 | 0.0 | +— / -e0445166-70a5-4135-a45e-ff238a95b228 |
| Jogador 2 | 4-5 | 237 | BUY | ALL_IN | 7.0 | 7 | 16 | 1 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31638243794441223 | 0.0 | 0.0 | +fcc4f620-7b85-40ed-a42c-2eadd37a82fd / -— |
| Jogador 2 | 4-5 | 238 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 14 | 1 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 239 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 14 | 1 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016330596059560776 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 240 | PASS | ALL_IN | 7.0 | 7 | 14 | 1 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3199999928474426 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 242 | SELL | ALL_IN | 7.0 | 7 | 21 | 2 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5501125454902649 | 0.0 | 0.0 | +— / -1be0cdcc-ee10-44dc-ad1b-de9b53b25164 |
| Jogador 2 | 4-6 | 243 | BUY | ALL_IN | 7.0 | 7 | 24 | 2 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36492809653282166 | 0.0 | 0.0 | +772bccc4-15f4-4de2-95f8-82d0ed9a72d2 / -— |
| Jogador 2 | 4-6 | 244 | SELL | ALL_IN | 7.0 | 7 | 23 | 2 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007189652882516384 | 0.0 | 0.0 | +— / -b5b3098f-d48c-42b8-8022-639a25225980 |
| Jogador 2 | 4-6 | 245 | BUY | ALL_IN | 7.0 | 7 | 26 | 2 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3716614842414856 | 0.0 | 0.0 | +6e1d8af0-7f7c-4ec1-967c-e871072bc4e3 / -— |
| Jogador 2 | 4-6 | 246 | SELL | ALL_IN | 7.0 | 7 | 25 | 2 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7184000015258789 | 0.0 | 0.0 | +— / -772bccc4-15f4-4de2-95f8-82d0ed9a72d2 |
| Jogador 2 | 4-6 | 247 | BUY | ALL_IN | 7.0 | 7 | 26 | 2 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027847349643707275 | 0.0 | 0.0 | +99182042-c4b9-4801-b66a-1f4432d301f3 / -— |
| Jogador 2 | 4-6 | 248 | SELL | ALL_IN | 7.0 | 7 | 24 | 2 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -99182042-c4b9-4801-b66a-1f4432d301f3 |
| Jogador 2 | 4-6 | 249 | BUY | ALL_IN | 7.0 | 7 | 26 | 2 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03401253744959831 | 0.0 | 0.0 | +4a885bc0-41b4-43f1-94d3-8e755a10645c / -— |
| Jogador 2 | 4-6 | 250 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 25 | 2 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00019469609833322465 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 252 | SELL | ALL_IN | 7.0 | 7 | 34 | 3 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005966666620224714 | 0.0 | 0.0 | +— / -4a885bc0-41b4-43f1-94d3-8e755a10645c |
| Jogador 2 | 4-7 | 253 | BUY | ALL_IN | 7.0 | 7 | 35 | 3 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08778772503137589 | 0.0 | 0.0 | +d80c845d-24bc-4053-a60d-5d0122839b0c / -— |
| Jogador 2 | 4-7 | 254 | SELL | ALL_IN | 7.0 | 7 | 34 | 3 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023736385628581047 | 0.0 | 0.0 | +— / -d80c845d-24bc-4053-a60d-5d0122839b0c |
| Jogador 2 | 4-7 | 255 | BUY | ALL_IN | 7.0 | 7 | 35 | 3 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20345203578472137 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -— |
| Jogador 2 | 4-7 | 256 | SELL | ALL_IN | 7.0 | 7 | 33 | 3 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0022387944627553225 | 0.0 | 0.0 | +— / -a3def045-2a10-4672-a6d6-255c40fd1c90 |
| Jogador 2 | 4-7 | 257 | BUY | ALL_IN | 7.0 | 7 | 35 | 3 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2815170884132385 | 0.0 | 0.0 | +57d86f23-f167-472f-9878-21dcddc0a5f7 / -— |
| Jogador 2 | 4-7 | 258 | SELL | ALL_IN | 7.0 | 7 | 33 | 3 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -57d86f23-f167-472f-9878-21dcddc0a5f7 |
| Jogador 2 | 4-7 | 259 | BUY | ALL_IN | 7.0 | 7 | 35 | 3 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25859469175338745 | 0.0 | 0.0 | +362f7357-283e-4f88-bff3-ffa6314af821 / -— |
| Jogador 2 | 4-7 | 260 | SELL | ALL_IN | 7.0 | 7 | 34 | 3 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014633333310484886 | 0.0 | 0.0 | +— / -362f7357-283e-4f88-bff3-ffa6314af821 |
| Jogador 2 | 5-1 | 262 | BUY | ALL_IN | 7.0 | 7 | 44 | 4 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.396877259016037 | 0.0 | 0.0 | +e5f38fbd-826a-4067-a33f-86cf7eb98f30 / -— |
| Jogador 2 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 7.0 | 7 | 41 | 4 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09490508586168289 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 264 | CRAFT_AND_EQUIP | ALL_IN | 7.0 | 7 | 41 | 4 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.055538736283779144 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 265 | SELL | ALL_IN | 7.0 | 7 | 41 | 4 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7184000015258789 | 0.0 | 0.0 | +— / -6e1d8af0-7f7c-4ec1-967c-e871072bc4e3 |
| Jogador 2 | 5-1 | 266 | BUY | ALL_IN | 7.0 | 7 | 42 | 4 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3605104088783264 | 0.0 | 0.0 | +55cd39c0-65d5-410e-917e-501f584115fa / -— |
| Jogador 2 | 5-1 | 267 | SELL | ALL_IN | 7.0 | 7 | 39 | 3 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46986502408981323 | 0.0 | 0.0 | +— / -e5f38fbd-826a-4067-a33f-86cf7eb98f30 |
| Jogador 2 | 5-1 | 268 | BUY | ALL_IN | 7.0 | 7 | 42 | 4 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23392832279205322 | 0.0 | 0.0 | +98b600a1-736b-437d-a69e-8a7f7235d9c3 / -— |
| Jogador 2 | 5-1 | 269 | SELL | ALL_IN | 7.0 | 7 | 37 | 3 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08529999852180481 | 0.0 | 0.0 | +— / -98b600a1-736b-437d-a69e-8a7f7235d9c3 |
| Jogador 2 | 5-1 | 270 | BUY | ALL_IN | 7.0 | 7 | 42 | 4 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027813546359539032 | 0.0 | 0.0 | +c7a7408a-e7bd-428d-9935-4d5a002d8d9f / -— |
| Jogador 2 | 5-2 | 272 | SELL | ALL_IN | 7.0 | 7 | 51 | 5 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -c7a7408a-e7bd-428d-9935-4d5a002d8d9f |
| Jogador 2 | 5-2 | 273 | BUY | ALL_IN | 7.0 | 7 | 53 | 5 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4244336783885956 | 0.0 | 0.0 | +9f445115-49cc-4647-91a0-a80e347e9c62 / -— |
| Jogador 2 | 5-2 | 274 | SELL | ALL_IN | 7.0 | 7 | 49 | 4 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027899999171495438 | 0.0 | 0.0 | +— / -55cd39c0-65d5-410e-917e-501f584115fa |
| Jogador 2 | 5-2 | 275 | BUY | ALL_IN | 7.0 | 7 | 52 | 5 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11116835474967957 | 0.0 | 0.0 | +b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 / -— |
| Jogador 2 | 5-2 | 276 | SELL | ALL_IN | 7.0 | 7 | 49 | 4 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04956666752696037 | 0.0 | 0.0 | +— / -b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 |
| Jogador 2 | 5-2 | 277 | BUY | ALL_IN | 7.0 | 7 | 52 | 5 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05247752368450165 | 0.0 | 0.0 | +7a48aa2d-a43b-4e49-8230-77f4f2860cb2 / -— |
| Jogador 2 | 5-2 | 278 | SELL | ALL_IN | 7.0 | 7 | 49 | 4 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08076939731836319 | 0.0 | 0.0 | +— / -7a48aa2d-a43b-4e49-8230-77f4f2860cb2 |
| Jogador 2 | 5-2 | 279 | BUY | ALL_IN | 7.0 | 7 | 52 | 5 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2793096601963043 | 0.0 | 0.0 | +b701c6c1-2e19-44b9-ad6e-e5d64e1d364c / -— |
| Jogador 2 | 5-2 | 280 | SELL | ALL_IN | 7.0 | 7 | 50 | 5 | 32.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0061333333142101765 | 0.0 | 0.0 | +— / -b701c6c1-2e19-44b9-ad6e-e5d64e1d364c |
| Jogador 2 | 5-3 | 282 | BUY | ALL_IN | 7.0 | 7 | 64 | 5 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0800986289978027 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -74b1cd6f-12f4-4287-a5f6-9d016663ccf5,9d2d95f2-c079-43eb-a4cd-37b224a473a8 |
| Jogador 2 | 5-3 | 283 | BUY | ALL_IN | 7.0 | 7 | 61 | 5 | 26.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0797817707061768 | 0.0 | 0.0 | +ad363fca-33b7-4257-99d6-7093df66caf6 / -63304cf5-4aa7-473e-9bfb-ec04cd68ebbd,6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 5-3 | 284 | BUY | ALL_IN | 7.0 | 7 | 59 | 5 | 22.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4492751359939575 | 0.0 | 0.0 | +33e9808b-2f92-49e7-ac35-1f6f9388edef / -— |
| Jogador 2 | 5-3 | 285 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 57 | 5 | 22.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10209917277097702 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 286 | BUY | ALL_IN | 7.0 | 7 | 57 | 5 | 28.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.850353479385376 | 0.0 | 0.0 | +64215569-2a69-410d-a2f9-172544bef858 / -26462e09-ab6e-4b87-85a8-6bda974b0c45,a4188ec8-4188-4fdf-8d76-c559fc0c7daf |
| Jogador 2 | 5-3 | 287 | BUY | ALL_IN | 7.0 | 7 | 54 | 5 | 28.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15169379115104675 | 0.0 | 0.0 | +499f10b9-47ba-4cab-add1-31b452acae6d / -— |
| Jogador 2 | 5-3 | 288 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 51 | 5 | 28.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4641285538673401 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 289 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 51 | 5 | 36.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 290 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 51 | 5 | 36.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 292 | BUY | ALL_IN | 7.0 | 7 | 62 | 5 | 36.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5018026828765869 | 0.0 | 0.0 | +3329c812-11fa-4335-a982-f03e6ab28ee0 / -— |
| Jogador 2 | 5-4 | 293 | BUY | ALL_IN | 7.0 | 7 | 61 | 5 | 36.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6213914155960083 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -— |
| Jogador 2 | 5-4 | 294 | SELL | ALL_IN | 7.0 | 7 | 58 | 5 | 36.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06710000336170197 | 0.0 | 0.0 | +— / -64215569-2a69-410d-a2f9-172544bef858 |
| Jogador 2 | 5-4 | 295 | BUY | ALL_IN | 7.0 | 7 | 66 | 5 | 36.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4499434530735016 | 0.0 | 0.0 | +d9097eba-c1b2-4df8-9e5d-a9134dbfe52f / -— |
| Jogador 2 | 5-4 | 296 | SELL | ALL_IN | 7.0 | 7 | 65 | 5 | 36.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7268999814987183 | 0.0 | 0.0 | +— / -ad363fca-33b7-4257-99d6-7093df66caf6 |
| Jogador 2 | 5-4 | 297 | BUY | ALL_IN | 7.0 | 7 | 70 | 5 | 36.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24557851254940033 | 0.0 | 0.0 | +98991369-e5f0-4725-928c-f2fa5362bf73 / -— |
| Jogador 2 | 5-4 | 298 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 65 | 5 | 36.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04231233149766922 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 299 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 65 | 5 | 36.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 300 | MOVE_BOARD | ALL_IN | 7.0 | 7 | 65 | 5 | 36.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013817215338349342 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 302 | SELL | ALL_IN | 7.0 | 7 | 76 | 5 | 36.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7307999730110168 | 0.0 | 0.0 | +— / -908d49c8-626c-44b5-9b03-6a85442f358b |
| Jogador 2 | 5-5 | 303 | BUY | ALL_IN | 7.0 | 7 | 84 | 5 | 36.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06706637889146805 | 0.0 | 0.0 | +7de5aac5-85d7-4add-b5a7-1c89be9d7e40 / -— |
| Jogador 2 | 5-5 | 304 | SELL | ALL_IN | 7.0 | 7 | 80 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -7de5aac5-85d7-4add-b5a7-1c89be9d7e40 |
| Jogador 2 | 5-5 | 305 | BUY | ALL_IN | 7.0 | 7 | 84 | 5 | 36.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16823755204677582 | 0.0 | 0.0 | +407092ea-3a14-4555-9ebd-64a36c41d1d0 / -— |
| Jogador 2 | 5-5 | 306 | SELL | ALL_IN | 7.0 | 7 | 81 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -407092ea-3a14-4555-9ebd-64a36c41d1d0 |
| Jogador 2 | 5-5 | 307 | BUY | ALL_IN | 7.0 | 7 | 84 | 5 | 36.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27173471450805664 | 0.0 | 0.0 | +674bcfdb-fddd-498c-ba65-ef3a3b989f07 / -— |
| Jogador 2 | 5-5 | 308 | SELL | ALL_IN | 7.0 | 7 | 82 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -674bcfdb-fddd-498c-ba65-ef3a3b989f07 |
| Jogador 2 | 5-5 | 309 | BUY | ALL_IN | 7.0 | 7 | 84 | 5 | 36.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27173471450805664 | 0.0 | 0.0 | +2b89bd83-8449-4c63-9da2-62a46c68bdf5 / -— |
| Jogador 2 | 5-5 | 310 | REROLL | ALL_IN | 7.0 | 7 | 82 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 312 | SELL | ALL_IN | 7.0 | 7 | 93 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -2b89bd83-8449-4c63-9da2-62a46c68bdf5 |
| Jogador 2 | 5-6 | 313 | BUY | ALL_IN | 7.0 | 7 | 95 | 5 | 36.0 | Colosso/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4241970479488373 | 0.0 | 0.0 | +40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b / -— |
| Jogador 2 | 5-6 | 314 | SELL | ALL_IN | 7.0 | 7 | 92 | 5 | 36.0 | Colosso/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06233333423733711 | 0.0 | 0.0 | +— / -98991369-e5f0-4725-928c-f2fa5362bf73 |
| Jogador 2 | 5-6 | 315 | BUY | ALL_IN | 7.0 | 7 | 97 | 5 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05995452404022217 | 0.0 | 0.0 | +7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 / -— |
| Jogador 2 | 5-6 | 316 | SELL | ALL_IN | 7.0 | 7 | 94 | 5 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 |
| Jogador 2 | 5-6 | 317 | BUY | ALL_IN | 7.0 | 7 | 97 | 5 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00858042761683464 | 0.0 | 0.0 | +c2bf43be-e6e1-47ed-bcb4-606e37f26671 / -— |
| Jogador 2 | 5-6 | 318 | SELL | ALL_IN | 7.0 | 7 | 93 | 5 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -c2bf43be-e6e1-47ed-bcb4-606e37f26671 |
| Jogador 2 | 5-6 | 319 | BUY | ALL_IN | 7.0 | 7 | 97 | 5 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.049289826303720474 | 0.0 | 0.0 | +b58c0c0e-9c6f-4977-91d1-177b7113c439 / -— |
| Jogador 2 | 5-6 | 320 | SELL | ALL_IN | 7.0 | 7 | 94 | 5 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013539480045437813 | 0.0 | 0.0 | +— / -b58c0c0e-9c6f-4977-91d1-177b7113c439 |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22444601356983185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0904720276594162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40667274594306946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0396608114242554 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.117977499961853 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009961719624698162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 30 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5896894335746765 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 41 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22666983306407928 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2118057906627655 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 45 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26502329111099243 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25187569856643677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23012398183345795 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3955835998058319 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21856972575187683 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007629113737493753 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012296375818550587 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015378622338175774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 60 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9605743885040283 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 63 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33713147044181824 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 64 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33249542117118835 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26758691668510437 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 75 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8901172876358032 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 83 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 84 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.898055911064148 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 93 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 94 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001564412610605359 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10375984758138657 | 0.0 | 0.0 | +— / -5ead8548-7453-4fa1-856e-674995576a48 |
| Jogador 3 | 2-5 | 96 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09825731813907623 | 0.0 | 0.0 | +— / -f19f9e7f-f189-47fe-b571-be5065c6eb39 |
| Jogador 3 | 2-5 | 97 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1627606898546219 | 0.0 | 0.0 | +cdb48eea-209d-4833-9a68-79df61990332 / -— |
| Jogador 3 | 2-5 | 98 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0689999982714653 | 0.0 | 0.0 | +— / -cdb48eea-209d-4833-9a68-79df61990332 |
| Jogador 3 | 2-5 | 99 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 100 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 16.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18206821382045746 | 0.0 | 0.0 | +— / -41db1132-4e1c-48eb-8a9b-1b2c74cb22ce |
| Jogador 3 | 2-6 | 102 | BUY | STABILIZE | 89.0 | 5 | 8 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.045701026916504 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -c70251e8-af44-4466-808f-d49e9e5f57e9,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-6 | 103 | BUY | STABILIZE | 89.0 | 5 | 6 | 0 | 12.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479953289031982 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 5 | 0 | 10.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3978379964828491 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 105 | BUY_XP | STABILIZE | 89.0 | 5 | 5 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 106 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 1 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4007910192012787 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 107 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 1 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3189530074596405 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 109 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0159311443567276 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 110 | PASS | STABILIZE | 89.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 112 | BUY | FAST8 | 89.0 | 6 | 7 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9641535878181458 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 113 | BUY | FAST8 | 89.0 | 6 | 4 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33308669924736023 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 3 | 2-7 | 114 | BUY | FAST8 | 89.0 | 6 | 2 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3135092854499817 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 115 | MOVE_BOARD | FAST8 | 89.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0001243629230884835 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 116 | MOVE_BOARD | FAST8 | 89.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 117 | PASS | FAST8 | 89.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 122 | CRAFT_AND_EQUIP | FAST8 | 89.0 | 6 | 6 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2631056606769562 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 123 | BUY | FAST8 | 89.0 | 6 | 6 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19200095534324646 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-1 | 124 | MOVE_BOARD | FAST8 | 89.0 | 6 | 3 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.351080421358347e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 125 | BUY | FAST8 | 89.0 | 6 | 3 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010044346563518047 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -— |
| Jogador 3 | 3-1 | 126 | MOVE_BOARD | FAST8 | 89.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00030264712404459715 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 127 | MOVE_BOARD | FAST8 | 89.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015204341150820255 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 128 | MOVE_BOARD | FAST8 | 89.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014745784923434258 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 129 | PASS | FAST8 | 89.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 132 | BUY | FAST8 | 89.0 | 6 | 8 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.741909384727478 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 3-2 | 133 | MOVE_BENCH | FAST8 | 89.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40010151267051697 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 134 | BUY | FAST8 | 89.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2462332546710968 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 3 | 3-2 | 135 | MOVE_BOARD | FAST8 | 89.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -7.742900197627023e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 136 | MOVE_BOARD | FAST8 | 89.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 137 | PASS | FAST8 | 89.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 142 | BUY | FAST8 | 89.0 | 6 | 11 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6556245684623718 | 0.0 | 0.0 | +f0b6c16b-7610-454c-929d-7152f0a041d3 / -— |
| Jogador 3 | 3-3 | 143 | BUY | FAST8 | 89.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25709107518196106 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-3 | 144 | MOVE_BOARD | FAST8 | 89.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0002011680044233799 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 145 | MOVE_BOARD | FAST8 | 89.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014840573072433472 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 146 | PASS | FAST8 | 89.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 152 | SELL | FAST8 | 78.0 | 6 | 10 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41575556993484497 | 0.0 | 0.0 | +— / -2d1296a3-9aa4-42ab-8b86-34661e32a63d |
| Jogador 3 | 3-4 | 153 | BUY | FAST8 | 78.0 | 6 | 13 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7108652591705322 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 3 | 3-4 | 154 | MOVE_BOARD | FAST8 | 78.0 | 6 | 10 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.5523880544351414e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 155 | MOVE_BOARD | FAST8 | 78.0 | 6 | 10 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 156 | MOVE_BOARD | FAST8 | 78.0 | 6 | 10 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015088589861989021 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 157 | PASS | FAST8 | 78.0 | 6 | 10 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 162 | SELL | FAST8 | 78.0 | 6 | 16 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 |
| Jogador 3 | 3-5 | 163 | BUY | FAST8 | 78.0 | 6 | 19 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7540603876113892 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -c3f8419e-a450-4247-bb65-8de8dba1c8ee,d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 3 | 3-5 | 164 | BUY | FAST8 | 78.0 | 6 | 16 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21001045405864716 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 165 | MOVE_BOARD | FAST8 | 78.0 | 6 | 13 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004584055859595537 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 166 | MOVE_BOARD | FAST8 | 78.0 | 6 | 13 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 167 | MOVE_BOARD | FAST8 | 78.0 | 6 | 13 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016714412719011307 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 168 | PASS | FAST8 | 78.0 | 6 | 13 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 172 | BUY | FAST8 | 78.0 | 6 | 20 | 2 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7009481191635132 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -bca8862c-5e5b-4a51-9173-79218fbfea3d,f0b6c16b-7610-454c-929d-7152f0a041d3 |
| Jogador 3 | 3-6 | 173 | BUY | FAST8 | 78.0 | 6 | 18 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2519296407699585 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 3 | 3-6 | 174 | BUY | FAST8 | 78.0 | 6 | 15 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.090779148042202 | 0.0 | 0.0 | +1489b596-9339-407a-b49f-d01ecfdd6f78 / -— |
| Jogador 3 | 3-6 | 175 | MOVE_BOARD | FAST8 | 78.0 | 6 | 14 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 176 | MOVE_BOARD | FAST8 | 78.0 | 6 | 14 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014918859116733074 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 177 | PASS | FAST8 | 78.0 | 6 | 14 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 182 | SELL | FAST8 | 67.0 | 6 | 20 | 2 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -a9c52953-4532-455b-851f-04079adfd354 |
| Jogador 3 | 3-7 | 183 | BUY | FAST8 | 67.0 | 6 | 28 | 2 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2673121690750122 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 184 | SELL | FAST8 | 67.0 | 6 | 25 | 2 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7534999847412109 | 0.0 | 0.0 | +— / -0e31b1ec-3ead-480e-8577-f59bb5486d00 |
| Jogador 3 | 3-7 | 185 | BUY | FAST8 | 67.0 | 6 | 30 | 3 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14717097580432892 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-7 | 186 | MOVE_BOARD | FAST8 | 67.0 | 6 | 27 | 2 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005095069645904005 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 187 | MOVE_BENCH | FAST8 | 67.0 | 6 | 27 | 2 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6598384380340576 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 188 | PASS | FAST8 | 67.0 | 6 | 27 | 2 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023499999195337296 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 67.0 | 6 | 34 | 3 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18210986256599426 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 67.0 | 6 | 34 | 3 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12921471893787384 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 194 | SELL | FAST8 | 67.0 | 6 | 34 | 3 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 4-1 | 195 | BUY | FAST8 | 67.0 | 6 | 37 | 3 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7684397101402283 | 0.0 | 0.0 | +15d93457-0760-419e-87db-74223c1cb7f4 / -— |
| Jogador 3 | 4-1 | 196 | EQUIP_FROM_INVENTORY | FAST8 | 67.0 | 6 | 34 | 3 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15351566672325134 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 197 | MOVE_BENCH | FAST8 | 67.0 | 6 | 34 | 3 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06906726956367493 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 198 | SELL | FAST8 | 67.0 | 6 | 34 | 3 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007594909518957138 | 0.0 | 0.0 | +— / -1489b596-9339-407a-b49f-d01ecfdd6f78 |
| Jogador 3 | 4-1 | 199 | BUY | FAST8 | 67.0 | 6 | 35 | 3 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7658922076225281 | 0.0 | 0.0 | +f64919a5-eb2c-4e23-91ed-0067b3d90951 / -— |
| Jogador 3 | 4-1 | 200 | MOVE_BOARD | FAST8 | 67.0 | 6 | 32 | 3 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 202 | SELL | FAST8 | 53.0 | 6 | 41 | 4 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03138023242354393 | 0.0 | 0.0 | +— / -2fa86b11-4e28-4652-890e-f00a79068223 |
| Jogador 3 | 4-2 | 203 | BUY | FAST8 | 53.0 | 6 | 43 | 4 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7764244675636292 | 0.0 | 0.0 | +9bd6852a-b7a4-468c-a8cc-5318f7906eae / -— |
| Jogador 3 | 4-2 | 204 | SELL | FAST8 | 53.0 | 6 | 41 | 4 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0141333332285285 | 0.0 | 0.0 | +— / -527f78df-1e51-4731-9175-1c4812aa82ad |
| Jogador 3 | 4-2 | 205 | BUY | FAST8 | 53.0 | 6 | 45 | 4 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03214315325021744 | 0.0 | 0.0 | +967ab606-d775-468a-9c11-5ad0fd0e92f8 / -— |
| Jogador 3 | 4-2 | 206 | SELL | FAST8 | 53.0 | 6 | 44 | 4 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024374838918447495 | 0.0 | 0.0 | +— / -967ab606-d775-468a-9c11-5ad0fd0e92f8 |
| Jogador 3 | 4-2 | 207 | BUY | FAST8 | 53.0 | 6 | 45 | 4 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15956230461597443 | 0.0 | 0.0 | +974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 / -— |
| Jogador 3 | 4-2 | 208 | MOVE_BOARD | FAST8 | 53.0 | 6 | 43 | 4 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0008409502916038036 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 209 | MOVE_BENCH | FAST8 | 53.0 | 6 | 43 | 4 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6578344702720642 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 210 | MOVE_BENCH | FAST8 | 53.0 | 6 | 43 | 4 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08530238270759583 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 212 | SELL | FAST8 | 53.0 | 6 | 53 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010017246939241886 | 0.0 | 0.0 | +— / -974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 |
| Jogador 3 | 4-3 | 213 | BUY | FAST8 | 53.0 | 6 | 55 | 5 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.031216317787766457 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -— |
| Jogador 3 | 4-3 | 214 | SELL | FAST8 | 53.0 | 6 | 52 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022188881412148476 | 0.0 | 0.0 | +— / -d8ecc66e-097d-4caa-a657-90fcd1286c2b |
| Jogador 3 | 4-3 | 215 | BUY | FAST8 | 53.0 | 6 | 55 | 5 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00894040334969759 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 3 | 4-3 | 216 | SELL | FAST8 | 53.0 | 6 | 54 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026419339701533318 | 0.0 | 0.0 | +— / -27a4bd22-9c1f-4f9f-9192-06ea4933feb5 |
| Jogador 3 | 4-3 | 217 | BUY | FAST8 | 53.0 | 6 | 55 | 5 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11713217198848724 | 0.0 | 0.0 | +16acc555-c819-4f7c-b406-2f48f11ffc87 / -— |
| Jogador 3 | 4-3 | 218 | MOVE_BOARD | FAST8 | 53.0 | 6 | 52 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 219 | MOVE_BOARD | FAST8 | 53.0 | 6 | 52 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01569654606282711 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 220 | PASS | FAST8 | 53.0 | 6 | 52 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08101436495780945 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 222 | SELL | FAST8 | 40.0 | 6 | 62 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -16acc555-c819-4f7c-b406-2f48f11ffc87 |
| Jogador 3 | 4-4 | 223 | BUY | FAST8 | 40.0 | 6 | 65 | 5 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2733214497566223 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -— |
| Jogador 3 | 4-4 | 224 | SELL | FAST8 | 40.0 | 6 | 62 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -ad19ac66-9f86-4c29-8ae7-7222164aece1 |
| Jogador 3 | 4-4 | 225 | BUY | FAST8 | 40.0 | 6 | 65 | 5 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27833089232444763 | 0.0 | 0.0 | +b80a9778-b2ce-411b-8d08-24549c04367c / -— |
| Jogador 3 | 4-4 | 226 | MOVE_BOARD | FAST8 | 40.0 | 6 | 63 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 227 | MOVE_BOARD | FAST8 | 40.0 | 6 | 63 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 228 | PASS | FAST8 | 40.0 | 6 | 63 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09857280552387238 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 232 | SELL | FAST8 | 40.0 | 6 | 73 | 5 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -b80a9778-b2ce-411b-8d08-24549c04367c |
| Jogador 3 | 4-5 | 233 | BUY | FAST8 | 40.0 | 6 | 75 | 5 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8927230834960938 | 0.0 | 0.0 | +8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e / -aaa84ce8-7919-4ec3-92eb-cc03a9decca9,f64919a5-eb2c-4e23-91ed-0067b3d90951 |
| Jogador 3 | 4-5 | 234 | BUY | FAST8 | 40.0 | 6 | 72 | 5 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07702190428972244 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 3 | 4-5 | 235 | MOVE_BOARD | FAST8 | 40.0 | 6 | 70 | 5 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 236 | MOVE_BOARD | FAST8 | 40.0 | 6 | 70 | 5 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 237 | PASS | FAST8 | 40.0 | 6 | 70 | 5 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.244325652718544 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 242 | BUY | FAST8 | 40.0 | 6 | 81 | 5 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3303873538970947 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -— |
| Jogador 3 | 4-6 | 243 | SELL | FAST8 | 40.0 | 6 | 79 | 5 | 34.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e |
| Jogador 3 | 4-6 | 244 | BUY | FAST8 | 40.0 | 6 | 87 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32649752497673035 | 0.0 | 0.0 | +51a5a5d7-c5ea-43e2-a521-22fe0275c231 / -— |
| Jogador 3 | 4-6 | 245 | SELL | FAST8 | 40.0 | 6 | 86 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0476946085691452 | 0.0 | 0.0 | +— / -f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 |
| Jogador 3 | 4-6 | 246 | BUY | FAST8 | 40.0 | 6 | 88 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27623310685157776 | 0.0 | 0.0 | +241a8a03-6e6f-4a9a-8550-e9154f3e1e76 / -— |
| Jogador 3 | 4-6 | 247 | MOVE_BOARD | FAST8 | 40.0 | 6 | 86 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006965452339500189 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 248 | MOVE_BOARD | FAST8 | 40.0 | 6 | 86 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 249 | MOVE_BOARD | FAST8 | 40.0 | 6 | 86 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01569654606282711 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 250 | PASS | FAST8 | 40.0 | 6 | 86 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11806666105985641 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 252 | SELL | STABILIZE | 27.0 | 6 | 96 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -51a5a5d7-c5ea-43e2-a521-22fe0275c231 |
| Jogador 3 | 4-7 | 253 | BUY | STABILIZE | 27.0 | 6 | 97 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9655792117118835 | 0.0 | 0.0 | +deb56311-9843-48be-9a22-3529305d04e5 / -15d93457-0760-419e-87db-74223c1cb7f4,bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed |
| Jogador 3 | 4-7 | 254 | BUY | STABILIZE | 27.0 | 6 | 94 | 5 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9619156122207642 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -9bd6852a-b7a4-468c-a8cc-5318f7906eae,ab6084b0-65df-4a70-8591-687b320d98b6 |
| Jogador 3 | 4-7 | 255 | MOVE_BENCH | STABILIZE | 27.0 | 6 | 92 | 5 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1510494351387024 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 256 | BUY | STABILIZE | 27.0 | 6 | 92 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09790560603141785 | 0.0 | 0.0 | +b70671f9-0d78-4ae8-bd13-0267c96e7207 / -— |
| Jogador 3 | 4-7 | 257 | BUY | STABILIZE | 27.0 | 6 | 90 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1931321620941162 | 0.0 | 0.0 | +de8de4b5-48ea-4947-ae08-2b90d94b0fc1 / -— |
| Jogador 3 | 4-7 | 258 | SELL | STABILIZE | 27.0 | 6 | 87 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -24b29fe6-466c-42d5-9f92-5d6114f0f98f |
| Jogador 3 | 4-7 | 259 | BUY_XP | STABILIZE | 27.0 | 6 | 92 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005200000014156103 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 260 | MOVE_BOARD | STABILIZE | 27.0 | 6 | 88 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 262 | BUY | STABILIZE | 27.0 | 7 | 98 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6243139505386353 | 0.0 | 0.0 | +f32e50e0-1430-4549-a1dd-a8473ffe0bd4 / -— |
| Jogador 3 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 27.0 | 7 | 96 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22150222957134247 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 27.0 | 7 | 96 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15775145590305328 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 265 | SELL | STABILIZE | 27.0 | 7 | 96 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -deb56311-9843-48be-9a22-3529305d04e5 |
| Jogador 3 | 5-1 | 266 | BUY | STABILIZE | 27.0 | 7 | 104 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00935521349310875 | 0.0 | 0.0 | +50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de / -— |
| Jogador 3 | 5-1 | 267 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 103 | 5 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15475685894489288 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 268 | BUY | STABILIZE | 27.0 | 7 | 103 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21910253167152405 | 0.0 | 0.0 | +af98a89b-ee97-45ce-972a-3f41e280b6b2 / -— |
| Jogador 3 | 5-1 | 269 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 102 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00013303104788064957 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 270 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 102 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 272 | BUY | ALL_IN | 11.0 | 7 | 113 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9670730829238892 | 0.0 | 0.0 | +b3905667-bcb5-4e23-94fa-25160b14a95e / -— |
| Jogador 3 | 5-2 | 273 | SELL | ALL_IN | 11.0 | 7 | 112 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -af98a89b-ee97-45ce-972a-3f41e280b6b2 |
| Jogador 3 | 5-2 | 274 | BUY | ALL_IN | 11.0 | 7 | 113 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42208218574523926 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -— |
| Jogador 3 | 5-2 | 275 | MOVE_BOARD | ALL_IN | 11.0 | 7 | 110 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 276 | MOVE_BOARD | ALL_IN | 11.0 | 7 | 110 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 277 | PASS | ALL_IN | 11.0 | 7 | 110 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5558437705039978 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2201479971408844 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09193183481693268 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4641140401363373 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16314318776130676 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0601743720471859 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 30 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 41 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0128071308135986 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33921104669570923 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 43 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9801995158195496 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18384495377540588 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21620437502861023 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 55 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 56 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9554932713508606 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 63 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 64 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 72 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9438962936401367 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 73 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0434504747390747 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 74 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30420270562171936 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 75 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Camille | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5619999766349792 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 76 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 77 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10035977512598038 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 79 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5416666865348816 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-3 | 80 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4083148241043091 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13734230399131775 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23762108385562897 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15833333134651184 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005146525800228119 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11433333158493042 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08100000023841858 | 0.0 | 0.0 | +— / -0b62545c-1de0-47d8-bb4c-119f7e1526b3 |
| Jogador 4 | 2-4 | 89 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24995549023151398 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 90 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9549373388290405 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 4 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0011571645736694 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -86c535a4-a22b-4667-bc0f-46b4843d97cc,8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37761855125427246 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 94 | SELL | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -4b07138d-44fd-4515-8b65-d7db84f4639c |
| Jogador 4 | 2-5 | 95 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3863356113433838 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 4 | 2-5 | 96 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 97 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6152018308639526 | 0.0 | 0.0 | +— / -c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 4 | 2-5 | 98 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 1 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14828945696353912 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 100 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04833975434303284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 102 | BUY | STABILIZE | 90.0 | 6 | 6 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0516248941421509 | 0.0 | 0.0 | +814d07bd-0296-44af-9626-26a8a224d86f / -— |
| Jogador 4 | 2-6 | 103 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31527042388916016 | 0.0 | 0.0 | +f84bb43d-db12-46dd-a15c-28ef8fdb7fa2 / -— |
| Jogador 4 | 2-6 | 104 | SELL | STABILIZE | 90.0 | 6 | 4 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4323016405105591 | 0.0 | 0.0 | +— / -f84bb43d-db12-46dd-a15c-28ef8fdb7fa2 |
| Jogador 4 | 2-6 | 105 | SELL | STABILIZE | 90.0 | 6 | 5 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5572041869163513 | 0.0 | 0.0 | +— / -a92eca5d-299f-4f4d-a16b-d23981ef719f |
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
| Jogador 4 | 2-7 | 120 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 1 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03745700418949127 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 122 | BUY | STABILIZE | 82.0 | 6 | 7 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28148937225341797 | 0.0 | 0.0 | +8052731e-e34c-4de7-84b1-2b986cfeddaa / -— |
| Jogador 4 | 3-1 | 123 | BUY | STABILIZE | 82.0 | 6 | 5 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.31680309772491455 | 0.0 | 0.0 | +6bbf1aa9-e129-45c6-8668-699425d97c5d / -— |
| Jogador 4 | 3-1 | 124 | BUY | STABILIZE | 82.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.25474658608436584 | 0.0 | 0.0 | +cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 / -— |
| Jogador 4 | 3-1 | 125 | CRAFT_AND_EQUIP | STABILIZE | 82.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2364325225353241 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0008337869076058269 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 127 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015028858557343483 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014980264939367771 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 129 | PASS | STABILIZE | 82.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 132 | BUY | STABILIZE | 72.0 | 6 | 8 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379772901535034 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 133 | BUY | STABILIZE | 72.0 | 6 | 7 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879778742790222 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 6 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0152007341384888 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 135 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 6 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46136024594306946 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 136 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 6 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4436812698841095 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 137 | BUY | STABILIZE | 72.0 | 6 | 6 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2744118571281433 | 0.0 | 0.0 | +421bcbcb-ecb2-4af8-88d4-7be6cd284d27 / -— |
| Jogador 4 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 139 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 140 | PASS | STABILIZE | 72.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 142 | BUY | STABILIZE | 61.0 | 6 | 9 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.805484414100647 | 0.0 | 0.0 | +52018505-08c9-471f-83b9-fd5066efe55a / -— |
| Jogador 4 | 3-3 | 143 | BUY | STABILIZE | 61.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06729931384325027 | 0.0 | 0.0 | +58c38a13-23c5-4ac1-8601-f0636aeb33ab / -— |
| Jogador 4 | 3-3 | 144 | BUY | STABILIZE | 61.0 | 6 | 4 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06124130263924599 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 61.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05325847119092941 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 146 | MOVE_BENCH | STABILIZE | 61.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9416804909706116 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 147 | MOVE_BENCH | STABILIZE | 61.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028391843661665916 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 148 | MOVE_BENCH | STABILIZE | 61.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 149 | MOVE_BENCH | STABILIZE | 61.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9433853626251221 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 150 | PASS | STABILIZE | 61.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 152 | SELL | STABILIZE | 49.0 | 6 | 10 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 3-4 | 153 | BUY | STABILIZE | 49.0 | 6 | 13 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8038041591644287 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 154 | EQUIP_FROM_INVENTORY | STABILIZE | 49.0 | 6 | 10 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1560690701007843 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 155 | EQUIP_FROM_INVENTORY | STABILIZE | 49.0 | 6 | 10 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15013685822486877 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 156 | EQUIP_FROM_INVENTORY | STABILIZE | 49.0 | 6 | 10 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08430907875299454 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 157 | SELL | STABILIZE | 49.0 | 6 | 10 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03953489661216736 | 0.0 | 0.0 | +— / -ac8f2a7d-1627-4aa4-a35b-805bce651b0e |
| Jogador 4 | 3-4 | 158 | BUY | STABILIZE | 49.0 | 6 | 11 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7557864189147949 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -52018505-08c9-471f-83b9-fd5066efe55a,8052731e-e34c-4de7-84b1-2b986cfeddaa |
| Jogador 4 | 3-4 | 159 | MOVE_BENCH | STABILIZE | 49.0 | 6 | 9 | 0 | 12.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5089840888977051 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 160 | MOVE_BENCH | STABILIZE | 49.0 | 6 | 9 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5411137342453003 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 162 | BUY | STABILIZE | 49.0 | 6 | 16 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2852853536605835 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -— |
| Jogador 4 | 3-5 | 163 | BUY | STABILIZE | 49.0 | 6 | 14 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45494189858436584 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 4 | 3-5 | 164 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 12 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01331278495490551 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 12 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00121981929987669 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 166 | PASS | STABILIZE | 49.0 | 6 | 12 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 172 | SELL | STABILIZE | 49.0 | 6 | 19 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -7fd03119-ac82-49e1-b3bb-3a0caa31011f |
| Jogador 4 | 3-6 | 173 | BUY | STABILIZE | 49.0 | 6 | 24 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8124022483825684 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 174 | EQUIP_FROM_INVENTORY | STABILIZE | 49.0 | 6 | 21 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13403378427028656 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 175 | EQUIP_FROM_INVENTORY | STABILIZE | 49.0 | 6 | 21 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11166837811470032 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 176 | EQUIP_FROM_INVENTORY | STABILIZE | 49.0 | 6 | 21 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14002755284309387 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 177 | SELL | STABILIZE | 49.0 | 6 | 21 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022099999710917473 | 0.0 | 0.0 | +— / -58c38a13-23c5-4ac1-8601-f0636aeb33ab |
| Jogador 4 | 3-6 | 178 | BUY | STABILIZE | 49.0 | 6 | 24 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8103768229484558 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -— |
| Jogador 4 | 3-6 | 179 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 22 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.061245907098054886 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 180 | MOVE_BOARD | STABILIZE | 49.0 | 6 | 22 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02801797352731228 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 182 | SELL | STABILIZE | 38.0 | 6 | 29 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3073333203792572 | 0.0 | 0.0 | +— / -764470bb-9820-4e49-98f9-5a5f0ce5ca8f |
| Jogador 4 | 3-7 | 183 | BUY | STABILIZE | 38.0 | 6 | 31 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7906996011734009 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-7 | 184 | MOVE_BENCH | STABILIZE | 38.0 | 6 | 28 | 2 | 18.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4422042965888977 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 185 | BUY | STABILIZE | 38.0 | 6 | 28 | 2 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2536640465259552 | 0.0 | 0.0 | +e9d5f645-4afc-44f4-ae53-bc832c49f451 / -— |
| Jogador 4 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 26 | 2 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030024001374840736 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 187 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 26 | 2 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 188 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 26 | 2 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25382789969444275 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 189 | PASS | STABILIZE | 38.0 | 6 | 26 | 2 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08364592492580414 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 192 | BUY | STABILIZE | 38.0 | 6 | 33 | 3 | 22.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.837013840675354 | 0.0 | 0.0 | +465ecc70-f5da-47f4-a7c0-2005a8ed24c1 / -— |
| Jogador 4 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 6 | 32 | 3 | 22.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17893460392951965 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 6 | 32 | 3 | 22.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.212361142039299 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 195 | SELL | STABILIZE | 38.0 | 6 | 32 | 3 | 22.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 4 | 4-1 | 196 | BUY | STABILIZE | 38.0 | 6 | 40 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4910378158092499 | 0.0 | 0.0 | +5637ca02-9946-4d1a-9679-e5c316ef566b / -6bbf1aa9-e129-45c6-8668-699425d97c5d,e9d5f645-4afc-44f4-ae53-bc832c49f451 |
| Jogador 4 | 4-1 | 197 | BUY | STABILIZE | 38.0 | 6 | 38 | 3 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2321241945028305 | 0.0 | 0.0 | +9175d2a8-4736-402d-873b-cf4846b04d97 / -— |
| Jogador 4 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 35 | 3 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2402244657278061 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 35 | 3 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013523761183023453 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 35 | 3 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1460288017988205 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 202 | BUY | ALL_IN | 25.0 | 6 | 44 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9661244750022888 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -23f4d10f-2614-47b2-bfb2-4fb276764b5e,fe6546c3-86ef-40e1-aa7e-ff7e400fe628 |
| Jogador 4 | 4-2 | 203 | BUY | ALL_IN | 25.0 | 6 | 42 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.261974573135376 | 0.0 | 0.0 | +090f2ba6-5514-49ba-a80d-a0711cd06245 / -— |
| Jogador 4 | 4-2 | 204 | REROLL | ALL_IN | 25.0 | 6 | 39 | 3 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 205 | BUY | ALL_IN | 25.0 | 6 | 37 | 3 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3666296899318695 | 0.0 | 0.0 | +6388773b-0e99-40a9-8d68-895dcf16fce6 / -— |
| Jogador 4 | 4-2 | 206 | SELL | ALL_IN | 25.0 | 6 | 35 | 3 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05713333189487457 | 0.0 | 0.0 | +— / -5637ca02-9946-4d1a-9679-e5c316ef566b |
| Jogador 4 | 4-2 | 207 | BUY | ALL_IN | 25.0 | 6 | 40 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3518373668193817 | 0.0 | 0.0 | +ba7f039a-929c-4537-9eb6-f1dc4563cca8 / -— |
| Jogador 4 | 4-2 | 208 | SELL | ALL_IN | 25.0 | 6 | 37 | 3 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -4363594b-375b-45d4-9b1a-0c1ab96367a1 |
| Jogador 4 | 4-2 | 209 | BUY | ALL_IN | 25.0 | 6 | 42 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.049635812640190125 | 0.0 | 0.0 | +ea460790-b046-451d-9174-8b613e476241 / -— |
| Jogador 4 | 4-2 | 210 | REROLL | ALL_IN | 25.0 | 6 | 39 | 3 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 212 | SELL | ALL_IN | 14.0 | 6 | 46 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -9175d2a8-4736-402d-873b-cf4846b04d97 |
| Jogador 4 | 4-3 | 213 | BUY | ALL_IN | 14.0 | 6 | 49 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9171352982521057 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -— |
| Jogador 4 | 4-3 | 214 | SELL | ALL_IN | 14.0 | 6 | 47 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5468862652778625 | 0.0 | 0.0 | +— / -f71a7192-663d-46a0-93ef-b900c59c3bde |
| Jogador 4 | 4-3 | 215 | BUY | ALL_IN | 14.0 | 6 | 49 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05962171405553818 | 0.0 | 0.0 | +badbffc5-dd49-4cd8-8b4d-941ae020e6e3 / -— |
| Jogador 4 | 4-3 | 216 | SELL | ALL_IN | 14.0 | 6 | 46 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010833333246409893 | 0.0 | 0.0 | +— / -badbffc5-dd49-4cd8-8b4d-941ae020e6e3 |
| Jogador 4 | 4-3 | 217 | SELL | ALL_IN | 14.0 | 6 | 49 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49996817111968994 | 0.0 | 0.0 | +— / -090f2ba6-5514-49ba-a80d-a0711cd06245 |
| Jogador 4 | 4-3 | 218 | BUY | ALL_IN | 14.0 | 6 | 52 | 5 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25118592381477356 | 0.0 | 0.0 | +a9588010-57fa-4baf-b226-a30f519342e7 / -— |
| Jogador 4 | 4-3 | 219 | MOVE_BENCH | ALL_IN | 14.0 | 6 | 49 | 4 | 22.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8826879858970642 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 220 | MOVE_BENCH | ALL_IN | 14.0 | 6 | 49 | 4 | 26.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07109145075082779 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 222 | BUY | ALL_IN | 1.0 | 7 | 59 | 5 | 26.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9789547920227051 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -— |
| Jogador 4 | 4-4 | 223 | SELL | ALL_IN | 1.0 | 7 | 56 | 5 | 26.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -a9588010-57fa-4baf-b226-a30f519342e7 |
| Jogador 4 | 4-4 | 224 | BUY | ALL_IN | 1.0 | 7 | 59 | 5 | 26.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018831627443432808 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 4 | 4-4 | 225 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 55 | 5 | 26.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5486183762550354 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 226 | BUY | ALL_IN | 1.0 | 7 | 55 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22369173169136047 | 0.0 | 0.0 | +15c93ffb-d63e-43e6-aa46-ba2beed9cb53 / -— |
| Jogador 4 | 4-4 | 227 | MOVE_BOARD | ALL_IN | 1.0 | 7 | 52 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002583634341135621 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 228 | MOVE_BOARD | ALL_IN | 1.0 | 7 | 52 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 229 | MOVE_BOARD | ALL_IN | 1.0 | 7 | 52 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014672665856778622 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 230 | PASS | ALL_IN | 1.0 | 7 | 52 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48054325580596924 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 232 | SELL | ALL_IN | 1.0 | 7 | 63 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -15c93ffb-d63e-43e6-aa46-ba2beed9cb53 |
| Jogador 4 | 4-5 | 233 | BUY | ALL_IN | 1.0 | 7 | 66 | 5 | 28.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.104830026626587 | 0.0 | 0.0 | +a72137b3-498b-40e1-938a-639f56745f08 / -465ecc70-f5da-47f4-a7c0-2005a8ed24c1,cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 |
| Jogador 4 | 4-5 | 234 | BUY | ALL_IN | 1.0 | 7 | 65 | 5 | 26.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11869942396879196 | 0.0 | 0.0 | +9cc98c55-1b3a-4b31-ae06-f66098e86e8f / -— |
| Jogador 4 | 4-5 | 235 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 62 | 5 | 26.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05507370084524155 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 236 | SELL | ALL_IN | 1.0 | 7 | 62 | 5 | 24.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -ba7f039a-929c-4537-9eb6-f1dc4563cca8 |
| Jogador 4 | 4-5 | 237 | BUY | ALL_IN | 1.0 | 7 | 65 | 5 | 24.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11619493365287781 | 0.0 | 0.0 | +652568b9-7093-4e77-8b9c-7ed286cf7f4c / -— |
| Jogador 4 | 4-5 | 238 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 62 | 5 | 24.0 | Florescer/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4027542173862457 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 239 | MOVE_BOARD | ALL_IN | 1.0 | 7 | 62 | 5 | 30.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015674330294132233 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 240 | BUY | ALL_IN | 1.0 | 7 | 62 | 5 | 30.0 | Florescer/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0629236102104187 | 0.0 | 0.0 | +1ff42607-ccac-4d3f-8277-bccddf08862f / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.26577791571617126 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.24549612402915955 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12370830029249191 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11255644261837006 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17292346060276031 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012102286331355572 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4293290078639984 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2171582281589508 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 41 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3299944996833801 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28838351368904114 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 43 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0326346158981323 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19878919422626495 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21278688311576843 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4088495075702667 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2263445407152176 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 57 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9720179438591003 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 64 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0441603660583496 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12276269495487213 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 75 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2461250126361847 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4363275468349457 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 77 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1628062129020691 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03177344799041748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 79 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2579782009124756 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 80 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3106883466243744 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 83 | BUY | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21873369812965393 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 84 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05810000002384186 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 85 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08818167448043823 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-4 | 86 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 87 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0973338857293129 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-4 | 88 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10482131689786911 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-4 | 89 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1889336258172989 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 90 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1796543449163437 | 0.0 | 0.0 | +32b7b452-7702-43a3-b3c4-8eda786225b9 / -— |
| Jogador 5 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26717713475227356 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 93 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3246573209762573 | 0.0 | 0.0 | +de78e1b7-ed58-42dd-8374-76b578543e94 / -— |
| Jogador 5 | 2-5 | 94 | SELL | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030366666615009308 | 0.0 | 0.0 | +— / -32b7b452-7702-43a3-b3c4-8eda786225b9 |
| Jogador 5 | 2-5 | 95 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 96 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030533334240317345 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-5 | 97 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40817776322364807 | 0.0 | 0.0 | +— / -de78e1b7-ed58-42dd-8374-76b578543e94 |
| Jogador 5 | 2-5 | 98 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.098382368683815 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3566199839115143 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 102 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015697868540883064 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 103 | BUY | STABILIZE | 100.0 | 6 | 5 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021104251965880394 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05602027103304863 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 105 | SELL | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 106 | SELL | STABILIZE | 100.0 | 6 | 5 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3451807200908661 | 0.0 | 0.0 | +— / -135065df-1ebc-413d-86f1-4df28bd3ee41 |
| Jogador 5 | 2-6 | 107 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005923189222812653 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 108 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 109 | SELL | STABILIZE | 100.0 | 6 | 2 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3343333303928375 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-6 | 110 | SELL | STABILIZE | 100.0 | 6 | 3 | 0 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49260789155960083 | 0.0 | 0.0 | +— / -486e92ad-4dcf-4c0e-a470-e0b87777d380 |
| Jogador 5 | 2-7 | 112 | BUY | STABILIZE | 94.0 | 6 | 11 | 1 | 20.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179349422454834 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -02c39b42-90d5-4e01-9380-460b6c1cb993,eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 2-7 | 113 | BUY | STABILIZE | 94.0 | 6 | 10 | 1 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025081027299165726 | 0.0 | 0.0 | +6eee9a92-4235-46af-ae42-c38acd6847ef / -— |
| Jogador 5 | 2-7 | 114 | BUY | STABILIZE | 94.0 | 6 | 8 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018524540588259697 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 115 | BUY | STABILIZE | 94.0 | 6 | 6 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6000106930732727 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 116 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 4 | 0 | 18.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1665094941854477 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 117 | BUY_XP | STABILIZE | 94.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 118 | SELL | STABILIZE | 94.0 | 6 | 0 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 2-7 | 119 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5688530802726746 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 120 | BUY | STABILIZE | 94.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1389489471912384 | 0.0 | 0.0 | +c5593e47-f48a-4362-b230-dfa3d7d36ec9 / -— |
| Jogador 5 | 3-1 | 122 | BUY | STABILIZE | 94.0 | 6 | 7 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28185996413230896 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 5 | 3-1 | 123 | BUY | STABILIZE | 94.0 | 6 | 5 | 0 | 22.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6824053525924683 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -46838f8d-8037-485c-8c34-9639f14ada19,837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-1 | 124 | BUY | STABILIZE | 94.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.20742452144622803 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 125 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12315776944160461 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011002927087247372 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 127 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014393298886716366 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 128 | SELL | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11633333563804626 | 0.0 | 0.0 | +— / -ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-1 | 129 | BUY_XP | STABILIZE | 94.0 | 6 | 5 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 130 | BUY | STABILIZE | 94.0 | 6 | 1 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.253347247838974 | 0.0 | 0.0 | +f7526b6b-8c94-4229-bd3f-1e538c769fec / -— |
| Jogador 5 | 3-2 | 132 | BUY | STABILIZE | 84.0 | 6 | 6 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.722278892993927 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 133 | BUY | STABILIZE | 84.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7045624852180481 | 0.0 | 0.0 | +1662b43d-12f4-45d6-b1bf-3733d5214808 / -— |
| Jogador 5 | 3-2 | 134 | BUY | STABILIZE | 84.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13984745740890503 | 0.0 | 0.0 | +d218597b-b641-4a4c-867a-41227b83fcff / -— |
| Jogador 5 | 3-2 | 135 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -f7526b6b-8c94-4229-bd3f-1e538c769fec |
| Jogador 5 | 3-2 | 136 | SELL | STABILIZE | 84.0 | 6 | 1 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -d218597b-b641-4a4c-867a-41227b83fcff |
| Jogador 5 | 3-2 | 137 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5348383784294128 | 0.0 | 0.0 | +— / -c5593e47-f48a-4362-b230-dfa3d7d36ec9 |
| Jogador 5 | 3-2 | 138 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 139 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11793138831853867 | 0.0 | 0.0 | +— / -1662b43d-12f4-45d6-b1bf-3733d5214808 |
| Jogador 5 | 3-2 | 140 | SELL | STABILIZE | 84.0 | 6 | 1 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5398730635643005 | 0.0 | 0.0 | +— / -e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 3-3 | 142 | BUY | STABILIZE | 84.0 | 6 | 10 | 1 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2038484364748001 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 143 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2852558493614197 | 0.0 | 0.0 | +a29f1c5b-c2f0-48be-b39c-0aa0d57fb94a / -— |
| Jogador 5 | 3-3 | 144 | BUY | STABILIZE | 84.0 | 6 | 5 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16185922920703888 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-3 | 145 | SELL | STABILIZE | 84.0 | 6 | 2 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09709914028644562 | 0.0 | 0.0 | +— / -a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 5 | 3-3 | 146 | BUY_XP | STABILIZE | 84.0 | 6 | 5 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 147 | SELL | STABILIZE | 84.0 | 6 | 1 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12244912981987 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-3 | 148 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0609700009226799 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 149 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 0 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5296773910522461 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 150 | MOVE_BOARD | FAST8 | 84.0 | 7 | 0 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014907710254192352 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 152 | BUY | FAST8 | 84.0 | 7 | 7 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007005379535257816 | 0.0 | 0.0 | +46fc5f36-cf3e-422e-89f3-9501ec9d7d12 / -— |
| Jogador 5 | 3-4 | 153 | BUY | FAST8 | 84.0 | 7 | 5 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06690805405378342 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 154 | BUY | FAST8 | 84.0 | 7 | 2 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09683044999837875 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -— |
| Jogador 5 | 3-4 | 155 | MOVE_BOARD | FAST8 | 84.0 | 7 | 0 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0071263620629906654 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 156 | MOVE_BOARD | FAST8 | 84.0 | 7 | 0 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007987325079739094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 157 | PASS | FAST8 | 84.0 | 7 | 0 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 162 | BUY | FAST8 | 84.0 | 7 | 6 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21785573661327362 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -— |
| Jogador 5 | 3-5 | 163 | BUY | FAST8 | 84.0 | 7 | 5 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4832949936389923 | 0.0 | 0.0 | +6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 / -— |
| Jogador 5 | 3-5 | 164 | BUY | FAST8 | 84.0 | 7 | 3 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09563397616147995 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-5 | 165 | MOVE_BOARD | FAST8 | 84.0 | 7 | 0 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006579700391739607 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 166 | MOVE_BOARD | FAST8 | 84.0 | 7 | 0 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09205684810876846 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 167 | PASS | FAST8 | 84.0 | 7 | 0 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 172 | BUY | FAST8 | 84.0 | 7 | 7 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5873178243637085 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-6 | 173 | SELL | FAST8 | 84.0 | 7 | 4 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 3-6 | 174 | BUY | FAST8 | 84.0 | 7 | 6 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0026035483460873365 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-6 | 175 | SELL | FAST8 | 84.0 | 7 | 3 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 3-6 | 176 | BUY_XP | FAST8 | 84.0 | 7 | 6 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 177 | SELL | FAST8 | 84.0 | 7 | 2 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0736985132098198 | 0.0 | 0.0 | +— / -750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 5 | 3-6 | 178 | BUY_XP | FAST8 | 84.0 | 7 | 5 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 179 | SELL | FAST8 | 84.0 | 7 | 1 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4883333444595337 | 0.0 | 0.0 | +— / -46fc5f36-cf3e-422e-89f3-9501ec9d7d12 |
| Jogador 5 | 3-6 | 180 | SELL | FAST8 | 84.0 | 7 | 3 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04899999871850014 | 0.0 | 0.0 | +— / -6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 |
| Jogador 5 | 3-7 | 182 | BUY | FAST8 | 84.0 | 7 | 12 | 1 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25269901752471924 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 183 | BUY | FAST8 | 84.0 | 7 | 9 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16852177679538727 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 5 | 3-7 | 184 | SELL | FAST8 | 84.0 | 7 | 6 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3449999988079071 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 5 | 3-7 | 185 | SELL | FAST8 | 84.0 | 7 | 9 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.402082622051239 | 0.0 | 0.0 | +— / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 5 | 3-7 | 186 | BUY | FAST8 | 84.0 | 7 | 12 | 1 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15807922184467316 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 187 | BUY_XP | FAST8 | 84.0 | 7 | 9 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 188 | BUY_XP | FAST8 | 84.0 | 7 | 5 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 189 | MOVE_BOARD | FAST8 | 84.0 | 7 | 1 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08368836343288422 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 190 | MOVE_BOARD | FAST8 | 84.0 | 7 | 1 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014416522346436977 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 192 | BUY | FAST8 | 84.0 | 7 | 7 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.44337937235832214 | 0.0 | 0.0 | +6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 / -— |
| Jogador 5 | 4-1 | 193 | BUY | FAST8 | 84.0 | 7 | 5 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.20673102140426636 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 194 | CRAFT_AND_EQUIP | FAST8 | 84.0 | 7 | 2 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1231241375207901 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 195 | CRAFT_AND_EQUIP | FAST8 | 84.0 | 7 | 2 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15047703683376312 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 196 | SELL | FAST8 | 84.0 | 7 | 2 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06593254953622818 | 0.0 | 0.0 | +— / -8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 |
| Jogador 5 | 4-1 | 197 | BUY | FAST8 | 84.0 | 7 | 5 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07991418987512589 | 0.0 | 0.0 | +0c07379e-5dd1-42e9-aa7a-a764f949deee / -— |
| Jogador 5 | 4-1 | 198 | MOVE_BENCH | FAST8 | 84.0 | 7 | 2 | 0 | 26.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008398939855396748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 199 | SELL | FAST8 | 84.0 | 7 | 2 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.51223224401474 | 0.0 | 0.0 | +— / -6eee9a92-4235-46af-ae42-c38acd6847ef |
| Jogador 5 | 4-1 | 200 | BUY_XP | FAST8 | 84.0 | 7 | 4 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 202 | BUY | FAST8 | 72.0 | 7 | 5 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7371872067451477 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 5 | 4-2 | 203 | SELL | FAST8 | 72.0 | 7 | 4 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09505132585763931 | 0.0 | 0.0 | +— / -6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 |
| Jogador 5 | 4-2 | 204 | SELL | FAST8 | 72.0 | 7 | 6 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6309999823570251 | 0.0 | 0.0 | +— / -a29f1c5b-c2f0-48be-b39c-0aa0d57fb94a |
| Jogador 5 | 4-2 | 205 | BUY | FAST8 | 72.0 | 7 | 8 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06741955876350403 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 5 | 4-2 | 206 | BUY_XP | FAST8 | 72.0 | 7 | 4 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 207 | MOVE_BENCH | FAST8 | 72.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09989441931247711 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 208 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041534993797540665 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 209 | SELL | STABILIZE | 72.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07470404356718063 | 0.0 | 0.0 | +— / -df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 4-2 | 210 | BUY | STABILIZE | 72.0 | 7 | 3 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020418601110577583 | 0.0 | 0.0 | +dde5ed69-0fc4-4d15-b12c-a5252a239040 / -— |
| Jogador 5 | 4-3 | 212 | BUY | STABILIZE | 72.0 | 7 | 6 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8036748766899109 | 0.0 | 0.0 | +c7841e00-91da-410b-b00f-62f4bf32f666 / -— |
| Jogador 5 | 4-3 | 213 | BUY | STABILIZE | 72.0 | 7 | 3 | 0 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8378543257713318 | 0.0 | 0.0 | +485dab1f-b3a1-4170-8ed6-c0035072ae9b / -9593a62e-442f-410a-8a0c-7d781e2487cc,ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 4-3 | 214 | BUY | STABILIZE | 72.0 | 7 | 2 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003989240620285273 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 5 | 4-3 | 215 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 0 | 0 | 22.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40273433923721313 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 216 | MOVE_BOARD | FAST8 | 72.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000852756202221 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 217 | MOVE_BOARD | FAST8 | 72.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 218 | PASS | FAST8 | 72.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 222 | BUY | FAST8 | 72.0 | 7 | 7 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7331596612930298 | 0.0 | 0.0 | +17170204-1921-4cf1-b92b-cc73bb0701ea / -— |
| Jogador 5 | 4-4 | 223 | SELL | FAST8 | 72.0 | 7 | 5 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -485dab1f-b3a1-4170-8ed6-c0035072ae9b |
| Jogador 5 | 4-4 | 224 | BUY | FAST8 | 72.0 | 7 | 8 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6775563359260559 | 0.0 | 0.0 | +84a3b0f5-c448-4fe1-b001-5ceff2ed306a / -— |
| Jogador 5 | 4-4 | 225 | MOVE_BOARD | FAST8 | 72.0 | 7 | 5 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 226 | MOVE_BOARD | FAST8 | 72.0 | 7 | 5 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039793577045202255 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 227 | PASS | FAST8 | 72.0 | 7 | 5 | 0 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 232 | SELL | FAST8 | 72.0 | 7 | 11 | 1 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -80c51b33-0a85-4f21-a797-9551aa10760f |
| Jogador 5 | 4-5 | 233 | BUY | FAST8 | 72.0 | 7 | 13 | 1 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7292358875274658 | 0.0 | 0.0 | +d6a00f0c-4823-44d6-b326-67595876998d / -— |
| Jogador 5 | 4-5 | 234 | MOVE_BOARD | FAST8 | 72.0 | 7 | 12 | 1 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02468976005911827 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 235 | SELL | FAST8 | 72.0 | 7 | 12 | 1 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -d9fdb961-a3e3-4e39-9970-e46ffd59fc3b |
| Jogador 5 | 4-5 | 236 | BUY | FAST8 | 72.0 | 7 | 16 | 1 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05386602506041527 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -— |
| Jogador 5 | 4-5 | 237 | MOVE_BOARD | FAST8 | 72.0 | 7 | 15 | 1 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.504889072151855e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 238 | MOVE_BOARD | FAST8 | 72.0 | 7 | 15 | 1 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 239 | MOVE_BOARD | FAST8 | 72.0 | 7 | 15 | 1 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 240 | PASS | FAST8 | 72.0 | 7 | 15 | 1 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 242 | SELL | FAST8 | 61.0 | 7 | 21 | 2 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023499999195337296 | 0.0 | 0.0 | +— / -bc0aa086-b5e5-4809-833f-193c5c0da181 |
| Jogador 5 | 4-6 | 243 | BUY | FAST8 | 61.0 | 7 | 22 | 2 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7129677534103394 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -1457cd1e-c240-4ce5-9217-a91bddfc8807,4af85188-f11e-4aca-8165-ba8e7f535670 |
| Jogador 5 | 4-6 | 244 | BUY | FAST8 | 61.0 | 7 | 19 | 1 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10099896788597107 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 5 | 4-6 | 245 | BUY | FAST8 | 61.0 | 7 | 15 | 1 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06429893523454666 | 0.0 | 0.0 | +20821a31-3317-4f82-bbb2-b70cdebdd893 / -— |
| Jogador 5 | 4-6 | 246 | MOVE_BOARD | FAST8 | 61.0 | 7 | 14 | 1 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 247 | MOVE_BOARD | FAST8 | 61.0 | 7 | 14 | 1 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015471572056412697 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 248 | PASS | FAST8 | 61.0 | 7 | 14 | 1 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 252 | SELL | FAST8 | 48.0 | 7 | 21 | 2 | 28.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5740000009536743 | 0.0 | 0.0 | +— / -023f01af-91d0-4e07-8229-2b7cded83151 |
| Jogador 5 | 4-7 | 253 | BUY | FAST8 | 48.0 | 7 | 29 | 2 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2343820035457611 | 0.0 | 0.0 | +3c59d736-011d-480c-a9af-1df7a3b4caab / -— |
| Jogador 5 | 4-7 | 254 | SELL | FAST8 | 48.0 | 7 | 28 | 2 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02645210362970829 | 0.0 | 0.0 | +— / -20821a31-3317-4f82-bbb2-b70cdebdd893 |
| Jogador 5 | 4-7 | 255 | BUY | FAST8 | 48.0 | 7 | 29 | 2 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21011626720428467 | 0.0 | 0.0 | +aaebedb3-18bf-4ae6-948e-7b326b573f1c / -— |
| Jogador 5 | 4-7 | 256 | MOVE_BOARD | FAST8 | 48.0 | 7 | 25 | 2 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0034116795286536217 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 257 | MOVE_BOARD | FAST8 | 48.0 | 7 | 25 | 2 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011306642554700375 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 258 | PASS | FAST8 | 48.0 | 7 | 25 | 2 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03214285895228386 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 48.0 | 7 | 33 | 3 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09895822405815125 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 48.0 | 7 | 33 | 3 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1250707060098648 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 264 | SELL | FAST8 | 48.0 | 7 | 33 | 3 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0141333332285285 | 0.0 | 0.0 | +— / -aaebedb3-18bf-4ae6-948e-7b326b573f1c |
| Jogador 5 | 5-1 | 265 | BUY | FAST8 | 48.0 | 7 | 37 | 3 | 28.0 | Espinhos Negros/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7612552642822266 | 0.0 | 0.0 | +c69a2be1-356a-4576-9887-6d1790221a5e / -— |
| Jogador 5 | 5-1 | 266 | SELL | FAST8 | 48.0 | 7 | 34 | 3 | 28.0 | Espinhos Negros/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04529696702957153 | 0.0 | 0.0 | +— / -ec9662c5-0734-41a3-9999-224d7716228b |
| Jogador 5 | 5-1 | 267 | BUY | FAST8 | 48.0 | 7 | 38 | 3 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1445896029472351 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 5 | 5-1 | 268 | SELL | FAST8 | 48.0 | 7 | 35 | 3 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04786914587020874 | 0.0 | 0.0 | +— / -d78561b4-3dcc-42fb-9983-2ed5d62f8606 |
| Jogador 5 | 5-1 | 269 | BUY | FAST8 | 48.0 | 7 | 38 | 3 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010209611617028713 | 0.0 | 0.0 | +0d120db3-34e2-47e3-a57c-0d65dcc56342 / -— |
| Jogador 5 | 5-1 | 270 | MOVE_BOARD | FAST8 | 48.0 | 7 | 34 | 3 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.704505267407512e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 272 | SELL | STABILIZE | 33.0 | 7 | 43 | 4 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -0d120db3-34e2-47e3-a57c-0d65dcc56342 |
| Jogador 5 | 5-2 | 273 | BUY | STABILIZE | 33.0 | 7 | 47 | 4 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8859594464302063 | 0.0 | 0.0 | +9a96b07c-5b37-4be7-855e-dc2d942e7171 / -— |
| Jogador 5 | 5-2 | 274 | SELL | STABILIZE | 33.0 | 7 | 44 | 4 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5098214745521545 | 0.0 | 0.0 | +— / -84a3b0f5-c448-4fe1-b001-5ceff2ed306a |
| Jogador 5 | 5-2 | 275 | BUY | STABILIZE | 33.0 | 7 | 47 | 4 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9704863429069519 | 0.0 | 0.0 | +5e843c10-0a8b-4781-983a-8e6e6f28253e / -17170204-1921-4cf1-b92b-cc73bb0701ea,a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 |
| Jogador 5 | 5-2 | 276 | BUY | STABILIZE | 33.0 | 7 | 45 | 4 | 24.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9622918963432312 | 0.0 | 0.0 | +e9bb05f6-3838-423a-bfd2-3791379b479e / -0f1b15a2-9978-4691-a15e-483ccd03db7f,c69a2be1-356a-4576-9887-6d1790221a5e |
| Jogador 5 | 5-2 | 277 | MOVE_BENCH | STABILIZE | 33.0 | 7 | 42 | 4 | 18.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3091045916080475 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 278 | BUY | STABILIZE | 33.0 | 7 | 42 | 4 | 30.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9685156941413879 | 0.0 | 0.0 | +1c5a9322-14c8-4df9-937b-842dcaa1f372 / -5627d898-cff3-4664-87d1-40a8f3656ab3,d6a00f0c-4823-44d6-b326-67595876998d |
| Jogador 5 | 5-2 | 279 | MOVE_BENCH | STABILIZE | 33.0 | 7 | 41 | 4 | 28.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3315883278846741 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 280 | BUY | STABILIZE | 33.0 | 7 | 41 | 4 | 34.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12745235860347748 | 0.0 | 0.0 | +aee0c45d-0178-4238-987f-5ee83dae7bce / -— |
| Jogador 5 | 5-3 | 282 | BUY | STABILIZE | 33.0 | 7 | 50 | 5 | 34.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3160029351711273 | 0.0 | 0.0 | +987e61e4-0d34-49cf-b1ef-a95a7a5dfb21 / -— |
| Jogador 5 | 5-3 | 283 | BUY | STABILIZE | 33.0 | 7 | 48 | 4 | 34.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5263274312019348 | 0.0 | 0.0 | +a5e92183-8d5d-434c-9294-47c6b7bfb91b / -— |
| Jogador 5 | 5-3 | 284 | SELL | STABILIZE | 33.0 | 7 | 45 | 4 | 34.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -5e843c10-0a8b-4781-983a-8e6e6f28253e |
| Jogador 5 | 5-3 | 285 | BUY | STABILIZE | 33.0 | 7 | 50 | 5 | 34.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02093770168721676 | 0.0 | 0.0 | +d8392323-28e4-4e98-a466-5958bf400729 / -— |
| Jogador 5 | 5-3 | 286 | MOVE_BOARD | STABILIZE | 33.0 | 7 | 47 | 4 | 34.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00021248741541057825 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 287 | MOVE_BOARD | STABILIZE | 33.0 | 7 | 47 | 4 | 34.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014786718413233757 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 288 | PASS | STABILIZE | 33.0 | 7 | 47 | 4 | 34.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07610952109098434 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 292 | BUY | ALL_IN | 17.0 | 7 | 57 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9593181014060974 | 0.0 | 0.0 | +dcb61be2-9a58-49bc-9f11-2f5fce42e7ea / -— |
| Jogador 5 | 5-4 | 293 | SELL | ALL_IN | 17.0 | 7 | 56 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6963000297546387 | 0.0 | 0.0 | +— / -1c5a9322-14c8-4df9-937b-842dcaa1f372 |
| Jogador 5 | 5-4 | 294 | BUY | ALL_IN | 17.0 | 7 | 59 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.6443613171577454 | 0.0 | 0.0 | +f2dbe099-e518-4261-b120-9f327b112dcb / -— |
| Jogador 5 | 5-4 | 295 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 7 | 56 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06174773722887039 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 296 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 7 | 56 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.041378188878297806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 297 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 56 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 298 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 56 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055709388107061386 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 299 | PASS | ALL_IN | 17.0 | 7 | 56 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4693956673145294 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 302 | SELL | ALL_IN | 17.0 | 8 | 67 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04153333231806755 | 0.0 | 0.0 | +— / -aee0c45d-0178-4238-987f-5ee83dae7bce |
| Jogador 5 | 5-5 | 303 | BUY | ALL_IN | 17.0 | 8 | 68 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19680163264274597 | 0.0 | 0.0 | +9c07608c-00e1-40f1-9671-6d8bc584a6c9 / -— |
| Jogador 5 | 5-5 | 304 | SELL | ALL_IN | 17.0 | 8 | 64 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042399998754262924 | 0.0 | 0.0 | +— / -9c07608c-00e1-40f1-9671-6d8bc584a6c9 |
| Jogador 5 | 5-5 | 305 | BUY | ALL_IN | 17.0 | 8 | 68 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09346990287303925 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 5 | 5-5 | 306 | SELL | ALL_IN | 17.0 | 8 | 64 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -0c5adb43-b194-486e-b59c-c0f3b5479d40 |
| Jogador 5 | 5-5 | 307 | BUY | ALL_IN | 17.0 | 8 | 68 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002701606834307313 | 0.0 | 0.0 | +e5f61076-ec13-419b-a4e8-d91b9975cfd6 / -— |
| Jogador 5 | 5-5 | 308 | SELL | ALL_IN | 17.0 | 8 | 63 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0025333333760499954 | 0.0 | 0.0 | +— / -e5f61076-ec13-419b-a4e8-d91b9975cfd6 |
| Jogador 5 | 5-5 | 309 | BUY | ALL_IN | 17.0 | 8 | 68 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19467826187610626 | 0.0 | 0.0 | +e978e901-0a52-4f01-ba52-a83fbcc3b439 / -— |
| Jogador 5 | 5-5 | 310 | REROLL | ALL_IN | 17.0 | 8 | 65 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 312 | SELL | ALL_IN | 1.0 | 8 | 75 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -e978e901-0a52-4f01-ba52-a83fbcc3b439 |
| Jogador 5 | 5-6 | 313 | BUY | ALL_IN | 1.0 | 8 | 78 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4463772475719452 | 0.0 | 0.0 | +b311d350-7bab-48ee-9833-0883606b4a2f / -— |
| Jogador 5 | 5-6 | 314 | SELL | ALL_IN | 1.0 | 8 | 76 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6217666864395142 | 0.0 | 0.0 | +— / -f2dbe099-e518-4261-b120-9f327b112dcb |
| Jogador 5 | 5-6 | 315 | BUY | ALL_IN | 1.0 | 8 | 79 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42779865860939026 | 0.0 | 0.0 | +6eff87be-d18f-4f46-a9c6-9ae977c887e0 / -— |
| Jogador 5 | 5-6 | 316 | SELL | ALL_IN | 1.0 | 8 | 76 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -d8392323-28e4-4e98-a466-5958bf400729 |
| Jogador 5 | 5-6 | 317 | BUY | ALL_IN | 1.0 | 8 | 79 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0905519351363182 | 0.0 | 0.0 | +68a0405b-6231-471f-98a5-1661d32f4ac4 / -— |
| Jogador 5 | 5-6 | 318 | SELL | ALL_IN | 1.0 | 8 | 75 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -68a0405b-6231-471f-98a5-1661d32f4ac4 |
| Jogador 5 | 5-6 | 319 | BUY | ALL_IN | 1.0 | 8 | 79 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0678824856877327 | 0.0 | 0.0 | +9c3b3b78-e99c-4947-b958-cce156ecccb1 / -— |
| Jogador 5 | 5-6 | 320 | SELL | ALL_IN | 1.0 | 8 | 77 | 5 | 40.0 | Espinhos Negros/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -9c3b3b78-e99c-4947-b958-cce156ecccb1 |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | -0.15334774553775787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Sentry | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17399217188358307 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2196885347366333 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0373011827468872 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039901405572891235 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012773334980010986 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011599136516451836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 30 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5747041702270508 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 41 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0239715576171875 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 42 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 52 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12833119928836823 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15204384922981262 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2898862063884735 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 55 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 56 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26425060629844666 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 63 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2476654052734375 | 0.0 | 0.0 | +048e9074-b134-49ed-a105-88dca63d1aa3 / -— |
| Jogador 6 | 2-2 | 64 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -6a01f661-884f-4c25-9dbe-384a6fe3a5e6 |
| Jogador 6 | 2-2 | 65 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07944674044847488 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 66 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 72 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28942158818244934 | 0.0 | 0.0 | +b1ecd1fa-793c-40ad-a9e3-9d35d5030339 / -— |
| Jogador 6 | 2-3 | 73 | BUY | STABILIZE | 89.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17973856627941132 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 74 | BUY | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2379845678806305 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 75 | SELL | STABILIZE | 89.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1451774537563324 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-3 | 76 | SELL | STABILIZE | 89.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15191948413848877 | 0.0 | 0.0 | +— / -b1ecd1fa-793c-40ad-a9e3-9d35d5030339 |
| Jogador 6 | 2-3 | 77 | PASS | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 82 | BUY | LOSS_STREAK | 83.0 | 5 | 9 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1128760352730751 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 83 | BUY | LOSS_STREAK | 83.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17069022357463837 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 84 | BUY | LOSS_STREAK | 83.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7370080947875977 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 85 | BUY_XP | LOSS_STREAK | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 86 | SELL | LOSS_STREAK | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013266666792333126 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-4 | 87 | SELL | LOSS_STREAK | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10965542495250702 | 0.0 | 0.0 | +— / -048e9074-b134-49ed-a105-88dca63d1aa3 |
| Jogador 6 | 2-4 | 88 | BUY_XP | LOSS_STREAK | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 89 | SELL | LOSS_STREAK | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1437745839357376 | 0.0 | 0.0 | +— / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 |
| Jogador 6 | 2-4 | 90 | PASS | LOSS_STREAK | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 92 | BUY | LOSS_STREAK | 83.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8707958459854126 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 93 | BUY | LOSS_STREAK | 83.0 | 5 | 7 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21572400629520416 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 94 | SELL | STABILIZE | 83.0 | 5 | 5 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12204575538635254 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-5 | 95 | SELL | STABILIZE | 83.0 | 5 | 7 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45176538825035095 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-5 | 96 | SELL | STABILIZE | 83.0 | 5 | 9 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41324830055236816 | 0.0 | 0.0 | +— / -a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 2-5 | 97 | SELL | STABILIZE | 83.0 | 5 | 12 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0224478244781494 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-5 | 98 | BUY | STABILIZE | 83.0 | 5 | 13 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3572264015674591 | 0.0 | 0.0 | +f957e607-dd51-492b-9186-252da4e0c12f / -— |
| Jogador 6 | 2-5 | 99 | BUY_XP | STABILIZE | 83.0 | 5 | 12 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 100 | BUY_XP | STABILIZE | 83.0 | 5 | 8 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 102 | BUY | STABILIZE | 78.0 | 6 | 10 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2112056314945221 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 103 | BUY_XP | STABILIZE | 78.0 | 6 | 7 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 104 | SELL | STABILIZE | 78.0 | 6 | 3 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4944157302379608 | 0.0 | 0.0 | +— / -f957e607-dd51-492b-9186-252da4e0c12f |
| Jogador 6 | 2-6 | 105 | BUY_XP | STABILIZE | 78.0 | 6 | 4 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 106 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 0 | 0 | 14.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29526472091674805 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 107 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 0 | 0 | 14.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1395607739686966 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 108 | PASS | STABILIZE | 78.0 | 6 | 0 | 0 | 16.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 112 | BUY | STABILIZE | 73.0 | 6 | 7 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0317537784576416 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 113 | SELL | STABILIZE | 73.0 | 6 | 4 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -18934be2-4988-4f62-9f62-07ba151231f2 |
| Jogador 6 | 2-7 | 114 | SELL | STABILIZE | 73.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 2-7 | 115 | BUY | STABILIZE | 73.0 | 6 | 6 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35904356837272644 | 0.0 | 0.0 | +dc83202b-476c-4438-90aa-a615b764b7e4 / -— |
| Jogador 6 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00029836283647455275 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 117 | SELL | STABILIZE | 73.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4946684241294861 | 0.0 | 0.0 | +— / -dc83202b-476c-4438-90aa-a615b764b7e4 |
| Jogador 6 | 2-7 | 118 | SELL | STABILIZE | 73.0 | 6 | 6 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0190000534057617 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 2-7 | 119 | BUY_XP | STABILIZE | 73.0 | 6 | 9 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 120 | BUY_XP | STABILIZE | 73.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 122 | BUY | STABILIZE | 73.0 | 6 | 8 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.10052359104156494 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 73.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22872674465179443 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 124 | BUY_XP | STABILIZE | 73.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 125 | SELL | STABILIZE | 73.0 | 6 | 1 | 0 | 16.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09566666930913925 | 0.0 | 0.0 | +— / -a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 |
| Jogador 6 | 3-1 | 126 | SELL | STABILIZE | 73.0 | 6 | 4 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 3-1 | 127 | BUY | STABILIZE | 73.0 | 6 | 7 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.009057527408003807 | 0.0 | 0.0 | +ab127012-83d7-46f0-a16c-b20582d1179b / -— |
| Jogador 6 | 3-1 | 128 | BUY | STABILIZE | 73.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10848916321992874 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-1 | 129 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 1 | 0 | 16.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19894807040691376 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 130 | SELL | STABILIZE | 73.0 | 6 | 1 | 0 | 22.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.060508403927087784 | 0.0 | 0.0 | +— / -ab127012-83d7-46f0-a16c-b20582d1179b |
| Jogador 6 | 3-2 | 132 | BUY | STABILIZE | 73.0 | 6 | 9 | 0 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8369395136833191 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 133 | BUY | STABILIZE | 73.0 | 6 | 8 | 0 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.287619411945343 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -— |
| Jogador 6 | 3-2 | 134 | SELL | STABILIZE | 73.0 | 6 | 7 | 0 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5490000247955322 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 3-2 | 135 | EQUIP_FROM_INVENTORY | STABILIZE | 73.0 | 6 | 10 | 1 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1321266144514084 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 136 | EQUIP_FROM_INVENTORY | STABILIZE | 73.0 | 6 | 10 | 1 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.16428157687187195 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 137 | EQUIP_FROM_INVENTORY | STABILIZE | 73.0 | 6 | 10 | 1 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1427438110113144 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 138 | BUY_XP | STABILIZE | 73.0 | 6 | 10 | 1 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 139 | BUY_XP | STABILIZE | 73.0 | 6 | 6 | 0 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 140 | SELL | STABILIZE | 73.0 | 6 | 2 | 0 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -e29364db-c484-4e4d-954d-7f4940131ffc |
| Jogador 6 | 3-3 | 142 | BUY | STABILIZE | 64.0 | 7 | 8 | 0 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8036528825759888 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 143 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 5 | 0 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11213073879480362 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 144 | BUY | FAST8 | 64.0 | 7 | 5 | 0 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07173997163772583 | 0.0 | 0.0 | +31c30451-3999-47b1-8bcf-77e137137b2a / -— |
| Jogador 6 | 3-3 | 145 | MOVE_BOARD | FAST8 | 64.0 | 7 | 2 | 0 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08514481782913208 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 146 | MOVE_BENCH | FAST8 | 64.0 | 7 | 2 | 0 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4320165514945984 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 147 | BUY | FAST8 | 64.0 | 7 | 2 | 0 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.26346614956855774 | 0.0 | 0.0 | +952adeb2-fe24-47af-9748-5131b91dcc06 / -— |
| Jogador 6 | 3-3 | 148 | MOVE_BOARD | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11634370684623718 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 149 | MOVE_BOARD | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08958196640014648 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 150 | MOVE_BOARD | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08343619853258133 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 152 | BUY | FAST8 | 64.0 | 7 | 6 | 0 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19727511703968048 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -— |
| Jogador 6 | 3-4 | 153 | BUY | FAST8 | 64.0 | 7 | 2 | 0 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2635869085788727 | 0.0 | 0.0 | +4698e3b3-0833-4895-a1f1-26b372b2f965 / -— |
| Jogador 6 | 3-4 | 154 | MOVE_BOARD | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052580226212739944 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 155 | MOVE_BOARD | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013875344768166542 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 156 | MOVE_BOARD | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013987078331410885 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 157 | MOVE_BOARD | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 158 | PASS | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 162 | BUY | FAST8 | 64.0 | 7 | 5 | 0 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2103351503610611 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 163 | BUY | FAST8 | 64.0 | 7 | 2 | 0 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2612460255622864 | 0.0 | 0.0 | +506f7312-07d8-4165-bd67-f7a69cf9a19c / -— |
| Jogador 6 | 3-5 | 164 | MOVE_BOARD | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003692182945087552 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 165 | MOVE_BOARD | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013819301500916481 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 166 | PASS | FAST8 | 64.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 172 | BUY | FAST8 | 55.0 | 7 | 5 | 0 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006608057767152786 | 0.0 | 0.0 | +604cc5dc-6c20-4d5a-b3a7-8862adfe1930 / -— |
| Jogador 6 | 3-6 | 173 | BUY | FAST8 | 55.0 | 7 | 2 | 0 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12931516766548157 | 0.0 | 0.0 | +ab050f92-777b-429f-9ed8-9b6c63794641 / -— |
| Jogador 6 | 3-6 | 174 | SELL | FAST8 | 55.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -506f7312-07d8-4165-bd67-f7a69cf9a19c |
| Jogador 6 | 3-6 | 175 | BUY | FAST8 | 55.0 | 7 | 2 | 0 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09443262964487076 | 0.0 | 0.0 | +171724e7-58bd-404f-820b-2bb32c5c193e / -— |
| Jogador 6 | 3-6 | 176 | MOVE_BOARD | FAST8 | 55.0 | 7 | 1 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09666474908590317 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 177 | MOVE_BOARD | FAST8 | 55.0 | 7 | 1 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27195632457733154 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 178 | PASS | FAST8 | 55.0 | 7 | 1 | 0 | 32.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 182 | BUY | FAST8 | 55.0 | 7 | 7 | 0 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3951900005340576 | 0.0 | 0.0 | +604a85af-ff68-41a7-8795-73fdc7723c0e / -— |
| Jogador 6 | 3-7 | 183 | BUY | FAST8 | 55.0 | 7 | 5 | 0 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11320306360721588 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 184 | SELL | FAST8 | 55.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02176666632294655 | 0.0 | 0.0 | +— / -171724e7-58bd-404f-820b-2bb32c5c193e |
| Jogador 6 | 3-7 | 185 | BUY | FAST8 | 55.0 | 7 | 1 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14414362609386444 | 0.0 | 0.0 | +3a40e3a6-b3e3-4f35-8fa0-e81c89d72db6 / -— |
| Jogador 6 | 3-7 | 186 | SELL | FAST8 | 55.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005966666620224714 | 0.0 | 0.0 | +— / -3a40e3a6-b3e3-4f35-8fa0-e81c89d72db6 |
| Jogador 6 | 3-7 | 187 | SELL | FAST8 | 55.0 | 7 | 1 | 0 | 32.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -952adeb2-fe24-47af-9748-5131b91dcc06 |
| Jogador 6 | 3-7 | 188 | BUY | FAST8 | 55.0 | 7 | 3 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09120788425207138 | 0.0 | 0.0 | +89cec488-9a0e-4838-b486-2504a0742476 / -— |
| Jogador 6 | 3-7 | 189 | SELL | FAST8 | 55.0 | 7 | 1 | 0 | 32.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -4698e3b3-0833-4895-a1f1-26b372b2f965 |
| Jogador 6 | 3-7 | 190 | SELL | FAST8 | 55.0 | 7 | 3 | 0 | 32.0 | Feérico/DA_18_GnarSmall | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -89cec488-9a0e-4838-b486-2504a0742476 |
| Jogador 6 | 4-1 | 192 | BUY | FAST8 | 55.0 | 7 | 10 | 1 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0572548508644104 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -— |
| Jogador 6 | 4-1 | 193 | BUY | FAST8 | 55.0 | 7 | 7 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08375522494316101 | 0.0 | 0.0 | +a8a8381a-f3a8-45ec-9106-293d73fca0c8 / -— |
| Jogador 6 | 4-1 | 194 | CRAFT_AND_EQUIP | FAST8 | 55.0 | 7 | 4 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11595385521650314 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 195 | CRAFT_AND_EQUIP | FAST8 | 55.0 | 7 | 4 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1141359731554985 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 196 | BUY_XP | FAST8 | 55.0 | 7 | 4 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 197 | SELL | FAST8 | 55.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09300000220537186 | 0.0 | 0.0 | +— / -a8a8381a-f3a8-45ec-9106-293d73fca0c8 |
| Jogador 6 | 4-1 | 198 | BUY | FAST8 | 55.0 | 7 | 3 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021615704521536827 | 0.0 | 0.0 | +3d7ba32f-3349-479e-bb6f-9cd1f2006149 / -— |
| Jogador 6 | 4-1 | 199 | SELL | FAST8 | 55.0 | 7 | 2 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3932109475135803 | 0.0 | 0.0 | +— / -3d7ba32f-3349-479e-bb6f-9cd1f2006149 |
| Jogador 6 | 4-1 | 200 | BUY | FAST8 | 55.0 | 7 | 3 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0843799039721489 | 0.0 | 0.0 | +78525c90-c4d2-425d-ba90-a03664c60a28 / -— |
| Jogador 6 | 4-2 | 202 | BUY | FAST8 | 55.0 | 7 | 8 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5191389918327332 | 0.0 | 0.0 | +93f7279f-b03b-407b-b623-c0a2bd88f877 / -— |
| Jogador 6 | 4-2 | 203 | SELL | FAST8 | 55.0 | 7 | 5 | 0 | 32.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02360105887055397 | 0.0 | 0.0 | +— / -78525c90-c4d2-425d-ba90-a03664c60a28 |
| Jogador 6 | 4-2 | 204 | BUY | FAST8 | 55.0 | 7 | 7 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10367265343666077 | 0.0 | 0.0 | +6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb / -— |
| Jogador 6 | 4-2 | 205 | BUY_XP | FAST8 | 55.0 | 7 | 4 | 0 | 32.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 206 | SELL | FAST8 | 55.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb |
| Jogador 6 | 4-2 | 207 | BUY | FAST8 | 55.0 | 7 | 3 | 0 | 32.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08360104262828827 | 0.0 | 0.0 | +7fd8b302-97aa-4373-94f4-adfcad477ed2 / -— |
| Jogador 6 | 4-2 | 208 | MOVE_BENCH | FAST8 | 55.0 | 7 | 0 | 0 | 32.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17103436589241028 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 209 | MOVE_BOARD | FAST8 | 55.0 | 7 | 0 | 0 | 34.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19854144752025604 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 210 | PASS | FAST8 | 55.0 | 7 | 0 | 0 | 34.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 212 | SELL | FAST8 | 43.0 | 7 | 5 | 0 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007366666570305824 | 0.0 | 0.0 | +— / -7fd8b302-97aa-4373-94f4-adfcad477ed2 |
| Jogador 6 | 4-3 | 213 | BUY | FAST8 | 43.0 | 7 | 8 | 0 | 34.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044064052402973175 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 6 | 4-3 | 214 | BUY_XP | FAST8 | 43.0 | 7 | 4 | 0 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 215 | SELL | FAST8 | 43.0 | 7 | 0 | 0 | 34.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -604cc5dc-6c20-4d5a-b3a7-8862adfe1930 |
| Jogador 6 | 4-3 | 216 | BUY | FAST8 | 43.0 | 7 | 3 | 0 | 34.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05289958789944649 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 6 | 4-3 | 217 | MOVE_BOARD | FAST8 | 43.0 | 7 | 1 | 0 | 34.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 218 | MOVE_BOARD | FAST8 | 43.0 | 7 | 1 | 0 | 34.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 219 | PASS | FAST8 | 43.0 | 7 | 1 | 0 | 34.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 222 | SELL | FAST8 | 43.0 | 7 | 7 | 0 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010783271864056587 | 0.0 | 0.0 | +— / -e85c6ab6-f36c-40b4-88e2-b7380b4c9652 |
| Jogador 6 | 4-4 | 223 | BUY | FAST8 | 43.0 | 7 | 9 | 0 | 34.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21655239164829254 | 0.0 | 0.0 | +8995f621-b355-44ec-816e-797184bdc266 / -— |
| Jogador 6 | 4-4 | 224 | BUY_XP | FAST8 | 43.0 | 7 | 8 | 0 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 225 | BUY_XP | FAST8 | 43.0 | 7 | 4 | 0 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 226 | MOVE_BOARD | FAST8 | 43.0 | 7 | 0 | 0 | 34.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2136112004518509 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 227 | MOVE_BOARD | FAST8 | 43.0 | 7 | 0 | 0 | 34.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00018405420996714383 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 228 | MOVE_BOARD | FAST8 | 43.0 | 7 | 0 | 0 | 34.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013733243569731712 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 229 | PASS | FAST8 | 43.0 | 7 | 0 | 0 | 34.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 232 | SELL | FAST8 | 43.0 | 7 | 5 | 0 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -1fa69553-5270-4459-986b-600f748711b7 |
| Jogador 6 | 4-5 | 233 | BUY | FAST8 | 43.0 | 7 | 9 | 0 | 34.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018006619065999985 | 0.0 | 0.0 | +262702a6-b710-4129-9dc6-0c1a04514ff9 / -— |
| Jogador 6 | 4-5 | 234 | MOVE_BOARD | FAST8 | 43.0 | 7 | 8 | 0 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 235 | MOVE_BOARD | FAST8 | 43.0 | 7 | 8 | 0 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07094480097293854 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 236 | PASS | FAST8 | 43.0 | 7 | 8 | 0 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 242 | SELL | STABILIZE | 30.0 | 7 | 13 | 1 | 34.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03889999911189079 | 0.0 | 0.0 | +— / -891aea62-e06a-46d4-8250-a3d4a56e847d |
| Jogador 6 | 4-6 | 243 | BUY | STABILIZE | 30.0 | 7 | 18 | 1 | 34.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1628357470035553 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 6 | 4-6 | 244 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 14 | 1 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 245 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 14 | 1 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15207670629024506 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 246 | PASS | STABILIZE | 30.0 | 7 | 14 | 1 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 252 | SELL | STABILIZE | 30.0 | 7 | 21 | 2 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02345317229628563 | 0.0 | 0.0 | +— / -262702a6-b710-4129-9dc6-0c1a04514ff9 |
| Jogador 6 | 4-7 | 253 | BUY | STABILIZE | 30.0 | 7 | 22 | 2 | 34.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7837340831756592 | 0.0 | 0.0 | +2f2ff445-f60a-4a05-b37a-41b8a6d6c7f9 / -43da0d73-facd-488b-b856-94e9496a97f9,ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b |
| Jogador 6 | 4-7 | 254 | BUY | STABILIZE | 30.0 | 7 | 19 | 1 | 28.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5249563455581665 | 0.0 | 0.0 | +2f5d8cb8-8ba3-45e9-a345-00e931d34490 / -93f7279f-b03b-407b-b623-c0a2bd88f877,f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 6 | 4-7 | 255 | BUY | STABILIZE | 30.0 | 7 | 16 | 1 | 28.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022099707275629044 | 0.0 | 0.0 | +d6a929d8-6d7c-4bcd-880d-d819daca2ae0 / -— |
| Jogador 6 | 4-7 | 256 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 13 | 1 | 28.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24580544233322144 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 257 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 13 | 1 | 28.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 258 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 13 | 1 | 28.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03460773453116417 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 259 | PASS | STABILIZE | 30.0 | 7 | 13 | 1 | 28.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 262 | BUY | STABILIZE | 30.0 | 7 | 19 | 1 | 34.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7966933846473694 | 0.0 | 0.0 | +77489602-9456-4a97-aa7e-df7ef91d5e4a / -— |
| Jogador 6 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 30.0 | 7 | 16 | 1 | 34.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15057723224163055 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 30.0 | 7 | 16 | 1 | 34.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15775145590305328 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 265 | BUY | STABILIZE | 30.0 | 7 | 16 | 1 | 34.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10214734822511673 | 0.0 | 0.0 | +9af900db-c181-448a-9736-30f08f062a00 / -— |
| Jogador 6 | 5-1 | 266 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 12 | 1 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10545884817838669 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 267 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 12 | 1 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13293218612670898 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 268 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 12 | 1 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 269 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 12 | 1 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05148756131529808 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 270 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 12 | 1 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02110918052494526 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 272 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 20 | 2 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 273 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 20 | 2 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17895543575286865 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 274 | PASS | STABILIZE | 30.0 | 7 | 20 | 2 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041206348687410355 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 282 | SELL | STABILIZE | 30.0 | 7 | 29 | 2 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.044160086661577225 | 0.0 | 0.0 | +— / -2f5d8cb8-8ba3-45e9-a345-00e931d34490 |
| Jogador 6 | 5-3 | 283 | BUY | STABILIZE | 30.0 | 7 | 37 | 3 | 34.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8444325923919678 | 0.0 | 0.0 | +7a419783-907e-47e2-bf69-29a54ee18a02 / -— |
| Jogador 6 | 5-3 | 284 | SELL | STABILIZE | 30.0 | 7 | 34 | 3 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -2f2ff445-f60a-4a05-b37a-41b8a6d6c7f9 |
| Jogador 6 | 5-3 | 285 | BUY | STABILIZE | 30.0 | 7 | 42 | 4 | 34.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9729978442192078 | 0.0 | 0.0 | +f0264dc3-6749-4682-929e-fab42383532a / -3cb4d077-df9a-4fd2-9a68-7301aff1b657,3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 5-3 | 286 | SELL | STABILIZE | 30.0 | 7 | 41 | 4 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -f0264dc3-6749-4682-929e-fab42383532a |
| Jogador 6 | 5-3 | 287 | BUY | STABILIZE | 30.0 | 7 | 44 | 4 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9688828587532043 | 0.0 | 0.0 | +64d87de4-68df-4a72-8b8d-f78039ae4ce5 / -31c30451-3999-47b1-8bcf-77e137137b2a,77489602-9456-4a97-aa7e-df7ef91d5e4a |
| Jogador 6 | 5-3 | 288 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 41 | 4 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.20541030168533325 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 289 | BUY | STABILIZE | 30.0 | 7 | 41 | 4 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8885491490364075 | 0.0 | 0.0 | +b2517873-8317-401b-8461-1d86969edbd7 / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4,7a419783-907e-47e2-bf69-29a54ee18a02 |
| Jogador 6 | 5-3 | 290 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 38 | 3 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.1591586321592331 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 292 | BUY | ALL_IN | 14.0 | 7 | 46 | 4 | 32.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8941940069198608 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -— |
| Jogador 6 | 5-4 | 293 | BUY | ALL_IN | 14.0 | 7 | 42 | 4 | 32.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.1767125129699707 | 0.0 | 0.0 | +8da82a9e-0746-43e1-81c3-fa22ec3bb863 / -— |
| Jogador 6 | 5-4 | 294 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 38 | 3 | 32.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.24968074262142181 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 295 | BUY | ALL_IN | 14.0 | 7 | 38 | 3 | 40.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.021981554105877876 | 0.0 | 0.0 | +6fb5e8f1-2656-486b-9478-161c1b430d5f / -— |
| Jogador 6 | 5-4 | 296 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 7 | 35 | 3 | 40.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09313812851905823 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 297 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 7 | 35 | 3 | 40.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11458312720060349 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 298 | BUY | ALL_IN | 14.0 | 7 | 35 | 3 | 40.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2589879333972931 | 0.0 | 0.0 | +d30c92eb-1279-4532-b763-7c30826c8430 / -— |
| Jogador 6 | 5-4 | 299 | MOVE_BOARD | ALL_IN | 14.0 | 7 | 33 | 3 | 40.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 300 | MOVE_BOARD | ALL_IN | 14.0 | 7 | 33 | 3 | 40.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 302 | BUY | ALL_IN | 14.0 | 7 | 41 | 4 | 52.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12429575622081757 | 0.0 | 0.0 | +01c587bb-ca4f-4690-9e4b-d1e9c44fd33e / -— |
| Jogador 6 | 5-5 | 303 | SELL | ALL_IN | 14.0 | 7 | 38 | 3 | 52.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6047999858856201 | 0.0 | 0.0 | +— / -64d87de4-68df-4a72-8b8d-f78039ae4ce5 |
| Jogador 6 | 5-5 | 304 | BUY | ALL_IN | 14.0 | 7 | 46 | 4 | 52.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.16719330847263336 | 0.0 | 0.0 | +d3fddd9d-ee81-418d-9c58-0baa4ed99f61 / -— |
| Jogador 6 | 5-5 | 305 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 7 | 44 | 4 | 52.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08709803968667984 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 306 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 7 | 44 | 4 | 52.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08858870714902878 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 307 | MOVE_BOARD | ALL_IN | 14.0 | 7 | 44 | 4 | 52.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.836635525862221e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 308 | MOVE_BOARD | ALL_IN | 14.0 | 7 | 44 | 4 | 52.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014968072064220905 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 309 | PASS | ALL_IN | 14.0 | 7 | 44 | 4 | 52.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4309079349040985 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589178562164307 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2799173593521118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.143971249461174 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012334865517914295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40434256196022034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0484532117843628 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23116838932037354 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004352054558694363 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005867671221494675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 31 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 41 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.036877989768982 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24497109651565552 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007539904909208417 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1995791792869568 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 45 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8279920220375061 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19963383674621582 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24531260132789612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30116716027259827 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 56 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475654602050781 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15446844696998596 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 65 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17884759604930878 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04722195118665695 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 68 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-2 | 69 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11032819002866745 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 70 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1539985090494156 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 72 | BUY | STABILIZE | 94.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475438833236694 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 73 | BUY | STABILIZE | 94.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6454818248748779 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 6 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17262005805969238 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 75 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09766226261854172 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 76 | SELL | STABILIZE | 94.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6189197301864624 | 0.0 | 0.0 | +— / -3394d5fc-ee48-4a08-8669-05984c804b53 |
| Jogador 7 | 2-3 | 77 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14206402003765106 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 78 | BUY_XP | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 79 | PASS | STABILIZE | 94.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 80 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1743561327457428 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 82 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31487756967544556 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 83 | BUY | STABILIZE | 94.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2571878731250763 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 84 | PASS | STABILIZE | 94.0 | 5 | 1 | 0 | 16.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 92 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28898781538009644 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 93 | BUY | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31405267119407654 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
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
| Jogador 7 | 2-7 | 115 | MOVE_BOARD | FAST8 | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015011870302259922 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 116 | MOVE_BOARD | FAST8 | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01493695005774498 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 117 | PASS | FAST8 | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 122 | BUY | FAST8 | 94.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.21450947225093842 | 0.0 | 0.0 | +033a84d9-70f6-46a8-a6eb-a2f03be70400 / -— |
| Jogador 7 | 3-1 | 123 | CRAFT_AND_EQUIP | FAST8 | 94.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15356650948524475 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 124 | BUY_XP | FAST8 | 94.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 125 | MOVE_BOARD | FAST8 | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0004193209169898182 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 126 | MOVE_BOARD | FAST8 | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014673740603029728 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 127 | PASS | FAST8 | 94.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 132 | BUY | FAST8 | 84.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7269442677497864 | 0.0 | 0.0 | +46320c4e-6bc0-49d6-b150-be378fa422cf / -— |
| Jogador 7 | 3-2 | 133 | BUY | FAST8 | 84.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21166644990444183 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -— |
| Jogador 7 | 3-2 | 134 | PASS | FAST8 | 84.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 142 | BUY | FAST8 | 84.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20220279693603516 | 0.0 | 0.0 | +652ff984-c3ac-48d7-9fb6-e95aed0a047d / -— |
| Jogador 7 | 3-3 | 143 | BUY_XP | FAST8 | 84.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 144 | SELL | FAST8 | 84.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 3-3 | 145 | BUY | FAST8 | 84.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12788110971450806 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 146 | SELL | FAST8 | 84.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045499999076128006 | 0.0 | 0.0 | +— / -f116ca4e-dbe8-457e-83a5-958525aa384a |
| Jogador 7 | 3-3 | 147 | BUY_XP | FAST8 | 84.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 148 | SELL | FAST8 | 84.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4826222360134125 | 0.0 | 0.0 | +— / -652ff984-c3ac-48d7-9fb6-e95aed0a047d |
| Jogador 7 | 3-3 | 149 | BUY | FAST8 | 84.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20054718852043152 | 0.0 | 0.0 | +4d03897d-0113-4a29-a864-75305c142d97 / -— |
| Jogador 7 | 3-3 | 150 | MOVE_BOARD | FAST8 | 84.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00015958370931912214 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 152 | BUY | FAST8 | 74.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7679950594902039 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -4e206e09-40e3-4699-81cb-8aaf01109dea,a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 7 | 3-4 | 153 | BUY | FAST8 | 74.0 | 6 | 4 | 0 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7611241936683655 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -2c7e844d-925a-43bb-8be8-65a71d11f964,6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 74.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09934893995523453 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 155 | MOVE_BENCH | STABILIZE | 74.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13976743817329407 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 156 | SELL | FAST8 | 74.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -1ff50c59-5133-459e-8bf1-d449c26efabf |
| Jogador 7 | 3-4 | 157 | EQUIP_FROM_INVENTORY | FAST8 | 74.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08521726727485657 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 158 | EQUIP_FROM_INVENTORY | FAST8 | 74.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06649921834468842 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 159 | BUY_XP | FAST8 | 74.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 160 | MOVE_BOARD | FAST8 | 74.0 | 6 | 0 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0012134799035266042 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 162 | BUY | FAST8 | 74.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18406768143177032 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 7 | 3-5 | 163 | BUY | FAST8 | 74.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026206282898783684 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 164 | MOVE_BOARD | FAST8 | 74.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.2953298614302184e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 165 | SELL | FAST8 | 74.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6190000176429749 | 0.0 | 0.0 | +— / -cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 3-5 | 166 | EQUIP_FROM_INVENTORY | FAST8 | 74.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1384444683790207 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 167 | BUY | FAST8 | 74.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1529586911201477 | 0.0 | 0.0 | +f546078f-fc3e-44a9-9b8f-25c46a043168 / -— |
| Jogador 7 | 3-5 | 168 | BUY | FAST8 | 74.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036592841148376465 | 0.0 | 0.0 | +2074e6ec-81e7-41c9-be7e-a0d9310fbafa / -— |
| Jogador 7 | 3-5 | 169 | MOVE_BOARD | FAST8 | 74.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019604790955781937 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 170 | MOVE_BOARD | FAST8 | 74.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004602947738021612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 172 | SELL | FAST8 | 63.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -2074e6ec-81e7-41c9-be7e-a0d9310fbafa |
| Jogador 7 | 3-6 | 173 | BUY | FAST8 | 63.0 | 6 | 13 | 1 | 26.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5861504673957825 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 174 | SELL | FAST8 | 63.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02403770200908184 | 0.0 | 0.0 | +— / -4d03897d-0113-4a29-a864-75305c142d97 |
| Jogador 7 | 3-6 | 175 | BUY | FAST8 | 63.0 | 6 | 12 | 1 | 26.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028375770896673203 | 0.0 | 0.0 | +6caec849-54f8-4ec1-90a4-fc0587510013 / -— |
| Jogador 7 | 3-6 | 176 | BUY_XP | FAST8 | 63.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 177 | BUY_XP | FAST8 | 63.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04650000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 178 | MOVE_BENCH | FAST8 | 63.0 | 7 | 1 | 0 | 26.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16575798392295837 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 179 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 28.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014993302524089813 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 180 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 28.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999010600149632 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 182 | BUY | FAST8 | 63.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7316693067550659 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 183 | BUY | FAST8 | 63.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7347633838653564 | 0.0 | 0.0 | +21135c93-ae87-47a0-899c-7eaa0c2c30b8 / -— |
| Jogador 7 | 3-7 | 184 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.9570746088866144e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 185 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015357553958892822 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 186 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014918461441993713 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 187 | PASS | FAST8 | 63.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 63.0 | 7 | 6 | 0 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10398124903440475 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 63.0 | 7 | 6 | 0 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15886153280735016 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 194 | SELL | FAST8 | 63.0 | 7 | 6 | 0 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002955665811896324 | 0.0 | 0.0 | +— / -f546078f-fc3e-44a9-9b8f-25c46a043168 |
| Jogador 7 | 4-1 | 195 | BUY | FAST8 | 63.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0582755021750927 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 7 | 4-1 | 196 | BUY_XP | FAST8 | 63.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 197 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00010747917258413509 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 198 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016015805304050446 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 199 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014294106513261795 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 200 | PASS | FAST8 | 63.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 202 | SELL | FAST8 | 63.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07463907450437546 | 0.0 | 0.0 | +— / -6caec849-54f8-4ec1-90a4-fc0587510013 |
| Jogador 7 | 4-2 | 203 | BUY | FAST8 | 63.0 | 7 | 11 | 1 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13128428161144257 | 0.0 | 0.0 | +0803068a-0141-4e75-ab81-12bb13986025 / -— |
| Jogador 7 | 4-2 | 204 | SELL | FAST8 | 63.0 | 7 | 9 | 0 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05875183269381523 | 0.0 | 0.0 | +— / -f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 4-2 | 205 | BUY | FAST8 | 63.0 | 7 | 12 | 1 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7309730648994446 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -— |
| Jogador 7 | 4-2 | 206 | BUY_XP | FAST8 | 63.0 | 7 | 10 | 1 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 207 | BUY_XP | FAST8 | 63.0 | 7 | 6 | 0 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 208 | SELL | FAST8 | 63.0 | 7 | 2 | 0 | 34.0 | Colosso/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04312499240040779 | 0.0 | 0.0 | +— / -97d52b06-365b-44ad-b4f9-63e0f9503c8a |
| Jogador 7 | 4-2 | 209 | BUY_XP | FAST8 | 63.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 210 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04958932846784592 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 212 | BUY | FAST8 | 63.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13301017880439758 | 0.0 | 0.0 | +a7893c5d-2faa-4292-9240-f3cc5813151e / -— |
| Jogador 7 | 4-3 | 213 | BUY_XP | FAST8 | 63.0 | 7 | 4 | 0 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 214 | SELL | FAST8 | 63.0 | 7 | 0 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -a7893c5d-2faa-4292-9240-f3cc5813151e |
| Jogador 7 | 4-3 | 215 | BUY | FAST8 | 63.0 | 7 | 4 | 0 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056144244968891144 | 0.0 | 0.0 | +2357a4df-3c61-4957-83c3-572bbb99ac5a / -— |
| Jogador 7 | 4-3 | 216 | SELL | FAST8 | 63.0 | 7 | 2 | 0 | 34.0 | Colosso/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028866667300462723 | 0.0 | 0.0 | +— / -2357a4df-3c61-4957-83c3-572bbb99ac5a |
| Jogador 7 | 4-3 | 217 | BUY_XP | FAST8 | 63.0 | 7 | 4 | 0 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 218 | MOVE_BOARD | FAST8 | 63.0 | 7 | 0 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0732584074139595 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 219 | MOVE_BOARD | FAST8 | 63.0 | 7 | 0 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20101819932460785 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 220 | PASS | FAST8 | 63.0 | 7 | 0 | 0 | 34.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 222 | BUY | FAST8 | 63.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7636673450469971 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -46320c4e-6bc0-49d6-b150-be378fa422cf,599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 7 | 4-4 | 223 | MOVE_BENCH | FAST8 | 63.0 | 7 | 4 | 0 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5706069469451904 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 224 | BUY | FAST8 | 63.0 | 7 | 4 | 0 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11990348249673843 | 0.0 | 0.0 | +42cf45df-f7dd-418d-a241-d89e69523352 / -— |
| Jogador 7 | 4-4 | 225 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 226 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24390362203121185 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 227 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05471370369195938 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 228 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011512796394526958 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 229 | MOVE_BOARD | FAST8 | 63.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 230 | PASS | FAST8 | 63.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 232 | BUY | FAST8 | 63.0 | 7 | 7 | 0 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045833948999643326 | 0.0 | 0.0 | +9717d30c-f073-470c-a6ce-7db8257de559 / -— |
| Jogador 7 | 4-5 | 233 | SELL | FAST8 | 63.0 | 7 | 3 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -d175e09c-3ed6-4fb3-8c97-0c167862e29e |
| Jogador 7 | 4-5 | 234 | BUY | FAST8 | 63.0 | 7 | 11 | 1 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07716403156518936 | 0.0 | 0.0 | +0f5471bd-1451-4979-adc9-aced6bb63610 / -— |
| Jogador 7 | 4-5 | 235 | BUY_XP | FAST8 | 63.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 236 | BUY_XP | FAST8 | 63.0 | 7 | 4 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 237 | MOVE_BOARD | FAST8 | 63.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05037553235888481 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 238 | MOVE_BOARD | FAST8 | 63.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10136006027460098 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 239 | PASS | FAST8 | 63.0 | 7 | 0 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 242 | SELL | FAST8 | 63.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060877881944179535 | 0.0 | 0.0 | +— / -0f5471bd-1451-4979-adc9-aced6bb63610 |
| Jogador 7 | 4-6 | 243 | BUY | FAST8 | 63.0 | 7 | 11 | 1 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6665524840354919 | 0.0 | 0.0 | +4aa5d560-d9d3-45f9-802a-bdbe95788762 / -0cf5c315-d2f3-4854-a95b-07912b83ea81,d69fa0dc-74b6-4ee7-90f7-aaca5405c59c |
| Jogador 7 | 4-6 | 244 | BUY | FAST8 | 63.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21796193718910217 | 0.0 | 0.0 | +6ea982ab-292d-42fc-99e6-d67c89f9f4fe / -— |
| Jogador 7 | 4-6 | 245 | MOVE_BENCH | FAST8 | 63.0 | 7 | 7 | 0 | 26.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4391731917858124 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 246 | BUY | FAST8 | 63.0 | 7 | 7 | 0 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20913982391357422 | 0.0 | 0.0 | +b0c1aba5-b1bd-48df-abec-19efa8e49d6d / -— |
| Jogador 7 | 4-6 | 247 | MOVE_BOARD | FAST8 | 63.0 | 7 | 4 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 248 | MOVE_BOARD | FAST8 | 63.0 | 7 | 4 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 249 | PASS | FAST8 | 63.0 | 7 | 4 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 252 | SELL | FAST8 | 63.0 | 7 | 11 | 1 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5499547123908997 | 0.0 | 0.0 | +— / -4aa5d560-d9d3-45f9-802a-bdbe95788762 |
| Jogador 7 | 4-7 | 253 | BUY | FAST8 | 63.0 | 7 | 19 | 1 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7658041715621948 | 0.0 | 0.0 | +5416d773-cb2c-442a-8ee9-0d46d22c2087 / -033a84d9-70f6-46a8-a6eb-a2f03be70400,21135c93-ae87-47a0-899c-7eaa0c2c30b8 |
| Jogador 7 | 4-7 | 254 | EQUIP_FROM_INVENTORY | STABILIZE | 63.0 | 7 | 17 | 1 | 24.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10852598398923874 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 255 | EQUIP_FROM_INVENTORY | STABILIZE | 63.0 | 7 | 17 | 1 | 24.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10852598398923874 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 256 | EQUIP_FROM_INVENTORY | STABILIZE | 63.0 | 7 | 17 | 1 | 24.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1331990510225296 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 257 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 17 | 1 | 24.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40685388445854187 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 258 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 17 | 1 | 22.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40592139959335327 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 259 | BUY_XP | FAST8 | 63.0 | 7 | 17 | 1 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01841999962925911 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 260 | BUY_XP | FAST8 | 63.0 | 7 | 13 | 1 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05290624871850014 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 262 | CRAFT_AND_EQUIP | ECON | 63.0 | 8 | 16 | 1 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.0823686495423317 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 263 | CRAFT_AND_EQUIP | ECON | 63.0 | 8 | 16 | 1 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11527988314628601 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 264 | MOVE_BENCH | ECON | 63.0 | 8 | 16 | 1 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17727263271808624 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 265 | MOVE_BENCH | ECON | 63.0 | 8 | 16 | 1 | 26.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07710830122232437 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 266 | BUY | ECON | 63.0 | 8 | 16 | 1 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016896966844797134 | 0.0 | 0.0 | +2f75fcd7-1405-49fd-8a0c-649c1f8a9f09 / -— |
| Jogador 7 | 5-1 | 267 | BUY | ECON | 63.0 | 8 | 11 | 1 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049172401428222656 | 0.0 | 0.0 | +5821f43b-b898-4842-b309-d175f2284a84 / -— |
| Jogador 7 | 5-1 | 268 | BUY_XP | ECON | 63.0 | 8 | 9 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017999999690800905 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 269 | BUY_XP | ECON | 63.0 | 8 | 5 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 270 | MOVE_BOARD | ECON | 63.0 | 8 | 1 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0030704650562256575 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 272 | SELL | ECON | 63.0 | 8 | 10 | 1 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -5416d773-cb2c-442a-8ee9-0d46d22c2087 |
| Jogador 7 | 5-2 | 273 | BUY | ECON | 63.0 | 8 | 15 | 1 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21171993017196655 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 7 | 5-2 | 274 | BUY_XP | ECON | 63.0 | 8 | 12 | 1 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08179999887943268 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 275 | BUY_XP | ECON | 63.0 | 8 | 8 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 276 | BUY_XP | ECON | 63.0 | 8 | 4 | 0 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 277 | MOVE_BENCH | ECON | 63.0 | 8 | 0 | 0 | 32.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40883535146713257 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 278 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 279 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 280 | PASS | WINSTREAK | 63.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 282 | BUY | WINSTREAK | 63.0 | 8 | 9 | 0 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03180460259318352 | 0.0 | 0.0 | +7f9f3188-2482-4518-9fd2-34f0ea1527a9 / -— |
| Jogador 7 | 5-3 | 283 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 7 | 0 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013284384040161967 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 284 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 7 | 0 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1815391629934311 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 285 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 7 | 0 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02849864400923252 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 286 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 7 | 0 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 287 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 7 | 0 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 288 | PASS | WINSTREAK | 63.0 | 8 | 7 | 0 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 292 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 16 | 1 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003268506145104766 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 293 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 16 | 1 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014715333469212055 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 294 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 16 | 1 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01539207249879837 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 295 | PASS | WINSTREAK | 63.0 | 8 | 16 | 1 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028285713866353035 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 302 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 25 | 2 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005421829409897327 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 303 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 25 | 2 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014621439389884472 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 304 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 25 | 2 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 305 | PASS | WINSTREAK | 63.0 | 8 | 25 | 2 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035357143729925156 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 312 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 35 | 3 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.2465146710383124e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 313 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 35 | 3 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 314 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 35 | 3 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500227116048336 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 315 | PASS | WINSTREAK | 63.0 | 8 | 35 | 3 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043214283883571625 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 322 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 47 | 4 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.859398020722438e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 323 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 47 | 4 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014996631070971489 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 324 | PASS | WINSTREAK | 63.0 | 8 | 47 | 4 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.052642855793237686 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 332 | EQUIP_FROM_INVENTORY | WINSTREAK | 63.0 | 8 | 59 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13435231149196625 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 333 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 59 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00956905260682106 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 334 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 59 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007483206689357758 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 335 | PASS | WINSTREAK | 63.0 | 8 | 59 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1023666262626648 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 342 | SELL | WINSTREAK | 63.0 | 8 | 73 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -7f9f3188-2482-4518-9fd2-34f0ea1527a9 |
| Jogador 7 | 6-2 | 343 | BUY | WINSTREAK | 63.0 | 8 | 75 | 5 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4142581820487976 | 0.0 | 0.0 | +aa803972-8af8-46d7-b430-079819730c36 / -— |
| Jogador 7 | 6-2 | 344 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 73 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030210865661501884 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 345 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 73 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013243081979453564 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 346 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 73 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011100084520876408 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 347 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 73 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014897795394062996 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 348 | PASS | WINSTREAK | 63.0 | 8 | 73 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1138707622885704 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 352 | SELL | WINSTREAK | 63.0 | 8 | 87 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -5821f43b-b898-4842-b309-d175f2284a84 |
| Jogador 7 | 6-3 | 353 | BUY | WINSTREAK | 63.0 | 8 | 89 | 5 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9220479130744934 | 0.0 | 0.0 | +4b4293ce-1cca-473e-8c07-b441686985ac / -— |
| Jogador 7 | 6-3 | 354 | MOVE_BOARD | WINSTREAK | 63.0 | 8 | 86 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.3268698239699006e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 355 | SELL | WINSTREAK | 63.0 | 8 | 86 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09960000216960907 | 0.0 | 0.0 | +— / -daa7f698-2fa2-43d7-ae73-ec616b006db4 |
| Jogador 7 | 6-3 | 356 | BUY | WINSTREAK | 63.0 | 8 | 89 | 5 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04675464704632759 | 0.0 | 0.0 | +8025eaf5-b02b-4f94-b381-b94321bca206 / -— |
| Jogador 7 | 6-3 | 357 | SELL | WINSTREAK | 63.0 | 8 | 86 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03200000151991844 | 0.0 | 0.0 | +— / -8025eaf5-b02b-4f94-b381-b94321bca206 |
| Jogador 7 | 6-3 | 358 | BUY | WINSTREAK | 63.0 | 8 | 89 | 5 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1934167593717575 | 0.0 | 0.0 | +00497e43-57ef-4c25-a34b-0be0155bb92d / -— |
| Jogador 7 | 6-3 | 359 | SELL | WINSTREAK | 63.0 | 8 | 85 | 5 | 42.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -00497e43-57ef-4c25-a34b-0be0155bb92d |
| Jogador 7 | 6-3 | 360 | BUY | WINSTREAK | 63.0 | 8 | 89 | 5 | 42.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016672849655151367 | 0.0 | 0.0 | +c4ec99e0-d973-42e9-a20e-1a9e7f5bf89a / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031589943915605545 | 0.0 | 0.0 | +88a02960-5ebe-4b20-b667-1a8ce2728578 / -— |
| Jogador 8 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16182130575180054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3620654344558716 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012301865965127945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5032565593719482 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0140845775604248 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36052340269088745 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 28 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 41 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28077805042266846 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9758638739585876 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 43 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1734657883644104 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 44 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2513078451156616 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 45 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11591774970293045 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 46 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1142356395721436 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -88a02960-5ebe-4b20-b667-1a8ce2728578,dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2009154111146927 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17923711240291595 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05874161794781685 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.103344440460205 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 57 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12421705573797226 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03411445766687393 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-1 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32108795642852783 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03419312834739685 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26146838068962097 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 63 | BUY | STABILIZE | 95.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2964135706424713 | 0.0 | 0.0 | +ebe77c97-f249-4265-ae03-bc8115a4795f / -— |
| Jogador 8 | 2-2 | 64 | SELL | STABILIZE | 95.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21281053125858307 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-2 | 65 | BUY_XP | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 66 | PASS | STABILIZE | 95.0 | 4 | 2 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 8 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.046098232269287 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 73 | BUY | STABILIZE | 90.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36479753255844116 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 74 | SELL | STABILIZE | 90.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-3 | 75 | BUY | STABILIZE | 90.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22588230669498444 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 76 | SELL | STABILIZE | 90.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13300000131130219 | 0.0 | 0.0 | +— / -ebe77c97-f249-4265-ae03-bc8115a4795f |
| Jogador 8 | 2-3 | 77 | SELL | STABILIZE | 90.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14517425000667572 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5311523675918579 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 79 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 7 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08554541319608688 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 80 | SELL | STABILIZE | 90.0 | 4 | 7 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10100000351667404 | 0.0 | 0.0 | +— / -a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 8 | 2-4 | 82 | BUY | LOSS_STREAK | 84.0 | 5 | 15 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20011378824710846 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 83 | MOVE_BENCH | LOSS_STREAK | 84.0 | 5 | 12 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09412594884634018 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 84 | BUY | LOSS_STREAK | 84.0 | 5 | 12 | 1 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016324933618307114 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 85 | MOVE_BENCH | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48129725456237793 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 86 | BUY | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04594850912690163 | 0.0 | 0.0 | +3644801e-2247-403d-8b81-d2d3f15c2f55 / -— |
| Jogador 8 | 2-4 | 87 | SELL | LOSS_STREAK | 84.0 | 5 | 8 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3996666669845581 | 0.0 | 0.0 | +— / -3644801e-2247-403d-8b81-d2d3f15c2f55 |
| Jogador 8 | 2-4 | 88 | SELL | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3076666593551636 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-4 | 89 | BUY | LOSS_STREAK | 84.0 | 5 | 12 | 1 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030430641025304794 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 8 | 2-4 | 90 | SELL | LOSS_STREAK | 84.0 | 5 | 11 | 1 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3569999933242798 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 8 | 2-5 | 92 | BUY | LOSS_STREAK | 84.0 | 5 | 19 | 1 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9693825840950012 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 93 | BUY | LOSS_STREAK | 84.0 | 5 | 18 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2951633632183075 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 94 | BUY | STABILIZE | 84.0 | 5 | 16 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29031121730804443 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 95 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.490450918674469 | 0.0 | 0.0 | +— / -35e1a0f6-207d-4df2-b096-fc07962d094a |
| Jogador 8 | 2-5 | 96 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 15 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30819740891456604 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 97 | SELL | STABILIZE | 84.0 | 5 | 15 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5798666477203369 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-5 | 98 | BUY | STABILIZE | 84.0 | 5 | 18 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08949927240610123 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-5 | 99 | BUY_XP | STABILIZE | 84.0 | 5 | 16 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 100 | BUY_XP | STABILIZE | 84.0 | 5 | 12 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 102 | BUY | STABILIZE | 84.0 | 5 | 14 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9777796864509583 | 0.0 | 0.0 | +c737e99a-613e-4f1a-a50e-7a865169f90c / -— |
| Jogador 8 | 2-6 | 103 | BUY | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32871952652931213 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 104 | SELL | STABILIZE | 84.0 | 5 | 10 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05799546837806702 | 0.0 | 0.0 | +— / -c0d8da9e-5ede-4a26-8c5c-e2a908318bfd |
| Jogador 8 | 2-6 | 105 | BUY | STABILIZE | 84.0 | 5 | 12 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13876228034496307 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 106 | SELL | STABILIZE | 84.0 | 5 | 9 | 0 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3423333466053009 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 2-6 | 107 | SELL | STABILIZE | 84.0 | 5 | 12 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18589305877685547 | 0.0 | 0.0 | +— / -87600495-fe90-4832-ab42-9a5cb0ebe3f4 |
| Jogador 8 | 2-6 | 108 | SELL | STABILIZE | 84.0 | 5 | 15 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 2-6 | 109 | BUY | STABILIZE | 84.0 | 5 | 16 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0850246250629425 | 0.0 | 0.0 | +c9a1ea77-662a-469a-ba7f-eac0713c0c52 / -— |
| Jogador 8 | 2-6 | 110 | SELL | STABILIZE | 84.0 | 5 | 14 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37566667795181274 | 0.0 | 0.0 | +— / -c9a1ea77-662a-469a-ba7f-eac0713c0c52 |
| Jogador 8 | 2-7 | 112 | BUY | STABILIZE | 84.0 | 5 | 24 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.355785995721817 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 113 | BUY | STABILIZE | 84.0 | 5 | 21 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06387972831726074 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 114 | SELL | STABILIZE | 84.0 | 5 | 18 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3191694915294647 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 2-7 | 115 | BUY | STABILIZE | 84.0 | 5 | 21 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20156064629554749 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 116 | SELL | STABILIZE | 84.0 | 5 | 20 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41966667771339417 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 2-7 | 117 | BUY | STABILIZE | 84.0 | 5 | 21 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11780723929405212 | 0.0 | 0.0 | +60b0249f-e02f-4aca-b90d-75e9bcc822b8 / -— |
| Jogador 8 | 2-7 | 118 | SELL | STABILIZE | 84.0 | 5 | 20 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3943333327770233 | 0.0 | 0.0 | +— / -60b0249f-e02f-4aca-b90d-75e9bcc822b8 |
| Jogador 8 | 2-7 | 119 | SELL | STABILIZE | 84.0 | 5 | 21 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18939507007598877 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 2-7 | 120 | SELL | STABILIZE | 84.0 | 5 | 24 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -5de56114-806a-4f58-8241-b3b8434a2154 |
| Jogador 8 | 3-1 | 122 | BUY | STABILIZE | 84.0 | 5 | 33 | 3 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1409929096698761 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 123 | BUY | STABILIZE | 84.0 | 5 | 29 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0013406898360699415 | 0.0 | 0.0 | +88420167-3841-43dd-b1d0-3e5ab2294c78 / -— |
| Jogador 8 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 5 | 27 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.26044148206710815 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 125 | BUY_XP | STABILIZE | 84.0 | 5 | 27 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10628499835729599 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 126 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 23 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06051783263683319 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 127 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 23 | 2 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.385818749666214 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 128 | MOVE_BOARD | FAST8 | 84.0 | 6 | 23 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015165128745138645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 129 | BUY | FAST8 | 84.0 | 6 | 23 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.269667387008667 | 0.0 | 0.0 | +a5c0595b-85f9-4c71-a156-675d22a7b3c2 / -— |
| Jogador 8 | 3-1 | 130 | MOVE_BOARD | FAST8 | 84.0 | 6 | 21 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 132 | BUY | FAST8 | 84.0 | 6 | 30 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11953677237033844 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 133 | BUY | FAST8 | 84.0 | 6 | 26 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011059205047786236 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 134 | BUY | FAST8 | 84.0 | 6 | 25 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0924394503235817 | 0.0 | 0.0 | +5326031a-1b7e-4dbd-b58b-1e81029d42a1 / -— |
| Jogador 8 | 3-2 | 135 | MOVE_BOARD | FAST8 | 84.0 | 6 | 23 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017286833608523011 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 136 | BUY_XP | FAST8 | 84.0 | 6 | 23 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 137 | SELL | FAST8 | 84.0 | 6 | 19 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31299999356269836 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-2 | 138 | BUY_XP | FAST8 | 84.0 | 6 | 20 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 139 | BUY_XP | FAST8 | 84.0 | 6 | 16 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 140 | BUY_XP | FAST8 | 84.0 | 6 | 12 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 142 | BUY | FAST8 | 84.0 | 6 | 15 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21054641902446747 | 0.0 | 0.0 | +1af578c1-57cf-4752-93e7-d0eebc6e8ae5 / -— |
| Jogador 8 | 3-3 | 143 | BUY | FAST8 | 84.0 | 6 | 13 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01673102006316185 | 0.0 | 0.0 | +3bf8af53-85e7-4e5b-8cf8-b7198a955e8d / -— |
| Jogador 8 | 3-3 | 144 | BUY | FAST8 | 84.0 | 6 | 12 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3003251254558563 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 145 | SELL | FAST8 | 84.0 | 6 | 9 | 0 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05649999901652336 | 0.0 | 0.0 | +— / -3bf8af53-85e7-4e5b-8cf8-b7198a955e8d |
| Jogador 8 | 3-3 | 146 | SELL | FAST8 | 84.0 | 6 | 10 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020999999716877937 | 0.0 | 0.0 | +— / -a5c0595b-85f9-4c71-a156-675d22a7b3c2 |
| Jogador 8 | 3-3 | 147 | SELL | FAST8 | 84.0 | 6 | 12 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04899999871850014 | 0.0 | 0.0 | +— / -88420167-3841-43dd-b1d0-3e5ab2294c78 |
| Jogador 8 | 3-3 | 148 | BUY | FAST8 | 84.0 | 6 | 14 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0706252008676529 | 0.0 | 0.0 | +8df39648-f588-452a-b234-32da76c43aff / -— |
| Jogador 8 | 3-3 | 149 | SELL | FAST8 | 84.0 | 6 | 13 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3655177056789398 | 0.0 | 0.0 | +— / -8df39648-f588-452a-b234-32da76c43aff |
| Jogador 8 | 3-3 | 150 | SELL | FAST8 | 84.0 | 6 | 14 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.061876632273197174 | 0.0 | 0.0 | +— / -5326031a-1b7e-4dbd-b58b-1e81029d42a1 |
| Jogador 8 | 3-4 | 152 | BUY | FAST8 | 84.0 | 6 | 25 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24681594967842102 | 0.0 | 0.0 | +eb7e36f0-cef9-4a2e-979a-f8a357da73e8 / -— |
| Jogador 8 | 3-4 | 153 | BUY | FAST8 | 84.0 | 6 | 24 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009836411336436868 | 0.0 | 0.0 | +e8355df5-8ee7-44a3-ab88-3708c14fd5dc / -— |
| Jogador 8 | 3-4 | 154 | BUY | FAST8 | 84.0 | 6 | 23 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22635821998119354 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 155 | SELL | FAST8 | 84.0 | 6 | 20 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39264577627182007 | 0.0 | 0.0 | +— / -e8355df5-8ee7-44a3-ab88-3708c14fd5dc |
| Jogador 8 | 3-4 | 156 | BUY | FAST8 | 84.0 | 6 | 21 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1972464621067047 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 157 | SELL | FAST8 | 84.0 | 6 | 19 | 1 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26899999380111694 | 0.0 | 0.0 | +— / -d5848998-33f3-4632-94c0-60388a7cc6b8 |
| Jogador 8 | 3-4 | 158 | SELL | FAST8 | 84.0 | 6 | 21 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3423333466053009 | 0.0 | 0.0 | +— / -82e109f9-54c8-492d-93e5-7e0dd0034b15 |
| Jogador 8 | 3-4 | 159 | SELL | FAST8 | 84.0 | 6 | 24 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -e4605ac7-0b51-4f1c-a658-f7d25f9a9dae |
| Jogador 8 | 3-4 | 160 | SELL | FAST8 | 84.0 | 6 | 27 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014333332888782024 | 0.0 | 0.0 | +— / -4ac49c80-f0c3-47ae-a031-96928d244e13 |
| Jogador 8 | 3-5 | 162 | BUY | FAST8 | 84.0 | 6 | 41 | 4 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6914997696876526 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 163 | BUY | FAST8 | 84.0 | 6 | 39 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8124799132347107 | 0.0 | 0.0 | +6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 / -1af578c1-57cf-4752-93e7-d0eebc6e8ae5,9b5e9e71-6772-49bc-979f-11f446f27b11 |
| Jogador 8 | 3-5 | 164 | BUY | FAST8 | 84.0 | 6 | 37 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2381594330072403 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 8 | 3-5 | 165 | SELL | FAST8 | 84.0 | 6 | 34 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 |
| Jogador 8 | 3-5 | 166 | SELL | FAST8 | 84.0 | 6 | 39 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5529999732971191 | 0.0 | 0.0 | +— / -eb7e36f0-cef9-4a2e-979a-f8a357da73e8 |
| Jogador 8 | 3-5 | 167 | BUY | FAST8 | 84.0 | 6 | 40 | 4 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12819309532642365 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 8 | 3-5 | 168 | BUY_XP | FAST8 | 84.0 | 6 | 37 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004757499787956476 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 169 | BUY_XP | FAST8 | 84.0 | 6 | 33 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07524249702692032 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 170 | BUY_XP | FAST8 | 84.0 | 6 | 29 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08860000222921371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 172 | BUY | FAST8 | 84.0 | 7 | 36 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7635684013366699 | 0.0 | 0.0 | +b55260cd-3c6a-4cb8-99d0-b7c6471103ad / -— |
| Jogador 8 | 3-6 | 173 | BUY | FAST8 | 84.0 | 7 | 33 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2520100176334381 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 174 | BUY | FAST8 | 84.0 | 7 | 30 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1441650688648224 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 175 | MOVE_BENCH | FAST8 | 84.0 | 7 | 26 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40158215165138245 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 176 | BUY | FAST8 | 84.0 | 7 | 26 | 2 | 34.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2259654849767685 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -— |
| Jogador 8 | 3-6 | 177 | MOVE_BOARD | FAST8 | 84.0 | 7 | 24 | 2 | 34.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 178 | MOVE_BOARD | FAST8 | 84.0 | 7 | 24 | 2 | 34.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 179 | PASS | FAST8 | 84.0 | 7 | 24 | 2 | 34.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02199999988079071 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 182 | BUY | FAST8 | 84.0 | 7 | 35 | 3 | 34.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07099445909261703 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 183 | BUY | FAST8 | 84.0 | 7 | 32 | 3 | 34.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27008533477783203 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 8 | 3-7 | 184 | MOVE_BOARD | FAST8 | 84.0 | 7 | 29 | 2 | 34.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0011844867840409279 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 185 | SELL | FAST8 | 84.0 | 7 | 29 | 2 | 34.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08910000324249268 | 0.0 | 0.0 | +— / -112206a4-c285-4f76-878a-056248cba468 |
| Jogador 8 | 3-7 | 186 | BUY | FAST8 | 84.0 | 7 | 32 | 3 | 34.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03549084812402725 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 8 | 3-7 | 187 | MOVE_BOARD | FAST8 | 84.0 | 7 | 31 | 3 | 34.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 188 | SELL | FAST8 | 84.0 | 7 | 31 | 3 | 34.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005785343702882528 | 0.0 | 0.0 | +— / -a14e4b8f-77c5-4909-a9ee-0044b836a877 |
| Jogador 8 | 3-7 | 189 | SELL | FAST8 | 84.0 | 7 | 32 | 3 | 34.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4183333218097687 | 0.0 | 0.0 | +— / -849ea0fc-7f61-4907-8abb-b25c8cc82efc |
| Jogador 8 | 3-7 | 190 | MOVE_BOARD | FAST8 | 84.0 | 7 | 35 | 3 | 34.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 192 | BUY | FAST8 | 84.0 | 7 | 46 | 4 | 34.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8579959273338318 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -64afe66e-d5a9-466c-a4ff-9d32c9f153ce,f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 4-1 | 193 | BUY | FAST8 | 84.0 | 7 | 45 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6128393411636353 | 0.0 | 0.0 | +88035b70-61e0-4279-9d55-e451f412f0d3 / -— |
| Jogador 8 | 4-1 | 194 | CRAFT_AND_EQUIP | FAST8 | 84.0 | 7 | 42 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22672857344150543 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 195 | CRAFT_AND_EQUIP | FAST8 | 84.0 | 7 | 42 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24980567395687103 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 196 | BUY | FAST8 | 84.0 | 7 | 42 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04976925998926163 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 8 | 4-1 | 197 | SELL | FAST8 | 84.0 | 7 | 39 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -2faa526c-d29e-47a9-9eb3-5030750cb483 |
| Jogador 8 | 4-1 | 198 | BUY_XP | FAST8 | 84.0 | 7 | 42 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09842000156641006 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 199 | BUY_XP | FAST8 | 84.0 | 7 | 38 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01841999962925911 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 200 | BUY_XP | FAST8 | 84.0 | 7 | 34 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01841999962925911 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 202 | BUY | FAST8 | 84.0 | 7 | 42 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41300323605537415 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -— |
| Jogador 8 | 4-2 | 203 | SELL | FAST8 | 84.0 | 7 | 39 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0460510216653347 | 0.0 | 0.0 | +— / -1e81ac95-667f-494d-89eb-2bcdcf887a7e |
| Jogador 8 | 4-2 | 204 | BUY | FAST8 | 84.0 | 7 | 42 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07168050110340118 | 0.0 | 0.0 | +08a36d54-bb5c-48a6-afb1-e0f9943bf069 / -— |
| Jogador 8 | 4-2 | 205 | SELL | FAST8 | 84.0 | 7 | 38 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0724666640162468 | 0.0 | 0.0 | +— / -08a36d54-bb5c-48a6-afb1-e0f9943bf069 |
| Jogador 8 | 4-2 | 206 | BUY_XP | FAST8 | 84.0 | 7 | 42 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09842000156641006 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 207 | BUY_XP | FAST8 | 84.0 | 7 | 38 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01841999962925911 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 208 | BUY_XP | FAST8 | 84.0 | 7 | 34 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01841999962925911 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 209 | BUY_XP | FAST8 | 84.0 | 7 | 30 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09842000156641006 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 210 | BUY_XP | FAST8 | 84.0 | 7 | 26 | 2 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01841999962925911 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 212 | BUY | FAST8 | 84.0 | 7 | 33 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7690063714981079 | 0.0 | 0.0 | +696f53ae-1413-47cc-b491-9870b7bcba51 / -— |
| Jogador 8 | 4-3 | 213 | SELL | FAST8 | 84.0 | 7 | 31 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46925845742225647 | 0.0 | 0.0 | +— / -dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 |
| Jogador 8 | 4-3 | 214 | BUY | FAST8 | 84.0 | 7 | 34 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08620814234018326 | 0.0 | 0.0 | +7dfeef88-7e1d-43b8-b012-017278ec61dc / -— |
| Jogador 8 | 4-3 | 215 | SELL | FAST8 | 84.0 | 7 | 31 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -7dfeef88-7e1d-43b8-b012-017278ec61dc |
| Jogador 8 | 4-3 | 216 | BUY | FAST8 | 84.0 | 7 | 34 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0824369490146637 | 0.0 | 0.0 | +e1867f53-f97a-4c7a-bce3-24aa037ce27f / -— |
| Jogador 8 | 4-3 | 217 | SELL | FAST8 | 84.0 | 7 | 30 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -e1867f53-f97a-4c7a-bce3-24aa037ce27f |
| Jogador 8 | 4-3 | 218 | SELL | FAST8 | 84.0 | 7 | 34 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5227690935134888 | 0.0 | 0.0 | +— / -88035b70-61e0-4279-9d55-e451f412f0d3 |
| Jogador 8 | 4-3 | 219 | BUY_XP | FAST8 | 84.0 | 7 | 37 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01841999962925911 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 220 | SELL | FAST8 | 84.0 | 7 | 33 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4423777759075165 | 0.0 | 0.0 | +— / -a23ee552-279e-4c6c-aa05-6197043e8f1d |
| Jogador 8 | 4-4 | 222 | BUY | FAST8 | 72.0 | 7 | 45 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8281354904174805 | 0.0 | 0.0 | +1022f12a-84e9-4eeb-81dc-706092de3728 / -— |
| Jogador 8 | 4-4 | 223 | BUY | FAST8 | 72.0 | 7 | 42 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8555426001548767 | 0.0 | 0.0 | +e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 / -696f53ae-1413-47cc-b491-9870b7bcba51,b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 |
| Jogador 8 | 4-4 | 224 | BUY | FAST8 | 72.0 | 7 | 40 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21502725780010223 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 8 | 4-4 | 225 | SELL | FAST8 | 72.0 | 7 | 38 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5450000166893005 | 0.0 | 0.0 | +— / -e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 |
| Jogador 8 | 4-4 | 226 | BUY_XP | FAST8 | 72.0 | 7 | 43 | 4 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09842000156641006 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 227 | BUY_XP | FAST8 | 72.0 | 7 | 39 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07968749850988388 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 228 | MOVE_BENCH | ECON | 72.0 | 8 | 35 | 3 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0606953464448452 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 229 | MOVE_BENCH | ECON | 72.0 | 8 | 35 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2690659761428833 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 230 | BUY | ECON | 72.0 | 8 | 35 | 3 | 36.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05094870924949646 | 0.0 | 0.0 | +11b28280-bb53-4ca7-81b7-5ce8705303a5 / -— |
| Jogador 8 | 4-5 | 232 | BUY | ECON | 72.0 | 8 | 42 | 4 | 36.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07745794951915741 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 8 | 4-5 | 233 | BUY | ECON | 72.0 | 8 | 39 | 3 | 36.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08045153319835663 | 0.0 | 0.0 | +42aa4dc8-e388-40dd-a210-4c59e358afcd / -— |
| Jogador 8 | 4-5 | 234 | BUY | ECON | 72.0 | 8 | 35 | 3 | 36.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041657838970422745 | 0.0 | 0.0 | +a5c83255-d413-4d36-92a8-3552e6785108 / -— |
| Jogador 8 | 4-5 | 235 | MOVE_BOARD | ECON | 72.0 | 8 | 33 | 3 | 36.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 236 | MOVE_BOARD | ECON | 72.0 | 8 | 33 | 3 | 36.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012443402782082558 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 237 | PASS | ECON | 72.0 | 8 | 33 | 3 | 36.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 242 | BUY | ECON | 72.0 | 8 | 42 | 4 | 42.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7907611131668091 | 0.0 | 0.0 | +590d07db-5e90-4705-a7ae-96f84fd06382 / -— |
| Jogador 8 | 4-6 | 243 | MOVE_BOARD | ECON | 72.0 | 8 | 40 | 4 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 244 | MOVE_BOARD | ECON | 72.0 | 8 | 40 | 4 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 245 | PASS | ECON | 72.0 | 8 | 40 | 4 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15785714983940125 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 252 | MOVE_BOARD | ECON | 72.0 | 8 | 51 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 253 | MOVE_BOARD | ECON | 72.0 | 8 | 51 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 254 | PASS | ECON | 72.0 | 8 | 51 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03547321632504463 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 262 | CRAFT_AND_EQUIP | ECON | 72.0 | 8 | 62 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06962829828262329 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 263 | CRAFT_AND_EQUIP | ECON | 72.0 | 8 | 62 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11618173867464066 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 264 | MOVE_BOARD | ECON | 72.0 | 8 | 62 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.307935786433518e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 265 | SELL | ECON | 72.0 | 8 | 62 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021789109334349632 | 0.0 | 0.0 | +— / -11b28280-bb53-4ca7-81b7-5ce8705303a5 |
| Jogador 8 | 5-1 | 266 | BUY | ECON | 72.0 | 8 | 63 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14680631458759308 | 0.0 | 0.0 | +45ae38c5-7e69-41bb-9a93-f14db3af3587 / -— |
| Jogador 8 | 5-1 | 267 | MOVE_BOARD | ECON | 72.0 | 8 | 59 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 268 | MOVE_BOARD | ECON | 72.0 | 8 | 59 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 269 | PASS | ECON | 72.0 | 8 | 59 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09383607655763626 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 272 | SELL | ECON | 58.0 | 8 | 69 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -a5c83255-d413-4d36-92a8-3552e6785108 |
| Jogador 8 | 5-2 | 273 | BUY | ECON | 58.0 | 8 | 71 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7452792525291443 | 0.0 | 0.0 | +a1357716-abf4-4d4f-abb8-34f2681f16dd / -— |
| Jogador 8 | 5-2 | 274 | SELL | ECON | 58.0 | 8 | 68 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02252502739429474 | 0.0 | 0.0 | +— / -42aa4dc8-e388-40dd-a210-4c59e358afcd |
| Jogador 8 | 5-2 | 275 | BUY | ECON | 58.0 | 8 | 72 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33701765537261963 | 0.0 | 0.0 | +39b89fbe-9520-4eaa-80f9-81e03232c83c / -— |
| Jogador 8 | 5-2 | 276 | MOVE_BOARD | ECON | 58.0 | 8 | 69 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 277 | MOVE_BOARD | ECON | 58.0 | 8 | 69 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 278 | PASS | ECON | 58.0 | 8 | 69 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10127647966146469 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 282 | SELL | ECON | 42.0 | 8 | 80 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05713333189487457 | 0.0 | 0.0 | +— / -45ae38c5-7e69-41bb-9a93-f14db3af3587 |
| Jogador 8 | 5-3 | 283 | BUY | ECON | 42.0 | 8 | 84 | 5 | 42.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0022263526916504 | 0.0 | 0.0 | +d2afd490-f89f-47c9-8279-a88acde5b1b6 / -590d07db-5e90-4705-a7ae-96f84fd06382,5b96c8f7-bacb-47df-8666-30d30d49549d |
| Jogador 8 | 5-3 | 284 | BUY | ECON | 42.0 | 8 | 82 | 5 | 38.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8567274212837219 | 0.0 | 0.0 | +f00a538c-0607-4d8b-babe-7c13daf80c42 / -— |
| Jogador 8 | 5-3 | 285 | SELL | ECON | 42.0 | 8 | 79 | 5 | 38.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -d2afd490-f89f-47c9-8279-a88acde5b1b6 |
| Jogador 8 | 5-3 | 286 | BUY | ECON | 42.0 | 8 | 84 | 5 | 38.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.001591682434082 | 0.0 | 0.0 | +2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d / -39b89fbe-9520-4eaa-80f9-81e03232c83c,f00a538c-0607-4d8b-babe-7c13daf80c42 |
| Jogador 8 | 5-3 | 287 | BUY | ECON | 42.0 | 8 | 81 | 5 | 38.0 | Enfeitiçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019758611917495728 | 0.0 | 0.0 | +a267d973-f857-4dda-89e1-209bff42ab6f / -— |
| Jogador 8 | 5-3 | 288 | BUY | ECON | 42.0 | 8 | 78 | 5 | 38.0 | Enfeitiçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04214362055063248 | 0.0 | 0.0 | +76fcc4d0-4988-4e99-8ac0-c251f0b99dcd / -— |
| Jogador 8 | 5-3 | 289 | MOVE_BOARD | ECON | 42.0 | 8 | 76 | 5 | 38.0 | Enfeitiçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001096380758099258 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 290 | MOVE_BOARD | ECON | 42.0 | 8 | 76 | 5 | 38.0 | Enfeitiçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 292 | SELL | ECON | 42.0 | 8 | 87 | 5 | 38.0 | Enfeitiçador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d |
| Jogador 8 | 5-4 | 293 | BUY | ECON | 42.0 | 8 | 95 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5215674042701721 | 0.0 | 0.0 | +150a2da3-f559-4a40-a058-005e9c74e11f / -— |
| Jogador 8 | 5-4 | 294 | SELL | ECON | 42.0 | 8 | 92 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015533333644270897 | 0.0 | 0.0 | +— / -76fcc4d0-4988-4e99-8ac0-c251f0b99dcd |
| Jogador 8 | 5-4 | 295 | BUY | ECON | 42.0 | 8 | 94 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3527024984359741 | 0.0 | 0.0 | +efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 / -— |
| Jogador 8 | 5-4 | 296 | SELL | ECON | 42.0 | 8 | 91 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4545666575431824 | 0.0 | 0.0 | +— / -a267d973-f857-4dda-89e1-209bff42ab6f |
| Jogador 8 | 5-4 | 297 | BUY | ECON | 42.0 | 8 | 94 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03526065871119499 | 0.0 | 0.0 | +8486b8a9-20fe-4234-bbba-0efa031c3b76 / -— |
| Jogador 8 | 5-4 | 298 | MOVE_BOARD | ECON | 42.0 | 8 | 90 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 299 | MOVE_BOARD | ECON | 42.0 | 8 | 90 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 300 | PASS | ECON | 42.0 | 8 | 90 | 5 | 38.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12867063283920288 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 302 | BUY | ECON | 42.0 | 8 | 100 | 5 | 46.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7153869271278381 | 0.0 | 0.0 | +3ae84928-bc2a-4c1e-8663-b7ad05da4501 / -— |
| Jogador 8 | 5-5 | 303 | SELL | ECON | 42.0 | 8 | 97 | 5 | 46.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -150a2da3-f559-4a40-a058-005e9c74e11f |
| Jogador 8 | 5-5 | 304 | BUY | ECON | 42.0 | 8 | 100 | 5 | 46.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7003851532936096 | 0.0 | 0.0 | +0a6e3194-ed55-43ad-ac66-31e08ccda7aa / -— |
| Jogador 8 | 5-5 | 305 | MOVE_BOARD | ECON | 42.0 | 8 | 97 | 5 | 46.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 306 | MOVE_BOARD | ECON | 42.0 | 8 | 97 | 5 | 46.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 307 | PASS | ECON | 42.0 | 8 | 97 | 5 | 46.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1353365182876587 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 312 | SELL | ECON | 42.0 | 8 | 109 | 5 | 46.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5129340291023254 | 0.0 | 0.0 | +— / -3ae84928-bc2a-4c1e-8663-b7ad05da4501 |
| Jogador 8 | 5-6 | 313 | BUY | ECON | 42.0 | 8 | 112 | 5 | 46.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3972700238227844 | 0.0 | 0.0 | +c93990ff-0a6f-46bc-8fc1-12623d55abc1 / -— |
| Jogador 8 | 5-6 | 314 | SELL | ECON | 42.0 | 8 | 108 | 5 | 46.0 | Enfeitiçador/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5078999996185303 | 0.0 | 0.0 | +— / -0a6e3194-ed55-43ad-ac66-31e08ccda7aa |
| Jogador 8 | 5-6 | 315 | BUY | ECON | 42.0 | 8 | 111 | 5 | 46.0 | Enfeitiçador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9703799486160278 | 0.0 | 0.0 | +1ad1f705-7e6b-4c1f-811c-2863dbf2db9e / -7fb0217d-521c-42b5-995c-81e299b3b934,a1357716-abf4-4d4f-abb8-34f2681f16dd |
| Jogador 8 | 5-6 | 316 | BUY | ECON | 42.0 | 8 | 108 | 5 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37692922353744507 | 0.0 | 0.0 | +2a2b613e-8850-4c70-ab66-bc18356178e8 / -— |
| Jogador 8 | 5-6 | 317 | BUY | ECON | 42.0 | 8 | 107 | 5 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03663884848356247 | 0.0 | 0.0 | +7d8564c6-8151-4e04-b028-2121cb064215 / -— |
| Jogador 8 | 5-6 | 318 | MOVE_BOARD | ECON | 42.0 | 8 | 105 | 5 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 319 | MOVE_BOARD | ECON | 42.0 | 8 | 105 | 5 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 320 | PASS | ECON | 42.0 | 8 | 105 | 5 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1430618166923523 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 322 | SELL | ECON | 42.0 | 8 | 117 | 5 | 46.0 | Enfeitiçador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1182333305478096 | 0.0 | 0.0 | +— / -1ad1f705-7e6b-4c1f-811c-2863dbf2db9e |
| Jogador 8 | 5-7 | 323 | BUY | ECON | 42.0 | 8 | 125 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8690500259399414 | 0.0 | 0.0 | +e89905aa-6564-4e15-bc3a-c281646446bc / -— |
| Jogador 8 | 5-7 | 324 | SELL | ECON | 42.0 | 8 | 122 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -7d8564c6-8151-4e04-b028-2121cb064215 |
| Jogador 8 | 5-7 | 325 | BUY | ECON | 42.0 | 8 | 124 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19363287091255188 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -— |
| Jogador 8 | 5-7 | 326 | SELL | ECON | 42.0 | 8 | 120 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -4261ad99-2607-4d90-978c-9e9abffd6d95 |
| Jogador 8 | 5-7 | 327 | BUY | ECON | 42.0 | 8 | 124 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19363439083099365 | 0.0 | 0.0 | +56332309-e8e8-464a-904f-e9253912cd2f / -— |
| Jogador 8 | 5-7 | 328 | MOVE_BOARD | ECON | 42.0 | 8 | 120 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 329 | MOVE_BOARD | ECON | 42.0 | 8 | 120 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 330 | PASS | ECON | 42.0 | 8 | 120 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15780650079250336 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ECON | 42.0 | 8 | 131 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.01723370887339115 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 333 | SELL | ECON | 42.0 | 8 | 131 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -56332309-e8e8-464a-904f-e9253912cd2f |
| Jogador 8 | 6-1 | 334 | BUY | ECON | 42.0 | 8 | 135 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7230440378189087 | 0.0 | 0.0 | +e7c18780-1d70-4a15-ad72-2eaa0f81df8d / -— |
| Jogador 8 | 6-1 | 335 | SELL | ECON | 42.0 | 8 | 131 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -2a2b613e-8850-4c70-ab66-bc18356178e8 |
| Jogador 8 | 6-1 | 336 | BUY | ECON | 42.0 | 8 | 132 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05251765996217728 | 0.0 | 0.0 | +63c47a3f-6712-4cfa-9376-6140da170089 / -— |
| Jogador 8 | 6-1 | 337 | MOVE_BOARD | ECON | 42.0 | 8 | 128 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -6.0121055867057294e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 338 | MOVE_BOARD | ECON | 42.0 | 8 | 128 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014945494942367077 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 339 | PASS | ECON | 42.0 | 8 | 128 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1804772913455963 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 342 | SELL | ALL_IN | 23.0 | 8 | 138 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02276334911584854 | 0.0 | 0.0 | +— / -63c47a3f-6712-4cfa-9376-6140da170089 |
| Jogador 8 | 6-2 | 343 | BUY | ALL_IN | 23.0 | 8 | 142 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5445646047592163 | 0.0 | 0.0 | +3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 / -— |
| Jogador 8 | 6-2 | 344 | SELL | ALL_IN | 23.0 | 8 | 141 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6769000291824341 | 0.0 | 0.0 | +— / -3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 |
| Jogador 8 | 6-2 | 345 | BUY | ALL_IN | 23.0 | 8 | 142 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2935151755809784 | 0.0 | 0.0 | +ae9da355-52b7-402c-be6e-41fa1148a550 / -— |
| Jogador 8 | 6-2 | 346 | SELL | ALL_IN | 23.0 | 8 | 141 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08111539483070374 | 0.0 | 0.0 | +— / -ae9da355-52b7-402c-be6e-41fa1148a550 |
| Jogador 8 | 6-2 | 347 | BUY | ALL_IN | 23.0 | 8 | 142 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061906006187200546 | 0.0 | 0.0 | +425a58b3-d906-4381-9afc-00f9852c9982 / -— |
| Jogador 8 | 6-2 | 348 | SELL | ALL_IN | 23.0 | 8 | 139 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014142206870019436 | 0.0 | 0.0 | +— / -425a58b3-d906-4381-9afc-00f9852c9982 |
| Jogador 8 | 6-2 | 349 | BUY | ALL_IN | 23.0 | 8 | 142 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07467624545097351 | 0.0 | 0.0 | +2ac6d717-87f1-4421-929e-1934a9317e72 / -— |
| Jogador 8 | 6-2 | 350 | MOVE_BOARD | ALL_IN | 23.0 | 8 | 141 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.167440404969966e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 352 | SELL | ALL_IN | 6.0 | 8 | 152 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015236873179674149 | 0.0 | 0.0 | +— / -2ac6d717-87f1-4421-929e-1934a9317e72 |
| Jogador 8 | 6-3 | 353 | BUY | ALL_IN | 6.0 | 8 | 153 | 5 | 46.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0812277793884277 | 0.0 | 0.0 | +5e8a73b8-846a-49a9-be41-30c3baf2cb55 / -8486b8a9-20fe-4234-bbba-0efa031c3b76,e7c18780-1d70-4a15-ad72-2eaa0f81df8d |
| Jogador 8 | 6-3 | 354 | BUY | ALL_IN | 6.0 | 8 | 149 | 5 | 38.0 | Enfeitiçador/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25244778394699097 | 0.0 | 0.0 | +5d95f8bc-0c01-4c67-8764-4410eb32ee93 / -— |
| Jogador 8 | 6-3 | 355 | SELL | ALL_IN | 6.0 | 8 | 145 | 5 | 38.0 | Enfeitiçador/DA_Amumu18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0819307416677475 | 0.0 | 0.0 | +— / -5e8a73b8-846a-49a9-be41-30c3baf2cb55 |
| Jogador 8 | 6-3 | 356 | BUY | ALL_IN | 6.0 | 8 | 156 | 5 | 38.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024328233674168587 | 0.0 | 0.0 | +46b04fe4-ef4d-4449-94d0-d8bc9660c4e0 / -— |
| Jogador 8 | 6-3 | 357 | SELL | ALL_IN | 6.0 | 8 | 154 | 5 | 38.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -46b04fe4-ef4d-4449-94d0-d8bc9660c4e0 |
| Jogador 8 | 6-3 | 358 | BUY | ALL_IN | 6.0 | 8 | 156 | 5 | 38.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23196493089199066 | 0.0 | 0.0 | +3a17cc98-2024-4ac0-b627-9a751d138cd9 / -— |
| Jogador 8 | 6-3 | 359 | SELL | ALL_IN | 6.0 | 8 | 155 | 5 | 38.0 | Enfeitiçador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01133333332836628 | 0.0 | 0.0 | +— / -3a17cc98-2024-4ac0-b627-9a751d138cd9 |
| Jogador 8 | 6-3 | 360 | BUY | ALL_IN | 6.0 | 8 | 156 | 5 | 38.0 | Enfeitiçador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26673316955566406 | 0.0 | 0.0 | +e29db20a-6b71-4518-ac7d-1e5d9eb67582 / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 197 | 193 | 95 | 12 | 9 | 0 | 2 | 0 | 74 | 38.0 |
- Jogador 1 — gasto por ação: BUY: 145g, BUY_XP: 44g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 45g, stage 3: 66g, stage 4: 66g, stage 5: 10g
| Jogador 2 | 253 | 286 | 187 | 8 | 12 | 0 | 1 | 0 | 97 | 36.0 |
- Jogador 2 — gasto por ação: BUY: 228g, BUY_XP: 56g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 58g, stage 3: 99g, stage 4: 48g, stage 5: 74g
| Jogador 3 | 182 | 144 | 77 | 3 | 5 | 0 | 0 | 0 | 110 | 40.0 |
- Jogador 3 — gasto por ação: BUY: 120g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 46g, stage 3: 36g, stage 4: 47g, stage 5: 8g
| Jogador 4 | 173 | 161 | 82 | 8 | 6 | 1 | 2 | 0 | 59 | 30.0 |
- Jogador 4 — gasto por ação: BUY: 125g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 69g, stage 3: 35g, stage 4: 51g
| Jogador 5 | 231 | 265 | 148 | 7 | 15 | 0 | 1 | 0 | 79 | 40.0 |
- Jogador 5 — gasto por ação: BUY: 191g, BUY_XP: 72g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 65g, stage 3: 82g, stage 4: 50g, stage 5: 61g
| Jogador 6 | 210 | 222 | 100 | 8 | 17 | 0 | 0 | 0 | 44 | 52.0 |
- Jogador 6 — gasto por ação: BUY: 154g, BUY_XP: 68g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 65g, stage 3: 58g, stage 4: 59g, stage 5: 35g
| Jogador 7 | 239 | 240 | 88 | 8 | 22 | 2 | 0 | 0 | 86 | 42.0 |
- Jogador 7 — gasto por ação: BUY: 136g, BUY_XP: 104g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 50g, stage 3: 62g, stage 4: 75g, stage 5: 32g, stage 6: 15g
| Jogador 8 | 272 | 327 | 189 | 25 | 19 | 1 | 0 | 0 | 155 | 38.0 |
- Jogador 8 — gasto por ação: BUY: 239g, BUY_XP: 88g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 58g, stage 3: 90g, stage 4: 86g, stage 5: 60g, stage 6: 26g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 11 | 8 |
- Jogador 1 · 2-7 · step 115: PASS com 6g, HP 95, nível 6/8 (STABILIZE).
- Jogador 1 · 3-7 · step 190: PASS com 8g, HP 51, nível 7/8 (FAST8).
- Jogador 1 · 4-1 · step 200: PASS com 11g, HP 51, nível 7/8 (FAST8).
- Jogador 1 · 4-2 · step 209: PASS com 20g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 4-3 · step 218: PASS com 29g, HP 30, nível 7/8 (STABILIZE).
- Jogador 1 · 4-6 · step 245: REROLL com 50g, HP 20, nível 7/8 (ALL_IN).
- Jogador 1 · 4-6 · step 249: REROLL com 50g, HP 20, nível 7/8 (ALL_IN).
- Jogador 1 · 5-2 · step 277: PASS com 74g, HP 7, nível 7/8 (ALL_IN).
| Jogador 2 | 14 | 2 |
- Jogador 2 · 4-5 · step 240: PASS com 14g, HP 7, nível 7/8 (ALL_IN).
- Jogador 2 · 5-5 · step 310: REROLL com 82g, HP 7, nível 7/8 (ALL_IN).
| Jogador 3 | 6 | 11 |
- Jogador 3 · 3-2 · step 137: PASS com 4g, HP 89, nível 6/8 (FAST8).
- Jogador 3 · 3-3 · step 146: PASS com 5g, HP 89, nível 6/8 (FAST8).
- Jogador 3 · 3-4 · step 157: PASS com 10g, HP 78, nível 6/8 (FAST8).
- Jogador 3 · 3-5 · step 168: PASS com 13g, HP 78, nível 6/8 (FAST8).
- Jogador 3 · 3-6 · step 177: PASS com 14g, HP 78, nível 6/8 (FAST8).
- Jogador 3 · 3-7 · step 188: PASS com 27g, HP 67, nível 6/8 (FAST8).
- Jogador 3 · 4-3 · step 220: PASS com 52g, HP 53, nível 6/8 (FAST8).
- Jogador 3 · 4-4 · step 228: PASS com 63g, HP 40, nível 6/8 (FAST8).
- Jogador 3 · 4-5 · step 237: PASS com 70g, HP 40, nível 6/8 (FAST8).
- Jogador 3 · 4-6 · step 250: PASS com 86g, HP 40, nível 6/8 (FAST8).
- Jogador 3 · 5-2 · step 277: PASS com 110g, HP 11, nível 7/8 (ALL_IN).
| Jogador 4 | 8 | 5 |
- Jogador 4 · 3-5 · step 166: PASS com 12g, HP 49, nível 6/8 (STABILIZE).
- Jogador 4 · 3-7 · step 189: PASS com 26g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-2 · step 204: REROLL com 39g, HP 25, nível 6/8 (ALL_IN).
- Jogador 4 · 4-2 · step 210: REROLL com 39g, HP 25, nível 6/8 (ALL_IN).
- Jogador 4 · 4-4 · step 230: PASS com 52g, HP 1, nível 7/8 (ALL_IN).
| Jogador 5 | 18 | 6 |
- Jogador 5 · 4-4 · step 227: PASS com 5g, HP 72, nível 7/8 (FAST8).
- Jogador 5 · 4-5 · step 240: PASS com 15g, HP 72, nível 7/8 (FAST8).
- Jogador 5 · 4-6 · step 248: PASS com 14g, HP 61, nível 7/8 (FAST8).
- Jogador 5 · 4-7 · step 258: PASS com 25g, HP 48, nível 7/8 (FAST8).
- Jogador 5 · 5-3 · step 288: PASS com 47g, HP 33, nível 7/8 (STABILIZE).
- Jogador 5 · 5-4 · step 299: PASS com 56g, HP 17, nível 7/8 (ALL_IN).
| Jogador 6 | 17 | 5 |
- Jogador 6 · 4-5 · step 236: PASS com 8g, HP 43, nível 7/8 (FAST8).
- Jogador 6 · 4-6 · step 246: PASS com 14g, HP 30, nível 7/8 (STABILIZE).
- Jogador 6 · 4-7 · step 259: PASS com 13g, HP 30, nível 7/8 (STABILIZE).
- Jogador 6 · 5-2 · step 274: PASS com 20g, HP 30, nível 7/8 (STABILIZE).
- Jogador 6 · 5-5 · step 309: PASS com 44g, HP 14, nível 7/8 (ALL_IN).
| Jogador 7 | 26 | 1 |
- Jogador 7 · 4-6 · step 249: PASS com 4g, HP 63, nível 7/8 (FAST8).
| Jogador 8 | 22 | 1 |
- Jogador 8 · 3-6 · step 179: PASS com 24g, HP 84, nível 7/8 (FAST8).

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
| Jogador 1 | 197 | 54 | 38 | 105 | 0.0003 | 0.0899 | -0.0004 | 0.2873 | 0.0007 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0248 (63 ações), BUY_XP: Δ 0.0089 (11 ações), CRAFT_AND_EQUIP: Δ 0.0063 (7 ações), MOVE_BENCH: Δ -0.0145 (17 ações), MOVE_BOARD: Δ 0.0281 (48 ações), PASS: Δ 0.0000 (19 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0123 (30 ações)
| Jogador 2 | 253 | 34 | 24 | 195 | 0.0019 | 0.4763 | 0.0003 | 0.3806 | 0.0016 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0011 (101 ações), BUY_XP: Δ 0.0077 (14 ações), CRAFT_AND_EQUIP: Δ 0.0010 (7 ações), MOVE_BENCH: Δ 0.0151 (16 ações), MOVE_BOARD: Δ -0.0026 (31 ações), PASS: Δ 0.0000 (10 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0043 (73 ações)
| Jogador 3 | 182 | 33 | 39 | 110 | 0.0017 | 0.2469 | 0.0008 | 0.2968 | 0.0009 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0178 (58 ações), BUY_XP: Δ 0.0081 (6 ações), CRAFT_AND_EQUIP: Δ 0.0106 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0336 (16 ações), MOVE_BOARD: Δ 0.0044 (47 ações), PASS: Δ 0.0000 (22 ações), SELL: Δ 0.0193 (25 ações)
| Jogador 4 | 173 | 42 | 31 | 100 | 0.0032 | -0.0677 | 0.0022 | 0.3972 | 0.0010 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0299 (61 ações), BUY_XP: Δ 0.0135 (8 ações), CRAFT_AND_EQUIP: Δ 0.0028 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.1734 (6 ações), MOVE_BENCH: Δ -0.0004 (23 ações), MOVE_BOARD: Δ 0.0268 (28 ações), PASS: Δ 0.0000 (12 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0171 (28 ações)
| Jogador 5 | 231 | 39 | 33 | 159 | 0.0012 | 0.1978 | -0.0002 | 0.3741 | 0.0014 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0144 (85 ações), BUY_XP: Δ 0.0078 (18 ações), CRAFT_AND_EQUIP: Δ 0.0187 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0227 (17 ações), MOVE_BOARD: Δ 0.0076 (31 ações), PASS: Δ 0.0000 (15 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0109 (55 ações)
| Jogador 6 | 210 | 41 | 33 | 136 | 0.0030 | -0.5512 | 0.0016 | 0.3868 | 0.0014 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0005 (67 ações), BUY_XP: Δ 0.0000 (17 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (7 ações), MOVE_BENCH: Δ 0.1280 (12 ações), MOVE_BOARD: Δ -0.0353 (40 ações), PASS: Δ 0.0000 (20 ações), SELL: Δ 0.0135 (40 ações)
| Jogador 7 | 239 | 56 | 41 | 142 | 0.0068 | 0.1204 | 0.0055 | 0.3498 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0167 (58 ações), BUY_XP: Δ 0.0072 (26 ações), CRAFT_AND_EQUIP: Δ 0.0086 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0182 (10 ações), MOVE_BENCH: Δ 0.0028 (17 ações), MOVE_BOARD: Δ 0.0160 (68 ações), PASS: Δ 0.0000 (25 ações), SELL: Δ 0.0365 (28 ações)
| Jogador 8 | 272 | 42 | 34 | 196 | 0.0042 | 0.2008 | 0.0022 | 0.3215 | 0.0020 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0036 (104 ações), BUY_XP: Δ 0.0266 (22 ações), CRAFT_AND_EQUIP: Δ 0.0030 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0547 (15 ações), MOVE_BOARD: Δ 0.0016 (36 ações), PASS: Δ 0.0000 (16 ações), SELL: Δ 0.0005 (71 ações)
- Jogador 1 — rounds avaliados: 27; correlação estrutural/combate: -0.115; posicional/combate: -0.281.
- Jogador 1 — combate positive: score estrutural prévio 0.047
  score posicional prévio 0.268
- Jogador 1 — combate negative: score estrutural prévio 0.156
  score posicional prévio 0.327
- Jogador 2 — rounds avaliados: 31; correlação estrutural/combate: -0.324; posicional/combate: -0.058.
- Jogador 2 — combate positive: score estrutural prévio 0.368
  score posicional prévio 0.379
- Jogador 2 — combate negative: score estrutural prévio 0.708
  score posicional prévio 0.387
- Jogador 3 — rounds avaliados: 27; correlação estrutural/combate: 0.072; posicional/combate: -0.001.
- Jogador 3 — combate positive: score estrutural prévio 0.262
  score posicional prévio 0.306
- Jogador 3 — combate negative: score estrutural prévio 0.242
  score posicional prévio 0.304
- Jogador 4 — rounds avaliados: 23; correlação estrutural/combate: 0.313; posicional/combate: -0.120.
- Jogador 4 — combate positive: score estrutural prévio 0.134
  score posicional prévio 0.406
- Jogador 4 — combate negative: score estrutural prévio -0.119
  score posicional prévio 0.398
- Jogador 5 — rounds avaliados: 31; correlação estrutural/combate: -0.274; posicional/combate: -0.028.
- Jogador 5 — combate positive: score estrutural prévio 0.102
  score posicional prévio 0.376
- Jogador 5 — combate negative: score estrutural prévio 0.353
  score posicional prévio 0.385
- Jogador 6 — rounds avaliados: 30; correlação estrutural/combate: 0.116; posicional/combate: -0.356.
- Jogador 6 — combate positive: score estrutural prévio -0.396
  score posicional prévio 0.295
- Jogador 6 — combate negative: score estrutural prévio -0.591
  score posicional prévio 0.442
- Jogador 7 — rounds avaliados: 35; correlação estrutural/combate: -0.003; posicional/combate: -0.304.
- Jogador 7 — combate positive: score estrutural prévio 0.157
  score posicional prévio 0.336
- Jogador 7 — combate negative: score estrutural prévio 0.202
  score posicional prévio 0.464
- Jogador 8 — rounds avaliados: 35; correlação estrutural/combate: 0.136; posicional/combate: -0.271.
- Jogador 8 — combate positive: score estrutural prévio 0.310
  score posicional prévio 0.311
- Jogador 8 — combate negative: score estrutural prévio 0.153
  score posicional prévio 0.348

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 223 | OK (223) | 7 | 0 | 0 | 0 | 7 | 0 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Crownguard, TFT_Item_HextechGunblade, TFT_Item_InfinityEdge, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon, TFT_Item_SpectralGauntlet; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 283 | OK (283) | 7 | 0 | 0 | 0 | 7 | 0 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 208 | OK (208) | 7 | 0 | 0 | 0 | 7 | 1 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_Redemption, TFT_Item_SteraksGage, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 195 | OK (195) | 5 | 0 | 0 | 1 | 5 | 3 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 261 | OK (261) | 7 | 0 | 0 | 0 | 7 | 2 |
- Jogador 5 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_GuinsoosRageblade, TFT_Item_IonicSpark, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 239 | OK (239) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 6 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 274 | OK (274) | 8 | 0 | 0 | 0 | 8 | 3 |
- Jogador 7 — IDs equipados observados: TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_RunaansHurricane, TFT_Item_StatikkShiv; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 306 | OK (306) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 8 — IDs equipados observados: DA_18_EmblemHunter, TFT_Item_AdaptiveHelm, TFT_Item_DragonsClaw, TFT_Item_HextechGunblade, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.110 | 0.000 |
| Jogador 1 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.001 | 0.000 |
| Jogador 1 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 1 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.012 | 0.000 |
| Jogador 1 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 6 | 5 | 4 → 4 | -0.014 | 0.427 |
| Jogador 1 | 2-2 | 10 | 2.000 | 0.000 | 0 → 0 | 3 → 3 | 14% → 18% | 6 → 8 | 9 | 4 → 5 | -0.027 | 0.259 |
| Jogador 1 | 2-3 | 8 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 18% → 18% | 8 → 5 | 11 | 5 → 5 | 0.000 | -0.296 |
| Jogador 1 | 2-4 | 7 | 2.000 | 4.000 | 0 → 0 | 3 → 2 | 18% → 18% | 5 → 6 | 4 | 5 → 5 | -0.002 | 0.000 |
| Jogador 1 | 2-5 | 10 | 0.000 | 4.000 | 0 → 0 | 2 → 3 | 18% → 18% | 6 → 7 | 8 | 5 → 6 | 0.073 | 0.256 |
| Jogador 1 | 2-6 | 9 | 6.000 | 6.000 | 0 → 1 | 3 → 2 | 18% → 21% | 7 → 7 | 7 | 6 → 6 | 0.007 | 0.324 |
| Jogador 1 | 2-7 | 5 | 2.000 | -2.000 | 1 → 2 | 2 → 1 | 21% → 18% | 7 → 12 | 1 | 6 → 6 | -0.086 | 0.000 |
| Jogador 1 | 3-1 | 10 | 4.000 | -4.000 | 2 → 2 | 1 → 1 | 18% → 21% | 12 → 7 | 12 | 6 → 6 | -0.006 | 0.281 |
| Jogador 1 | 3-2 | 7 | 0.000 | 14.000 | 2 → 2 | 1 → 1 | 21% → 21% | 7 → 5 | 7 | 6 → 6 | 0.104 | -0.402 |
| Jogador 1 | 3-3 | 6 | 4.000 | 6.000 | 2 → 2 | 1 → 1 | 21% → 21% | 5 → 6 | 5 | 6 → 6 | 0.023 | -0.471 |
| Jogador 1 | 3-4 | 10 | 0.000 | 4.000 | 2 → 2 | 1 → 1 | 21% → 21% | 6 → 6 | 9 | 6 → 6 | -0.012 | 0.000 |
| Jogador 1 | 3-5 | 10 | -4.000 | -12.000 | 2 → 2 | 1 → 1 | 21% → 18% | 6 → 20 | 7 | 6 → 6 | -0.029 | -0.264 |
| Jogador 1 | 3-6 | 10 | 2.000 | 8.000 | 2 → 2 | 1 → 3 | 18% → 21% | 20 → 13 | 17 | 6 → 7 | -0.034 | -0.291 |
| Jogador 1 | 3-7 | 10 | 6.000 | 4.000 | 2 → 2 | 3 → 5 | 21% → 25% | 13 → 14 | 9 | 7 → 7 | -0.072 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | 6.000 | 2 → 2 | 5 → 5 | 25% → 25% | 14 → 19 | 3 | 7 → 7 | 0.062 | -0.258 |
| Jogador 1 | 4-2 | 9 | 0.000 | -2.000 | 2 → 2 | 5 → 5 | 25% → 25% | 19 → 30 | 4 | 7 → 7 | 0.017 | -0.292 |
| Jogador 1 | 4-3 | 8 | 0.000 | 2.000 | 2 → 2 | 5 → 5 | 25% → 25% | 30 → 38 | 7 | 7 → 7 | -0.123 | 0.376 |
| Jogador 1 | 4-4 | 10 | 0.000 | -2.000 | 2 → 2 | 5 → 4 | 25% → 25% | 38 → 46 | 11 | 7 → 7 | -0.001 | 0.000 |
| Jogador 1 | 4-5 | 10 | 0.000 | 6.000 | 2 → 2 | 4 → 4 | 25% → 25% | 46 → 52 | 11 | 7 → 7 | 0.052 | -0.258 |
| Jogador 1 | 4-6 | 10 | -6.000 | 4.000 | 2 → 2 | 4 → 3 | 25% → 21% | 52 → 55 | 19 | 7 → 7 | -0.014 | -0.290 |
| Jogador 1 | 4-7 | 10 | 4.000 | -2.000 | 2 → 2 | 3 → 3 | 21% → 21% | 55 → 66 | 11 | 7 → 7 | 0.094 | 0.000 |
| Jogador 1 | 5-1 | 10 | 8.000 | -10.000 | 2 → 3 | 3 → 3 | 21% → 25% | 66 → 77 | 7 | 7 → 7 | -0.005 | 0.000 |
| Jogador 1 | 5-2 | 7 | -38.000 | -42.000 | 3 → 0 | 3 → 0 | 25% → 0% | 77 → 74 | 3 | 7 → 7 | -0.118 | -0.429 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 21, COMPOSITION_COMPATIBILITY: 20, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 59 ações e piorou em 41.
- Jogador 1 — estado final: ouro 74, nível 7, vida 7.0, colocação 7.
| Jogador 2 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.161 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.109 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 3 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 10 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 11% → 14% | 4 → 5 | 5 | 4 → 4 | 0.026 | -0.226 |
| Jogador 2 | 2-2 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 1 | 14% → 14% | 5 → 6 | 8 | 4 → 4 | 0.033 | -0.243 |
| Jogador 2 | 2-3 | 10 | 6.000 | -2.000 | 1 → 1 | 1 → 1 | 14% → 18% | 6 → 6 | 10 | 4 → 5 | 0.009 | 0.251 |
| Jogador 2 | 2-4 | 6 | 0.000 | 12.000 | 1 → 1 | 1 → 1 | 18% → 18% | 6 → 5 | 6 | 5 → 5 | 0.003 | 0.000 |
| Jogador 2 | 2-5 | 10 | 4.000 | 2.000 | 1 → 1 | 1 → 1 | 18% → 18% | 5 → 7 | 5 | 5 → 5 | 0.003 | -0.248 |
| Jogador 2 | 2-6 | 10 | 0.000 | -4.000 | 1 → 1 | 1 → 2 | 18% → 18% | 7 → 7 | 14 | 5 → 5 | 0.001 | -0.254 |
| Jogador 2 | 2-7 | 10 | 2.000 | 4.000 | 1 → 1 | 2 → 3 | 18% → 21% | 7 → 6 | 10 | 5 → 6 | 0.012 | 0.000 |
| Jogador 2 | 3-1 | 10 | 0.000 | 4.000 | 1 → 1 | 3 → 2 | 21% → 21% | 6 → 6 | 12 | 6 → 6 | 0.000 | -0.278 |
| Jogador 2 | 3-2 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 9 | 9 | 6 → 6 | 0.000 | -0.273 |
| Jogador 2 | 3-3 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 3 | 21% → 21% | 9 → 8 | 18 | 6 → 6 | 0.000 | 0.303 |
| Jogador 2 | 3-4 | 10 | 0.000 | -6.000 | 1 → 1 | 3 → 3 | 21% → 21% | 8 → 8 | 14 | 6 → 7 | 0.005 | 0.000 |
| Jogador 2 | 3-5 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 2 | 21% → 21% | 8 → 7 | 15 | 7 → 7 | 0.000 | -0.273 |
| Jogador 2 | 3-6 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 3 | 21% → 21% | 7 → 11 | 13 | 7 → 7 | 0.000 | -0.281 |
| Jogador 2 | 3-7 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 2 | 21% → 21% | 11 → 11 | 18 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 10 | 6.000 | 14.000 | 1 → 1 | 2 → 2 | 21% → 25% | 11 → 7 | 10 | 7 → 7 | -0.037 | 0.299 |
| Jogador 2 | 4-2 | 9 | 4.000 | 6.000 | 1 → 2 | 2 → 1 | 25% → 25% | 7 → 6 | 6 | 7 → 7 | 0.059 | -0.302 |
| Jogador 2 | 4-3 | 6 | 0.000 | 12.000 | 2 → 2 | 1 → 2 | 25% → 25% | 6 → 6 | 6 | 7 → 7 | -0.030 | -0.467 |
| Jogador 2 | 4-4 | 10 | 0.000 | -2.000 | 2 → 2 | 2 → 3 | 25% → 25% | 6 → 13 | 7 | 7 → 7 | 0.024 | 0.000 |
| Jogador 2 | 4-5 | 10 | 0.000 | -2.000 | 2 → 2 | 3 → 5 | 25% → 25% | 13 → 21 | 8 | 7 → 7 | -0.094 | 0.276 |
| Jogador 2 | 4-6 | 10 | 0.000 | -8.000 | 2 → 2 | 5 → 4 | 25% → 25% | 21 → 34 | 5 | 7 → 7 | 0.002 | 0.306 |
| Jogador 2 | 4-7 | 10 | 0.000 | -2.000 | 2 → 2 | 4 → 4 | 25% → 25% | 34 → 44 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 10 | 0.000 | 8.000 | 2 → 2 | 4 → 4 | 25% → 25% | 44 → 51 | 13 | 7 → 7 | 0.000 | 0.301 |
| Jogador 2 | 5-2 | 10 | 0.000 | -2.000 | 2 → 2 | 4 → 4 | 25% → 25% | 51 → 64 | 12 | 7 → 7 | 0.000 | 0.307 |
| Jogador 2 | 5-3 | 10 | 4.000 | 6.000 | 2 → 2 | 4 → 1 | 25% → 25% | 64 → 62 | 13 | 7 → 7 | -0.051 | 0.000 |
| Jogador 2 | 5-4 | 10 | 0.000 | 0.000 | 2 → 2 | 1 → 2 | 25% → 25% | 62 → 76 | 10 | 7 → 7 | 0.039 | 0.000 |
| Jogador 2 | 5-5 | 10 | 0.000 | -8.000 | 2 → 2 | 2 → 2 | 25% → 25% | 76 → 93 | 13 | 7 → 7 | 0.006 | 0.296 |
| Jogador 2 | 5-6 | 10 | -36.000 | -44.000 | 2 → 0 | 2 → 0 | 25% → 0% | 93 → 97 | 13 | 7 → 7 | -0.052 | -0.278 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 48, COMPOSITION_COMPATIBILITY: 31, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 15; mudanças de composição: 0; posicionamento melhorou em 37 ações e piorou em 26.
- Jogador 2 — estado final: ouro 97, nível 7, vida 7.0, colocação 4.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.060 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 3 | 1-4 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.002 | 0.000 |
| Jogador 3 | 2-1 | 10 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.003 | 0.261 |
| Jogador 3 | 2-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.684 |
| Jogador 3 | 2-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 6 | 7 | 4 → 5 | 0.006 | -0.484 |
| Jogador 3 | 2-4 | 4 | 4.000 | -2.000 | 1 → 1 | 1 → 2 | 14% → 18% | 6 → 6 | 5 | 5 → 5 | 0.026 | 0.000 |
| Jogador 3 | 2-5 | 10 | 0.000 | -8.000 | 1 → 1 | 2 → 3 | 18% → 18% | 6 → 8 | 12 | 5 → 5 | -0.007 | -0.248 |
| Jogador 3 | 2-6 | 10 | 12.000 | -12.000 | 1 → 3 | 3 → 1 | 18% → 21% | 8 → 7 | 7 | 5 → 6 | 0.015 | 0.270 |
| Jogador 3 | 2-7 | 7 | 0.000 | 12.000 | 3 → 3 | 1 → 2 | 21% → 21% | 7 → 6 | 6 | 6 → 6 | -0.002 | 0.000 |
| Jogador 3 | 3-1 | 9 | 0.000 | 10.000 | 3 → 3 | 2 → 2 | 21% → 21% | 6 → 8 | 5 | 6 → 6 | 0.008 | 0.307 |
| Jogador 3 | 3-2 | 7 | 2.000 | 4.000 | 3 → 3 | 2 → 1 | 21% → 21% | 8 → 11 | 4 | 6 → 6 | -0.006 | 0.426 |
| Jogador 3 | 3-3 | 6 | 0.000 | 12.000 | 3 → 3 | 1 → 2 | 21% → 21% | 11 → 10 | 6 | 6 → 6 | -0.001 | -0.463 |
| Jogador 3 | 3-4 | 7 | 0.000 | 2.000 | 3 → 3 | 2 → 3 | 21% → 21% | 10 → 16 | 3 | 6 → 6 | 0.007 | 0.000 |
| Jogador 3 | 3-5 | 8 | 0.000 | 0.000 | 3 → 3 | 3 → 2 | 21% → 21% | 16 → 20 | 6 | 6 → 6 | -0.020 | 0.356 |
| Jogador 3 | 3-6 | 7 | 0.000 | 8.000 | 3 → 3 | 2 → 1 | 21% → 21% | 20 → 20 | 6 | 6 → 6 | -0.008 | -0.396 |
| Jogador 3 | 3-7 | 8 | 2.000 | -10.000 | 3 → 2 | 1 → 2 | 21% → 21% | 20 → 34 | 6 | 6 → 6 | 0.004 | 0.000 |
| Jogador 3 | 4-1 | 10 | 2.000 | 4.000 | 2 → 2 | 2 → 4 | 21% → 21% | 34 → 41 | 6 | 6 → 6 | 0.009 | -0.283 |
| Jogador 3 | 4-2 | 10 | 0.000 | -4.000 | 2 → 2 | 4 → 5 | 21% → 21% | 41 → 53 | 5 | 6 → 6 | 0.018 | 0.285 |
| Jogador 3 | 4-3 | 10 | 0.000 | 2.000 | 2 → 2 | 5 → 5 | 21% → 21% | 53 → 62 | 7 | 6 → 6 | -0.016 | -0.275 |
| Jogador 3 | 4-4 | 8 | 0.000 | -2.000 | 2 → 2 | 5 → 5 | 21% → 21% | 62 → 73 | 5 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 7 | 0.000 | 0.000 | 2 → 2 | 5 → 4 | 21% → 21% | 73 → 81 | 5 | 6 → 6 | -0.009 | 0.419 |
| Jogador 3 | 4-6 | 10 | 0.000 | -6.000 | 2 → 2 | 4 → 4 | 21% → 21% | 81 → 96 | 5 | 6 → 6 | 0.006 | -0.280 |
| Jogador 3 | 4-7 | 10 | -4.000 | 4.000 | 2 → 2 | 4 → 2 | 21% → 18% | 96 → 98 | 14 | 6 → 7 | 0.008 | 0.000 |
| Jogador 3 | 5-1 | 10 | 10.000 | -14.000 | 2 → 2 | 2 → 3 | 18% → 25% | 98 → 113 | 4 | 7 → 7 | -0.013 | -0.275 |
| Jogador 3 | 5-2 | 7 | -40.000 | -26.000 | 2 → 0 | 3 → 0 | 25% → 0% | 113 → 110 | 4 | 7 → 7 | -0.079 | -0.414 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 26, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 14; mudanças de composição: 0; posicionamento melhorou em 39 ações e piorou em 41.
- Jogador 3 — estado final: ouro 110, nível 7, vida 11.0, colocação 6.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 4 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.065 | 0.000 |
| Jogador 4 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 4 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.013 | 0.000 |
| Jogador 4 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 5 | 5 | 4 → 4 | -0.021 | -0.404 |
| Jogador 4 | 2-2 | 4 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 14% → 18% | 5 → 6 | 5 | 4 → 5 | 0.034 | 0.684 |
| Jogador 4 | 2-3 | 10 | 4.000 | -4.000 | 0 → 0 | 3 → 2 | 18% → 18% | 6 → 9 | 9 | 5 → 5 | 0.005 | 0.269 |
| Jogador 4 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 10 | 12 | 5 → 5 | -0.013 | 0.000 |
| Jogador 4 | 2-5 | 10 | 2.000 | 0.000 | 0 → 0 | 3 → 2 | 18% → 21% | 10 → 6 | 14 | 5 → 6 | -0.012 | -0.237 |
| Jogador 4 | 2-6 | 10 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 21% → 21% | 6 → 8 | 12 | 6 → 6 | 0.015 | -0.274 |
| Jogador 4 | 2-7 | 10 | 4.000 | 2.000 | 0 → 0 | 3 → 2 | 21% → 21% | 8 → 7 | 12 | 6 → 6 | 0.019 | 0.000 |
| Jogador 4 | 3-1 | 9 | 0.000 | 10.000 | 0 → 0 | 2 → 3 | 21% → 21% | 7 → 8 | 5 | 6 → 6 | 0.044 | -0.287 |
| Jogador 4 | 3-2 | 10 | 2.000 | 6.000 | 0 → 0 | 3 → 2 | 21% → 21% | 8 → 9 | 5 | 6 → 6 | -0.089 | -0.283 |
| Jogador 4 | 3-3 | 10 | -2.000 | 14.000 | 0 → 0 | 2 → 3 | 21% → 21% | 9 → 10 | 6 | 6 → 6 | -0.091 | -0.286 |
| Jogador 4 | 3-4 | 10 | 4.000 | -4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 10 → 16 | 5 | 6 → 6 | 0.142 | 0.000 |
| Jogador 4 | 3-5 | 6 | 0.000 | 8.000 | 0 → 0 | 3 → 4 | 21% → 21% | 16 → 19 | 4 | 6 → 6 | 0.018 | 0.469 |
| Jogador 4 | 3-6 | 10 | 0.000 | -4.000 | 0 → 0 | 4 → 6 | 21% → 21% | 19 → 29 | 5 | 6 → 6 | -0.044 | -0.268 |
| Jogador 4 | 3-7 | 9 | -2.000 | 2.000 | 0 → 0 | 6 → 5 | 21% → 21% | 29 → 33 | 5 | 6 → 6 | -0.045 | 0.000 |
| Jogador 4 | 4-1 | 10 | 0.000 | -4.000 | 0 → 0 | 5 → 5 | 21% → 21% | 33 → 44 | 6 | 6 → 6 | 0.013 | -0.290 |
| Jogador 4 | 4-2 | 10 | 0.000 | 6.000 | 0 → 0 | 5 → 5 | 21% → 21% | 44 → 46 | 17 | 6 → 6 | 0.006 | -0.268 |
| Jogador 4 | 4-3 | 10 | 4.000 | -10.000 | 0 → 0 | 5 → 4 | 21% → 21% | 46 → 59 | 8 | 6 → 7 | 0.055 | -0.285 |
| Jogador 4 | 4-4 | 10 | 2.000 | 12.000 | 0 → 0 | 4 → 5 | 21% → 25% | 59 → 63 | 10 | 7 → 7 | 0.027 | 0.000 |
| Jogador 4 | 4-5 | 10 | -28.000 | -44.000 | 0 → 0 | 5 → 0 | 25% → 0% | 63 → 59 | 10 | 7 → 7 | -0.090 | -0.276 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 16, COMPOSITION_COMPATIBILITY: 19, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 17; mudanças de composição: 0; posicionamento melhorou em 46 ações e piorou em 33.
- Jogador 4 — estado final: ouro 59, nível 7, vida 1.0, colocação 8.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.112 | 0.000 |
| Jogador 5 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.003 | 0.000 |
| Jogador 5 | 2-1 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.000 | 0.340 |
| Jogador 5 | 2-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.641 |
| Jogador 5 | 2-3 | 10 | 6.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 7 | 11 | 4 → 5 | -0.007 | 0.256 |
| Jogador 5 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 8 | 12 | 5 → 5 | 0.006 | 0.000 |
| Jogador 5 | 2-5 | 10 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 8 → 7 | 12 | 5 → 6 | -0.010 | 0.264 |
| Jogador 5 | 2-6 | 10 | 0.000 | -6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 11 | 9 | 6 → 6 | 0.019 | -0.253 |
| Jogador 5 | 2-7 | 10 | 2.000 | 8.000 | 0 → 0 | 1 → 1 | 21% → 21% | 11 → 7 | 12 | 6 → 6 | 0.001 | 0.000 |
| Jogador 5 | 3-1 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 0 | 21% → 21% | 7 → 6 | 12 | 6 → 6 | 0.031 | -0.263 |
| Jogador 5 | 3-2 | 10 | 0.000 | -4.000 | 0 → 0 | 0 → 0 | 21% → 21% | 6 → 10 | 10 | 6 → 6 | 0.000 | 0.300 |
| Jogador 5 | 3-3 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 25% | 10 → 7 | 16 | 6 → 7 | -0.008 | 0.295 |
| Jogador 5 | 3-4 | 7 | 0.000 | 14.000 | 0 → 0 | 0 → 0 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | -0.002 | 0.000 |
| Jogador 5 | 3-5 | 7 | 0.000 | 12.000 | 0 → 0 | 0 → 1 | 25% → 25% | 6 → 7 | 6 | 7 → 7 | -0.069 | 0.388 |
| Jogador 5 | 3-6 | 10 | 0.000 | -12.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 12 | 14 | 7 → 7 | 0.000 | 0.308 |
| Jogador 5 | 3-7 | 10 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 12 → 7 | 17 | 7 → 7 | 0.060 | 0.000 |
| Jogador 5 | 4-1 | 10 | 2.000 | 4.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 5 | 12 | 7 → 7 | 0.010 | -0.271 |
| Jogador 5 | 4-2 | 10 | -4.000 | 6.000 | 0 → 0 | 1 → 2 | 25% → 25% | 5 → 6 | 12 | 7 → 7 | 0.032 | 0.288 |
| Jogador 5 | 4-3 | 8 | 4.000 | 6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 6 → 7 | 6 | 7 → 7 | -0.005 | 0.364 |
| Jogador 5 | 4-4 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 4 | 25% → 25% | 7 → 11 | 5 | 7 → 7 | -0.120 | 0.000 |
| Jogador 5 | 4-5 | 10 | 0.000 | -8.000 | 0 → 0 | 4 → 5 | 25% → 25% | 11 → 21 | 2 | 7 → 7 | 0.067 | -0.268 |
| Jogador 5 | 4-6 | 8 | 0.000 | 8.000 | 0 → 0 | 5 → 4 | 25% → 25% | 21 → 21 | 8 | 7 → 7 | -0.035 | -0.344 |
| Jogador 5 | 4-7 | 8 | 0.000 | -4.000 | 0 → 0 | 4 → 4 | 25% → 25% | 21 → 33 | 5 | 7 → 7 | 0.051 | 0.000 |
| Jogador 5 | 5-1 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 5 | 25% → 25% | 33 → 43 | 10 | 7 → 7 | 0.030 | -0.285 |
| Jogador 5 | 5-2 | 10 | 6.000 | -12.000 | 0 → 1 | 5 → 2 | 25% → 21% | 43 → 50 | 10 | 7 → 7 | -0.018 | 0.000 |
| Jogador 5 | 5-3 | 8 | 6.000 | 2.000 | 1 → 1 | 2 → 3 | 21% → 25% | 50 → 57 | 8 | 7 → 7 | -0.001 | -0.350 |
| Jogador 5 | 5-4 | 9 | 0.000 | 4.000 | 1 → 1 | 3 → 5 | 25% → 25% | 57 → 67 | 4 | 7 → 8 | -0.101 | 0.000 |
| Jogador 5 | 5-5 | 10 | 0.000 | 4.000 | 1 → 1 | 5 → 5 | 25% → 25% | 67 → 75 | 18 | 8 → 8 | 0.000 | -0.280 |
| Jogador 5 | 5-6 | 10 | -40.000 | -44.000 | 1 → 0 | 5 → 0 | 25% → 0% | 75 → 79 | 11 | 8 → 8 | -0.025 | -0.285 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 33, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 19; mudanças de composição: 0; posicionamento melhorou em 42 ações e piorou em 35.
- Jogador 5 — estado final: ouro 79, nível 8, vida 1.0, colocação 3.
| Jogador 6 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.163 | 0.000 |
| Jogador 6 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.039 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.021 | -0.412 |
| Jogador 6 | 2-2 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | -0.010 | -0.430 |
| Jogador 6 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 9 | 5 | 4 → 5 | -0.005 | -0.369 |
| Jogador 6 | 2-4 | 10 | 6.000 | -8.000 | 0 → 0 | 2 → 3 | 14% → 18% | 9 → 8 | 13 | 5 → 5 | -0.002 | 0.000 |
| Jogador 6 | 2-5 | 10 | 0.000 | -8.000 | 0 → 0 | 3 → 3 | 18% → 18% | 8 → 10 | 12 | 5 → 6 | 0.015 | -0.242 |
| Jogador 6 | 2-6 | 8 | 2.000 | 2.000 | 0 → 0 | 3 → 3 | 18% → 21% | 10 → 7 | 11 | 6 → 6 | 0.009 | -0.296 |
| Jogador 6 | 2-7 | 10 | 0.000 | -4.000 | 0 → 0 | 3 → 2 | 21% → 21% | 7 → 8 | 12 | 6 → 6 | 0.002 | 0.000 |
| Jogador 6 | 3-1 | 10 | 6.000 | -4.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 9 | 13 | 6 → 6 | 0.058 | 0.295 |
| Jogador 6 | 3-2 | 10 | -2.000 | -2.000 | 0 → 0 | 2 → 1 | 21% → 18% | 9 → 8 | 10 | 6 → 7 | 0.017 | -0.259 |
| Jogador 6 | 3-3 | 10 | 12.000 | 4.000 | 0 → 0 | 1 → 2 | 18% → 25% | 8 → 6 | 8 | 7 → 7 | -0.007 | 0.300 |
| Jogador 6 | 3-4 | 8 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | 0.064 | 0.000 |
| Jogador 6 | 3-5 | 6 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 25% → 25% | 5 → 5 | 5 | 7 → 7 | -0.026 | -0.423 |
| Jogador 6 | 3-6 | 8 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 25% → 25% | 5 → 7 | 6 | 7 → 7 | -0.118 | 0.369 |
| Jogador 6 | 3-7 | 10 | 0.000 | 4.000 | 0 → 0 | 2 → 3 | 25% → 25% | 7 → 10 | 10 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 10 | 0.000 | 10.000 | 0 → 0 | 3 → 3 | 25% → 25% | 10 → 8 | 13 | 7 → 7 | 0.000 | 0.276 |
| Jogador 6 | 4-2 | 10 | 2.000 | 6.000 | 0 → 0 | 3 → 4 | 25% → 25% | 8 → 5 | 13 | 7 → 7 | 0.028 | -0.276 |
| Jogador 6 | 4-3 | 9 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 5 → 7 | 10 | 7 → 7 | 0.000 | 0.329 |
| Jogador 6 | 4-4 | 9 | 0.000 | -2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 7 → 5 | 9 | 7 → 7 | 0.034 | 0.000 |
| Jogador 6 | 4-5 | 6 | 0.000 | -6.000 | 0 → 0 | 4 → 4 | 25% → 25% | 5 → 13 | 1 | 7 → 7 | -0.012 | -0.458 |
| Jogador 6 | 4-6 | 6 | 0.000 | -2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 13 → 21 | 4 | 7 → 7 | -0.028 | 0.494 |
| Jogador 6 | 4-7 | 9 | 0.000 | 4.000 | 0 → 0 | 4 → 2 | 25% → 25% | 21 → 19 | 9 | 7 → 7 | 0.021 | 0.000 |
| Jogador 6 | 5-1 | 10 | 0.000 | 14.000 | 0 → 0 | 2 → 3 | 25% → 25% | 19 → 20 | 7 | 7 → 7 | 0.022 | 0.292 |
| Jogador 6 | 5-2 | 4 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 20 → 29 | 0 | 7 → 7 | -0.074 | 0.730 |
| Jogador 6 | 5-3 | 10 | -2.000 | -20.000 | 0 → 0 | 3 → 1 | 25% → 18% | 29 → 46 | 10 | 7 → 7 | 0.050 | -0.290 |
| Jogador 6 | 5-4 | 10 | 20.000 | 6.000 | 0 → 1 | 1 → 2 | 18% → 25% | 46 → 41 | 13 | 7 → 7 | 0.017 | 0.000 |
| Jogador 6 | 5-5 | 9 | -52.000 | -48.000 | 1 → 0 | 2 → 0 | 25% → 0% | 41 → 44 | 5 | 7 → 7 | -0.075 | -0.311 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 24, COMPOSITION_COMPATIBILITY: 26, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 47 ações e piorou em 37.
- Jogador 6 — estado final: ouro 44, nível 7, vida 14.0, colocação 5.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.043 | 0.000 |
| Jogador 7 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.077 | 0.000 |
| Jogador 7 | 2-1 | 6 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.016 | 0.427 |
| Jogador 7 | 2-2 | 10 | -2.000 | 4.000 | 0 → 0 | 3 → 2 | 14% → 11% | 8 → 8 | 8 | 4 → 4 | 0.015 | -0.258 |
| Jogador 7 | 2-3 | 10 | 10.000 | -6.000 | 0 → 0 | 2 → 2 | 11% → 14% | 8 → 8 | 9 | 4 → 5 | 0.051 | 0.274 |
| Jogador 7 | 2-4 | 4 | 6.000 | 8.000 | 0 → 0 | 2 → 2 | 14% → 18% | 8 → 6 | 7 | 5 → 5 | -0.013 | 0.000 |
| Jogador 7 | 2-5 | 6 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 18% → 18% | 6 → 9 | 4 | 5 → 5 | -0.012 | 0.419 |
| Jogador 7 | 2-6 | 10 | 0.000 | -2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 9 | 12 | 5 → 5 | 0.013 | 0.269 |
| Jogador 7 | 2-7 | 7 | 8.000 | -2.000 | 0 → 0 | 3 → 3 | 18% → 21% | 9 → 8 | 7 | 5 → 6 | 0.028 | 0.000 |
| Jogador 7 | 3-1 | 7 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 8 → 7 | 6 | 6 → 6 | -0.009 | -0.376 |
| Jogador 7 | 3-2 | 4 | 0.000 | 12.000 | 0 → 0 | 3 → 4 | 21% → 21% | 7 → 7 | 6 | 6 → 6 | 0.000 | 0.692 |
| Jogador 7 | 3-3 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 4 | 21% → 21% | 7 → 5 | 14 | 6 → 6 | -0.006 | -0.263 |
| Jogador 7 | 3-4 | 10 | -4.000 | 0.000 | 0 → 0 | 4 → 2 | 21% → 18% | 5 → 5 | 8 | 6 → 6 | 0.040 | 0.000 |
| Jogador 7 | 3-5 | 10 | 0.000 | 4.000 | 0 → 0 | 2 → 2 | 18% → 18% | 5 → 11 | 8 | 6 → 6 | 0.006 | -0.268 |
| Jogador 7 | 3-6 | 10 | 8.000 | -4.000 | 0 → 0 | 2 → 3 | 18% → 25% | 11 → 7 | 14 | 6 → 7 | -0.027 | 0.298 |
| Jogador 7 | 3-7 | 7 | 0.000 | 12.000 | 0 → 0 | 3 → 5 | 25% → 25% | 7 → 6 | 6 | 7 → 7 | -0.022 | 0.000 |
| Jogador 7 | 4-1 | 10 | 0.000 | 2.000 | 0 → 0 | 5 → 5 | 25% → 25% | 6 → 8 | 7 | 7 → 7 | -0.005 | 0.306 |
| Jogador 7 | 4-2 | 10 | 0.000 | -10.000 | 0 → 0 | 5 → 6 | 25% → 25% | 8 → 8 | 16 | 7 → 7 | -0.048 | 0.293 |
| Jogador 7 | 4-3 | 10 | 0.000 | 0.000 | 0 → 0 | 6 → 6 | 25% → 25% | 8 → 7 | 14 | 7 → 7 | -0.036 | 0.293 |
| Jogador 7 | 4-4 | 10 | -2.000 | 8.000 | 0 → 0 | 6 → 5 | 25% → 25% | 7 → 7 | 6 | 7 → 7 | 0.054 | 0.000 |
| Jogador 7 | 4-5 | 9 | 0.000 | 2.000 | 0 → 0 | 5 → 5 | 25% → 25% | 7 → 8 | 15 | 7 → 7 | -0.035 | 0.317 |
| Jogador 7 | 4-6 | 9 | 0.000 | 2.000 | 0 → 0 | 5 → 4 | 25% → 25% | 8 → 11 | 7 | 7 → 7 | -0.008 | 0.000 |
| Jogador 7 | 4-7 | 10 | -2.000 | -10.000 | 0 → 0 | 4 → 3 | 25% → 21% | 11 → 16 | 10 | 7 → 8 | -0.004 | 0.000 |
| Jogador 7 | 5-1 | 10 | 2.000 | 12.000 | 0 → 0 | 3 → 3 | 21% → 25% | 16 → 10 | 15 | 8 → 8 | -0.009 | 0.289 |
| Jogador 7 | 5-2 | 10 | 10.000 | -12.000 | 0 → 0 | 3 → 3 | 25% → 29% | 10 → 9 | 15 | 8 → 8 | 0.007 | 0.317 |
| Jogador 7 | 5-3 | 8 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 29% → 29% | 9 → 16 | 2 | 8 → 8 | 0.056 | 0.384 |
| Jogador 7 | 5-4 | 5 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 29% → 29% | 16 → 25 | 0 | 8 → 8 | 0.009 | 0.000 |
| Jogador 7 | 5-5 | 5 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 29% → 29% | 25 → 35 | 0 | 8 → 8 | 0.162 | 0.000 |
| Jogador 7 | 5-6 | 5 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 29% → 29% | 35 → 47 | 0 | 8 → 8 | -0.009 | 0.587 |
| Jogador 7 | 5-7 | 4 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 29% → 29% | 47 → 59 | 0 | 8 → 8 | -0.004 | 0.000 |
| Jogador 7 | 6-1 | 5 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 29% → 29% | 59 → 73 | 0 | 8 → 8 | -0.129 | 0.611 |
| Jogador 7 | 6-2 | 8 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 29% → 29% | 73 → 87 | 2 | 8 → 8 | 0.057 | 0.373 |
| Jogador 7 | 6-3 | 10 | 0.000 | 2.000 | 0 → 0 | 3 → 4 | 29% → 29% | 87 → 87 | 13 | 8 → 8 | -0.005 | 0.310 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 23, COMPOSITION_COMPATIBILITY: 16, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 12; mudanças de composição: 0; posicionamento melhorou em 58 ações e piorou em 44.
- Jogador 7 — estado final: ouro 87, nível 8, vida 63.0, colocação 1.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.113 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.074 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 3 | 3 → 4 | 0.007 | 0.000 |
| Jogador 8 | 2-1 | 10 | 6.000 | 0.000 | 0 → 1 | 2 → 0 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.024 | -0.242 |
| Jogador 8 | 2-2 | 6 | 0.000 | 2.000 | 1 → 1 | 0 → 0 | 14% → 14% | 6 → 8 | 7 | 4 → 4 | 0.010 | -0.404 |
| Jogador 8 | 2-3 | 10 | -2.000 | 0.000 | 1 → 1 | 0 → 1 | 14% → 14% | 8 → 15 | 5 | 4 → 5 | -0.022 | -0.253 |
| Jogador 8 | 2-4 | 10 | 6.000 | 0.000 | 1 → 1 | 1 → 1 | 14% → 18% | 15 → 19 | 8 | 5 → 5 | 0.079 | 0.000 |
| Jogador 8 | 2-5 | 10 | 4.000 | 2.000 | 1 → 1 | 1 → 2 | 18% → 18% | 19 → 14 | 16 | 5 → 5 | 0.020 | 0.264 |
| Jogador 8 | 2-6 | 10 | 0.000 | -4.000 | 1 → 1 | 2 → 2 | 18% → 18% | 14 → 24 | 9 | 5 → 5 | -0.022 | 0.251 |
| Jogador 8 | 2-7 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 2 | 18% → 18% | 24 → 33 | 8 | 5 → 5 | 0.022 | 0.000 |
| Jogador 8 | 3-1 | 10 | 8.000 | 8.000 | 1 → 1 | 2 → 2 | 18% → 21% | 33 → 30 | 12 | 5 → 6 | 0.020 | 0.281 |
| Jogador 8 | 3-2 | 10 | 0.000 | 12.000 | 1 → 1 | 2 → 2 | 21% → 21% | 30 → 15 | 23 | 6 → 6 | -0.018 | 0.290 |
| Jogador 8 | 3-3 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 15 → 25 | 7 | 6 → 6 | -0.022 | 0.281 |
| Jogador 8 | 3-4 | 10 | 0.000 | -12.000 | 1 → 1 | 2 → 2 | 21% → 21% | 25 → 41 | 7 | 6 → 6 | 0.022 | 0.000 |
| Jogador 8 | 3-5 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 41 → 36 | 22 | 6 → 7 | 0.005 | 0.290 |
| Jogador 8 | 3-6 | 9 | 6.000 | 18.000 | 1 → 1 | 2 → 3 | 21% → 25% | 36 → 35 | 12 | 7 → 7 | 0.014 | 0.317 |
| Jogador 8 | 3-7 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 35 → 46 | 7 | 7 → 7 | -0.014 | 0.000 |
| Jogador 8 | 4-1 | 10 | -2.000 | 10.000 | 1 → 1 | 3 → 3 | 25% → 21% | 46 → 42 | 19 | 7 → 7 | -0.010 | 0.288 |
| Jogador 8 | 4-2 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 4 | 21% → 21% | 42 → 33 | 27 | 7 → 7 | 0.000 | 0.280 |
| Jogador 8 | 4-3 | 10 | 0.000 | -16.000 | 1 → 1 | 4 → 3 | 21% → 21% | 33 → 45 | 13 | 7 → 7 | 0.000 | -0.276 |
| Jogador 8 | 4-4 | 10 | 4.000 | 0.000 | 1 → 1 | 3 → 3 | 21% → 25% | 45 → 42 | 16 | 7 → 8 | 0.003 | 0.000 |
| Jogador 8 | 4-5 | 7 | 6.000 | 12.000 | 1 → 1 | 3 → 3 | 25% → 29% | 42 → 42 | 9 | 8 → 8 | 0.022 | 0.416 |
| Jogador 8 | 4-6 | 5 | 0.000 | 4.000 | 1 → 1 | 3 → 4 | 29% → 29% | 42 → 51 | 2 | 8 → 8 | 0.000 | 0.582 |
| Jogador 8 | 4-7 | 4 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 29% → 29% | 51 → 62 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 9 | 0.000 | 6.000 | 1 → 1 | 4 → 4 | 29% → 29% | 62 → 69 | 4 | 8 → 8 | 0.002 | -0.304 |
| Jogador 8 | 5-2 | 8 | 0.000 | 0.000 | 1 → 1 | 4 → 5 | 29% → 29% | 69 → 80 | 6 | 8 → 8 | 0.000 | -0.344 |
| Jogador 8 | 5-3 | 10 | -4.000 | 4.000 | 1 → 1 | 5 → 4 | 29% → 25% | 80 → 87 | 13 | 8 → 8 | 0.041 | 0.297 |
| Jogador 8 | 5-4 | 10 | 8.000 | -10.000 | 1 → 1 | 4 → 4 | 25% → 29% | 87 → 100 | 10 | 8 → 8 | 0.004 | 0.000 |
| Jogador 8 | 5-5 | 7 | 0.000 | 6.000 | 1 → 1 | 4 → 6 | 29% → 29% | 100 → 109 | 6 | 8 → 8 | 0.000 | 0.425 |
| Jogador 8 | 5-6 | 10 | 0.000 | 2.000 | 1 → 1 | 6 → 3 | 29% → 29% | 109 → 117 | 10 | 8 → 8 | -0.006 | 0.304 |
| Jogador 8 | 5-7 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 4 | 29% → 29% | 117 → 131 | 11 | 8 → 8 | 0.006 | 0.000 |
| Jogador 8 | 6-1 | 9 | 0.000 | 6.000 | 1 → 1 | 4 → 5 | 29% → 29% | 131 → 138 | 8 | 8 → 8 | -0.007 | -0.317 |
| Jogador 8 | 6-2 | 10 | 0.000 | -6.000 | 1 → 1 | 5 → 5 | 29% → 29% | 138 → 152 | 6 | 8 → 8 | 0.041 | -0.280 |
| Jogador 8 | 6-3 | 10 | -46.000 | -50.000 | 1 → 0 | 5 → 0 | 29% → 0% | 152 → 155 | 12 | 8 → 8 | -0.144 | -0.290 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 40, COMPOSITION_COMPATIBILITY: 36, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 19; mudanças de composição: 0; posicionamento melhorou em 46 ações e piorou em 37.
- Jogador 8 — estado final: ouro 155, nível 8, vida 6.0, colocação 2.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 63 | 30 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 1 | 0 |
| Jogador 2 | 101 | 73 | 7 | 9 | 12 | 1 | 0 | 0 | 22 | 10 | 1 | 0 |
| Jogador 3 | 58 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 1 | 0 | 0 |
| Jogador 4 | 61 | 28 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 6 | 1 | 0 |
| Jogador 5 | 85 | 55 | 1 | 3 | 4 | 1 | 1 | 1 | 8 | 4 | 0 | 0 |
| Jogador 6 | 67 | 40 | 0 | 1 | 2 | 0 | 1 | 0 | 4 | 2 | 4 | 0 |
| Jogador 7 | 58 | 28 | 0 | 0 | 0 | 0 | 0 | 1 | 6 | 1 | 0 | 0 |
| Jogador 8 | 104 | 71 | 8 | 9 | 11 | 2 | 1 | 0 | 15 | 0 | 4 | 0 |
- Jogador 1 — venda DA_18_Ornn (2-5, step 94): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Yunara (4-2, step 204): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_KhaZix (3-1, step 127): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Caitlyn (3-2, step 136): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Warwick (3-4, step 156): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Sejuani (3-5, step 170): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rengar (4-6, step 242): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_KhaZix (5-1, step 267): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_RekSai (3-4, step 152): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Scuttlecrab18 (3-7, step 184): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_18_Rakan (2-7, step 116): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Alistar (3-7, step 182): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_MasterYi_AD (4-1, step 195): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Sejuani (4-3, step 214): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_CrimsonRaptor18 (4-3, step 217): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_RekSai (2-7, step 118): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Sentry (3-2, step 137): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (3-2, step 140): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Alistar (3-6, step 179): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Cassiopeia (3-7, step 185): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Scuttlecrab18 (4-1, step 199): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Rammus (5-2, step 274): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_Vi18 (5-6, step 314): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-5, step 97): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Rakan (2-7, step 113): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_KogMaw18_AD (2-7, step 118): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Sentry (3-2, step 134): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Xayah (5-3, step 286): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 6 — venda DA_Fiddlesticks18 (5-5, step 303): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Camille (2-6, step 106): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rakan (3-4, step 156): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_KogMaw18_AD (3-5, step 165): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Hecarim (4-7, step 252): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_Karma18 (2-6, step 108): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Veigar (4-1, step 197): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Vi18 (4-3, step 213): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_MasterYi_AD (4-3, step 218): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Hecarim (5-4, step 296): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Vi18 (5-6, step 312): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 8 — venda DA_18_MasterYi_AD (5-6, step 314): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.

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
| MEDIUM | Jogador 1 | 4-2 | 204 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 2-2 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 527 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-3 | 634 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 733 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-6 | 988 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 989 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1063 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1193 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1194 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1506 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-4 | 1507 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1643 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-5 | 1644 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1778 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-6 | 1779 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 1912 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-7 | 1913 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 2050 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 2171 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 2172 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-3 | 2284 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-3 | 2285 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 2425 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-4 | 2426 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 2565 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-5 | 2566 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-6 | 2701 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-6 | 2702 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-7 | 2839 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-7 | 2840 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-1 | 2976 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-1 | 2977 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-2 | 3079 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 5-2 | 3080 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 4-2 | 2261 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-5 | 95 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-5 | 97 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Leona) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-6 | 110 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-7 | 115 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_RekSai) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-1 | 126 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-1 | 127 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-2 | 136 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-2 | 140 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-4 | 155 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-4 | 156 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-4 | 156 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Warwick) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-5 | 165 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-5 | 170 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-6 | 177 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 2 | 3-6 | 180 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-7 | 189 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Varus) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-7 | 190 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Krug18) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 4-6 | 242 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-1 | 267 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 282 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 283 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 284 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 285 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 286 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 287 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 288 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 289 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 290 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 291 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 292 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 293 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 294 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 295 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 296 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 297 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 298 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 299 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 300 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 301 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 302 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 303 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 304 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 305 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 306 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 307 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 308 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 309 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 310 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 311 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 312 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 313 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-2 | 2442 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2534 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2811 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-5 | 2812 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 2948 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-6 | 2949 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 3083 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-7 | 3084 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 3222 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-1 | 3223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 3360 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-2 | 3361 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-3 | 3505 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-3 | 3506 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-4 | 3649 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-4 | 3650 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-5 | 3786 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-5 | 3787 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-6 | 3928 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 5-6 | 3929 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| HIGH | Jogador 3 | 3-4 | 152 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-6 | 934 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 1034 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1161 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1261 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1450 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 1773 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 1912 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 2048 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-3 | 2188 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-4 | 2300 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-5 | 2398 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-6 | 2535 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-7 | 2668 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-1 | 2807 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-2 | 2911 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 5-2 | 2912 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 2-6 | 104 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 4 | 2-7 | 116 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 4-3 | 214 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 2-5 | 850 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-6 | 982 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-2 | 1370 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-3 | 1502 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-5 | 1724 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-6 | 1863 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-6 | 1864 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 1984 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-7 | 1985 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-1 | 2124 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-1 | 2125 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 2259 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-2 | 2260 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-3 | 2400 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-3 | 2401 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-4 | 2537 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 2678 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-5 | 2679 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 3-4 | 1701 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-6 | 1961 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-6 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_LeBlanc) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 109 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-2 | 136 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-2 | 137 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sentry' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-2 | 140 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-6 | 179 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-7 | 184 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rengar) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-7 | 185 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-1 | 199 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-6 | 314 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 2-1 | 56 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 57 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 2-7 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 248 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 5-1 | 265 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-3 | 558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 822 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 956 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1686 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1818 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-7 | 1951 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-1 | 2087 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2333 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2334 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-4 | 2438 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-4 | 2439 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-5 | 2579 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-5 | 2580 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 2692 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-7 | 2801 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 2939 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-1 | 2940 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-2 | 3084 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-2 | 3085 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 3197 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-3 | 3198 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-4 | 3327 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-4 | 3328 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-5 | 3468 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-5 | 3469 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-6 | 3607 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-6 | 3608 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 5-2 | 3174 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 2-3 | 76 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 6 | 2-5 | 95 | PURCHASE_SALE_REVIEW | Compra de DA_18_Kayle foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 2-5 | 97 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 2-7 | 113 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 2-7 | 117 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 2-7 | 118 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 3-1 | 130 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Murkwolf18) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 6 | 3-2 | 134 | SOLD_CORE_UNIT | Venda de 'DA_18_Sentry' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 3-7 | 190 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 6 | 4-1 | 199 | PURCHASE_SALE_REVIEW | Compra de DA_Cinderling18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 6 | 5-5 | 303 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
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
| LOW | Jogador 6 | 2-5 | 100 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 107 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 108 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 226 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 227 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 228 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 229 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 253 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 254 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 255 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 256 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 257 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 258 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 259 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 261 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 262 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 263 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 264 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 265 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 266 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 267 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 268 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 269 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 270 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 271 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 272 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 273 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 274 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-2 | 281 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 282 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 283 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 284 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 285 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-3 | 223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-4 | 270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-1 | 355 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-2 | 439 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 537 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 670 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-5 | 806 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-6 | 913 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1046 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1181 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1318 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1454 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1455 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-4 | 1562 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1647 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1648 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-6 | 1759 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-6 | 1760 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-7 | 1895 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1896 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-1 | 2031 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 2032 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 2165 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 2166 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 2287 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 2288 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 2414 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 2415 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-5 | 2500 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-5 | 2501 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-6 | 2586 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 2587 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 2712 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-7 | 2713 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-1 | 2855 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 2856 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 2919 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-2 | 2920 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-3 | 3067 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-3 | 3068 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-4 | 3210 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-4 | 3211 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-5 | 3343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-5 | 3344 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 4-5 | 2563 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-6 | 2689 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 5-1 | 2896 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-6 | 106 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 3-4 | 156 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 3-5 | 165 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
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
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 429 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 567 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-5 | 853 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-6 | 987 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-7 | 1083 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-5 | 1667 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1804 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 2040 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-1 | 2041 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2173 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-2 | 2174 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2309 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-3 | 2310 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2451 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-4 | 2452 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2576 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-5 | 2577 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2703 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-6 | 2704 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2841 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-7 | 2842 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 2976 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-1 | 2977 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-2 | 3112 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-2 | 3113 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-3 | 3231 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-3 | 3232 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-4 | 3309 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-4 | 3310 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-5 | 3387 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-5 | 3388 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-6 | 3465 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-6 | 3466 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-7 | 3531 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-1 | 3607 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-2 | 3726 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-3 | 3865 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-3 | 3866 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| MEDIUM | Jogador 7 | 4-6 | 2818 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-7 | 2930 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-7 | 2941 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 5-1 | 3016 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 5-1 | 3027 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 5-1 | 3038 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 8 | 1-4 | 45 | PURCHASE_SALE_REVIEW | Compra de DA_18_RekSai foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-4 | 87 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kobuko) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-4 | 88 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_KhaZix) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-4 | 90 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 8 | 2-5 | 95 | PURCHASE_SALE_REVIEW | Compra de DA_18_Warwick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-6 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Diana) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 8 | 2-6 | 107 | PURCHASE_SALE_REVIEW | Compra de DA_18_Tristana foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-6 | 108 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Karma18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 2-6 | 110 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-7 | 114 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Vi18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-7 | 116 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-7 | 118 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Ornn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 8 | 3-3 | 149 | PURCHASE_SALE_REVIEW | Compra de DA_18_Xayah foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 3-4 | 155 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kobuko) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-4 | 157 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sejuani) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-4 | 158 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_CrimsonRaptor18) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 8 | 4-1 | 197 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-3 | 213 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-3 | 218 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-4 | 296 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 5-3 | 286 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 287 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 288 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 289 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 290 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-3 | 291 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-6 | 315 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-6 | 316 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-6 | 317 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-6 | 318 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-6 | 319 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-6 | 320 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-6 | 321 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-7 | 322 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-7 | 323 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-7 | 324 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-7 | 325 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-7 | 326 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-7 | 327 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-7 | 328 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-7 | 329 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-7 | 330 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 5-7 | 331 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-1 | 332 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-1 | 333 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-1 | 334 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-1 | 335 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-1 | 336 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-1 | 337 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-1 | 338 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-1 | 339 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-1 | 341 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-2 | 342 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-2 | 343 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-2 | 344 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-2 | 345 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-2 | 346 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-2 | 347 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-2 | 348 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-2 | 349 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-2 | 350 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-2 | 351 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-3 | 352 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-3 | 353 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-3 | 354 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-3 | 355 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-3 | 356 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-3 | 357 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-3 | 358 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-3 | 359 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-3 | 360 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 6-3 | 361 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-3 | 224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-4 | 321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 457 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-2 | 540 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-3 | 677 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 812 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-5 | 947 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-5 | 948 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 2-6 | 1086 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-6 | 1087 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 2-7 | 1224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1225 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-1 | 1359 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1360 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-2 | 1491 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-2 | 1492 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-3 | 1627 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1628 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-4 | 1763 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-4 | 1764 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-5 | 1900 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-5 | 1901 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-6 | 2024 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-6 | 2025 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-7 | 2160 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 2161 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 2299 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 2300 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2430 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-2 | 2431 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2567 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 2568 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 2699 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-4 | 2700 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 2797 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-5 | 2798 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-6 | 2873 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-6 | 2874 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-7 | 2936 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-7 | 2937 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-1 | 3063 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-1 | 3064 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-2 | 3179 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-2 | 3180 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-3 | 3318 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-3 | 3319 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-4 | 3455 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-4 | 3456 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-5 | 3554 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-5 | 3555 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-6 | 3690 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-6 | 3691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-7 | 3829 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-7 | 3830 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-1 | 3958 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-2 | 4101 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-3 | 4241 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 6-3 | 4242 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 4-3 | 2640 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
