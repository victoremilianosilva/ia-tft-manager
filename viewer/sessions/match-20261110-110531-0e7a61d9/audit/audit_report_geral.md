# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **5150**
- Achados: **790**
- CRITICAL: 0 | HIGH: 14 | MEDIUM: 60 | LOW: 716

## Metadados da sessão

- Match ID: 0e7a61d9-0e8d-41ba-b45f-f309e494957f
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 3d63262fb93d7504bfc05b4e6efd43b7d3bf9e722c0407b8e8b1bd7903bc856d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4472**
- Entradas posteriores à eliminação ignoradas: **678**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 63 | 7 | 12 | 4 | 67 | 2 | 2 | não/inconclusivo | 0 |
| Jogador 6 | 62 | 9 | 33 | 7 | 67 | 6 | 0 | não/inconclusivo | 0 |
| Jogador 7 | 129 | 8 | 17 | 6 | 85 | 3 | 2 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 186 | 66 | 42 | 6 | 1 | 12 | 49 | 0.0932 | 7 | 18 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 14, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 5, ALL_IN::PASS: 2, ALL_IN::REROLL: 1, ALL_IN::SELL: 11, STABILIZE::BUY: 52, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 28, STABILIZE::PASS: 10, STABILIZE::SELL: 31
- Jogador 1 — recompensas por ação: BUY: média 0.2536 (n=66), BUY_XP: média -0.0167 (n=6), ITEM: média 0.1550 (n=10), MOVE_BENCH: média 0.2544 (n=16), MOVE_BOARD: média 0.0049 (n=33), PASS: média -0.0833 (n=12), REROLL: média -0.0700 (n=1), SELL: média -0.0955 (n=42)
| Jogador 2 | 303 | 115 | 87 | 20 | 3 | 17 | 51 | 0.0341 | 6 | 41 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 55, ALL_IN::BUY_XP: 1, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 4, ALL_IN::MOVE_BOARD: 20, ALL_IN::PASS: 6, ALL_IN::REROLL: 3, ALL_IN::SELL: 48, STABILIZE::BUY: 60, STABILIZE::BUY_XP: 19, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 10, STABILIZE::MOVE_BOARD: 17, STABILIZE::PASS: 11, STABILIZE::SELL: 39
- Jogador 2 — recompensas por ação: BUY: média 0.1609 (n=115), BUY_XP: média -0.0090 (n=20), ITEM: média 0.1620 (n=10), MOVE_BENCH: média 0.3100 (n=14), MOVE_BOARD: média -0.0095 (n=37), PASS: média -0.1747 (n=17), REROLL: média -0.0700 (n=3), SELL: média -0.1197 (n=87)
| Jogador 3 | 228 | 72 | 37 | 10 | 1 | 26 | 74 | 0.0944 | 7 | 29 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 6, ALL_IN::ITEM: 1, ALL_IN::MOVE_BENCH: 3, ALL_IN::MOVE_BOARD: 3, ALL_IN::REROLL: 1, ALL_IN::SELL: 4, FAST8::BUY: 23, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 24, FAST8::PASS: 10, FAST8::SELL: 15, STABILIZE::BUY: 43, STABILIZE::BUY_XP: 10, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 28, STABILIZE::PASS: 16, STABILIZE::SELL: 18
- Jogador 3 — recompensas por ação: BUY: média 0.3417 (n=72), BUY_XP: média -0.0210 (n=10), ITEM: média 0.1575 (n=8), MOVE_BENCH: média 0.2389 (n=19), MOVE_BOARD: média -0.0036 (n=55), PASS: média -0.0389 (n=26), REROLL: média -0.0700 (n=1), SELL: média -0.1995 (n=37)
| Jogador 4 | 197 | 67 | 36 | 12 | 2 | 15 | 52 | 0.0926 | 6 | 26 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 10, ALL_IN::ITEM: 5, ALL_IN::MOVE_BOARD: 2, ALL_IN::PASS: 1, ALL_IN::REROLL: 1, ALL_IN::SELL: 8, STABILIZE::BUY: 57, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 39, STABILIZE::PASS: 14, STABILIZE::REROLL: 1, STABILIZE::SELL: 28
- Jogador 4 — recompensas por ação: BUY: média 0.3225 (n=67), BUY_XP: média -0.0167 (n=12), ITEM: média 0.1615 (n=13), MOVE_BENCH: média 0.1855 (n=11), MOVE_BOARD: média -0.0080 (n=41), PASS: média -0.0313 (n=15), REROLL: média -0.1350 (n=2), SELL: média -0.1731 (n=36)
| Jogador 5 | 181 | 76 | 52 | 6 | 3 | 11 | 28 | 0.0387 | 8 | 22 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 13, ALL_IN::MOVE_BENCH: 2, ALL_IN::REROLL: 3, ALL_IN::SELL: 9, STABILIZE::BUY: 63, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 20, STABILIZE::MOVE_BOARD: 6, STABILIZE::PASS: 11, STABILIZE::SELL: 43
- Jogador 5 — recompensas por ação: BUY: média 0.2663 (n=76), BUY_XP: média -0.0183 (n=6), ITEM: média 0.1820 (n=5), MOVE_BENCH: média -0.0255 (n=22), MOVE_BOARD: média 0.0517 (n=6), PASS: média -0.0445 (n=11), REROLL: média -0.0700 (n=3), SELL: média -0.2515 (n=52)
| Jogador 6 | 249 | 67 | 33 | 33 | 0 | 20 | 77 | 0.0998 | 12 | 60 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 11, ALL_IN::BUY_XP: 10, ALL_IN::ITEM: 1, ALL_IN::MOVE_BENCH: 5, ALL_IN::MOVE_BOARD: 2, ALL_IN::OTHER: 1, ALL_IN::SELL: 6, FAST8::BUY: 15, FAST8::BUY_XP: 5, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 35, FAST8::PASS: 9, FAST8::SELL: 9, STABILIZE::BUY: 41, STABILIZE::BUY_XP: 18, STABILIZE::ITEM: 13, STABILIZE::MOVE_BENCH: 10, STABILIZE::MOVE_BOARD: 24, STABILIZE::PASS: 11, STABILIZE::SELL: 18
- Jogador 6 — recompensas por ação: BUY: média 0.4139 (n=67), BUY_XP: média 0.0727 (n=33), ITEM: média 0.1322 (n=18), MOVE_BENCH: média 0.1956 (n=16), MOVE_BOARD: média -0.0136 (n=61), OTHER: média 0.0100 (n=1), PASS: média -0.0085 (n=20), SELL: média -0.2970 (n=33)
| Jogador 7 | 279 | 85 | 47 | 17 | 0 | 22 | 91 | 0.0916 | 7 | 49 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 12, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 8, ALL_IN::PASS: 2, ALL_IN::SELL: 8, ECON::BUY: 8, ECON::ITEM: 1, ECON::MOVE_BENCH: 2, ECON::MOVE_BOARD: 9, ECON::PASS: 1, ECON::SELL: 5, FAST8::BUY: 10, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 16, FAST8::PASS: 4, FAST8::SELL: 5, STABILIZE::BUY: 55, STABILIZE::BUY_XP: 17, STABILIZE::ITEM: 12, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 40, STABILIZE::PASS: 15, STABILIZE::SELL: 29
- Jogador 7 — recompensas por ação: BUY: média 0.3465 (n=85), BUY_XP: média -0.0412 (n=17), ITEM: média 0.1294 (n=17), MOVE_BENCH: média 0.2739 (n=18), MOVE_BOARD: média -0.0060 (n=73), PASS: média -0.0696 (n=22), SELL: média -0.1774 (n=47)
| Jogador 8 | 213 | 85 | 58 | 14 | 3 | 10 | 35 | 0.0645 | 16 | 23 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 12, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 3, ALL_IN::MOVE_BOARD: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 6, STABILIZE::BUY: 73, STABILIZE::BUY_XP: 14, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 9, STABILIZE::MOVE_BOARD: 22, STABILIZE::PASS: 10, STABILIZE::REROLL: 1, STABILIZE::SELL: 52
- Jogador 8 — recompensas por ação: BUY: média 0.2842 (n=85), BUY_XP: média -0.0314 (n=14), ITEM: média 0.1625 (n=8), MOVE_BENCH: média 0.2992 (n=12), MOVE_BOARD: média -0.0117 (n=23), PASS: média -0.0030 (n=10), REROLL: média -0.1400 (n=3), SELL: média -0.2438 (n=58)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 11:05:36 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | ? | 11:05:38 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | ? | 11:05:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 11:05:43 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 11:05:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 11:05:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-1 | 11:05:45 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 11:05:46 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 11:05:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 11:05:48 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 1-2 | 11:05:50 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-2 | 11:05:51 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 11:05:51 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 11:05:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-2 | 11:05:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 11:05:58 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 11:05:59 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 11:05:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 11:06:06 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 11:06:08 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 1-4 | 11:06:09 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 11:06:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-4 | 11:06:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 11:06:11 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 2-1 | 11:06:17 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 11:06:18 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.1300 |  |
| Jogador 1 | 2-1 | 11:06:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 11:06:18 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-1 | 11:06:19 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.2800 |  |
| Jogador 1 | 2-1 | 11:06:19 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 11:06:20 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1700 |  |
| Jogador 1 | 2-1 | 11:06:20 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-1 | 11:06:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-2 | 11:06:26 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 1 | 2-2 | 11:06:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 11:06:27 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-2 | 11:06:28 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1800 |  |
| Jogador 1 | 2-2 | 11:06:28 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 1 | 2-2 | 11:06:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 11:06:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 11:06:38 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 1 | 2-3 | 11:06:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 2-3 | 11:06:39 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 1 | 2-3 | 11:06:39 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 2-3 | 11:06:40 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 2-3 | 11:06:40 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 1 | 2-3 | 11:06:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0300 |  |
| Jogador 1 | 2-3 | 11:06:41 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.5600 |  |
| Jogador 1 | 2-3 | 11:06:42 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 1 | 2-4 | 11:06:51 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Defendente | DA_18_Akali_AD | 0.3700 |  |
| Jogador 1 | 2-4 | 11:06:51 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Akali_AD | 0.1600 |  |
| Jogador 1 | 2-4 | 11:06:52 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Akali_AD | 0.0600 |  |
| Jogador 1 | 2-4 | 11:06:52 | MOVE Bench -> Board: Shen (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Akali_AD | 0.0700 |  |
| Jogador 1 | 2-4 | 11:06:53 | MOVE Board -> Board: Ornn (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-4 | 11:06:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-4 | 11:06:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 11:07:05 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Defendente | DA_18_Akali_AD | 1.0500 |  |
| Jogador 1 | 2-5 | 11:07:05 | MOVE Bench -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Defendente | DA_18_Akali_AD | -0.6700 |  |
| Jogador 1 | 2-5 | 11:07:06 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Defendente | DA_18_Akali_AD | 0.4100 |  |
| Jogador 1 | 2-5 | 11:07:06 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Defendente | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-5 | 11:07:07 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Defendente | DA_18_Akali_AD | -0.2900 |  |
| Jogador 1 | 2-5 | 11:07:07 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Defendente | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 2-5 | 11:07:08 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Defendente | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 2-5 | 11:07:08 | MOVE Board -> Board: Elise (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Defendente | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 2-5 | 11:07:09 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-6 | 11:07:21 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Defendente | DA_18_Akali_AD | 0.9500 |  |
| Jogador 1 | 2-6 | 11:07:21 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Defendente | DA_18_Akali_AD | -0.0700 |  |
| Jogador 1 | 2-6 | 11:07:22 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Defendente | DA_18_Akali_AD | 0.3700 |  |
| Jogador 1 | 2-6 | 11:07:22 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Defendente | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 2-6 | 11:07:23 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 11:07:24 | MOVE Board -> Board: Shen (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-6 | 11:07:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 11:07:40 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_SparringGloves -> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Defendente | DA_18_Akali_AD | 0.1700 |  |
| Jogador 1 | 2-7 | 11:07:40 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Defendente | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 2-7 | 11:07:41 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Defendente | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 2-7 | 11:07:41 | MOVE Board -> Board: Elise (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-7 | 11:07:42 | MOVE Board -> Board: Akali (i:4.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-7 | 11:07:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 11:08:02 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Defendente | DA_18_Akali_AD | -0.5800 |  |
| Jogador 1 | 3-1 | 11:08:03 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Defendente | DA_18_Akali_AD | 0.4500 |  |
| Jogador 1 | 3-1 | 11:08:03 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Ornn (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Defendente | DA_18_Akali_AD | 0.1400 |  |
| Jogador 1 | 3-1 | 11:08:04 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Ornn (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Defendente | DA_18_Akali_AD | 0.1600 |  |
| Jogador 1 | 3-1 | 11:08:04 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 11:08:05 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Defendente | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 3-1 | 11:08:05 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 11:08:06 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Defendente | DA_18_Akali_AD | 0.0900 |  |
| Jogador 1 | 3-1 | 11:08:06 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Defendente | DA_18_Akali_AD | -0.0700 |  |
| Jogador 1 | 3-2 | 11:08:24 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 11:08:25 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Defendente | DA_18_Akali_AD | 0.8000 |  |
| Jogador 1 | 3-2 | 11:08:25 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Defendente | DA_18_Akali_AD | -0.0300 |  |
| Jogador 1 | 3-2 | 11:08:26 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Defendente | DA_18_Akali_AD | 0.0600 |  |
| Jogador 1 | 3-2 | 11:08:26 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Defendente | DA_18_Akali_AD | 0.1000 |  |
| Jogador 1 | 3-2 | 11:08:27 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Defendente | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 3-2 | 11:08:27 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Defendente | DA_18_Akali_AD | -0.2000 |  |
| Jogador 1 | 3-2 | 11:08:28 | MOVE Board -> Board: Leona (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-2 | 11:08:28 | MOVE Board -> Board: Shen (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 11:08:48 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Defendente | DA_18_Akali_AD | 0.1100 |  |
| Jogador 1 | 3-3 | 11:08:48 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Defendente | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 11:08:49 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 11:08:49 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Defendente | DA_18_Akali_AD | -0.0300 |  |
| Jogador 1 | 3-3 | 11:08:50 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 11:08:50 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Defendente | DA_18_Akali_AD | -0.2900 |  |
| Jogador 1 | 3-3 | 11:08:51 | MOVE Board -> Board: Elise (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-3 | 11:08:51 | MOVE Board -> Board: Akali (i:4.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Defendente | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 11:08:52 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-4 | 11:09:15 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Defendente | DA_18_Akali_AD | 0.1000 |  |
| Jogador 1 | 3-4 | 11:09:16 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Defendente | DA_18_Akali_AD | 0.7500 |  |
| Jogador 1 | 3-4 | 11:09:16 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Defendente | DA_18_Akali_AD | 0.0900 |  |
| Jogador 1 | 3-4 | 11:09:17 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Defendente | DA_18_Akali_AD | -0.0300 |  |
| Jogador 1 | 3-4 | 11:09:17 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-4 | 11:09:18 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Defendente | DA_18_Akali_AD | -0.3700 |  |
| Jogador 1 | 3-4 | 11:09:19 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Defendente | DA_18_Akali_AD | 0.1000 |  |
| Jogador 1 | 3-4 | 11:09:19 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Defendente | DA_18_Akali_AD | -0.3700 |  |
| Jogador 1 | 3-4 | 11:09:19 | MOVE Board -> Board: Shen (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-5 | 11:09:43 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Defendente | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 3-5 | 11:09:44 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Defendente | DA_18_Akali_AD | 0.8700 |  |
| Jogador 1 | 3-5 | 11:09:44 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Defendente | DA_18_Akali_AD | 0.8100 |  |
| Jogador 1 | 3-5 | 11:09:45 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 2 | Defendente | DA_18_Akali_AD | -0.5000 |  |
| Jogador 1 | 3-5 | 11:09:45 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Defendente | DA_18_Akali_AD | 0.2400 |  |
| Jogador 1 | 3-5 | 11:09:46 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Leona (i:2.0) (tabuleiro slot 26) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Defendente | DA_18_Akali_AD | 0.1400 |  |
| Jogador 1 | 3-5 | 11:09:46 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Defendente | DA_18_Akali_AD | 0.4300 |  |
| Jogador 1 | 3-5 | 11:09:47 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Defendente | DA_18_Akali_AD | 0.0300 |  |
| Jogador 1 | 3-5 | 11:09:47 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 11:10:12 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 11:10:13 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Defendente | DA_18_Akali_AD | 0.5000 |  |
| Jogador 1 | 3-6 | 11:10:13 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 11:10:14 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Defendente | DA_18_Akali_AD | 0.6600 |  |
| Jogador 1 | 3-6 | 11:10:14 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Defendente | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 3-6 | 11:10:15 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Defendente | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 3-6 | 11:10:15 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Defendente | DA_18_Akali_AD | -0.2800 |  |
| Jogador 1 | 3-6 | 11:10:16 | MOVE Board -> Board: Nidalee (i:8.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-6 | 11:10:16 | MOVE Board -> Board: Xayah (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 3-7 | 11:10:43 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NeedlesslyLargeRod -> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Defendente | DA_18_Akali_AD | 0.1100 |  |
| Jogador 1 | 3-7 | 11:10:43 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_BFSword -> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Defendente | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 3-7 | 11:10:44 | VENDEU: Elise (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Defendente | DA_18_Akali_AD | -0.0800 |  |
| Jogador 1 | 3-7 | 11:10:44 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Defendente | DA_18_Akali_AD | 0.3100 |  |
| Jogador 1 | 3-7 | 11:10:45 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Defendente | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 3-7 | 11:10:46 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Defendente | DA_18_Akali_AD | 0.0100 |  |
| Jogador 1 | 3-7 | 11:10:46 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 3-7 | 11:10:47 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Defendente | DA_18_Akali_AD | 0.4700 |  |
| Jogador 1 | 3-7 | 11:10:48 | MOVE Board -> Board: Leona (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 11:11:21 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Defendente | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 4-1 | 11:11:21 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Defendente | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 4-1 | 11:11:22 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Defendente | DA_18_Akali_AD | -0.0900 |  |
| Jogador 1 | 4-1 | 11:11:22 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Defendente | DA_18_Akali_AD | 0.0300 |  |
| Jogador 1 | 4-1 | 11:11:23 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 11:11:23 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Defendente | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 4-1 | 11:11:24 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Defendente | DA_18_Akali_AD | -0.0500 |  |
| Jogador 1 | 4-1 | 11:11:24 | MOVE Board -> Board: Xayah (i:2.0) <-> Nidalee (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 11:11:25 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-2 | 11:11:55 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Defendente | DA_18_Akali_AD | 0.9400 |  |
| Jogador 1 | 4-2 | 11:11:56 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Defendente | DA_18_Akali_AD | -0.6800 |  |
| Jogador 1 | 4-2 | 11:11:56 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Defendente | DA_18_Akali_AD | 1.0200 |  |
| Jogador 1 | 4-2 | 11:11:57 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Defendente | DA_18_Akali_AD | -0.2300 |  |
| Jogador 1 | 4-2 | 11:11:57 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Defendente | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 4-2 | 11:11:58 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Defendente | DA_18_Akali_AD | -0.2700 |  |
| Jogador 1 | 4-2 | 11:11:58 | MOVE Board -> Board: Vi (i:6.0) <-> Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-2 | 11:11:59 | MOVE Board -> Board: Xayah (i:2.0) <-> Nidalee (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 4-2 | 11:11:59 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Defendente | DA_18_Akali_AD | -0.4700 |  |
| Jogador 1 | 4-3 | 11:12:30 | VENDEU: Ornn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Defendente | DA_18_Akali_AD | -0.7200 |  |
| Jogador 1 | 4-3 | 11:12:31 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Defendente | DA_18_Akali_AD | 0.9600 |  |
| Jogador 1 | 4-3 | 11:12:31 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Akali (i:4.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Defendente | DA_18_Akali_AD | 0.1400 |  |
| Jogador 1 | 4-3 | 11:12:31 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Akali (i:4.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Defendente | DA_18_Akali_AD | 0.1300 |  |
| Jogador 1 | 4-3 | 11:12:32 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Defendente | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 4-3 | 11:12:33 | COMPROU: Alistar (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Defendente | DA_18_Akali_AD | 0.1300 |  |
| Jogador 1 | 4-3 | 11:12:33 | VENDEU: Alistar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Defendente | DA_18_Akali_AD | -0.0300 |  |
| Jogador 1 | 4-3 | 11:12:34 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Defendente | DA_18_Akali_AD | 0.0400 |  |
| Jogador 1 | 4-3 | 11:12:34 | MOVE Board -> Board: Nidalee (i:8.0) <-> Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-4 | 11:13:08 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 4-4 | 11:13:08 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Defendente | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 4-4 | 11:13:09 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Defendente | DA_18_Akali_AD | -0.5500 |  |
| Jogador 1 | 4-4 | 11:13:09 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Defendente | DA_18_Akali_AD | 0.2300 |  |
| Jogador 1 | 4-4 | 11:13:10 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-4 | 11:13:11 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Defendente | DA_18_Akali_AD | -0.1400 |  |
| Jogador 1 | 4-4 | 11:13:11 | MOVE Board -> Board: Leona (i:2.0) <-> Akali (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-4 | 11:13:13 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 4-4 | 11:13:14 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Defendente | DA_18_Akali_AD | -0.5300 |  |
| Jogador 1 | 4-5 | 11:13:56 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Defendente | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 4-5 | 11:13:57 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Defendente | DA_18_Akali_AD | -0.2200 |  |
| Jogador 1 | 4-5 | 11:13:57 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-5 | 11:13:58 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Defendente | DA_18_Akali_AD | 0.0100 |  |
| Jogador 1 | 4-5 | 11:13:59 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Defendente | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 4-5 | 11:14:00 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Defendente | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 4-5 | 11:14:00 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Defendente | DA_18_Akali_AD | -0.0700 |  |
| Jogador 1 | 4-5 | 11:14:01 | VENDEU: Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Defendente | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 4-5 | 11:14:01 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Defendente | DA_18_Akali_AD | 1.0700 |  |
| Jogador 2 | ? | 11:05:36 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | ? | 11:05:38 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | ? | 11:05:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 11:05:43 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 11:05:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 11:05:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 1-1 | 11:05:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 11:05:48 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 1-2 | 11:05:50 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 11:05:51 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 11:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 11:05:55 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 11:05:58 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 11:05:59 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 11:05:59 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-3 | 11:06:00 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-3 | 11:06:02 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 11:06:02 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 11:06:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 11:06:06 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 11:06:08 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 11:06:09 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 11:06:09 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 11:06:10 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 1-4 | 11:06:10 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 1-4 | 11:06:11 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-4 | 11:06:11 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 1-4 | 11:06:11 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 11:06:12 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 1-4 | 11:06:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 11:06:17 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 2-1 | 11:06:18 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 2-1 | 11:06:18 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 2-1 | 11:06:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 11:06:26 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-2 | 11:06:27 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 2-2 | 11:06:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-2 | 11:06:28 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-2 | 11:06:28 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-2 | 11:06:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 11:06:38 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.7600 |  |
| Jogador 2 | 2-3 | 11:06:38 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-3 | 11:06:39 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-3 | 11:06:39 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 11:06:40 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 2-3 | 11:06:40 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 2-3 | 11:06:41 | MOVE Board -> Board: Vi (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 11:06:41 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 11:06:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-4 | 11:06:51 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 2-4 | 11:06:51 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-4 | 11:06:52 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-4 | 11:06:52 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 11:06:53 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.1700 |  |
| Jogador 2 | 2-4 | 11:06:53 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-4 | 11:06:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 11:06:54 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-4 | 11:06:54 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-5 | 11:07:05 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 2-5 | 11:07:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 11:07:06 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-5 | 11:07:06 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Veigar | -0.4200 |  |
| Jogador 2 | 2-5 | 11:07:07 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 2-5 | 11:07:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 11:07:08 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 2-5 | 11:07:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-5 | 11:07:09 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 2-6 | 11:07:21 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | 0.2800 |  |
| Jogador 2 | 2-6 | 11:07:21 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 2-6 | 11:07:22 | MOVE Bench -> Board: Lillia (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 2-6 | 11:07:22 | MOVE Board -> Board: Lillia (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-6 | 11:07:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-6 | 11:07:24 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-6 | 11:07:24 | MOVE Board -> Board: Veigar (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-6 | 11:07:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-7 | 11:07:40 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 2-7 | 11:07:40 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 2-7 | 11:07:41 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 2-7 | 11:07:41 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 2-7 | 11:07:42 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-7 | 11:07:42 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 2-7 | 11:07:43 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 11:07:44 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-7 | 11:07:44 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 11:08:02 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | 0.8400 |  |
| Jogador 2 | 3-1 | 11:08:03 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 3-1 | 11:08:03 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.2400 |  |
| Jogador 2 | 3-1 | 11:08:04 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.3000 |  |
| Jogador 2 | 3-1 | 11:08:04 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.5800 |  |
| Jogador 2 | 3-1 | 11:08:05 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.3000 |  |
| Jogador 2 | 3-1 | 11:08:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 11:08:06 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-1 | 11:08:06 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 3-2 | 11:08:24 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-2 | 11:08:25 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-2 | 11:08:25 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 3-2 | 11:08:26 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 3-2 | 11:08:26 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 3-2 | 11:08:27 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.3000 |  |
| Jogador 2 | 3-2 | 11:08:27 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 3-2 | 11:08:28 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.3000 |  |
| Jogador 2 | 3-2 | 11:08:28 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 3-3 | 11:08:48 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 3-3 | 11:08:48 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-3 | 11:08:49 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 3-3 | 11:08:49 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-3 | 11:08:50 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-3 | 11:08:50 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 11:08:51 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-3 | 11:08:51 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 3-3 | 11:08:52 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 3-4 | 11:09:15 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.6600 |  |
| Jogador 2 | 3-4 | 11:09:16 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-4 | 11:09:16 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 3-4 | 11:09:17 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-4 | 11:09:17 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 3-4 | 11:09:18 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-4 | 11:09:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-4 | 11:09:19 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-4 | 11:09:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 3-5 | 11:09:43 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 3-5 | 11:09:44 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-5 | 11:09:44 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 3-5 | 11:09:45 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-5 | 11:09:45 | MOVE Board -> Board: Rammus (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-5 | 11:09:46 | MOVE Board -> Board: Veigar (i:4.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-5 | 11:09:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-6 | 11:10:12 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-6 | 11:10:13 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Feérico | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-6 | 11:10:13 | VENDEU: Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-6 | 11:10:14 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Feérico | DA_18_Tristana | 0.8300 |  |
| Jogador 2 | 3-6 | 11:10:14 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 2 | 3-6 | 11:10:15 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Feérico | DA_18_Tristana | -0.2400 |  |
| Jogador 2 | 3-6 | 11:10:15 | MOVE Board -> Board: Lillia (i:8.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 3-6 | 11:10:16 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 3-6 | 11:10:16 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 3-7 | 11:10:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Feérico | DA_18_Tristana | 0.1900 |  |
| Jogador 2 | 3-7 | 11:10:43 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Feérico | DA_18_Tristana | 0.2100 |  |
| Jogador 2 | 3-7 | 11:10:44 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Feérico | DA_18_Veigar | -0.4900 |  |
| Jogador 2 | 3-7 | 11:10:44 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 3-7 | 11:10:45 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-7 | 11:10:46 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Feérico | DA_18_Veigar | -0.2400 |  |
| Jogador 2 | 3-7 | 11:10:46 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-7 | 11:10:47 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Feérico | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 3-7 | 11:10:48 | MOVE Bench -> Board: Lillia (i:8.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Feérico | DA_18_Veigar | -0.3900 |  |
| Jogador 2 | 4-1 | 11:11:21 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Feérico | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-1 | 11:11:21 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Feérico | DA_18_Veigar | 0.8400 |  |
| Jogador 2 | 4-1 | 11:11:22 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 4-1 | 11:11:22 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Feérico | DA_18_Veigar | -0.5000 |  |
| Jogador 2 | 4-1 | 11:11:23 | EQUIP_FROM_INVENTORY: TFT_Item_RunaansHurricane -> Vi (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Feérico | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 4-1 | 11:11:23 | EQUIP_FROM_INVENTORY: TFT_Item_Crownguard -> Vi (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Feérico | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 4-1 | 11:11:24 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Feérico | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 4-1 | 11:11:24 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-1 | 11:11:25 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-2 | 11:11:55 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Feérico | DA_18_Veigar | 0.2800 |  |
| Jogador 2 | 4-2 | 11:11:56 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-2 | 11:11:56 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 4-2 | 11:11:57 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-2 | 11:11:57 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-2 | 11:11:58 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Feérico | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 4-2 | 11:11:58 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-2 | 11:11:59 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 4-2 | 11:11:59 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-3 | 11:12:30 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Feérico | DA_18_Veigar | 0.8800 |  |
| Jogador 2 | 4-3 | 11:12:31 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 4-3 | 11:12:31 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Feérico | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 4-3 | 11:12:31 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 4-3 | 11:12:32 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-3 | 11:12:33 | VENDEU: Rammus (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Feérico | DA_18_Veigar | -0.7000 |  |
| Jogador 2 | 4-3 | 11:12:33 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 11 | 0 | Feérico | DA_18_Veigar | -0.3000 |  |
| Jogador 2 | 4-3 | 11:12:34 | VENDEU: Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 12 | 0 | Feérico | DA_18_Veigar | -0.7200 |  |
| Jogador 2 | 4-3 | 11:12:34 | VENDEU: Rubrivirim (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 13 | 0 | Feérico | DA_18_Veigar | -0.5100 |  |
| Jogador 2 | 4-4 | 11:13:08 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 16 | 1 | Feérico | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 4-4 | 11:13:08 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 13 | 1 | Feérico | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 4-4 | 11:13:09 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 11 | 1 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 4-4 | 11:13:09 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 13 | 1 | Feérico | DA_18_Veigar | -0.3500 |  |
| Jogador 2 | 4-4 | 11:13:10 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 16 | 1 | Feérico | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 4-4 | 11:13:11 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Feérico | DA_18_Veigar | -0.5900 |  |
| Jogador 2 | 4-4 | 11:13:11 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 13 | 1 | Feérico | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 4-4 | 11:13:13 | MOVE Bench -> Board: Rengar (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 13 | 1 | Feérico | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 4-4 | 11:13:14 | MOVE Board -> Board: Rengar (i:6.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 13 | 1 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-5 | 11:13:56 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 19 | 1 | Feérico | DA_18_Veigar | 0.3900 |  |
| Jogador 2 | 4-5 | 11:13:57 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 18 | 1 | Feérico | DA_18_Veigar | 0.3700 |  |
| Jogador 2 | 4-5 | 11:13:57 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 16 | 1 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-5 | 11:13:58 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 15 | 1 | Feérico | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 4-5 | 11:13:59 | MOVE Board -> Board: Tristana (i:6.0) <-> Veigar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 15 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-5 | 11:14:00 | MOVE Board -> Board: Veigar (i:4.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 15 | 1 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-5 | 11:14:00 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 15 | 1 | Feérico | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 4-6 | 11:14:53 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 21 | 1 | Feérico | DA_18_Veigar | 0.3400 |  |
| Jogador 2 | 4-6 | 11:14:54 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 19 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-6 | 11:14:54 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Feérico | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 4-6 | 11:14:54 | MOVE Board -> Board: Lillia (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-6 | 11:14:55 | MOVE Board -> Board: Tristana (i:6.0) <-> Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 4-6 | 11:14:55 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 18 | 1 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-6 | 11:14:56 | COMPROU: Varus (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Feérico | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 4-6 | 11:14:56 | MOVE Board -> Board: Rengar (i:6.0) <-> Veigar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-6 | 11:14:57 | MOVE Board -> Board: Veigar (i:4.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-7 | 11:15:38 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 23 | 1 | Feérico | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 4-7 | 11:15:38 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 23 | 1 | Feérico | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 4-7 | 11:15:39 | VENDEU: Varus (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 4-7 | 11:15:39 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 22 | 1 | Feérico | DA_18_Veigar | 0.5200 |  |
| Jogador 2 | 4-7 | 11:15:40 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 1 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-7 | 11:15:41 | COMPROU: Lux (Sabugueiro) (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 19 | 1 | Feérico | DA_18_Veigar | -0.2200 |  |
| Jogador 2 | 4-7 | 11:15:41 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 21 | 1 | Feérico | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-7 | 11:15:42 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 18 | 1 | Feérico | DA_18_Veigar | -0.2000 |  |
| Jogador 2 | 4-7 | 11:15:42 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Feérico | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 5-1 | 11:16:24 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 25 | 2 | Feérico | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 5-1 | 11:16:25 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 28 | 2 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-1 | 11:16:25 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 25 | 2 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 5-1 | 11:16:26 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 28 | 2 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-1 | 11:16:27 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 24 | 2 | Feérico | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 5-1 | 11:16:27 | VENDEU: Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 28 | 2 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-1 | 11:16:28 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 25 | 2 | Feérico | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 5-1 | 11:16:28 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 28 | 2 | Feérico | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 5-1 | 11:16:29 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 26 | 2 | Feérico | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 5-2 | 11:17:18 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 5-2 | 11:17:19 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Feérico | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 5-2 | 11:17:19 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-2 | 11:17:20 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Feérico | DA_18_Veigar | -0.2400 |  |
| Jogador 2 | 5-2 | 11:17:20 | VENDEU: Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 5-2 | 11:17:21 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 34 | 2 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-2 | 11:17:21 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 5-2 | 11:17:22 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 34 | 2 | Feérico | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 5-2 | 11:17:22 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 5-3 | 11:18:11 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Feérico | DA_18_Veigar | 0.9700 |  |
| Jogador 2 | 5-3 | 11:18:11 | VENDEU: Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 3 | Feérico | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 5-3 | 11:18:12 | COMPROU: Alune (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 45 | 3 | Feérico | DA_18_Veigar | 0.2500 |  |
| Jogador 2 | 5-3 | 11:18:14 | VENDEU: Lux (Sabugueiro) (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 3 | Feérico | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 5-3 | 11:18:14 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 47 | 3 | Feérico | DA_18_Veigar | -0.2100 |  |
| Jogador 2 | 5-3 | 11:18:15 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 3 | Feérico | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 5-3 | 11:18:15 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 5-3 | 11:18:16 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Feérico | DA_18_Veigar | 0.5900 |  |
| Jogador 2 | 5-4 | 11:18:42 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 55 | 4 | Feérico | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 5-4 | 11:18:42 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-4 | 11:18:43 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 5-4 | 11:18:43 | MOVE Board -> Board: Veigar (i:2.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-4 | 11:18:44 | MOVE Board -> Board: Tristana (i:6.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-4 | 11:18:44 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Feérico | DA_18_Veigar | -0.4800 |  |
| Jogador 2 | 5-5 | 11:19:32 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-5 | 11:19:33 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 69 | 5 | Feérico | DA_18_Veigar | 0.3900 |  |
| Jogador 2 | 5-5 | 11:19:33 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-5 | 11:19:34 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Feérico | DA_18_Veigar | 0.3700 |  |
| Jogador 2 | 5-5 | 11:19:34 | MOVE Board -> Board: Lillia (i:8.0) <-> Veigar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-5 | 11:19:34 | MOVE Board -> Board: Veigar (i:4.0) <-> Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-5 | 11:19:35 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Feérico | DA_18_Veigar | -0.4900 |  |
| Jogador 2 | 5-6 | 11:20:20 | VENDEU: Alune (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 5-6 | 11:20:20 | COMPROU: Lux (Lunar) (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Feérico | DA_18_Veigar | -0.1300 |  |
| Jogador 2 | 5-6 | 11:20:21 | VENDEU: Lux (Lunar) (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-6 | 11:20:21 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Feérico | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 5-6 | 11:20:22 | MOVE Board -> Board: Rengar (i:6.0) <-> Kobuko (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-6 | 11:20:22 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-6 | 11:20:23 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Feérico | DA_18_Veigar | -0.5200 |  |
| Jogador 2 | 5-7 | 11:21:13 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Veigar (i:4.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Feérico | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 5-7 | 11:21:13 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Feérico | DA_18_Veigar | -0.5400 |  |
| Jogador 2 | 5-7 | 11:21:14 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-7 | 11:21:14 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-7 | 11:21:15 | MOVE Board -> Board: Veigar (i:2.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-7 | 11:21:15 | MOVE Board -> Board: Tristana (i:6.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-7 | 11:21:16 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Feérico | DA_18_Veigar | -0.5500 |  |
| Jogador 2 | 6-1 | 11:22:10 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 6-1 | 11:22:11 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Feérico | DA_18_Veigar | 0.4400 |  |
| Jogador 2 | 6-1 | 11:22:11 | MOVE Board -> Board: Lillia (i:8.0) <-> Veigar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 6-1 | 11:22:12 | VENDEU: Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 6-1 | 11:22:12 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 6-1 | 11:22:13 | MOVE Board -> Board: Veigar (i:4.0) <-> Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 6-1 | 11:22:13 | MOVE Board -> Board: Rengar (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 6-1 | 11:22:14 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Feérico | DA_18_Veigar | -0.5700 |  |
| Jogador 2 | 6-2 | 11:23:03 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 6-2 | 11:23:03 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Feérico | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 6-2 | 11:23:04 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 6-2 | 11:23:04 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Feérico | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 6-2 | 11:23:05 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 6-2 | 11:23:05 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 6-2 | 11:23:05 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 6-2 | 11:23:06 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 6-2 | 11:23:06 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 6-3 | 11:23:56 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 6-3 | 11:23:57 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Feérico | DA_18_Veigar | 0.9600 |  |
| Jogador 2 | 6-3 | 11:23:57 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Feérico | DA_18_Veigar | -0.5500 |  |
| Jogador 2 | 6-3 | 11:23:58 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 6-3 | 11:23:58 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 6-3 | 11:23:58 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 6-3 | 11:23:59 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 6-3 | 11:23:59 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Feérico | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 6-3 | 11:24:00 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 6-4 | 11:25:00 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 6-4 | 11:25:00 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Feérico | DA_18_Veigar | 0.4600 |  |
| Jogador 2 | 6-4 | 11:25:00 | VENDEU: Sett (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Feérico | DA_18_Veigar | -0.5600 |  |
| Jogador 2 | 6-4 | 11:25:01 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Feérico | DA_18_Veigar | -0.1400 |  |
| Jogador 2 | 6-4 | 11:25:01 | VENDEU: Sett (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 6-4 | 11:25:02 | COMPROU: Morgana (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Feérico | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 6-4 | 11:25:02 | VENDEU: Morgana (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 6-4 | 11:25:02 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Feérico | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 6-4 | 11:25:03 | VENDEU: Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 6-5 | 11:25:53 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Feérico | DA_18_Lillia | 1.1100 |  |
| Jogador 2 | 6-5 | 11:25:54 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Feérico | DA_18_Lillia | 0.3300 |  |
| Jogador 2 | 6-5 | 11:25:54 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Feérico | DA_18_Lillia | 0.4200 |  |
| Jogador 2 | 6-5 | 11:25:55 | VENDEU: Lillia (i:16.0) | ALL_IN | HP crítico: gastar para sobreviver | 164 | 5 | Feérico | DA_18_Veigar | -0.7200 |  |
| Jogador 2 | 6-5 | 11:25:55 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 161 | 5 | Feérico | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 6-5 | 11:25:55 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 6-5 | 11:25:56 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 162 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 6-5 | 11:25:56 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 161 | 5 | Feérico | DA_18_Veigar | 1.0000 |  |
| Jogador 2 | 6-5 | 11:25:57 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 164 | 5 | Feérico | DA_18_Veigar | -0.5500 |  |
| Jogador 3 | ? | 11:05:36 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | ? | 11:05:38 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | ? | 11:05:38 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | ? | 11:05:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 11:05:43 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 11:05:43 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 11:05:44 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-1 | 11:05:45 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 1-1 | 11:05:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 11:05:48 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-2 | 11:05:50 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 11:05:51 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 11:05:51 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 11:05:52 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-2 | 11:05:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 11:05:55 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 1-3 | 11:05:58 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 11:05:59 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 11:05:59 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 11:06:00 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 11:06:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 11:06:06 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 1-4 | 11:06:08 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 1-4 | 11:06:09 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 11:06:09 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 11:06:10 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 11:06:10 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 1-4 | 11:06:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-1 | 11:06:17 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-1 | 11:06:18 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 11:06:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 11:06:26 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-2 | 11:06:27 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 2-2 | 11:06:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-2 | 11:06:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 11:06:38 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-3 | 11:06:38 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 2-3 | 11:06:39 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 2-3 | 11:06:39 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 2-3 | 11:06:40 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-3 | 11:06:40 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 2-3 | 11:06:41 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-3 | 11:06:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 11:06:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 2-4 | 11:06:51 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-4 | 11:06:52 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-4 | 11:06:52 | MOVE Bench -> Board: Diana (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.3800 |  |
| Jogador 3 | 2-4 | 11:06:53 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 2-4 | 11:06:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 11:07:05 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 11:07:05 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 2-5 | 11:07:06 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 11:07:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 2-5 | 11:07:07 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 11:07:07 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.5800 |  |
| Jogador 3 | 2-5 | 11:07:08 | MOVE Board -> Board: Yorick (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-5 | 11:07:08 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-5 | 11:07:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 11:07:21 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-6 | 11:07:21 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-6 | 11:07:22 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.2900 |  |
| Jogador 3 | 2-6 | 11:07:22 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 11:07:23 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 2-6 | 11:07:24 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 2-6 | 11:07:24 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.2900 |  |
| Jogador 3 | 2-6 | 11:07:24 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-6 | 11:07:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 2-7 | 11:07:40 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.5200 |  |
| Jogador 3 | 2-7 | 11:07:40 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.2800 |  |
| Jogador 3 | 2-7 | 11:07:41 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.1700 |  |
| Jogador 3 | 2-7 | 11:07:41 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-7 | 11:07:42 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-7 | 11:07:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 11:08:02 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.7100 |  |
| Jogador 3 | 3-1 | 11:08:03 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 3-1 | 11:08:03 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 11:08:04 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 3-1 | 11:08:04 | MOVE Board -> Board: Akali (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 11:08:05 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-1 | 11:08:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-2 | 11:08:24 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Akali_AD | -0.3400 |  |
| Jogador 3 | 3-2 | 11:08:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | 3-2 | 11:08:25 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-2 | 11:08:26 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | -0.3400 |  |
| Jogador 3 | 3-2 | 11:08:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 11:08:27 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-2 | 11:08:27 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.2500 |  |
| Jogador 3 | 3-2 | 11:08:28 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-2 | 11:08:28 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 11:08:48 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-3 | 11:08:48 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Akali_AD | 0.8000 |  |
| Jogador 3 | 3-3 | 11:08:49 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Akali_AD | -0.5900 |  |
| Jogador 3 | 3-3 | 11:08:49 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | -0.1900 |  |
| Jogador 3 | 3-3 | 11:08:50 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 11:08:50 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 11:08:51 | MOVE Board -> Board: Diana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 11:08:51 | MOVE Board -> Board: Akali (i:4.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 11:08:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 11:09:15 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-4 | 11:09:16 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.8300 |  |
| Jogador 3 | 3-4 | 11:09:16 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.2800 |  |
| Jogador 3 | 3-4 | 11:09:17 | MOVE Board -> Board: Diana (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 11:09:17 | MOVE Board -> Board: Diana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 11:09:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 11:09:43 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.8100 |  |
| Jogador 3 | 3-5 | 11:09:44 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Akali_AD | -0.4900 |  |
| Jogador 3 | 3-5 | 11:09:44 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Akali_AD | 0.8000 |  |
| Jogador 3 | 3-5 | 11:09:45 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-5 | 11:09:45 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-5 | 11:09:46 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 11:09:46 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-5 | 11:09:47 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-5 | 11:09:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-6 | 11:10:12 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 3-6 | 11:10:13 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 3-6 | 11:10:13 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_18_Akali_AD | -0.4900 |  |
| Jogador 3 | 3-6 | 11:10:14 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_18_Akali_AD | 0.3500 |  |
| Jogador 3 | 3-6 | 11:10:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-6 | 11:10:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 3-6 | 11:10:15 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 1 | Colosso | DA_18_Akali_AD | 0.5700 |  |
| Jogador 3 | 3-6 | 11:10:16 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 1 | Colosso | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 3-6 | 11:10:16 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-7 | 11:10:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 3-7 | 11:10:43 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_TearOfTheGoddess -> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 3-7 | 11:10:44 | VENDEU: Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-7 | 11:10:44 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Akali_AD | 0.7300 |  |
| Jogador 3 | 3-7 | 11:10:45 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-7 | 11:10:46 | MOVE Board -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-7 | 11:10:46 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 11:11:21 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-1 | 11:11:21 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Colosso | DA_18_Akali_AD | -0.2800 |  |
| Jogador 3 | 4-1 | 11:11:22 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 11:11:22 | MOVE Board -> Board: Diana (i:6.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-1 | 11:11:23 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-2 | 11:11:55 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-2 | 11:11:56 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 4-2 | 11:11:56 | MOVE Board -> Board: Akali (i:4.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 11:11:57 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-2 | 11:11:57 | MOVE Board -> Board: Yorick (i:4.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-2 | 11:11:58 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-3 | 11:12:30 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 11:12:31 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-3 | 11:12:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 4-4 | 11:13:08 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-4 | 11:13:08 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Colosso | DA_18_Akali_AD | 0.8500 |  |
| Jogador 3 | 4-4 | 11:13:09 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Colosso | DA_KogMaw18_AD | 0.7700 |  |
| Jogador 3 | 4-4 | 11:13:09 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 3 | Colosso | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 3 | 4-4 | 11:13:10 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Colosso | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 3 | 4-4 | 11:13:11 | MOVE Board -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 4-4 | 11:13:11 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 11:13:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Colosso | DA_KogMaw18_AD | -0.1800 |  |
| Jogador 3 | 4-5 | 11:13:56 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 3 | 4-5 | 11:13:57 | MOVE Board -> Board: Akali (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 4-5 | 11:13:57 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 3 | 4-5 | 11:13:58 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 3 | 4-6 | 11:14:53 | VENDEU: Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 4 | Colosso | DA_KogMaw18_AD | -0.6000 |  |
| Jogador 3 | 4-6 | 11:14:54 | COMPROU: Sivir (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 58 | 4 | Colosso | DA_KogMaw18_AD | 0.6300 |  |
| Jogador 3 | 4-6 | 11:14:54 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 4 | Colosso | DA_Scuttlecrab18 | -0.6000 |  |
| Jogador 3 | 4-6 | 11:14:54 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 4 | Colosso | DA_Scuttlecrab18 | 0.6500 |  |
| Jogador 3 | 4-6 | 11:14:55 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 4 | Colosso | DA_Scuttlecrab18 | -0.0700 |  |
| Jogador 3 | 4-6 | 11:14:55 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 4 | Colosso | DA_Scuttlecrab18 | 0.3000 |  |
| Jogador 3 | 4-6 | 11:14:56 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 4 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-6 | 11:14:56 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 4 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 4-6 | 11:14:57 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 4 | Colosso | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 4-7 | 11:15:38 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Colosso | DA_Scuttlecrab18 | 0.2200 |  |
| Jogador 3 | 4-7 | 11:15:38 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Colosso | DA_Scuttlecrab18 | 0.1600 |  |
| Jogador 3 | 4-7 | 11:15:39 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 76 | 5 | Colosso | DA_Scuttlecrab18 | -0.5900 |  |
| Jogador 3 | 4-7 | 11:15:39 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 74 | 5 | Colosso | DA_Scuttlecrab18 | 0.9100 |  |
| Jogador 3 | 4-7 | 11:15:40 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Colosso | DA_Scuttlecrab18 | -0.0700 |  |
| Jogador 3 | 4-7 | 11:15:41 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Colosso | DA_Scuttlecrab18 | -0.2700 |  |
| Jogador 3 | 4-7 | 11:15:41 | VENDEU: Lobo Trevoguari (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Colosso | DA_Scuttlecrab18 | -0.1300 |  |
| Jogador 3 | 4-7 | 11:15:42 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 76 | 5 | Colosso | DA_Scuttlecrab18 | 0.6100 |  |
| Jogador 3 | 4-7 | 11:15:42 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 76 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-1 | 11:16:24 | VENDEU: Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 5-1 | 11:16:25 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 89 | 5 | Colosso | DA_Scuttlecrab18 | 0.8700 |  |
| Jogador 3 | 5-1 | 11:16:25 | VENDEU: Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Colosso | DA_Scuttlecrab18 | -0.4400 |  |
| Jogador 3 | 5-1 | 11:16:26 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 87 | 5 | Colosso | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 3 | 5-1 | 11:16:27 | VENDEU: Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-1 | 11:16:27 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 5-1 | 11:16:28 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-1 | 11:16:28 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-1 | 11:16:29 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_Scuttlecrab18 | -0.1100 |  |
| Jogador 3 | 5-2 | 11:17:18 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 5-2 | 11:17:19 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Colosso | DA_Scuttlecrab18 | 0.1300 |  |
| Jogador 3 | 5-2 | 11:17:19 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_Scuttlecrab18 | -0.4300 |  |
| Jogador 3 | 5-2 | 11:17:20 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Colosso | DA_Scuttlecrab18 | -0.1600 |  |
| Jogador 3 | 5-2 | 11:17:20 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-2 | 11:17:21 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-2 | 11:17:21 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-2 | 11:17:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Colosso | DA_Scuttlecrab18 | -0.1300 |  |
| Jogador 3 | 5-3 | 11:18:11 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-3 | 11:18:11 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 110 | 5 | Colosso | DA_Scuttlecrab18 | 0.9500 |  |
| Jogador 3 | 5-3 | 11:18:12 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 108 | 5 | Colosso | DA_Scuttlecrab18 | 0.3500 |  |
| Jogador 3 | 5-3 | 11:18:14 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Colosso | DA_Scuttlecrab18 | -0.8500 |  |
| Jogador 3 | 5-3 | 11:18:14 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 110 | 5 | Colosso | DA_Scuttlecrab18 | 0.1800 |  |
| Jogador 3 | 5-3 | 11:18:15 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 110 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-3 | 11:18:15 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Colosso | DA_Scuttlecrab18 | -0.0600 |  |
| Jogador 3 | 5-3 | 11:18:16 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 113 | 5 | Colosso | DA_Scuttlecrab18 | 0.4300 |  |
| Jogador 3 | 5-4 | 11:18:42 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 120 | 5 | Colosso | DA_Scuttlecrab18 | 0.1000 |  |
| Jogador 3 | 5-4 | 11:18:42 | COMPROU: Lux (Espinhos Negros) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Colosso | DA_Scuttlecrab18 | -0.1600 |  |
| Jogador 3 | 5-4 | 11:18:43 | MOVE Board -> Board: Vi (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-4 | 11:18:43 | MOVE Board -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-4 | 11:18:44 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Colosso | DA_Scuttlecrab18 | -0.1500 |  |
| Jogador 3 | 5-5 | 11:19:32 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Colosso | DA_Scuttlecrab18 | -0.0600 |  |
| Jogador 3 | 5-5 | 11:19:33 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Colosso | DA_Scuttlecrab18 | 0.1700 |  |
| Jogador 3 | 5-5 | 11:19:33 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Colosso | DA_Scuttlecrab18 | -0.0600 |  |
| Jogador 3 | 5-5 | 11:19:34 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Colosso | DA_Scuttlecrab18 | -0.2500 |  |
| Jogador 3 | 5-5 | 11:19:34 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-5 | 11:19:34 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-5 | 11:19:35 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Colosso | DA_Scuttlecrab18 | -0.2000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 5-6 | 11:20:20 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-6 | 11:20:20 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Colosso | DA_18_Diana | 1.0600 |  |
| Jogador 3 | 5-6 | 11:20:21 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Colosso | DA_18_Diana | 0.2600 |  |
| Jogador 3 | 5-6 | 11:20:21 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Colosso | DA_18_Diana | 0.5000 |  |
| Jogador 3 | 5-6 | 11:20:22 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Colosso | DA_Lux18_Blackthorn | -0.7200 |  |
| Jogador 3 | 5-6 | 11:20:22 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Colosso | DA_Lux18_Blackthorn | 0.3900 |  |
| Jogador 3 | 5-6 | 11:20:23 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Colosso | DA_Lux18_Blackthorn | -0.4000 |  |
| Jogador 3 | 5-6 | 11:20:23 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Colosso | DA_Lux18_Blackthorn | -0.0700 |  |
| Jogador 3 | 5-6 | 11:20:24 | VENDEU: Lux (Espinhos Negros) (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 3 | 5-7 | 11:21:13 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Colosso | DA_18_Yorick | 0.7400 |  |
| Jogador 3 | 5-7 | 11:21:13 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Akali (i:4.0) (tabuleiro slot 12) | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Colosso | DA_18_Yorick | 0.0700 |  |
| Jogador 3 | 5-7 | 11:21:14 | VENDEU: Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Colosso | DA_18_Yorick | -0.7100 |  |
| Jogador 3 | 5-7 | 11:21:14 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Colosso | DA_18_Yorick | -0.0400 |  |
| Jogador 3 | 5-7 | 11:21:15 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Colosso | DA_18_Yorick | 0.5300 |  |
| Jogador 3 | 5-7 | 11:21:15 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Colosso | DA_18_Yorick | -0.0400 |  |
| Jogador 3 | 5-7 | 11:21:16 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 5-7 | 11:21:16 | MOVE Board -> Board: Rakan (i:2.0) <-> Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 3 | 5-7 | 11:21:16 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | ? | 11:05:36 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | ? | 11:05:38 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | ? | 11:05:38 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | ? | 11:05:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 11:05:43 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 11:05:43 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 11:05:44 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-1 | 11:05:45 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 1-1 | 11:05:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 11:05:48 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4600 |  |
| Jogador 4 | 1-2 | 11:05:50 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 11:05:51 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 11:05:51 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 11:05:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-2 | 11:05:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 11:05:58 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 11:05:59 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 11:05:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 11:06:06 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 4 | 1-4 | 11:06:08 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 1-4 | 11:06:09 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-4 | 11:06:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 1-4 | 11:06:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 11:06:11 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3900 |  |
| Jogador 4 | 2-1 | 11:06:17 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 2-1 | 11:06:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 2-1 | 11:06:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-2 | 11:06:26 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 4 | 2-2 | 11:06:27 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-2 | 11:06:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-2 | 11:06:28 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-2 | 11:06:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 11:06:29 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 11:06:29 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 11:06:29 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 4 | 2-2 | 11:06:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 11:06:38 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-3 | 11:06:38 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-3 | 11:06:39 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 4 | 2-3 | 11:06:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-3 | 11:06:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-3 | 11:06:40 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 2-3 | 11:06:41 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 2-3 | 11:06:41 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 4 | 2-3 | 11:06:42 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.9500 |  |
| Jogador 4 | 2-4 | 11:06:51 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 1.0000 |  |
| Jogador 4 | 2-4 | 11:06:51 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 2-4 | 11:06:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-4 | 11:06:52 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 4 | 2-4 | 11:06:53 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 4 | 2-4 | 11:06:53 | MOVE Bench -> Board: Diana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 2-4 | 11:06:54 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 4 | 2-4 | 11:06:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 2-4 | 11:06:54 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-5 | 11:07:05 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 4 | 2-5 | 11:07:05 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 4 | 2-5 | 11:07:06 | MOVE Board -> Board: Karma (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 4 | 2-5 | 11:07:06 | MOVE Board -> Board: Diana (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 2-5 | 11:07:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-6 | 11:07:21 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 4 | 2-6 | 11:07:21 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 4 | 2-6 | 11:07:22 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4200 |  |
| Jogador 4 | 2-6 | 11:07:22 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.3100 |  |
| Jogador 4 | 2-6 | 11:07:23 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 4 | 2-6 | 11:07:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-6 | 11:07:24 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 4 | 2-6 | 11:07:24 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-6 | 11:07:25 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-7 | 11:07:40 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 2-7 | 11:07:40 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-7 | 11:07:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 11:07:41 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 2-7 | 11:07:42 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-7 | 11:07:42 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 4 | 2-7 | 11:07:43 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.2300 |  |
| Jogador 4 | 2-7 | 11:07:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 11:07:44 | MOVE Board -> Board: Diana (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-1 | 11:08:02 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 4 | 3-1 | 11:08:03 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-1 | 11:08:03 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.5500 |  |
| Jogador 4 | 3-1 | 11:08:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-1 | 11:08:04 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-1 | 11:08:05 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 4 | 3-1 | 11:08:05 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Diana (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 4 | 3-1 | 11:08:06 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Diana (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 4 | 3-1 | 11:08:06 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Diana (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 3-2 | 11:08:24 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 4 | 3-2 | 11:08:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 4 | 3-2 | 11:08:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 3-2 | 11:08:26 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.3500 |  |
| Jogador 4 | 3-2 | 11:08:26 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-2 | 11:08:27 | MOVE Board -> Board: Karma (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-2 | 11:08:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-3 | 11:08:48 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 3-3 | 11:08:48 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 4 | 3-3 | 11:08:49 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 4 | 3-3 | 11:08:49 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-3 | 11:08:50 | MOVE Board -> Board: Yunara (i:8.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-3 | 11:08:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 11:09:15 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-4 | 11:09:16 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 11:09:16 | MOVE Board -> Board: Karma (i:2.0) <-> Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-4 | 11:09:17 | MOVE Board -> Board: Yunara (i:8.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-4 | 11:09:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 11:09:43 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-5 | 11:09:44 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 3-5 | 11:09:44 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 4 | 3-5 | 11:09:45 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 11:09:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 3-5 | 11:09:46 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-5 | 11:09:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 11:10:12 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_18_MasterYi_AD | 0.8300 |  |
| Jogador 4 | 3-6 | 11:10:13 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_18_MasterYi_AD | 0.3500 |  |
| Jogador 4 | 3-6 | 11:10:13 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_MasterYi_AD | 0.2200 |  |
| Jogador 4 | 3-6 | 11:10:14 | MOVE Board -> Board: Karma (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 11:10:14 | MOVE Board -> Board: Yorick (i:2.0) <-> Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 4 | 3-6 | 11:10:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 11:10:43 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_MasterYi_AD | 0.8000 |  |
| Jogador 4 | 3-7 | 11:10:43 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_MasterYi_AD | 0.1600 |  |
| Jogador 4 | 3-7 | 11:10:44 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_MasterYi_AD | 0.2200 |  |
| Jogador 4 | 3-7 | 11:10:44 | VENDEU: Master Yi (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Florescer | DA_18_Yunara | -0.0400 |  |
| Jogador 4 | 3-7 | 11:10:45 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_18_Yunara | -0.0200 |  |
| Jogador 4 | 3-7 | 11:10:46 | MOVE Board -> Board: Yunara (i:8.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 3-7 | 11:10:46 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_18_Yunara | -0.3700 |  |
| Jogador 4 | 3-7 | 11:10:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 4-1 | 11:11:21 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Florescer | DA_18_Yunara | -0.0600 |  |
| Jogador 4 | 4-1 | 11:11:21 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Florescer | DA_18_Yunara | 0.8100 |  |
| Jogador 4 | 4-1 | 11:11:22 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 4-1 | 11:11:22 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Florescer | DA_18_Yunara | 0.7500 |  |
| Jogador 4 | 4-1 | 11:11:23 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Florescer | DA_18_Yunara | -0.0400 |  |
| Jogador 4 | 4-1 | 11:11:23 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Florescer | DA_18_Yunara | 0.2300 |  |
| Jogador 4 | 4-1 | 11:11:24 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 4-1 | 11:11:24 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Florescer | DA_18_Yunara | -0.4200 |  |
| Jogador 4 | 4-1 | 11:11:25 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Florescer | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 4-2 | 11:11:55 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 4-2 | 11:11:56 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Florescer | DA_18_Yunara | 0.8700 |  |
| Jogador 4 | 4-2 | 11:11:56 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Florescer | DA_18_Yunara | 0.2200 |  |
| Jogador 4 | 4-2 | 11:11:57 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Florescer | DA_18_Yunara | 0.1200 |  |
| Jogador 4 | 4-2 | 11:11:57 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Florescer | DA_18_Yunara | -0.7500 |  |
| Jogador 4 | 4-2 | 11:11:58 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 4-2 | 11:11:58 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Florescer | DA_18_Yunara | -0.2000 |  |
| Jogador 4 | 4-2 | 11:11:59 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_18_Yunara | -0.0200 |  |
| Jogador 4 | 4-2 | 11:11:59 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Florescer | DA_18_Yunara | 0.2900 |  |
| Jogador 4 | 4-3 | 11:12:30 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 4-3 | 11:12:31 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_18_Yunara | -0.2400 |  |
| Jogador 4 | 4-3 | 11:12:31 | VENDEU: Sivir (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Florescer | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 4-3 | 11:12:31 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_18_Yunara | -0.0500 |  |
| Jogador 4 | 4-3 | 11:12:32 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Florescer | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 4-3 | 11:12:33 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_18_Yunara | -0.2300 |  |
| Jogador 4 | 4-3 | 11:12:33 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Florescer | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 4-3 | 11:12:34 | MOVE Board -> Board: Sejuani (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Florescer | DA_18_Yunara | 0.0900 |  |
| Jogador 4 | 4-3 | 11:12:34 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Florescer | DA_18_Yunara | -0.0300 |  |
| Jogador 4 | 4-4 | 11:13:08 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Florescer | DA_18_Yunara | 0.1400 |  |
| Jogador 4 | 4-4 | 11:13:08 | MOVE Board -> Board: Karma (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Florescer | DA_18_Yunara | -0.0800 |  |
| Jogador 4 | 4-4 | 11:13:09 | VENDEU: Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Florescer | DA_18_Yunara | -0.0300 |  |
| Jogador 4 | 4-4 | 11:13:09 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_18_Yunara | -0.2300 |  |
| Jogador 4 | 4-4 | 11:13:10 | MOVE Board -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 4-4 | 11:13:11 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 4-4 | 11:13:11 | MOVE Board -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_18_Yunara | 0.0200 |  |
| Jogador 4 | 4-4 | 11:13:13 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_18_Yunara | -0.0200 |  |
| Jogador 4 | 4-4 | 11:13:14 | MOVE Board -> Board: Karma (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 4-5 | 11:13:56 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Florescer | DA_18_Yunara | 0.0900 |  |
| Jogador 4 | 4-5 | 11:13:57 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 3 | Florescer | DA_18_Yunara | 0.8400 |  |
| Jogador 4 | 4-5 | 11:13:57 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 3 | Florescer | DA_18_Yunara | -0.0800 |  |
| Jogador 4 | 4-5 | 11:13:58 | MOVE Bench -> Board: Soraka (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 36 | 3 | Florescer | DA_18_Yunara | 0.4000 |  |
| Jogador 4 | 4-5 | 11:13:59 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 3 | Florescer | DA_18_Yunara | -0.1800 |  |
| Jogador 4 | 4-5 | 11:14:00 | MOVE Board -> Board: Soraka (i:8.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 3 | Florescer | DA_18_Yunara | 0.0300 |  |
| Jogador 4 | 4-5 | 11:14:00 | MOVE Board -> Board: Yorick (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 3 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 4-5 | 11:14:01 | MOVE Board -> Board: Sejuani (i:4.0) <-> Yunara (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 3 | Florescer | DA_18_Yunara | 0.1700 |  |
| Jogador 4 | 4-5 | 11:14:01 | MOVE Board -> Board: Yunara (i:8.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 3 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 4-6 | 11:14:53 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 3 | Florescer | DA_18_Yunara | -0.5100 |  |
| Jogador 4 | 4-6 | 11:14:54 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Karma (i:2.0) (tabuleiro slot 12) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 3 | Florescer | DA_18_Yunara | 0.1400 |  |
| Jogador 4 | 4-6 | 11:14:54 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Yunara (i:8.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 3 | Florescer | DA_18_Yunara | 0.1000 |  |
| Jogador 4 | 4-6 | 11:14:54 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Yunara (i:8.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 52 | 3 | Florescer | DA_18_Yunara | 0.1700 |  |
| Jogador 4 | 4-6 | 11:14:55 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Florescer | DA_18_Yunara | 0.1000 |  |
| Jogador 4 | 4-6 | 11:14:55 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 3 | Florescer | DA_18_Yunara | 0.0600 |  |
| Jogador 4 | 4-6 | 11:14:56 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 47 | 3 | Florescer | DA_18_Yunara | -0.3000 |  |
| Jogador 4 | 4-6 | 11:14:56 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 3 | Florescer | DA_18_Yunara | 0.0900 |  |
| Jogador 4 | 4-6 | 11:14:57 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 48 | 3 | Florescer | DA_18_Yunara | -0.2700 |  |
| Jogador 4 | 4-7 | 11:15:38 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Yunara (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 4 | Florescer | DA_18_Yunara | 0.2400 |  |
| Jogador 4 | 4-7 | 11:15:38 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_TearOfTheGoddess -> Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 4 | Florescer | DA_18_Yunara | 0.0800 |  |
| Jogador 4 | 4-7 | 11:15:39 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 60 | 4 | Florescer | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 4-7 | 11:15:39 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Florescer | DA_18_Yunara | 0.6200 |  |
| Jogador 4 | 4-7 | 11:15:40 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 60 | 4 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 4-7 | 11:15:41 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Florescer | DA_18_Yunara | 0.4200 |  |
| Jogador 4 | 4-7 | 11:15:41 | MOVE Board -> Board: Karma (i:2.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 4 | 4-7 | 11:15:42 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 4 | 4-7 | 11:15:42 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 57 | 4 | Florescer | DA_18_Yunara | -0.4700 |  |
| Jogador 4 | 5-1 | 11:16:24 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Florescer | DA_18_Yunara | -0.1400 |  |
| Jogador 4 | 5-1 | 11:16:25 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 69 | 5 | Florescer | DA_18_Yunara | 1.0900 |  |
| Jogador 4 | 5-1 | 11:16:25 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Florescer | DA_18_Yunara | -0.2200 |  |
| Jogador 4 | 5-1 | 11:16:26 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Florescer | DA_18_Yunara | -0.2700 |  |
| Jogador 4 | 5-1 | 11:16:27 | VENDEU: Kayle (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Florescer | DA_18_Yunara | -0.7100 |  |
| Jogador 4 | 5-1 | 11:16:27 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Florescer | DA_18_Yunara | -0.2400 |  |
| Jogador 4 | 5-1 | 11:16:28 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Florescer | DA_18_Yunara | -0.0700 |  |
| Jogador 4 | 5-1 | 11:16:28 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Florescer | DA_18_Yunara | 0.0100 |  |
| Jogador 4 | 5-1 | 11:16:29 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 63 | 5 | Florescer | DA_18_Yunara | 0.4500 |  |
| Jogador 5 | ? | 11:05:36 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | ? | 11:05:38 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 5 | ? | 11:05:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 11:05:43 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 11:05:43 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 11:05:44 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-1 | 11:05:45 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 11:05:46 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 11:05:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 11:05:48 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4300 |  |
| Jogador 5 | 1-2 | 11:05:50 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 1-2 | 11:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 11:05:58 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 11:05:59 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 11:05:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 11:06:06 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 11:06:08 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 5 | 1-4 | 11:06:09 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 5 | 1-4 | 11:06:09 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 5 | 1-4 | 11:06:10 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 11:06:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 11:06:17 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-1 | 11:06:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 11:06:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 11:06:26 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 5 | 2-2 | 11:06:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 2-2 | 11:06:27 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 5 | 2-2 | 11:06:28 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 11:06:28 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 5 | 2-2 | 11:06:29 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 11:06:29 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0300 |  |
| Jogador 5 | 2-2 | 11:06:29 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-2 | 11:06:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 11:06:38 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.3100 |  |
| Jogador 5 | 2-3 | 11:06:38 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-3 | 11:06:39 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-3 | 11:06:39 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-3 | 11:06:40 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.1700 |  |
| Jogador 5 | 2-3 | 11:06:40 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0800 |  |
| Jogador 5 | 2-3 | 11:06:41 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 11:06:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 11:06:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-4 | 11:06:51 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2900 |  |
| Jogador 5 | 2-4 | 11:06:51 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3400 |  |
| Jogador 5 | 2-4 | 11:06:52 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 2-4 | 11:06:52 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1200 |  |
| Jogador 5 | 2-4 | 11:06:53 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-4 | 11:06:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 11:06:54 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3500 |  |
| Jogador 5 | 2-4 | 11:06:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-4 | 11:06:54 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.4000 |  |
| Jogador 5 | 2-5 | 11:07:05 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3600 |  |
| Jogador 5 | 2-5 | 11:07:05 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0900 |  |
| Jogador 5 | 2-5 | 11:07:06 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 11:07:06 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 11:07:07 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-5 | 11:07:07 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 2-5 | 11:07:08 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.4300 |  |
| Jogador 5 | 2-5 | 11:07:08 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-5 | 11:07:09 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-6 | 11:07:21 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.3500 |  |
| Jogador 5 | 2-6 | 11:07:21 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.9600 |  |
| Jogador 5 | 2-6 | 11:07:22 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.2100 |  |
| Jogador 5 | 2-6 | 11:07:22 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-6 | 11:07:23 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-6 | 11:07:24 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.1100 |  |
| Jogador 5 | 2-6 | 11:07:24 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.4200 |  |
| Jogador 5 | 2-6 | 11:07:24 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.3800 |  |
| Jogador 5 | 2-6 | 11:07:25 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 2-7 | 11:07:40 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Yunara | 0.7500 |  |
| Jogador 5 | 2-7 | 11:07:40 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Yunara | 0.1900 |  |
| Jogador 5 | 2-7 | 11:07:41 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Yunara | 0.1100 |  |
| Jogador 5 | 2-7 | 11:07:41 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Yunara | 0.0300 |  |
| Jogador 5 | 2-7 | 11:07:42 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Tristana | -0.6200 |  |
| Jogador 5 | 2-7 | 11:07:42 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Tristana | -0.2700 |  |
| Jogador 5 | 2-7 | 11:07:43 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 2-7 | 11:07:44 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Tristana | -0.2400 |  |
| Jogador 5 | 2-7 | 11:07:44 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Tristana | -0.3500 |  |
| Jogador 5 | 3-1 | 11:08:02 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_18_Tristana | 0.6900 |  |
| Jogador 5 | 3-1 | 11:08:03 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Tristana | 0.2700 |  |
| Jogador 5 | 3-1 | 11:08:03 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-1 | 11:08:04 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_18_Tristana | -0.1000 |  |
| Jogador 5 | 3-1 | 11:08:04 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_18_Tristana | -0.2400 |  |
| Jogador 5 | 3-1 | 11:08:05 | MOVE Bench -> Board: Tristana (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_18_Tristana | -0.0800 |  |
| Jogador 5 | 3-1 | 11:08:05 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_18_Tristana | -0.5400 |  |
| Jogador 5 | 3-1 | 11:08:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_18_Tristana | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-2 | 11:08:24 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_18_Tristana | 0.7900 |  |
| Jogador 5 | 3-2 | 11:08:25 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_18_Tristana | 0.2800 |  |
| Jogador 5 | 3-2 | 11:08:25 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Enfeitiçador | DA_18_Tristana | 0.2000 |  |
| Jogador 5 | 3-2 | 11:08:26 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Enfeitiçador | DA_18_Tristana | 0.2800 |  |
| Jogador 5 | 3-2 | 11:08:26 | MOVE Bench -> Board: Tristana (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Enfeitiçador | DA_18_Tristana | -0.4100 |  |
| Jogador 5 | 3-2 | 11:08:27 | MOVE Bench -> Board: Karma (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Enfeitiçador | DA_18_Tristana | -0.1800 |  |
| Jogador 5 | 3-2 | 11:08:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-3 | 11:08:48 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 3-3 | 11:08:48 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Enfeitiçador | DA_18_Tristana | 0.8100 |  |
| Jogador 5 | 3-3 | 11:08:49 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Enfeitiçador | DA_18_Tristana | -0.1300 |  |
| Jogador 5 | 3-3 | 11:08:49 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Enfeitiçador | DA_18_Tristana | 0.5900 |  |
| Jogador 5 | 3-3 | 11:08:50 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Enfeitiçador | DA_18_Tristana | -0.4700 |  |
| Jogador 5 | 3-3 | 11:08:50 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 0 | Enfeitiçador | DA_18_Tristana | -0.4900 |  |
| Jogador 5 | 3-3 | 11:08:51 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Enfeitiçador | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 3-3 | 11:08:51 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Enfeitiçador | DA_18_Tristana | 0.2400 |  |
| Jogador 5 | 3-3 | 11:08:52 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 0 | Enfeitiçador | DA_18_Tristana | -0.3200 |  |
| Jogador 5 | 3-4 | 11:09:15 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_18_Tristana | 0.8100 |  |
| Jogador 5 | 3-4 | 11:09:16 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_18_Tristana | 0.3800 |  |
| Jogador 5 | 3-4 | 11:09:16 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Tristana | 0.1200 |  |
| Jogador 5 | 3-4 | 11:09:17 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-4 | 11:09:17 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Tristana | -0.6300 |  |
| Jogador 5 | 3-4 | 11:09:18 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Enfeitiçador | DA_18_Tristana | -0.1900 |  |
| Jogador 5 | 3-4 | 11:09:19 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Enfeitiçador | DA_18_Tristana | 0.0500 |  |
| Jogador 5 | 3-4 | 11:09:19 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Tristana | -0.3600 |  |
| Jogador 5 | 3-4 | 11:09:19 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_18_Tristana | -0.3500 |  |
| Jogador 5 | 3-5 | 11:09:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Enfeitiçador | DA_18_Tristana | 0.1800 |  |
| Jogador 5 | 3-5 | 11:09:44 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-5 | 11:09:44 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Enfeitiçador | DA_18_Tristana | -0.4300 |  |
| Jogador 5 | 3-5 | 11:09:45 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_18_Tristana | 0.0200 |  |
| Jogador 5 | 3-5 | 11:09:45 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Enfeitiçador | DA_18_Tristana | -0.3700 |  |
| Jogador 5 | 3-5 | 11:09:46 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_18_Tristana | -0.2800 |  |
| Jogador 5 | 3-5 | 11:09:46 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Enfeitiçador | DA_18_Tristana | -0.3200 |  |
| Jogador 5 | 3-5 | 11:09:47 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Enfeitiçador | DA_18_Tristana | -0.3600 |  |
| Jogador 5 | 3-5 | 11:09:47 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Enfeitiçador | DA_18_Tristana | -0.1000 |  |
| Jogador 5 | 3-6 | 11:10:12 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 4 | Enfeitiçador | DA_18_Tristana | 0.8500 |  |
| Jogador 5 | 3-6 | 11:10:13 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 4 | Enfeitiçador | DA_18_Tristana | 0.0200 |  |
| Jogador 5 | 3-6 | 11:10:13 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 4 | Enfeitiçador | DA_18_Tristana | -0.2200 |  |
| Jogador 5 | 3-6 | 11:10:14 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 4 | Enfeitiçador | DA_18_Tristana | -0.3400 |  |
| Jogador 5 | 3-6 | 11:10:14 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 4 | Enfeitiçador | DA_18_Tristana | -0.3700 |  |
| Jogador 5 | 3-6 | 11:10:15 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Enfeitiçador | DA_18_Tristana | -0.5400 |  |
| Jogador 5 | 3-6 | 11:10:15 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Enfeitiçador | DA_18_Tristana | -0.9400 |  |
| Jogador 5 | 3-6 | 11:10:16 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Tristana | -0.4900 |  |
| Jogador 5 | 3-6 | 11:10:16 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Enfeitiçador | DA_18_Tristana | -1.0300 |  |
| Jogador 5 | 3-7 | 11:10:43 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Enfeitiçador | DA_18_Tristana | 1.0700 |  |
| Jogador 5 | 3-7 | 11:10:43 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Enfeitiçador | DA_18_Tristana | 0.4500 |  |
| Jogador 5 | 3-7 | 11:10:44 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_18_Tristana | 0.1900 |  |
| Jogador 5 | 3-7 | 11:10:44 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_18_Tristana | 0.1400 |  |
| Jogador 5 | 3-7 | 11:10:45 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_18_Tristana | 0.1700 |  |
| Jogador 5 | 3-7 | 11:10:46 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_18_Tristana | -0.6400 |  |
| Jogador 5 | 3-7 | 11:10:46 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Enfeitiçador | DA_18_Tristana | 0.2300 |  |
| Jogador 5 | 3-7 | 11:10:47 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Enfeitiçador | DA_18_Tristana | -0.4000 |  |
| Jogador 5 | 3-7 | 11:10:48 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Enfeitiçador | DA_18_Tristana | -0.4600 |  |
| Jogador 5 | 4-1 | 11:11:21 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Enfeitiçador | DA_18_Tristana | -0.1000 |  |
| Jogador 5 | 4-1 | 11:11:21 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Enfeitiçador | DA_18_Tristana | 0.1400 |  |
| Jogador 5 | 4-1 | 11:11:22 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Tristana | -0.2200 |  |
| Jogador 5 | 4-1 | 11:11:22 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Enfeitiçador | DA_18_Tristana | 0.4300 |  |
| Jogador 5 | 4-1 | 11:11:23 | MOVE Bench -> Board: Shen (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Enfeitiçador | DA_18_Tristana | -0.5900 |  |
| Jogador 5 | 4-1 | 11:11:23 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Enfeitiçador | DA_18_Tristana | -0.6700 |  |
| Jogador 5 | 4-1 | 11:11:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Enfeitiçador | DA_18_Tristana | -0.2300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-2 | 11:11:55 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Enfeitiçador | DA_18_Tristana | 0.2300 |  |
| Jogador 5 | 4-2 | 11:11:56 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Enfeitiçador | DA_18_Tristana | 0.1200 |  |
| Jogador 5 | 4-2 | 11:11:56 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 4-2 | 11:11:57 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Enfeitiçador | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 4-2 | 11:11:57 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Enfeitiçador | DA_18_Tristana | -0.1300 |  |
| Jogador 5 | 4-2 | 11:11:58 | MOVE Bench -> Board: Tristana (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Enfeitiçador | DA_18_Tristana | 0.0500 |  |
| Jogador 5 | 4-2 | 11:11:58 | MOVE Bench -> Board: Shen (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Enfeitiçador | DA_18_Tristana | -0.6000 |  |
| Jogador 5 | 4-2 | 11:11:59 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Enfeitiçador | DA_18_Tristana | -0.3900 |  |
| Jogador 5 | 4-2 | 11:11:59 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Enfeitiçador | DA_18_Tristana | -0.2600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-3 | 11:12:30 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Enfeitiçador | DA_18_Tristana | 0.9900 |  |
| Jogador 5 | 4-3 | 11:12:31 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Enfeitiçador | DA_18_Tristana | 0.5100 |  |
| Jogador 5 | 4-3 | 11:12:31 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Enfeitiçador | DA_18_Tristana | 0.1200 |  |
| Jogador 5 | 4-3 | 11:12:31 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Enfeitiçador | DA_18_Tristana | 0.1400 |  |
| Jogador 5 | 4-3 | 11:12:32 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Enfeitiçador | DA_18_Tristana | -0.2700 |  |
| Jogador 5 | 4-3 | 11:12:33 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Enfeitiçador | DA_18_Tristana | -0.0700 |  |
| Jogador 5 | 4-3 | 11:12:33 | VENDEU: Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Enfeitiçador | DA_18_Tristana | -0.0500 |  |
| Jogador 5 | 4-3 | 11:12:34 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Enfeitiçador | DA_18_Tristana | 0.9600 |  |
| Jogador 5 | 4-3 | 11:12:34 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Enfeitiçador | DA_18_Tristana | 0.0200 |  |
| Jogador 5 | 4-4 | 11:13:08 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Enfeitiçador | DA_18_Tristana | 0.9600 |  |
| Jogador 5 | 4-4 | 11:13:08 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Enfeitiçador | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 4-4 | 11:13:09 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Enfeitiçador | DA_18_Tristana | 0.0600 |  |
| Jogador 5 | 4-4 | 11:13:09 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Enfeitiçador | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 4-4 | 11:13:10 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Enfeitiçador | DA_18_Tristana | -0.2000 |  |
| Jogador 5 | 4-4 | 11:13:11 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Enfeitiçador | DA_18_Tristana | -0.0700 |  |
| Jogador 5 | 4-4 | 11:13:11 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Enfeitiçador | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 4-4 | 11:13:13 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Enfeitiçador | DA_18_Tristana | 0.1400 |  |
| Jogador 5 | 4-4 | 11:13:14 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Enfeitiçador | DA_18_Tristana | -0.0500 |  |
| Jogador 5 | 4-5 | 11:13:56 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Enfeitiçador | DA_18_Tristana | 0.5300 |  |
| Jogador 5 | 4-5 | 11:13:57 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 4-5 | 11:13:57 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Enfeitiçador | DA_18_Tristana | 0.1300 |  |
| Jogador 5 | 4-5 | 11:13:58 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Enfeitiçador | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 4-5 | 11:13:59 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Enfeitiçador | DA_18_Tristana | 0.0500 |  |
| Jogador 5 | 4-5 | 11:14:00 | MOVE Bench -> Board: Tristana (i:6.0) <-> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Enfeitiçador | DA_18_Tristana | -0.4000 |  |
| Jogador 5 | 4-5 | 11:14:00 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Enfeitiçador | DA_18_Tristana | -0.0700 |  |
| Jogador 5 | 4-5 | 11:14:01 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 4-5 | 11:14:01 | COMPROU: Kobuko (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Enfeitiçador | DA_18_Tristana | 0.6300 |  |
| Jogador 6 | ? | 11:05:36 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 11:05:38 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | -0.1500 |  |
| Jogador 6 | ? | 11:05:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 11:05:43 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 11:05:43 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 11:05:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 11:05:48 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2200 |  |
| Jogador 6 | 1-2 | 11:05:50 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 6 | 1-2 | 11:05:51 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 6 | 1-2 | 11:05:51 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 11:05:52 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 11:05:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-2 | 11:05:55 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.5700 |  |
| Jogador 6 | 1-3 | 11:05:58 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0200 |  |
| Jogador 6 | 1-3 | 11:05:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 11:06:06 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 1-4 | 11:06:08 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 6 | 1-4 | 11:06:09 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 6 | 1-4 | 11:06:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 6 | 1-4 | 11:06:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 11:06:11 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0900 |  |
| Jogador 6 | 2-1 | 11:06:17 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-1 | 11:06:18 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-1 | 11:06:18 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-1 | 11:06:18 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.1500 |  |
| Jogador 6 | 2-1 | 11:06:19 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1000 |  |
| Jogador 6 | 2-1 | 11:06:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 11:06:26 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-2 | 11:06:27 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2100 |  |
| Jogador 6 | 2-2 | 11:06:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.0500 |  |
| Jogador 6 | 2-2 | 11:06:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 11:06:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.9500 |  |
| Jogador 6 | 2-3 | 11:06:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.9400 |  |
| Jogador 6 | 2-3 | 11:06:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-3 | 11:06:39 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.2600 |  |
| Jogador 6 | 2-3 | 11:06:40 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-3 | 11:06:40 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 11:06:41 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-3 | 11:06:41 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-3 | 11:06:42 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | -0.4000 |  |
| Jogador 6 | 2-4 | 11:06:51 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Fumegante | DA_18_Tristana | 0.9300 |  |
| Jogador 6 | 2-4 | 11:06:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Tristana | 0.9800 |  |
| Jogador 6 | 2-4 | 11:06:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-4 | 11:06:52 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | -0.1200 |  |
| Jogador 6 | 2-4 | 11:06:53 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | -1.0200 |  |
| Jogador 6 | 2-4 | 11:06:53 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Tristana | -0.6000 |  |
| Jogador 6 | 2-4 | 11:06:54 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | 0.4000 |  |
| Jogador 6 | 2-4 | 11:06:54 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Tristana | -0.6300 |  |
| Jogador 6 | 2-4 | 11:06:54 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | 0.2300 |  |
| Jogador 6 | 2-5 | 11:07:05 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Fumegante | DA_18_Tristana | 1.1100 |  |
| Jogador 6 | 2-5 | 11:07:05 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Fumegante | DA_18_Tristana | 0.4100 |  |
| Jogador 6 | 2-5 | 11:07:06 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | 0.3100 |  |
| Jogador 6 | 2-5 | 11:07:06 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-5 | 11:07:07 | MOVE Board -> Board: Cascalho (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | 0.0400 |  |
| Jogador 6 | 2-5 | 11:07:07 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | -0.0800 |  |
| Jogador 6 | 2-5 | 11:07:08 | MOVE Board -> Board: Cascalho (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-5 | 11:07:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-6 | 11:07:21 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Fumegante | DA_18_Tristana | 1.0300 |  |
| Jogador 6 | 2-6 | 11:07:21 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Fumegante | DA_18_Tristana | 0.4000 |  |
| Jogador 6 | 2-6 | 11:07:22 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-6 | 11:07:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-6 | 11:07:23 | MOVE Board -> Board: Shen (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-6 | 11:07:24 | MOVE Board -> Board: Cascalho (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-6 | 11:07:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-7 | 11:07:40 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | 0.2700 |  |
| Jogador 6 | 2-7 | 11:07:40 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | 0.2000 |  |
| Jogador 6 | 2-7 | 11:07:41 | VENDEU: Kayle (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Fumegante | DA_18_Tristana | -0.6200 |  |
| Jogador 6 | 2-7 | 11:07:41 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Fumegante | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 2-7 | 11:07:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-7 | 11:07:42 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Tristana | -0.0700 |  |
| Jogador 6 | 2-7 | 11:07:43 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-7 | 11:07:44 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-7 | 11:07:44 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 3-1 | 11:08:02 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Fumegante | DA_18_Tristana | 0.8300 |  |
| Jogador 6 | 3-1 | 11:08:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 3-1 | 11:08:03 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Fumegante | DA_18_Tristana | -0.4800 |  |
| Jogador 6 | 3-1 | 11:08:04 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Xayah (i:2.0) (tabuleiro slot 26) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Fumegante | DA_18_Tristana | 0.1400 |  |
| Jogador 6 | 3-1 | 11:08:04 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Xayah (i:2.0) (tabuleiro slot 26) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Fumegante | DA_18_Tristana | 0.1500 |  |
| Jogador 6 | 3-1 | 11:08:05 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Xayah (i:2.0) (tabuleiro slot 26) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Fumegante | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 3-1 | 11:08:05 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Tristana | 0.2700 |  |
| Jogador 6 | 3-1 | 11:08:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 3-1 | 11:08:06 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | -0.4800 |  |
| Jogador 6 | 3-2 | 11:08:24 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 3-2 | 11:08:25 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 3-2 | 11:08:25 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-2 | 11:08:26 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-2 | 11:08:26 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-2 | 11:08:27 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | -0.0900 |  |
| Jogador 6 | 3-2 | 11:08:27 | MOVE Board -> Board: Tristana (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-2 | 11:08:28 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 3-2 | 11:08:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-3 | 11:08:48 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Fumegante | DA_18_Tristana | 0.2800 |  |
| Jogador 6 | 3-3 | 11:08:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-3 | 11:08:49 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-3 | 11:08:49 | MOVE Board -> Board: Tristana (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-3 | 11:08:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-4 | 11:09:15 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Fumegante | DA_18_Tristana | 0.8000 |  |
| Jogador 6 | 3-4 | 11:09:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 3-4 | 11:09:16 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Fumegante | DA_18_Tristana | -0.0700 |  |
| Jogador 6 | 3-4 | 11:09:17 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-4 | 11:09:17 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Fumegante | DA_18_Tristana | 0.5300 |  |
| Jogador 6 | 3-4 | 11:09:18 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-4 | 11:09:19 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 3-4 | 11:09:19 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-5 | 11:09:43 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Fumegante | DA_18_Tristana | 0.0100 |  |
| Jogador 6 | 3-5 | 11:09:44 | MOVE Board -> Board: Tristana (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Fumegante | DA_18_Tristana | -0.3400 |  |
| Jogador 6 | 3-5 | 11:09:44 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-5 | 11:09:45 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-6 | 11:10:12 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Fumegante | DA_18_Tristana | 0.1200 |  |
| Jogador 6 | 3-6 | 11:10:13 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-6 | 11:10:13 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Fumegante | DA_18_Tristana | 0.0100 |  |
| Jogador 6 | 3-6 | 11:10:14 | COMPROU: Gnar (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Fumegante | DA_18_GnarSmall | -0.0600 |  |
| Jogador 6 | 3-6 | 11:10:14 | MOVE Board -> Board: Shen (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Fumegante | DA_18_GnarSmall | 0.1700 |  |
| Jogador 6 | 3-6 | 11:10:15 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Fumegante | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-6 | 11:10:15 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Fumegante | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-6 | 11:10:16 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Fumegante | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-7 | 11:10:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fumegante | DA_18_GnarSmall | 0.3600 |  |
| Jogador 6 | 3-7 | 11:10:43 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_SparringGloves -> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fumegante | DA_18_GnarSmall | 0.2300 |  |
| Jogador 6 | 3-7 | 11:10:44 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fumegante | DA_18_GnarSmall | 0.1800 |  |
| Jogador 6 | 3-7 | 11:10:44 | MOVE Board -> Board: Xayah (i:2.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fumegante | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-7 | 11:10:45 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fumegante | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-7 | 11:10:46 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fumegante | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-1 | 11:11:21 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Fumegante | DA_18_GnarSmall | 0.4800 |  |
| Jogador 6 | 4-1 | 11:11:21 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fumegante | DA_18_GnarSmall | -0.0300 |  |
| Jogador 6 | 4-1 | 11:11:22 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fumegante | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-1 | 11:11:22 | MOVE Board -> Board: Shen (i:4.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fumegante | DA_18_GnarSmall | -0.1700 |  |
| Jogador 6 | 4-1 | 11:11:23 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fumegante | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-2 | 11:11:55 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Fumegante | DA_18_GnarSmall | 0.2100 |  |
| Jogador 6 | 4-2 | 11:11:56 | MOVE Board -> Board: Xayah (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Fumegante | DA_18_GnarSmall | 0.2600 |  |
| Jogador 6 | 4-2 | 11:11:56 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Fumegante | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 11:11:57 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Fumegante | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 11:11:57 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Fumegante | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-3 | 11:12:30 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Fumegante | DA_18_GnarSmall | 0.0800 |  |
| Jogador 6 | 4-3 | 11:12:31 | VENDEU: Rammus (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 1 | Fumegante | DA_18_GnarSmall | -0.0500 |  |
| Jogador 6 | 4-3 | 11:12:31 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Fumegante | DA_18_GnarSmall | 0.2100 |  |
| Jogador 6 | 4-3 | 11:12:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Fumegante | DA_18_GnarSmall | 0.0300 |  |
| Jogador 6 | 4-3 | 11:12:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Fumegante | DA_18_GnarSmall | 0.0300 |  |
| Jogador 6 | 4-3 | 11:12:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Fumegante | DA_18_GnarSmall | -0.0500 |  |
| Jogador 6 | 4-3 | 11:12:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Fumegante | DA_18_GnarSmall | 0.0300 |  |
| Jogador 6 | 4-3 | 11:12:34 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 1 | Fumegante | DA_18_GnarSmall | -0.0900 |  |
| Jogador 6 | 4-3 | 11:12:34 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 1 | Fumegante | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-4 | 11:13:08 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 0 | Fumegante | DA_18_GnarSmall | -0.0400 |  |
| Jogador 6 | 4-4 | 11:13:08 | COMPROU: Varus (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 0 | Fumegante | DA_18_GnarSmall | 0.7400 |  |
| Jogador 6 | 4-4 | 11:13:09 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 0 | Fumegante | DA_18_GnarSmall | 0.0700 |  |
| Jogador 6 | 4-4 | 11:13:09 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 0 | Fumegante | DA_18_GnarSmall | 0.7300 |  |
| Jogador 6 | 4-4 | 11:13:10 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 0 | Fumegante | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-4 | 11:13:11 | MOVE Board -> Board: Shen (i:4.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 0 | Fumegante | DA_18_GnarSmall | -0.2700 |  |
| Jogador 6 | 4-4 | 11:13:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 0 | Fumegante | DA_18_GnarSmall | -0.0300 |  |
| Jogador 6 | 4-5 | 11:13:56 | VENDEU: Gnar (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Fumegante | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-5 | 11:13:57 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Fumegante | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 6 | 4-5 | 11:13:57 | MOVE Board -> Board: Xayah (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Fumegante | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 6 | 4-5 | 11:13:58 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Fumegante | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 4-5 | 11:13:59 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Fumegante | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 4-6 | 11:14:53 | VENDEU: Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Fumegante | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 4-6 | 11:14:54 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Fumegante | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 6 | 4-6 | 11:14:54 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Fumegante | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 6 | 4-6 | 11:14:54 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Fumegante | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 6 | 4-6 | 11:14:55 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Fumegante | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 6 | 4-6 | 11:14:55 | MOVE Board -> Board: Shen (i:4.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Fumegante | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 6 | 4-6 | 11:14:56 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Fumegante | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 6 | 4-6 | 11:14:56 | MOVE Board -> Board: Tristana (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Fumegante | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-6 | 11:14:57 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Fumegante | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-7 | 11:15:38 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Fumegante | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 6 | 4-7 | 11:15:38 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Fumegante | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 6 | 4-7 | 11:15:39 | VENDEU: Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 58 | 4 | Fumegante | DA_KogMaw18_AD | -0.4200 |  |
| Jogador 6 | 4-7 | 11:15:39 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 4 | Fumegante | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 6 | 4-7 | 11:15:40 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Fumegante | DA_KogMaw18_AD | -0.5900 |  |
| Jogador 6 | 4-7 | 11:15:41 | COMPROU: Aphelios (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Fumegante | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 6 | 4-7 | 11:15:41 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Fumegante | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-7 | 11:15:42 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Fumegante | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 6 | 4-7 | 11:15:42 | MOVE Board -> Board: Shen (i:4.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Fumegante | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 5-1 | 11:16:24 | VENDEU: Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Fumegante | DA_KogMaw18_AD | -0.4900 |  |
| Jogador 6 | 5-1 | 11:16:25 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Fumegante | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 5-1 | 11:16:25 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Fumegante | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 6 | 5-1 | 11:16:26 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Fumegante | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 5-1 | 11:16:27 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Fumegante | DA_KogMaw18_AD | -0.1300 |  |
| Jogador 6 | 5-1 | 11:16:27 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Fumegante | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 6 | 5-2 | 11:17:18 | VENDEU: Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Fumegante | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 6 | 5-2 | 11:17:19 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.9500 |  |
| Jogador 6 | 5-2 | 11:17:19 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Fumegante | DA_CrimsonRaptor18 | 1.0200 |  |
| Jogador 6 | 5-2 | 11:17:20 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Fumegante | DA_CrimsonRaptor18 | 1.0200 |  |
| Jogador 6 | 5-2 | 11:17:20 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.2800 |  |
| Jogador 6 | 5-2 | 11:17:21 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Fumegante | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 6 | 5-2 | 11:17:21 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.4700 |  |
| Jogador 6 | 5-2 | 11:17:22 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.0200 |  |
| Jogador 6 | 5-2 | 11:17:22 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.5300 |  |
| Jogador 6 | 5-3 | 11:18:11 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.4000 |  |
| Jogador 6 | 5-3 | 11:18:11 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Fumegante | DA_CrimsonRaptor18 | -0.1700 |  |
| Jogador 6 | 5-3 | 11:18:12 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Fumegante | DA_CrimsonRaptor18 | -0.2600 |  |
| Jogador 6 | 5-3 | 11:18:14 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.2500 |  |
| Jogador 6 | 5-3 | 11:18:14 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.0300 |  |
| Jogador 6 | 5-3 | 11:18:15 | MOVE Board -> Board: Varus (i:2.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Fumegante | DA_CrimsonRaptor18 | -0.3400 |  |
| Jogador 6 | 5-3 | 11:18:15 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.2700 |  |
| Jogador 6 | 5-3 | 11:18:16 | MOVE Board -> Board: Shen (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Fumegante | DA_CrimsonRaptor18 | -0.2100 |  |
| Jogador 6 | 5-4 | 11:18:42 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 80 | 5 | Fumegante | DA_CrimsonRaptor18 | -0.5900 |  |
| Jogador 6 | 5-4 | 11:18:42 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Fumegante | DA_CrimsonRaptor18 | -0.2300 |  |
| Jogador 6 | 5-4 | 11:18:43 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Kog'Maw (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 6 | 5-4 | 11:18:43 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Kog'Maw (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.1300 |  |
| Jogador 6 | 5-4 | 11:18:44 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Kog'Maw (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 6 | 5-4 | 11:18:44 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Fumegante | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 6 | 5-4 | 11:18:44 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Fumegante | DA_Fiddlesticks18 | 0.3400 |  |
| Jogador 6 | 5-4 | 11:18:45 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Shen (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Fumegante | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 6 | 5-4 | 11:18:45 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Shen (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Fumegante | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 6 | 5-4 | 11:18:46 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Shen (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Fumegante | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 6 | 5-5 | 11:19:32 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Fumegante | DA_KogMaw18_AD | -0.6000 |  |
| Jogador 6 | 5-5 | 11:19:33 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Fumegante | DA_KogMaw18_AD | 0.4200 |  |
| Jogador 6 | 5-5 | 11:19:33 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Tristana (i:6.0) (tabuleiro slot 9) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Fumegante | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 6 | 5-5 | 11:19:34 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Fumegante | DA_KogMaw18_AD | 0.7000 |  |
| Jogador 6 | 5-5 | 11:19:34 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Fumegante | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 6 | 5-5 | 11:19:34 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Fumegante | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 6 | 5-5 | 11:19:35 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Fumegante | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 6 | 5-5 | 11:19:35 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 80 | 5 | Fumegante | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 6 | 5-5 | 11:19:36 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Fumegante | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 6 | 5-6 | 11:20:20 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Fumegante | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 5-6 | 11:20:20 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Fumegante | DA_18_Tristana | 1.0500 |  |
| Jogador 6 | 5-6 | 11:20:21 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Fumegante | DA_18_Tristana | 0.0600 |  |
| Jogador 6 | 5-6 | 11:20:21 | MOVE Bench -> Board: Zyra (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Fumegante | DA_18_Tristana | 0.1700 |  |
| Jogador 6 | 5-6 | 11:20:22 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Fumegante | DA_18_Tristana | 0.0500 |  |
| Jogador 6 | 5-6 | 11:20:22 | MOVE Board -> Board: Zyra (i:8.0) <-> Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Fumegante | DA_18_Tristana | -0.1000 |  |
| Jogador 6 | 5-6 | 11:20:23 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Fumegante | DA_18_Tristana | 0.1500 |  |
| Jogador 6 | 5-6 | 11:20:23 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Fumegante | DA_18_Tristana | -0.1700 |  |
| Jogador 6 | 5-6 | 11:20:24 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Fumegante | DA_18_Tristana | 0.1500 |  |
| Jogador 6 | 5-7 | 11:21:13 | EQUIP_FROM_INVENTORY: DA_18_EmblemSpellweaver -> Mamãe Bicuda (i:6.0) (tabuleiro slot 9) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Fumegante | DA_18_Tristana | 0.0100 |  |
| Jogador 6 | 5-7 | 11:21:13 | VENDEU: Tristana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Fumegante | DA_KogMaw18_AD | -0.6900 |  |
| Jogador 6 | 5-7 | 11:21:14 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Fumegante | DA_KogMaw18_AD | 0.9000 |  |
| Jogador 6 | 5-7 | 11:21:14 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Mamãe Bicuda (i:6.0) (tabuleiro slot 9) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Fumegante | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 6 | 5-7 | 11:21:15 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Fumegante | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 6 | 5-7 | 11:21:15 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 84 | 5 | Fumegante | DA_KogMaw18_AD | 0.5000 |  |
| Jogador 6 | 5-7 | 11:21:16 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Fumegante | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 6 | 5-7 | 11:21:16 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Fumegante | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 6 | 5-7 | 11:21:16 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Fumegante | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 6 | 6-1 | 11:22:10 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Fumegante | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 6 | 6-1 | 11:22:11 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Fumegante | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 6-1 | 11:22:11 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Fumegante | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 6 | 6-1 | 11:22:12 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Fumegante | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 6 | 6-1 | 11:22:12 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Fumegante | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 6 | 6-1 | 11:22:13 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Fumegante | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 6 | 6-1 | 11:22:13 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Fumegante | DA_KogMaw18_AD | 0.7000 |  |
| Jogador 6 | 6-1 | 11:22:14 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Fumegante | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 6 | 6-1 | 11:22:14 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 5 | Fumegante | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 6 | 6-2 | 11:23:03 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Fumegante | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 6-2 | 11:23:03 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 69 | 5 | Fumegante | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 6 | 6-2 | 11:23:04 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Fumegante | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 6 | 6-2 | 11:23:04 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 68 | 5 | Fumegante | DA_18_Zyra | 1.1100 |  |
| Jogador 6 | 6-2 | 11:23:05 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Fumegante | DA_18_Zyra | 1.1000 |  |
| Jogador 6 | 6-2 | 11:23:05 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Fumegante | DA_18_Zyra | 0.2200 |  |
| Jogador 6 | 6-2 | 11:23:05 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Fumegante | DA_18_Zyra | -0.1700 |  |
| Jogador 6 | 6-2 | 11:23:06 | MOVE Bench -> Board: Malphite (i:8.0) <-> Rubrivira (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Fumegante | DA_18_Zyra | -0.0800 |  |
| Jogador 6 | 6-2 | 11:23:06 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Fumegante | DA_18_Zyra | -0.1100 |  |
| Jogador 7 | ? | 11:05:36 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 11:05:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 11:05:43 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 11:05:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 11:05:44 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-1 | 11:05:45 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-1 | 11:05:46 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 11:05:46 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 11:05:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 11:05:48 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 7 | 1-2 | 11:05:50 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 11:05:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 11:05:51 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 11:05:52 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 11:05:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 11:05:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 11:05:58 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-3 | 11:05:59 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-3 | 11:05:59 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 11:06:00 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2000 |  |
| Jogador 7 | 1-3 | 11:06:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 11:06:06 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8300 |  |
| Jogador 7 | 1-4 | 11:06:08 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-4 | 11:06:09 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-4 | 11:06:09 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 7 | 1-4 | 11:06:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 11:06:11 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4400 |  |
| Jogador 7 | 2-1 | 11:06:17 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 11:06:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-1 | 11:06:18 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 11:06:18 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 11:06:19 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 11:06:19 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-1 | 11:06:20 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | -0.6300 |  |
| Jogador 7 | 2-1 | 11:06:20 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 2-1 | 11:06:20 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Varus (i:2.0) (tabuleiro slot 9) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1500 |  |
| Jogador 7 | 2-2 | 11:06:26 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 1.0500 |  |
| Jogador 7 | 2-2 | 11:06:27 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.6500 |  |
| Jogador 7 | 2-2 | 11:06:27 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1700 |  |
| Jogador 7 | 2-2 | 11:06:28 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 11:06:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-3 | 11:06:38 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.3100 |  |
| Jogador 7 | 2-3 | 11:06:38 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 2-3 | 11:06:39 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Sentinel18 | -0.1300 |  |
| Jogador 7 | 2-3 | 11:06:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-3 | 11:06:40 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-3 | 11:06:40 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 2-3 | 11:06:41 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Sentinel18 | -0.1000 |  |
| Jogador 7 | 2-3 | 11:06:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-3 | 11:06:42 | VENDEU: Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Varus | -0.1100 |  |
| Jogador 7 | 2-4 | 11:06:51 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Varus | 0.2700 |  |
| Jogador 7 | 2-4 | 11:06:51 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Varus | 0.3600 |  |
| Jogador 7 | 2-4 | 11:06:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | -0.0600 |  |
| Jogador 7 | 2-4 | 11:06:52 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | -0.6200 |  |
| Jogador 7 | 2-4 | 11:06:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0600 |  |
| Jogador 7 | 2-4 | 11:06:53 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | -0.6300 |  |
| Jogador 7 | 2-4 | 11:06:54 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | -0.7600 |  |
| Jogador 7 | 2-4 | 11:06:54 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0600 |  |
| Jogador 7 | 2-4 | 11:06:54 | MOVE Board -> Board: Varus (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 2-5 | 11:07:05 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.2200 |  |
| Jogador 7 | 2-5 | 11:07:05 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.1700 |  |
| Jogador 7 | 2-5 | 11:07:06 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.1500 |  |
| Jogador 7 | 2-5 | 11:07:06 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 2-5 | 11:07:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 2-5 | 11:07:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 2-6 | 11:07:21 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | -0.0500 |  |
| Jogador 7 | 2-6 | 11:07:21 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.0600 |  |
| Jogador 7 | 2-6 | 11:07:22 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 2-6 | 11:07:22 | MOVE Board -> Board: Rengar (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 2-6 | 11:07:23 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 2-6 | 11:07:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 2-7 | 11:07:40 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.5800 |  |
| Jogador 7 | 2-7 | 11:07:40 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.2600 |  |
| Jogador 7 | 2-7 | 11:07:41 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0300 |  |
| Jogador 7 | 2-7 | 11:07:41 | MOVE Board -> Board: Varus (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.2000 |  |
| Jogador 7 | 2-7 | 11:07:42 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0900 |  |
| Jogador 7 | 2-7 | 11:07:42 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | -0.0400 |  |
| Jogador 7 | 2-7 | 11:07:43 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Varus | -0.0900 |  |
| Jogador 7 | 2-7 | 11:07:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 2-7 | 11:07:44 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 3-1 | 11:08:02 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.2700 |  |
| Jogador 7 | 3-1 | 11:08:03 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.1200 |  |
| Jogador 7 | 3-1 | 11:08:03 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-1 | 11:08:04 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0500 |  |
| Jogador 7 | 3-1 | 11:08:04 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.0100 |  |
| Jogador 7 | 3-1 | 11:08:05 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 3-1 | 11:08:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 3-1 | 11:08:06 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0800 |  |
| Jogador 7 | 3-1 | 11:08:06 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 3-2 | 11:08:24 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Varus | 0.8400 |  |
| Jogador 7 | 3-2 | 11:08:25 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Varus | 0.7400 |  |
| Jogador 7 | 3-2 | 11:08:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | -0.0300 |  |
| Jogador 7 | 3-2 | 11:08:26 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Varus | -0.6300 |  |
| Jogador 7 | 3-2 | 11:08:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0300 |  |
| Jogador 7 | 3-2 | 11:08:27 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | -0.0500 |  |
| Jogador 7 | 3-2 | 11:08:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0300 |  |
| Jogador 7 | 3-2 | 11:08:28 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | -0.2100 |  |
| Jogador 7 | 3-2 | 11:08:28 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Varus | -0.2300 |  |
| Jogador 7 | 3-3 | 11:08:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Varus | 0.7300 |  |
| Jogador 7 | 3-3 | 11:08:48 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Varus | 0.6500 |  |
| Jogador 7 | 3-3 | 11:08:49 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | -0.0300 |  |
| Jogador 7 | 3-3 | 11:08:49 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | -0.4800 |  |
| Jogador 7 | 3-3 | 11:08:50 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.2800 |  |
| Jogador 7 | 3-3 | 11:08:50 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.4200 |  |
| Jogador 7 | 3-3 | 11:08:51 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0600 |  |
| Jogador 7 | 3-3 | 11:08:51 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.1000 |  |
| Jogador 7 | 3-3 | 11:08:52 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0900 |  |
| Jogador 7 | 3-4 | 11:09:15 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Varus | 0.2900 |  |
| Jogador 7 | 3-4 | 11:09:16 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.1100 |  |
| Jogador 7 | 3-4 | 11:09:16 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0400 |  |
| Jogador 7 | 3-4 | 11:09:17 | MOVE Board -> Board: Varus (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.2900 |  |
| Jogador 7 | 3-4 | 11:09:17 | MOVE Board -> Board: Rakan (i:2.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 3-4 | 11:09:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-5 | 11:09:43 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.3800 |  |
| Jogador 7 | 3-5 | 11:09:44 | MOVE Board -> Board: Rengar (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-5 | 11:09:44 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 3-5 | 11:09:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-6 | 11:10:12 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | 0.0100 |  |
| Jogador 7 | 3-6 | 11:10:13 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Varus | 0.7200 |  |
| Jogador 7 | 3-6 | 11:10:13 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | 0.0800 |  |
| Jogador 7 | 3-6 | 11:10:14 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Varus | 0.4900 |  |
| Jogador 7 | 3-6 | 11:10:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | -0.0300 |  |
| Jogador 7 | 3-6 | 11:10:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0300 |  |
| Jogador 7 | 3-6 | 11:10:15 | VENDEU: Rengar (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Varus | -0.1200 |  |
| Jogador 7 | 3-6 | 11:10:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | -0.0300 |  |
| Jogador 7 | 3-6 | 11:10:16 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Varus (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.1500 |  |
| Jogador 7 | 3-7 | 11:10:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Varus | 0.1700 |  |
| Jogador 7 | 3-7 | 11:10:43 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Varus | 0.2100 |  |
| Jogador 7 | 3-7 | 11:10:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Varus | -0.1100 |  |
| Jogador 7 | 3-7 | 11:10:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | -0.0300 |  |
| Jogador 7 | 3-7 | 11:10:45 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | -0.0700 |  |
| Jogador 7 | 3-7 | 11:10:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0300 |  |
| Jogador 7 | 3-7 | 11:10:46 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.1000 |  |
| Jogador 7 | 3-7 | 11:10:47 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 3-7 | 11:10:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-1 | 11:11:21 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Varus | 0.2700 |  |
| Jogador 7 | 4-1 | 11:11:21 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-1 | 11:11:22 | MOVE Board -> Board: Rakan (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.0400 |  |
| Jogador 7 | 4-1 | 11:11:22 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-1 | 11:11:23 | MOVE Board -> Board: Hecarim (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-1 | 11:11:23 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-2 | 11:11:55 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | -0.1700 |  |
| Jogador 7 | 4-2 | 11:11:56 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-2 | 11:11:56 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | -0.0300 |  |
| Jogador 7 | 4-2 | 11:11:57 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.3100 |  |
| Jogador 7 | 4-2 | 11:11:57 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-2 | 11:11:58 | MOVE Board -> Board: Rakan (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-2 | 11:11:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-3 | 11:12:30 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Varus | 0.0700 |  |
| Jogador 7 | 4-3 | 11:12:31 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Varus | 0.7200 |  |
| Jogador 7 | 4-3 | 11:12:31 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-3 | 11:12:31 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Varus | 0.2700 |  |
| Jogador 7 | 4-3 | 11:12:32 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-3 | 11:12:33 | MOVE Board -> Board: Hecarim (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-3 | 11:12:33 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-3 | 11:12:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-4 | 11:13:08 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Varus | -0.0400 |  |
| Jogador 7 | 4-4 | 11:13:08 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | 0.1700 |  |
| Jogador 7 | 4-4 | 11:13:09 | MOVE Board -> Board: Rakan (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-4 | 11:13:09 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-4 | 11:13:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-5 | 11:13:56 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-5 | 11:13:57 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Varus | 0.8700 |  |
| Jogador 7 | 4-5 | 11:13:57 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_18_Varus | -0.5800 |  |
| Jogador 7 | 4-5 | 11:13:58 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_KogMaw18_AD | 0.8500 |  |
| Jogador 7 | 4-5 | 11:13:59 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 7 | 4-5 | 11:14:00 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 7 | 4-5 | 11:14:00 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Varus (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 4-5 | 11:14:01 | MOVE Bench -> Board: Kog'Maw (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Colosso | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 7 | 4-5 | 11:14:01 | EQUIP_FROM_INVENTORY: TFT_Item_RunaansHurricane -> Aronguejo (i:4.0) (tabuleiro slot 9) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 4-6 | 11:14:53 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Colosso | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 7 | 4-6 | 11:14:54 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Colosso | DA_KogMaw18_AD | 0.8800 |  |
| Jogador 7 | 4-6 | 11:14:54 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Colosso | DA_KogMaw18_AD | 0.5500 |  |
| Jogador 7 | 4-6 | 11:14:54 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Colosso | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 7 | 4-6 | 11:14:55 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Camille (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 4-6 | 11:14:55 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Colosso | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 7 | 4-6 | 11:14:56 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-6 | 11:14:56 | VENDEU: Hecarim (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 7 | 4-6 | 11:14:57 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Colosso | DA_KogMaw18_AD | -0.4300 |  |
| Jogador 7 | 4-7 | 11:15:38 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 7 | 4-7 | 11:15:38 | COMPROU: Ashe (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Colosso | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 7 | 4-7 | 11:15:39 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 4-7 | 11:15:39 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_TearOfTheGoddess -> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Colosso | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 7 | 4-7 | 11:15:40 | MOVE Bench -> Board: Ashe (i:10.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Colosso | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 7 | 4-7 | 11:15:41 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 3 | Colosso | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 7 | 4-7 | 11:15:41 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 3 | Colosso | DA_KogMaw18_AD | -0.3100 |  |
| Jogador 7 | 4-7 | 11:15:42 | MOVE Board -> Board: Ashe (i:10.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-7 | 11:15:42 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 3 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-1 | 11:16:24 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Colosso | DA_KogMaw18_AD | 0.5900 |  |
| Jogador 7 | 5-1 | 11:16:25 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 3 | Colosso | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 7 | 5-1 | 11:16:25 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 3 | Colosso | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 7 | 5-1 | 11:16:26 | MOVE Board -> Board: Grompe (i:4.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-1 | 11:16:27 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Ashe (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 3 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-1 | 11:16:27 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 3 | Colosso | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 7 | 5-2 | 11:17:18 | MOVE Board -> Board: Ashe (i:10.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-2 | 11:17:19 | MOVE Board -> Board: Camille (i:2.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Fera do Rift | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 7 | 5-2 | 11:17:19 | MOVE Board -> Board: Grompe (i:4.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Fera do Rift | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-2 | 11:17:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Fera do Rift | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 7 | 5-3 | 11:18:11 | VENDEU: Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Fera do Rift | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 5-3 | 11:18:11 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Fera do Rift | DA_KogMaw18_AD | 0.2600 |  |
| Jogador 7 | 5-3 | 11:18:12 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Ashe (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Fera do Rift | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 7 | 5-3 | 11:18:14 | MOVE Board -> Board: Ashe (i:10.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Fera do Rift | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-3 | 11:18:14 | VENDEU: Caitlyn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Fera do Rift | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-3 | 11:18:15 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Fera do Rift | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 7 | 5-3 | 11:18:15 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-3 | 11:18:16 | MOVE Board -> Board: Grompe (i:4.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Fera do Rift | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 5-4 | 11:18:42 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 58 | 4 | Fera do Rift | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 5-4 | 11:18:42 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Fera do Rift | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 7 | 5-4 | 11:18:43 | MOVE Board -> Board: Camille (i:2.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-4 | 11:18:43 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Ashe (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Fera do Rift | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 5-4 | 11:18:44 | MOVE Board -> Board: Ashe (i:10.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Fera do Rift | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-4 | 11:18:44 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Fera do Rift | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 7 | 5-5 | 11:19:32 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 7 | 5-5 | 11:19:33 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 7 | 5-5 | 11:19:33 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 5-5 | 11:19:34 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 7 | 5-5 | 11:19:34 | MOVE Board -> Board: Ashe (i:10.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-5 | 11:19:34 | MOVE Board -> Board: Grompe (i:4.0) <-> Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.1800 |  |
| Jogador 7 | 5-5 | 11:19:35 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 7 | 5-6 | 11:20:20 | VENDEU: Master Yi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 82 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 7 | 5-6 | 11:20:20 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 79 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.9300 |  |
| Jogador 7 | 5-6 | 11:20:21 | VENDEU: Krugue (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 82 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 7 | 5-6 | 11:20:21 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 80 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.4300 |  |
| Jogador 7 | 5-6 | 11:20:22 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 80 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.5000 |  |
| Jogador 7 | 5-6 | 11:20:22 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 7 | 5-6 | 11:20:23 | MOVE Board -> Board: Akali (i:2.0) <-> Grompe (i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 7 | 5-6 | 11:20:23 | MOVE Board -> Board: Grompe (i:4.0) <-> Ashe (i:10.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 7 | 5-6 | 11:20:24 | MOVE Board -> Board: Ashe (i:10.0) <-> Mamãe Bicuda (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 76 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 7 | 5-7 | 11:21:13 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Akali (i:2.0) (tabuleiro slot 19) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 86 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 7 | 5-7 | 11:21:13 | VENDEU: Nidalee (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 90 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 7 | 5-7 | 11:21:14 | COMPROU: Grompe (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 88 | 5 | Fera do Rift | DA_KogMaw18_AD | 1.0600 |  |
| Jogador 7 | 5-7 | 11:21:14 | COMPROU: Soraka (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.1400 |  |
| Jogador 7 | 5-7 | 11:21:15 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-7 | 11:21:15 | MOVE Bench -> Board: Grompe (i:8.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 84 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.5800 |  |
| Jogador 7 | 5-7 | 11:21:16 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 81 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.2200 |  |
| Jogador 7 | 5-7 | 11:21:16 | MOVE Board -> Board: Grompe (i:8.0) <-> Camille (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 81 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-7 | 11:21:16 | MOVE Board -> Board: Camille (i:2.0) <-> Kog'Maw (i:12.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 81 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 6-1 | 11:22:10 | VENDEU: Kha'Zix (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 96 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 6-1 | 11:22:11 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 94 | 5 | Fera do Rift | DA_KogMaw18_AD | 1.0100 |  |
| Jogador 7 | 6-1 | 11:22:11 | VENDEU: Soraka (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 98 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 6-1 | 11:22:12 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 94 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 6-1 | 11:22:12 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Akali (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 94 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 6-1 | 11:22:13 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 94 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 6-1 | 11:22:13 | MOVE Board -> Board: Akali (i:2.0) <-> Kog'Maw (i:12.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 94 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 6-1 | 11:22:14 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 94 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 7 | 6-2 | 11:23:03 | VENDEU: Nidalee (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 7 | 6-2 | 11:23:03 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Fera do Rift | DA_KogMaw18_AD | 1.1100 |  |
| Jogador 7 | 6-2 | 11:23:04 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.5100 |  |
| Jogador 7 | 6-2 | 11:23:04 | VENDEU: Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.6900 |  |
| Jogador 7 | 6-2 | 11:23:05 | COMPROU: Camille (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.8700 |  |
| Jogador 7 | 6-2 | 11:23:05 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 7 | 6-2 | 11:23:05 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Akali (i:2.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 7 | 6-2 | 11:23:06 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Akali (i:2.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 7 | 6-2 | 11:23:06 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 6-3 | 11:23:56 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Fera do Rift | DA_KogMaw18_AD | 1.0100 |  |
| Jogador 7 | 6-3 | 11:23:57 | VENDEU: Camille (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 7 | 6-3 | 11:23:57 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.1700 |  |
| Jogador 7 | 6-3 | 11:23:58 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Aronguejo (i:4.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 6-3 | 11:23:58 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 6-3 | 11:23:58 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 6-3 | 11:23:59 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 6-3 | 11:23:59 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 7 | 6-4 | 11:25:00 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.6400 |  |
| Jogador 7 | 6-4 | 11:25:00 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.5100 |  |
| Jogador 7 | 6-4 | 11:25:00 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.4700 |  |
| Jogador 7 | 6-4 | 11:25:01 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 6-4 | 11:25:01 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.4100 |  |
| Jogador 7 | 6-4 | 11:25:02 | MOVE Board -> Board: Malphite (i:8.0) <-> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 6-4 | 11:25:02 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Kog'Maw (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 6-4 | 11:25:02 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.5500 |  |
| Jogador 7 | 6-5 | 11:25:53 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 7 | 6-5 | 11:25:54 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.4500 |  |
| Jogador 7 | 6-5 | 11:25:54 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.1400 |  |
| Jogador 7 | 6-5 | 11:25:55 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.2300 |  |
| Jogador 7 | 6-5 | 11:25:55 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 6-5 | 11:25:55 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.2300 |  |
| Jogador 7 | 6-5 | 11:25:56 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Ashe (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Fera do Rift | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 6-5 | 11:25:56 | MOVE Board -> Board: Ashe (i:10.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 6-5 | 11:25:57 | MOVE Board -> Board: Akali (i:2.0) <-> Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Fera do Rift | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 8 | ? | 11:05:36 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | ? | 11:05:38 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | ? | 11:05:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 11:05:43 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 11:05:43 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-1 | 11:05:44 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-1 | 11:05:45 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3600 |  |
| Jogador 8 | 1-1 | 11:05:46 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-1 | 11:05:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 11:05:48 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5000 |  |
| Jogador 8 | 1-2 | 11:05:50 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 8 | 1-2 | 11:05:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 8 | 1-2 | 11:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 11:05:58 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-3 | 11:05:59 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 8 | 1-3 | 11:05:59 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1700 |  |
| Jogador 8 | 1-3 | 11:06:00 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 8 | 1-3 | 11:06:02 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 8 | 1-3 | 11:06:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 11:06:06 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.1100 |  |
| Jogador 8 | 1-4 | 11:06:08 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 1-4 | 11:06:09 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 1-4 | 11:06:09 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 1-4 | 11:06:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 1.1000 |  |
| Jogador 8 | 1-4 | 11:06:10 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 1-4 | 11:06:11 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 1-4 | 11:06:11 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.3200 |  |
| Jogador 8 | 1-4 | 11:06:11 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 1-4 | 11:06:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-1 | 11:06:17 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-1 | 11:06:18 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.3000 |  |
| Jogador 8 | 2-1 | 11:06:18 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | -0.2100 |  |
| Jogador 8 | 2-1 | 11:06:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-1 | 11:06:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-2 | 11:06:26 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | 1.0500 |  |
| Jogador 8 | 2-2 | 11:06:27 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2300 |  |
| Jogador 8 | 2-2 | 11:06:27 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-2 | 11:06:28 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2500 |  |
| Jogador 8 | 2-2 | 11:06:28 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | -0.4300 |  |
| Jogador 8 | 2-2 | 11:06:29 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | -0.1300 |  |
| Jogador 8 | 2-2 | 11:06:29 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1700 |  |
| Jogador 8 | 2-2 | 11:06:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-2 | 11:06:30 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.6300 |  |
| Jogador 8 | 2-3 | 11:06:38 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | 0.8200 |  |
| Jogador 8 | 2-3 | 11:06:38 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2900 |  |
| Jogador 8 | 2-3 | 11:06:39 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1700 |  |
| Jogador 8 | 2-3 | 11:06:39 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | -0.1300 |  |
| Jogador 8 | 2-3 | 11:06:40 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 2-3 | 11:06:40 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-3 | 11:06:41 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 2-3 | 11:06:41 | MOVE Board -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-3 | 11:06:42 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Karma18 | -0.1100 |  |
| Jogador 8 | 2-4 | 11:06:51 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_Karma18 | 0.9600 |  |
| Jogador 8 | 2-4 | 11:06:51 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | 0.3800 |  |
| Jogador 8 | 2-4 | 11:06:52 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-4 | 11:06:52 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_Karma18 | -0.5500 |  |
| Jogador 8 | 2-4 | 11:06:53 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_Karma18 | -0.5000 |  |
| Jogador 8 | 2-4 | 11:06:53 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Enfeitiçador | DA_Karma18 | -0.8400 |  |
| Jogador 8 | 2-4 | 11:06:54 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Enfeitiçador | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 2-4 | 11:06:54 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-4 | 11:06:54 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_Karma18 | -0.3100 |  |
| Jogador 8 | 2-5 | 11:07:05 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Espinhos Negros | DA_Karma18 | 0.9600 |  |
| Jogador 8 | 2-5 | 11:07:05 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Espinhos Negros | DA_Karma18 | 0.3600 |  |
| Jogador 8 | 2-5 | 11:07:06 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Espinhos Negros | DA_Karma18 | 0.3600 |  |
| Jogador 8 | 2-5 | 11:07:06 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_18_Diana | -0.6300 |  |
| Jogador 8 | 2-5 | 11:07:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Espinhos Negros | DA_18_Diana | -0.0400 |  |
| Jogador 8 | 2-5 | 11:07:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Espinhos Negros | DA_18_Diana | -0.0400 |  |
| Jogador 8 | 2-5 | 11:07:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 1 | Espinhos Negros | DA_18_Diana | -0.0700 |  |
| Jogador 8 | 2-5 | 11:07:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Espinhos Negros | DA_18_Diana | -0.0600 |  |
| Jogador 8 | 2-5 | 11:07:09 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 1 | Espinhos Negros | DA_18_Diana | -0.6100 |  |
| Jogador 8 | 2-6 | 11:07:21 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Diana | 0.3600 |  |
| Jogador 8 | 2-6 | 11:07:21 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Diana | 0.2800 |  |
| Jogador 8 | 2-6 | 11:07:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Diana | -0.0600 |  |
| Jogador 8 | 2-6 | 11:07:22 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Diana | -0.1500 |  |
| Jogador 8 | 2-6 | 11:07:23 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Diana | -0.6300 |  |
| Jogador 8 | 2-6 | 11:07:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Diana | -0.0600 |  |
| Jogador 8 | 2-6 | 11:07:24 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Warwick | -0.6300 |  |
| Jogador 8 | 2-6 | 11:07:24 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Warwick | -1.0200 |  |
| Jogador 8 | 2-6 | 11:07:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Warwick | -0.0600 |  |
| Jogador 8 | 2-7 | 11:07:40 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Warwick | 0.5600 |  |
| Jogador 8 | 2-7 | 11:07:40 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Warwick | 0.2000 |  |
| Jogador 8 | 2-7 | 11:07:41 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Warwick | 0.2500 |  |
| Jogador 8 | 2-7 | 11:07:41 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Warwick | -0.1400 |  |
| Jogador 8 | 2-7 | 11:07:42 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Warwick | -0.5400 |  |
| Jogador 8 | 2-7 | 11:07:42 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Lillia | 0.1000 |  |
| Jogador 8 | 2-7 | 11:07:43 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Lillia | 0.5800 |  |
| Jogador 8 | 2-7 | 11:07:44 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_18_Lillia | -0.0200 |  |
| Jogador 8 | 2-7 | 11:07:44 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Warwick | -0.0600 |  |
| Jogador 8 | 3-1 | 11:08:02 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 3-1 | 11:08:03 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_Brambleback18 | 0.1500 |  |
| Jogador 8 | 3-1 | 11:08:03 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_Brambleback18 | 0.0100 |  |
| Jogador 8 | 3-1 | 11:08:04 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_Brambleback18 | -0.4200 |  |
| Jogador 8 | 3-1 | 11:08:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_Brambleback18 | -0.0100 |  |
| Jogador 8 | 3-1 | 11:08:05 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_Brambleback18 | -0.0800 |  |
| Jogador 8 | 3-1 | 11:08:05 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_Brambleback18 | -0.0800 |  |
| Jogador 8 | 3-1 | 11:08:06 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_Brambleback18 | -0.0600 |  |
| Jogador 8 | 3-1 | 11:08:06 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Warwick | -0.1000 |  |
| Jogador 8 | 3-2 | 11:08:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_18_Warwick | 0.1400 |  |
| Jogador 8 | 3-2 | 11:08:25 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Warwick | -0.1400 |  |
| Jogador 8 | 3-2 | 11:08:25 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Warwick | -0.0600 |  |
| Jogador 8 | 3-2 | 11:08:26 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Warwick | -0.4200 |  |
| Jogador 8 | 3-2 | 11:08:26 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Espinhos Negros | DA_18_Warwick | -0.3500 |  |
| Jogador 8 | 3-2 | 11:08:27 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Warwick | -0.0100 |  |
| Jogador 8 | 3-2 | 11:08:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Warwick | -0.0100 |  |
| Jogador 8 | 3-2 | 11:08:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Warwick | 0.0600 |  |
| Jogador 8 | 3-2 | 11:08:28 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Warwick | 0.4000 |  |
| Jogador 8 | 3-3 | 11:08:48 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0800 |  |
| Jogador 8 | 3-3 | 11:08:48 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.5600 |  |
| Jogador 8 | 3-3 | 11:08:49 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 8 | 3-3 | 11:08:49 | MOVE Board -> Board: Warwick (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 8 | 3-3 | 11:08:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 8 | 3-4 | 11:09:15 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.2000 |  |
| Jogador 8 | 3-4 | 11:09:16 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.2400 |  |
| Jogador 8 | 3-4 | 11:09:16 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 8 | 3-4 | 11:09:17 | MOVE Board -> Board: Rakan (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 8 | 3-4 | 11:09:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 8 | 3-5 | 11:09:43 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.2800 |  |
| Jogador 8 | 3-5 | 11:09:44 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.2800 |  |
| Jogador 8 | 3-5 | 11:09:44 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 8 | 3-5 | 11:09:45 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0400 |  |
| Jogador 8 | 3-5 | 11:09:45 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.1300 |  |
| Jogador 8 | 3-5 | 11:09:46 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0300 |  |
| Jogador 8 | 3-5 | 11:09:46 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 8 | 3-5 | 11:09:47 | VENDEU: Malphite (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.1500 |  |
| Jogador 8 | 3-5 | 11:09:47 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.5000 |  |
| Jogador 8 | 3-6 | 11:10:12 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.2800 |  |
| Jogador 8 | 3-6 | 11:10:13 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 8 | 3-6 | 11:10:13 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0400 |  |
| Jogador 8 | 3-6 | 11:10:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 8 | 3-6 | 11:10:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 8 | 3-6 | 11:10:15 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 8 | 3-6 | 11:10:15 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.3600 |  |
| Jogador 8 | 3-6 | 11:10:16 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 8 | 3-6 | 11:10:16 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 1 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 8 | 3-7 | 11:10:43 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.8400 |  |
| Jogador 8 | 3-7 | 11:10:43 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.2000 |  |
| Jogador 8 | 3-7 | 11:10:44 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.2800 |  |
| Jogador 8 | 3-7 | 11:10:44 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.2900 |  |
| Jogador 8 | 3-7 | 11:10:45 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_SparringGloves -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.2200 |  |
| Jogador 8 | 3-7 | 11:10:46 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.1700 |  |
| Jogador 8 | 3-7 | 11:10:46 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 8 | 3-7 | 11:10:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 8 | 3-7 | 11:10:48 | MOVE Board -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 8 | 4-1 | 11:11:21 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 8 | 4-1 | 11:11:21 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_CrimsonRaptor18 | 0.0400 |  |
| Jogador 8 | 4-1 | 11:11:22 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_18_Azir | 0.0800 |  |
| Jogador 8 | 4-1 | 11:11:22 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Azir | -0.3000 |  |
| Jogador 8 | 4-1 | 11:11:23 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Azir | 0.0600 |  |
| Jogador 8 | 4-1 | 11:11:23 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Azir | -0.0500 |  |
| Jogador 8 | 4-1 | 11:11:24 | MOVE Board -> Board: Rakan (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Azir | 0.0000 |  |
| Jogador 8 | 4-1 | 11:11:24 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Azir | -0.0100 |  |
| Jogador 8 | 4-1 | 11:11:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Azir | 0.0000 |  |
| Jogador 8 | 4-2 | 11:11:55 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Espinhos Negros | DA_18_Azir | -0.0200 |  |
| Jogador 8 | 4-2 | 11:11:56 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Espinhos Negros | DA_18_Azir | 0.8000 |  |
| Jogador 8 | 4-2 | 11:11:56 | VENDEU: Sivir (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Espinhos Negros | DA_18_Azir | 0.0100 |  |
| Jogador 8 | 4-2 | 11:11:57 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Espinhos Negros | DA_18_Azir | 0.7000 |  |
| Jogador 8 | 4-2 | 11:11:57 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Espinhos Negros | DA_18_Azir | 0.0000 |  |
| Jogador 8 | 4-2 | 11:11:58 | MOVE Board -> Board: Veigar (i:2.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Espinhos Negros | DA_18_Azir | -0.0300 |  |
| Jogador 8 | 4-2 | 11:11:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Espinhos Negros | DA_18_Azir | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 4-3 | 11:12:30 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Espinhos Negros | DA_18_Azir | -0.5000 |  |
| Jogador 8 | 4-3 | 11:12:31 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Espinhos Negros | DA_18_Azir | 0.8100 |  |
| Jogador 8 | 4-3 | 11:12:31 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Espinhos Negros | DA_18_Azir | -0.5700 |  |
| Jogador 8 | 4-3 | 11:12:31 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_18_Azir | 0.0400 |  |
| Jogador 8 | 4-3 | 11:12:32 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Espinhos Negros | DA_18_Azir | -0.0100 |  |
| Jogador 8 | 4-3 | 11:12:33 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_18_Azir | 0.0400 |  |
| Jogador 8 | 4-3 | 11:12:33 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_18_Azir | -0.2800 |  |
| Jogador 8 | 4-3 | 11:12:34 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_18_Azir | 0.0700 |  |
| Jogador 8 | 4-3 | 11:12:34 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Espinhos Negros | DA_18_Azir | 0.7400 |  |
| Jogador 8 | 4-4 | 11:13:08 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Espinhos Negros | DA_18_Diana | -0.5800 |  |
| Jogador 8 | 4-4 | 11:13:08 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Espinhos Negros | DA_Fiddlesticks18 | 0.8600 |  |
| Jogador 8 | 4-4 | 11:13:09 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 8 | 4-4 | 11:13:09 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 8 | 4-4 | 11:13:10 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Espinhos Negros | DA_18_Diana | -0.4900 |  |
| Jogador 8 | 4-4 | 11:13:11 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Espinhos Negros | DA_18_Diana | 0.5200 |  |
| Jogador 8 | 4-4 | 11:13:11 | MOVE Board -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Espinhos Negros | DA_18_Diana | 0.0200 |  |
| Jogador 8 | 4-4 | 11:13:13 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Espinhos Negros | DA_18_Diana | -0.0100 |  |
| Jogador 8 | 4-4 | 11:13:14 | MOVE Board -> Board: Rakan (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Espinhos Negros | DA_18_Diana | -0.0200 |  |
| Jogador 8 | 4-5 | 11:13:56 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Espinhos Negros | DA_18_Diana | 0.0100 |  |
| Jogador 8 | 4-5 | 11:13:57 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Espinhos Negros | DA_18_Diana | -0.2600 |  |
| Jogador 8 | 4-5 | 11:13:57 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Espinhos Negros | DA_18_Diana | 0.0100 |  |
| Jogador 8 | 4-5 | 11:13:58 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 33 | 2 | Espinhos Negros | DA_18_Diana | -0.2200 |  |
| Jogador 8 | 4-5 | 11:13:59 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Espinhos Negros | DA_18_Diana | 0.0100 |  |
| Jogador 8 | 4-5 | 11:14:00 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Espinhos Negros | DA_18_Diana | -0.2700 |  |
| Jogador 8 | 4-5 | 11:14:00 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Espinhos Negros | DA_18_Diana | 0.0300 |  |
| Jogador 8 | 4-5 | 11:14:01 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Espinhos Negros | DA_18_Diana | -0.2700 |  |
| Jogador 8 | 4-5 | 11:14:01 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Espinhos Negros | DA_18_Diana | 0.0000 |  |
| Jogador 8 | 4-6 | 11:14:53 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 44 | 3 | Espinhos Negros | DA_18_Diana | 0.0300 |  |
| Jogador 8 | 4-6 | 11:14:54 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Espinhos Negros | DA_18_Diana | 0.8200 |  |
| Jogador 8 | 4-6 | 11:14:54 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Espinhos Negros | DA_18_Diana | 0.1200 |  |
| Jogador 8 | 4-6 | 11:14:54 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Espinhos Negros | DA_18_Diana | 0.1500 |  |
| Jogador 8 | 4-6 | 11:14:55 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 33 | 3 | Espinhos Negros | DA_18_Diana | -0.0700 |  |
| Jogador 8 | 4-6 | 11:14:55 | VENDEU: Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Espinhos Negros | DA_18_Diana | -0.6700 |  |
| Jogador 8 | 4-6 | 11:14:56 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 35 | 3 | Espinhos Negros | DA_18_Diana | 0.9400 |  |
| Jogador 8 | 4-6 | 11:14:56 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 32 | 3 | Espinhos Negros | DA_18_Diana | -0.0100 |  |
| Jogador 8 | 4-6 | 11:14:57 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 29 | 3 | Espinhos Negros | DA_18_Diana | -0.2900 |  |
| Jogador 8 | 4-7 | 11:15:38 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Espinhos Negros | DA_18_Diana | 0.1200 |  |
| Jogador 8 | 4-7 | 11:15:38 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NegatronCloak -> Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 2 | Espinhos Negros | DA_18_Diana | 0.1000 |  |
| Jogador 8 | 4-7 | 11:15:39 | VENDEU: Diana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 45 | 2 | Espinhos Negros | DA_Brambleback18 | -0.5800 |  |
| Jogador 8 | 4-7 | 11:15:39 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 2 | Espinhos Negros | DA_Brambleback18 | 0.3000 |  |
| Jogador 8 | 4-7 | 11:15:40 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 45 | 2 | Espinhos Negros | DA_Brambleback18 | 0.0100 |  |
| Jogador 8 | 4-7 | 11:15:41 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 42 | 2 | Espinhos Negros | DA_Brambleback18 | 0.3600 |  |
| Jogador 8 | 4-7 | 11:15:41 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 45 | 2 | Espinhos Negros | DA_Brambleback18 | -0.0100 |  |
| Jogador 8 | 4-7 | 11:15:42 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 2 | Espinhos Negros | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 4-7 | 11:15:42 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 41 | 2 | Espinhos Negros | DA_Brambleback18 | -0.0700 |  |
| Jogador 8 | 5-1 | 11:16:24 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Espinhos Negros | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 5-1 | 11:16:25 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 4 | Espinhos Negros | DA_Brambleback18 | 1.0700 |  |
| Jogador 8 | 5-1 | 11:16:25 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Espinhos Negros | DA_Brambleback18 | 1.0700 |  |
| Jogador 8 | 5-1 | 11:16:26 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Espinhos Negros | DA_Brambleback18 | 0.2300 |  |
| Jogador 8 | 5-1 | 11:16:27 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Espinhos Negros | DA_Brambleback18 | 0.3300 |  |
| Jogador 8 | 5-1 | 11:16:27 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Teemo (i:4.0) (tabuleiro slot 12) | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Espinhos Negros | DA_Brambleback18 | 0.0600 |  |
| Jogador 8 | 5-1 | 11:16:28 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 50 | 4 | Espinhos Negros | DA_Brambleback18 | 0.0000 |  |
| Jogador 8 | 5-1 | 11:16:28 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 47 | 4 | Espinhos Negros | DA_Brambleback18 | -0.2900 |  |
| Jogador 8 | 5-1 | 11:16:29 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 47 | 4 | Espinhos Negros | DA_Brambleback18 | 0.4000 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 24 | 25 | 125 | 24 | 15 | 186 | 7 | 18 |
| Jogador 2 | 38 | 41 | 205 | 38 | 17 | 303 | 6 | 41 |
| Jogador 3 | 33 | 34 | 170 | 33 | 17 | 228 | 7 | 29 |
| Jogador 4 | 27 | 29 | 145 | 27 | 16 | 197 | 6 | 26 |
| Jogador 5 | 24 | 27 | 135 | 24 | 15 | 181 | 8 | 22 |
| Jogador 6 | 35 | 35 | 175 | 35 | 17 | 249 | 12 | 60 |
| Jogador 7 | 38 | 38 | 190 | 38 | 18 | 279 | 7 | 49 |
| Jogador 8 | 27 | 30 | 150 | 27 | 16 | 213 | 16 | 23 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 186 | 186 | 186 | 0 | 176 | 0 | 186 | 186 | 186 | 66/54 |
| Jogador 2 | 303 | 303 | 303 | 0 | 293 | 0 | 303 | 303 | 303 | 115/101 |
| Jogador 3 | 228 | 228 | 228 | 0 | 220 | 0 | 228 | 228 | 228 | 72/57 |
| Jogador 4 | 197 | 197 | 197 | 0 | 184 | 0 | 197 | 197 | 197 | 67/52 |
| Jogador 5 | 181 | 181 | 181 | 0 | 176 | 0 | 181 | 181 | 181 | 76/62 |
| Jogador 6 | 249 | 249 | 249 | 0 | 230 | 0 | 249 | 249 | 249 | 67/53 |
| Jogador 7 | 279 | 279 | 279 | 0 | 262 | 0 | 279 | 279 | 279 | 85/69 |
| Jogador 8 | 213 | 213 | 213 | 0 | 205 | 0 | 213 | 213 | 213 | 85/72 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.20922301709651947 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.25060486793518066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23841141164302826 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22248587012290955 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013312771916389465 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42622989416122437 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3469875156879425 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25063249468803406 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0387812852859497 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0314135551452637 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 39 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 50 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9796043038368225 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 51 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19132192432880402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 52 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17696425318717957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 53 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 54 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3993305265903473 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33605867624282837 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 63 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12911485135555267 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 2-2 | 64 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06063566356897354 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2755657434463501 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00807955488562584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 68 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17293129861354828 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 2-2 | 69 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32695478200912476 | 0.0 | 0.0 | +e76c0caf-1c3d-493f-9a21-659dd8587fc2 / -— |
| Jogador 1 | 2-2 | 70 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3526345491409302 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 74 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3346176743507385 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 75 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17837630212306976 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 1 | 2-3 | 76 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15091802179813385 | 0.0 | 0.0 | +— / -e76c0caf-1c3d-493f-9a21-659dd8587fc2 |
| Jogador 1 | 2-3 | 77 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 78 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3627091348171234 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 83 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 84 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1941869854927063 | 0.0 | 0.0 | +— / -73185d11-22d3-4a1d-803a-b37e82272098 |
| Jogador 1 | 2-4 | 85 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17438462376594543 | 0.0 | 0.0 | +7d8f4f6b-4eba-4c31-9834-bd81a3765520 / -— |
| Jogador 1 | 2-4 | 86 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -7d8f4f6b-4eba-4c31-9834-bd81a3765520 |
| Jogador 1 | 2-4 | 87 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20662473142147064 | 0.0 | 0.0 | +— / -d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 2-4 | 88 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025839999318122864 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 89 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5626901388168335 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 90 | BUY | STABILIZE | 100.0 | 6 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20797860622406006 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -— |
| Jogador 1 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 6 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3701365888118744 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 93 | BUY | STABILIZE | 100.0 | 6 | 4 | 0 | 12.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16430982947349548 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 94 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 12.0 | Defendente/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060818687081336975 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 95 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 12.0 | Defendente/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07295645773410797 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 14.0 | Defendente/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 97 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 14.0 | Defendente/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 98 | PASS | STABILIZE | 100.0 | 6 | 1 | 0 | 14.0 | Defendente/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 102 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 14.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475451946258545 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 7 | 0 | 10.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6740431785583496 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 7 | 0 | 8.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4128207266330719 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 105 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 12.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041939154267311096 | 0.0 | 0.0 | +b32c67a7-6903-403a-9ed6-519ac8487685 / -— |
| Jogador 1 | 2-6 | 106 | BUY | STABILIZE | 100.0 | 6 | 5 | 0 | 12.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2868916988372803 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 107 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 2 | 0 | 12.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40170007944107056 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 108 | BUY | STABILIZE | 100.0 | 6 | 2 | 0 | 16.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0614018514752388 | 0.0 | 0.0 | +f095cd70-c807-4086-a3f1-ddda4f6aa574 / -— |
| Jogador 1 | 2-6 | 109 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 16.0 | Defendente/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02482723817229271 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 16.0 | Defendente/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 112 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 16.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9498274326324463 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-7 | 113 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 12.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06790900975465775 | 0.0 | 0.0 | +07130d94-c79f-4052-b3e9-7f867421f01b / -— |
| Jogador 1 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 5 | 0 | 12.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37007376551628113 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 115 | BUY | STABILIZE | 100.0 | 6 | 5 | 0 | 16.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05940694361925125 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 3 | 0 | 16.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 3 | 0 | 16.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 118 | PASS | STABILIZE | 100.0 | 6 | 3 | 0 | 16.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 6 | 10 | 1 | 18.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16661198437213898 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 123 | BUY | STABILIZE | 100.0 | 6 | 10 | 1 | 18.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015561171807348728 | 0.0 | 0.0 | +dca8bf82-80ac-4054-9a77-3891a7de23e2 / -— |
| Jogador 1 | 3-1 | 124 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 18.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05879678949713707 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 5 | 0 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010515077970921993 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 5 | 0 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 127 | PASS | STABILIZE | 100.0 | 6 | 5 | 0 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 132 | SELL | STABILIZE | 88.0 | 6 | 10 | 1 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -2a286030-5984-44b5-87ff-6c948d2e672e |
| Jogador 1 | 3-2 | 133 | BUY | STABILIZE | 88.0 | 6 | 13 | 1 | 18.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.45360225439071655 | 0.0 | 0.0 | +dc9a3df1-7032-4c92-a919-ca17ae7639ea / -— |
| Jogador 1 | 3-2 | 134 | EQUIP_FROM_INVENTORY | STABILIZE | 88.0 | 6 | 11 | 1 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14313654601573944 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 135 | EQUIP_FROM_INVENTORY | STABILIZE | 88.0 | 6 | 11 | 1 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15583772957324982 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 11 | 1 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019411628600209951 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 137 | SELL | STABILIZE | 88.0 | 6 | 11 | 1 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -f095cd70-c807-4086-a3f1-ddda4f6aa574 |
| Jogador 1 | 3-2 | 138 | BUY | STABILIZE | 88.0 | 6 | 13 | 1 | 18.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0011569566559046507 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 139 | SELL | STABILIZE | 88.0 | 6 | 9 | 0 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0944666638970375 | 0.0 | 0.0 | +— / -07130d94-c79f-4052-b3e9-7f867421f01b |
| Jogador 1 | 3-2 | 140 | BUY | STABILIZE | 88.0 | 6 | 11 | 1 | 18.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07342714816331863 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 1 | 3-3 | 142 | SELL | STABILIZE | 77.0 | 6 | 14 | 1 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010234801098704338 | 0.0 | 0.0 | +— / -b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 1 | 3-3 | 143 | BUY | STABILIZE | 77.0 | 6 | 16 | 1 | 18.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8035223484039307 | 0.0 | 0.0 | +e6ee6b15-d413-4678-8ffb-29272199a53d / -— |
| Jogador 1 | 3-3 | 144 | SELL | STABILIZE | 77.0 | 6 | 13 | 1 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0254080668091774 | 0.0 | 0.0 | +— / -dca8bf82-80ac-4054-9a77-3891a7de23e2 |
| Jogador 1 | 3-3 | 145 | BUY | STABILIZE | 77.0 | 6 | 15 | 1 | 18.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06432346999645233 | 0.0 | 0.0 | +66b5ed5e-7fdf-4135-a334-e693715e302d / -— |
| Jogador 1 | 3-3 | 146 | MOVE_BENCH | STABILIZE | 77.0 | 6 | 13 | 1 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09841547161340714 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 147 | SELL | STABILIZE | 77.0 | 6 | 13 | 1 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024108340963721275 | 0.0 | 0.0 | +— / -66b5ed5e-7fdf-4135-a334-e693715e302d |
| Jogador 1 | 3-3 | 148 | BUY | STABILIZE | 77.0 | 6 | 15 | 1 | 22.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2026110589504242 | 0.0 | 0.0 | +45450b46-63b4-488f-9469-3348c6da8f4b / -— |
| Jogador 1 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 12 | 1 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00021654127340298146 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 12 | 1 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 152 | SELL | STABILIZE | 66.0 | 6 | 19 | 1 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10599999874830246 | 0.0 | 0.0 | +— / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 3-4 | 153 | BUY | STABILIZE | 66.0 | 6 | 22 | 2 | 22.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01783882826566696 | 0.0 | 0.0 | +0450963e-c7e2-4ff5-a2f5-09e65fa63527 / -— |
| Jogador 1 | 3-4 | 154 | SELL | STABILIZE | 66.0 | 6 | 20 | 2 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -0450963e-c7e2-4ff5-a2f5-09e65fa63527 |
| Jogador 1 | 3-4 | 155 | BUY | STABILIZE | 66.0 | 6 | 22 | 2 | 22.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025058075785636902 | 0.0 | 0.0 | +54b47885-6cb9-42e7-a9bb-049e0e2d2956 / -— |
| Jogador 1 | 3-4 | 156 | SELL | STABILIZE | 66.0 | 6 | 21 | 2 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0070333331823349 | 0.0 | 0.0 | +— / -54b47885-6cb9-42e7-a9bb-049e0e2d2956 |
| Jogador 1 | 3-4 | 157 | BUY | STABILIZE | 66.0 | 6 | 22 | 2 | 22.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28749313950538635 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 66.0 | 6 | 20 | 2 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.546155054820701e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 66.0 | 6 | 20 | 2 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015441878698766232 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 66.0 | 6 | 20 | 2 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0137751754373312 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 162 | SELL | STABILIZE | 66.0 | 6 | 28 | 2 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10400000214576721 | 0.0 | 0.0 | +— / -bddefab1-7dd7-4954-816c-45dbd44b947b |
| Jogador 1 | 3-5 | 163 | BUY | STABILIZE | 66.0 | 6 | 30 | 3 | 22.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7481716275215149 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -— |
| Jogador 1 | 3-5 | 164 | SELL | STABILIZE | 66.0 | 6 | 28 | 2 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09083333611488342 | 0.0 | 0.0 | +— / -9fe58106-e0c4-4ecc-b152-13c8c0eb564e |
| Jogador 1 | 3-5 | 165 | BUY | STABILIZE | 66.0 | 6 | 31 | 3 | 22.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02753833495080471 | 0.0 | 0.0 | +a9184317-58b7-4804-9aef-3e2c08c20935 / -— |
| Jogador 1 | 3-5 | 166 | SELL | STABILIZE | 66.0 | 6 | 30 | 3 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0070333331823349 | 0.0 | 0.0 | +— / -a9184317-58b7-4804-9aef-3e2c08c20935 |
| Jogador 1 | 3-5 | 167 | BUY | STABILIZE | 66.0 | 6 | 31 | 3 | 22.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3684089183807373 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 1 | 3-5 | 168 | SELL | STABILIZE | 66.0 | 6 | 29 | 2 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10400000214576721 | 0.0 | 0.0 | +— / -727765c8-7f02-491e-a6da-12b0dab59f6d |
| Jogador 1 | 3-5 | 169 | BUY | STABILIZE | 66.0 | 6 | 31 | 3 | 22.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.368409126996994 | 0.0 | 0.0 | +c5557e24-8174-4d79-9e22-c2cbbb8225a8 / -— |
| Jogador 1 | 3-5 | 170 | MOVE_BOARD | STABILIZE | 66.0 | 6 | 29 | 2 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.822783663868904e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 172 | SELL | STABILIZE | 55.0 | 6 | 37 | 3 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -c5557e24-8174-4d79-9e22-c2cbbb8225a8 |
| Jogador 1 | 3-6 | 173 | BUY | STABILIZE | 55.0 | 6 | 39 | 3 | 22.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8658864498138428 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -9aa6122c-e49a-48a2-ba24-7adcd3b7cb56,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-6 | 174 | BUY | STABILIZE | 55.0 | 6 | 37 | 3 | 18.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.811839759349823 | 0.0 | 0.0 | +600071dd-5c17-4f03-903f-d1cd6c20bb28 / -— |
| Jogador 1 | 3-6 | 175 | SELL | STABILIZE | 55.0 | 6 | 36 | 3 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 3-6 | 176 | BUY | STABILIZE | 55.0 | 6 | 41 | 4 | 18.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.23549436032772064 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 177 | EQUIP_FROM_INVENTORY | STABILIZE | 55.0 | 6 | 39 | 3 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14072677493095398 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 178 | MOVE_BENCH | STABILIZE | 55.0 | 6 | 39 | 3 | 18.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43316835165023804 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 179 | BUY | STABILIZE | 55.0 | 6 | 39 | 3 | 20.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02825731784105301 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 1 | 3-6 | 180 | MOVE_BOARD | STABILIZE | 55.0 | 6 | 35 | 3 | 20.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004648370377253741 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 182 | SELL | STABILIZE | 45.0 | 6 | 45 | 4 | 20.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004349244758486748 | 0.0 | 0.0 | +— / -7c218f01-e884-46da-8a1a-2d2db27a5ff1 |
| Jogador 1 | 3-7 | 183 | BUY | STABILIZE | 45.0 | 6 | 48 | 4 | 20.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4997102916240692 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 1 | 3-7 | 184 | SELL | STABILIZE | 45.0 | 6 | 44 | 4 | 20.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002166666556149721 | 0.0 | 0.0 | +— / -45450b46-63b4-488f-9469-3348c6da8f4b |
| Jogador 1 | 3-7 | 185 | BUY | STABILIZE | 45.0 | 6 | 47 | 4 | 20.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6630684733390808 | 0.0 | 0.0 | +c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 / -b32c67a7-6903-403a-9ed6-519ac8487685,dc9a3df1-7032-4c92-a919-ca17ae7639ea |
| Jogador 1 | 3-7 | 186 | MOVE_BENCH | STABILIZE | 45.0 | 6 | 45 | 4 | 16.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4002019762992859 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 187 | BUY | STABILIZE | 45.0 | 6 | 45 | 4 | 24.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021408075466752052 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 1 | 3-7 | 188 | BUY | STABILIZE | 45.0 | 6 | 43 | 4 | 24.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2840375602245331 | 0.0 | 0.0 | +68d2cec6-d29b-4173-a696-ac20ccb1f079 / -— |
| Jogador 1 | 3-7 | 189 | MOVE_BOARD | STABILIZE | 45.0 | 6 | 41 | 4 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011189165525138378 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 45.0 | 6 | 41 | 4 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003811586182564497 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 45.0 | 6 | 52 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11185671389102936 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 45.0 | 6 | 52 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.187686949968338 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 194 | SELL | STABILIZE | 45.0 | 6 | 52 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07699678838253021 | 0.0 | 0.0 | +— / -c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 |
| Jogador 1 | 4-1 | 195 | BUY | STABILIZE | 45.0 | 6 | 57 | 5 | 24.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30594950914382935 | 0.0 | 0.0 | +8ff9f97f-9d27-44d5-ae97-a6d618c568a1 / -— |
| Jogador 1 | 4-1 | 196 | SELL | STABILIZE | 45.0 | 6 | 54 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -68d2cec6-d29b-4173-a696-ac20ccb1f079 |
| Jogador 1 | 4-1 | 197 | BUY | STABILIZE | 45.0 | 6 | 56 | 5 | 24.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00894057098776102 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 1 | 4-1 | 198 | SELL | STABILIZE | 45.0 | 6 | 53 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010395772755146027 | 0.0 | 0.0 | +— / -227dbcdb-af5c-4318-94d1-f01a7847d100 |
| Jogador 1 | 4-1 | 199 | BUY | STABILIZE | 45.0 | 6 | 55 | 5 | 24.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47247177362442017 | 0.0 | 0.0 | +502a6e8c-8f81-456f-a1ef-c6bb8dd6fc7e / -— |
| Jogador 1 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 45.0 | 6 | 52 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 202 | SELL | STABILIZE | 33.0 | 6 | 65 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019281474873423576 | 0.0 | 0.0 | +— / -145f7470-8c0f-4957-b8d6-97939ddaeba1 |
| Jogador 1 | 4-2 | 203 | BUY | STABILIZE | 33.0 | 6 | 69 | 5 | 24.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39807742834091187 | 0.0 | 0.0 | +6fa83356-562b-4a26-a77d-3e989089e70a / -— |
| Jogador 1 | 4-2 | 204 | SELL | STABILIZE | 33.0 | 6 | 68 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08625509589910507 | 0.0 | 0.0 | +— / -8ff9f97f-9d27-44d5-ae97-a6d618c568a1 |
| Jogador 1 | 4-2 | 205 | BUY | STABILIZE | 33.0 | 6 | 71 | 5 | 24.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.033486977219581604 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 1 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 33.0 | 6 | 68 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.175739705824526e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 207 | SELL | STABILIZE | 33.0 | 6 | 68 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022130463272333145 | 0.0 | 0.0 | +— / -5af104f2-7959-4ca5-91a9-7d44494532ea |
| Jogador 1 | 4-2 | 208 | BUY | STABILIZE | 33.0 | 6 | 71 | 5 | 24.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05152558907866478 | 0.0 | 0.0 | +301afc05-ad23-4ed2-a835-108235c399e0 / -— |
| Jogador 1 | 4-2 | 209 | MOVE_BOARD | STABILIZE | 33.0 | 6 | 69 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.116582653703517e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 210 | SELL | STABILIZE | 33.0 | 6 | 69 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -301afc05-ad23-4ed2-a835-108235c399e0 |
| Jogador 1 | 4-3 | 212 | BUY | ALL_IN | 21.0 | 6 | 84 | 5 | 24.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.939487874507904 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -— |
| Jogador 1 | 4-3 | 213 | SELL | ALL_IN | 21.0 | 6 | 82 | 5 | 24.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6825000047683716 | 0.0 | 0.0 | +— / -6fa83356-562b-4a26-a77d-3e989089e70a |
| Jogador 1 | 4-3 | 214 | BUY | ALL_IN | 21.0 | 6 | 83 | 5 | 24.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0187265872955322 | 0.0 | 0.0 | +ba7f039a-929c-4537-9eb6-f1dc4563cca8 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 4-3 | 215 | BUY | ALL_IN | 21.0 | 6 | 82 | 5 | 22.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23027463257312775 | 0.0 | 0.0 | +6388773b-0e99-40a9-8d68-895dcf16fce6 / -— |
| Jogador 1 | 4-3 | 216 | MOVE_BENCH | ALL_IN | 21.0 | 6 | 79 | 5 | 22.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4008355140686035 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 217 | BUY | ALL_IN | 21.0 | 6 | 79 | 5 | 28.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27390769124031067 | 0.0 | 0.0 | +cb30dcaa-bc26-4584-9b50-24e47e70fcb0 / -— |
| Jogador 1 | 4-3 | 218 | MOVE_BOARD | ALL_IN | 21.0 | 6 | 78 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0013723140582442284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 219 | MOVE_BOARD | ALL_IN | 21.0 | 6 | 78 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013622540980577469 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 220 | PASS | ALL_IN | 21.0 | 6 | 78 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47198325395584106 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 222 | SELL | ALL_IN | 8.0 | 6 | 91 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7214999794960022 | 0.0 | 0.0 | +— / -ba7f039a-929c-4537-9eb6-f1dc4563cca8 |
| Jogador 1 | 4-4 | 223 | BUY | ALL_IN | 8.0 | 6 | 94 | 5 | 28.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9628390669822693 | 0.0 | 0.0 | +e1867f53-f97a-4c7a-bce3-24aa037ce27f / -— |
| Jogador 1 | 4-4 | 224 | EQUIP_FROM_INVENTORY | ALL_IN | 8.0 | 6 | 93 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1435888111591339 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 225 | EQUIP_FROM_INVENTORY | ALL_IN | 8.0 | 6 | 93 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12785273790359497 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 226 | SELL | ALL_IN | 8.0 | 6 | 93 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -cb30dcaa-bc26-4584-9b50-24e47e70fcb0 |
| Jogador 1 | 4-4 | 227 | BUY | ALL_IN | 8.0 | 6 | 94 | 5 | 28.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12535367906093597 | 0.0 | 0.0 | +7dfeef88-7e1d-43b8-b012-017278ec61dc / -— |
| Jogador 1 | 4-4 | 228 | SELL | ALL_IN | 8.0 | 6 | 92 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03172031044960022 | 0.0 | 0.0 | +— / -7dfeef88-7e1d-43b8-b012-017278ec61dc |
| Jogador 1 | 4-4 | 229 | BUY | ALL_IN | 8.0 | 6 | 94 | 5 | 28.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.040161147713661194 | 0.0 | 0.0 | +fcd8f4bf-7e1f-42b3-a989-5b3683394c89 / -— |
| Jogador 1 | 4-4 | 230 | MOVE_BOARD | ALL_IN | 8.0 | 6 | 92 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 232 | SELL | ALL_IN | 8.0 | 6 | 105 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -fcd8f4bf-7e1f-42b3-a989-5b3683394c89 |
| Jogador 1 | 4-5 | 233 | BUY | ALL_IN | 8.0 | 6 | 107 | 5 | 28.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39973631501197815 | 0.0 | 0.0 | +c49cf468-6fa4-4d94-bc3a-9dc8f7111626 / -— |
| Jogador 1 | 4-5 | 234 | SELL | ALL_IN | 8.0 | 6 | 104 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5541666746139526 | 0.0 | 0.0 | +— / -6388773b-0e99-40a9-8d68-895dcf16fce6 |
| Jogador 1 | 4-5 | 235 | BUY | ALL_IN | 8.0 | 6 | 107 | 5 | 28.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2258400022983551 | 0.0 | 0.0 | +226f36b1-cb9a-464a-a10a-3f21ebd41f24 / -— |
| Jogador 1 | 4-5 | 236 | SELL | ALL_IN | 8.0 | 6 | 104 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -c49cf468-6fa4-4d94-bc3a-9dc8f7111626 |
| Jogador 1 | 4-5 | 237 | BUY | ALL_IN | 8.0 | 6 | 107 | 5 | 28.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13920463621616364 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 1 | 4-5 | 238 | MOVE_BOARD | ALL_IN | 8.0 | 6 | 103 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 239 | MOVE_BOARD | ALL_IN | 8.0 | 6 | 103 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998691156506538 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 240 | PASS | ALL_IN | 8.0 | 6 | 103 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5327625870704651 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 242 | SELL | ALL_IN | 8.0 | 6 | 114 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -226f36b1-cb9a-464a-a10a-3f21ebd41f24 |
| Jogador 1 | 4-6 | 243 | BUY | ALL_IN | 8.0 | 6 | 117 | 5 | 28.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2188752144575119 | 0.0 | 0.0 | +7e0d7932-1b83-4918-9292-6e60957e6022 / -— |
| Jogador 1 | 4-6 | 244 | SELL | ALL_IN | 8.0 | 6 | 114 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -7e0d7932-1b83-4918-9292-6e60957e6022 |
| Jogador 1 | 4-6 | 245 | BUY | ALL_IN | 8.0 | 6 | 117 | 5 | 28.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0051310984417796135 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -— |
| Jogador 1 | 4-6 | 246 | SELL | ALL_IN | 8.0 | 6 | 115 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023079581558704376 | 0.0 | 0.0 | +— / -50edcbf1-13cd-4f98-bf35-d5a474fbe20c |
| Jogador 1 | 4-6 | 247 | BUY | ALL_IN | 8.0 | 6 | 117 | 5 | 28.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014635909348726273 | 0.0 | 0.0 | +241a8a03-6e6f-4a9a-8550-e9154f3e1e76 / -— |
| Jogador 1 | 4-6 | 248 | REROLL | ALL_IN | 8.0 | 6 | 115 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 249 | SELL | ALL_IN | 8.0 | 6 | 113 | 5 | 28.0 | Defendente/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -241a8a03-6e6f-4a9a-8550-e9154f3e1e76 |
| Jogador 1 | 4-6 | 250 | BUY | ALL_IN | 8.0 | 6 | 115 | 5 | 28.0 | Defendente/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0748039484024048 | 0.0 | 0.0 | +362f7357-283e-4f88-bff3-ffa6314af821 / -801687e6-da6a-4ab1-8032-a45daf0e6554,e1867f53-f97a-4c7a-bce3-24aa037ce27f |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29996994137763977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.16027452051639557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43195363879203796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 15 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5009031295776367 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1178059577941895 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11989116668701172 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 25 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3088749945163727 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40793588757514954 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0721161365509033 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20201948285102844 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 40 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4003269076347351 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024478765204548836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 42 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012103810906410217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 43 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 50 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0379815101623535 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 51 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18191413581371307 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 52 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.27329137921333313 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 53 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2662402093410492 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 54 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14821511507034302 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047492608428001404 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19650211930274963 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 2 | 2-1 | 57 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028999745845794678 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004016788676381111 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 59 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4023333191871643 | 0.0 | 0.0 | +— / -2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 |
| Jogador 2 | 2-1 | 60 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 62 | BUY | STABILIZE | 96.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179670095443726 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 63 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2369430959224701 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 64 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17829301953315735 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 65 | PASS | STABILIZE | 96.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 72 | BUY | STABILIZE | 91.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29859861731529236 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 73 | BUY | STABILIZE | 91.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042062703520059586 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 74 | BUY_XP | STABILIZE | 91.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 75 | SELL | STABILIZE | 91.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8824999928474426 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-3 | 76 | BUY | STABILIZE | 91.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030762862414121628 | 0.0 | 0.0 | +e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 / -— |
| Jogador 2 | 2-3 | 77 | PASS | STABILIZE | 91.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 82 | BUY | STABILIZE | 86.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7648670673370361 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 2 | 2-4 | 83 | BUY | STABILIZE | 86.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2953852415084839 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 84 | BUY | STABILIZE | 86.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07453805953264236 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 85 | SELL | STABILIZE | 86.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00026666666963137686 | 0.0 | 0.0 | +— / -e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 |
| Jogador 2 | 2-4 | 86 | MOVE_BENCH | STABILIZE | 86.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40131717920303345 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 87 | BUY | STABILIZE | 86.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057884909212589264 | 0.0 | 0.0 | +ce928be1-b3ba-4640-b93c-d15c8a92833e / -— |
| Jogador 2 | 2-4 | 88 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0035479911603033543 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 89 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011196475476026535 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 90 | PASS | STABILIZE | 86.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 92 | BUY | STABILIZE | 86.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13581883907318115 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 93 | SELL | STABILIZE | 86.0 | 5 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0027000000700354576 | 0.0 | 0.0 | +— / -ce928be1-b3ba-4640-b93c-d15c8a92833e |
| Jogador 2 | 2-5 | 94 | BUY | STABILIZE | 86.0 | 5 | 5 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007320189382880926 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 95 | SELL | STABILIZE | 86.0 | 5 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03613138571381569 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-5 | 96 | BUY | STABILIZE | 86.0 | 5 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16917698085308075 | 0.0 | 0.0 | +6a071ec5-c3f4-41b3-a0d8-c1aee62cffee / -— |
| Jogador 2 | 2-5 | 97 | SELL | STABILIZE | 86.0 | 5 | 1 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00996666681021452 | 0.0 | 0.0 | +— / -8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 2-5 | 98 | BUY_XP | STABILIZE | 86.0 | 5 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 99 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 0 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.6332486817846075e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 100 | SELL | STABILIZE | 86.0 | 5 | 0 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -6a071ec5-c3f4-41b3-a0d8-c1aee62cffee |
| Jogador 2 | 2-6 | 102 | BUY | STABILIZE | 81.0 | 5 | 9 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16185922920703888 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 103 | BUY_XP | STABILIZE | 81.0 | 5 | 6 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 104 | SELL | STABILIZE | 81.0 | 5 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -d1840f93-35b0-4e88-b58e-eea7267beedc |
| Jogador 2 | 2-6 | 105 | SELL | STABILIZE | 81.0 | 5 | 5 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42233332991600037 | 0.0 | 0.0 | +— / -97fc5647-5995-4f21-aa03-13454546919a |
| Jogador 2 | 2-6 | 106 | BUY | STABILIZE | 81.0 | 5 | 8 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10292933136224747 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 107 | BUY_XP | STABILIZE | 81.0 | 5 | 6 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 108 | SELL | STABILIZE | 81.0 | 5 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10688215494155884 | 0.0 | 0.0 | +— / -6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 2-6 | 109 | BUY_XP | STABILIZE | 81.0 | 5 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 110 | SELL | STABILIZE | 81.0 | 6 | 0 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14723564684391022 | 0.0 | 0.0 | +— / -081b684f-5d42-45c5-9a68-12127e5330a7 |
| Jogador 2 | 2-7 | 112 | BUY | STABILIZE | 76.0 | 6 | 10 | 1 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27938687801361084 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 113 | BUY | STABILIZE | 76.0 | 6 | 6 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1432335078716278 | 0.0 | 0.0 | +6340ebaf-bd41-4f47-bdce-50e06faa4044 / -— |
| Jogador 2 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4108906090259552 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 4 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 116 | BUY_XP | STABILIZE | 76.0 | 6 | 4 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0013390252133831382 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 118 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013678359799087048 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 119 | PASS | STABILIZE | 76.0 | 6 | 0 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 122 | BUY | STABILIZE | 76.0 | 6 | 7 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2046688050031662 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 123 | BUY | STABILIZE | 76.0 | 6 | 4 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11510974913835526 | 0.0 | 0.0 | +4312fba1-1471-4fb3-af6f-257248fa1437 / -— |
| Jogador 2 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 76.0 | 6 | 2 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2646680474281311 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 125 | BUY | STABILIZE | 76.0 | 6 | 2 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.040484875440597534 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 126 | SELL | STABILIZE | 76.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02757301554083824 | 0.0 | 0.0 | +— / -a0ebc646-2e71-4b07-9208-401aa0cda6bb |
| Jogador 2 | 3-1 | 127 | SELL | STABILIZE | 76.0 | 6 | 2 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09090838581323624 | 0.0 | 0.0 | +— / -6340ebaf-bd41-4f47-bdce-50e06faa4044 |
| Jogador 2 | 3-1 | 128 | BUY_XP | STABILIZE | 76.0 | 6 | 4 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 129 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.4766971617063973e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 130 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998615719377995 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 132 | BUY | STABILIZE | 66.0 | 6 | 8 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8372519016265869 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -7ca9b803-76eb-4283-9648-7f98bfd81149,d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 2 | 3-2 | 133 | BUY | STABILIZE | 66.0 | 6 | 7 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04086491838097572 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 134 | BUY | STABILIZE | 66.0 | 6 | 6 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23672468960285187 | 0.0 | 0.0 | +e86a4466-cd1f-48a3-a825-cab2e361b72a / -— |
| Jogador 2 | 3-2 | 135 | BUY | STABILIZE | 66.0 | 6 | 5 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29599300026893616 | 0.0 | 0.0 | +f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 / -— |
| Jogador 2 | 3-2 | 136 | SELL | STABILIZE | 66.0 | 6 | 3 | 0 | 24.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -5489a8f6-2466-4171-b91e-64c367875d3c |
| Jogador 2 | 3-2 | 137 | BUY | STABILIZE | 66.0 | 6 | 6 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2961244583129883 | 0.0 | 0.0 | +e6614d74-9c11-4502-8719-4d49167f44ab / -— |
| Jogador 2 | 3-2 | 138 | BUY_XP | STABILIZE | 66.0 | 6 | 4 | 0 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 139 | SELL | STABILIZE | 66.0 | 6 | 0 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0018333332845941186 | 0.0 | 0.0 | +— / -e86a4466-cd1f-48a3-a825-cab2e361b72a |
| Jogador 2 | 3-2 | 140 | SELL | STABILIZE | 66.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09893037378787994 | 0.0 | 0.0 | +— / -584e7960-a541-4d45-8ea1-8a75e288c387 |
| Jogador 2 | 3-3 | 142 | BUY | STABILIZE | 66.0 | 6 | 8 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8038710355758667 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 143 | BUY | STABILIZE | 66.0 | 6 | 5 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0296635739505291 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 144 | SELL | STABILIZE | 66.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 |
| Jogador 2 | 3-3 | 145 | BUY | STABILIZE | 66.0 | 6 | 3 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08130595088005066 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 146 | SELL | STABILIZE | 66.0 | 6 | 0 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -e6614d74-9c11-4502-8719-4d49167f44ab |
| Jogador 2 | 3-3 | 147 | BUY | STABILIZE | 66.0 | 6 | 2 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29596132040023804 | 0.0 | 0.0 | +c30a99f5-ce2d-4bbf-9aab-93017ad40255 / -— |
| Jogador 2 | 3-3 | 148 | SELL | STABILIZE | 66.0 | 6 | 0 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -c30a99f5-ce2d-4bbf-9aab-93017ad40255 |
| Jogador 2 | 3-3 | 149 | BUY | STABILIZE | 66.0 | 6 | 2 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2959613502025604 | 0.0 | 0.0 | +e08cb89b-8a77-44fe-be4c-46c2b45cbe9b / -— |
| Jogador 2 | 3-3 | 150 | SELL | STABILIZE | 66.0 | 6 | 0 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -e08cb89b-8a77-44fe-be4c-46c2b45cbe9b |
| Jogador 2 | 3-4 | 152 | BUY | STABILIZE | 55.0 | 6 | 7 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019156446680426598 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -— |
| Jogador 2 | 3-4 | 153 | SELL | STABILIZE | 55.0 | 6 | 5 | 0 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021467484533786774 | 0.0 | 0.0 | +— / -c4c0b136-020d-4c1e-9517-8e0bf4c5a628 |
| Jogador 2 | 3-4 | 154 | BUY | STABILIZE | 55.0 | 6 | 7 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019198201596736908 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 2 | 3-4 | 155 | SELL | STABILIZE | 55.0 | 6 | 5 | 0 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02147136814892292 | 0.0 | 0.0 | +— / -c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 2 | 3-4 | 156 | BUY | STABILIZE | 55.0 | 6 | 7 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043069299310445786 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 157 | BUY_XP | STABILIZE | 55.0 | 6 | 5 | 0 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 158 | SELL | STABILIZE | 55.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 3-4 | 159 | BUY | STABILIZE | 55.0 | 6 | 3 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29370254278182983 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 2 | 3-4 | 160 | SELL | STABILIZE | 55.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -ff0d9869-c346-4210-be85-1e802a25dd8b |
| Jogador 2 | 3-5 | 162 | BUY | STABILIZE | 55.0 | 6 | 8 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6604251265525818 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 163 | SELL | STABILIZE | 55.0 | 6 | 5 | 0 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024018533527851105 | 0.0 | 0.0 | +— / -4312fba1-1471-4fb3-af6f-257248fa1437 |
| Jogador 2 | 3-5 | 164 | BUY | STABILIZE | 55.0 | 6 | 7 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04344548285007477 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 165 | SELL | STABILIZE | 55.0 | 6 | 5 | 0 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024022405967116356 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 3-5 | 166 | BUY | STABILIZE | 55.0 | 6 | 7 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27555927634239197 | 0.0 | 0.0 | +c5a8f36d-74b1-4944-a3db-bfb601a89b59 / -— |
| Jogador 2 | 3-5 | 167 | SELL | STABILIZE | 55.0 | 6 | 6 | 0 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014633333310484886 | 0.0 | 0.0 | +— / -c5a8f36d-74b1-4944-a3db-bfb601a89b59 |
| Jogador 2 | 3-5 | 168 | BUY_XP | STABILIZE | 55.0 | 6 | 7 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 169 | SELL | STABILIZE | 55.0 | 6 | 3 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050333332270383835 | 0.0 | 0.0 | +— / -3880fbd9-322b-4375-b855-fbb779a0cb47 |
| Jogador 2 | 3-5 | 170 | BUY_XP | STABILIZE | 55.0 | 6 | 6 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06353499740362167 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 172 | BUY | STABILIZE | 44.0 | 7 | 8 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.287974089384079 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-6 | 173 | BUY | STABILIZE | 44.0 | 7 | 7 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02509416826069355 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 174 | MOVE_BENCH | STABILIZE | 44.0 | 7 | 3 | 0 | 24.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4012325406074524 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 175 | BUY | STABILIZE | 44.0 | 7 | 3 | 0 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05333390459418297 | 0.0 | 0.0 | +8fb80cc8-4120-41a0-bc96-35f81a466ed9 / -— |
| Jogador 2 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 0 | 0 | 30.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005285354563966393 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 0 | 0 | 30.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01446986198425293 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 178 | PASS | STABILIZE | 44.0 | 7 | 0 | 0 | 30.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 182 | SELL | STABILIZE | 34.0 | 7 | 6 | 0 | 30.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00563333323225379 | 0.0 | 0.0 | +— / -8fb80cc8-4120-41a0-bc96-35f81a466ed9 |
| Jogador 2 | 3-7 | 183 | BUY | STABILIZE | 34.0 | 7 | 9 | 0 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8015130758285522 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 184 | SELL | STABILIZE | 34.0 | 7 | 5 | 0 | 30.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -23157bd6-5e8f-4416-bb7f-2e5d71a06543 |
| Jogador 2 | 3-7 | 185 | BUY | STABILIZE | 34.0 | 7 | 9 | 0 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8338992595672607 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -0c15e414-bc67-46de-a087-fb7708db0dfe,e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-7 | 186 | BUY | STABILIZE | 34.0 | 7 | 6 | 0 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055827416479587555 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 2 | 3-7 | 187 | BUY | STABILIZE | 34.0 | 7 | 3 | 0 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24247443675994873 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 2 | 3-7 | 188 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 0 | 0 | 30.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 189 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 0 | 0 | 30.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997908845543861 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 190 | PASS | STABILIZE | 34.0 | 7 | 0 | 0 | 30.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 34.0 | 7 | 6 | 0 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1934857815504074 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 34.0 | 7 | 6 | 0 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20590198040008545 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 194 | SELL | STABILIZE | 34.0 | 7 | 6 | 0 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 4-1 | 195 | BUY | STABILIZE | 34.0 | 7 | 14 | 1 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055781930685043335 | 0.0 | 0.0 | +a4188ec8-4188-4fdf-8d76-c559fc0c7daf / -— |
| Jogador 2 | 4-1 | 196 | SELL | STABILIZE | 34.0 | 7 | 11 | 1 | 30.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010833333246409893 | 0.0 | 0.0 | +— / -ed0dab77-fd87-4677-8428-7505ccd34b86 |
| Jogador 2 | 4-1 | 197 | BUY | STABILIZE | 34.0 | 7 | 14 | 1 | 30.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2376215010881424 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 2 | 4-1 | 198 | BUY_XP | STABILIZE | 34.0 | 7 | 11 | 1 | 30.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 199 | BUY_XP | STABILIZE | 34.0 | 7 | 7 | 0 | 30.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 200 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 3 | 0 | 30.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38864660263061523 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 202 | SELL | STABILIZE | 34.0 | 7 | 9 | 0 | 36.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08910000324249268 | 0.0 | 0.0 | +— / -1be0cdcc-ee10-44dc-ad1b-de9b53b25164 |
| Jogador 2 | 4-2 | 203 | BUY | STABILIZE | 34.0 | 7 | 12 | 1 | 36.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379881381988525 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-2 | 204 | BUY | STABILIZE | 34.0 | 7 | 11 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05043894797563553 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -— |
| Jogador 2 | 4-2 | 205 | SELL | STABILIZE | 34.0 | 7 | 9 | 0 | 34.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -b7e13ed2-571b-4245-ba21-401b1eef8660 |
| Jogador 2 | 4-2 | 206 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 7 | 12 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07796462625265121 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 207 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 7 | 12 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07332409918308258 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 208 | BUY_XP | STABILIZE | 34.0 | 7 | 12 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 209 | BUY_XP | STABILIZE | 34.0 | 7 | 8 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 210 | BUY_XP | STABILIZE | 34.0 | 7 | 4 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 212 | BUY | STABILIZE | 34.0 | 7 | 7 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28331148624420166 | 0.0 | 0.0 | +104aaac3-252c-4c1b-9ad8-fc10a35c6cda / -— |
| Jogador 2 | 4-3 | 213 | SELL | STABILIZE | 34.0 | 7 | 4 | 0 | 34.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011509096249938011 | 0.0 | 0.0 | +— / -23793b7b-2dab-48f0-a8ba-db85fc14c1c5 |
| Jogador 2 | 4-3 | 214 | BUY | STABILIZE | 34.0 | 7 | 6 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036387909203767776 | 0.0 | 0.0 | +84886290-556f-45e9-805b-9ca86a80ba27 / -— |
| Jogador 2 | 4-3 | 215 | SELL | STABILIZE | 34.0 | 7 | 5 | 0 | 34.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00563333323225379 | 0.0 | 0.0 | +— / -a4188ec8-4188-4fdf-8d76-c559fc0c7daf |
| Jogador 2 | 4-3 | 216 | BUY_XP | STABILIZE | 34.0 | 7 | 8 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 217 | SELL | STABILIZE | 34.0 | 7 | 4 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07668451219797134 | 0.0 | 0.0 | +— / -74b1cd6f-12f4-4287-a5f6-9d016663ccf5 |
| Jogador 2 | 4-3 | 218 | BUY_XP | STABILIZE | 34.0 | 7 | 7 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 219 | SELL | STABILIZE | 34.0 | 7 | 3 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 4-3 | 220 | BUY_XP | STABILIZE | 34.0 | 7 | 7 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 222 | BUY | ALL_IN | 23.0 | 7 | 8 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8830292820930481 | 0.0 | 0.0 | +bb2e33e3-fe6f-4344-b113-aeba7ace7a2d / -cce8de69-f877-4e86-b720-6aea91e68f47,e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 4-4 | 223 | BUY | ALL_IN | 23.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016673153266310692 | 0.0 | 0.0 | +a2b57772-7a23-4ffd-ace1-d2a7a3f5a7cd / -— |
| Jogador 2 | 4-4 | 224 | MOVE_BENCH | ALL_IN | 23.0 | 7 | 3 | 0 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30604690313339233 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 225 | BUY | ALL_IN | 23.0 | 7 | 3 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020527053624391556 | 0.0 | 0.0 | +d974e68a-e978-4335-8827-a94a9219be58 / -— |
| Jogador 2 | 4-4 | 226 | MOVE_BOARD | ALL_IN | 23.0 | 7 | 0 | 0 | 34.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0001444549416191876 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 227 | SELL | ALL_IN | 23.0 | 7 | 0 | 0 | 34.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7045999765396118 | 0.0 | 0.0 | +— / -bb2e33e3-fe6f-4344-b113-aeba7ace7a2d |
| Jogador 2 | 4-4 | 228 | SELL | ALL_IN | 23.0 | 7 | 8 | 0 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29687198996543884 | 0.0 | 0.0 | +— / -d974e68a-e978-4335-8827-a94a9219be58 |
| Jogador 2 | 4-4 | 229 | SELL | ALL_IN | 23.0 | 7 | 11 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7185999751091003 | 0.0 | 0.0 | +— / -f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 4-4 | 230 | SELL | ALL_IN | 23.0 | 7 | 12 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5116444230079651 | 0.0 | 0.0 | +— / -84886290-556f-45e9-805b-9ca86a80ba27 |
| Jogador 2 | 4-5 | 232 | BUY | ALL_IN | 23.0 | 7 | 19 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23975332081317902 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -— |
| Jogador 2 | 4-5 | 233 | BUY | ALL_IN | 23.0 | 7 | 16 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1001235693693161 | 0.0 | 0.0 | +7643f027-a90f-4f3a-8b4c-7be4cba17f95 / -— |
| Jogador 2 | 4-5 | 234 | BUY | ALL_IN | 23.0 | 7 | 13 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04029610753059387 | 0.0 | 0.0 | +8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e / -— |
| Jogador 2 | 4-5 | 235 | SELL | ALL_IN | 23.0 | 7 | 11 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3490000069141388 | 0.0 | 0.0 | +— / -8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e |
| Jogador 2 | 4-5 | 236 | SELL | ALL_IN | 23.0 | 7 | 13 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39759790897369385 | 0.0 | 0.0 | +— / -7643f027-a90f-4f3a-8b4c-7be4cba17f95 |
| Jogador 2 | 4-5 | 237 | SELL | ALL_IN | 23.0 | 7 | 16 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5905274152755737 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 4-5 | 238 | BUY_XP | ALL_IN | 23.0 | 7 | 17 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11219999939203262 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 239 | MOVE_BENCH | ALL_IN | 23.0 | 7 | 13 | 1 | 34.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40081384778022766 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 240 | MOVE_BOARD | ALL_IN | 23.0 | 7 | 13 | 1 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014974338002502918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 242 | BUY | ALL_IN | 11.0 | 7 | 20 | 2 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3882150650024414 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 2 | 4-6 | 243 | BUY | ALL_IN | 11.0 | 7 | 19 | 1 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37362295389175415 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 2 | 4-6 | 244 | BUY | ALL_IN | 11.0 | 7 | 18 | 1 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014417444355785847 | 0.0 | 0.0 | +20821a31-3317-4f82-bbb2-b70cdebdd893 / -— |
| Jogador 2 | 4-6 | 245 | BUY | ALL_IN | 11.0 | 7 | 16 | 1 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0387694388628006 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -— |
| Jogador 2 | 4-6 | 246 | MOVE_BOARD | ALL_IN | 11.0 | 7 | 15 | 1 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -7.28368031559512e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 247 | MOVE_BOARD | ALL_IN | 11.0 | 7 | 15 | 1 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014925760217010975 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 248 | PASS | ALL_IN | 11.0 | 7 | 15 | 1 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35507407784461975 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 252 | BUY | ALL_IN | 11.0 | 7 | 22 | 2 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3420095145702362 | 0.0 | 0.0 | +80130f72-2d7c-49db-8d6f-4c0a962260e8 / -— |
| Jogador 2 | 4-7 | 253 | BUY | ALL_IN | 11.0 | 7 | 21 | 2 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0007560504018329084 | 0.0 | 0.0 | +aaebedb3-18bf-4ae6-948e-7b326b573f1c / -— |
| Jogador 2 | 4-7 | 254 | BUY | ALL_IN | 11.0 | 7 | 19 | 1 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.275894433259964 | 0.0 | 0.0 | +3c59d736-011d-480c-a9af-1df7a3b4caab / -— |
| Jogador 2 | 4-7 | 255 | MOVE_BOARD | ALL_IN | 11.0 | 7 | 17 | 1 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.2398818682868296e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 256 | MOVE_BOARD | ALL_IN | 11.0 | 7 | 17 | 1 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015013781376183033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 257 | SELL | ALL_IN | 11.0 | 7 | 17 | 1 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011348983272910118 | 0.0 | 0.0 | +— / -023f01af-91d0-4e07-8229-2b7cded83151 |
| Jogador 2 | 4-7 | 258 | BUY | ALL_IN | 11.0 | 7 | 18 | 1 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25040438771247864 | 0.0 | 0.0 | +bcd06176-e1d7-43fb-abd4-b6faea8c7927 / -— |
| Jogador 2 | 4-7 | 259 | MOVE_BOARD | ALL_IN | 11.0 | 7 | 17 | 1 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.635059778796858e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 260 | MOVE_BOARD | ALL_IN | 11.0 | 7 | 17 | 1 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014993376098573208 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 11.0 | 8 | 23 | 2 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10109783709049225 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 11.0 | 8 | 23 | 2 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15848317742347717 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 264 | SELL | ALL_IN | 11.0 | 8 | 23 | 2 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014633333310484886 | 0.0 | 0.0 | +— / -bcd06176-e1d7-43fb-abd4-b6faea8c7927 |
| Jogador 2 | 5-1 | 265 | BUY | ALL_IN | 11.0 | 8 | 24 | 2 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5181174278259277 | 0.0 | 0.0 | +c69a2be1-356a-4576-9887-6d1790221a5e / -— |
| Jogador 2 | 5-1 | 266 | SELL | ALL_IN | 11.0 | 8 | 22 | 2 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -3c59d736-011d-480c-a9af-1df7a3b4caab |
| Jogador 2 | 5-1 | 267 | BUY | ALL_IN | 11.0 | 8 | 24 | 2 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22066795825958252 | 0.0 | 0.0 | +ff181737-4995-4a67-add2-4f55cebabbee / -— |
| Jogador 2 | 5-1 | 268 | SELL | ALL_IN | 11.0 | 8 | 19 | 1 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08579999953508377 | 0.0 | 0.0 | +— / -a2b57772-7a23-4ffd-ace1-d2a7a3f5a7cd |
| Jogador 2 | 5-1 | 269 | BUY | ALL_IN | 11.0 | 8 | 21 | 2 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20410457253456116 | 0.0 | 0.0 | +2949d735-3c16-4a45-835b-e11a9c12b16a / -— |
| Jogador 2 | 5-1 | 270 | SELL | ALL_IN | 11.0 | 8 | 18 | 1 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0745432898402214 | 0.0 | 0.0 | +— / -aaebedb3-18bf-4ae6-948e-7b326b573f1c |
| Jogador 2 | 5-2 | 272 | BUY | ALL_IN | 11.0 | 8 | 29 | 2 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16102908551692963 | 0.0 | 0.0 | +e9bb05f6-3838-423a-bfd2-3791379b479e / -— |
| Jogador 2 | 5-2 | 273 | SELL | ALL_IN | 11.0 | 8 | 25 | 2 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002166666556149721 | 0.0 | 0.0 | +— / -2949d735-3c16-4a45-835b-e11a9c12b16a |
| Jogador 2 | 5-2 | 274 | BUY | ALL_IN | 11.0 | 8 | 28 | 2 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0739355981349945 | 0.0 | 0.0 | +9a96b07c-5b37-4be7-855e-dc2d942e7171 / -— |
| Jogador 2 | 5-2 | 275 | SELL | ALL_IN | 11.0 | 8 | 25 | 2 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -9a96b07c-5b37-4be7-855e-dc2d942e7171 |
| Jogador 2 | 5-2 | 276 | BUY | ALL_IN | 11.0 | 8 | 28 | 2 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0535086914896965 | 0.0 | 0.0 | +1c5a9322-14c8-4df9-937b-842dcaa1f372 / -— |
| Jogador 2 | 5-2 | 277 | SELL | ALL_IN | 11.0 | 8 | 24 | 2 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -1c5a9322-14c8-4df9-937b-842dcaa1f372 |
| Jogador 2 | 5-2 | 278 | BUY | ALL_IN | 11.0 | 8 | 28 | 2 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2742060124874115 | 0.0 | 0.0 | +aee0c45d-0178-4238-987f-5ee83dae7bce / -— |
| Jogador 2 | 5-2 | 279 | SELL | ALL_IN | 11.0 | 8 | 25 | 2 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -aee0c45d-0178-4238-987f-5ee83dae7bce |
| Jogador 2 | 5-2 | 280 | BUY | ALL_IN | 11.0 | 8 | 28 | 2 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2776101231575012 | 0.0 | 0.0 | +5e843c10-0a8b-4781-983a-8e6e6f28253e / -— |
| Jogador 2 | 5-3 | 282 | SELL | ALL_IN | 11.0 | 8 | 35 | 3 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -5e843c10-0a8b-4781-983a-8e6e6f28253e |
| Jogador 2 | 5-3 | 283 | BUY | ALL_IN | 11.0 | 8 | 37 | 3 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07078452408313751 | 0.0 | 0.0 | +eb418af1-c963-4da2-b052-86a153fc5ba1 / -— |
| Jogador 2 | 5-3 | 284 | SELL | ALL_IN | 11.0 | 8 | 33 | 3 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011986893601715565 | 0.0 | 0.0 | +— / -eb418af1-c963-4da2-b052-86a153fc5ba1 |
| Jogador 2 | 5-3 | 285 | BUY | ALL_IN | 11.0 | 8 | 37 | 3 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2359423041343689 | 0.0 | 0.0 | +57ba484a-6228-4263-8171-00a8a5893bea / -— |
| Jogador 2 | 5-3 | 286 | SELL | ALL_IN | 11.0 | 8 | 33 | 3 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0141333332285285 | 0.0 | 0.0 | +— / -57ba484a-6228-4263-8171-00a8a5893bea |
| Jogador 2 | 5-3 | 287 | BUY | ALL_IN | 11.0 | 8 | 37 | 3 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01242435909807682 | 0.0 | 0.0 | +95eba9e8-10f5-48d5-86de-3d9a446b2e65 / -— |
| Jogador 2 | 5-3 | 288 | SELL | ALL_IN | 11.0 | 8 | 34 | 3 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00563333323225379 | 0.0 | 0.0 | +— / -95eba9e8-10f5-48d5-86de-3d9a446b2e65 |
| Jogador 2 | 5-3 | 289 | BUY | ALL_IN | 11.0 | 8 | 37 | 3 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23097939789295197 | 0.0 | 0.0 | +0c96798c-ee23-488b-974f-74e8e3da6aa6 / -— |
| Jogador 2 | 5-3 | 290 | SELL | ALL_IN | 11.0 | 8 | 34 | 3 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010833333246409893 | 0.0 | 0.0 | +— / -0c96798c-ee23-488b-974f-74e8e3da6aa6 |
| Jogador 2 | 5-4 | 292 | BUY | ALL_IN | 11.0 | 8 | 47 | 4 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9651659727096558 | 0.0 | 0.0 | +8da82a9e-0746-43e1-81c3-fa22ec3bb863 / -— |
| Jogador 2 | 5-4 | 293 | SELL | ALL_IN | 11.0 | 8 | 46 | 4 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05079999938607216 | 0.0 | 0.0 | +— / -e9bb05f6-3838-423a-bfd2-3791379b479e |
| Jogador 2 | 5-4 | 294 | BUY | ALL_IN | 11.0 | 8 | 50 | 5 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24544136226177216 | 0.0 | 0.0 | +d30c92eb-1279-4532-b763-7c30826c8430 / -— |
| Jogador 2 | 5-4 | 295 | SELL | ALL_IN | 11.0 | 8 | 45 | 4 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08529999852180481 | 0.0 | 0.0 | +— / -ff181737-4995-4a67-add2-4f55cebabbee |
| Jogador 2 | 5-4 | 296 | BUY | ALL_IN | 11.0 | 8 | 50 | 5 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20827066898345947 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -— |
| Jogador 2 | 5-4 | 297 | SELL | ALL_IN | 11.0 | 8 | 47 | 4 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07783333212137222 | 0.0 | 0.0 | +— / -ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 |
| Jogador 2 | 5-4 | 298 | BUY | ALL_IN | 11.0 | 8 | 50 | 5 | 40.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01298987865447998 | 0.0 | 0.0 | +91eb044c-6989-4b6a-a9fa-a59f75b56743 / -— |
| Jogador 2 | 5-4 | 299 | MOVE_BENCH | ALL_IN | 11.0 | 8 | 49 | 4 | 40.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5939018726348877 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 301 | BUY | ALL_IN | 11.0 | 8 | 59 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14929412305355072 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 2 | 5-5 | 302 | SELL | ALL_IN | 11.0 | 8 | 55 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -0c5adb43-b194-486e-b59c-c0f3b5479d40 |
| Jogador 2 | 5-5 | 303 | BUY | ALL_IN | 11.0 | 8 | 59 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02689114585518837 | 0.0 | 0.0 | +83a3ef65-b342-4ec8-b2d1-be99c3602f81 / -— |
| Jogador 2 | 5-5 | 304 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 56 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 305 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 56 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0148787135258317 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 306 | PASS | ALL_IN | 11.0 | 8 | 56 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4816569983959198 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 312 | SELL | ALL_IN | 11.0 | 8 | 69 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -83a3ef65-b342-4ec8-b2d1-be99c3602f81 |
| Jogador 2 | 5-6 | 313 | BUY | ALL_IN | 11.0 | 8 | 72 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3922366499900818 | 0.0 | 0.0 | +85fb6db6-e1b0-4fa1-b99a-2f205305ef0b / -— |
| Jogador 2 | 5-6 | 314 | SELL | ALL_IN | 11.0 | 8 | 69 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013100703246891499 | 0.0 | 0.0 | +— / -80130f72-2d7c-49db-8d6f-4c0a962260e8 |
| Jogador 2 | 5-6 | 315 | BUY | ALL_IN | 11.0 | 8 | 70 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36821454763412476 | 0.0 | 0.0 | +9f1c634e-13c7-4b59-838c-4b676fa059be / -— |
| Jogador 2 | 5-6 | 316 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 66 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.684499046765268e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 317 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 66 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015136374160647392 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 318 | PASS | ALL_IN | 11.0 | 8 | 66 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4946306049823761 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 322 | SELL | ALL_IN | 11.0 | 8 | 80 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0599694550037384 | 0.0 | 0.0 | +— / -d30c92eb-1279-4532-b763-7c30826c8430 |
| Jogador 2 | 5-7 | 323 | BUY | ALL_IN | 11.0 | 8 | 85 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13077136874198914 | 0.0 | 0.0 | +5de51369-647a-45bd-95b7-c8efe44c5484 / -— |
| Jogador 2 | 5-7 | 324 | SELL | ALL_IN | 11.0 | 8 | 80 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02419999986886978 | 0.0 | 0.0 | +— / -5de51369-647a-45bd-95b7-c8efe44c5484 |
| Jogador 2 | 5-7 | 325 | BUY | ALL_IN | 11.0 | 8 | 85 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14586997032165527 | 0.0 | 0.0 | +c5520bc4-3123-40f3-b275-83fa8cb06309 / -— |
| Jogador 2 | 5-7 | 326 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 82 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 327 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 82 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014887888915836811 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 328 | PASS | ALL_IN | 11.0 | 8 | 82 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5163498520851135 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ALL_IN | 11.0 | 8 | 95 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09588988125324249 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 333 | SELL | ALL_IN | 11.0 | 8 | 95 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5426145195960999 | 0.0 | 0.0 | +— / -20821a31-3317-4f82-bbb2-b70cdebdd893 |
| Jogador 2 | 6-1 | 334 | BUY | ALL_IN | 11.0 | 8 | 97 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0033142685424536467 | 0.0 | 0.0 | +6b7f5603-ce44-4b91-8a3e-939c4fbb26ac / -— |
| Jogador 2 | 6-1 | 335 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 93 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00011064262798754498 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 336 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 93 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999687671661377 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 337 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 93 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999225735664368 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 338 | PASS | ALL_IN | 11.0 | 8 | 93 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5509331822395325 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 342 | SELL | ALL_IN | 11.0 | 8 | 107 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0018272800371050835 | 0.0 | 0.0 | +— / -c69a2be1-356a-4576-9887-6d1790221a5e |
| Jogador 2 | 6-2 | 343 | BUY | ALL_IN | 11.0 | 8 | 109 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.436341255903244 | 0.0 | 0.0 | +5e8a73b8-846a-49a9-be41-30c3baf2cb55 / -— |
| Jogador 2 | 6-2 | 344 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 105 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.3400816644425504e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 345 | SELL | ALL_IN | 11.0 | 8 | 105 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -91eb044c-6989-4b6a-a9fa-a59f75b56743 |
| Jogador 2 | 6-2 | 346 | BUY | ALL_IN | 11.0 | 8 | 106 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016681384295225143 | 0.0 | 0.0 | +3a17cc98-2024-4ac0-b627-9a751d138cd9 / -— |
| Jogador 2 | 6-2 | 347 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 104 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0008360486244782805 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 348 | MOVE_BOARD | ALL_IN | 11.0 | 8 | 104 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016205981373786926 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 349 | PASS | ALL_IN | 11.0 | 8 | 104 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5679250955581665 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 352 | SELL | ALL_IN | 11.0 | 8 | 118 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009708571247756481 | 0.0 | 0.0 | +— / -3a17cc98-2024-4ac0-b627-9a751d138cd9 |
| Jogador 2 | 6-3 | 353 | BUY | ALL_IN | 11.0 | 8 | 120 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10733597725629807 | 0.0 | 0.0 | +b0f8dc80-dd2b-4dde-87a9-b855a1c13da5 / -— |
| Jogador 2 | 6-3 | 354 | SELL | ALL_IN | 11.0 | 8 | 117 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02960343100130558 | 0.0 | 0.0 | +— / -b0f8dc80-dd2b-4dde-87a9-b855a1c13da5 |
| Jogador 2 | 6-3 | 355 | BUY | ALL_IN | 11.0 | 8 | 120 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14997565746307373 | 0.0 | 0.0 | +249d7b90-0660-4e4f-885a-7791c1cac21a / -— |
| Jogador 2 | 6-3 | 356 | SELL | ALL_IN | 11.0 | 8 | 116 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -249d7b90-0660-4e4f-885a-7791c1cac21a |
| Jogador 2 | 6-3 | 357 | BUY | ALL_IN | 11.0 | 8 | 120 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01686917431652546 | 0.0 | 0.0 | +ffd44f6f-388e-4792-ae4f-77f2faa3e95f / -— |
| Jogador 2 | 6-3 | 358 | SELL | ALL_IN | 11.0 | 8 | 116 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0035937561187893152 | 0.0 | 0.0 | +— / -ffd44f6f-388e-4792-ae4f-77f2faa3e95f |
| Jogador 2 | 6-3 | 359 | BUY | ALL_IN | 11.0 | 8 | 120 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023358551785349846 | 0.0 | 0.0 | +54b8f150-85a6-4fad-9a4f-3b04897733cf / -— |
| Jogador 2 | 6-3 | 360 | REROLL | ALL_IN | 11.0 | 8 | 118 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 362 | SELL | ALL_IN | 11.0 | 8 | 130 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -54b8f150-85a6-4fad-9a4f-3b04897733cf |
| Jogador 2 | 6-4 | 363 | BUY | ALL_IN | 11.0 | 8 | 132 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9642468690872192 | 0.0 | 0.0 | +6875f839-cf68-443f-9776-887087b375d3 / -— |
| Jogador 2 | 6-4 | 364 | SELL | ALL_IN | 11.0 | 8 | 129 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5457666516304016 | 0.0 | 0.0 | +— / -85fb6db6-e1b0-4fa1-b99a-2f205305ef0b |
| Jogador 2 | 6-4 | 365 | BUY | ALL_IN | 11.0 | 8 | 132 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022381337359547615 | 0.0 | 0.0 | +80241b75-9eb3-4b89-a754-8df65ec59786 / -— |
| Jogador 2 | 6-4 | 366 | SELL | ALL_IN | 11.0 | 8 | 129 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -80241b75-9eb3-4b89-a754-8df65ec59786 |
| Jogador 2 | 6-4 | 367 | BUY | ALL_IN | 11.0 | 8 | 132 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02454693615436554 | 0.0 | 0.0 | +2328111b-018a-4ca1-a9e7-f7cd9627fd43 / -— |
| Jogador 2 | 6-4 | 368 | SELL | ALL_IN | 11.0 | 8 | 129 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001734966761432588 | 0.0 | 0.0 | +— / -2328111b-018a-4ca1-a9e7-f7cd9627fd43 |
| Jogador 2 | 6-4 | 369 | BUY | ALL_IN | 11.0 | 8 | 132 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27571165561676025 | 0.0 | 0.0 | +d1f4a2a4-f3cb-413d-8ed8-b373fa56f1f2 / -— |
| Jogador 2 | 6-4 | 370 | REROLL | ALL_IN | 11.0 | 8 | 130 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 372 | SELL | ALL_IN | 11.0 | 8 | 141 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -d1f4a2a4-f3cb-413d-8ed8-b373fa56f1f2 |
| Jogador 2 | 6-5 | 373 | BUY | ALL_IN | 11.0 | 8 | 143 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46445131301879883 | 0.0 | 0.0 | +49eaab97-475e-4663-a2b7-61d755bf19ca / -— |
| Jogador 2 | 6-5 | 374 | SELL | ALL_IN | 11.0 | 8 | 142 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.555733323097229 | 0.0 | 0.0 | +— / -6b7f5603-ce44-4b91-8a3e-939c4fbb26ac |
| Jogador 2 | 6-5 | 375 | BUY | ALL_IN | 11.0 | 8 | 146 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14368392527103424 | 0.0 | 0.0 | +b5e5c8e4-7fb5-4b4b-b284-f0794e78eadc / -— |
| Jogador 2 | 6-5 | 376 | SELL | ALL_IN | 11.0 | 8 | 142 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -5e8a73b8-846a-49a9-be41-30c3baf2cb55 |
| Jogador 2 | 6-5 | 377 | BUY | ALL_IN | 11.0 | 8 | 146 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2666355073451996 | 0.0 | 0.0 | +52799e57-7b54-4dc5-b7f8-c39c8f57e7fa / -— |
| Jogador 2 | 6-5 | 378 | SELL | ALL_IN | 11.0 | 8 | 142 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -52799e57-7b54-4dc5-b7f8-c39c8f57e7fa |
| Jogador 2 | 6-5 | 379 | BUY | ALL_IN | 11.0 | 8 | 146 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04044293612241745 | 0.0 | 0.0 | +6f0b2edb-0f61-4838-b698-703f080582a1 / -— |
| Jogador 2 | 6-5 | 380 | SELL | ALL_IN | 11.0 | 8 | 145 | 5 | 42.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -6f0b2edb-0f61-4838-b698-703f080582a1 |
| Jogador 2 | 6-6 | 382 | BUY | ALL_IN | 11.0 | 8 | 160 | 5 | 42.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1117879152297974 | 0.0 | 0.0 | +389bcf7d-1a3c-4360-8bcf-a98cacecbaea / -729ccd5b-adc5-4bca-9523-dcb532e93ecb,e0445166-70a5-4135-a45e-ff238a95b228 |
| Jogador 2 | 6-6 | 383 | MOVE_BENCH | ALL_IN | 11.0 | 8 | 156 | 5 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3313489556312561 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 384 | BUY | ALL_IN | 11.0 | 8 | 156 | 5 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4164472818374634 | 0.0 | 0.0 | +edd9f925-ac58-4285-a53c-ca70b782c682 / -— |
| Jogador 2 | 6-6 | 385 | SELL | ALL_IN | 11.0 | 8 | 153 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7235000133514404 | 0.0 | 0.0 | +— / -389bcf7d-1a3c-4360-8bcf-a98cacecbaea |
| Jogador 2 | 6-6 | 386 | BUY | ALL_IN | 11.0 | 8 | 164 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15116408467292786 | 0.0 | 0.0 | +a960f5cb-d806-4d73-9146-244e1ecde6f2 / -— |
| Jogador 2 | 6-6 | 387 | REROLL | ALL_IN | 11.0 | 8 | 161 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 388 | SELL | ALL_IN | 11.0 | 8 | 159 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -a960f5cb-d806-4d73-9146-244e1ecde6f2 |
| Jogador 2 | 6-6 | 389 | BUY | ALL_IN | 11.0 | 8 | 162 | 5 | 28.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0005853176116943 | 0.0 | 0.0 | +280265b0-7892-4e7e-b654-e2cc7b0ea97b / -— |
| Jogador 2 | 6-6 | 390 | SELL | ALL_IN | 11.0 | 8 | 161 | 5 | 28.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5457666516304016 | 0.0 | 0.0 | +— / -edd9f925-ac58-4285-a53c-ca70b782c682 |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22444601356983185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0904720276594162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40667274594306946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0396608114242554 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.117977499961853 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009961719624698162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5896894335746765 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22690147161483765 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21204201877117157 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 41 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 50 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26404017210006714 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 51 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25187569856643677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 52 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23012398183345795 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3955889344215393 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21845154464244843 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007322629448026419 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 56 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9629704356193542 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 63 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3368203938007355 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 64 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.332294225692749 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2684517502784729 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 75 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8901119828224182 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4073731303215027 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 84 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15196119248867035 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 85 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0855945572257042 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 86 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 87 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07994060218334198 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 88 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01492172572761774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 89 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.898396372795105 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 93 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 94 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012150134891271591 | 0.0 | 0.0 | +— / -5ead8548-7453-4fa1-856e-674995576a48 |
| Jogador 3 | 2-5 | 95 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3835572898387909 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 96 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08108741044998169 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 97 | PASS | STABILIZE | 100.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 102 | BUY | STABILIZE | 94.0 | 5 | 7 | 0 | 22.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9474028944969177 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -c70251e8-af44-4466-808f-d49e9e5f57e9,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 5 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5893630385398865 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 104 | BUY | STABILIZE | 94.0 | 5 | 5 | 0 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499644637107849 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 105 | BUY_XP | STABILIZE | 94.0 | 5 | 4 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 0 | 0 | 24.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0018833595095202327 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 107 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 0 | 0 | 24.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5836116671562195 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 0 | 0 | 28.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015004673041403294 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 109 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 0 | 0 | 28.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 110 | PASS | STABILIZE | 94.0 | 5 | 0 | 0 | 28.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 112 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.893706202507019 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 113 | BUY | STABILIZE | 94.0 | 5 | 3 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3388095498085022 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 114 | BUY | STABILIZE | 94.0 | 5 | 2 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28736773133277893 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 3 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 0 | 0 | 28.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.121690239524469e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 116 | SELL | STABILIZE | 94.0 | 5 | 0 | 0 | 28.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -bca8862c-5e5b-4a51-9173-79218fbfea3d |
| Jogador 3 | 2-7 | 117 | SELL | STABILIZE | 94.0 | 5 | 2 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07099141925573349 | 0.0 | 0.0 | +— / -f19f9e7f-f189-47fe-b571-be5065c6eb39 |
| Jogador 3 | 2-7 | 118 | BUY | STABILIZE | 94.0 | 5 | 4 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2873613238334656 | 0.0 | 0.0 | +60c8a84d-7243-462c-a452-5901135c78b8 / -— |
| Jogador 3 | 2-7 | 119 | SELL | STABILIZE | 94.0 | 5 | 2 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020999999716877937 | 0.0 | 0.0 | +— / -60c8a84d-7243-462c-a452-5901135c78b8 |
| Jogador 3 | 2-7 | 120 | BUY_XP | STABILIZE | 94.0 | 5 | 4 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 122 | BUY | STABILIZE | 94.0 | 6 | 5 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.521328866481781 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -— |
| Jogador 3 | 3-1 | 123 | BUY | STABILIZE | 94.0 | 6 | 3 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2808443009853363 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 0 | 0 | 28.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17379078269004822 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 0 | 0 | 28.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039448320865631104 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 34.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 127 | PASS | STABILIZE | 94.0 | 6 | 0 | 0 | 34.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 132 | BUY | STABILIZE | 94.0 | 6 | 7 | 0 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7119351625442505 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 3-2 | 133 | BUY | STABILIZE | 94.0 | 6 | 6 | 0 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06760329753160477 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 3 | 3-2 | 134 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 135 | BUY | STABILIZE | 94.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.051782846450805664 | 0.0 | 0.0 | +f2020469-2f4e-4b95-96e4-1e7d091f1ab0 / -— |
| Jogador 3 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 2 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 2 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 138 | PASS | STABILIZE | 94.0 | 6 | 2 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 142 | SELL | STABILIZE | 94.0 | 6 | 9 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3357555568218231 | 0.0 | 0.0 | +— / -2d1296a3-9aa4-42ab-8b86-34661e32a63d |
| Jogador 3 | 3-3 | 143 | BUY | STABILIZE | 94.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28594619035720825 | 0.0 | 0.0 | +f0b6c16b-7610-454c-929d-7152f0a041d3 / -— |
| Jogador 3 | 3-3 | 144 | SELL | STABILIZE | 94.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002457842929288745 | 0.0 | 0.0 | +— / -f2020469-2f4e-4b95-96e4-1e7d091f1ab0 |
| Jogador 3 | 3-3 | 145 | BUY | STABILIZE | 94.0 | 6 | 11 | 1 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3381313383579254 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-3 | 146 | BUY_XP | STABILIZE | 94.0 | 6 | 7 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 147 | SELL | STABILIZE | 94.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007286300882697105 | 0.0 | 0.0 | +— / -6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 |
| Jogador 3 | 3-3 | 148 | BUY | STABILIZE | 94.0 | 6 | 6 | 0 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25352299213409424 | 0.0 | 0.0 | +e8b0d22c-35bc-459e-a90c-7db13fcbe34f / -— |
| Jogador 3 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -6.177926024975022e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0148960305377841 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 152 | SELL | STABILIZE | 94.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010833333246409893 | 0.0 | 0.0 | +— / -e8b0d22c-35bc-459e-a90c-7db13fcbe34f |
| Jogador 3 | 3-4 | 153 | BUY | STABILIZE | 94.0 | 6 | 13 | 1 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8000332117080688 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 3 | 3-4 | 154 | SELL | STABILIZE | 94.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5879999995231628 | 0.0 | 0.0 | +— / -e2f28d51-690c-476e-b097-e5c69258f933 |
| Jogador 3 | 3-4 | 155 | BUY | STABILIZE | 94.0 | 6 | 11 | 1 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19408710300922394 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 156 | BUY_XP | STABILIZE | 94.0 | 6 | 8 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 157 | BUY_XP | STABILIZE | 94.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 34.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 34.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 160 | PASS | STABILIZE | 94.0 | 6 | 0 | 0 | 34.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 162 | SELL | STABILIZE | 94.0 | 6 | 6 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -ab6084b0-65df-4a70-8591-687b320d98b6 |
| Jogador 3 | 3-5 | 163 | BUY | STABILIZE | 94.0 | 6 | 8 | 0 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8323454260826111 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -c3f8419e-a450-4247-bb65-8de8dba1c8ee,d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 3 | 3-5 | 164 | BUY | STABILIZE | 94.0 | 6 | 5 | 0 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2761324942111969 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 2 | 0 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 2 | 0 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 167 | PASS | STABILIZE | 94.0 | 6 | 2 | 0 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 172 | BUY | STABILIZE | 83.0 | 6 | 7 | 0 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8059395551681519 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -— |
| Jogador 3 | 3-6 | 173 | SELL | STABILIZE | 83.0 | 6 | 5 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -a9c52953-4532-455b-851f-04079adfd354 |
| Jogador 3 | 3-6 | 174 | BUY | STABILIZE | 83.0 | 6 | 13 | 1 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.795692503452301 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 3 | 3-6 | 175 | SELL | STABILIZE | 83.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -f5c14a50-b095-4a36-995f-2a8514e46f1c |
| Jogador 3 | 3-6 | 176 | BUY | STABILIZE | 83.0 | 6 | 13 | 1 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014448318630456924 | 0.0 | 0.0 | +1489b596-9339-407a-b49f-d01ecfdd6f78 / -— |
| Jogador 3 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.926351099740714e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015113059431314468 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 179 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 180 | PASS | STABILIZE | 83.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 182 | SELL | STABILIZE | 72.0 | 6 | 19 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0656699687242508 | 0.0 | 0.0 | +— / -1489b596-9339-407a-b49f-d01ecfdd6f78 |
| Jogador 3 | 3-7 | 183 | BUY | STABILIZE | 72.0 | 6 | 20 | 2 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2085704356431961 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-7 | 184 | SELL | STABILIZE | 72.0 | 6 | 17 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49430060386657715 | 0.0 | 0.0 | +— / -2fa86b11-4e28-4652-890e-f00a79068223 |
| Jogador 3 | 3-7 | 185 | BUY | STABILIZE | 72.0 | 6 | 19 | 1 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3484942317008972 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 186 | BUY_XP | STABILIZE | 72.0 | 6 | 16 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 187 | BUY_XP | STABILIZE | 72.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03784000128507614 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 188 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5688921809196472 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 189 | BUY | FAST8 | 72.0 | 7 | 8 | 0 | 38.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06750371307134628 | 0.0 | 0.0 | +cbcde5b6-8f03-4d96-ade5-1ef113ab25bc / -— |
| Jogador 3 | 3-7 | 190 | MOVE_BOARD | FAST8 | 72.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00014768475375603884 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 72.0 | 7 | 13 | 1 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07265005260705948 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 72.0 | 7 | 13 | 1 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08506087213754654 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 194 | SELL | FAST8 | 72.0 | 7 | 13 | 1 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02176666632294655 | 0.0 | 0.0 | +— / -cbcde5b6-8f03-4d96-ade5-1ef113ab25bc |
| Jogador 3 | 4-1 | 195 | BUY | FAST8 | 72.0 | 7 | 14 | 1 | 38.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7321086525917053 | 0.0 | 0.0 | +15d93457-0760-419e-87db-74223c1cb7f4 / -— |
| Jogador 3 | 4-1 | 196 | MOVE_BOARD | FAST8 | 72.0 | 7 | 11 | 1 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 197 | MOVE_BOARD | FAST8 | 72.0 | 7 | 11 | 1 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 198 | PASS | FAST8 | 72.0 | 7 | 11 | 1 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 202 | SELL | FAST8 | 60.0 | 7 | 18 | 1 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019411278888583183 | 0.0 | 0.0 | +— / -41db1132-4e1c-48eb-8a9b-1b2c74cb22ce |
| Jogador 3 | 4-2 | 203 | BUY | FAST8 | 60.0 | 7 | 20 | 2 | 38.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28486135601997375 | 0.0 | 0.0 | +0534477f-2ff8-47a7-b71b-1a1d5430589e / -— |
| Jogador 3 | 4-2 | 204 | MOVE_BOARD | FAST8 | 60.0 | 7 | 16 | 1 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 205 | MOVE_BOARD | FAST8 | 60.0 | 7 | 16 | 1 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 206 | PASS | FAST8 | 60.0 | 7 | 16 | 1 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025714285671710968 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 212 | SELL | FAST8 | 60.0 | 7 | 23 | 2 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -0534477f-2ff8-47a7-b71b-1a1d5430589e |
| Jogador 3 | 4-3 | 213 | BUY | FAST8 | 60.0 | 7 | 27 | 2 | 38.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03738696500658989 | 0.0 | 0.0 | +2001a193-3868-4a3f-8a71-3a9f95c04a02 / -— |
| Jogador 3 | 4-3 | 214 | MOVE_BOARD | FAST8 | 60.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00016898124886211008 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 215 | MOVE_BOARD | FAST8 | 60.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014845519326627254 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 216 | MOVE_BOARD | FAST8 | 60.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014887535013258457 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 217 | PASS | FAST8 | 60.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03142857179045677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 222 | MOVE_BOARD | FAST8 | 60.0 | 7 | 33 | 3 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.1695074944291264e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 223 | MOVE_BOARD | FAST8 | 60.0 | 7 | 33 | 3 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 224 | PASS | FAST8 | 60.0 | 7 | 33 | 3 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037857141345739365 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 232 | SELL | FAST8 | 60.0 | 7 | 42 | 4 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -2001a193-3868-4a3f-8a71-3a9f95c04a02 |
| Jogador 3 | 4-5 | 233 | BUY | FAST8 | 60.0 | 7 | 45 | 4 | 38.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.853220522403717 | 0.0 | 0.0 | +61362365-2cf7-40e4-95f9-98e28728fd39 / -15d93457-0760-419e-87db-74223c1cb7f4,bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed |
| Jogador 3 | 4-5 | 234 | BUY | FAST8 | 60.0 | 7 | 42 | 4 | 38.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7717179656028748 | 0.0 | 0.0 | +1ff42607-ccac-4d3f-8277-bccddf08862f / -aaa84ce8-7919-4ec3-92eb-cc03a9decca9,b75c9bc5-9bc7-465a-a97c-59156e5c482d |
| Jogador 3 | 4-5 | 235 | BUY | FAST8 | 60.0 | 7 | 39 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06921897828578949 | 0.0 | 0.0 | +9cc98c55-1b3a-4b31-ae06-f66098e86e8f / -— |
| Jogador 3 | 4-5 | 236 | BUY | FAST8 | 60.0 | 7 | 36 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11868032068014145 | 0.0 | 0.0 | +a72137b3-498b-40e1-938a-639f56745f08 / -— |
| Jogador 3 | 4-5 | 237 | MOVE_BOARD | FAST8 | 60.0 | 7 | 34 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 238 | MOVE_BOARD | FAST8 | 60.0 | 7 | 34 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 239 | PASS | FAST8 | 60.0 | 7 | 34 | 3 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1785714328289032 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 242 | BUY | FAST8 | 60.0 | 7 | 44 | 4 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29800763726234436 | 0.0 | 0.0 | +5c43307a-6d61-4493-a1ed-cb428d79a254 / -— |
| Jogador 3 | 4-6 | 243 | MOVE_BOARD | FAST8 | 60.0 | 7 | 43 | 4 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 244 | MOVE_BOARD | FAST8 | 60.0 | 7 | 43 | 4 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015153384767472744 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 245 | PASS | FAST8 | 60.0 | 7 | 43 | 4 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 252 | SELL | FAST8 | 60.0 | 7 | 54 | 5 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -61362365-2cf7-40e4-95f9-98e28728fd39 |
| Jogador 3 | 4-7 | 253 | BUY | FAST8 | 60.0 | 7 | 62 | 5 | 38.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6256738901138306 | 0.0 | 0.0 | +2f5d8cb8-8ba3-45e9-a345-00e931d34490 / -— |
| Jogador 3 | 4-7 | 254 | SELL | FAST8 | 60.0 | 7 | 58 | 5 | 38.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -1ff42607-ccac-4d3f-8277-bccddf08862f |
| Jogador 3 | 4-7 | 255 | BUY | FAST8 | 60.0 | 7 | 66 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6496092081069946 | 0.0 | 0.0 | +2f2ff445-f60a-4a05-b37a-41b8a6d6c7f9 / -— |
| Jogador 3 | 4-7 | 256 | SELL | FAST8 | 60.0 | 7 | 64 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07013333588838577 | 0.0 | 0.0 | +— / -9cc98c55-1b3a-4b31-ae06-f66098e86e8f |
| Jogador 3 | 4-7 | 257 | BUY | FAST8 | 60.0 | 7 | 67 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2972375750541687 | 0.0 | 0.0 | +d6a929d8-6d7c-4bcd-880d-d819daca2ae0 / -— |
| Jogador 3 | 4-7 | 258 | MOVE_BOARD | FAST8 | 60.0 | 7 | 64 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 259 | MOVE_BOARD | FAST8 | 60.0 | 7 | 64 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015002410858869553 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 260 | PASS | FAST8 | 60.0 | 7 | 64 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08862585574388504 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 60.0 | 7 | 75 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22150222957134247 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 60.0 | 7 | 75 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15775145590305328 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 264 | SELL | FAST8 | 60.0 | 7 | 75 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -5c43307a-6d61-4493-a1ed-cb428d79a254 |
| Jogador 3 | 5-1 | 265 | BUY | FAST8 | 60.0 | 7 | 76 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9051365852355957 | 0.0 | 0.0 | +9af900db-c181-448a-9736-30f08f062a00 / -2f2ff445-f60a-4a05-b37a-41b8a6d6c7f9,a72137b3-498b-40e1-938a-639f56745f08 |
| Jogador 3 | 5-1 | 266 | BUY | FAST8 | 60.0 | 7 | 74 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06522148847579956 | 0.0 | 0.0 | +77489602-9456-4a97-aa7e-df7ef91d5e4a / -— |
| Jogador 3 | 5-1 | 267 | BUY | FAST8 | 60.0 | 7 | 73 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27211663126945496 | 0.0 | 0.0 | +678a6f43-ca48-46c9-8c5b-6790493f4841 / -— |
| Jogador 3 | 5-1 | 268 | SELL | FAST8 | 60.0 | 7 | 72 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1301722675561905 | 0.0 | 0.0 | +— / -9af900db-c181-448a-9736-30f08f062a00 |
| Jogador 3 | 5-1 | 269 | BUY | FAST8 | 60.0 | 7 | 77 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6096370816230774 | 0.0 | 0.0 | +e270a6b1-23dd-49a0-8694-ba911eae4c71 / -— |
| Jogador 3 | 5-1 | 270 | MOVE_BOARD | FAST8 | 60.0 | 7 | 76 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 272 | SELL | FAST8 | 60.0 | 7 | 89 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025066666305065155 | 0.0 | 0.0 | +— / -77489602-9456-4a97-aa7e-df7ef91d5e4a |
| Jogador 3 | 5-2 | 273 | BUY | FAST8 | 60.0 | 7 | 90 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8708939552307129 | 0.0 | 0.0 | +d22aa2b7-7c7c-4d47-89be-0f1b8755971c / -— |
| Jogador 3 | 5-2 | 274 | SELL | FAST8 | 60.0 | 7 | 89 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4372999966144562 | 0.0 | 0.0 | +— / -678a6f43-ca48-46c9-8c5b-6790493f4841 |
| Jogador 3 | 5-2 | 275 | BUY | FAST8 | 60.0 | 7 | 90 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0214680228382349 | 0.0 | 0.0 | +45b96060-6eda-4d0b-9012-e80db31b71d2 / -— |
| Jogador 3 | 5-2 | 276 | SELL | FAST8 | 60.0 | 7 | 87 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006866666488349438 | 0.0 | 0.0 | +— / -e270a6b1-23dd-49a0-8694-ba911eae4c71 |
| Jogador 3 | 5-2 | 277 | BUY | FAST8 | 60.0 | 7 | 88 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03790240362286568 | 0.0 | 0.0 | +b6883c6a-7149-4088-8506-20bd8dfed6a5 / -— |
| Jogador 3 | 5-2 | 278 | MOVE_BOARD | FAST8 | 60.0 | 7 | 86 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 279 | MOVE_BOARD | FAST8 | 60.0 | 7 | 86 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 280 | PASS | FAST8 | 60.0 | 7 | 86 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11481554806232452 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 282 | SELL | FAST8 | 60.0 | 7 | 100 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03078462928533554 | 0.0 | 0.0 | +— / -b6883c6a-7149-4088-8506-20bd8dfed6a5 |
| Jogador 3 | 5-3 | 283 | BUY | FAST8 | 60.0 | 7 | 102 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13365867733955383 | 0.0 | 0.0 | +d2afd490-f89f-47c9-8279-a88acde5b1b6 / -— |
| Jogador 3 | 5-3 | 284 | SELL | FAST8 | 60.0 | 7 | 99 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4295550286769867 | 0.0 | 0.0 | +— / -9028d514-586b-4d0e-b042-07389323c8cf |
| Jogador 3 | 5-3 | 285 | BUY | FAST8 | 60.0 | 7 | 102 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15820027887821198 | 0.0 | 0.0 | +f00a538c-0607-4d8b-babe-7c13daf80c42 / -— |
| Jogador 3 | 5-3 | 286 | MOVE_BOARD | FAST8 | 60.0 | 7 | 99 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.25858223834075e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 287 | MOVE_BOARD | FAST8 | 60.0 | 7 | 99 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 288 | MOVE_BOARD | FAST8 | 60.0 | 7 | 99 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 289 | PASS | FAST8 | 60.0 | 7 | 99 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12564173340797424 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 292 | SELL | FAST8 | 44.0 | 7 | 109 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006986371008679271 | 0.0 | 0.0 | +— / -f00a538c-0607-4d8b-babe-7c13daf80c42 |
| Jogador 3 | 5-4 | 293 | BUY | FAST8 | 44.0 | 7 | 112 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9525918364524841 | 0.0 | 0.0 | +0e5921d4-a056-4f42-951e-93de5f2834bb / -0e31b1ec-3ead-480e-8577-f59bb5486d00,f0b6c16b-7610-454c-929d-7152f0a041d3 |
| Jogador 3 | 5-4 | 294 | BUY | STABILIZE | 44.0 | 7 | 110 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34758955240249634 | 0.0 | 0.0 | +babdcded-7f64-4c88-a087-ff2e10b58b8d / -— |
| Jogador 3 | 5-4 | 295 | SELL | STABILIZE | 44.0 | 7 | 108 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8500000238418579 | 0.0 | 0.0 | +— / -0e5921d4-a056-4f42-951e-93de5f2834bb |
| Jogador 3 | 5-4 | 296 | BUY | STABILIZE | 44.0 | 7 | 113 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1816088855266571 | 0.0 | 0.0 | +edd2748e-d629-4a8a-8174-4c1ef3f5f852 / -— |
| Jogador 3 | 5-4 | 297 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 110 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 298 | SELL | STABILIZE | 44.0 | 7 | 110 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -edd2748e-d629-4a8a-8174-4c1ef3f5f852 |
| Jogador 3 | 5-4 | 299 | MOVE_BENCH | STABILIZE | 44.0 | 7 | 113 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42710068821907043 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 301 | BUY | FAST8 | 44.0 | 7 | 123 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10442976653575897 | 0.0 | 0.0 | +01c587bb-ca4f-4690-9e4b-d1e9c44fd33e / -— |
| Jogador 3 | 5-5 | 302 | BUY | FAST8 | 44.0 | 7 | 120 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15594112873077393 | 0.0 | 0.0 | +d3fddd9d-ee81-418d-9c58-0baa4ed99f61 / -— |
| Jogador 3 | 5-5 | 303 | MOVE_BOARD | FAST8 | 44.0 | 7 | 115 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 304 | MOVE_BOARD | FAST8 | 44.0 | 7 | 115 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 305 | PASS | FAST8 | 44.0 | 7 | 115 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.147039532661438 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 312 | SELL | STABILIZE | 29.0 | 7 | 126 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -01c587bb-ca4f-4690-9e4b-d1e9c44fd33e |
| Jogador 3 | 5-6 | 313 | BUY | STABILIZE | 29.0 | 7 | 129 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17350837588310242 | 0.0 | 0.0 | +8068dc77-9528-4a1d-b4dc-5ac216e8684f / -— |
| Jogador 3 | 5-6 | 314 | SELL | STABILIZE | 29.0 | 7 | 126 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -8068dc77-9528-4a1d-b4dc-5ac216e8684f |
| Jogador 3 | 5-6 | 315 | BUY | STABILIZE | 29.0 | 7 | 129 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24589060246944427 | 0.0 | 0.0 | +3365b4aa-125c-4f72-bcc5-01c5a205b9b0 / -— |
| Jogador 3 | 5-6 | 316 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 125 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 317 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 125 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 318 | PASS | STABILIZE | 29.0 | 7 | 125 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20250920951366425 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 322 | SELL | ALL_IN | 12.0 | 7 | 136 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -3365b4aa-125c-4f72-bcc5-01c5a205b9b0 |
| Jogador 3 | 5-7 | 323 | BUY | ALL_IN | 12.0 | 7 | 140 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.058367133140564 | 0.0 | 0.0 | +194da7dc-39b4-40e3-869d-326ace65137b / -79786887-d318-4836-b2f0-c0f03e86cbe5,8a68772c-3f02-4f2e-882b-4fa69fbb6750 |
| Jogador 3 | 5-7 | 324 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 137 | 5 | 28.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2574743926525116 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 325 | BUY | ALL_IN | 12.0 | 7 | 137 | 5 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4979683756828308 | 0.0 | 0.0 | +2a2b613e-8850-4c70-ab66-bc18356178e8 / -— |
| Jogador 3 | 5-7 | 326 | SELL | ALL_IN | 12.0 | 7 | 136 | 5 | 30.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7167999744415283 | 0.0 | 0.0 | +— / -194da7dc-39b4-40e3-869d-326ace65137b |
| Jogador 3 | 5-7 | 327 | BUY | ALL_IN | 12.0 | 7 | 144 | 5 | 30.0 | Colosso/DA_Lux18_Blackthorn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39037206768989563 | 0.0 | 0.0 | +1ad1f705-7e6b-4c1f-811c-2863dbf2db9e / -— |
| Jogador 3 | 5-7 | 328 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 141 | 5 | 30.0 | Colosso/DA_Lux18_Blackthorn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3952369689941406 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 329 | REROLL | ALL_IN | 12.0 | 7 | 141 | 5 | 34.0 | Colosso/DA_Lux18_Blackthorn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 330 | SELL | ALL_IN | 12.0 | 7 | 139 | 5 | 34.0 | Colosso/DA_Lux18_Blackthorn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02419999986886978 | 0.0 | 0.0 | +— / -d3fddd9d-ee81-418d-9c58-0baa4ed99f61 |
| Jogador 3 | 6-1 | 332 | BUY | ALL_IN | 12.0 | 7 | 155 | 5 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7448980808258057 | 0.0 | 0.0 | +aa803972-8af8-46d7-b430-079819730c36 / -— |
| Jogador 3 | 6-1 | 333 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 7 | 152 | 5 | 34.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0652429386973381 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 334 | SELL | ALL_IN | 12.0 | 7 | 152 | 5 | 34.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7077000141143799 | 0.0 | 0.0 | +— / -2a2b613e-8850-4c70-ab66-bc18356178e8 |
| Jogador 3 | 6-1 | 335 | BUY | ALL_IN | 12.0 | 7 | 153 | 5 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.040115825831890106 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -— |
| Jogador 3 | 6-1 | 336 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 150 | 5 | 34.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5284400582313538 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 337 | BUY | ALL_IN | 12.0 | 7 | 150 | 5 | 36.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03935350850224495 | 0.0 | 0.0 | +dc423197-9320-4651-b71d-a62086416f9d / -— |
| Jogador 3 | 6-1 | 338 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 148 | 5 | 36.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.4587301342980936e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 339 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 148 | 5 | 36.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01567547582089901 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 340 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 148 | 5 | 36.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01432458870112896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2201479971408844 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09193183481693268 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4641140401363373 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16314318776130676 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0601743720471859 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0128185749053955 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3392305076122284 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 39 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 50 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9802137017250061 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 51 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18394431471824646 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 52 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2162981927394867 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 53 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 54 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39172792434692383 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9557392001152039 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 63 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 64 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 72 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9438801407814026 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 73 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0434482097625732 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 74 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30417701601982117 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 75 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Camille | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5619999766349792 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 76 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 77 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10036245733499527 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 79 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5416666865348816 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-3 | 80 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1373056173324585 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2375916838645935 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15833333134651184 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005146525800228119 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11433333158493042 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08100000023841858 | 0.0 | 0.0 | +— / -0b62545c-1de0-47d8-bb4c-119f7e1526b3 |
| Jogador 4 | 2-4 | 89 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24982136487960815 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 90 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9548463821411133 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 4 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0011241436004639 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -86c535a4-a22b-4667-bc0f-46b4843d97cc,8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38447263836860657 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 4 | 2-5 | 94 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20774511992931366 | 0.0 | 0.0 | +— / -4b07138d-44fd-4515-8b65-d7db84f4639c |
| Jogador 4 | 2-5 | 96 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2166287750005722 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39750707149505615 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 98 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5793910026550293 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 2-5 | 99 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013034125789999962 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.329289972782135 | 0.0 | 0.0 | +f71a7192-663d-46a0-93ef-b900c59c3bde / -— |
| Jogador 4 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 6 | 5 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06815066188573837 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21333634853363037 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04971316084265709 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 106 | PASS | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 112 | BUY | STABILIZE | 88.0 | 6 | 6 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38963407278060913 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 113 | BUY | STABILIZE | 88.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19012689590454102 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -— |
| Jogador 4 | 2-7 | 114 | SELL | STABILIZE | 88.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41841304302215576 | 0.0 | 0.0 | +— / -4a0403a3-c999-4d4c-83f0-7270e8576aed |
| Jogador 4 | 2-7 | 115 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.310269832611084 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 116 | SELL | STABILIZE | 88.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09433333575725555 | 0.0 | 0.0 | +— / -b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a |
| Jogador 4 | 2-7 | 117 | BUY_XP | STABILIZE | 88.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 118 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16936028003692627 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014632930979132652 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 120 | BUY | STABILIZE | 88.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10269292443990707 | 0.0 | 0.0 | +53a27943-148b-4522-9826-3f2e0b8a7858 / -— |
| Jogador 4 | 3-1 | 122 | BUY | STABILIZE | 88.0 | 6 | 6 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8031469583511353 | 0.0 | 0.0 | +8052731e-e34c-4de7-84b1-2b986cfeddaa / -— |
| Jogador 4 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 88.0 | 6 | 4 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24285174906253815 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 124 | BUY_XP | STABILIZE | 88.0 | 6 | 4 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 125 | SELL | STABILIZE | 88.0 | 6 | 0 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05220000073313713 | 0.0 | 0.0 | +— / -53a27943-148b-4522-9826-3f2e0b8a7858 |
| Jogador 4 | 3-1 | 126 | BUY | STABILIZE | 88.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04126187041401863 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 127 | SELL | STABILIZE | 88.0 | 6 | 0 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 3-1 | 128 | SELL | STABILIZE | 88.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2303333282470703 | 0.0 | 0.0 | +— / -5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-1 | 129 | BUY_XP | STABILIZE | 88.0 | 6 | 5 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 130 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 1 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00013458005560096353 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 132 | BUY | STABILIZE | 76.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.837992787361145 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 133 | BUY | STABILIZE | 76.0 | 6 | 6 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879989445209503 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 5 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5546117424964905 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 135 | BUY_XP | STABILIZE | 76.0 | 6 | 5 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 1 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01178455539047718 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 137 | SELL | STABILIZE | 76.0 | 6 | 1 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 3-2 | 138 | EQUIP_FROM_INVENTORY | STABILIZE | 76.0 | 6 | 4 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12787555158138275 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 139 | EQUIP_FROM_INVENTORY | STABILIZE | 76.0 | 6 | 4 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12188177555799484 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 140 | EQUIP_FROM_INVENTORY | STABILIZE | 76.0 | 6 | 4 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0995163768529892 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 142 | BUY | STABILIZE | 65.0 | 6 | 10 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7558249235153198 | 0.0 | 0.0 | +52018505-08c9-471f-83b9-fd5066efe55a / -8052731e-e34c-4de7-84b1-2b986cfeddaa,c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 4 | 3-3 | 143 | BUY_XP | STABILIZE | 65.0 | 6 | 8 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 144 | BUY_XP | STABILIZE | 65.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02827499993145466 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 145 | MOVE_BENCH | STABILIZE | 65.0 | 7 | 0 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.348833829164505 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 0 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012709405273199081 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 147 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 0 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013698259368538857 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 148 | PASS | STABILIZE | 65.0 | 7 | 0 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 152 | BUY | STABILIZE | 65.0 | 7 | 6 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28172567486763 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 153 | BUY | STABILIZE | 65.0 | 7 | 3 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23322336375713348 | 0.0 | 0.0 | +e01be6cf-34fe-4057-aef3-c08c504794cf / -— |
| Jogador 4 | 3-4 | 154 | BUY | STABILIZE | 65.0 | 7 | 1 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17582087218761444 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -— |
| Jogador 4 | 3-4 | 155 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 0 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.48598327441141e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 156 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 0 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 157 | PASS | STABILIZE | 65.0 | 7 | 0 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 162 | BUY | STABILIZE | 65.0 | 7 | 5 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8028365969657898 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 4 | 3-5 | 163 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 2 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.658543811179698e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 164 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 2 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 2 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 166 | PASS | STABILIZE | 65.0 | 7 | 2 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 172 | BUY | STABILIZE | 65.0 | 7 | 9 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2859177589416504 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -— |
| Jogador 4 | 3-6 | 173 | BUY | STABILIZE | 65.0 | 7 | 7 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10006819665431976 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 174 | BUY | STABILIZE | 65.0 | 7 | 4 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06878025829792023 | 0.0 | 0.0 | +f722cd46-0c4e-42e7-80ff-4b910c28d572 / -— |
| Jogador 4 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 1 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.9905312809860334e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 1 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019898544996976852 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 1 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010079379193484783 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 178 | PASS | STABILIZE | 65.0 | 7 | 1 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 182 | BUY | STABILIZE | 65.0 | 7 | 8 | 0 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.833499014377594 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,40f2a32f-1ace-4700-8a79-e6b5d3212036 |
| Jogador 4 | 3-7 | 183 | BUY | STABILIZE | 65.0 | 7 | 5 | 0 | 30.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34598439931869507 | 0.0 | 0.0 | +59f588eb-e3f3-4907-ab23-af073a26bd6a / -— |
| Jogador 4 | 3-7 | 184 | BUY | STABILIZE | 65.0 | 7 | 2 | 0 | 30.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21780440211296082 | 0.0 | 0.0 | +e3fdce1f-991f-4305-9aaa-fbf72ede6c01 / -— |
| Jogador 4 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 0 | 0 | 30.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00023748962848912925 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 0 | 0 | 30.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015018709935247898 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 187 | PASS | STABILIZE | 65.0 | 7 | 0 | 0 | 30.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 192 | BUY | STABILIZE | 65.0 | 7 | 6 | 0 | 30.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.796880304813385 | 0.0 | 0.0 | +42733dbd-0bc3-461b-95ab-76daf5ad6296 / -— |
| Jogador 4 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 65.0 | 7 | 3 | 0 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15875931084156036 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 65.0 | 7 | 3 | 0 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21661390364170074 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 195 | SELL | STABILIZE | 65.0 | 7 | 3 | 0 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03999999910593033 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 4 | 4-1 | 196 | BUY | STABILIZE | 65.0 | 7 | 11 | 1 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015506031922996044 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -— |
| Jogador 4 | 4-1 | 197 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 9 | 0 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 9 | 0 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37051910161972046 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 199 | PASS | STABILIZE | 65.0 | 7 | 9 | 0 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 202 | SELL | STABILIZE | 53.0 | 7 | 14 | 1 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.061106473207473755 | 0.0 | 0.0 | +— / -d754fcfc-6d22-4bc0-8643-8f4bef9afda5 |
| Jogador 4 | 4-2 | 203 | BUY | STABILIZE | 53.0 | 7 | 15 | 1 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8059033751487732 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -— |
| Jogador 4 | 4-2 | 204 | SELL | STABILIZE | 53.0 | 7 | 13 | 1 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -210d2415-663d-4768-bbc2-238766c2b863 |
| Jogador 4 | 4-2 | 205 | BUY | STABILIZE | 53.0 | 7 | 15 | 1 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7478047013282776 | 0.0 | 0.0 | +55944609-f4df-4e53-a1d1-31c79a148b22 / -— |
| Jogador 4 | 4-2 | 206 | SELL | STABILIZE | 53.0 | 7 | 13 | 1 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04353923350572586 | 0.0 | 0.0 | +— / -8e1a5a7a-d27d-47c9-a197-b383c1c3da3b |
| Jogador 4 | 4-2 | 207 | BUY | STABILIZE | 53.0 | 7 | 16 | 1 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23007355630397797 | 0.0 | 0.0 | +f394f34c-c68b-4213-9eb0-88f302976405 / -— |
| Jogador 4 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 53.0 | 7 | 15 | 1 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012766991276293993 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 209 | SELL | STABILIZE | 53.0 | 7 | 15 | 1 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41584450006484985 | 0.0 | 0.0 | +— / -59f588eb-e3f3-4907-ab23-af073a26bd6a |
| Jogador 4 | 4-2 | 210 | BUY | STABILIZE | 53.0 | 7 | 18 | 1 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011047953739762306 | 0.0 | 0.0 | +090f2ba6-5514-49ba-a80d-a0711cd06245 / -— |
| Jogador 4 | 4-3 | 212 | SELL | STABILIZE | 41.0 | 7 | 21 | 2 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010619296692311764 | 0.0 | 0.0 | +— / -f722cd46-0c4e-42e7-80ff-4b910c28d572 |
| Jogador 4 | 4-3 | 213 | BUY | STABILIZE | 41.0 | 7 | 24 | 2 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8659180402755737 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -23f4d10f-2614-47b2-bfb2-4fb276764b5e,4363594b-375b-45d4-9b1a-0c1ab96367a1 |
| Jogador 4 | 4-3 | 214 | BUY | STABILIZE | 41.0 | 7 | 22 | 2 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21706421673297882 | 0.0 | 0.0 | +7b3e8122-3b51-46b5-94a8-68fb77156e0e / -— |
| Jogador 4 | 4-3 | 215 | BUY | STABILIZE | 41.0 | 7 | 19 | 1 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12487958371639252 | 0.0 | 0.0 | +26462e09-ab6e-4b87-85a8-6bda974b0c45 / -— |
| Jogador 4 | 4-3 | 216 | SELL | STABILIZE | 41.0 | 7 | 15 | 1 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7534999847412109 | 0.0 | 0.0 | +— / -3bbd7105-b508-437d-ac84-11e01a499779 |
| Jogador 4 | 4-3 | 217 | BUY | STABILIZE | 41.0 | 7 | 20 | 2 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004717550706118345 | 0.0 | 0.0 | +60138930-82d5-4f1c-a5fe-a22ea4b70d36 / -— |
| Jogador 4 | 4-3 | 218 | REROLL | STABILIZE | 41.0 | 7 | 17 | 1 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20399999618530273 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 219 | SELL | STABILIZE | 41.0 | 7 | 15 | 1 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -60138930-82d5-4f1c-a5fe-a22ea4b70d36 |
| Jogador 4 | 4-3 | 220 | BUY | STABILIZE | 41.0 | 7 | 18 | 1 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2859179973602295 | 0.0 | 0.0 | +a7893c5d-2faa-4292-9240-f3cc5813151e / -— |
| Jogador 4 | 4-4 | 222 | SELL | STABILIZE | 41.0 | 7 | 23 | 2 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0075333332642912865 | 0.0 | 0.0 | +— / -090f2ba6-5514-49ba-a80d-a0711cd06245 |
| Jogador 4 | 4-4 | 223 | BUY | STABILIZE | 41.0 | 7 | 27 | 2 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24403034150600433 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -— |
| Jogador 4 | 4-4 | 224 | SELL | STABILIZE | 41.0 | 7 | 23 | 2 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0141333332285285 | 0.0 | 0.0 | +— / -ad19ac66-9f86-4c29-8ae7-7222164aece1 |
| Jogador 4 | 4-4 | 225 | BUY | STABILIZE | 41.0 | 7 | 27 | 2 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049745913594961166 | 0.0 | 0.0 | +e4764e13-e26d-4358-980a-c7c625e26726 / -— |
| Jogador 4 | 4-4 | 226 | SELL | STABILIZE | 41.0 | 7 | 24 | 2 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00563333323225379 | 0.0 | 0.0 | +— / -e4764e13-e26d-4358-980a-c7c625e26726 |
| Jogador 4 | 4-4 | 227 | BUY | STABILIZE | 41.0 | 7 | 27 | 2 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23210348188877106 | 0.0 | 0.0 | +b80a9778-b2ce-411b-8d08-24549c04367c / -— |
| Jogador 4 | 4-4 | 228 | SELL | STABILIZE | 41.0 | 7 | 24 | 2 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -b80a9778-b2ce-411b-8d08-24549c04367c |
| Jogador 4 | 4-4 | 229 | MOVE_BOARD | STABILIZE | 41.0 | 7 | 27 | 2 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09308589994907379 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 230 | MOVE_BOARD | STABILIZE | 41.0 | 7 | 27 | 2 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030821869149804115 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 232 | BUY | STABILIZE | 41.0 | 7 | 34 | 3 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13750645518302917 | 0.0 | 0.0 | +f99cdd31-4a55-4a5e-941a-2800b8afdd7a / -— |
| Jogador 4 | 4-5 | 233 | MOVE_BOARD | STABILIZE | 41.0 | 7 | 30 | 3 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0759873315691948 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 234 | SELL | STABILIZE | 41.0 | 7 | 30 | 3 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03266666829586029 | 0.0 | 0.0 | +— / -f99cdd31-4a55-4a5e-941a-2800b8afdd7a |
| Jogador 4 | 4-5 | 235 | BUY | STABILIZE | 41.0 | 7 | 34 | 3 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23222871124744415 | 0.0 | 0.0 | +31ea6d79-501d-4f2a-821d-7058334be82f / -— |
| Jogador 4 | 4-5 | 236 | MOVE_BOARD | STABILIZE | 41.0 | 7 | 31 | 3 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.51782679092139e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 237 | MOVE_BOARD | STABILIZE | 41.0 | 7 | 31 | 3 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014697014354169369 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 41.0 | 7 | 31 | 3 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021919142454862595 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 41.0 | 7 | 31 | 3 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022992810234427452 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 240 | MOVE_BOARD | STABILIZE | 41.0 | 7 | 31 | 3 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0137708755210042 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 242 | SELL | STABILIZE | 29.0 | 7 | 39 | 3 | 30.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08910000324249268 | 0.0 | 0.0 | +— / -31ea6d79-501d-4f2a-821d-7058334be82f |
| Jogador 4 | 4-6 | 243 | BUY | STABILIZE | 29.0 | 7 | 42 | 4 | 30.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8411000370979309 | 0.0 | 0.0 | +84e865bc-366e-45cd-85e4-fa7314688368 / -42733dbd-0bc3-461b-95ab-76daf5ad6296,a92eca5d-299f-4f4d-a16b-d23981ef719f |
| Jogador 4 | 4-6 | 244 | BUY | STABILIZE | 29.0 | 7 | 39 | 3 | 24.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07636426389217377 | 0.0 | 0.0 | +0435182d-aea5-44fe-ba36-601627982b66 / -— |
| Jogador 4 | 4-6 | 245 | MOVE_BENCH | STABILIZE | 29.0 | 7 | 36 | 3 | 24.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4006116986274719 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 246 | BUY | STABILIZE | 29.0 | 7 | 36 | 3 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1817980259656906 | 0.0 | 0.0 | +b0c1aba5-b1bd-48df-abec-19efa8e49d6d / -— |
| Jogador 4 | 4-6 | 247 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 35 | 3 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031159348785877228 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 248 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 35 | 3 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 249 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 35 | 3 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17294083535671234 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 250 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 35 | 3 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 252 | SELL | ALL_IN | 17.0 | 7 | 44 | 4 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5062222480773926 | 0.0 | 0.0 | +— / -84e865bc-366e-45cd-85e4-fa7314688368 |
| Jogador 4 | 4-7 | 253 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 7 | 52 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13526783883571625 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 254 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 7 | 52 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09964186698198318 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 255 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 7 | 52 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1690795123577118 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 256 | BUY | ALL_IN | 17.0 | 7 | 52 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.102190762758255 | 0.0 | 0.0 | +a64cf09b-42bf-494e-9603-d387b6740200 / -— |
| Jogador 4 | 4-7 | 257 | SELL | ALL_IN | 17.0 | 7 | 49 | 4 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06131426990032196 | 0.0 | 0.0 | +— / -b0c1aba5-b1bd-48df-abec-19efa8e49d6d |
| Jogador 4 | 4-7 | 258 | BUY | ALL_IN | 17.0 | 7 | 50 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2975904941558838 | 0.0 | 0.0 | +ecf369a7-649e-45fe-ad90-8f29e1714fe6 / -— |
| Jogador 4 | 4-7 | 259 | SELL | ALL_IN | 17.0 | 7 | 47 | 4 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09221207350492477 | 0.0 | 0.0 | +— / -0435182d-aea5-44fe-ba36-601627982b66 |
| Jogador 4 | 4-7 | 260 | BUY | ALL_IN | 17.0 | 7 | 50 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2745884358882904 | 0.0 | 0.0 | +91966802-adc2-46d2-9e7e-194283bca85c / -— |
| Jogador 4 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 17.0 | 7 | 58 | 5 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2417495995759964 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 17.0 | 7 | 58 | 5 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08114929497241974 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 264 | SELL | ALL_IN | 17.0 | 7 | 58 | 5 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -91966802-adc2-46d2-9e7e-194283bca85c |
| Jogador 4 | 5-1 | 265 | BUY | ALL_IN | 17.0 | 7 | 60 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6222413182258606 | 0.0 | 0.0 | +6594349f-ecaa-4212-b063-815acae6d0bb / -— |
| Jogador 4 | 5-1 | 266 | SELL | ALL_IN | 17.0 | 7 | 57 | 5 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005393814062699676 | 0.0 | 0.0 | +— / -ecf369a7-649e-45fe-ad90-8f29e1714fe6 |
| Jogador 4 | 5-1 | 267 | BUY | ALL_IN | 17.0 | 7 | 60 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42084237933158875 | 0.0 | 0.0 | +5821f43b-b898-4842-b309-d175f2284a84 / -— |
| Jogador 4 | 5-1 | 268 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 57 | 5 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 269 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 57 | 5 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014989243820309639 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 270 | PASS | ALL_IN | 17.0 | 7 | 57 | 5 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47057005763053894 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 272 | SELL | ALL_IN | 1.0 | 7 | 68 | 5 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13989999890327454 | 0.0 | 0.0 | +— / -5821f43b-b898-4842-b309-d175f2284a84 |
| Jogador 4 | 5-2 | 273 | BUY | ALL_IN | 1.0 | 7 | 71 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0851314067840576 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -55944609-f4df-4e53-a1d1-31c79a148b22,e01be6cf-34fe-4057-aef3-c08c504794cf |
| Jogador 4 | 5-2 | 274 | BUY | ALL_IN | 1.0 | 7 | 69 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2202741652727127 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -— |
| Jogador 4 | 5-2 | 275 | BUY | ALL_IN | 1.0 | 7 | 66 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2700851559638977 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 4 | 5-2 | 276 | SELL | ALL_IN | 1.0 | 7 | 63 | 5 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.707966685295105 | 0.0 | 0.0 | +— / -8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 |
| Jogador 4 | 5-2 | 277 | BUY | ALL_IN | 1.0 | 7 | 68 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2443922609090805 | 0.0 | 0.0 | +f84cc827-410f-47eb-bd95-bd650acfdd4b / -— |
| Jogador 4 | 5-2 | 278 | REROLL | ALL_IN | 1.0 | 7 | 66 | 5 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 279 | SELL | ALL_IN | 1.0 | 7 | 64 | 5 | 32.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -f84cc827-410f-47eb-bd95-bd650acfdd4b |
| Jogador 4 | 5-2 | 280 | BUY | ALL_IN | 1.0 | 7 | 66 | 5 | 32.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45225560665130615 | 0.0 | 0.0 | +f0264dc3-6749-4682-929e-fab42383532a / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.26577791571617126 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.24549612402915955 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12370830029249191 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11255644261837006 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17292346060276031 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012102286331355572 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4293290078639984 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2171582281589508 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3304295241832733 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28900668025016785 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 39 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 50 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0326523780822754 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 51 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19876615703105927 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 52 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2127651423215866 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4089089035987854 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2262270599603653 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 55 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9722437858581543 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 64 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0441960096359253 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12276759743690491 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 75 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2461172193288803 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4363231658935547 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 77 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1627991795539856 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03177344799041748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 79 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25817784667015076 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 80 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3106866776943207 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21888257563114166 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05810000002384186 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 85 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0881052315235138 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-4 | 86 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1673043966293335 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07833333313465118 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09794705361127853 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-4 | 89 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 90 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2902454137802124 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3394306004047394 | 0.0 | 0.0 | +2e4ab22c-62d7-425c-9528-2e1315655c24 / -— |
| Jogador 5 | 2-5 | 94 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06970000267028809 | 0.0 | 0.0 | +— / -486e92ad-4dcf-4c0e-a470-e0b87777d380 |
| Jogador 5 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1223333328962326 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 5 | 2-5 | 96 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3170260488986969 | 0.0 | 0.0 | +28f66ef1-93d6-4cc8-a0c9-e84e844dee28 / -— |
| Jogador 5 | 2-5 | 97 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 98 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3515999913215637 | 0.0 | 0.0 | +— / -28f66ef1-93d6-4cc8-a0c9-e84e844dee28 |
| Jogador 5 | 2-5 | 99 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39711567759513855 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36481964588165283 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09186519682407379 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06104522570967674 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 105 | BUY | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05930067226290703 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 106 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08731768280267715 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-6 | 107 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06522078812122345 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 108 | SELL | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43148890137672424 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-6 | 109 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005137316416949034 | 0.0 | 0.0 | +53312511-4e10-4904-82c0-8a8e69c039cd / -— |
| Jogador 5 | 2-6 | 110 | BUY | STABILIZE | 95.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0050762249156832695 | 0.0 | 0.0 | +b6a21130-c9dc-45ad-8ddb-9223b0ec8751 / -— |
| Jogador 5 | 2-7 | 112 | BUY | STABILIZE | 88.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34532737731933594 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 113 | BUY | STABILIZE | 88.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9630588889122009 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 114 | BUY | STABILIZE | 88.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20998093485832214 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -— |
| Jogador 5 | 2-7 | 115 | SELL | STABILIZE | 88.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034699998795986176 | 0.0 | 0.0 | +— / -53312511-4e10-4904-82c0-8a8e69c039cd |
| Jogador 5 | 2-7 | 116 | SELL | STABILIZE | 88.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03592974692583084 | 0.0 | 0.0 | +— / -b6a21130-c9dc-45ad-8ddb-9223b0ec8751 |
| Jogador 5 | 2-7 | 117 | BUY | STABILIZE | 88.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10740545392036438 | 0.0 | 0.0 | +6eee9a92-4235-46af-ae42-c38acd6847ef / -— |
| Jogador 5 | 2-7 | 118 | SELL | STABILIZE | 88.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41966667771339417 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 2-7 | 119 | SELL | STABILIZE | 88.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37566667795181274 | 0.0 | 0.0 | +— / -6eee9a92-4235-46af-ae42-c38acd6847ef |
| Jogador 5 | 2-7 | 120 | BUY | STABILIZE | 88.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00808158703148365 | 0.0 | 0.0 | +c5593e47-f48a-4362-b230-dfa3d7d36ec9 / -— |
| Jogador 5 | 3-1 | 122 | BUY | STABILIZE | 88.0 | 6 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7501031756401062 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -46838f8d-8037-485c-8c34-9639f14ada19,837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 88.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.190902441740036 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 124 | BUY | STABILIZE | 88.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11416009068489075 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 125 | BUY | STABILIZE | 88.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028782688081264496 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 5 | 3-1 | 126 | SELL | STABILIZE | 88.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-1 | 127 | BUY | STABILIZE | 88.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2711927890777588 | 0.0 | 0.0 | +79ed9815-7667-4e50-86a3-420599ce8c79 / -— |
| Jogador 5 | 3-1 | 128 | SELL | STABILIZE | 88.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -c5593e47-f48a-4362-b230-dfa3d7d36ec9 |
| Jogador 5 | 3-1 | 129 | SELL | STABILIZE | 88.0 | 6 | 8 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2409999966621399 | 0.0 | 0.0 | +— / -79ed9815-7667-4e50-86a3-420599ce8c79 |
| Jogador 5 | 3-1 | 130 | BUY | STABILIZE | 88.0 | 6 | 10 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35375088453292847 | 0.0 | 0.0 | +f7526b6b-8c94-4229-bd3f-1e538c769fec / -— |
| Jogador 5 | 3-2 | 132 | BUY | STABILIZE | 76.0 | 6 | 15 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6885117888450623 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 133 | BUY | STABILIZE | 76.0 | 6 | 12 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27089130878448486 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -— |
| Jogador 5 | 3-2 | 134 | SELL | STABILIZE | 76.0 | 6 | 10 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -f7526b6b-8c94-4229-bd3f-1e538c769fec |
| Jogador 5 | 3-2 | 135 | SELL | STABILIZE | 76.0 | 6 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09637503325939178 | 0.0 | 0.0 | +— / -a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 |
| Jogador 5 | 3-2 | 136 | BUY | STABILIZE | 76.0 | 6 | 13 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23657487332820892 | 0.0 | 0.0 | +35a674f6-a230-480b-a93f-f7ec76d78658 / -— |
| Jogador 5 | 3-2 | 137 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08453013747930527 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 138 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5417330861091614 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 139 | PASS | STABILIZE | 76.0 | 6 | 11 | 1 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 142 | BUY | STABILIZE | 76.0 | 6 | 18 | 1 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7901210188865662 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -— |
| Jogador 5 | 3-3 | 143 | BUY | STABILIZE | 76.0 | 6 | 16 | 1 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2812163531780243 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 144 | BUY | STABILIZE | 76.0 | 6 | 12 | 1 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20151914656162262 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 145 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 9 | 0 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27738186717033386 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 146 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4135897159576416 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 147 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 9 | 0 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1822836995124817 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 148 | PASS | STABILIZE | 76.0 | 6 | 9 | 0 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 152 | SELL | STABILIZE | 65.0 | 6 | 14 | 1 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -35a674f6-a230-480b-a93f-f7ec76d78658 |
| Jogador 5 | 3-4 | 153 | BUY | STABILIZE | 65.0 | 6 | 16 | 1 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8078071475028992 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 5 | 3-4 | 154 | SELL | STABILIZE | 65.0 | 6 | 15 | 1 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -8a4d0946-b80f-4fbb-ab7c-d43c2697c34e |
| Jogador 5 | 3-4 | 155 | BUY | STABILIZE | 65.0 | 6 | 19 | 1 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5894448757171631 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -— |
| Jogador 5 | 3-4 | 156 | SELL | STABILIZE | 65.0 | 6 | 18 | 1 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46722230315208435 | 0.0 | 0.0 | +— / -ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 3-4 | 157 | SELL | STABILIZE | 65.0 | 6 | 19 | 1 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4920464754104614 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-4 | 158 | BUY | STABILIZE | 65.0 | 6 | 22 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026212986558675766 | 0.0 | 0.0 | +46fc5f36-cf3e-422e-89f3-9501ec9d7d12 / -— |
| Jogador 5 | 3-4 | 159 | MOVE_BENCH | STABILIZE | 65.0 | 6 | 20 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24107077717781067 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 160 | SELL | STABILIZE | 65.0 | 6 | 20 | 2 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32100000977516174 | 0.0 | 0.0 | +— / -46fc5f36-cf3e-422e-89f3-9501ec9d7d12 |
| Jogador 5 | 3-5 | 162 | BUY | STABILIZE | 65.0 | 6 | 29 | 2 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8092711567878723 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -02c39b42-90d5-4e01-9380-460b6c1cb993,eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 3-5 | 163 | MOVE_BENCH | STABILIZE | 65.0 | 6 | 28 | 2 | 14.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3809250295162201 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 164 | BUY | STABILIZE | 65.0 | 6 | 28 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11882858723402023 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-5 | 165 | BUY | STABILIZE | 65.0 | 6 | 25 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018777988851070404 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 166 | SELL | STABILIZE | 65.0 | 6 | 22 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 3-5 | 167 | BUY | STABILIZE | 65.0 | 6 | 25 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1883605271577835 | 0.0 | 0.0 | +6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 / -— |
| Jogador 5 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 65.0 | 6 | 24 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0489426925778389 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 169 | SELL | STABILIZE | 65.0 | 6 | 24 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3596666753292084 | 0.0 | 0.0 | +— / -6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 |
| Jogador 5 | 3-5 | 170 | SELL | STABILIZE | 65.0 | 6 | 25 | 2 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.352293461561203 | 0.0 | 0.0 | +— / -9bbd1da9-6a26-472c-912e-165ea4031b90 |
| Jogador 5 | 3-6 | 172 | BUY | STABILIZE | 54.0 | 6 | 36 | 3 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18381638824939728 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -— |
| Jogador 5 | 3-6 | 173 | BUY | STABILIZE | 54.0 | 6 | 35 | 3 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009022529236972332 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-6 | 174 | SELL | STABILIZE | 54.0 | 6 | 33 | 3 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42633333802223206 | 0.0 | 0.0 | +— / -bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 |
| Jogador 5 | 3-6 | 175 | BUY | STABILIZE | 54.0 | 6 | 34 | 3 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021113118156790733 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 5 | 3-6 | 176 | SELL | STABILIZE | 54.0 | 6 | 33 | 3 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37299999594688416 | 0.0 | 0.0 | +— / -82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 |
| Jogador 5 | 3-6 | 177 | BUY | STABILIZE | 54.0 | 6 | 34 | 3 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2756994664669037 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-6 | 178 | SELL | STABILIZE | 54.0 | 6 | 32 | 3 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32100000977516174 | 0.0 | 0.0 | +— / -1457cd1e-c240-4ce5-9217-a91bddfc8807 |
| Jogador 5 | 3-6 | 179 | SELL | STABILIZE | 54.0 | 6 | 34 | 3 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36204108595848083 | 0.0 | 0.0 | +— / -750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 5 | 3-6 | 180 | SELL | STABILIZE | 54.0 | 6 | 36 | 3 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09756173938512802 | 0.0 | 0.0 | +— / -4af85188-f11e-4aca-8165-ba8e7f535670 |
| Jogador 5 | 3-7 | 182 | BUY | STABILIZE | 54.0 | 6 | 49 | 4 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8485396504402161 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -— |
| Jogador 5 | 3-7 | 183 | BUY | STABILIZE | 54.0 | 6 | 47 | 4 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021681442856788635 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 184 | BUY | STABILIZE | 54.0 | 6 | 44 | 4 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22031590342521667 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 5 | 3-7 | 185 | SELL | STABILIZE | 54.0 | 6 | 41 | 4 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3449999988079071 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 5 | 3-7 | 186 | SELL | STABILIZE | 54.0 | 6 | 44 | 4 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37033334374427795 | 0.0 | 0.0 | +— / -8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 |
| Jogador 5 | 3-7 | 187 | SELL | STABILIZE | 54.0 | 6 | 47 | 4 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5408179759979248 | 0.0 | 0.0 | +— / -1d7b6420-388f-4cb1-b25c-2e5a3dfec742 |
| Jogador 5 | 3-7 | 188 | SELL | STABILIZE | 54.0 | 6 | 50 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9435162544250488 | 0.0 | 0.0 | +— / -8a4e95ea-d35a-4690-9313-126b5d86773e |
| Jogador 5 | 3-7 | 189 | SELL | STABILIZE | 54.0 | 6 | 52 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49348005652427673 | 0.0 | 0.0 | +— / -4d8c374c-264c-47d9-8cfc-78cbf64ceda0 |
| Jogador 5 | 3-7 | 190 | SELL | STABILIZE | 54.0 | 6 | 54 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0262999534606934 | 0.0 | 0.0 | +— / -6084e8d8-82f2-47e3-b8e1-4077ad70efe5 |
| Jogador 5 | 4-1 | 192 | BUY | STABILIZE | 54.0 | 6 | 65 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0713670253753662 | 0.0 | 0.0 | +0c07379e-5dd1-42e9-aa7a-a764f949deee / -135065df-1ebc-413d-86f1-4df28bd3ee41,691cde76-cf1b-4a60-b818-65f790e312ec |
| Jogador 5 | 4-1 | 193 | BUY | STABILIZE | 54.0 | 6 | 63 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.45291802287101746 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 194 | BUY | STABILIZE | 54.0 | 6 | 60 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.19001951813697815 | 0.0 | 0.0 | +f6de9b7d-1373-459e-b34a-7b878d1a1268 / -— |
| Jogador 5 | 4-1 | 195 | CRAFT_AND_EQUIP | STABILIZE | 54.0 | 6 | 59 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13963034749031067 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 196 | CRAFT_AND_EQUIP | STABILIZE | 54.0 | 6 | 59 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16698326170444489 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 197 | SELL | STABILIZE | 54.0 | 6 | 59 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6414999961853027 | 0.0 | 0.0 | +— / -0c07379e-5dd1-42e9-aa7a-a764f949deee |
| Jogador 5 | 4-1 | 198 | BUY | STABILIZE | 54.0 | 6 | 64 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23357976973056793 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 5 | 4-1 | 199 | MOVE_BENCH | STABILIZE | 54.0 | 6 | 61 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3957660496234894 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 200 | SELL | STABILIZE | 54.0 | 6 | 61 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45601686835289 | 0.0 | 0.0 | +— / -f6de9b7d-1373-459e-b34a-7b878d1a1268 |
| Jogador 5 | 4-2 | 202 | BUY | STABILIZE | 43.0 | 6 | 72 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0963398814201355 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 5 | 4-2 | 203 | BUY | STABILIZE | 43.0 | 6 | 68 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1441177874803543 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 5 | 4-2 | 204 | BUY | STABILIZE | 43.0 | 6 | 67 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2187565565109253 | 0.0 | 0.0 | +02c8aff1-803e-42bc-b7c2-f7cd6d986b4f / -— |
| Jogador 5 | 4-2 | 205 | BUY | STABILIZE | 43.0 | 6 | 65 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42816361784935 | 0.0 | 0.0 | +dde5ed69-0fc4-4d15-b12c-a5252a239040 / -— |
| Jogador 5 | 4-2 | 206 | MOVE_BENCH | STABILIZE | 43.0 | 6 | 63 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5850246548652649 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 207 | MOVE_BENCH | STABILIZE | 43.0 | 6 | 63 | 5 | 22.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.672516405582428 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 208 | PASS | STABILIZE | 43.0 | 6 | 63 | 5 | 22.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23271946609020233 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 212 | BUY | STABILIZE | 31.0 | 6 | 74 | 5 | 22.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22673094272613525 | 0.0 | 0.0 | +72c247af-bdc3-410c-98dd-dd72b56f2818 / -— |
| Jogador 5 | 4-3 | 213 | BUY | STABILIZE | 31.0 | 6 | 71 | 5 | 22.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1235879436135292 | 0.0 | 0.0 | +333b0a0b-8868-40b2-96e9-71e468c5dd1f / -— |
| Jogador 5 | 4-3 | 214 | BUY | STABILIZE | 31.0 | 6 | 70 | 5 | 22.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0024254722520709038 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 5 | 4-3 | 215 | SELL | STABILIZE | 31.0 | 6 | 67 | 5 | 22.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -333b0a0b-8868-40b2-96e9-71e468c5dd1f |
| Jogador 5 | 4-3 | 216 | SELL | STABILIZE | 31.0 | 6 | 68 | 5 | 22.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.128901407122612 | 0.0 | 0.0 | +— / -9593a62e-442f-410a-8a0c-7d781e2487cc |
| Jogador 5 | 4-3 | 217 | MOVE_BENCH | STABILIZE | 31.0 | 6 | 69 | 5 | 22.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04894525185227394 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 218 | MOVE_BENCH | STABILIZE | 31.0 | 6 | 69 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5998611450195312 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 219 | MOVE_BENCH | STABILIZE | 31.0 | 6 | 69 | 5 | 22.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39167526364326477 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 220 | PASS | STABILIZE | 31.0 | 6 | 69 | 5 | 22.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2617717385292053 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 222 | BUY | ALL_IN | 19.0 | 6 | 80 | 5 | 22.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9870338439941406 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -02c8aff1-803e-42bc-b7c2-f7cd6d986b4f,dde5ed69-0fc4-4d15-b12c-a5252a239040 |
| Jogador 5 | 4-4 | 223 | MOVE_BENCH | ALL_IN | 19.0 | 6 | 78 | 5 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5103239417076111 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 224 | BUY | ALL_IN | 19.0 | 6 | 78 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1203056052327156 | 0.0 | 0.0 | +15c93ffb-d63e-43e6-aa46-ba2beed9cb53 / -— |
| Jogador 5 | 4-4 | 225 | BUY | ALL_IN | 19.0 | 6 | 76 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1423274278640747 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 5 | 4-4 | 226 | BUY | ALL_IN | 19.0 | 6 | 75 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27493545413017273 | 0.0 | 0.0 | +677ea844-e1bf-4c68-a0b0-136abb86ba7b / -— |
| Jogador 5 | 4-4 | 227 | REROLL | ALL_IN | 19.0 | 6 | 73 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 228 | SELL | ALL_IN | 19.0 | 6 | 71 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05236666649580002 | 0.0 | 0.0 | +— / -e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 |
| Jogador 5 | 4-4 | 229 | BUY | ALL_IN | 19.0 | 6 | 76 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9561327695846558 | 0.0 | 0.0 | +d1f19609-8b5f-489d-a2cf-d015fe7ed27e / -— |
| Jogador 5 | 4-4 | 230 | SELL | ALL_IN | 19.0 | 6 | 75 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -677ea844-e1bf-4c68-a0b0-136abb86ba7b |
| Jogador 5 | 4-5 | 232 | BUY | ALL_IN | 19.0 | 6 | 88 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9608092904090881 | 0.0 | 0.0 | +ac547bcb-d285-480d-b50e-3cfba572db5a / -— |
| Jogador 5 | 4-5 | 233 | SELL | ALL_IN | 19.0 | 6 | 85 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033310096710920334 | 0.0 | 0.0 | +— / -b755a0c5-f515-4f95-8f58-1e05f40ad302 |
| Jogador 5 | 4-5 | 234 | BUY | ALL_IN | 19.0 | 6 | 86 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06387101113796234 | 0.0 | 0.0 | +715d5bfc-c8c3-4dec-a247-9e07ee2755e8 / -— |
| Jogador 5 | 4-5 | 235 | SELL | ALL_IN | 19.0 | 6 | 83 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030016018077731133 | 0.0 | 0.0 | +— / -15c93ffb-d63e-43e6-aa46-ba2beed9cb53 |
| Jogador 5 | 4-5 | 236 | BUY | ALL_IN | 19.0 | 6 | 85 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19631381332874298 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -— |
| Jogador 5 | 4-5 | 237 | REROLL | ALL_IN | 19.0 | 6 | 84 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 238 | SELL | ALL_IN | 19.0 | 6 | 82 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -8aa832ec-4c09-43bd-ae21-baf7268e468d |
| Jogador 5 | 4-5 | 239 | BUY | ALL_IN | 19.0 | 6 | 83 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13889651000499725 | 0.0 | 0.0 | +4a885bc0-41b4-43f1-94d3-8e755a10645c / -— |
| Jogador 5 | 4-5 | 240 | SELL | ALL_IN | 19.0 | 6 | 82 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047943297773599625 | 0.0 | 0.0 | +— / -4a885bc0-41b4-43f1-94d3-8e755a10645c |
| Jogador 5 | 4-6 | 242 | BUY | ALL_IN | 7.0 | 6 | 94 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5343185067176819 | 0.0 | 0.0 | +27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 / -— |
| Jogador 5 | 4-6 | 243 | SELL | ALL_IN | 7.0 | 6 | 91 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00426666671410203 | 0.0 | 0.0 | +— / -27a4bd22-9c1f-4f9f-9192-06ea4933feb5 |
| Jogador 5 | 4-6 | 244 | BUY | ALL_IN | 7.0 | 6 | 94 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13082954287528992 | 0.0 | 0.0 | +8b75555c-d84d-4b8a-8d6c-012585a05b99 / -— |
| Jogador 5 | 4-6 | 245 | SELL | ALL_IN | 7.0 | 6 | 91 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03335161507129669 | 0.0 | 0.0 | +— / -8b75555c-d84d-4b8a-8d6c-012585a05b99 |
| Jogador 5 | 4-6 | 246 | BUY | ALL_IN | 7.0 | 6 | 94 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04510735720396042 | 0.0 | 0.0 | +18e21ac6-f873-4310-95c8-bd8e62612479 / -— |
| Jogador 5 | 4-6 | 247 | MOVE_BENCH | ALL_IN | 7.0 | 6 | 92 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3985154628753662 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 248 | REROLL | ALL_IN | 7.0 | 6 | 92 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 249 | SELL | ALL_IN | 7.0 | 6 | 90 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01503401156514883 | 0.0 | 0.0 | +— / -18e21ac6-f873-4310-95c8-bd8e62612479 |
| Jogador 5 | 4-6 | 250 | BUY | ALL_IN | 7.0 | 6 | 92 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6336605548858643 | 0.0 | 0.0 | +de8de4b5-48ea-4947-ae08-2b90d94b0fc1 / -— |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | -0.15334774553775787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Sentry | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17399217188358307 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2196885347366333 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0373011827468872 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039901405572891235 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012773334980010986 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011599136516451836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5747041702270508 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0245673656463623 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 38 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 50 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12828443944454193 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 51 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15200024843215942 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29008981585502625 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 53 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 54 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0912872776389122 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26468825340270996 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 63 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24724523723125458 | 0.0 | 0.0 | +048e9074-b134-49ed-a105-88dca63d1aa3 / -— |
| Jogador 6 | 2-2 | 64 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -6a01f661-884f-4c25-9dbe-384a6fe3a5e6 |
| Jogador 6 | 2-2 | 65 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15483227372169495 | 0.0 | 0.0 | +f82eae62-dfe9-41bc-b346-71bf2c7cca02 / -— |
| Jogador 6 | 2-2 | 66 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -f82eae62-dfe9-41bc-b346-71bf2c7cca02 |
| Jogador 6 | 2-2 | 67 | PASS | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 72 | BUY | STABILIZE | 89.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2892988324165344 | 0.0 | 0.0 | +b1ecd1fa-793c-40ad-a9e3-9d35d5030339 / -— |
| Jogador 6 | 2-3 | 73 | BUY | STABILIZE | 89.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21115592122077942 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 74 | BUY_XP | STABILIZE | 89.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 75 | PASS | STABILIZE | 89.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 82 | BUY | STABILIZE | 85.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9454267024993896 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 83 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9424229860305786 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -18934be2-4988-4f62-9f62-07ba151231f2,646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-4 | 84 | BUY_XP | STABILIZE | 85.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 85 | SELL | STABILIZE | 85.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2590000033378601 | 0.0 | 0.0 | +— / -53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 2-4 | 86 | BUY_XP | STABILIZE | 85.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 87 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.982695514219813e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 88 | SELL | STABILIZE | 85.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1520828753709793 | 0.0 | 0.0 | +— / -b1ecd1fa-793c-40ad-a9e3-9d35d5030339 |
| Jogador 6 | 2-4 | 89 | BUY | STABILIZE | 85.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18279336392879486 | 0.0 | 0.0 | +2c497125-ca06-46b1-a3b3-9a59d904705b / -— |
| Jogador 6 | 2-4 | 90 | SELL | STABILIZE | 85.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4023333191871643 | 0.0 | 0.0 | +— / -2c497125-ca06-46b1-a3b3-9a59d904705b |
| Jogador 6 | 2-5 | 92 | BUY | STABILIZE | 85.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9272152185440063 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 93 | BUY | STABILIZE | 85.0 | 5 | 5 | 0 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9770972728729248 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 94 | BUY_XP | STABILIZE | 85.0 | 5 | 4 | 0 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 95 | SELL | STABILIZE | 85.0 | 5 | 0 | 0 | 14.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12361583113670349 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-5 | 96 | SELL | STABILIZE | 85.0 | 5 | 2 | 0 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -908afab9-748c-4057-a2a9-d2686c5d52e0 |
| Jogador 6 | 2-5 | 97 | SELL | STABILIZE | 85.0 | 5 | 3 | 0 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6017333269119263 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-5 | 98 | BUY | STABILIZE | 85.0 | 5 | 4 | 0 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3962841033935547 | 0.0 | 0.0 | +f957e607-dd51-492b-9186-252da4e0c12f / -— |
| Jogador 6 | 2-5 | 99 | SELL | STABILIZE | 85.0 | 5 | 3 | 0 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -f957e607-dd51-492b-9186-252da4e0c12f |
| Jogador 6 | 2-5 | 100 | BUY | STABILIZE | 85.0 | 5 | 4 | 0 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22994814813137054 | 0.0 | 0.0 | +0023f061-5310-4e39-849a-22ad49993d8c / -— |
| Jogador 6 | 2-6 | 102 | BUY | STABILIZE | 78.0 | 6 | 8 | 0 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.114105224609375 | 0.0 | 0.0 | +53bbd605-d60b-4555-b5e8-29f1cfbb83b4 / -048e9074-b134-49ed-a105-88dca63d1aa3,c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 6 | 0 | 14.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41043993830680847 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 104 | BUY | STABILIZE | 78.0 | 6 | 6 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3116987943649292 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 3 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 3 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04490218311548233 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 3 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08315784484148026 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 3 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 109 | PASS | STABILIZE | 78.0 | 6 | 3 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 112 | BUY | STABILIZE | 78.0 | 6 | 9 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0323044061660767 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 113 | BUY | STABILIZE | 78.0 | 6 | 6 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4016523063182831 | 0.0 | 0.0 | +dc83202b-476c-4438-90aa-a615b764b7e4 / -— |
| Jogador 6 | 2-7 | 114 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 5 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0014300689799711108 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 115 | BUY_XP | STABILIZE | 78.0 | 6 | 5 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0023998459801077843 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 118 | PASS | STABILIZE | 78.0 | 6 | 1 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 122 | BUY | STABILIZE | 78.0 | 6 | 6 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2748181223869324 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 78.0 | 6 | 3 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1961282342672348 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 124 | SELL | STABILIZE | 78.0 | 6 | 3 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -53bbd605-d60b-4555-b5e8-29f1cfbb83b4 |
| Jogador 6 | 3-1 | 125 | BUY | STABILIZE | 78.0 | 6 | 8 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021265555173158646 | 0.0 | 0.0 | +ab127012-83d7-46f0-a16c-b20582d1179b / -— |
| Jogador 6 | 3-1 | 126 | BUY_XP | STABILIZE | 78.0 | 6 | 6 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 127 | SELL | STABILIZE | 78.0 | 6 | 2 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07104198634624481 | 0.0 | 0.0 | +— / -ab127012-83d7-46f0-a16c-b20582d1179b |
| Jogador 6 | 3-1 | 128 | BUY_XP | STABILIZE | 78.0 | 6 | 4 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 129 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 0 | 0 | 18.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00025891230325214565 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 130 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 0 | 0 | 18.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05648591369390488 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 132 | BUY | STABILIZE | 78.0 | 6 | 7 | 0 | 22.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.832139790058136 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 133 | BUY_XP | STABILIZE | 78.0 | 6 | 6 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 134 | SELL | STABILIZE | 78.0 | 6 | 2 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4759437143802643 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 3-2 | 135 | EQUIP_FROM_INVENTORY | STABILIZE | 78.0 | 6 | 5 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14023464918136597 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 136 | EQUIP_FROM_INVENTORY | STABILIZE | 78.0 | 6 | 5 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15145161747932434 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 137 | EQUIP_FROM_INVENTORY | STABILIZE | 78.0 | 6 | 5 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.18372629582881927 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 138 | BUY | STABILIZE | 78.0 | 6 | 5 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27140453457832336 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -— |
| Jogador 6 | 3-2 | 139 | BUY_XP | STABILIZE | 78.0 | 6 | 4 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 140 | SELL | STABILIZE | 78.0 | 6 | 0 | 0 | 18.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4796256124973297 | 0.0 | 0.0 | +— / -e29364db-c484-4e4d-954d-7f4940131ffc |
| Jogador 6 | 3-3 | 142 | BUY | STABILIZE | 67.0 | 6 | 6 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01621842570602894 | 0.0 | 0.0 | +50f9a30c-27db-4ed0-804e-548f87950b17 / -— |
| Jogador 6 | 3-3 | 143 | MOVE_BENCH | STABILIZE | 67.0 | 6 | 3 | 0 | 18.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24094273149967194 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 144 | BUY | STABILIZE | 67.0 | 6 | 3 | 0 | 24.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00445645721629262 | 0.0 | 0.0 | +952adeb2-fe24-47af-9748-5131b91dcc06 / -— |
| Jogador 6 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 1 | 0 | 24.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00029697708669118583 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 1 | 0 | 24.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010561301372945309 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 147 | SELL | STABILIZE | 67.0 | 6 | 1 | 0 | 24.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -952adeb2-fe24-47af-9748-5131b91dcc06 |
| Jogador 6 | 3-3 | 148 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 3 | 0 | 24.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 3 | 0 | 24.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0167310182005167 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 150 | PASS | STABILIZE | 67.0 | 6 | 3 | 0 | 24.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 152 | BUY | STABILIZE | 67.0 | 6 | 9 | 0 | 30.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28296592831611633 | 0.0 | 0.0 | +ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c / -— |
| Jogador 6 | 3-4 | 153 | BUY_XP | STABILIZE | 67.0 | 6 | 6 | 0 | 30.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 154 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 2 | 0 | 30.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 155 | MOVE_BOARD | STABILIZE | 67.0 | 6 | 2 | 0 | 30.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 156 | PASS | STABILIZE | 67.0 | 6 | 2 | 0 | 30.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 162 | BUY | STABILIZE | 67.0 | 7 | 7 | 0 | 30.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8025696873664856 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 163 | BUY_XP | STABILIZE | 67.0 | 7 | 4 | 0 | 30.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 164 | SELL | STABILIZE | 67.0 | 7 | 0 | 0 | 30.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06527044624090195 | 0.0 | 0.0 | +— / -50f9a30c-27db-4ed0-804e-548f87950b17 |
| Jogador 6 | 3-5 | 165 | BUY | STABILIZE | 67.0 | 7 | 3 | 0 | 30.0 | Fumegante/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01409362256526947 | 0.0 | 0.0 | +06db3a99-d008-406a-ac86-30884335d7c2 / -— |
| Jogador 6 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 67.0 | 7 | 0 | 0 | 30.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5265360474586487 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 167 | MOVE_BOARD | FAST8 | 67.0 | 7 | 0 | 0 | 36.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 168 | MOVE_BOARD | FAST8 | 67.0 | 7 | 0 | 0 | 36.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 169 | PASS | FAST8 | 67.0 | 7 | 0 | 0 | 36.0 | Fumegante/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 172 | BUY | FAST8 | 67.0 | 7 | 7 | 0 | 36.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008995930664241314 | 0.0 | 0.0 | +604cc5dc-6c20-4d5a-b3a7-8862adfe1930 / -— |
| Jogador 6 | 3-6 | 173 | MOVE_BOARD | FAST8 | 67.0 | 7 | 4 | 0 | 36.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33750119805336 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 174 | MOVE_BOARD | FAST8 | 67.0 | 7 | 4 | 0 | 36.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00023242687166202813 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 175 | PASS | FAST8 | 67.0 | 7 | 4 | 0 | 36.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 182 | BUY | FAST8 | 67.0 | 7 | 11 | 1 | 36.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12212715297937393 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 6 | 3-7 | 183 | MOVE_BOARD | FAST8 | 67.0 | 7 | 7 | 0 | 36.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 184 | MOVE_BOARD | FAST8 | 67.0 | 7 | 7 | 0 | 36.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007822530344128609 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 185 | BUY | FAST8 | 67.0 | 7 | 7 | 0 | 36.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05992766469717026 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 186 | MOVE_BOARD | FAST8 | 67.0 | 7 | 2 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16586555540561676 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 187 | MOVE_BOARD | FAST8 | 67.0 | 7 | 2 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 188 | MOVE_BOARD | FAST8 | 67.0 | 7 | 2 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 189 | PASS | FAST8 | 67.0 | 7 | 2 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 192 | BUY | FAST8 | 67.0 | 7 | 8 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.36488738656044006 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -— |
| Jogador 6 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 67.0 | 7 | 5 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22917914390563965 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 194 | CRAFT_AND_EQUIP | FAST8 | 67.0 | 7 | 5 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18232114613056183 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 195 | MOVE_BOARD | FAST8 | 67.0 | 7 | 5 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 196 | MOVE_BOARD | FAST8 | 67.0 | 7 | 5 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 197 | PASS | FAST8 | 67.0 | 7 | 5 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 202 | BUY | FAST8 | 67.0 | 7 | 12 | 1 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48154646158218384 | 0.0 | 0.0 | +93f7279f-b03b-407b-b623-c0a2bd88f877 / -06db3a99-d008-406a-ac86-30884335d7c2,f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 6 | 4-2 | 203 | BUY | FAST8 | 67.0 | 7 | 9 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03484061732888222 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 6 | 4-2 | 204 | MOVE_BOARD | FAST8 | 67.0 | 7 | 5 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 205 | MOVE_BOARD | FAST8 | 67.0 | 7 | 5 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1719738095998764 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 206 | PASS | FAST8 | 67.0 | 7 | 5 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 212 | BUY | FAST8 | 67.0 | 7 | 13 | 1 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21413516998291016 | 0.0 | 0.0 | +badbffc5-dd49-4cd8-8b4d-941ae020e6e3 / -— |
| Jogador 6 | 4-3 | 213 | MOVE_BOARD | FAST8 | 67.0 | 7 | 11 | 1 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2647349536418915 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 214 | MOVE_BOARD | FAST8 | 67.0 | 7 | 11 | 1 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 215 | MOVE_BOARD | FAST8 | 67.0 | 7 | 11 | 1 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 216 | PASS | FAST8 | 67.0 | 7 | 11 | 1 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 222 | MOVE_BOARD | FAST8 | 67.0 | 7 | 21 | 2 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08197249472141266 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 223 | SELL | FAST8 | 67.0 | 7 | 21 | 2 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04873419180512428 | 0.0 | 0.0 | +— / -93f7279f-b03b-407b-b623-c0a2bd88f877 |
| Jogador 6 | 4-4 | 224 | BUY | FAST8 | 67.0 | 7 | 29 | 2 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21061190962791443 | 0.0 | 0.0 | +84a3b0f5-c448-4fe1-b001-5ceff2ed306a / -— |
| Jogador 6 | 4-4 | 225 | BUY_XP | FAST8 | 67.0 | 7 | 28 | 2 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025696000084280968 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 226 | BUY_XP | FAST8 | 67.0 | 7 | 24 | 2 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025696000084280968 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 227 | BUY_XP | FAST8 | 67.0 | 7 | 20 | 2 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05430399999022484 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 228 | BUY_XP | FAST8 | 67.0 | 7 | 16 | 1 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025696000084280968 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 229 | BUY_XP | FAST8 | 67.0 | 7 | 12 | 1 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 230 | MOVE_BOARD | FAST8 | 67.0 | 7 | 8 | 0 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00455680163577199 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 232 | SELL | FAST8 | 67.0 | 7 | 16 | 1 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03856666758656502 | 0.0 | 0.0 | +— / -604cc5dc-6c20-4d5a-b3a7-8862adfe1930 |
| Jogador 6 | 4-5 | 233 | BUY | FAST8 | 67.0 | 7 | 19 | 1 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7375903129577637 | 0.0 | 0.0 | +fe12befc-b473-4f91-9e51-558a03efa3ad / -— |
| Jogador 6 | 4-5 | 234 | SELL | FAST8 | 67.0 | 7 | 18 | 1 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0706450566649437 | 0.0 | 0.0 | +— / -86530a1f-5325-45fa-bf43-86419ccfda54 |
| Jogador 6 | 4-5 | 235 | BUY | FAST8 | 67.0 | 7 | 22 | 2 | 36.0 | Fumegante/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7314758896827698 | 0.0 | 0.0 | +9717d30c-f073-470c-a6ce-7db8257de559 / -— |
| Jogador 6 | 4-5 | 236 | MOVE_BOARD | FAST8 | 67.0 | 7 | 20 | 2 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 237 | MOVE_BOARD | FAST8 | 67.0 | 7 | 20 | 2 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27419570088386536 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 238 | PASS | FAST8 | 67.0 | 7 | 20 | 2 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02857142873108387 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 242 | SELL | FAST8 | 67.0 | 7 | 31 | 3 | 36.0 | Fumegante/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0024999999441206455 | 0.0 | 0.0 | +— / -891aea62-e06a-46d4-8250-a3d4a56e847d |
| Jogador 6 | 4-6 | 243 | BUY | FAST8 | 67.0 | 7 | 36 | 3 | 36.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016294507309794426 | 0.0 | 0.0 | +d366508d-f33b-485a-8ff3-e5d0a248ae3e / -— |
| Jogador 6 | 4-6 | 244 | MOVE_BOARD | FAST8 | 67.0 | 7 | 32 | 3 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08479209244251251 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 245 | MOVE_BOARD | FAST8 | 67.0 | 7 | 32 | 3 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024783115833997726 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 246 | PASS | FAST8 | 67.0 | 7 | 32 | 3 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037142857909202576 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 252 | SELL | FAST8 | 67.0 | 7 | 44 | 4 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01933693140745163 | 0.0 | 0.0 | +— / -d366508d-f33b-485a-8ff3-e5d0a248ae3e |
| Jogador 6 | 4-7 | 253 | BUY | FAST8 | 67.0 | 7 | 48 | 4 | 36.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.749984085559845 | 0.0 | 0.0 | +952ea2b4-387d-455d-b1ad-fb0de8c46e47 / -— |
| Jogador 6 | 4-7 | 254 | MOVE_BOARD | FAST8 | 67.0 | 7 | 45 | 4 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04674818739295006 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 255 | MOVE_BOARD | FAST8 | 67.0 | 7 | 45 | 4 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06584729254245758 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 256 | MOVE_BOARD | FAST8 | 67.0 | 7 | 45 | 4 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.034118980169296265 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 257 | MOVE_BOARD | FAST8 | 67.0 | 7 | 45 | 4 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24176082015037537 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 258 | MOVE_BOARD | FAST8 | 67.0 | 7 | 45 | 4 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0381375215947628 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 259 | MOVE_BOARD | FAST8 | 67.0 | 7 | 45 | 4 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 260 | MOVE_BOARD | FAST8 | 67.0 | 7 | 45 | 4 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002053854987025261 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 67.0 | 7 | 57 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13861620426177979 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 67.0 | 7 | 57 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.090667724609375 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 264 | SELL | FAST8 | 67.0 | 7 | 57 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42482537031173706 | 0.0 | 0.0 | +— / -84a3b0f5-c448-4fe1-b001-5ceff2ed306a |
| Jogador 6 | 5-1 | 265 | BUY | FAST8 | 67.0 | 7 | 58 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8402089476585388 | 0.0 | 0.0 | +986fbe1e-1826-4be7-a5d6-410a4c0a3f2f / -— |
| Jogador 6 | 5-1 | 266 | SELL | FAST8 | 67.0 | 7 | 55 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5925999879837036 | 0.0 | 0.0 | +— / -badbffc5-dd49-4cd8-8b4d-941ae020e6e3 |
| Jogador 6 | 5-1 | 267 | BUY | FAST8 | 67.0 | 7 | 57 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33850473165512085 | 0.0 | 0.0 | +da6c9f59-1fc3-467d-8845-bf7b38b4232c / -— |
| Jogador 6 | 5-1 | 268 | MOVE_BOARD | FAST8 | 67.0 | 7 | 53 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.487292896257713e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 269 | MOVE_BOARD | FAST8 | 67.0 | 7 | 53 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05221748724579811 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 270 | MOVE_BOARD | FAST8 | 67.0 | 7 | 53 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 272 | SELL | FAST8 | 51.0 | 7 | 63 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4850222170352936 | 0.0 | 0.0 | +— / -665661af-7240-4a65-bf3d-f4ecf3532a85 |
| Jogador 6 | 5-2 | 273 | BUY | FAST8 | 51.0 | 7 | 67 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017345331609249115 | 0.0 | 0.0 | +39b89fbe-9520-4eaa-80f9-81e03232c83c / -— |
| Jogador 6 | 5-2 | 274 | MOVE_BOARD | FAST8 | 51.0 | 7 | 66 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030745673924684525 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 275 | MOVE_BOARD | FAST8 | 51.0 | 7 | 66 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 276 | MOVE_BOARD | FAST8 | 51.0 | 7 | 66 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.128302663564682 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 277 | PASS | FAST8 | 51.0 | 7 | 66 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09898970276117325 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 282 | SELL | FAST8 | 51.0 | 7 | 77 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -39b89fbe-9520-4eaa-80f9-81e03232c83c |
| Jogador 6 | 5-3 | 283 | BUY | FAST8 | 51.0 | 7 | 78 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9538231492042542 | 0.0 | 0.0 | +aea521ef-8511-4b98-9c6d-e83b814777df / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4,ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c |
| Jogador 6 | 5-3 | 284 | BUY | STABILIZE | 51.0 | 7 | 75 | 5 | 30.0 | Fumegante/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0228736400604248 | 0.0 | 0.0 | +98991369-e5f0-4725-928c-f2fa5362bf73 / -986fbe1e-1826-4be7-a5d6-410a4c0a3f2f,a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 |
| Jogador 6 | 5-3 | 285 | BUY | STABILIZE | 51.0 | 7 | 72 | 5 | 24.0 | Fumegante/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0212852954864502 | 0.0 | 0.0 | +d9097eba-c1b2-4df8-9e5d-a9134dbfe52f / -3cb4d077-df9a-4fd2-9a68-7301aff1b657,3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 5-3 | 286 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 71 | 5 | 22.0 | Fumegante/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2774529457092285 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 287 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 71 | 5 | 24.0 | Fumegante/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08837006241083145 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 288 | BUY | STABILIZE | 51.0 | 7 | 71 | 5 | 28.0 | Fumegante/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4686342775821686 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -— |
| Jogador 6 | 5-3 | 289 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 68 | 5 | 28.0 | Fumegante/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018611041828989983 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 290 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 68 | 5 | 28.0 | Fumegante/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5322366952896118 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 292 | BUY | STABILIZE | 36.0 | 7 | 78 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3988506495952606 | 0.0 | 0.0 | +efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 / -— |
| Jogador 6 | 5-4 | 293 | BUY | STABILIZE | 36.0 | 7 | 74 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17040960490703583 | 0.0 | 0.0 | +8486b8a9-20fe-4234-bbba-0efa031c3b76 / -— |
| Jogador 6 | 5-4 | 294 | BUY | STABILIZE | 36.0 | 7 | 71 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2556171715259552 | 0.0 | 0.0 | +150a2da3-f559-4a40-a058-005e9c74e11f / -— |
| Jogador 6 | 5-4 | 295 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 67 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24560396373271942 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 296 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 67 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03316724672913551 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 297 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 67 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34076932072639465 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 298 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 67 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27204376459121704 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 299 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 67 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21499449014663696 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 301 | SELL | STABILIZE | 36.0 | 7 | 77 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -d9097eba-c1b2-4df8-9e5d-a9134dbfe52f |
| Jogador 6 | 5-5 | 302 | BUY | STABILIZE | 36.0 | 7 | 80 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.23218214511871338 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 6 | 5-5 | 303 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 7 | 77 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08671565353870392 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 304 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 7 | 77 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1310582458972931 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 305 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 7 | 77 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08723637461662292 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 306 | SELL | STABILIZE | 36.0 | 7 | 77 | 5 | 34.0 | Fumegante/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -aea521ef-8511-4b98-9c6d-e83b814777df |
| Jogador 6 | 5-5 | 307 | BUY | STABILIZE | 36.0 | 7 | 85 | 5 | 34.0 | Fumegante/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.34475988149642944 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -— |
| Jogador 6 | 5-5 | 308 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 7 | 82 | 5 | 34.0 | Fumegante/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08189375698566437 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 309 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 7 | 82 | 5 | 34.0 | Fumegante/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10040926933288574 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 310 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 7 | 82 | 5 | 34.0 | Fumegante/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10079403966665268 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 312 | SELL | STABILIZE | 36.0 | 7 | 93 | 5 | 34.0 | Fumegante/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -98991369-e5f0-4725-928c-f2fa5362bf73 |
| Jogador 6 | 5-6 | 313 | BUY | STABILIZE | 36.0 | 7 | 101 | 5 | 34.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.41537895798683167 | 0.0 | 0.0 | +c2bf43be-e6e1-47ed-bcb4-606e37f26671 / -— |
| Jogador 6 | 5-6 | 314 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 7 | 100 | 5 | 34.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09689909964799881 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 315 | BUY_XP | STABILIZE | 36.0 | 7 | 100 | 5 | 34.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6978225111961365 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 316 | BUY_XP | STABILIZE | 36.0 | 8 | 96 | 5 | 34.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04264000058174133 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 317 | BUY_XP | STABILIZE | 36.0 | 8 | 92 | 5 | 34.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04264000058174133 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 318 | BUY_XP | STABILIZE | 36.0 | 8 | 88 | 5 | 34.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04264000058174133 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 319 | BUY_XP | STABILIZE | 36.0 | 8 | 84 | 5 | 34.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04264000058174133 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 320 | BUY_XP | STABILIZE | 36.0 | 8 | 80 | 5 | 34.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04264000058174133 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 322 | SELL | ALL_IN | 22.0 | 8 | 86 | 5 | 34.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002453695749863982 | 0.0 | 0.0 | +— / -8486b8a9-20fe-4234-bbba-0efa031c3b76 |
| Jogador 6 | 5-7 | 323 | BUY | ALL_IN | 22.0 | 8 | 89 | 5 | 34.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.051171064376831 | 0.0 | 0.0 | +e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 / -43da0d73-facd-488b-b856-94e9496a97f9,952ea2b4-387d-455d-b1ad-fb0de8c46e47 |
| Jogador 6 | 5-7 | 324 | BUY | ALL_IN | 22.0 | 8 | 86 | 5 | 28.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05966491997241974 | 0.0 | 0.0 | +93581e04-3f00-4430-8e5b-c953196bc1de / -— |
| Jogador 6 | 5-7 | 325 | MOVE_BENCH | ALL_IN | 22.0 | 8 | 82 | 5 | 28.0 | Fumegante/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16641399264335632 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 326 | BUY | ALL_IN | 22.0 | 8 | 82 | 5 | 36.0 | Fumegante/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05426487326622009 | 0.0 | 0.0 | +d632ff66-a7c4-43d3-afb3-b83c174cda35 / -— |
| Jogador 6 | 5-7 | 327 | MOVE_BOARD | ALL_IN | 22.0 | 8 | 78 | 5 | 36.0 | Fumegante/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09787524491548538 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 328 | BUY_XP | ALL_IN | 22.0 | 8 | 78 | 5 | 36.0 | Fumegante/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1470700055360794 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 329 | MOVE_BOARD | ALL_IN | 22.0 | 8 | 74 | 5 | 36.0 | Fumegante/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17299744486808777 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 330 | BUY_XP | ALL_IN | 22.0 | 8 | 74 | 5 | 36.0 | Fumegante/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14632000029087067 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 8 | 80 | 5 | 36.0 | Fumegante/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.005366666708141565 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 333 | SELL | ALL_IN | 22.0 | 8 | 80 | 5 | 36.0 | Fumegante/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6887999773025513 | 0.0 | 0.0 | +— / -e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 |
| Jogador 6 | 6-1 | 334 | BUY | ALL_IN | 22.0 | 8 | 88 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8996036648750305 | 0.0 | 0.0 | +425a58b3-d906-4381-9afc-00f9852c9982 / -— |
| Jogador 6 | 6-1 | 335 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 8 | 84 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09544806182384491 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 336 | SELL | ALL_IN | 22.0 | 8 | 84 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -150a2da3-f559-4a40-a058-005e9c74e11f |
| Jogador 6 | 6-1 | 337 | BUY | ALL_IN | 22.0 | 8 | 88 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4993429183959961 | 0.0 | 0.0 | +2ac6d717-87f1-4421-929e-1934a9317e72 / -— |
| Jogador 6 | 6-1 | 338 | BUY_XP | ALL_IN | 22.0 | 8 | 84 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08182000368833542 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 339 | BUY_XP | ALL_IN | 22.0 | 8 | 80 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08182000368833542 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 340 | BUY_XP | ALL_IN | 22.0 | 8 | 76 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08182000368833542 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 342 | SELL | ALL_IN | 4.0 | 8 | 83 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5837308764457703 | 0.0 | 0.0 | +— / -2d5214b0-3e0c-4e71-8664-2459bf616650 |
| Jogador 6 | 6-2 | 343 | BUY | ALL_IN | 4.0 | 8 | 86 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007896733470261097 | 0.0 | 0.0 | +04ebf9b8-7683-4270-b98a-a3bfb342dcf8 / -— |
| Jogador 6 | 6-2 | 344 | BUY_XP | ALL_IN | 4.0 | 8 | 82 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14781999588012695 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 345 | BUY_XP | ALL_IN | 4.0 | 8 | 78 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1470700055360794 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 346 | BUY_XP | ALL_IN | 4.0 | 8 | 74 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14632000029087067 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 347 | BUY_XP | ALL_IN | 4.0 | 8 | 70 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14556999504566193 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 348 | BUY_XP | ALL_IN | 4.0 | 8 | 66 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7039200067520142 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 349 | MOVE_BENCH | ALL_IN | 4.0 | 9 | 62 | 5 | 36.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15044696629047394 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 350 | BUY | ALL_IN | 4.0 | 9 | 62 | 5 | 44.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21477960050106049 | 0.0 | 0.0 | +4321582a-0b45-4666-a119-7b49e92d012a / -— |
| Jogador 6 | 6-3 | 352 | SELL | ALL_IN | 4.0 | 9 | 70 | 5 | 44.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -4321582a-0b45-4666-a119-7b49e92d012a |
| Jogador 6 | 6-3 | 353 | BUY | ALL_IN | 4.0 | 9 | 73 | 5 | 44.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9420684576034546 | 0.0 | 0.0 | +5184a53b-fca3-448c-b5ab-7daa37b0c259 / -— |
| Jogador 6 | 6-3 | 354 | SELL | ALL_IN | 4.0 | 9 | 69 | 5 | 44.0 | Fumegante/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03200000151991844 | 0.0 | 0.0 | +— / -f078e755-d142-4dad-99d0-7e7599e3016d |
| Jogador 6 | 6-3 | 355 | BUY | ALL_IN | 4.0 | 9 | 72 | 5 | 44.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1080100536346436 | 0.0 | 0.0 | +c71adf7d-8d74-439d-8863-dac0f4f20cd1 / -5184a53b-fca3-448c-b5ab-7daa37b0c259,efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 |
| Jogador 6 | 6-3 | 356 | BUY | ALL_IN | 4.0 | 9 | 68 | 5 | 36.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1023321151733398 | 0.0 | 0.0 | +e1be174a-f112-4e1b-8bf6-738af52f27e8 / -0023f061-5310-4e39-849a-22ad49993d8c,9717d30c-f073-470c-a6ce-7db8257de559 |
| Jogador 6 | 6-3 | 357 | MOVE_BENCH | ALL_IN | 4.0 | 9 | 66 | 5 | 28.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21819740533828735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-3 | 358 | BUY | ALL_IN | 4.0 | 9 | 66 | 5 | 36.0 | Fumegante/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1675199568271637 | 0.0 | 0.0 | +f1ece814-0986-421f-b5df-0b457ebaa484 / -— |
| Jogador 6 | 6-3 | 359 | MOVE_BENCH | ALL_IN | 4.0 | 9 | 62 | 5 | 36.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08454527705907822 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-3 | 360 | MOVE_BENCH | ALL_IN | 4.0 | 9 | 62 | 5 | 36.0 | Fumegante/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10705666244029999 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589178562164307 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2799173593521118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.143971249461174 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012334865517914295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40434256196022034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0484532117843628 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23116838932037354 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004352054558694363 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005867671221494675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 28 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0368695259094238 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24539557099342346 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007539904909208417 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1995791792869568 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 41 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 50 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8280844688415527 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 51 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19951866567134857 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 52 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2452055960893631 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 53 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3010636866092682 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 54 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4375952184200287 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.047579050064087 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15446844696998596 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 65 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17929254472255707 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04722195118665695 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 68 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-2 | 69 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11020808666944504 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 70 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15388517081737518 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 72 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.047540307044983 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 73 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6480351686477661 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 6 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17148840427398682 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 75 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09782183915376663 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 76 | PASS | STABILIZE | 95.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3061787784099579 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2085912674665451 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12747173011302948 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0014732929412275553 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08233333379030228 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 7 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10064122825860977 | 0.0 | 0.0 | +— / -2c7e844d-925a-43bb-8be8-65a71d11f964 |
| Jogador 7 | 2-4 | 89 | BUY_XP | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 90 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10899999737739563 | 0.0 | 0.0 | +— / -fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 11 | 1 | 14.0 | —/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2675422132015228 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 14.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36377549171447754 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 94 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6203517317771912 | 0.0 | 0.0 | +— / -caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 7 | 2-5 | 96 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 97 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 7 | 2-5 | 98 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7614842057228088 | 0.0 | 0.0 | +— / -dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 7 | 2-5 | 99 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057581815868616104 | 0.0 | 0.0 | +1d709136-338f-4fef-90fc-b2aa1b83d879 / -— |
| Jogador 7 | 2-5 | 100 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Varus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.387534424196929e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 102 | BUY | STABILIZE | 89.0 | 6 | 6 | 0 | 14.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22205376625061035 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 103 | BUY | STABILIZE | 89.0 | 6 | 3 | 0 | 14.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17440450191497803 | 0.0 | 0.0 | +a146f2d5-4da5-4c0e-bb09-de3177c72417 / -— |
| Jogador 7 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 1 | 0 | 14.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15022942423820496 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015429118648171425 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014364929869771004 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 107 | PASS | STABILIZE | 89.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 112 | BUY | STABILIZE | 89.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0474395789206028 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 113 | BUY | STABILIZE | 89.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06407973915338516 | 0.0 | 0.0 | +1e0a3ead-540d-4169-a1fc-3e79592564a0 / -— |
| Jogador 7 | 2-7 | 114 | BUY | STABILIZE | 89.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019214190542697906 | 0.0 | 0.0 | +ac02c0c4-a10d-497d-b6c1-d458ad7ae58c / -— |
| Jogador 7 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 0 | 0 | 26.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 0 | 0 | 26.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015785979107022285 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 117 | PASS | STABILIZE | 89.0 | 6 | 0 | 0 | 26.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 122 | BUY | STABILIZE | 89.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5752594470977783 | 0.0 | 0.0 | +5d00c8ab-55fb-42ec-b8ec-75011c7722fc / -— |
| Jogador 7 | 3-1 | 123 | BUY | STABILIZE | 89.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2611599862575531 | 0.0 | 0.0 | +033a84d9-70f6-46a8-a6eb-a2f03be70400 / -— |
| Jogador 7 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 89.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.030730459839105606 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20028893649578094 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09284424036741257 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 127 | SELL | STABILIZE | 89.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04018308222293854 | 0.0 | 0.0 | +— / -ac02c0c4-a10d-497d-b6c1-d458ad7ae58c |
| Jogador 7 | 3-1 | 128 | SELL | STABILIZE | 89.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -a146f2d5-4da5-4c0e-bb09-de3177c72417 |
| Jogador 7 | 3-1 | 129 | BUY_XP | STABILIZE | 89.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 130 | BUY | STABILIZE | 89.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006356180179864168 | 0.0 | 0.0 | +dbe9f465-e302-46d0-9bd4-93969fde6ecb / -— |
| Jogador 7 | 3-2 | 132 | BUY | STABILIZE | 89.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2724998891353607 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -— |
| Jogador 7 | 3-2 | 133 | BUY | STABILIZE | 89.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1175190880894661 | 0.0 | 0.0 | +46320c4e-6bc0-49d6-b150-be378fa422cf / -— |
| Jogador 7 | 3-2 | 134 | SELL | STABILIZE | 89.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.999999747378752e-05 | 0.0 | 0.0 | +— / -dbe9f465-e302-46d0-9bd4-93969fde6ecb |
| Jogador 7 | 3-2 | 135 | BUY | STABILIZE | 89.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04806273430585861 | 0.0 | 0.0 | +fa331d8d-1e0c-49b4-848e-8ad58859331c / -— |
| Jogador 7 | 3-2 | 136 | SELL | STABILIZE | 89.0 | 6 | 0 | 0 | 26.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01158076524734497 | 0.0 | 0.0 | +— / -fa331d8d-1e0c-49b4-848e-8ad58859331c |
| Jogador 7 | 3-2 | 137 | SELL | STABILIZE | 89.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 3-2 | 138 | BUY_XP | STABILIZE | 89.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 139 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08422263711690903 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 140 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01176848728209734 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 142 | BUY | STABILIZE | 89.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.837906539440155 | 0.0 | 0.0 | +652ff984-c3ac-48d7-9fb6-e95aed0a047d / -242805ca-f275-4e04-a2f5-81e0b6680dd1,7159421f-b5ea-4d10-9cc5-59186d62983d |
| Jogador 7 | 3-3 | 143 | BUY | STABILIZE | 89.0 | 6 | 7 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7407530546188354 | 0.0 | 0.0 | +ac1c8000-a262-4fb1-9cfb-9ac071e5e10f / -— |
| Jogador 7 | 3-3 | 144 | BUY_XP | STABILIZE | 89.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 145 | SELL | STABILIZE | 89.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -652ff984-c3ac-48d7-9fb6-e95aed0a047d |
| Jogador 7 | 3-3 | 146 | BUY_XP | STABILIZE | 89.0 | 6 | 5 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 147 | SELL | STABILIZE | 89.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050333332270383835 | 0.0 | 0.0 | +— / -46320c4e-6bc0-49d6-b150-be378fa422cf |
| Jogador 7 | 3-3 | 148 | BUY_XP | STABILIZE | 89.0 | 6 | 4 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 149 | SELL | STABILIZE | 89.0 | 6 | 0 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20900000631809235 | 0.0 | 0.0 | +— / -033a84d9-70f6-46a8-a6eb-a2f03be70400 |
| Jogador 7 | 3-3 | 150 | SELL | STABILIZE | 89.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2303333282470703 | 0.0 | 0.0 | +— / -daa7f698-2fa2-43d7-ae73-ec616b006db4 |
| Jogador 7 | 3-4 | 152 | BUY | STABILIZE | 79.0 | 6 | 10 | 1 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7279898524284363 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -— |
| Jogador 7 | 3-4 | 153 | BUY | STABILIZE | 79.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6494110226631165 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -— |
| Jogador 7 | 3-4 | 154 | BUY_XP | STABILIZE | 79.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 155 | SELL | STABILIZE | 79.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4790794253349304 | 0.0 | 0.0 | +— / -1e0a3ead-540d-4169-a1fc-3e79592564a0 |
| Jogador 7 | 3-4 | 156 | BUY | STABILIZE | 79.0 | 6 | 4 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27539312839508057 | 0.0 | 0.0 | +7e545d27-1847-4016-b42b-e7db1960ae89 / -— |
| Jogador 7 | 3-4 | 157 | MOVE_BENCH | STABILIZE | 79.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4217856228351593 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 158 | BUY | STABILIZE | 79.0 | 6 | 2 | 0 | 28.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058760739862918854 | 0.0 | 0.0 | +94d1da64-f0c8-4fd8-a610-b7e86f10378e / -— |
| Jogador 7 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 79.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09976159036159515 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 79.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0929320678114891 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 162 | BUY | STABILIZE | 79.0 | 7 | 6 | 0 | 28.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2854299247264862 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 7 | 3-5 | 163 | BUY | STABILIZE | 79.0 | 7 | 5 | 0 | 28.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11377984285354614 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 164 | BUY | STABILIZE | 79.0 | 7 | 2 | 0 | 28.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.040451645851135254 | 0.0 | 0.0 | +f546078f-fc3e-44a9-9b8f-25c46a043168 / -— |
| Jogador 7 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 79.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2916422486305237 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 79.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 167 | PASS | STABILIZE | 79.0 | 7 | 0 | 0 | 28.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 172 | BUY | STABILIZE | 79.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3756788671016693 | 0.0 | 0.0 | +69ccc61a-403b-4025-8359-b2061dc6ad10 / -— |
| Jogador 7 | 3-6 | 173 | MOVE_BOARD | STABILIZE | 79.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 174 | MOVE_BOARD | STABILIZE | 79.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 175 | PASS | STABILIZE | 79.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 182 | SELL | STABILIZE | 79.0 | 7 | 10 | 1 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014633333310484886 | 0.0 | 0.0 | +— / -94d1da64-f0c8-4fd8-a610-b7e86f10378e |
| Jogador 7 | 3-7 | 183 | BUY | STABILIZE | 79.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7184022665023804 | 0.0 | 0.0 | +21135c93-ae87-47a0-899c-7eaa0c2c30b8 / -— |
| Jogador 7 | 3-7 | 184 | SELL | STABILIZE | 79.0 | 7 | 9 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07973333448171616 | 0.0 | 0.0 | +— / -5d00c8ab-55fb-42ec-b8ec-75011c7722fc |
| Jogador 7 | 3-7 | 185 | BUY | STABILIZE | 79.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49100565910339355 | 0.0 | 0.0 | +06fb62e5-6766-4156-bf7d-0da443a9b20c / -1d709136-338f-4fef-90fc-b2aa1b83d879,69ccc61a-403b-4025-8359-b2061dc6ad10 |
| Jogador 7 | 3-7 | 186 | BUY_XP | STABILIZE | 79.0 | 7 | 8 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 187 | BUY_XP | STABILIZE | 79.0 | 7 | 4 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 188 | SELL | STABILIZE | 79.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12338826805353165 | 0.0 | 0.0 | +— / -06fb62e5-6766-4156-bf7d-0da443a9b20c |
| Jogador 7 | 3-7 | 189 | BUY_XP | STABILIZE | 79.0 | 7 | 8 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 190 | EQUIP_FROM_INVENTORY | STABILIZE | 79.0 | 7 | 4 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14710895717144012 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 79.0 | 7 | 10 | 1 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17436330020427704 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 79.0 | 7 | 10 | 1 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20930609107017517 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 194 | BUY_XP | STABILIZE | 79.0 | 7 | 10 | 1 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 195 | BUY_XP | STABILIZE | 79.0 | 7 | 6 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 196 | SELL | STABILIZE | 79.0 | 7 | 2 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07353641837835312 | 0.0 | 0.0 | +— / -f546078f-fc3e-44a9-9b8f-25c46a043168 |
| Jogador 7 | 4-1 | 197 | BUY_XP | STABILIZE | 79.0 | 7 | 4 | 0 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 198 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10166876018047333 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 79.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009327629581093788 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 200 | PASS | STABILIZE | 79.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 202 | BUY | STABILIZE | 79.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27255603671073914 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -— |
| Jogador 7 | 4-2 | 203 | BUY | STABILIZE | 79.0 | 7 | 5 | 0 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0032328066881746054 | 0.0 | 0.0 | +00f38555-1887-4fe2-9930-934055269095 / -— |
| Jogador 7 | 4-2 | 204 | MOVE_BOARD | STABILIZE | 79.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038968320935964584 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 205 | MOVE_BOARD | STABILIZE | 79.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015613083960488439 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 79.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 207 | PASS | STABILIZE | 79.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 212 | BUY | STABILIZE | 68.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1651892513036728 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 7 | 4-3 | 213 | BUY | STABILIZE | 68.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012147783301770687 | 0.0 | 0.0 | +485dab1f-b3a1-4170-8ed6-c0035072ae9b / -— |
| Jogador 7 | 4-3 | 214 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02582540363073349 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 215 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3069044053554535 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 216 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015037178993225098 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 217 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015466632321476936 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 218 | PASS | STABILIZE | 68.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 222 | SELL | STABILIZE | 68.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07280000299215317 | 0.0 | 0.0 | +— / -485dab1f-b3a1-4170-8ed6-c0035072ae9b |
| Jogador 7 | 4-4 | 223 | BUY | STABILIZE | 68.0 | 7 | 10 | 1 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7216153740882874 | 0.0 | 0.0 | +7b49fb38-6e0e-4a72-a2ce-0527827d36a6 / -— |
| Jogador 7 | 4-4 | 224 | SELL | STABILIZE | 68.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023960135877132416 | 0.0 | 0.0 | +— / -00f38555-1887-4fe2-9930-934055269095 |
| Jogador 7 | 4-4 | 225 | BUY | STABILIZE | 68.0 | 7 | 9 | 0 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2741754651069641 | 0.0 | 0.0 | +bae633d7-8337-461a-9a84-9c9758392bb6 / -— |
| Jogador 7 | 4-4 | 226 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.000470215076347813 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 227 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015074293129146099 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014889167621731758 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 229 | PASS | STABILIZE | 68.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 232 | SELL | STABILIZE | 68.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04173518717288971 | 0.0 | 0.0 | +— / -f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 4-5 | 233 | BUY | STABILIZE | 68.0 | 7 | 14 | 1 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16797485947608948 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 7 | 4-5 | 234 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00011333173461025581 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 235 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014857202768325806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 236 | PASS | STABILIZE | 68.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 242 | SELL | STABILIZE | 68.0 | 7 | 19 | 1 | 30.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018200000748038292 | 0.0 | 0.0 | +— / -f384fea6-9b6f-4f9c-81ec-a8284d5ba140 |
| Jogador 7 | 4-6 | 243 | BUY | STABILIZE | 68.0 | 7 | 21 | 2 | 30.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8679969906806946 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -1ff50c59-5133-459e-8bf1-d449c26efabf,4e206e09-40e3-4699-81cb-8aaf01109dea |
| Jogador 7 | 4-6 | 244 | SELL | STABILIZE | 68.0 | 7 | 20 | 2 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 |
| Jogador 7 | 4-6 | 245 | BUY | STABILIZE | 68.0 | 7 | 23 | 2 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8531782031059265 | 0.0 | 0.0 | +5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 / -6c691ca5-c042-46de-8d64-493514f2d793,cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 4-6 | 246 | MOVE_BENCH | STABILIZE | 68.0 | 7 | 20 | 2 | 14.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.18933576345443726 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 247 | MOVE_BENCH | STABILIZE | 68.0 | 7 | 20 | 2 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.19555459916591644 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 248 | EQUIP_FROM_INVENTORY | STABILIZE | 68.0 | 7 | 20 | 2 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0793628916144371 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 249 | MOVE_BENCH | STABILIZE | 68.0 | 7 | 20 | 2 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.19446352124214172 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 250 | EQUIP_FROM_INVENTORY | FAST8 | 68.0 | 7 | 20 | 2 | 36.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07835493236780167 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 252 | BUY | FAST8 | 68.0 | 7 | 29 | 2 | 36.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8093064427375793 | 0.0 | 0.0 | +58cbdbde-2151-438c-8897-902bef9bcd92 / -0cf5c315-d2f3-4854-a95b-07912b83ea81,7b49fb38-6e0e-4a72-a2ce-0527827d36a6 |
| Jogador 7 | 4-7 | 253 | BUY | STABILIZE | 68.0 | 7 | 26 | 2 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8786507248878479 | 0.0 | 0.0 | +b0c8ce74-5ce1-4ed0-82ac-f95013475f3c / -21135c93-ae87-47a0-899c-7eaa0c2c30b8,7e545d27-1847-4016-b42b-e7db1960ae89 |
| Jogador 7 | 4-7 | 254 | MOVE_BENCH | STABILIZE | 68.0 | 7 | 24 | 2 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.5515798330307007 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 255 | MOVE_BENCH | STABILIZE | 68.0 | 7 | 24 | 2 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.1704060435295105 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 256 | EQUIP_FROM_INVENTORY | STABILIZE | 68.0 | 7 | 24 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08340783417224884 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 257 | BUY | STABILIZE | 68.0 | 7 | 24 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10258112847805023 | 0.0 | 0.0 | +18d25cfb-d559-4efa-b708-c9987987590b / -— |
| Jogador 7 | 4-7 | 258 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 22 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003150721313431859 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 259 | SELL | STABILIZE | 68.0 | 7 | 22 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5389999747276306 | 0.0 | 0.0 | +— / -58cbdbde-2151-438c-8897-902bef9bcd92 |
| Jogador 7 | 4-7 | 260 | SELL | STABILIZE | 68.0 | 7 | 30 | 3 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42864787578582764 | 0.0 | 0.0 | +— / -18d25cfb-d559-4efa-b708-c9987987590b |
| Jogador 7 | 5-1 | 262 | BUY | STABILIZE | 68.0 | 7 | 41 | 4 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.00907857995480299 | 0.0 | 0.0 | +99857cfa-b422-4167-bb01-d9fd94a55d88 / -— |
| Jogador 7 | 5-1 | 263 | BUY | STABILIZE | 68.0 | 7 | 39 | 3 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.11561312526464462 | 0.0 | 0.0 | +4432f76a-94cc-4a96-b72b-1cf35b310dca / -— |
| Jogador 7 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 68.0 | 7 | 34 | 3 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08439714461565018 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 265 | CRAFT_AND_EQUIP | STABILIZE | 68.0 | 7 | 34 | 3 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19517089426517487 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 266 | MOVE_BENCH | STABILIZE | 68.0 | 7 | 34 | 3 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15041689574718475 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 267 | BUY | FAST8 | 68.0 | 7 | 34 | 3 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.065437451004982 | 0.0 | 0.0 | +3658b5d8-450f-451a-8487-5b3bdd7c385b / -— |
| Jogador 7 | 5-1 | 268 | BUY | FAST8 | 68.0 | 7 | 32 | 3 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30877870321273804 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -— |
| Jogador 7 | 5-1 | 269 | MOVE_BOARD | FAST8 | 68.0 | 7 | 29 | 2 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019930540584027767 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 270 | MOVE_BOARD | FAST8 | 68.0 | 7 | 29 | 2 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013223376125097275 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 272 | BUY | FAST8 | 68.0 | 7 | 39 | 3 | 46.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5909007787704468 | 0.0 | 0.0 | +499f10b9-47ba-4cab-add1-31b452acae6d / -— |
| Jogador 7 | 5-2 | 273 | BUY | FAST8 | 68.0 | 7 | 37 | 3 | 46.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3096180260181427 | 0.0 | 0.0 | +64215569-2a69-410d-a2f9-172544bef858 / -— |
| Jogador 7 | 5-2 | 274 | BUY | FAST8 | 68.0 | 7 | 34 | 3 | 46.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1171753779053688 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -— |
| Jogador 7 | 5-2 | 275 | MOVE_BOARD | FAST8 | 68.0 | 7 | 32 | 3 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 276 | MOVE_BOARD | FAST8 | 68.0 | 7 | 32 | 3 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01420395728200674 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 277 | PASS | FAST8 | 68.0 | 7 | 32 | 3 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04085714370012283 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 282 | MOVE_BOARD | FAST8 | 55.0 | 7 | 40 | 4 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.760942339198664e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 283 | MOVE_BOARD | FAST8 | 55.0 | 7 | 40 | 4 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06814080476760864 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 284 | MOVE_BOARD | FAST8 | 55.0 | 7 | 40 | 4 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 285 | PASS | FAST8 | 55.0 | 7 | 40 | 4 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04714285582304001 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 292 | SELL | FAST8 | 55.0 | 7 | 50 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03049047663807869 | 0.0 | 0.0 | +— / -42f739bb-e676-4a27-a96f-c09d09d592bb |
| Jogador 7 | 5-4 | 293 | BUY | FAST8 | 55.0 | 7 | 51 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2592008709907532 | 0.0 | 0.0 | +407092ea-3a14-4555-9ebd-64a36c41d1d0 / -— |
| Jogador 7 | 5-4 | 294 | MOVE_BOARD | FAST8 | 55.0 | 7 | 47 | 4 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006825841497629881 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 295 | MOVE_BOARD | FAST8 | 55.0 | 7 | 47 | 4 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014984969981014729 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 296 | SELL | FAST8 | 55.0 | 7 | 47 | 4 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -3658b5d8-450f-451a-8487-5b3bdd7c385b |
| Jogador 7 | 5-4 | 297 | BUY | FAST8 | 55.0 | 7 | 49 | 4 | 46.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0665859803557396 | 0.0 | 0.0 | +7de5aac5-85d7-4add-b5a7-1c89be9d7e40 / -— |
| Jogador 7 | 5-4 | 298 | MOVE_BOARD | FAST8 | 55.0 | 7 | 47 | 4 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00010913916048593819 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 299 | MOVE_BOARD | FAST8 | 55.0 | 7 | 47 | 4 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015004112385213375 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 301 | SELL | FAST8 | 55.0 | 7 | 56 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017465360462665558 | 0.0 | 0.0 | +— / -7de5aac5-85d7-4add-b5a7-1c89be9d7e40 |
| Jogador 7 | 5-5 | 302 | BUY | FAST8 | 55.0 | 7 | 58 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34121906757354736 | 0.0 | 0.0 | +b250e22d-7193-4ea5-879d-5c7b41145719 / -— |
| Jogador 7 | 5-5 | 303 | MOVE_BOARD | FAST8 | 55.0 | 7 | 57 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.0116169657267164e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 304 | MOVE_BOARD | FAST8 | 55.0 | 7 | 57 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015019345097243786 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 305 | MOVE_BOARD | FAST8 | 55.0 | 7 | 57 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014978600665926933 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 306 | PASS | FAST8 | 55.0 | 7 | 57 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09242651611566544 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 312 | SELL | FAST8 | 40.0 | 7 | 67 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049779895693063736 | 0.0 | 0.0 | +— / -7fb0217d-521c-42b5-995c-81e299b3b934 |
| Jogador 7 | 5-6 | 313 | BUY | FAST8 | 40.0 | 7 | 70 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28168970346450806 | 0.0 | 0.0 | +9c3b3b78-e99c-4947-b958-cce156ecccb1 / -— |
| Jogador 7 | 5-6 | 314 | SELL | FAST8 | 40.0 | 7 | 67 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -80c51b33-0a85-4f21-a797-9551aa10760f |
| Jogador 7 | 5-6 | 315 | BUY | FAST8 | 40.0 | 7 | 71 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031091513112187386 | 0.0 | 0.0 | +b311d350-7bab-48ee-9833-0883606b4a2f / -— |
| Jogador 7 | 5-6 | 316 | MOVE_BOARD | FAST8 | 40.0 | 7 | 68 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007373717380687594 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 317 | MOVE_BOARD | FAST8 | 40.0 | 7 | 68 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1773938685655594 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 318 | PASS | FAST8 | 40.0 | 7 | 68 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11292767524719238 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 322 | SELL | ECON | 40.0 | 8 | 79 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03692783787846565 | 0.0 | 0.0 | +— / -b311d350-7bab-48ee-9833-0883606b4a2f |
| Jogador 7 | 5-7 | 323 | BUY | ECON | 40.0 | 8 | 82 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.931905210018158 | 0.0 | 0.0 | +920ec426-49cf-489f-aad8-3f5461b93be6 / -— |
| Jogador 7 | 5-7 | 324 | SELL | ECON | 40.0 | 8 | 79 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09960000216960907 | 0.0 | 0.0 | +— / -9c3b3b78-e99c-4947-b958-cce156ecccb1 |
| Jogador 7 | 5-7 | 325 | BUY | ECON | 40.0 | 8 | 82 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.433737576007843 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -— |
| Jogador 7 | 5-7 | 326 | MOVE_BENCH | ECON | 40.0 | 8 | 80 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49850642681121826 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 327 | BUY | ECON | 40.0 | 8 | 80 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09636013209819794 | 0.0 | 0.0 | +56332309-e8e8-464a-904f-e9253912cd2f / -— |
| Jogador 7 | 5-7 | 328 | MOVE_BOARD | ECON | 40.0 | 8 | 76 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050022199749946594 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 329 | MOVE_BOARD | ECON | 40.0 | 8 | 76 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1221994087100029 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 330 | MOVE_BOARD | ECON | 40.0 | 8 | 76 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03764220327138901 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ECON | 40.0 | 8 | 86 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12819766998291016 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 333 | SELL | ECON | 40.0 | 8 | 86 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04209916666150093 | 0.0 | 0.0 | +— / -56332309-e8e8-464a-904f-e9253912cd2f |
| Jogador 7 | 6-1 | 334 | BUY | ECON | 40.0 | 8 | 90 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.062389850616455 | 0.0 | 0.0 | +8025eaf5-b02b-4f94-b381-b94321bca206 / -499f10b9-47ba-4cab-add1-31b452acae6d,99857cfa-b422-4167-bb01-d9fd94a55d88 |
| Jogador 7 | 6-1 | 335 | BUY | ECON | 40.0 | 8 | 88 | 5 | 44.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1422262340784073 | 0.0 | 0.0 | +00497e43-57ef-4c25-a34b-0be0155bb92d / -— |
| Jogador 7 | 6-1 | 336 | MOVE_BOARD | ECON | 40.0 | 8 | 84 | 5 | 44.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0018703022506088018 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 337 | MOVE_BENCH | ECON | 40.0 | 8 | 84 | 5 | 44.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.581858217716217 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 338 | BUY | ECON | 40.0 | 8 | 84 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2239326387643814 | 0.0 | 0.0 | +663beb45-28d7-42de-b6b8-a81e8676f55f / -— |
| Jogador 7 | 6-1 | 339 | MOVE_BOARD | ECON | 40.0 | 8 | 81 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004729472566395998 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 340 | MOVE_BOARD | ECON | 40.0 | 8 | 81 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01410819310694933 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 342 | SELL | ECON | 40.0 | 8 | 93 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -663beb45-28d7-42de-b6b8-a81e8676f55f |
| Jogador 7 | 6-2 | 343 | BUY | ECON | 40.0 | 8 | 96 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0074563026428223 | 0.0 | 0.0 | +9f271ee0-c506-40b7-b3f3-bac209974ba2 / -— |
| Jogador 7 | 6-2 | 344 | SELL | ECON | 40.0 | 8 | 94 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -00497e43-57ef-4c25-a34b-0be0155bb92d |
| Jogador 7 | 6-2 | 345 | BUY | ECON | 40.0 | 8 | 98 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08597172796726227 | 0.0 | 0.0 | +c55e9bf2-c9cf-4b76-a40c-6e8d73205402 / -— |
| Jogador 7 | 6-2 | 346 | MOVE_BOARD | ECON | 40.0 | 8 | 94 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.8727636415860616e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 347 | MOVE_BOARD | ECON | 40.0 | 8 | 94 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499923225492239 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 348 | MOVE_BOARD | ECON | 40.0 | 8 | 94 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0152767114341259 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 349 | PASS | ECON | 40.0 | 8 | 94 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1501854658126831 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 352 | SELL | ALL_IN | 23.0 | 8 | 104 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03937958925962448 | 0.0 | 0.0 | +— / -c55e9bf2-c9cf-4b76-a40c-6e8d73205402 |
| Jogador 7 | 6-3 | 353 | BUY | ALL_IN | 23.0 | 8 | 108 | 5 | 52.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1112892627716064 | 0.0 | 0.0 | +b053a0fd-0f0b-4343-a920-f0a36d36e771 / -920ec426-49cf-489f-aad8-3f5461b93be6,bae633d7-8337-461a-9a84-9c9758392bb6 |
| Jogador 7 | 6-3 | 354 | BUY | ALL_IN | 23.0 | 8 | 105 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5062718391418457 | 0.0 | 0.0 | +ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 / -— |
| Jogador 7 | 6-3 | 355 | SELL | ALL_IN | 23.0 | 8 | 101 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6859999895095825 | 0.0 | 0.0 | +— / -b053a0fd-0f0b-4343-a920-f0a36d36e771 |
| Jogador 7 | 6-3 | 356 | BUY | ALL_IN | 23.0 | 8 | 109 | 5 | 46.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.869873046875 | 0.0 | 0.0 | +497fbcb9-9d15-43f0-ad71-96eeceeee99d / -ac1c8000-a262-4fb1-9cfb-9ac071e5e10f,bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 6-3 | 357 | MOVE_BENCH | ALL_IN | 23.0 | 8 | 108 | 5 | 44.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.33757466077804565 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 358 | EQUIP_FROM_INVENTORY | ALL_IN | 23.0 | 8 | 108 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1317611187696457 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 359 | EQUIP_FROM_INVENTORY | ALL_IN | 23.0 | 8 | 108 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07324820756912231 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 360 | BUY | ALL_IN | 23.0 | 8 | 108 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09404259920120239 | 0.0 | 0.0 | +bfff6629-3ccc-4136-82a4-319a2fc5350e / -— |
| Jogador 7 | 6-4 | 362 | BUY | ALL_IN | 23.0 | 8 | 115 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0058317184448242 | 0.0 | 0.0 | +d8ca1093-815c-4f3e-af3e-fd6c4ab6ecd8 / -— |
| Jogador 7 | 6-4 | 363 | SELL | ALL_IN | 23.0 | 8 | 111 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07100000232458115 | 0.0 | 0.0 | +— / -497fbcb9-9d15-43f0-ad71-96eeceeee99d |
| Jogador 7 | 6-4 | 364 | BUY | ALL_IN | 23.0 | 8 | 114 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.17414112389087677 | 0.0 | 0.0 | +14c1ca8a-e057-4184-9c83-0b8846824932 / -— |
| Jogador 7 | 6-4 | 365 | EQUIP_FROM_INVENTORY | ALL_IN | 23.0 | 8 | 110 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08008281886577606 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 366 | MOVE_BOARD | ALL_IN | 23.0 | 8 | 110 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.8636355864364305e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 367 | MOVE_BOARD | ALL_IN | 23.0 | 8 | 110 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015001283027231693 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 368 | MOVE_BOARD | ALL_IN | 23.0 | 8 | 110 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998398721218109 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 369 | PASS | ALL_IN | 23.0 | 8 | 110 | 5 | 48.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5401641726493835 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 372 | BUY | ALL_IN | 23.0 | 8 | 120 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6401458978652954 | 0.0 | 0.0 | +c3596d89-03d2-4fc7-afaf-591f10423252 / -— |
| Jogador 7 | 6-5 | 373 | SELL | ALL_IN | 23.0 | 8 | 117 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5121666789054871 | 0.0 | 0.0 | +— / -217a3ebb-1953-4f1e-bfdd-a3c9438e791e |
| Jogador 7 | 6-5 | 374 | BUY | ALL_IN | 23.0 | 8 | 120 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46590349078178406 | 0.0 | 0.0 | +e903e009-8dae-4fc9-b0ec-bc028c3f9f3e / -— |
| Jogador 7 | 6-5 | 375 | SELL | ALL_IN | 23.0 | 8 | 119 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -64215569-2a69-410d-a2f9-172544bef858 |
| Jogador 7 | 6-5 | 376 | BUY | ALL_IN | 23.0 | 8 | 122 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40513381361961365 | 0.0 | 0.0 | +24d03668-5dc4-4b40-9439-a1d67522d0a3 / -— |
| Jogador 7 | 6-5 | 377 | MOVE_BOARD | ALL_IN | 23.0 | 8 | 119 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 378 | MOVE_BOARD | ALL_IN | 23.0 | 8 | 119 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500083040446043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 379 | PASS | ALL_IN | 23.0 | 8 | 119 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5525792837142944 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 382 | SELL | ALL_IN | 6.0 | 8 | 130 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09960000216960907 | 0.0 | 0.0 | +— / -24d03668-5dc4-4b40-9439-a1d67522d0a3 |
| Jogador 7 | 6-6 | 383 | BUY | ALL_IN | 6.0 | 8 | 133 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44982030987739563 | 0.0 | 0.0 | +ff6d5b66-5b8f-49b1-bbad-4231b794c2f1 / -— |
| Jogador 7 | 6-6 | 384 | SELL | ALL_IN | 6.0 | 8 | 130 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1377333402633667 | 0.0 | 0.0 | +— / -ff6d5b66-5b8f-49b1-bbad-4231b794c2f1 |
| Jogador 7 | 6-6 | 385 | BUY | ALL_IN | 6.0 | 8 | 133 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.227092906832695 | 0.0 | 0.0 | +0366f83c-b9d4-47c2-aa5e-4dc1021bd201 / -— |
| Jogador 7 | 6-6 | 386 | SELL | ALL_IN | 6.0 | 8 | 129 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -0366f83c-b9d4-47c2-aa5e-4dc1021bd201 |
| Jogador 7 | 6-6 | 387 | BUY | ALL_IN | 6.0 | 8 | 133 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22710131108760834 | 0.0 | 0.0 | +533790d1-aca6-417d-b163-b0bda70d1500 / -— |
| Jogador 7 | 6-6 | 388 | MOVE_BOARD | ALL_IN | 6.0 | 8 | 129 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.2229837049490015e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 389 | MOVE_BOARD | ALL_IN | 6.0 | 8 | 129 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499962992966175 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 390 | MOVE_BOARD | ALL_IN | 6.0 | 8 | 129 | 5 | 56.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000196173787117 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031589943915605545 | 0.0 | 0.0 | +88a02960-5ebe-4b20-b667-1a8ce2728578 / -— |
| Jogador 8 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16182130575180054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3620654344558716 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012301865965127945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5032565593719482 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0140845775604248 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36052340269088745 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 25 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2815742790699005 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.976382315158844 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 39 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17352721095085144 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 40 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25140801072120667 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 41 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11591137945652008 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 42 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 50 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1142686605453491 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -88a02960-5ebe-4b20-b667-1a8ce2728578,dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 2-1 | 51 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20080365240573883 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 52 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17912892997264862 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059163305908441544 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1034753322601318 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12414442747831345 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03405940160155296 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32108646631240845 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03419312834739685 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 59 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2614271342754364 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 63 | BUY | STABILIZE | 95.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2963619828224182 | 0.0 | 0.0 | +ebe77c97-f249-4265-ae03-bc8115a4795f / -— |
| Jogador 8 | 2-2 | 64 | SELL | STABILIZE | 95.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21314561367034912 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-2 | 65 | BUY_XP | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 66 | PASS | STABILIZE | 95.0 | 4 | 2 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 8 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0461983680725098 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 73 | BUY | STABILIZE | 90.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2250448763370514 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 74 | SELL | STABILIZE | 90.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-3 | 75 | BUY | STABILIZE | 90.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25466209650039673 | 0.0 | 0.0 | +01f4a73c-7202-4ee3-964e-d32370c3c547 / -— |
| Jogador 8 | 2-3 | 76 | SELL | STABILIZE | 90.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4267919659614563 | 0.0 | 0.0 | +— / -01f4a73c-7202-4ee3-964e-d32370c3c547 |
| Jogador 8 | 2-3 | 77 | SELL | STABILIZE | 90.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13300000131130219 | 0.0 | 0.0 | +— / -ebe77c97-f249-4265-ae03-bc8115a4795f |
| Jogador 8 | 2-3 | 78 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16691596806049347 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 79 | BUY_XP | STABILIZE | 90.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 80 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6312364339828491 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 82 | BUY | STABILIZE | 85.0 | 5 | 7 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8192214965820312 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 8 | 2-4 | 83 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2852819263935089 | 0.0 | 0.0 | +3644801e-2247-403d-8b81-d2d3f15c2f55 / -— |
| Jogador 8 | 2-4 | 84 | BUY | STABILIZE | 85.0 | 5 | 5 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1715211272239685 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 85 | SELL | STABILIZE | 85.0 | 5 | 2 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13300000131130219 | 0.0 | 0.0 | +— / -3644801e-2247-403d-8b81-d2d3f15c2f55 |
| Jogador 8 | 2-4 | 86 | SELL | STABILIZE | 85.0 | 5 | 3 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08766666799783707 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-4 | 87 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14467568695545197 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 88 | SELL | STABILIZE | 85.0 | 5 | 3 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07966666668653488 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 2-4 | 89 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 6 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0016735019162297249 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 90 | SELL | STABILIZE | 85.0 | 5 | 6 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11206073313951492 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-5 | 92 | BUY | STABILIZE | 85.0 | 5 | 15 | 1 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9582369923591614 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 93 | BUY | STABILIZE | 85.0 | 5 | 13 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37755587697029114 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 94 | BUY | STABILIZE | 85.0 | 5 | 12 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2621837854385376 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 95 | SELL | STABILIZE | 85.0 | 5 | 9 | 0 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5529999732971191 | 0.0 | 0.0 | +— / -b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 2-5 | 96 | SELL | STABILIZE | 85.0 | 5 | 10 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4954918324947357 | 0.0 | 0.0 | +— / -2e656a3d-eed0-40bb-a831-443d972d6588 |
| Jogador 8 | 2-5 | 97 | SELL | STABILIZE | 85.0 | 5 | 13 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8403252363204956 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 8 | 2-5 | 98 | SELL | STABILIZE | 85.0 | 5 | 14 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38855549693107605 | 0.0 | 0.0 | +— / -5de56114-806a-4f58-8241-b3b8434a2154 |
| Jogador 8 | 2-5 | 99 | BUY | STABILIZE | 85.0 | 5 | 15 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09109673649072647 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 13 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31087327003479004 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 102 | BUY | STABILIZE | 85.0 | 5 | 20 | 2 | 16.0 | Espinhos Negros/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.959572970867157 | 0.0 | 0.0 | +c737e99a-613e-4f1a-a50e-7a865169f90c / -— |
| Jogador 8 | 2-6 | 103 | BUY | STABILIZE | 85.0 | 5 | 19 | 1 | 16.0 | Espinhos Negros/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3582055866718292 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 104 | BUY | STABILIZE | 85.0 | 5 | 16 | 1 | 16.0 | Espinhos Negros/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3649255633354187 | 0.0 | 0.0 | +b482ecdd-cc1a-40fa-8c21-cd1cac92b594 / -— |
| Jogador 8 | 2-6 | 105 | SELL | STABILIZE | 85.0 | 5 | 15 | 1 | 16.0 | Espinhos Negros/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc |
| Jogador 8 | 2-6 | 106 | BUY_XP | STABILIZE | 85.0 | 5 | 18 | 1 | 16.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 107 | BUY_XP | STABILIZE | 85.0 | 5 | 14 | 1 | 16.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 108 | BUY_XP | STABILIZE | 85.0 | 5 | 10 | 1 | 16.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07040499895811081 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 109 | BUY_XP | STABILIZE | 85.0 | 6 | 6 | 0 | 16.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 110 | SELL | STABILIZE | 85.0 | 6 | 2 | 0 | 16.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6099604368209839 | 0.0 | 0.0 | +— / -b482ecdd-cc1a-40fa-8c21-cd1cac92b594 |
| Jogador 8 | 2-7 | 112 | BUY | STABILIZE | 80.0 | 6 | 8 | 0 | 16.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3624860346317291 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 113 | BUY | STABILIZE | 80.0 | 6 | 5 | 0 | 16.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2840205729007721 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 114 | BUY_XP | STABILIZE | 80.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 115 | SELL | STABILIZE | 80.0 | 6 | 0 | 0 | 16.0 | Espinhos Negros/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14749163389205933 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 2-7 | 116 | SELL | STABILIZE | 80.0 | 6 | 1 | 0 | 16.0 | Espinhos Negros/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6276326179504395 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 2-7 | 117 | BUY_XP | STABILIZE | 80.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 118 | SELL | STABILIZE | 80.0 | 6 | 0 | 0 | 16.0 | Espinhos Negros/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 2-7 | 119 | SELL | STABILIZE | 80.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-7 | 120 | BUY_XP | STABILIZE | 80.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 122 | BUY | STABILIZE | 80.0 | 6 | 5 | 0 | 16.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5606078505516052 | 0.0 | 0.0 | +a5c0595b-85f9-4c71-a156-675d22a7b3c2 / -— |
| Jogador 8 | 3-1 | 123 | BUY | STABILIZE | 80.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.20150865614414215 | 0.0 | 0.0 | +7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 / -— |
| Jogador 8 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 80.0 | 6 | 1 | 0 | 16.0 | Espinhos Negros/DA_18_Warwick | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24866244196891785 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 125 | SELL | STABILIZE | 80.0 | 6 | 1 | 0 | 16.0 | Espinhos Negros/DA_18_Warwick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1443961262702942 | 0.0 | 0.0 | +— / -7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 |
| Jogador 8 | 3-1 | 126 | SELL | STABILIZE | 80.0 | 6 | 3 | 0 | 16.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.536689043045044 | 0.0 | 0.0 | +— / -a5c0595b-85f9-4c71-a156-675d22a7b3c2 |
| Jogador 8 | 3-1 | 127 | BUY | STABILIZE | 80.0 | 6 | 5 | 0 | 16.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09739480912685394 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 128 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 1 | 0 | 16.0 | Espinhos Negros/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5797179937362671 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 129 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018137209117412567 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 130 | SELL | STABILIZE | 80.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06416017562150955 | 0.0 | 0.0 | +— / -4d995451-2e5c-43c2-93f0-22e074e35ab2 |
| Jogador 8 | 3-2 | 132 | BUY | STABILIZE | 80.0 | 6 | 11 | 1 | 18.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004717349540442228 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 133 | BUY | STABILIZE | 80.0 | 6 | 7 | 0 | 18.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14702461659908295 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 134 | BUY | STABILIZE | 80.0 | 6 | 6 | 0 | 18.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014954843558371067 | 0.0 | 0.0 | +5326031a-1b7e-4dbd-b58b-1e81029d42a1 / -— |
| Jogador 8 | 3-2 | 135 | SELL | STABILIZE | 80.0 | 6 | 4 | 0 | 18.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4177192747592926 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-2 | 136 | BUY_XP | STABILIZE | 80.0 | 6 | 5 | 0 | 18.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 137 | SELL | STABILIZE | 80.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07997411489486694 | 0.0 | 0.0 | +— / -5326031a-1b7e-4dbd-b58b-1e81029d42a1 |
| Jogador 8 | 3-2 | 138 | BUY | STABILIZE | 80.0 | 6 | 3 | 0 | 18.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08327861875295639 | 0.0 | 0.0 | +ece93d63-49d6-472c-9a10-7ece135feacc / -— |
| Jogador 8 | 3-2 | 139 | SELL | STABILIZE | 80.0 | 6 | 1 | 0 | 18.0 | Espinhos Negros/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05833333358168602 | 0.0 | 0.0 | +— / -ece93d63-49d6-472c-9a10-7ece135feacc |
| Jogador 8 | 3-2 | 140 | SELL | STABILIZE | 80.0 | 6 | 3 | 0 | 18.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09626069664955139 | 0.0 | 0.0 | +— / -4ac49c80-f0c3-47ae-a031-96928d244e13 |
| Jogador 8 | 3-3 | 142 | BUY | STABILIZE | 70.0 | 6 | 12 | 1 | 18.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1388004869222641 | 0.0 | 0.0 | +3bf8af53-85e7-4e5b-8cf8-b7198a955e8d / -— |
| Jogador 8 | 3-3 | 143 | BUY | STABILIZE | 70.0 | 6 | 11 | 1 | 18.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14220501482486725 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 144 | BUY | STABILIZE | 70.0 | 6 | 8 | 0 | 18.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055941443890333176 | 0.0 | 0.0 | +1af578c1-57cf-4752-93e7-d0eebc6e8ae5 / -— |
| Jogador 8 | 3-3 | 145 | SELL | STABILIZE | 70.0 | 6 | 6 | 0 | 18.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4175935983657837 | 0.0 | 0.0 | +— / -3bf8af53-85e7-4e5b-8cf8-b7198a955e8d |
| Jogador 8 | 3-3 | 146 | SELL | STABILIZE | 70.0 | 6 | 7 | 0 | 18.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3490000069141388 | 0.0 | 0.0 | +— / -1af578c1-57cf-4752-93e7-d0eebc6e8ae5 |
| Jogador 8 | 3-3 | 147 | BUY | STABILIZE | 70.0 | 6 | 9 | 0 | 18.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010761383920907974 | 0.0 | 0.0 | +7c751800-5068-42ba-a253-3a49bfe52334 / -— |
| Jogador 8 | 3-3 | 148 | BUY_XP | STABILIZE | 70.0 | 6 | 8 | 0 | 18.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 149 | BUY_XP | STABILIZE | 70.0 | 6 | 4 | 0 | 18.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0609700009226799 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 150 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 0 | 0 | 18.0 | Espinhos Negros/DA_18_Warwick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40251728892326355 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 152 | BUY | STABILIZE | 70.0 | 7 | 6 | 0 | 24.0 | Espinhos Negros/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07962382584810257 | 0.0 | 0.0 | +41782483-877e-4dce-bef9-4f1f3d5757bd / -— |
| Jogador 8 | 3-4 | 153 | BUY | STABILIZE | 70.0 | 7 | 3 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5604977607727051 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 154 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0003296881914138794 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 155 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 156 | PASS | STABILIZE | 70.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 162 | BUY | STABILIZE | 70.0 | 7 | 5 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20103880763053894 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 163 | BUY | STABILIZE | 70.0 | 7 | 2 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23809848725795746 | 0.0 | 0.0 | +fa5dc86b-f736-4083-b9df-5cc174b726f2 / -— |
| Jogador 8 | 3-5 | 164 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001866067061200738 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 166 | PASS | STABILIZE | 70.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 172 | BUY | STABILIZE | 70.0 | 7 | 7 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27718305587768555 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 173 | BUY | STABILIZE | 70.0 | 7 | 3 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27935177087783813 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 174 | SELL | STABILIZE | 70.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09033333510160446 | 0.0 | 0.0 | +— / -7c751800-5068-42ba-a253-3a49bfe52334 |
| Jogador 8 | 3-6 | 175 | SELL | STABILIZE | 70.0 | 7 | 1 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -fa5dc86b-f736-4083-b9df-5cc174b726f2 |
| Jogador 8 | 3-6 | 176 | SELL | STABILIZE | 70.0 | 7 | 3 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1289999932050705 | 0.0 | 0.0 | +— / -9b5e9e71-6772-49bc-979f-11f446f27b11 |
| Jogador 8 | 3-6 | 177 | BUY | STABILIZE | 70.0 | 7 | 6 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02883937582373619 | 0.0 | 0.0 | +b55260cd-3c6a-4cb8-99d0-b7c6471103ad / -— |
| Jogador 8 | 3-6 | 178 | SELL | STABILIZE | 70.0 | 7 | 3 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050333332270383835 | 0.0 | 0.0 | +— / -b55260cd-3c6a-4cb8-99d0-b7c6471103ad |
| Jogador 8 | 3-6 | 179 | SELL | STABILIZE | 70.0 | 7 | 6 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15166667103767395 | 0.0 | 0.0 | +— / -a23ee552-279e-4c6c-aa05-6197043e8f1d |
| Jogador 8 | 3-6 | 180 | SELL | STABILIZE | 70.0 | 7 | 10 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5016666650772095 | 0.0 | 0.0 | +— / -41782483-877e-4dce-bef9-4f1f3d5757bd |
| Jogador 8 | 3-7 | 182 | BUY | STABILIZE | 60.0 | 7 | 19 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2829747200012207 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 183 | BUY | STABILIZE | 60.0 | 7 | 16 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001863613142631948 | 0.0 | 0.0 | +3625f791-4c9f-4b95-bdf7-4a322dcd55d3 / -— |
| Jogador 8 | 3-7 | 184 | BUY | STABILIZE | 60.0 | 7 | 13 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035460978746414185 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 8 | 3-7 | 185 | BUY_XP | STABILIZE | 60.0 | 7 | 10 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 186 | BUY_XP | STABILIZE | 60.0 | 7 | 6 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 187 | SELL | STABILIZE | 60.0 | 7 | 2 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04786241054534912 | 0.0 | 0.0 | +— / -112206a4-c285-4f76-878a-056248cba468 |
| Jogador 8 | 3-7 | 188 | SELL | STABILIZE | 60.0 | 7 | 5 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3596666753292084 | 0.0 | 0.0 | +— / -3625f791-4c9f-4b95-bdf7-4a322dcd55d3 |
| Jogador 8 | 3-7 | 189 | BUY | STABILIZE | 60.0 | 7 | 8 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05423246696591377 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 8 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 7 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00012046053598169237 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 192 | BUY | STABILIZE | 60.0 | 7 | 12 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8384544253349304 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -— |
| Jogador 8 | 4-1 | 193 | BUY | STABILIZE | 60.0 | 7 | 11 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1981806457042694 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 8 | 4-1 | 194 | BUY | STABILIZE | 60.0 | 7 | 8 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2777503430843353 | 0.0 | 0.0 | +2c153083-6c43-425e-90d5-23f7f2058592 / -— |
| Jogador 8 | 4-1 | 195 | BUY | STABILIZE | 60.0 | 7 | 5 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2855904996395111 | 0.0 | 0.0 | +b2a77bec-e150-4d98-847c-9f2cfb50cbe7 / -— |
| Jogador 8 | 4-1 | 196 | CRAFT_AND_EQUIP | STABILIZE | 60.0 | 7 | 4 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21870186924934387 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 197 | CRAFT_AND_EQUIP | STABILIZE | 60.0 | 7 | 4 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17231479287147522 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 4 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0030964284669607878 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 4 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 4 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014979253523051739 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 202 | SELL | STABILIZE | 60.0 | 7 | 10 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00579217029735446 | 0.0 | 0.0 | +— / -a14e4b8f-77c5-4909-a9ee-0044b836a877 |
| Jogador 8 | 4-2 | 203 | BUY | STABILIZE | 60.0 | 7 | 11 | 1 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038557734340429306 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -— |
| Jogador 8 | 4-2 | 204 | SELL | STABILIZE | 60.0 | 7 | 8 | 0 | 24.0 | Espinhos Negros/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07783333212137222 | 0.0 | 0.0 | +— / -82e109f9-54c8-492d-93e5-7e0dd0034b15 |
| Jogador 8 | 4-2 | 205 | BUY | STABILIZE | 60.0 | 7 | 11 | 1 | 24.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30323177576065063 | 0.0 | 0.0 | +08a36d54-bb5c-48a6-afb1-e0f9943bf069 / -— |
| Jogador 8 | 4-2 | 206 | SELL | STABILIZE | 60.0 | 7 | 7 | 0 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05556792393326759 | 0.0 | 0.0 | +— / -dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 |
| Jogador 8 | 4-2 | 207 | BUY | STABILIZE | 60.0 | 7 | 10 | 1 | 24.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05346700921654701 | 0.0 | 0.0 | +7e0c9595-0ca2-44d4-bfe9-3752c7a89e0d / -— |
| Jogador 8 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 8 | 0 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 209 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 8 | 0 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999802224338055 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 210 | PASS | STABILIZE | 60.0 | 7 | 8 | 0 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 212 | SELL | STABILIZE | 60.0 | 7 | 15 | 1 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -7e0c9595-0ca2-44d4-bfe9-3752c7a89e0d |
| Jogador 8 | 4-3 | 213 | BUY | STABILIZE | 60.0 | 7 | 17 | 1 | 24.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.797237753868103 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 8 | 4-3 | 214 | SELL | STABILIZE | 60.0 | 7 | 14 | 1 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0141333332285285 | 0.0 | 0.0 | +— / -08a36d54-bb5c-48a6-afb1-e0f9943bf069 |
| Jogador 8 | 4-3 | 215 | BUY | STABILIZE | 60.0 | 7 | 18 | 1 | 24.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.702843189239502 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 8 | 4-3 | 216 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 16 | 1 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0008353058365173638 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 217 | MOVE_BOARD | STABILIZE | 60.0 | 7 | 16 | 1 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03408973664045334 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 218 | PASS | STABILIZE | 60.0 | 7 | 16 | 1 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025714285671710968 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 222 | SELL | STABILIZE | 49.0 | 7 | 22 | 2 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49666666984558105 | 0.0 | 0.0 | +— / -e85c6ab6-f36c-40b4-88e2-b7380b4c9652 |
| Jogador 8 | 4-4 | 223 | BUY | STABILIZE | 49.0 | 7 | 24 | 2 | 24.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8139922618865967 | 0.0 | 0.0 | +ddae48a6-5360-4660-9fa1-143ac35635ee / -— |
| Jogador 8 | 4-4 | 224 | SELL | STABILIZE | 49.0 | 7 | 21 | 2 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5686444640159607 | 0.0 | 0.0 | +— / -b2a77bec-e150-4d98-847c-9f2cfb50cbe7 |
| Jogador 8 | 4-4 | 225 | BUY | STABILIZE | 49.0 | 7 | 22 | 2 | 24.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04037512466311455 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 8 | 4-4 | 226 | SELL | STABILIZE | 49.0 | 7 | 20 | 2 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008933333680033684 | 0.0 | 0.0 | +— / -d175e09c-3ed6-4fb3-8c97-0c167862e29e |
| Jogador 8 | 4-4 | 227 | BUY | STABILIZE | 49.0 | 7 | 22 | 2 | 24.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.040364690124988556 | 0.0 | 0.0 | +42cf45df-f7dd-418d-a241-d89e69523352 / -— |
| Jogador 8 | 4-4 | 228 | REROLL | STABILIZE | 49.0 | 7 | 20 | 2 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2840000092983246 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 229 | SELL | STABILIZE | 49.0 | 7 | 18 | 1 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07106667011976242 | 0.0 | 0.0 | +— / -42cf45df-f7dd-418d-a241-d89e69523352 |
| Jogador 8 | 4-4 | 230 | BUY | STABILIZE | 49.0 | 7 | 20 | 2 | 24.0 | Espinhos Negros/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7363041639328003 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -— |
| Jogador 8 | 4-5 | 232 | SELL | STABILIZE | 49.0 | 7 | 23 | 2 | 24.0 | Espinhos Negros/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -849ea0fc-7f61-4907-8abb-b25c8cc82efc |
| Jogador 8 | 4-5 | 233 | BUY | STABILIZE | 49.0 | 7 | 26 | 2 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.863045334815979 | 0.0 | 0.0 | +cba152f4-af54-4d82-a35d-67aa165174be / -23366968-ed3f-43d0-9f24-bb7691bf5d45,ddae48a6-5360-4660-9fa1-143ac35635ee |
| Jogador 8 | 4-5 | 234 | BUY | STABILIZE | 49.0 | 7 | 23 | 2 | 24.0 | Espinhos Negros/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015930386260151863 | 0.0 | 0.0 | +98b72340-a402-45bc-9493-71263e3168d6 / -— |
| Jogador 8 | 4-5 | 235 | BUY | STABILIZE | 49.0 | 7 | 20 | 2 | 24.0 | Espinhos Negros/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09743041545152664 | 0.0 | 0.0 | +f3e882b5-333e-44e3-ae82-cacacc8b1137 / -— |
| Jogador 8 | 4-5 | 236 | SELL | STABILIZE | 49.0 | 7 | 18 | 1 | 24.0 | Espinhos Negros/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -cba152f4-af54-4d82-a35d-67aa165174be |
| Jogador 8 | 4-5 | 237 | BUY | STABILIZE | 49.0 | 7 | 26 | 2 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5154016613960266 | 0.0 | 0.0 | +20a4e507-09d3-42d7-b748-4dde14e82ddf / -— |
| Jogador 8 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 49.0 | 7 | 24 | 2 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019840560853481293 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 49.0 | 7 | 24 | 2 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014989971183240414 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 240 | MOVE_BOARD | STABILIZE | 49.0 | 7 | 24 | 2 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015001589432358742 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 242 | SELL | STABILIZE | 36.0 | 7 | 32 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00563333323225379 | 0.0 | 0.0 | +— / -98b72340-a402-45bc-9493-71263e3168d6 |
| Jogador 8 | 4-6 | 243 | BUY | STABILIZE | 36.0 | 7 | 35 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26036208868026733 | 0.0 | 0.0 | +6722b147-c2a7-4fd0-a943-5036adb3e3a1 / -— |
| Jogador 8 | 4-6 | 244 | SELL | STABILIZE | 36.0 | 7 | 32 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008348622359335423 | 0.0 | 0.0 | +— / -6722b147-c2a7-4fd0-a943-5036adb3e3a1 |
| Jogador 8 | 4-6 | 245 | BUY | STABILIZE | 36.0 | 7 | 35 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22226175665855408 | 0.0 | 0.0 | +1388df2e-8cb4-4e29-8b30-776c29406917 / -— |
| Jogador 8 | 4-6 | 246 | SELL | STABILIZE | 36.0 | 7 | 33 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008173353038728237 | 0.0 | 0.0 | +— / -1388df2e-8cb4-4e29-8b30-776c29406917 |
| Jogador 8 | 4-6 | 247 | BUY | STABILIZE | 36.0 | 7 | 35 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26532912254333496 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 8 | 4-6 | 248 | SELL | STABILIZE | 36.0 | 7 | 32 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -04520fe5-4449-4632-b275-e5e28d642007 |
| Jogador 8 | 4-6 | 249 | BUY | STABILIZE | 36.0 | 7 | 35 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26532334089279175 | 0.0 | 0.0 | +755060be-13bb-4686-9ee9-e53fef2d75b2 / -— |
| Jogador 8 | 4-6 | 250 | MOVE_BOARD | STABILIZE | 36.0 | 7 | 32 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.971777813509107e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 252 | SELL | ALL_IN | 23.0 | 7 | 41 | 4 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -755060be-13bb-4686-9ee9-e53fef2d75b2 |
| Jogador 8 | 4-7 | 253 | BUY | ALL_IN | 23.0 | 7 | 44 | 4 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8229107856750488 | 0.0 | 0.0 | +9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 / -20a4e507-09d3-42d7-b748-4dde14e82ddf,f3e882b5-333e-44e3-ae82-cacacc8b1137 |
| Jogador 8 | 4-7 | 254 | BUY | ALL_IN | 23.0 | 7 | 42 | 4 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11938665807247162 | 0.0 | 0.0 | +e5f38fbd-826a-4067-a33f-86cf7eb98f30 / -— |
| Jogador 8 | 4-7 | 255 | BUY | ALL_IN | 23.0 | 7 | 38 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15152767300605774 | 0.0 | 0.0 | +c7a7408a-e7bd-428d-9935-4d5a002d8d9f / -— |
| Jogador 8 | 4-7 | 256 | REROLL | ALL_IN | 23.0 | 7 | 35 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 257 | SELL | ALL_IN | 23.0 | 7 | 33 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6656000018119812 | 0.0 | 0.0 | +— / -9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 |
| Jogador 8 | 4-7 | 258 | BUY | ALL_IN | 23.0 | 7 | 38 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9363394975662231 | 0.0 | 0.0 | +f32e50e0-1430-4549-a1dd-a8473ffe0bd4 / -1fa69553-5270-4459-986b-600f748711b7,2c153083-6c43-425e-90d5-23f7f2058592 |
| Jogador 8 | 4-7 | 259 | BUY | ALL_IN | 23.0 | 7 | 35 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009191809222102165 | 0.0 | 0.0 | +eeb774dc-b3d1-4a90-8a93-b71a9b754169 / -— |
| Jogador 8 | 4-7 | 260 | BUY | ALL_IN | 23.0 | 7 | 32 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28749901056289673 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -— |
| Jogador 8 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 23.0 | 7 | 37 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11565002799034119 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 23.0 | 7 | 37 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10336042940616608 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 264 | SELL | ALL_IN | 23.0 | 7 | 37 | 3 | 24.0 | Espinhos Negros/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5795999765396118 | 0.0 | 0.0 | +— / -f32e50e0-1430-4549-a1dd-a8473ffe0bd4 |
| Jogador 8 | 5-1 | 265 | BUY | ALL_IN | 23.0 | 7 | 45 | 4 | 24.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.300059050321579 | 0.0 | 0.0 | +9f445115-49cc-4647-91a0-a80e347e9c62 / -— |
| Jogador 8 | 5-1 | 266 | SELL | ALL_IN | 23.0 | 7 | 42 | 4 | 24.0 | Espinhos Negros/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -eeb774dc-b3d1-4a90-8a93-b71a9b754169 |
| Jogador 8 | 5-1 | 267 | BUY | ALL_IN | 23.0 | 7 | 45 | 4 | 24.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3628910481929779 | 0.0 | 0.0 | +7a48aa2d-a43b-4e49-8230-77f4f2860cb2 / -— |
| Jogador 8 | 5-1 | 268 | SELL | ALL_IN | 23.0 | 7 | 42 | 4 | 24.0 | Espinhos Negros/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009911862201988697 | 0.0 | 0.0 | +— / -c7a7408a-e7bd-428d-9935-4d5a002d8d9f |
| Jogador 8 | 5-1 | 269 | BUY | ALL_IN | 23.0 | 7 | 45 | 4 | 24.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004471387714147568 | 0.0 | 0.0 | +b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 / -— |
| Jogador 8 | 5-1 | 270 | REROLL | ALL_IN | 23.0 | 7 | 43 | 4 | 24.0 | Espinhos Negros/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 272 | SELL | ALL_IN | 10.0 | 7 | 51 | 5 | 24.0 | Espinhos Negros/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 |
| Jogador 8 | 5-2 | 273 | BUY | ALL_IN | 10.0 | 7 | 53 | 5 | 24.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0672156810760498 | 0.0 | 0.0 | +438ec27b-d901-437b-82b5-64e6d46fccb1 / -35e1a0f6-207d-4df2-b096-fc07962d094a,a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 5-2 | 274 | BUY | ALL_IN | 10.0 | 7 | 51 | 5 | 20.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.066671371459961 | 0.0 | 0.0 | +987e61e4-0d34-49cf-b1ef-a95a7a5dfb21 / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,c737e99a-613e-4f1a-a50e-7a865169f90c |
| Jogador 8 | 5-2 | 275 | MOVE_BENCH | ALL_IN | 10.0 | 7 | 50 | 5 | 16.0 | Espinhos Negros/DA_Brambleback18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.22823485732078552 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 276 | MOVE_BENCH | ALL_IN | 10.0 | 7 | 50 | 5 | 22.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.3312946557998657 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 277 | EQUIP_FROM_INVENTORY | ALL_IN | 10.0 | 7 | 50 | 5 | 24.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06431352347135544 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 278 | MOVE_BOARD | ALL_IN | 10.0 | 7 | 50 | 5 | 24.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004342497792094946 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 279 | BUY | ALL_IN | 10.0 | 7 | 50 | 5 | 24.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2851695120334625 | 0.0 | 0.0 | +a5e92183-8d5d-434c-9294-47c6b7bfb91b / -— |
| Jogador 8 | 5-2 | 280 | MOVE_BENCH | ALL_IN | 10.0 | 7 | 47 | 4 | 24.0 | Espinhos Negros/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40284401178359985 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 186 | 163 | 100 | 7 | 4 | 0 | 1 | 0 | 114 | 26.0 |
- Jogador 1 — gasto por ação: BUY: 137g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 57g, stage 3: 53g, stage 4: 47g
| Jogador 2 | 303 | 365 | 242 | 11 | 18 | 2 | 3 | 0 | 164 | 28.0 |
- Jogador 2 — gasto por ação: BUY: 279g, BUY_XP: 80g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 6g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 67g, stage 3: 82g, stage 4: 76g, stage 5: 72g, stage 6: 61g
| Jogador 3 | 228 | 206 | 112 | 6 | 8 | 1 | 1 | 0 | 148 | 36.0 |
- Jogador 3 — gasto por ação: BUY: 164g, BUY_XP: 40g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 48g, stage 3: 64g, stage 4: 31g, stage 5: 48g, stage 6: 8g
| Jogador 4 | 197 | 203 | 107 | 9 | 9 | 1 | 2 | 0 | 63 | 32.0 |
- Jogador 4 — gasto por ação: BUY: 151g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 61g, stage 3: 53g, stage 4: 62g, stage 5: 21g
| Jogador 5 | 181 | 174 | 108 | 3 | 4 | 0 | 3 | 0 | 91 | 24.0 |
- Jogador 5 — gasto por ação: BUY: 144g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 6g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 59g, stage 3: 52g, stage 4: 56g
| Jogador 6 | 249 | 297 | 103 | 4 | 30 | 2 | 0 | 0 | 62 | 38.0 |
- Jogador 6 — gasto por ação: BUY: 165g, BUY_XP: 132g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 52g, stage 3: 57g, stage 4: 43g, stage 5: 79g, stage 6: 61g
| Jogador 7 | 279 | 271 | 138 | 9 | 17 | 0 | 0 | 0 | 129 | 56.0 |
- Jogador 7 — gasto por ação: BUY: 203g, BUY_XP: 68g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 58g, stage 3: 72g, stage 4: 42g, stage 5: 41g, stage 6: 52g
| Jogador 8 | 213 | 248 | 144 | 16 | 11 | 1 | 3 | 0 | 47 | 30.0 |
- Jogador 8 — gasto por ação: BUY: 186g, BUY_XP: 56g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 6g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 75g, stage 3: 75g, stage 4: 75g, stage 5: 16g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 6 | 4 |
- Jogador 1 · 3-1 · step 127: PASS com 5g, HP 100, nível 6/8 (STABILIZE).
- Jogador 1 · 4-3 · step 220: PASS com 78g, HP 21, nível 6/8 (ALL_IN).
- Jogador 1 · 4-5 · step 240: PASS com 103g, HP 8, nível 6/8 (ALL_IN).
- Jogador 1 · 4-6 · step 248: REROLL com 115g, HP 8, nível 6/8 (ALL_IN).
| Jogador 2 | 20 | 1 |
- Jogador 2 · 4-6 · step 248: PASS com 15g, HP 11, nível 7/8 (ALL_IN).
| Jogador 3 | 10 | 13 |
- Jogador 3 · 3-6 · step 180: PASS com 12g, HP 83, nível 6/8 (STABILIZE).
- Jogador 3 · 4-1 · step 198: PASS com 11g, HP 72, nível 7/8 (FAST8).
- Jogador 3 · 4-2 · step 206: PASS com 16g, HP 60, nível 7/8 (FAST8).
- Jogador 3 · 4-3 · step 217: PASS com 24g, HP 60, nível 7/8 (FAST8).
- Jogador 3 · 4-4 · step 224: PASS com 33g, HP 60, nível 7/8 (FAST8).
- Jogador 3 · 4-5 · step 239: PASS com 34g, HP 60, nível 7/8 (FAST8).
- Jogador 3 · 4-6 · step 245: PASS com 43g, HP 60, nível 7/8 (FAST8).
- Jogador 3 · 4-7 · step 260: PASS com 64g, HP 60, nível 7/8 (FAST8).
- Jogador 3 · 5-2 · step 280: PASS com 86g, HP 60, nível 7/8 (FAST8).
- Jogador 3 · 5-3 · step 289: PASS com 99g, HP 60, nível 7/8 (FAST8).
- Jogador 3 · 5-5 · step 305: PASS com 115g, HP 44, nível 7/8 (FAST8).
- Jogador 3 · 5-6 · step 318: PASS com 125g, HP 29, nível 7/8 (STABILIZE).
- Jogador 3 · 5-7 · step 329: REROLL com 141g, HP 12, nível 7/8 (ALL_IN).
| Jogador 4 | 12 | 4 |
- Jogador 4 · 4-1 · step 199: PASS com 9g, HP 65, nível 7/8 (STABILIZE).
- Jogador 4 · 4-3 · step 218: REROLL com 17g, HP 41, nível 7/8 (STABILIZE).
- Jogador 4 · 5-1 · step 270: PASS com 57g, HP 17, nível 7/8 (ALL_IN).
- Jogador 4 · 5-2 · step 278: REROLL com 66g, HP 1, nível 7/8 (ALL_IN).
| Jogador 5 | 6 | 7 |
- Jogador 5 · 3-2 · step 139: PASS com 11g, HP 76, nível 6/8 (STABILIZE).
- Jogador 5 · 3-3 · step 148: PASS com 9g, HP 76, nível 6/8 (STABILIZE).
- Jogador 5 · 4-2 · step 208: PASS com 63g, HP 43, nível 6/8 (STABILIZE).
- Jogador 5 · 4-3 · step 220: PASS com 69g, HP 31, nível 6/8 (STABILIZE).
- Jogador 5 · 4-4 · step 227: REROLL com 73g, HP 19, nível 6/8 (ALL_IN).
- Jogador 5 · 4-5 · step 237: REROLL com 84g, HP 19, nível 6/8 (ALL_IN).
- Jogador 5 · 4-6 · step 248: REROLL com 92g, HP 7, nível 6/8 (ALL_IN).
| Jogador 6 | 33 | 7 |
- Jogador 6 · 3-6 · step 175: PASS com 4g, HP 67, nível 7/8 (FAST8).
- Jogador 6 · 4-1 · step 197: PASS com 5g, HP 67, nível 7/8 (FAST8).
- Jogador 6 · 4-2 · step 206: PASS com 5g, HP 67, nível 7/8 (FAST8).
- Jogador 6 · 4-3 · step 216: PASS com 11g, HP 67, nível 7/8 (FAST8).
- Jogador 6 · 4-5 · step 238: PASS com 20g, HP 67, nível 7/8 (FAST8).
- Jogador 6 · 4-6 · step 246: PASS com 32g, HP 67, nível 7/8 (FAST8).
- Jogador 6 · 5-2 · step 277: PASS com 66g, HP 51, nível 7/8 (FAST8).
| Jogador 7 | 17 | 6 |
- Jogador 7 · 4-4 · step 229: PASS com 6g, HP 68, nível 7/8 (STABILIZE).
- Jogador 7 · 4-5 · step 236: PASS com 11g, HP 68, nível 7/8 (STABILIZE).
- Jogador 7 · 5-2 · step 277: PASS com 32g, HP 68, nível 7/8 (FAST8).
- Jogador 7 · 5-3 · step 285: PASS com 40g, HP 55, nível 7/8 (FAST8).
- Jogador 7 · 5-5 · step 306: PASS com 57g, HP 55, nível 7/8 (FAST8).
- Jogador 7 · 5-6 · step 318: PASS com 68g, HP 40, nível 7/8 (FAST8).
| Jogador 8 | 14 | 5 |
- Jogador 8 · 4-2 · step 210: PASS com 8g, HP 60, nível 7/8 (STABILIZE).
- Jogador 8 · 4-3 · step 218: PASS com 16g, HP 60, nível 7/8 (STABILIZE).
- Jogador 8 · 4-4 · step 228: REROLL com 20g, HP 49, nível 7/8 (STABILIZE).
- Jogador 8 · 4-7 · step 256: REROLL com 35g, HP 23, nível 7/8 (ALL_IN).
- Jogador 8 · 5-1 · step 270: REROLL com 43g, HP 23, nível 7/8 (ALL_IN).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

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
| Jogador 8 | 2 | 2 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 186 | 34 | 28 | 124 | 0.0063 | 0.3492 | 0.0037 | 0.2729 | 0.0026 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0129 (66 ações), BUY_XP: Δ 0.0162 (6 ações), CRAFT_AND_EQUIP: Δ 0.0028 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0060 (5 ações), MOVE_BENCH: Δ 0.0027 (16 ações), MOVE_BOARD: Δ 0.0428 (33 ações), PASS: Δ 0.0000 (12 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0102 (42 ações)
| Jogador 2 | 303 | 41 | 38 | 224 | 0.0005 | 0.5290 | -0.0004 | 0.3582 | 0.0009 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0116 (115 ações), BUY_XP: Δ 0.0049 (20 ações), CRAFT_AND_EQUIP: Δ 0.0009 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0310 (14 ações), MOVE_BOARD: Δ 0.0055 (37 ações), PASS: Δ 0.0035 (17 ações), REROLL: Δ 0.0000 (3 ações), SELL: Δ 0.0078 (87 ações)
| Jogador 3 | 228 | 50 | 46 | 132 | 0.0053 | 0.4121 | 0.0035 | 0.2786 | 0.0018 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0241 (72 ações), BUY_XP: Δ 0.0031 (10 ações), CRAFT_AND_EQUIP: Δ 0.0114 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0169 (19 ações), MOVE_BOARD: Δ 0.0236 (55 ações), PASS: Δ 0.0000 (26 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0324 (37 ações)
| Jogador 4 | 197 | 39 | 34 | 124 | 0.0043 | 0.0018 | 0.0031 | 0.3446 | 0.0012 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0114 (67 ações), BUY_XP: Δ 0.0130 (12 ações), CRAFT_AND_EQUIP: Δ 0.0020 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0336 (6 ações), MOVE_BENCH: Δ -0.0262 (11 ações), MOVE_BOARD: Δ 0.0125 (41 ações), PASS: Δ 0.0000 (15 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0283 (36 ações)
| Jogador 5 | 181 | 28 | 25 | 128 | 0.0021 | -0.0919 | 0.0001 | 0.3322 | 0.0020 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0107 (76 ações), BUY_XP: Δ 0.0162 (6 ações), CRAFT_AND_EQUIP: Δ 0.1133 (5 ações), MOVE_BENCH: Δ -0.0324 (22 ações), MOVE_BOARD: Δ 0.1181 (6 ações), PASS: Δ 0.0000 (11 ações), REROLL: Δ 0.0000 (3 ações), SELL: Δ 0.0103 (52 ações)
| Jogador 6 | 249 | 46 | 41 | 162 | 0.0015 | -0.5447 | 0.0004 | 0.4324 | 0.0011 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0212 (67 ações), BUY_XP: Δ 0.0018 (33 ações), CRAFT_AND_EQUIP: Δ 0.0427 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (12 ações), MOVE_BENCH: Δ 0.1602 (16 ações), MOVE_BOARD: Δ -0.0278 (61 ações), PASS: Δ 0.0000 (20 ações), SELL: Δ 0.0171 (33 ações)
| Jogador 7 | 279 | 62 | 49 | 168 | 0.0050 | 0.1372 | 0.0034 | 0.3448 | 0.0016 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0311 (85 ações), BUY_XP: Δ 0.0000 (17 ações), CRAFT_AND_EQUIP: Δ 0.0086 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0216 (10 ações), MOVE_BENCH: Δ 0.0128 (18 ações), MOVE_BOARD: Δ 0.0346 (73 ações), PASS: Δ 0.0000 (22 ações), SELL: Δ 0.0213 (47 ações)
| Jogador 8 | 213 | 32 | 26 | 155 | 0.0042 | 0.1335 | 0.0022 | 0.3165 | 0.0020 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0100 (85 ações), BUY_XP: Δ 0.0104 (14 ações), CRAFT_AND_EQUIP: Δ 0.0030 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0423 (12 ações), MOVE_BOARD: Δ 0.0340 (23 ações), PASS: Δ 0.0000 (10 ações), REROLL: Δ 0.0000 (3 ações), SELL: Δ 0.0051 (58 ações)
- Jogador 1 — rounds avaliados: 24; correlação estrutural/combate: -0.394; posicional/combate: -0.287.
- Jogador 1 — combate positive: score estrutural prévio 0.167
  score posicional prévio 0.249
- Jogador 1 — combate negative: score estrutural prévio 0.530
  score posicional prévio 0.315
- Jogador 2 — rounds avaliados: 38; correlação estrutural/combate: -0.094; posicional/combate: 0.287.
- Jogador 2 — combate positive: score estrutural prévio 0.572
  score posicional prévio 0.385
- Jogador 2 — combate negative: score estrutural prévio 0.699
  score posicional prévio 0.312
- Jogador 3 — rounds avaliados: 33; correlação estrutural/combate: -0.250; posicional/combate: -0.153.
- Jogador 3 — combate positive: score estrutural prévio 0.387
  score posicional prévio 0.269
- Jogador 3 — combate negative: score estrutural prévio 0.501
  score posicional prévio 0.311
- Jogador 4 — rounds avaliados: 27; correlação estrutural/combate: 0.248; posicional/combate: 0.014.
- Jogador 4 — combate positive: score estrutural prévio 0.095
  score posicional prévio 0.378
- Jogador 4 — combate negative: score estrutural prévio -0.131
  score posicional prévio 0.359
- Jogador 5 — rounds avaliados: 24; correlação estrutural/combate: -0.363; posicional/combate: -0.425.
- Jogador 5 — combate positive: score estrutural prévio -0.207
  score posicional prévio 0.313
- Jogador 5 — combate negative: score estrutural prévio 0.004
  score posicional prévio 0.348
- Jogador 6 — rounds avaliados: 35; correlação estrutural/combate: 0.174; posicional/combate: -0.123.
- Jogador 6 — combate positive: score estrutural prévio -0.441
  score posicional prévio 0.419
- Jogador 6 — combate negative: score estrutural prévio -0.667
  score posicional prévio 0.463
- Jogador 7 — rounds avaliados: 38; correlação estrutural/combate: -0.237; posicional/combate: -0.225.
- Jogador 7 — combate positive: score estrutural prévio 0.049
  score posicional prévio 0.316
- Jogador 7 — combate negative: score estrutural prévio 0.290
  score posicional prévio 0.393
- Jogador 8 — rounds avaliados: 27; correlação estrutural/combate: 0.117; posicional/combate: -0.325.
- Jogador 8 — combate positive: score estrutural prévio 0.396
  score posicional prévio 0.288
- Jogador 8 — combate negative: score estrutural prévio 0.163
  score posicional prévio 0.335

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 209 | OK (209) | 2 | 3 | 0 | 1 | 5 | 2 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_GuinsoosRageblade, TFT_Item_InfinityEdge, TFT_Item_MadredsBloodrazor, TFT_Item_Morellonomicon; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 341 | OK (341) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_Crownguard, TFT_Item_GargoyleStoneplate, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_RunaansHurricane; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 260 | OK (260) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_GuinsoosRageblade, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_RedBuff, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 223 | OK (223) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_BlueBuff, TFT_Item_JeweledGauntlet, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 204 | OK (204) | 5 | 0 | 0 | 1 | 5 | 0 |
- Jogador 5 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_IonicSpark, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_PowerGauntlet; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 283 | OK (283) | 5 | 3 | 0 | 0 | 8 | 3 |
- Jogador 6 — IDs equipados observados: DA_18_EmblemSpellweaver, TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_InfinityEdge, TFT_Item_Morellonomicon, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 316 | OK (316) | 8 | 0 | 0 | 0 | 8 | 3 |
- Jogador 7 — IDs equipados observados: TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_RunaansHurricane, TFT_Item_StatikkShiv; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 239 | OK (239) | 3 | 4 | 0 | 0 | 7 | 1 |
- Jogador 8 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_DragonsClaw, TFT_Item_InfinityEdge, TFT_Item_LastWhisper, TFT_Item_Morellonomicon, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.110 | 0.000 |
| Jogador 1 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.001 | 0.000 |
| Jogador 1 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 1 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.012 | 0.000 |
| Jogador 1 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 6 | 5 | 4 → 4 | -0.012 | 0.366 |
| Jogador 1 | 2-2 | 10 | 2.000 | 0.000 | 0 → 0 | 3 → 3 | 14% → 18% | 6 → 8 | 9 | 4 → 5 | -0.027 | 0.246 |
| Jogador 1 | 2-3 | 8 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 18% → 18% | 8 → 7 | 11 | 5 → 5 | 0.000 | 0.308 |
| Jogador 1 | 2-4 | 10 | 2.000 | -4.000 | 0 → 0 | 3 → 3 | 18% → 21% | 7 → 6 | 14 | 5 → 6 | 0.002 | 0.000 |
| Jogador 1 | 2-5 | 8 | 2.000 | 8.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 8 | 5 | 6 → 6 | 0.062 | 0.351 |
| Jogador 1 | 2-6 | 10 | 2.000 | 12.000 | 0 → 0 | 3 → 2 | 21% → 21% | 8 → 8 | 8 | 6 → 6 | -0.037 | 0.275 |
| Jogador 1 | 2-7 | 8 | 2.000 | 6.000 | 0 → 1 | 2 → 1 | 21% → 21% | 8 → 10 | 5 | 6 → 6 | -0.001 | 0.000 |
| Jogador 1 | 3-1 | 7 | 0.000 | 10.000 | 1 → 1 | 1 → 1 | 21% → 21% | 10 → 10 | 5 | 6 → 6 | -0.004 | -0.416 |
| Jogador 1 | 3-2 | 10 | 0.000 | 6.000 | 1 → 1 | 1 → 2 | 21% → 21% | 10 → 14 | 9 | 6 → 6 | 0.008 | -0.273 |
| Jogador 1 | 3-3 | 10 | 4.000 | 0.000 | 1 → 1 | 2 → 3 | 21% → 21% | 14 → 19 | 8 | 6 → 6 | 0.028 | -0.278 |
| Jogador 1 | 3-4 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 19 → 28 | 5 | 6 → 6 | 0.009 | 0.000 |
| Jogador 1 | 3-5 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 4 | 21% → 21% | 28 → 37 | 7 | 6 → 6 | 0.001 | -0.268 |
| Jogador 1 | 3-6 | 10 | -2.000 | 4.000 | 1 → 1 | 4 → 4 | 21% → 21% | 37 → 45 | 9 | 6 → 6 | 0.054 | -0.258 |
| Jogador 1 | 3-7 | 10 | 4.000 | 0.000 | 1 → 1 | 4 → 4 | 21% → 21% | 45 → 52 | 10 | 6 → 6 | -0.004 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 5 | 21% → 21% | 52 → 65 | 9 | 6 → 6 | 0.006 | -0.291 |
| Jogador 1 | 4-2 | 10 | 0.000 | -12.000 | 1 → 1 | 5 → 5 | 21% → 21% | 65 → 84 | 6 | 6 → 6 | -0.001 | -0.271 |
| Jogador 1 | 4-3 | 10 | 4.000 | 6.000 | 1 → 1 | 5 → 5 | 21% → 21% | 84 → 91 | 7 | 6 → 6 | -0.008 | -0.285 |
| Jogador 1 | 4-4 | 10 | 0.000 | 0.000 | 1 → 1 | 5 → 6 | 21% → 21% | 91 → 105 | 5 | 6 → 6 | 0.006 | 0.000 |
| Jogador 1 | 4-5 | 10 | 0.000 | 4.000 | 1 → 1 | 6 → 6 | 21% → 21% | 105 → 114 | 10 | 6 → 6 | 0.006 | 0.288 |
| Jogador 1 | 4-6 | 10 | -28.000 | -46.000 | 1 → 0 | 6 → 0 | 21% → 0% | 114 → 114 | 10 | 6 → 6 | -0.124 | -0.295 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 24, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 12; mudanças de composição: 0; posicionamento melhorou em 36 ações e piorou em 30.
- Jogador 1 — estado final: ouro 114, nível 6, vida 8.0, colocação 8.
| Jogador 2 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.161 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.109 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 3 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 12 | 2.000 | 4.000 | 1 → 1 | 1 → 2 | 11% → 14% | 4 → 6 | 5 | 4 → 4 | 0.022 | -0.188 |
| Jogador 2 | 2-2 | 5 | 0.000 | 6.000 | 1 → 1 | 2 → 1 | 14% → 14% | 6 → 8 | 4 | 4 → 4 | -0.012 | -0.464 |
| Jogador 2 | 2-3 | 7 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 7 | 10 | 4 → 5 | 0.016 | -0.332 |
| Jogador 2 | 2-4 | 10 | 6.000 | 6.000 | 1 → 1 | 1 → 2 | 14% → 18% | 7 → 7 | 8 | 5 → 5 | 0.020 | 0.000 |
| Jogador 2 | 2-5 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 18% | 7 → 9 | 13 | 5 → 5 | 0.018 | -0.232 |
| Jogador 2 | 2-6 | 10 | 0.000 | -12.000 | 1 → 1 | 2 → 2 | 18% → 18% | 9 → 10 | 17 | 5 → 6 | 0.005 | -0.232 |
| Jogador 2 | 2-7 | 9 | 8.000 | 4.000 | 1 → 1 | 2 → 2 | 18% → 21% | 10 → 7 | 10 | 6 → 6 | -0.015 | 0.000 |
| Jogador 2 | 3-1 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 7 → 8 | 10 | 6 → 6 | 0.013 | -0.263 |
| Jogador 2 | 3-2 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 1 | 21% → 21% | 8 → 8 | 11 | 6 → 6 | 0.000 | 0.276 |
| Jogador 2 | 3-3 | 10 | 0.000 | 12.000 | 1 → 1 | 1 → 2 | 21% → 21% | 8 → 7 | 14 | 6 → 6 | 0.000 | -0.273 |
| Jogador 2 | 3-4 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 7 → 8 | 12 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 3-5 | 10 | 0.000 | -4.000 | 1 → 1 | 2 → 3 | 21% → 21% | 8 → 8 | 14 | 6 → 7 | 0.005 | -0.273 |
| Jogador 2 | 3-6 | 8 | 6.000 | 10.000 | 1 → 1 | 3 → 3 | 21% → 25% | 8 → 6 | 8 | 7 → 7 | 0.008 | -0.329 |
| Jogador 2 | 3-7 | 10 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 25% → 25% | 6 → 6 | 13 | 7 → 7 | 0.003 | 0.000 |
| Jogador 2 | 4-1 | 10 | 6.000 | -12.000 | 1 → 1 | 3 → 3 | 25% → 25% | 6 → 9 | 14 | 7 → 7 | 0.009 | 0.288 |
| Jogador 2 | 4-2 | 10 | -2.000 | -4.000 | 1 → 1 | 3 → 2 | 25% → 21% | 9 → 7 | 15 | 7 → 7 | 0.001 | 0.283 |
| Jogador 2 | 4-3 | 10 | 0.000 | -16.000 | 1 → 1 | 2 → 2 | 21% → 21% | 7 → 8 | 16 | 7 → 7 | 0.000 | -0.268 |
| Jogador 2 | 4-4 | 10 | 0.000 | -12.000 | 1 → 1 | 2 → 1 | 21% → 21% | 8 → 19 | 8 | 7 → 7 | -0.036 | 0.000 |
| Jogador 2 | 4-5 | 10 | 6.000 | -2.000 | 1 → 1 | 1 → 1 | 21% → 25% | 19 → 20 | 12 | 7 → 7 | 0.025 | -0.271 |
| Jogador 2 | 4-6 | 8 | 0.000 | 10.000 | 1 → 1 | 1 → 1 | 25% → 25% | 20 → 22 | 5 | 7 → 7 | 0.023 | 0.364 |
| Jogador 2 | 4-7 | 10 | 0.000 | 10.000 | 1 → 1 | 1 → 1 | 25% → 25% | 22 → 23 | 6 | 7 → 8 | -0.029 | 0.000 |
| Jogador 2 | 5-1 | 10 | 0.000 | 6.000 | 1 → 1 | 1 → 2 | 25% → 25% | 23 → 29 | 10 | 8 → 8 | 0.000 | 0.292 |
| Jogador 2 | 5-2 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 25% → 25% | 29 → 35 | 16 | 8 → 8 | 0.000 | 0.307 |
| Jogador 2 | 5-3 | 10 | 0.000 | -4.000 | 1 → 1 | 2 → 2 | 25% → 25% | 35 → 47 | 14 | 8 → 8 | 0.000 | 0.302 |
| Jogador 2 | 5-4 | 9 | 2.000 | -6.000 | 1 → 1 | 2 → 3 | 25% → 29% | 47 → 59 | 10 | 8 → 8 | 0.004 | 0.000 |
| Jogador 2 | 5-5 | 7 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 29% → 29% | 59 → 69 | 7 | 8 → 8 | -0.031 | 0.444 |
| Jogador 2 | 5-6 | 8 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 29% → 29% | 69 → 80 | 7 | 8 → 8 | -0.025 | 0.367 |
| Jogador 2 | 5-7 | 8 | 0.000 | -4.000 | 1 → 1 | 4 → 4 | 29% → 29% | 80 → 95 | 8 | 8 → 8 | 0.009 | 0.000 |
| Jogador 2 | 6-1 | 8 | 0.000 | 4.000 | 1 → 1 | 4 → 3 | 29% → 29% | 95 → 107 | 4 | 8 → 8 | 0.082 | 0.375 |
| Jogador 2 | 6-2 | 9 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 29% → 29% | 107 → 118 | 6 | 8 → 8 | -0.110 | 0.337 |
| Jogador 2 | 6-3 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 29% → 29% | 118 → 130 | 15 | 8 → 8 | 0.000 | 0.315 |
| Jogador 2 | 6-4 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 29% → 29% | 130 → 141 | 13 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-5 | 10 | 0.000 | -10.000 | 1 → 1 | 4 → 3 | 29% → 29% | 141 → 160 | 10 | 8 → 8 | 0.000 | 0.309 |
| Jogador 2 | 6-6 | 10 | -14.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 25% | 160 → 165 | 13 | 8 → 8 | -0.018 | 0.297 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 53, COMPOSITION_COMPATIBILITY: 41, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 14; mudanças de composição: 0; posicionamento melhorou em 45 ações e piorou em 38.
- Jogador 2 — estado final: ouro 165, nível 8, vida 11.0, colocação 1.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.060 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 3 | 1-4 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.002 | 0.000 |
| Jogador 3 | 2-1 | 8 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.009 | 0.320 |
| Jogador 3 | 2-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.653 |
| Jogador 3 | 2-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 8 | 7 | 4 → 5 | 0.006 | 0.502 |
| Jogador 3 | 2-4 | 9 | 6.000 | 2.000 | 1 → 1 | 1 → 2 | 14% → 18% | 8 → 6 | 8 | 5 → 5 | 0.024 | 0.000 |
| Jogador 3 | 2-5 | 7 | 4.000 | -4.000 | 1 → 1 | 2 → 3 | 18% → 18% | 6 → 7 | 5 | 5 → 5 | 0.010 | -0.347 |
| Jogador 3 | 2-6 | 10 | 6.000 | -6.000 | 1 → 3 | 3 → 1 | 18% → 18% | 7 → 6 | 7 | 5 → 5 | 0.006 | 0.246 |
| Jogador 3 | 2-7 | 10 | 0.000 | 4.000 | 3 → 3 | 1 → 2 | 18% → 18% | 6 → 5 | 12 | 5 → 6 | 0.006 | 0.000 |
| Jogador 3 | 3-1 | 7 | 6.000 | 4.000 | 3 → 3 | 2 → 3 | 18% → 21% | 5 → 7 | 5 | 6 → 6 | -0.006 | 0.426 |
| Jogador 3 | 3-2 | 8 | 0.000 | 8.000 | 3 → 3 | 3 → 2 | 21% → 21% | 7 → 9 | 5 | 6 → 6 | -0.015 | 0.363 |
| Jogador 3 | 3-3 | 10 | 0.000 | 6.000 | 3 → 3 | 2 → 2 | 21% → 21% | 9 → 10 | 13 | 6 → 6 | 0.011 | 0.290 |
| Jogador 3 | 3-4 | 10 | 0.000 | 4.000 | 3 → 3 | 2 → 3 | 21% → 21% | 10 → 6 | 14 | 6 → 6 | 0.006 | 0.000 |
| Jogador 3 | 3-5 | 7 | 0.000 | 2.000 | 3 → 3 | 3 → 2 | 21% → 21% | 6 → 7 | 6 | 6 → 6 | -0.009 | -0.382 |
| Jogador 3 | 3-6 | 10 | 0.000 | -6.000 | 3 → 3 | 2 → 4 | 21% → 21% | 7 → 19 | 6 | 6 → 6 | -0.002 | -0.283 |
| Jogador 3 | 3-7 | 10 | 4.000 | 4.000 | 3 → 3 | 4 → 4 | 21% → 25% | 19 → 13 | 15 | 6 → 7 | -0.011 | 0.000 |
| Jogador 3 | 4-1 | 8 | 0.000 | 4.000 | 3 → 3 | 4 → 5 | 25% → 25% | 13 → 18 | 3 | 7 → 7 | 0.008 | -0.339 |
| Jogador 3 | 4-2 | 6 | 0.000 | 4.000 | 3 → 3 | 5 → 5 | 25% → 25% | 18 → 23 | 4 | 7 → 7 | 0.000 | 0.481 |
| Jogador 3 | 4-3 | 7 | 0.000 | -2.000 | 3 → 3 | 5 → 5 | 25% → 25% | 23 → 33 | 3 | 7 → 7 | 0.011 | 0.405 |
| Jogador 3 | 4-4 | 4 | 0.000 | 0.000 | 3 → 3 | 5 → 5 | 25% → 25% | 33 → 42 | 0 | 7 → 7 | -0.007 | 0.000 |
| Jogador 3 | 4-5 | 9 | 0.000 | 4.000 | 3 → 3 | 5 → 3 | 25% → 25% | 42 → 44 | 11 | 7 → 7 | 0.000 | 0.315 |
| Jogador 3 | 4-6 | 5 | 0.000 | 2.000 | 3 → 3 | 3 → 3 | 25% → 25% | 44 → 54 | 1 | 7 → 7 | -0.011 | 0.592 |
| Jogador 3 | 4-7 | 10 | 0.000 | -12.000 | 3 → 3 | 3 → 5 | 25% → 25% | 54 → 75 | 9 | 7 → 7 | 0.018 | 0.000 |
| Jogador 3 | 5-1 | 10 | 0.000 | -4.000 | 3 → 3 | 5 → 5 | 25% → 25% | 75 → 89 | 5 | 7 → 7 | -0.017 | 0.292 |
| Jogador 3 | 5-2 | 10 | 0.000 | 6.000 | 3 → 3 | 5 → 5 | 25% → 25% | 89 → 100 | 6 | 7 → 7 | 0.012 | 0.297 |
| Jogador 3 | 5-3 | 9 | 0.000 | 2.000 | 3 → 3 | 5 → 4 | 25% → 25% | 100 → 109 | 6 | 7 → 7 | -0.000 | -0.317 |
| Jogador 3 | 5-4 | 9 | 2.000 | -12.000 | 3 → 3 | 4 → 3 | 25% → 25% | 109 → 123 | 7 | 7 → 7 | -0.005 | 0.000 |
| Jogador 3 | 5-5 | 6 | 0.000 | 16.000 | 3 → 3 | 3 → 3 | 25% → 25% | 123 → 126 | 8 | 7 → 7 | -0.010 | -0.467 |
| Jogador 3 | 5-6 | 8 | 0.000 | 2.000 | 3 → 3 | 3 → 3 | 25% → 25% | 126 → 136 | 7 | 7 → 7 | 0.008 | -0.344 |
| Jogador 3 | 5-7 | 10 | -6.000 | -16.000 | 3 → 3 | 3 → 3 | 25% → 21% | 136 → 155 | 9 | 7 → 7 | 0.016 | 0.000 |
| Jogador 3 | 6-1 | 10 | -34.000 | -38.000 | 3 → 0 | 3 → 0 | 21% → 0% | 155 → 148 | 8 | 7 → 7 | -0.092 | -0.290 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 22, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 17; mudanças de composição: 0; posicionamento melhorou em 53 ações e piorou em 47.
- Jogador 3 — estado final: ouro 148, nível 7, vida 12.0, colocação 4.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 4 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.065 | 0.000 |
| Jogador 4 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 4 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.013 | 0.000 |
| Jogador 4 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 5 | 5 | 4 → 4 | -0.018 | -0.346 |
| Jogador 4 | 2-2 | 4 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 14% → 18% | 5 → 6 | 5 | 4 → 5 | 0.034 | 0.684 |
| Jogador 4 | 2-3 | 10 | 4.000 | -4.000 | 0 → 0 | 3 → 2 | 18% → 18% | 6 → 9 | 9 | 5 → 5 | 0.005 | 0.246 |
| Jogador 4 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 10 | 12 | 5 → 5 | -0.013 | 0.000 |
| Jogador 4 | 2-5 | 10 | 6.000 | -2.000 | 0 → 0 | 3 → 2 | 18% → 21% | 10 → 7 | 14 | 5 → 6 | -0.003 | 0.269 |
| Jogador 4 | 2-6 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 21% → 21% | 7 → 6 | 6 | 6 → 6 | -0.076 | -0.431 |
| Jogador 4 | 2-7 | 10 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 6 → 6 | 10 | 6 → 6 | 0.091 | 0.000 |
| Jogador 4 | 3-1 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 3 | 21% → 21% | 6 → 7 | 12 | 6 → 6 | -0.008 | -0.281 |
| Jogador 4 | 3-2 | 10 | 2.000 | -4.000 | 0 → 0 | 3 → 2 | 21% → 21% | 7 → 10 | 6 | 6 → 6 | -0.028 | -0.278 |
| Jogador 4 | 3-3 | 8 | 6.000 | -6.000 | 0 → 1 | 2 → 1 | 21% → 25% | 10 → 6 | 10 | 6 → 7 | 0.041 | 0.363 |
| Jogador 4 | 3-4 | 7 | 0.000 | 12.000 | 1 → 1 | 1 → 1 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | -0.004 | 0.000 |
| Jogador 4 | 3-5 | 6 | 0.000 | 6.000 | 1 → 1 | 1 → 2 | 25% → 25% | 5 → 9 | 3 | 7 → 7 | 0.009 | 0.475 |
| Jogador 4 | 3-6 | 8 | 0.000 | 16.000 | 1 → 1 | 2 → 2 | 25% → 25% | 9 → 8 | 8 | 7 → 7 | 0.015 | 0.345 |
| Jogador 4 | 3-7 | 7 | 0.000 | 10.000 | 1 → 1 | 2 → 2 | 25% → 25% | 8 → 6 | 8 | 7 → 7 | -0.031 | 0.000 |
| Jogador 4 | 4-1 | 9 | 0.000 | -2.000 | 1 → 1 | 2 → 3 | 25% → 25% | 6 → 14 | 5 | 7 → 7 | -0.127 | -0.302 |
| Jogador 4 | 4-2 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 4 | 25% → 25% | 14 → 21 | 9 | 7 → 7 | -0.004 | -0.271 |
| Jogador 4 | 4-3 | 10 | 0.000 | 4.000 | 1 → 1 | 4 → 3 | 25% → 25% | 21 → 23 | 16 | 7 → 7 | 0.000 | 0.301 |
| Jogador 4 | 4-4 | 10 | 0.000 | -8.000 | 1 → 1 | 3 → 3 | 25% → 25% | 23 → 34 | 10 | 7 → 7 | 0.035 | 0.000 |
| Jogador 4 | 4-5 | 10 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 25% → 25% | 34 → 39 | 7 | 7 → 7 | -0.010 | -0.266 |
| Jogador 4 | 4-6 | 10 | 2.000 | 0.000 | 1 → 1 | 3 → 2 | 25% → 25% | 39 → 44 | 7 | 7 → 7 | 0.029 | -0.286 |
| Jogador 4 | 4-7 | 10 | 0.000 | -4.000 | 1 → 1 | 2 → 2 | 25% → 25% | 44 → 58 | 8 | 7 → 7 | 0.086 | 0.000 |
| Jogador 4 | 5-1 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 25% → 25% | 58 → 68 | 6 | 7 → 7 | 0.004 | -0.275 |
| Jogador 4 | 5-2 | 10 | -32.000 | -42.000 | 1 → 0 | 3 → 0 | 25% → 0% | 68 → 63 | 15 | 7 → 7 | -0.097 | -0.280 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 24, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 12; mudanças de composição: 0; posicionamento melhorou em 43 ações e piorou em 36.
- Jogador 4 — estado final: ouro 63, nível 7, vida 1.0, colocação 6.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.112 | 0.000 |
| Jogador 5 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.003 | 0.000 |
| Jogador 5 | 2-1 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.000 | 0.340 |
| Jogador 5 | 2-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.641 |
| Jogador 5 | 2-3 | 10 | 6.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 5 | 11 | 4 → 5 | -0.007 | -0.237 |
| Jogador 5 | 2-4 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 5 → 6 | 11 | 5 → 5 | 0.000 | 0.000 |
| Jogador 5 | 2-5 | 10 | 2.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 6 → 6 | 13 | 5 → 6 | -0.006 | 0.246 |
| Jogador 5 | 2-6 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 9 | 7 | 6 → 6 | 0.019 | -0.269 |
| Jogador 5 | 2-7 | 10 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 9 → 11 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-1 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 1 | 21% → 21% | 11 → 15 | 10 | 6 → 6 | 0.001 | -0.286 |
| Jogador 5 | 3-2 | 9 | 4.000 | 4.000 | 0 → 0 | 1 → 2 | 21% → 21% | 15 → 18 | 7 | 6 → 6 | -0.053 | 0.328 |
| Jogador 5 | 3-3 | 8 | 0.000 | 18.000 | 0 → 0 | 2 → 3 | 21% → 21% | 18 → 14 | 9 | 6 → 6 | 0.000 | -0.341 |
| Jogador 5 | 3-4 | 10 | -4.000 | -12.000 | 0 → 0 | 3 → 3 | 21% → 21% | 14 → 29 | 4 | 6 → 6 | 0.019 | 0.000 |
| Jogador 5 | 3-5 | 10 | 4.000 | -2.000 | 0 → 0 | 3 → 2 | 21% → 21% | 29 → 36 | 8 | 6 → 6 | -0.019 | -0.288 |
| Jogador 5 | 3-6 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 36 → 49 | 6 | 6 → 6 | 0.000 | 0.276 |
| Jogador 5 | 3-7 | 10 | 0.000 | -12.000 | 0 → 0 | 2 → 1 | 21% → 21% | 49 → 65 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 10 | 4.000 | 0.000 | 0 → 0 | 1 → 0 | 21% → 21% | 65 → 72 | 9 | 6 → 6 | 0.078 | -0.268 |
| Jogador 5 | 4-2 | 8 | -2.000 | 20.000 | 0 → 0 | 0 → 1 | 21% → 21% | 72 → 74 | 9 | 6 → 6 | -0.005 | -0.333 |
| Jogador 5 | 4-3 | 10 | 0.000 | 10.000 | 0 → 0 | 1 → 1 | 21% → 21% | 74 → 80 | 7 | 6 → 6 | 0.000 | -0.266 |
| Jogador 5 | 4-4 | 10 | -2.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 80 → 88 | 10 | 6 → 6 | -0.019 | 0.000 |
| Jogador 5 | 4-5 | 10 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 88 → 94 | 10 | 6 → 6 | 0.000 | -0.286 |
| Jogador 5 | 4-6 | 10 | -20.000 | -46.000 | 0 → 0 | 2 → 0 | 21% → 0% | 94 → 91 | 11 | 6 → 6 | -0.043 | -0.280 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 29, COMPOSITION_COMPATIBILITY: 29, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 13; mudanças de composição: 1; posicionamento melhorou em 30 ações e piorou em 27.
- Jogador 5 — estado final: ouro 91, nível 6, vida 7.0, colocação 7.
| Jogador 6 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.163 | 0.000 |
| Jogador 6 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.039 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.018 | -0.346 |
| Jogador 6 | 2-2 | 7 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 8 | 6 | 4 → 4 | 0.000 | -0.369 |
| Jogador 6 | 2-3 | 5 | 6.000 | 0.000 | 0 → 0 | 2 → 2 | 14% → 18% | 8 → 7 | 7 | 4 → 5 | -0.010 | -0.462 |
| Jogador 6 | 2-4 | 10 | 0.000 | -4.000 | 0 → 0 | 2 → 2 | 18% → 18% | 7 → 7 | 11 | 5 → 5 | -0.001 | 0.000 |
| Jogador 6 | 2-5 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 7 → 8 | 10 | 5 → 6 | 0.004 | -0.264 |
| Jogador 6 | 2-6 | 9 | 4.000 | 2.000 | 0 → 0 | 3 → 2 | 18% → 21% | 8 → 9 | 5 | 6 → 6 | 0.014 | 0.279 |
| Jogador 6 | 2-7 | 8 | 0.000 | 8.000 | 0 → 0 | 2 → 3 | 21% → 21% | 9 → 6 | 8 | 6 → 6 | -0.043 | 0.000 |
| Jogador 6 | 3-1 | 10 | 4.000 | -6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 7 | 13 | 6 → 6 | 0.148 | 0.281 |
| Jogador 6 | 3-2 | 10 | -4.000 | 0.000 | 0 → 0 | 3 → 2 | 21% → 14% | 7 → 6 | 10 | 6 → 6 | -0.003 | -0.288 |
| Jogador 6 | 3-3 | 10 | 12.000 | -6.000 | 0 → 0 | 2 → 2 | 14% → 21% | 6 → 9 | 5 | 6 → 6 | -0.024 | 0.295 |
| Jogador 6 | 3-4 | 6 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 9 → 7 | 7 | 6 → 7 | 0.006 | 0.000 |
| Jogador 6 | 3-5 | 9 | 6.000 | 0.000 | 0 → 0 | 2 → 3 | 21% → 25% | 7 → 7 | 10 | 7 → 7 | 0.001 | 0.339 |
| Jogador 6 | 3-6 | 5 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 25% → 25% | 7 → 11 | 3 | 7 → 7 | -0.118 | 0.600 |
| Jogador 6 | 3-7 | 9 | 0.000 | 18.000 | 0 → 0 | 3 → 3 | 25% → 25% | 11 → 8 | 9 | 7 → 7 | 0.033 | 0.000 |
| Jogador 6 | 4-1 | 7 | 0.000 | 6.000 | 0 → 0 | 3 → 4 | 25% → 25% | 8 → 12 | 3 | 7 → 7 | 0.000 | 0.441 |
| Jogador 6 | 4-2 | 6 | 0.000 | 8.000 | 0 → 0 | 4 → 3 | 25% → 25% | 12 → 13 | 7 | 7 → 7 | -0.089 | 0.483 |
| Jogador 6 | 4-3 | 6 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 25% → 25% | 13 → 21 | 2 | 7 → 7 | 0.100 | 0.475 |
| Jogador 6 | 4-4 | 10 | 0.000 | -10.000 | 0 → 0 | 3 → 3 | 25% → 25% | 21 → 16 | 21 | 7 → 7 | 0.045 | 0.000 |
| Jogador 6 | 4-5 | 8 | 0.000 | -8.000 | 0 → 0 | 3 → 5 | 25% → 25% | 16 → 31 | 3 | 7 → 7 | -0.081 | 0.383 |
| Jogador 6 | 4-6 | 6 | 0.000 | -2.000 | 0 → 0 | 5 → 5 | 25% → 25% | 31 → 44 | 4 | 7 → 7 | -0.056 | 0.519 |
| Jogador 6 | 4-7 | 10 | 0.000 | -2.000 | 0 → 0 | 5 → 6 | 25% → 25% | 44 → 57 | 3 | 7 → 7 | 0.093 | 0.000 |
| Jogador 6 | 5-1 | 10 | 0.000 | 8.000 | 0 → 0 | 6 → 7 | 25% → 25% | 57 → 63 | 7 | 7 → 7 | -0.029 | -0.275 |
| Jogador 6 | 5-2 | 7 | 0.000 | -6.000 | 0 → 0 | 7 → 7 | 25% → 25% | 63 → 77 | 1 | 7 → 7 | -0.021 | 0.416 |
| Jogador 6 | 5-3 | 10 | -2.000 | 6.000 | 0 → 0 | 7 → 4 | 25% → 25% | 77 → 78 | 10 | 7 → 7 | -0.026 | -0.300 |
| Jogador 6 | 5-4 | 9 | 0.000 | 22.000 | 0 → 0 | 4 → 4 | 25% → 25% | 78 → 77 | 11 | 7 → 7 | 0.011 | 0.000 |
| Jogador 6 | 5-5 | 11 | 0.000 | -4.000 | 0 → 0 | 4 → 5 | 25% → 25% | 77 → 93 | 6 | 7 → 7 | 0.011 | 0.269 |
| Jogador 6 | 5-6 | 10 | 0.000 | -10.000 | 0 → 0 | 5 → 5 | 25% → 25% | 93 → 86 | 25 | 7 → 8 | 0.009 | -0.283 |
| Jogador 6 | 5-7 | 10 | 2.000 | 8.000 | 0 → 0 | 5 → 4 | 25% → 25% | 86 → 80 | 19 | 8 → 8 | -0.031 | 0.000 |
| Jogador 6 | 6-1 | 10 | 0.000 | -4.000 | 0 → 0 | 4 → 6 | 25% → 25% | 80 → 83 | 20 | 8 → 8 | 0.006 | -0.280 |
| Jogador 6 | 6-2 | 10 | 8.000 | 0.000 | 0 → 0 | 6 → 5 | 25% → 29% | 83 → 70 | 27 | 8 → 9 | -0.000 | 0.000 |
| Jogador 6 | 6-3 | 10 | -44.000 | -56.000 | 0 → 0 | 5 → 0 | 29% → 0% | 70 → 62 | 14 | 9 → 9 | 0.013 | -0.295 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 17, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 51 ações e piorou em 44.
- Jogador 6 — estado final: ouro 62, nível 9, vida 4.0, colocação 3.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.043 | 0.000 |
| Jogador 7 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.077 | 0.000 |
| Jogador 7 | 2-1 | 7 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.014 | 0.366 |
| Jogador 7 | 2-2 | 10 | -2.000 | 4.000 | 0 → 0 | 3 → 2 | 14% → 11% | 8 → 8 | 8 | 4 → 4 | 0.015 | -0.247 |
| Jogador 7 | 2-3 | 6 | 8.000 | 0.000 | 0 → 1 | 2 → 2 | 11% → 14% | 8 → 9 | 5 | 4 → 5 | 0.071 | 0.405 |
| Jogador 7 | 2-4 | 10 | 0.000 | -10.000 | 1 → 1 | 2 → 2 | 14% → 14% | 9 → 11 | 15 | 5 → 5 | 0.013 | 0.000 |
| Jogador 7 | 2-5 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 1 | 14% → 14% | 11 → 6 | 15 | 5 → 6 | 0.007 | -0.253 |
| Jogador 7 | 2-6 | 7 | 12.000 | -2.000 | 1 → 1 | 1 → 1 | 14% → 21% | 6 → 7 | 5 | 6 → 6 | 0.003 | 0.408 |
| Jogador 7 | 2-7 | 7 | 0.000 | 14.000 | 1 → 1 | 1 → 1 | 21% → 21% | 7 → 5 | 7 | 6 → 6 | -0.021 | 0.000 |
| Jogador 7 | 3-1 | 10 | 0.000 | 2.000 | 1 → 1 | 1 → 2 | 21% → 21% | 5 → 7 | 9 | 6 → 6 | -0.048 | 0.308 |
| Jogador 7 | 3-2 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 7 → 8 | 12 | 6 → 6 | 0.030 | 0.305 |
| Jogador 7 | 3-3 | 10 | -2.000 | -16.000 | 1 → 1 | 2 → 2 | 21% → 18% | 8 → 10 | 14 | 6 → 6 | -0.013 | -0.273 |
| Jogador 7 | 3-4 | 10 | 4.000 | 6.000 | 1 → 1 | 2 → 3 | 18% → 21% | 10 → 6 | 11 | 6 → 7 | 0.005 | 0.000 |
| Jogador 7 | 3-5 | 7 | 2.000 | 10.000 | 1 → 1 | 3 → 3 | 21% → 25% | 6 → 6 | 6 | 7 → 7 | -0.074 | 0.407 |
| Jogador 7 | 3-6 | 5 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 25% → 25% | 6 → 10 | 3 | 7 → 7 | -0.000 | 0.562 |
| Jogador 7 | 3-7 | 10 | -6.000 | -8.000 | 1 → 1 | 4 → 4 | 25% → 21% | 10 → 10 | 17 | 7 → 7 | -0.019 | 0.000 |
| Jogador 7 | 4-1 | 10 | 6.000 | -10.000 | 1 → 1 | 4 → 4 | 21% → 25% | 10 → 7 | 12 | 7 → 7 | 0.004 | 0.288 |
| Jogador 7 | 4-2 | 7 | 0.000 | 8.000 | 1 → 1 | 4 → 4 | 25% → 25% | 7 → 8 | 4 | 7 → 7 | 0.027 | -0.389 |
| Jogador 7 | 4-3 | 8 | 0.000 | 12.000 | 1 → 1 | 4 → 4 | 25% → 25% | 8 → 8 | 6 | 7 → 7 | 0.100 | 0.356 |
| Jogador 7 | 4-4 | 9 | 0.000 | 4.000 | 1 → 1 | 4 → 5 | 25% → 25% | 8 → 11 | 6 | 7 → 7 | 0.026 | 0.000 |
| Jogador 7 | 4-5 | 6 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 25% → 25% | 11 → 19 | 3 | 7 → 7 | 0.014 | 0.506 |
| Jogador 7 | 4-6 | 10 | 6.000 | -14.000 | 1 → 2 | 5 → 3 | 25% → 21% | 19 → 29 | 4 | 7 → 7 | -0.048 | 0.303 |
| Jogador 7 | 4-7 | 10 | -4.000 | -8.000 | 2 → 3 | 3 → 1 | 21% → 18% | 29 → 41 | 7 | 7 → 7 | 0.014 | 0.000 |
| Jogador 7 | 5-1 | 10 | 14.000 | 10.000 | 3 → 3 | 1 → 1 | 18% → 25% | 41 → 39 | 12 | 7 → 7 | -0.011 | 0.291 |
| Jogador 7 | 5-2 | 7 | 0.000 | 14.000 | 3 → 3 | 1 → 3 | 25% → 25% | 39 → 40 | 7 | 7 → 7 | 0.007 | -0.393 |
| Jogador 7 | 5-3 | 5 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 25% → 25% | 40 → 50 | 0 | 7 → 7 | -0.034 | 0.631 |
| Jogador 7 | 5-4 | 9 | 0.000 | 6.000 | 3 → 3 | 3 → 3 | 25% → 25% | 50 → 56 | 6 | 7 → 7 | 0.078 | 0.000 |
| Jogador 7 | 5-5 | 7 | 0.000 | -2.000 | 3 → 3 | 3 → 3 | 25% → 25% | 56 → 67 | 1 | 7 → 7 | 0.036 | -0.421 |
| Jogador 7 | 5-6 | 8 | 0.000 | -2.000 | 3 → 3 | 3 → 3 | 25% → 25% | 67 → 79 | 6 | 7 → 8 | -0.161 | 0.373 |
| Jogador 7 | 5-7 | 10 | 2.000 | 4.000 | 3 → 3 | 3 → 4 | 25% → 29% | 79 → 86 | 9 | 8 → 8 | 0.033 | 0.000 |
| Jogador 7 | 6-1 | 10 | 4.000 | 2.000 | 3 → 4 | 4 → 3 | 29% → 29% | 86 → 93 | 9 | 8 → 8 | 0.089 | 0.309 |
| Jogador 7 | 6-2 | 9 | 0.000 | -2.000 | 4 → 4 | 3 → 4 | 29% → 29% | 93 → 104 | 6 | 8 → 8 | -0.062 | -0.317 |
| Jogador 7 | 6-3 | 10 | -4.000 | -2.000 | 4 → 4 | 4 → 2 | 29% → 25% | 104 → 115 | 11 | 8 → 8 | 0.054 | 0.000 |
| Jogador 7 | 6-4 | 9 | 8.000 | 4.000 | 4 → 4 | 2 → 3 | 25% → 29% | 115 → 120 | 8 | 8 → 8 | 0.023 | 0.000 |
| Jogador 7 | 6-5 | 9 | 0.000 | 2.000 | 4 → 4 | 3 → 3 | 29% → 29% | 120 → 130 | 7 | 8 → 8 | -0.020 | -0.322 |
| Jogador 7 | 6-6 | 10 | -56.000 | -52.000 | 4 → 0 | 3 → 0 | 29% → 0% | 130 → 129 | 11 | 8 → 8 | -0.128 | -0.280 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 23, COMPOSITION_COMPATIBILITY: 34, IMMEDIATE_UPGRADE: 11, PAIR_POTENTIAL: 17; mudanças de composição: 1; posicionamento melhorou em 68 ações e piorou em 54.
- Jogador 7 — estado final: ouro 129, nível 8, vida 6.0, colocação 2.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.113 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.074 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 3 | 3 → 4 | 0.007 | 0.000 |
| Jogador 8 | 2-1 | 11 | 6.000 | 0.000 | 0 → 1 | 2 → 0 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.022 | -0.220 |
| Jogador 8 | 2-2 | 6 | 0.000 | 2.000 | 1 → 1 | 0 → 0 | 14% → 14% | 6 → 8 | 7 | 4 → 4 | 0.010 | -0.404 |
| Jogador 8 | 2-3 | 10 | 4.000 | 2.000 | 1 → 1 | 0 → 1 | 14% → 18% | 8 → 7 | 10 | 4 → 5 | 0.037 | -0.232 |
| Jogador 8 | 2-4 | 10 | 0.000 | -4.000 | 1 → 1 | 1 → 2 | 18% → 18% | 7 → 15 | 8 | 5 → 5 | -0.000 | 0.000 |
| Jogador 8 | 2-5 | 10 | 0.000 | 4.000 | 1 → 0 | 2 → 2 | 18% → 18% | 15 → 20 | 8 | 5 → 5 | 0.026 | 0.259 |
| Jogador 8 | 2-6 | 10 | 0.000 | 4.000 | 0 → 0 | 2 → 3 | 18% → 18% | 20 → 8 | 21 | 5 → 6 | 0.011 | -0.237 |
| Jogador 8 | 2-7 | 10 | 0.000 | -8.000 | 0 → 0 | 3 → 2 | 18% → 18% | 8 → 5 | 16 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 10 | 2.000 | -2.000 | 0 → 0 | 2 → 2 | 18% → 21% | 5 → 11 | 8 | 6 → 6 | -0.004 | 0.303 |
| Jogador 8 | 3-2 | 10 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 11 → 12 | 13 | 6 → 6 | 0.000 | -0.258 |
| Jogador 8 | 3-3 | 10 | 6.000 | 2.000 | 0 → 0 | 2 → 2 | 21% → 25% | 12 → 6 | 15 | 6 → 7 | 0.019 | 0.291 |
| Jogador 8 | 3-4 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 3 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | -0.006 | 0.000 |
| Jogador 8 | 3-5 | 6 | 0.000 | 10.000 | 0 → 0 | 3 → 3 | 25% → 25% | 5 → 7 | 5 | 7 → 7 | -0.016 | 0.483 |
| Jogador 8 | 3-6 | 10 | 0.000 | -12.000 | 0 → 0 | 3 → 2 | 25% → 25% | 7 → 19 | 10 | 7 → 7 | 0.000 | -0.258 |
| Jogador 8 | 3-7 | 10 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 25% → 25% | 19 → 12 | 18 | 7 → 7 | -0.000 | 0.000 |
| Jogador 8 | 4-1 | 10 | 0.000 | 16.000 | 0 → 0 | 2 → 3 | 25% → 25% | 12 → 10 | 8 | 7 → 7 | 0.064 | 0.285 |
| Jogador 8 | 4-2 | 10 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 25% → 25% | 10 → 15 | 9 | 7 → 7 | 0.000 | 0.288 |
| Jogador 8 | 4-3 | 8 | 0.000 | -2.000 | 0 → 0 | 3 → 5 | 25% → 25% | 15 → 22 | 5 | 7 → 7 | -0.105 | -0.334 |
| Jogador 8 | 4-4 | 10 | 0.000 | 6.000 | 0 → 0 | 5 → 6 | 25% → 25% | 22 → 23 | 12 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 10 | 0.000 | -4.000 | 0 → 0 | 6 → 6 | 25% → 25% | 23 → 32 | 10 | 7 → 7 | 0.056 | -0.290 |
| Jogador 8 | 4-6 | 10 | 0.000 | 0.000 | 0 → 0 | 6 → 6 | 25% → 25% | 32 → 41 | 11 | 7 → 7 | 0.042 | -0.275 |
| Jogador 8 | 4-7 | 10 | 0.000 | 12.000 | 0 → 0 | 6 → 4 | 25% → 25% | 41 → 37 | 20 | 7 → 7 | -0.006 | 0.000 |
| Jogador 8 | 5-1 | 10 | 0.000 | -8.000 | 0 → 0 | 4 → 5 | 25% → 25% | 37 → 51 | 10 | 7 → 7 | 0.006 | -0.275 |
| Jogador 8 | 5-2 | 10 | -24.000 | -48.000 | 0 → 0 | 5 → 0 | 25% → 0% | 51 → 47 | 6 | 7 → 7 | -0.126 | -0.290 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 30, COMPOSITION_COMPATIBILITY: 33, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 15; mudanças de composição: 1; posicionamento melhorou em 34 ações e piorou em 28.
- Jogador 8 — estado final: ouro 47, nível 7, vida 10.0, colocação 5.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 66 | 42 | 1 | 1 | 1 | 0 | 0 | 0 | 15 | 0 | 1 | 0 |
| Jogador 2 | 115 | 87 | 1 | 1 | 6 | 0 | 0 | 0 | 34 | 1 | 0 | 0 |
| Jogador 3 | 72 | 37 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 1 | 0 | 0 |
| Jogador 4 | 67 | 36 | 1 | 1 | 1 | 0 | 1 | 0 | 9 | 2 | 1 | 0 |
| Jogador 5 | 76 | 52 | 5 | 9 | 12 | 2 | 3 | 0 | 7 | 1 | 0 | 0 |
| Jogador 6 | 67 | 33 | 2 | 2 | 3 | 2 | 0 | 0 | 1 | 2 | 2 | 0 |
| Jogador 7 | 85 | 47 | 0 | 0 | 0 | 0 | 0 | 1 | 8 | 3 | 0 | 0 |
| Jogador 8 | 85 | 58 | 3 | 5 | 7 | 0 | 1 | 0 | 10 | 4 | 7 | 0 |
- Jogador 1 — venda DA_18_Rakan (3-2, step 132): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Ornn (4-4, step 222): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Rengar (4-5, step 234): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rakan (4-2, step 205): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_LeBlanc (6-1, step 333): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rengar (6-4, step 364): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Sett (6-5, step 374): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Lillia (6-6, step 385): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rengar (6-6, step 390): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_RekSai (3-3, step 142): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Murkwolf18 (3-7, step 184): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Xayah (5-2, step 274): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_KhaZix (5-3, step 284): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Scuttlecrab18 (5-4, step 295): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Rakan (2-5, step 98): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_18_Cassiopeia (4-2, step 209): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Yunara (4-3, step 216): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Diana (4-7, step 252): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=True, compensações posteriores=0.
- Jogador 5 — venda DA_18_Kobuko (3-4, step 156): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (3-4, step 157): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (3-5, step 166): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Yunara (3-7, step 188): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Karma18 (3-7, step 190): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-5, step 96): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-5, step 97): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Sentry (3-2, step 134): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Xayah (5-5, step 301): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Tristana (6-1, step 333): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_Krug18 (6-2, step 342): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Camille (2-5, step 98): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Warwick (3-4, step 155): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 7 — venda DA_18_Rakan (4-6, step 244): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_18_Hecarim (4-7, step 259): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rengar (6-5, step 373): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Sentry (2-5, step 97): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Karma18 (2-6, step 105): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Diana (2-7, step 118): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Veigar (2-7, step 119): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Scuttlecrab18 (3-1, step 126): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_CrimsonRaptor18 (3-6, step 180): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Teemo (4-4, step 222): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **4**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| LOW | Jogador 1 | 2-3 | 75 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 1 | 2-4 | 86 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kayle) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 1 | 3-2 | 132 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 4-4 | 222 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-5 | 234 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 2-2 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-4 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-4 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-4 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-4 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-4 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 539 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-3 | 646 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 781 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 1023 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 1024 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1134 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-7 | 1135 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1232 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1233 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1378 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-2 | 1379 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1518 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1657 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1798 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1939 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-6 | 2899 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 4-6 | 2900 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 2-1 | 59 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-5 | 100 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rengar) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-6 | 105 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_KogMaw18_AD) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 2 | 4-2 | 205 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-4 | 228 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 4-5 | 235 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Scuttlecrab18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 4-5 | 236 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Azir) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 6-1 | 333 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_LeBlanc' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-4 | 364 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-5 | 374 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sett' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 6-6 | 385 | SOLD_CORE_UNIT | Venda de 'DA_18_Lillia' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-6 | 390 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-7 | 1184 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-1 | 1319 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-2 | 1452 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-3 | 1589 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-4 | 1727 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-5 | 1859 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-6 | 1973 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-7 | 2111 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-1 | 2246 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-2 | 2385 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2519 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 2658 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2793 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 2907 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 3046 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-7 | 3047 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 3184 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-1 | 3185 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 3322 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-2 | 3323 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-3 | 3462 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-3 | 3463 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-4 | 3589 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-4 | 3590 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-5 | 3692 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-5 | 3693 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-6 | 3807 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-1 | 4040 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-2 | 4170 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-2 | 4171 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-3 | 4309 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-3 | 4310 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-4 | 4449 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-4 | 4450 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-5 | 4590 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-5 | 4591 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-6 | 4727 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-6 | 4728 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| HIGH | Jogador 3 | 3-3 | 142 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 3-7 | 184 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Murkwolf18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 5-2 | 274 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Xayah' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 5-3 | 284 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 5-4 | 295 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 238 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 239 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-7 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-7 | 253 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 323 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 324 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 325 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 326 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 327 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 328 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-7 | 329 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-1 | 450 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-2 | 512 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-3 | 582 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-4 | 700 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-5 | 794 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-6 | 924 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 1058 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1156 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-3 | 1407 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 1784 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 1921 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 2037 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 2126 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-3 | 2227 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-4 | 2291 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-5 | 2418 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-6 | 2494 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-7 | 2638 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-1 | 2779 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-2 | 2917 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-3 | 3045 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-4 | 3171 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-5 | 3259 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-6 | 3373 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-7 | 3512 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-1 | 3652 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 6-1 | 3653 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 3-5 | 1761 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-5 | 3350 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 4 | 2-7 | 114 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 3-1 | 127 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 4 | 4-2 | 209 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 4-3 | 216 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 207 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 208 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 209 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 210 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 217 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 218 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 219 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 220 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 226 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 227 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 228 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 229 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 230 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-5 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-5 | 238 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-5 | 239 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-5 | 240 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-6 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-6 | 248 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-6 | 249 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-6 | 250 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 2-6 | 945 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-7 | 1079 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-3 | 1463 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-4 | 1559 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-5 | 1643 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-6 | 1751 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-7 | 1847 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-1 | 1971 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-1 | 1972 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 2110 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-2 | 2111 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-3 | 2251 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-3 | 2252 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-4 | 2387 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-4 | 2388 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 2523 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-5 | 2524 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-6 | 2660 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-6 | 2661 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-7 | 2802 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-7 | 2803 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-1 | 2938 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-1 | 2939 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-2 | 3079 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-2 | 3080 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 2-4 | 87 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 107 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Elise) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-7 | 118 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rakan) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-7 | 119 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Scuttlecrab18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-1 | 129 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-4 | 156 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-4 | 157 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-4 | 160 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Alistar) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 5 | 3-5 | 166 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-5 | 169 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-6 | 176 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-6 | 178 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Murkwolf18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-7 | 185 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rengar) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-7 | 186 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Vi18) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-7 | 188 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-7 | 190 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Karma18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 2-1 | 54 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 55 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-3 | 558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 690 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 823 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 957 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-7 | 1092 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-1 | 1227 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1347 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-3 | 1455 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-4 | 1591 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1728 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1861 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-7 | 1997 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-1 | 2131 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 2240 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 2241 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-3 | 2377 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2378 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-4 | 2515 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-5 | 2657 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-6 | 2795 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 4-6 | 2796 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 3-1 | 1324 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-1 | 2217 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-2 | 2354 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-2 | 66 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 2-4 | 90 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 2-5 | 96 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 2-5 | 97 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 2-5 | 99 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 6 | 3-2 | 134 | SOLD_CORE_UNIT | Venda de 'DA_18_Sentry' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 3-2 | 140 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 3-3 | 147 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 6 | 5-5 | 301 | SOLD_CORE_UNIT | Venda de 'DA_18_Xayah' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 6-1 | 333 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 6-2 | 342 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Krug18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 2-2 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 75 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 283 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 284 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 285 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 286 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 287 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 288 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 289 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 290 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-3 | 291 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-4 | 292 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-4 | 293 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-4 | 294 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-4 | 295 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-4 | 296 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-4 | 297 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-4 | 298 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-4 | 299 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-4 | 300 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-5 | 306 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-5 | 307 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-5 | 308 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-5 | 309 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-5 | 310 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-5 | 311 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-3 | 223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-4 | 270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-1 | 367 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-2 | 463 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 535 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 666 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-5 | 800 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-6 | 922 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1032 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1033 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-1 | 1166 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1167 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-2 | 1306 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-3 | 1442 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1443 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-4 | 1525 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1526 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-5 | 1646 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1647 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-6 | 1719 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-6 | 1720 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-7 | 1843 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1844 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-1 | 1945 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 1946 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 2032 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 2033 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 2124 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 2125 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 2255 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 2256 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-5 | 2368 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-5 | 2369 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-6 | 2456 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 2457 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 2594 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-7 | 2595 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-1 | 2734 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 2735 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 2841 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-2 | 2842 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-3 | 2986 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-3 | 2987 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-4 | 3111 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-4 | 3112 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-5 | 3274 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-5 | 3275 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-6 | 3407 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-6 | 3408 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-7 | 3545 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-7 | 3546 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 6-1 | 3682 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 6-1 | 3683 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 6-2 | 3813 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 6-2 | 3814 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 6-3 | 3959 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 6-3 | 3960 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| HIGH | Jogador 6 | 2-6 | 958 | TEXT_MOVE_OSCILLATION | Possível alternância de duas unidades; confirme identidade/estado nos snapshots estruturados. |
| MEDIUM | Jogador 7 | 2-5 | 98 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 4-7 | 259 | SOLD_CORE_UNIT | Venda de 'DA_18_Hecarim' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 6-5 | 373 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 2-4 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 441 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 579 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-3 | 667 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-6 | 1038 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-6 | 1039 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-7 | 1140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-7 | 1141 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1277 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-1 | 1278 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1415 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-2 | 1416 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1549 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-3 | 1550 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1687 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-4 | 1688 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1791 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-5 | 1792 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1867 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-6 | 1868 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 2004 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-7 | 2005 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 2137 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-1 | 2138 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2238 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-2 | 2239 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2352 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-3 | 2353 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2479 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-5 | 2565 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-6 | 2706 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-7 | 2849 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-1 | 2991 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-2 | 3094 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-3 | 3172 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-4 | 3303 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-5 | 3407 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-6 | 3518 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-7 | 3656 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-1 | 3799 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-2 | 3930 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-3 | 4075 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-4 | 4206 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-4 | 4207 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-5 | 4336 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-5 | 4337 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-6 | 4475 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 6-6 | 4476 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 4-4 | 2542 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 8 | 1-4 | 41 | PURCHASE_SALE_REVIEW | Compra de DA_18_RekSai foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 8 | 2-3 | 76 | PURCHASE_SALE_REVIEW | Compra de DA_18_Xayah foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-4 | 86 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_KhaZix) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-4 | 88 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_MasterYi_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 8 | 2-5 | 95 | PURCHASE_SALE_REVIEW | Compra de DA_Karma18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 8 | 2-5 | 96 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rammus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-5 | 97 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sentry' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 2-6 | 105 | SOLD_CORE_UNIT | Venda de 'DA_Karma18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 2-7 | 115 | PURCHASE_SALE_REVIEW | Compra de DA_18_Akali_AD foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 8 | 2-7 | 118 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 2-7 | 119 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Veigar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 3-1 | 125 | PURCHASE_SALE_REVIEW | Compra de DA_Murkwolf18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 3-1 | 130 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Lillia) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-2 | 139 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-3 | 145 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-3 | 146 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_LeBlanc) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-6 | 178 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-6 | 180 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 3-7 | 187 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rengar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 4-4 | 222 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 3-1 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-1 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-2 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-4 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-5 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 179 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-7 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 8 | 4-3 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-3 | 217 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-3 | 218 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-4 | 226 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-4 | 227 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-4 | 228 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-4 | 229 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-4 | 230 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 238 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 239 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 240 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 8 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-3 | 224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-4 | 321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 468 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-2 | 551 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-3 | 684 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 817 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1624 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-4 | 1713 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-5 | 1800 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-6 | 1937 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-7 | 2071 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 2217 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2354 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2467 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 2468 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 2603 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-4 | 2604 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 2744 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-5 | 2745 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-2 | 3296 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 5-2 | 3297 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 4-2 | 2444 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
