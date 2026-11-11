# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4448**
- Achados: **725**
- CRITICAL: 0 | HIGH: 7 | MEDIUM: 64 | LOW: 654

## Metadados da sessão

- Match ID: 21e27f87-28eb-4280-9856-ff90181bb40d
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 3d63262fb93d7504bfc05b4e6efd43b7d3bf9e722c0407b8e8b1bd7903bc856d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **3953**
- Entradas posteriores à eliminação ignoradas: **495**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 59 | 6 | 8 | 5 | 39 | 0 | 2 | não/inconclusivo | 0 |
| Jogador 6 | 158 | 7 | 9 | 4 | 61 | 3 | 1 | não/inconclusivo | 0 |
| Jogador 7 | 188 | 7 | 5 | 11 | 65 | 0 | 0 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 196 | 69 | 29 | 7 | 0 | 11 | 67 | 0.1432 | 9 | 30 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 27, ALL_IN::ITEM: 6, ALL_IN::MOVE_BENCH: 8, ALL_IN::MOVE_BOARD: 3, ALL_IN::PASS: 1, ALL_IN::SELL: 10, STABILIZE::BUY: 42, STABILIZE::BUY_XP: 7, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 30, STABILIZE::MOVE_BOARD: 26, STABILIZE::PASS: 10, STABILIZE::SELL: 19
- Jogador 1 — recompensas por ação: BUY: média 0.5059 (n=69), BUY_XP: média -0.0214 (n=7), ITEM: média 0.1492 (n=13), MOVE_BENCH: média 0.0590 (n=38), MOVE_BOARD: média 0.0066 (n=29), PASS: média -0.0573 (n=11), SELL: média -0.3600 (n=29)
| Jogador 2 | 189 | 75 | 49 | 6 | 0 | 8 | 41 | 0.0985 | 4 | 43 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::SELL: 2, STABILIZE::BUY: 73, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 10, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 28, STABILIZE::PASS: 8, STABILIZE::SELL: 47
- Jogador 2 — recompensas por ação: BUY: média 0.2821 (n=75), BUY_XP: média -0.0083 (n=6), ITEM: média 0.1590 (n=10), MOVE_BENCH: média 0.2908 (n=13), MOVE_BOARD: média -0.0286 (n=28), PASS: média 0.0000 (n=8), SELL: média -0.1441 (n=49)
| Jogador 3 | 175 | 43 | 10 | 36 | 0 | 15 | 63 | 0.1294 | 3 | 42 |
- Jogador 3 — ações por estratégia: ECON::BUY: 9, ECON::BUY_XP: 8, ECON::ITEM: 1, ECON::MOVE_BENCH: 4, ECON::MOVE_BOARD: 6, ECON::SELL: 4, FAST8::BUY: 1, FAST8::BUY_XP: 9, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 12, FAST8::PASS: 4, STABILIZE::BUY: 26, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 16, STABILIZE::PASS: 9, STABILIZE::SELL: 4, WINSTREAK::BUY: 7, WINSTREAK::BUY_XP: 7, WINSTREAK::ITEM: 2, WINSTREAK::MOVE_BENCH: 2, WINSTREAK::MOVE_BOARD: 7, WINSTREAK::PASS: 2, WINSTREAK::SELL: 2
- Jogador 3 — recompensas por ação: BUY: média 0.4653 (n=43), BUY_XP: média -0.0181 (n=36), ITEM: média 0.1600 (n=8), MOVE_BENCH: média 0.2082 (n=22), MOVE_BOARD: média -0.0044 (n=41), PASS: média -0.0233 (n=15), SELL: média -0.2050 (n=10)
| Jogador 4 | 127 | 39 | 15 | 8 | 0 | 12 | 45 | 0.1011 | 7 | 12 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 1, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 4, ALL_IN::SELL: 1, STABILIZE::BUY: 38, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 28, STABILIZE::MOVE_BOARD: 13, STABILIZE::PASS: 12, STABILIZE::SELL: 14
- Jogador 4 — recompensas por ação: BUY: média 0.4995 (n=39), BUY_XP: média -0.0225 (n=8), ITEM: média 0.1562 (n=8), MOVE_BENCH: média -0.0884 (n=32), MOVE_BOARD: média -0.0039 (n=13), PASS: média -0.0125 (n=12), SELL: média -0.3120 (n=15)
| Jogador 5 | 161 | 71 | 51 | 6 | 0 | 6 | 18 | 0.0653 | 12 | 19 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 10, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 2, ALL_IN::SELL: 10, STABILIZE::BUY: 61, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 5, STABILIZE::PASS: 6, STABILIZE::SELL: 41
- Jogador 5 — recompensas por ação: BUY: média 0.2890 (n=71), BUY_XP: média -0.0183 (n=6), ITEM: média 0.1700 (n=9), MOVE_BENCH: média 0.1654 (n=13), MOVE_BOARD: média 0.0520 (n=5), PASS: média 0.0000 (n=6), SELL: média -0.2714 (n=51)
| Jogador 6 | 179 | 61 | 38 | 9 | 0 | 13 | 42 | 0.0790 | 12 | 36 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 8, ALL_IN::ITEM: 6, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 4, ALL_IN::OTHER: 1, ALL_IN::PASS: 1, ALL_IN::SELL: 5, STABILIZE::BUY: 53, STABILIZE::BUY_XP: 9, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 10, STABILIZE::MOVE_BOARD: 27, STABILIZE::PASS: 12, STABILIZE::SELL: 33
- Jogador 6 — recompensas por ação: BUY: média 0.3198 (n=61), BUY_XP: média -0.0456 (n=9), ITEM: média 0.1520 (n=15), MOVE_BENCH: média 0.2518 (n=11), MOVE_BOARD: média -0.0081 (n=31), OTHER: média 0.0000 (n=1), PASS: média -0.0539 (n=13), SELL: média -0.2382 (n=38)
| Jogador 7 | 174 | 65 | 31 | 5 | 1 | 16 | 48 | 0.1113 | 6 | 41 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 4, ALL_IN::ITEM: 1, ALL_IN::SELL: 5, STABILIZE::BUY: 61, STABILIZE::BUY_XP: 5, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 33, STABILIZE::PASS: 16, STABILIZE::REROLL: 1, STABILIZE::SELL: 26
- Jogador 7 — recompensas por ação: BUY: média 0.3823 (n=65), BUY_XP: média -0.0600 (n=5), ITEM: média 0.1600 (n=8), MOVE_BENCH: média 0.0427 (n=15), MOVE_BOARD: média -0.0058 (n=33), PASS: média -0.0244 (n=16), REROLL: média -0.1600 (n=1), SELL: média -0.2052 (n=31)
| Jogador 8 | 170 | 77 | 47 | 5 | 0 | 5 | 26 | 0.1089 | 9 | 27 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 4, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 2, ALL_IN::SELL: 1, STABILIZE::BUY: 73, STABILIZE::BUY_XP: 5, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 11, STABILIZE::PASS: 5, STABILIZE::SELL: 46
- Jogador 8 — recompensas por ação: BUY: média 0.3364 (n=77), BUY_XP: média -0.0500 (n=5), ITEM: média 0.1750 (n=10), MOVE_BENCH: média 0.1527 (n=15), MOVE_BOARD: média -0.0054 (n=11), PASS: média -0.0080 (n=5), SELL: média -0.2355 (n=47)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 08:32:45 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | ? | 08:32:47 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | ? | 08:32:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 08:32:52 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 08:32:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 08:32:53 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-1 | 08:32:54 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 08:32:55 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 08:32:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 08:32:57 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 1-2 | 08:32:59 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-2 | 08:33:00 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 08:33:00 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 08:33:01 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-2 | 08:33:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 08:33:08 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 08:33:08 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 08:33:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 08:33:16 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 08:33:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-4 | 08:33:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 08:33:22 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 2-1 | 08:33:25 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 08:33:25 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.1300 |  |
| Jogador 1 | 2-1 | 08:33:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 08:33:27 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-1 | 08:33:27 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.2800 |  |
| Jogador 1 | 2-1 | 08:33:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-2 | 08:33:36 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Diana | 0.3500 |  |
| Jogador 1 | 2-2 | 08:33:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Diana | -0.0400 |  |
| Jogador 1 | 2-2 | 08:33:38 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | -0.1700 |  |
| Jogador 1 | 2-2 | 08:33:39 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Diana | 0.3300 |  |
| Jogador 1 | 2-2 | 08:33:39 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | -0.1600 |  |
| Jogador 1 | 2-2 | 08:33:40 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | -0.1700 |  |
| Jogador 1 | 2-2 | 08:33:40 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 08:33:41 | MOVE Board -> Board: Ornn (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 08:33:50 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 2-3 | 08:33:50 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.3600 |  |
| Jogador 1 | 2-3 | 08:33:51 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.5000 |  |
| Jogador 1 | 2-3 | 08:33:51 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2000 |  |
| Jogador 1 | 2-3 | 08:33:52 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0400 |  |
| Jogador 1 | 2-3 | 08:33:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 08:33:53 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0400 |  |
| Jogador 1 | 2-3 | 08:33:54 | MOVE Board -> Board: Xayah (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 08:33:55 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-4 | 08:34:06 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Adaptador | DA_18_Ornn | 0.3100 |  |
| Jogador 1 | 2-4 | 08:34:07 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_18_Ornn | 0.3700 |  |
| Jogador 1 | 2-4 | 08:34:07 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Adaptador | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 1 | 2-4 | 08:34:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 2-4 | 08:34:08 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 08:34:09 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 2-4 | 08:34:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 08:34:23 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 2-5 | 08:34:24 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Adaptador | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 2-5 | 08:34:25 | MOVE Bench -> Board: Kayle (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Adaptador | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 1 | 2-5 | 08:34:26 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 2-5 | 08:34:26 | MOVE Board -> Board: Kayle (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 08:34:27 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | -0.4200 |  |
| Jogador 1 | 2-5 | 08:34:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 08:34:29 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.6000 |  |
| Jogador 1 | 2-6 | 08:34:44 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Adaptador | DA_KogMaw18_AD | 0.9800 |  |
| Jogador 1 | 2-6 | 08:34:44 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Adaptador | DA_KogMaw18_AD | 1.0400 |  |
| Jogador 1 | 2-6 | 08:34:45 | MOVE Bench -> Board: Xayah (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Adaptador | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 2-6 | 08:34:45 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Adaptador | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 1 | 2-6 | 08:34:46 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 1 | 2-6 | 08:34:47 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 2-6 | 08:34:48 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Adaptador | DA_KogMaw18_AD | -0.5900 |  |
| Jogador 1 | 2-6 | 08:34:48 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Kog'Maw (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Adaptador | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 1 | 2-6 | 08:34:49 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Adaptador | DA_KogMaw18_AD | 0.5700 |  |
| Jogador 1 | 2-7 | 08:35:05 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Adaptador | DA_KogMaw18_AD | 0.5000 |  |
| Jogador 1 | 2-7 | 08:35:06 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Kog'Maw (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Adaptador | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 1 | 2-7 | 08:35:06 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Adaptador | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 1 | 2-7 | 08:35:07 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 1 | 2-7 | 08:35:08 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 2-7 | 08:35:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-7 | 08:35:10 | MOVE Board -> Board: Akali (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 08:35:11 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Adaptador | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 1 | 3-1 | 08:35:21 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.6500 |  |
| Jogador 1 | 3-1 | 08:35:21 | MOVE Bench -> Board: Kayle (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 1 | 3-1 | 08:35:22 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Adaptador | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 1 | 3-1 | 08:35:23 | MOVE Bench -> Board: Grompe (i:4.0) <-> Kayle (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Adaptador | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-1 | 08:35:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 08:35:24 | MOVE Board -> Board: Grompe (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 08:35:25 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-1 | 08:35:26 | MOVE Bench -> Board: Kayle (i:8.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 1 | 3-2 | 08:35:36 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Adaptador | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 1 | 3-3 | 08:35:56 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Adaptador | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 3-3 | 08:35:57 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Kayle (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Adaptador | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 1 | 3-3 | 08:35:57 | VENDEU: Kayle (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Adaptador | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 1 | 3-3 | 08:35:58 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Adaptador | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 3-3 | 08:35:59 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 08:35:59 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 08:36:00 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Adaptador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 3-3 | 08:36:01 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Adaptador | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 3-3 | 08:36:01 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-4 | 08:36:21 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Adaptador | DA_KogMaw18_AD | 0.7800 |  |
| Jogador 1 | 3-4 | 08:36:22 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-4 | 08:36:23 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Adaptador | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 1 | 3-4 | 08:36:23 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Adaptador | DA_KogMaw18_AD | -0.1400 |  |
| Jogador 1 | 3-4 | 08:36:24 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Adaptador | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 1 | 3-4 | 08:36:25 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-4 | 08:36:25 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-4 | 08:36:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Adaptador | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-5 | 08:36:48 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-5 | 08:36:48 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Adaptador | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 1 | 3-5 | 08:36:49 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-5 | 08:36:50 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Adaptador | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 1 | 3-5 | 08:36:50 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Adaptador | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 1 | 3-5 | 08:36:52 | MOVE Bench -> Board: Grompe (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Adaptador | DA_KogMaw18_AD | -1.0900 |  |
| Jogador 1 | 3-5 | 08:36:53 | MOVE Bench -> Board: Akali (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Adaptador | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 1 | 3-5 | 08:36:53 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Adaptador | DA_KogMaw18_AD | -0.1400 |  |
| Jogador 1 | 3-6 | 08:37:06 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Adaptador | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 1 | 3-6 | 08:37:06 | MOVE Bench -> Board: Grompe (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Adaptador | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 3-6 | 08:37:07 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Adaptador | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 1 | 3-6 | 08:37:08 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Adaptador | DA_KogMaw18_AD | -0.3900 |  |
| Jogador 1 | 3-6 | 08:37:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Adaptador | DA_KogMaw18_AD | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-7 | 08:37:24 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Adaptador | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 1 | 3-7 | 08:37:25 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Adaptador | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 1 | 3-7 | 08:37:26 | MOVE Bench -> Board: Grompe (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Adaptador | DA_KogMaw18_AD | -0.2200 |  |
| Jogador 1 | 3-7 | 08:37:27 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Adaptador | DA_KogMaw18_AD | -0.3400 |  |
| Jogador 1 | 3-7 | 08:37:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Adaptador | DA_KogMaw18_AD | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-1 | 08:37:45 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Adaptador | DA_KogMaw18_AD | -0.5700 |  |
| Jogador 1 | 4-2 | 08:38:12 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Adaptador | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 1 | 4-2 | 08:38:12 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 56 | 4 | Adaptador | DA_KogMaw18_AD | -0.4700 |  |
| Jogador 1 | 4-2 | 08:38:13 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Adaptador | DA_KogMaw18_AD | 0.7800 |  |
| Jogador 1 | 4-2 | 08:38:14 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-2 | 08:38:15 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 57 | 4 | Adaptador | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 1 | 4-2 | 08:38:16 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 4 | Adaptador | DA_KogMaw18_AD | -0.5300 |  |
| Jogador 1 | 4-2 | 08:38:17 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 4 | Adaptador | DA_KogMaw18_AD | -0.9900 |  |
| Jogador 1 | 4-2 | 08:38:17 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 4 | Adaptador | DA_KogMaw18_AD | -0.3700 |  |
| Jogador 1 | 4-3 | 08:38:33 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Adaptador | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 4-3 | 08:38:33 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Adaptador | DA_KogMaw18_AD | 0.5100 |  |
| Jogador 1 | 4-3 | 08:38:35 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Adaptador | DA_KogMaw18_AD | -0.8100 |  |
| Jogador 1 | 4-3 | 08:38:36 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Adaptador | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 4-3 | 08:38:37 | MOVE Bench -> Board: Grompe (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Adaptador | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 4-3 | 08:38:37 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Adaptador | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 4-4 | 08:38:54 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Adaptador | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 1 | 4-4 | 08:38:55 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Adaptador | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 1 | 4-4 | 08:38:56 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Adaptador | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 1 | 4-5 | 08:39:27 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Adaptador | DA_KogMaw18_AD | 1.0300 |  |
| Jogador 1 | 4-5 | 08:39:27 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Adaptador | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 1 | 4-5 | 08:39:28 | MOVE Bench -> Board: Malphite (i:8.0) <-> Cascalho (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Adaptador | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 1 | 4-5 | 08:39:29 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Adaptador | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 4-5 | 08:39:30 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Adaptador | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 1 | 4-5 | 08:39:32 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Adaptador | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 4-6 | 08:39:50 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Adaptador | DA_KogMaw18_AD | 0.9800 |  |
| Jogador 1 | 4-6 | 08:39:50 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Adaptador | DA_KogMaw18_AD | 0.7800 |  |
| Jogador 1 | 4-7 | 08:40:25 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Akali (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Adaptador | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 4-7 | 08:40:26 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Adaptador | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 4-7 | 08:40:27 | VENDEU: Grompe (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Adaptador | DA_KogMaw18_AD | -0.6900 |  |
| Jogador 1 | 4-7 | 08:40:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Adaptador | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 4-7 | 08:40:28 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Adaptador | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 1 | 4-7 | 08:40:30 | VENDEU: Kog'Maw (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 99 | 5 | Adaptador | DA_18_Akali_AD | -0.7000 |  |
| Jogador 1 | 4-7 | 08:40:31 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 99 | 5 | Adaptador | DA_18_Akali_AD | 0.4100 |  |
| Jogador 1 | 5-1 | 08:40:49 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Adaptador | DA_18_Akali_AD | 0.7900 |  |
| Jogador 1 | 5-2 | 08:41:26 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Adaptador | DA_18_Akali_AD | 0.5000 |  |
| Jogador 1 | 5-2 | 08:41:27 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Malphite (i:8.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Adaptador | DA_18_Akali_AD | 0.0600 |  |
| Jogador 1 | 5-2 | 08:41:28 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Malphite (i:8.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Adaptador | DA_18_Akali_AD | 0.0800 |  |
| Jogador 1 | 5-2 | 08:41:29 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Krugue (i:6.0) (tabuleiro slot 23) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Adaptador | DA_18_Akali_AD | 0.0600 |  |
| Jogador 1 | 5-2 | 08:41:30 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Adaptador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 5-2 | 08:41:31 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Adaptador | DA_18_Akali_AD | 1.0500 |  |
| Jogador 1 | 5-3 | 08:41:52 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Adaptador | DA_18_Akali_AD | 0.9200 |  |
| Jogador 1 | 5-3 | 08:41:53 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Adaptador | DA_18_Akali_AD | 0.7000 |  |
| Jogador 1 | 5-4 | 08:42:30 | VENDEU: Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Adaptador | DA_18_Akali_AD | -0.6900 |  |
| Jogador 1 | 5-4 | 08:42:31 | COMPROU: Lux (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Adaptador | DA_18_Akali_AD | -0.1400 |  |
| Jogador 1 | 5-4 | 08:42:32 | MOVE Board -> Board: Cascalho (i:2.0) <-> Akali (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Adaptador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 5-4 | 08:42:33 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Adaptador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 5-4 | 08:42:34 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Adaptador | DA_18_Akali_AD | -0.5700 |  |
| Jogador 1 | 5-5 | 08:42:57 | VENDEU: Lux (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 158 | 5 | Adaptador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 5-5 | 08:42:58 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Adaptador | DA_18_Akali_AD | 1.0500 |  |
| Jogador 1 | 5-6 | 08:43:41 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 168 | 5 | Adaptador | DA_18_Diana | 1.0400 |  |
| Jogador 1 | 5-6 | 08:43:42 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 168 | 5 | Adaptador | DA_18_Diana | 0.2700 |  |
| Jogador 1 | 5-6 | 08:43:43 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 165 | 5 | Adaptador | DA_18_Diana | -0.1700 |  |
| Jogador 1 | 5-6 | 08:43:44 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Adaptador | DA_18_Diana | 0.0400 |  |
| Jogador 1 | 5-6 | 08:43:45 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Adaptador | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 5-6 | 08:43:46 | MOVE Bench -> Board: Diana (i:12.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Adaptador | DA_18_Diana | 0.4800 |  |
| Jogador 1 | 5-7 | 08:44:09 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 173 | 5 | Adaptador | DA_18_Diana | 0.9800 |  |
| Jogador 1 | 5-7 | 08:44:10 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Krugue (i:6.0) (tabuleiro slot 23) | ALL_IN | HP crítico: gastar para sobreviver | 173 | 5 | Adaptador | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 6-1 | 08:44:57 | VENDEU: Cascalho (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 190 | 5 | Adaptador | DA_18_Diana | -0.6900 |  |
| Jogador 1 | 6-1 | 08:44:58 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 189 | 5 | Adaptador | DA_18_Diana | 1.0800 |  |
| Jogador 1 | 6-1 | 08:44:59 | VENDEU: Kayle (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 191 | 5 | Adaptador | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 6-1 | 08:45:01 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Adaptador | DA_18_Diana | 1.1100 |  |
| Jogador 1 | 6-2 | 08:45:24 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 198 | 5 | Adaptador | DA_18_Diana | 1.1100 |  |
| Jogador 1 | 6-2 | 08:45:25 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 195 | 5 | Adaptador | DA_18_Diana | 0.8700 |  |
| Jogador 1 | 6-2 | 08:45:26 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 193 | 5 | Adaptador | DA_18_Diana | 0.2200 |  |
| Jogador 1 | 6-2 | 08:45:27 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 192 | 5 | Adaptador | DA_18_Diana | 0.2100 |  |
| Jogador 1 | 6-3 | 08:46:09 | VENDEU: Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 210 | 5 | Adaptador | DA_18_Diana | -0.7400 |  |
| Jogador 1 | 6-3 | 08:46:10 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 207 | 5 | Adaptador | DA_18_Diana | 0.5100 |  |
| Jogador 1 | 6-3 | 08:46:11 | VENDEU: Nidalee (i:16.0) | ALL_IN | HP crítico: gastar para sobreviver | 218 | 5 | Adaptador | DA_18_Diana | -0.7400 |  |
| Jogador 1 | 6-3 | 08:46:12 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 215 | 5 | Adaptador | DA_18_Diana | 1.0800 |  |
| Jogador 1 | 6-3 | 08:46:13 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Adaptador | DA_18_Diana | -0.1800 |  |
| Jogador 1 | 6-3 | 08:46:14 | MOVE Bench -> Board: Krugue (i:12.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Adaptador | DA_18_Diana | 0.4300 |  |
| Jogador 1 | 6-4 | 08:46:36 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 217 | 5 | Adaptador | DA_18_Diana | -0.0800 |  |
| Jogador 1 | 6-4 | 08:46:37 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 218 | 5 | Adaptador | DA_18_Diana | -0.0500 |  |
| Jogador 2 | ? | 08:32:45 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | ? | 08:32:47 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | ? | 08:32:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 08:32:52 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 08:32:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 08:32:53 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 1-1 | 08:32:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 08:32:57 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 1-2 | 08:32:59 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 08:33:00 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 08:33:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 08:33:04 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 08:33:08 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 08:33:08 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 08:33:09 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-3 | 08:33:09 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-3 | 08:33:11 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 08:33:12 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 08:33:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 08:33:16 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 08:33:20 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 08:33:20 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 1-4 | 08:33:21 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 1-4 | 08:33:22 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 2-1 | 08:33:25 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 2-1 | 08:33:25 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 2-1 | 08:33:26 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-1 | 08:33:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-1 | 08:33:27 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 2-1 | 08:33:31 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-2 | 08:33:36 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 2-2 | 08:33:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-2 | 08:33:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-2 | 08:33:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 08:33:50 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.9700 |  |
| Jogador 2 | 2-3 | 08:33:50 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.3300 |  |
| Jogador 2 | 2-3 | 08:33:51 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-3 | 08:33:51 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-3 | 08:33:52 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 2-3 | 08:33:53 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 2-3 | 08:33:53 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 2-3 | 08:33:54 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 08:33:55 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-4 | 08:34:06 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.3500 |  |
| Jogador 2 | 2-4 | 08:34:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 08:34:07 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 2-4 | 08:34:08 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-4 | 08:34:08 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 08:34:09 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.5000 |  |
| Jogador 2 | 2-4 | 08:34:10 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 2-4 | 08:34:10 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.5500 |  |
| Jogador 2 | 2-4 | 08:34:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 08:34:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 2-5 | 08:34:24 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.4900 |  |
| Jogador 2 | 2-5 | 08:34:25 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 2-5 | 08:34:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-5 | 08:34:26 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.6000 |  |
| Jogador 2 | 2-5 | 08:34:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-5 | 08:34:28 | MOVE Board -> Board: Veigar (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-5 | 08:34:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-6 | 08:34:44 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 2-6 | 08:34:44 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 2-6 | 08:34:45 | MOVE Board -> Board: Xayah (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-6 | 08:34:45 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-6 | 08:34:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-7 | 08:35:05 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 2-7 | 08:35:06 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 2-7 | 08:35:06 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 2-7 | 08:35:07 | MOVE Bench -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 2-7 | 08:35:08 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-7 | 08:35:09 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 2-7 | 08:35:10 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-7 | 08:35:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 08:35:21 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.8400 |  |
| Jogador 2 | 3-1 | 08:35:21 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.6900 |  |
| Jogador 2 | 3-1 | 08:35:22 | MOVE Bench -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.5100 |  |
| Jogador 2 | 3-1 | 08:35:23 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 3-1 | 08:35:23 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 3-1 | 08:35:24 | MOVE Board -> Board: Xayah (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-1 | 08:35:25 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-1 | 08:35:26 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 08:35:36 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-3 | 08:35:56 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 3-3 | 08:35:57 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-3 | 08:35:57 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 3-3 | 08:35:58 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-3 | 08:35:59 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-3 | 08:35:59 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 08:36:00 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-3 | 08:36:01 | MOVE Board -> Board: Kobuko (i:2.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-3 | 08:36:01 | MOVE Board -> Board: Xayah (i:4.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-4 | 08:36:21 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-4 | 08:36:22 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Veigar | 0.8100 |  |
| Jogador 2 | 3-4 | 08:36:23 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-4 | 08:36:23 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Veigar | 0.5400 |  |
| Jogador 2 | 3-4 | 08:36:24 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-4 | 08:36:25 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-4 | 08:36:25 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-4 | 08:36:26 | MOVE Board -> Board: Rakan (i:2.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-4 | 08:36:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Veigar | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-5 | 08:36:48 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-5 | 08:36:48 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Feérico | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 3-5 | 08:36:49 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Feérico | DA_18_Veigar | -0.5900 |  |
| Jogador 2 | 3-5 | 08:36:50 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Feérico | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 3-5 | 08:36:50 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Feérico | DA_18_Veigar | -0.4700 |  |
| Jogador 2 | 3-5 | 08:36:52 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 3-5 | 08:36:53 | MOVE Board -> Board: Xayah (i:4.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-5 | 08:36:53 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Veigar | -0.2400 |  |
| Jogador 2 | 3-6 | 08:37:06 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-6 | 08:37:06 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Feérico | DA_18_Veigar | 0.7500 |  |
| Jogador 2 | 3-6 | 08:37:07 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 3-6 | 08:37:08 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Feérico | DA_18_Veigar | 0.3900 |  |
| Jogador 2 | 3-6 | 08:37:08 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_18_Veigar | -0.3700 |  |
| Jogador 2 | 3-6 | 08:37:09 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-6 | 08:37:10 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-6 | 08:37:10 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Feérico | DA_18_Veigar | -0.3300 |  |
| Jogador 2 | 3-6 | 08:37:11 | MOVE Board -> Board: Lillia (i:8.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-7 | 08:37:24 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Feérico | DA_18_Veigar | 0.1700 |  |
| Jogador 2 | 3-7 | 08:37:25 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Feérico | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 3-7 | 08:37:26 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Feérico | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 3-7 | 08:37:27 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 3 | Feérico | DA_18_Veigar | 0.8300 |  |
| Jogador 2 | 3-7 | 08:37:27 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 3 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-7 | 08:37:28 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Feérico | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 3-7 | 08:37:29 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 3 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-7 | 08:37:29 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Feérico | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 4-1 | 08:37:45 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-2 | 08:38:12 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Feérico | DA_18_Tristana | 0.9600 |  |
| Jogador 2 | 4-2 | 08:38:12 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 77 | 5 | Feérico | DA_18_Tristana | -0.2800 |  |
| Jogador 2 | 4-2 | 08:38:13 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Feérico | DA_18_Tristana | -0.2800 |  |
| Jogador 2 | 4-2 | 08:38:14 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Feérico | DA_18_Tristana | 0.0100 |  |
| Jogador 2 | 4-2 | 08:38:15 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Feérico | DA_18_Veigar | -0.6000 |  |
| Jogador 2 | 4-2 | 08:38:16 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 82 | 5 | Feérico | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 4-2 | 08:38:17 | MOVE Board -> Board: Rakan (i:2.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 82 | 5 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 4-2 | 08:38:17 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-3 | 08:38:33 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 91 | 5 | Feérico | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 4-3 | 08:38:33 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-3 | 08:38:35 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 91 | 5 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 4-3 | 08:38:36 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-3 | 08:38:37 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 91 | 5 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 4-3 | 08:38:37 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-4 | 08:38:54 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 100 | 5 | Feérico | DA_18_Veigar | 0.3800 |  |
| Jogador 2 | 4-4 | 08:38:55 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-4 | 08:38:56 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Feérico | DA_18_Veigar | 0.3200 |  |
| Jogador 2 | 4-5 | 08:39:27 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 112 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-5 | 08:39:27 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Feérico | DA_18_Veigar | 0.9600 |  |
| Jogador 2 | 4-5 | 08:39:28 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Feérico | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 4-5 | 08:39:29 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 110 | 5 | Feérico | DA_18_Veigar | 0.3900 |  |
| Jogador 2 | 4-5 | 08:39:30 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Feérico | DA_18_Veigar | -0.5900 |  |
| Jogador 2 | 4-5 | 08:39:32 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Feérico | DA_18_Veigar | 0.3900 |  |
| Jogador 2 | 4-6 | 08:39:50 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 121 | 5 | Feérico | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 4-6 | 08:39:50 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 120 | 5 | Feérico | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 4-7 | 08:40:25 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Lillia (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 130 | 5 | Feérico | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 4-7 | 08:40:26 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Lillia (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 130 | 5 | Feérico | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 4-7 | 08:40:27 | EQUIP_FROM_INVENTORY: TFT_Item_RunaansHurricane -> Lillia (i:8.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 130 | 5 | Feérico | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-7 | 08:40:27 | EQUIP_FROM_INVENTORY: TFT_Item_Crownguard -> Kobuko (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 130 | 5 | Feérico | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 4-7 | 08:40:28 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 131 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-7 | 08:40:30 | COMPROU: Lux (Sabugueiro) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 126 | 5 | Feérico | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 4-7 | 08:40:31 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 126 | 5 | Feérico | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 5-1 | 08:40:49 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 134 | 5 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 5-2 | 08:41:26 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 148 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 5-2 | 08:41:27 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 145 | 5 | Feérico | DA_18_Veigar | 0.7100 |  |
| Jogador 2 | 5-2 | 08:41:28 | VENDEU: Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 150 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-2 | 08:41:29 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 147 | 5 | Feérico | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 5-2 | 08:41:30 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 150 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 5-2 | 08:41:31 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 148 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 5-3 | 08:41:52 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 162 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-3 | 08:41:53 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 161 | 5 | Feérico | DA_18_Veigar | 0.9600 |  |
| Jogador 2 | 5-4 | 08:42:30 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 175 | 5 | Feérico | DA_18_Veigar | -0.5100 |  |
| Jogador 2 | 5-4 | 08:42:31 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 171 | 5 | Feérico | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 5-4 | 08:42:32 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 174 | 5 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 5-4 | 08:42:33 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 171 | 5 | Feérico | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 5-4 | 08:42:34 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 174 | 5 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 5-4 | 08:42:35 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 172 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 5-5 | 08:42:57 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 185 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-5 | 08:42:58 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 181 | 5 | Feérico | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 5-6 | 08:43:41 | VENDEU: Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 195 | 5 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 5-6 | 08:43:42 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 192 | 5 | Feérico | DA_18_Veigar | 1.0200 |  |
| Jogador 2 | 5-6 | 08:43:43 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 189 | 5 | Feérico | DA_18_Veigar | 0.2100 |  |
| Jogador 2 | 5-6 | 08:43:44 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 186 | 5 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 5-6 | 08:43:45 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 194 | 5 | Feérico | DA_18_Veigar | -0.6000 |  |
| Jogador 2 | 5-6 | 08:43:46 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 190 | 5 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-7 | 08:44:09 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Kobuko (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Feérico | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 5-7 | 08:44:10 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 203 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 6-1 | 08:44:57 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 212 | 5 | Feérico | DA_18_Veigar | 0.6400 |  |
| Jogador 2 | 6-1 | 08:44:58 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 215 | 5 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 6-1 | 08:44:59 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 212 | 5 | Feérico | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 6-1 | 08:45:01 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 215 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 3 | ? | 08:32:45 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | ? | 08:32:47 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | ? | 08:32:47 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | ? | 08:32:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 08:32:52 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 08:32:52 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 08:32:53 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-1 | 08:32:54 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 1-1 | 08:32:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 08:32:57 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-2 | 08:32:59 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 08:33:00 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 08:33:00 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 08:33:01 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-2 | 08:33:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 08:33:04 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 1-3 | 08:33:08 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 08:33:08 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 08:33:09 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 08:33:09 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 08:33:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 08:33:16 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 08:33:20 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 08:33:20 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 08:33:21 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 1-4 | 08:33:22 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-1 | 08:33:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-1 | 08:33:25 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 08:33:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 08:33:36 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-2 | 08:33:37 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 2-2 | 08:33:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-2 | 08:33:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 08:33:50 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-3 | 08:33:50 | MOVE Bench -> Board: Camille (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | -0.3900 |  |
| Jogador 3 | 2-3 | 08:33:51 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 2-3 | 08:33:51 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 2-3 | 08:33:52 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 2-3 | 08:33:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-3 | 08:33:53 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 08:33:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 08:34:06 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 2-4 | 08:34:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-4 | 08:34:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 08:34:23 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-5 | 08:34:24 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 08:34:25 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.1100 |  |
| Jogador 3 | 2-5 | 08:34:26 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 08:34:26 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 2-5 | 08:34:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 2-5 | 08:34:28 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.2700 |  |
| Jogador 3 | 2-5 | 08:34:28 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 2-5 | 08:34:29 | MOVE Board -> Board: Yunara (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 08:34:44 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-6 | 08:34:44 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.1700 |  |
| Jogador 3 | 2-6 | 08:34:45 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 08:34:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 2-6 | 08:34:46 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.5300 |  |
| Jogador 3 | 2-6 | 08:34:47 | MOVE Board -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 08:34:48 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-6 | 08:34:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 08:35:05 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.2800 |  |
| Jogador 3 | 2-7 | 08:35:06 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 2-7 | 08:35:06 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 08:35:07 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-7 | 08:35:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-7 | 08:35:09 | MOVE Bench -> Board: Vi (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.3900 |  |
| Jogador 3 | 2-7 | 08:35:10 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.5800 |  |
| Jogador 3 | 2-7 | 08:35:11 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.5200 |  |
| Jogador 3 | 3-1 | 08:35:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-1 | 08:35:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-1 | 08:35:22 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | -0.5800 |  |
| Jogador 3 | 3-1 | 08:35:23 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.8300 |  |
| Jogador 3 | 3-1 | 08:35:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 3-1 | 08:35:24 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.4400 |  |
| Jogador 3 | 3-1 | 08:35:25 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-1 | 08:35:26 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-2 | 08:35:36 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | 3-3 | 08:35:56 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-3 | 08:35:57 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Colosso | DA_18_Akali_AD | 0.8000 |  |
| Jogador 3 | 3-3 | 08:35:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 08:35:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-3 | 08:35:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.0600 |  |
| Jogador 3 | 3-3 | 08:35:59 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 3-3 | 08:36:00 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 3-3 | 08:36:01 | MOVE Board -> Board: Vi (i:6.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 08:36:01 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-4 | 08:36:21 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 08:36:22 | MOVE Board -> Board: Akali (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 08:36:23 | MOVE Board -> Board: Vi (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 08:36:23 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 08:36:48 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 08:36:48 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-5 | 08:36:49 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 08:37:06 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 08:37:06 | MOVE Board -> Board: Vi (i:6.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-6 | 08:37:07 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Colosso | DA_18_Akali_AD | -0.0800 |  |
| Jogador 3 | 3-7 | 08:37:24 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Colosso | DA_18_Akali_AD | 0.1300 |  |
| Jogador 3 | 3-7 | 08:37:25 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_TearOfTheGoddess -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Colosso | DA_18_Akali_AD | 0.1900 |  |
| Jogador 3 | 3-7 | 08:37:26 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-7 | 08:37:27 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-7 | 08:37:27 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Colosso | DA_18_Akali_AD | -0.1800 |  |
| Jogador 3 | 4-1 | 08:37:45 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 08:38:12 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 4-2 | 08:38:12 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-2 | 08:38:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 4 | Colosso | DA_18_Akali_AD | 0.0300 |  |
| Jogador 3 | 4-2 | 08:38:14 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 4 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-2 | 08:38:15 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 35 | 4 | Colosso | DA_18_Akali_AD | 0.0300 |  |
| Jogador 3 | 4-2 | 08:38:16 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 4 | Colosso | DA_18_Akali_AD | 0.0300 |  |
| Jogador 3 | 4-2 | 08:38:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 4 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-2 | 08:38:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 4 | Colosso | DA_18_Akali_AD | 0.0300 |  |
| Jogador 3 | 4-3 | 08:38:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-3 | 08:38:33 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 24 | 2 | Colosso | DA_18_Akali_AD | 0.0900 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 3 | 4-3 | 08:38:35 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 24 | 2 | Colosso | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 4-3 | 08:38:36 | COMPROU: Krugue (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 21 | 2 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 08:38:37 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vi (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 21 | 2 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 08:38:37 | MOVE Board -> Board: Vi (i:6.0) <-> Rek'Sai (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 21 | 2 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 08:38:54 | VENDEU: Shen (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 4-4 | 08:38:55 | COMPROU: Vi (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 28 | 2 | Colosso | DA_18_Akali_AD | 0.7400 |  |
| Jogador 3 | 4-4 | 08:38:56 | MOVE Bench -> Board: Krugue (i:6.0) <-> Rek'Sai (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 28 | 2 | Colosso | DA_18_Akali_AD | -0.9200 |  |
| Jogador 3 | 4-5 | 08:39:27 | COMPROU: Master Yi (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 34 | 2 | Colosso | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 4-5 | 08:39:27 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 30 | 2 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-5 | 08:39:28 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 26 | 2 | Colosso | DA_18_Akali_AD | -0.1100 |  |
| Jogador 3 | 4-5 | 08:39:29 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 22 | 2 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-5 | 08:39:30 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 2 | Colosso | DA_18_Akali_AD | -0.1100 |  |
| Jogador 3 | 4-5 | 08:39:32 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 18 | 2 | Colosso | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 4-6 | 08:39:50 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 24 | 1 | Colosso | DA_18_Akali_AD | 0.8200 |  |
| Jogador 3 | 4-6 | 08:39:50 | COMPROU: Zyra (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 20 | 1 | Colosso | DA_18_Akali_AD | 0.1100 |  |
| Jogador 3 | 4-7 | 08:40:25 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 2 | Colosso | DA_18_Akali_AD | 0.2000 |  |
| Jogador 3 | 4-7 | 08:40:26 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Kha'Zix (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 2 | Colosso | DA_18_Akali_AD | 0.1400 |  |
| Jogador 3 | 4-7 | 08:40:27 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Kha'Zix (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 2 | Colosso | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 4-7 | 08:40:27 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 25 | 2 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 4-7 | 08:40:28 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 21 | 2 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-7 | 08:40:30 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 17 | 2 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 4-7 | 08:40:31 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 13 | 2 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 5-1 | 08:40:49 | VENDEU: Lobo Trevoguari (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 27 | 1 | Colosso | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 5-2 | 08:41:26 | COMPROU: Grompe (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 32 | 2 | Colosso | DA_18_Akali_AD | 0.7000 |  |
| Jogador 3 | 5-2 | 08:41:27 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 28 | 2 | Colosso | DA_18_Akali_AD | -0.0600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 3 | 5-2 | 08:41:28 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 24 | 2 | Colosso | DA_18_Akali_AD | 0.0200 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 3 | 5-2 | 08:41:29 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 20 | 2 | Colosso | DA_18_Akali_AD | 0.0200 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 3 | 5-2 | 08:41:30 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 16 | 2 | Colosso | DA_18_Akali_AD | -0.0600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 3 | 5-2 | 08:41:31 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 12 | 2 | Colosso | DA_18_Akali_AD | 0.0200 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 3 | 5-3 | 08:41:52 | VENDEU: Rek'Sai (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 22 | 1 | Colosso | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 5-3 | 08:41:53 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 20 | 1 | Colosso | DA_18_Akali_AD | 0.7700 |  |
| Jogador 3 | 5-4 | 08:42:30 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Yunara (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 28 | 2 | Colosso | DA_18_Akali_AD | 0.1300 |  |
| Jogador 3 | 5-4 | 08:42:31 | VENDEU: Vi (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 36 | 2 | Colosso | DA_18_Akali_AD | -0.4900 |  |
| Jogador 3 | 5-4 | 08:42:32 | COMPROU: Lux (Espinhos Negros) (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Colosso | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 5-4 | 08:42:33 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 27 | 2 | Colosso | DA_18_Akali_AD | -0.0100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 3 | 5-4 | 08:42:34 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 23 | 2 | Colosso | DA_18_Akali_AD | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 3 | 5-4 | 08:42:35 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 23 | 2 | Colosso | DA_18_Akali_AD | 0.5600 |  |
| Jogador 3 | 5-5 | 08:42:57 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 28 | 2 | Colosso | DA_18_Diana | 0.7700 |  |
| Jogador 3 | 5-5 | 08:42:58 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 25 | 2 | Colosso | DA_18_Diana | 0.2300 |  |
| Jogador 3 | 5-6 | 08:43:41 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Colosso | DA_18_Diana | 0.7800 |  |
| Jogador 3 | 5-6 | 08:43:42 | VENDEU: Yunara (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 33 | 2 | Colosso | DA_18_Diana | 0.0100 |  |
| Jogador 3 | 5-6 | 08:43:43 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 29 | 2 | Colosso | DA_18_Diana | 0.1800 |  |
| Jogador 3 | 5-6 | 08:43:44 | MOVE Board -> Board: Grompe (i:4.0) <-> Krugue (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 29 | 2 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 5-6 | 08:43:45 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 29 | 2 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 5-6 | 08:43:46 | MOVE Board -> Board: Diana (i:12.0) <-> Grompe (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 29 | 2 | Colosso | DA_18_Diana | -0.0200 |  |
| Jogador 3 | 5-7 | 08:44:09 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Kha'Zix (i:6.0) (tabuleiro slot 24) | ECON | ECON: acumular até o limite de juros de 50 | 37 | 2 | Colosso | DA_18_Diana | 0.0200 |  |
| Jogador 3 | 5-7 | 08:44:10 | MOVE Board -> Board: Grompe (i:4.0) <-> Fiddlesticks (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 37 | 2 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 6-1 | 08:44:57 | VENDEU: Mamãe Bicuda (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 50 | 3 | Colosso | DA_18_Diana | 0.0400 |  |
| Jogador 3 | 6-1 | 08:44:58 | COMPROU: Grompe (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 48 | 3 | Colosso | DA_18_Diana | 0.9700 |  |
| Jogador 3 | 6-1 | 08:44:59 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 48 | 3 | Colosso | DA_18_Diana | 0.2700 |  |
| Jogador 3 | 6-1 | 08:45:01 | COMPROU: Grompe (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 46 | 3 | Colosso | DA_18_Diana | 0.3900 |  |
| Jogador 3 | 6-2 | 08:45:24 | COMPROU: Master Yi (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 54 | 4 | Colosso | DA_18_Diana | 0.9100 |  |
| Jogador 3 | 6-2 | 08:45:25 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 54 | 4 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 6-2 | 08:45:26 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Akali (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 54 | 4 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 6-2 | 08:45:27 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 54 | 4 | Colosso | DA_18_Diana | -0.0400 |  |
| Jogador 3 | 6-3 | 08:46:09 | MOVE Board -> Board: Akali (i:4.0) <-> Krugue (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 67 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 6-3 | 08:46:10 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 67 | 5 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 6-3 | 08:46:11 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 67 | 5 | Colosso | DA_18_Diana | -0.0500 |  |
| Jogador 3 | 6-4 | 08:46:36 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 79 | 5 | Colosso | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 6-4 | 08:46:37 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Akali (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 79 | 5 | Colosso | DA_18_Diana | -0.0100 |  |
| Jogador 4 | ? | 08:32:45 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | ? | 08:32:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | ? | 08:32:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | ? | 08:32:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 08:32:52 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 08:32:52 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 08:32:53 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-1 | 08:32:54 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 1-1 | 08:32:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 08:32:57 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4600 |  |
| Jogador 4 | 1-2 | 08:32:59 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 08:33:00 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 08:33:00 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 08:33:01 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-2 | 08:33:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 08:33:08 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 08:33:08 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 08:33:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 08:33:16 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 4 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-4 | 08:33:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 1-4 | 08:33:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 08:33:22 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3900 |  |
| Jogador 4 | 2-1 | 08:33:25 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 2-1 | 08:33:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 2-1 | 08:33:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-1 | 08:33:31 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4300 |  |
| Jogador 4 | 2-2 | 08:33:36 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 4 | 2-2 | 08:33:37 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-2 | 08:33:38 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-2 | 08:33:39 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-2 | 08:33:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 08:33:40 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 08:33:40 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 08:33:41 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 4 | 2-3 | 08:33:50 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-3 | 08:33:50 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-3 | 08:33:51 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 4 | 2-3 | 08:33:51 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-3 | 08:33:52 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-3 | 08:33:53 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 2-3 | 08:33:53 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 2-3 | 08:33:54 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 4 | 2-3 | 08:33:55 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 4 | 2-4 | 08:34:06 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 1.0000 |  |
| Jogador 4 | 2-4 | 08:34:07 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 2-4 | 08:34:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-4 | 08:34:08 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 4 | 2-4 | 08:34:08 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 4 | 2-4 | 08:34:09 | MOVE Bench -> Board: Diana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 2-4 | 08:34:10 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 4 | 2-4 | 08:34:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 2-4 | 08:34:11 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-5 | 08:34:23 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 4 | 2-5 | 08:34:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 2-5 | 08:34:25 | MOVE Board -> Board: Karma (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 2-5 | 08:34:26 | MOVE Board -> Board: Yorick (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-5 | 08:34:26 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 2-5 | 08:34:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-6 | 08:34:44 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 4 | 2-6 | 08:34:44 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 4 | 2-6 | 08:34:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-6 | 08:34:45 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 4 | 2-6 | 08:34:46 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.5900 |  |
| Jogador 4 | 2-6 | 08:34:47 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 4 | 2-6 | 08:34:48 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 4 | 2-6 | 08:34:48 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 2-6 | 08:34:49 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 08:35:05 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 2-7 | 08:35:06 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 4 | 2-7 | 08:35:06 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-7 | 08:35:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 08:35:08 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 4 | 2-7 | 08:35:09 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 4 | 2-7 | 08:35:10 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 2-7 | 08:35:11 | MOVE Bench -> Board: Yorick (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 3-1 | 08:35:21 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 4 | 3-1 | 08:35:21 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 4 | 3-1 | 08:35:22 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-1 | 08:35:23 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.6000 |  |
| Jogador 4 | 3-1 | 08:35:23 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 4 | 3-1 | 08:35:24 | MOVE Bench -> Board: Yorick (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 4 | 3-1 | 08:35:25 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-1 | 08:35:26 | MOVE Board -> Board: Diana (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 3-2 | 08:35:36 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 4 | 3-3 | 08:35:56 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-3 | 08:35:57 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 4 | 3-3 | 08:35:57 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 3-3 | 08:35:58 | MOVE Bench -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 4 | 3-3 | 08:35:59 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | -0.4200 |  |
| Jogador 4 | 3-3 | 08:35:59 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | -0.3800 |  |
| Jogador 4 | 3-3 | 08:36:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 08:36:21 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Florescer | DA_18_Yunara | 0.8100 |  |
| Jogador 4 | 3-4 | 08:36:22 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_18_Yunara | 0.7800 |  |
| Jogador 4 | 3-4 | 08:36:23 | MOVE Bench -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_18_Yunara | 0.1100 |  |
| Jogador 4 | 3-4 | 08:36:23 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_18_Yunara | -0.0600 |  |
| Jogador 4 | 3-4 | 08:36:24 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_18_Yunara | -0.5000 |  |
| Jogador 4 | 3-4 | 08:36:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_18_Yunara | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-5 | 08:36:48 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_18_Yorick | -0.5000 |  |
| Jogador 4 | 3-5 | 08:36:48 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Florescer | DA_18_Yorick | 0.8500 |  |
| Jogador 4 | 3-5 | 08:36:49 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Florescer | DA_18_Yorick | -0.2400 |  |
| Jogador 4 | 3-5 | 08:36:50 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Florescer | DA_18_Yorick | 0.7100 |  |
| Jogador 4 | 3-5 | 08:36:50 | MOVE Bench -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Florescer | DA_18_Yorick | 0.0600 |  |
| Jogador 4 | 3-5 | 08:36:52 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Florescer | DA_18_Yorick | -0.3800 |  |
| Jogador 4 | 3-5 | 08:36:53 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Florescer | DA_18_Yorick | -0.4000 |  |
| Jogador 4 | 3-5 | 08:36:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Florescer | DA_18_Yorick | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-6 | 08:37:06 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Florescer | DA_18_Yorick | 0.7900 |  |
| Jogador 4 | 3-6 | 08:37:06 | MOVE Bench -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Florescer | DA_18_Yorick | 0.0800 |  |
| Jogador 4 | 3-6 | 08:37:07 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Florescer | DA_18_Yorick | -0.3900 |  |
| Jogador 4 | 3-6 | 08:37:08 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Florescer | DA_18_Yorick | -0.4100 |  |
| Jogador 4 | 3-6 | 08:37:08 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Florescer | DA_18_Yorick | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-7 | 08:37:24 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Florescer | DA_18_Yorick | 0.1500 |  |
| Jogador 4 | 3-7 | 08:37:25 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Florescer | DA_18_Yorick | 0.1800 |  |
| Jogador 4 | 3-7 | 08:37:26 | MOVE Bench -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Florescer | DA_18_Yorick | 0.0600 |  |
| Jogador 4 | 3-7 | 08:37:27 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Florescer | DA_18_Yorick | -0.3800 |  |
| Jogador 4 | 3-7 | 08:37:27 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Florescer | DA_18_Yorick | -0.4300 |  |
| Jogador 4 | 3-7 | 08:37:28 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Florescer | DA_18_Yorick | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-1 | 08:37:45 | VENDEU: Yorick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 49 | 3 | Florescer | DA_18_Yunara | -0.6700 |  |
| Jogador 4 | 4-2 | 08:38:12 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Florescer | DA_18_Yunara | 0.4600 |  |
| Jogador 4 | 4-2 | 08:38:12 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Sejuani (i:4.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Florescer | DA_18_Yunara | 0.0900 |  |
| Jogador 4 | 4-2 | 08:38:13 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Fiddlesticks (i:6.0) (tabuleiro slot 26) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Florescer | DA_18_Yunara | 0.1000 |  |
| Jogador 4 | 4-2 | 08:38:14 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Fiddlesticks (i:6.0) (tabuleiro slot 26) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Florescer | DA_18_Yunara | 0.0900 |  |
| Jogador 4 | 4-2 | 08:38:15 | MOVE Bench -> Board: Yunara (i:4.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Florescer | DA_18_Yunara | -0.8400 |  |
| Jogador 4 | 4-2 | 08:38:16 | MOVE Bench -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Florescer | DA_18_Yunara | 0.0600 |  |
| Jogador 4 | 4-2 | 08:38:17 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Florescer | DA_18_Yunara | -0.2500 |  |
| Jogador 4 | 4-2 | 08:38:17 | MOVE Bench -> Board: Yunara (i:4.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 4 | Florescer | DA_18_Yunara | -0.3900 |  |
| Jogador 5 | ? | 08:32:45 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | ? | 08:32:47 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 5 | ? | 08:32:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 08:32:52 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 08:32:52 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 08:32:53 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-1 | 08:32:54 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 08:32:55 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 08:32:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 08:32:57 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4300 |  |
| Jogador 5 | 1-2 | 08:32:59 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 1-2 | 08:33:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 08:33:08 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 08:33:08 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 08:33:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 08:33:16 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 5 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 5 | 1-4 | 08:33:20 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 5 | 1-4 | 08:33:20 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 08:33:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 08:33:25 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-1 | 08:33:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 08:33:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 08:33:36 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 5 | 2-2 | 08:33:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 2-2 | 08:33:38 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 5 | 2-2 | 08:33:39 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 08:33:39 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 5 | 2-2 | 08:33:40 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 08:33:40 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0300 |  |
| Jogador 5 | 2-2 | 08:33:41 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-3 | 08:33:50 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Cassiopeia | 0.3100 |  |
| Jogador 5 | 2-3 | 08:33:50 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-3 | 08:33:51 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 08:33:51 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-3 | 08:33:52 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-3 | 08:33:53 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.1700 |  |
| Jogador 5 | 2-3 | 08:33:53 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0800 |  |
| Jogador 5 | 2-3 | 08:33:54 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 08:33:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 08:34:06 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2900 |  |
| Jogador 5 | 2-4 | 08:34:07 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3400 |  |
| Jogador 5 | 2-4 | 08:34:07 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 2-4 | 08:34:08 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1200 |  |
| Jogador 5 | 2-4 | 08:34:08 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-4 | 08:34:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 08:34:10 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3500 |  |
| Jogador 5 | 2-4 | 08:34:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-4 | 08:34:11 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.4000 |  |
| Jogador 5 | 2-5 | 08:34:23 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3600 |  |
| Jogador 5 | 2-5 | 08:34:24 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0900 |  |
| Jogador 5 | 2-5 | 08:34:25 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 08:34:26 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 08:34:26 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-5 | 08:34:27 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 2-5 | 08:34:28 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.4300 |  |
| Jogador 5 | 2-5 | 08:34:28 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-5 | 08:34:29 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-6 | 08:34:44 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.3500 |  |
| Jogador 5 | 2-6 | 08:34:44 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.9600 |  |
| Jogador 5 | 2-6 | 08:34:45 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.2100 |  |
| Jogador 5 | 2-6 | 08:34:45 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-6 | 08:34:46 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-6 | 08:34:47 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.1100 |  |
| Jogador 5 | 2-6 | 08:34:48 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.4200 |  |
| Jogador 5 | 2-6 | 08:34:48 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.3800 |  |
| Jogador 5 | 2-6 | 08:34:49 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 2-7 | 08:35:05 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Yunara | 0.7500 |  |
| Jogador 5 | 2-7 | 08:35:06 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Yunara | 0.1900 |  |
| Jogador 5 | 2-7 | 08:35:06 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Yunara | 0.1100 |  |
| Jogador 5 | 2-7 | 08:35:07 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Yunara | 0.0300 |  |
| Jogador 5 | 2-7 | 08:35:08 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Tristana | -0.6200 |  |
| Jogador 5 | 2-7 | 08:35:09 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Tristana | -0.0700 |  |
| Jogador 5 | 2-7 | 08:35:10 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 2-7 | 08:35:11 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Tristana | -0.2600 |  |
| Jogador 5 | 3-1 | 08:35:21 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Tristana | 0.6900 |  |
| Jogador 5 | 3-1 | 08:35:21 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_18_Tristana | 0.2700 |  |
| Jogador 5 | 3-1 | 08:35:22 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Tristana | -0.0700 |  |
| Jogador 5 | 3-1 | 08:35:23 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_Tristana | -0.5400 |  |
| Jogador 5 | 3-1 | 08:35:23 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_Tristana | -0.2400 |  |
| Jogador 5 | 3-1 | 08:35:24 | MOVE Bench -> Board: Tristana (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_Tristana | -0.1000 |  |
| Jogador 5 | 3-1 | 08:35:25 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_Tristana | -0.3400 |  |
| Jogador 5 | 3-1 | 08:35:26 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Tristana | -0.1000 |  |
| Jogador 5 | 3-2 | 08:35:36 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_Tristana | 0.8200 |  |
| Jogador 5 | 3-3 | 08:35:56 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_18_Tristana | 0.8400 |  |
| Jogador 5 | 3-3 | 08:35:57 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_18_Tristana | 0.5000 |  |
| Jogador 5 | 3-3 | 08:35:57 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_18_Tristana | -0.0600 |  |
| Jogador 5 | 3-3 | 08:35:58 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_18_Tristana | -0.2900 |  |
| Jogador 5 | 3-3 | 08:35:59 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_18_Tristana | -0.5000 |  |
| Jogador 5 | 3-3 | 08:35:59 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Enfeitiçador | DA_18_Tristana | -0.5700 |  |
| Jogador 5 | 3-3 | 08:36:00 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Enfeitiçador | DA_18_Tristana | -0.7900 |  |
| Jogador 5 | 3-3 | 08:36:01 | MOVE Bench -> Board: Karma (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Enfeitiçador | DA_18_Tristana | 0.0200 |  |
| Jogador 5 | 3-3 | 08:36:01 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Enfeitiçador | DA_18_Yunara | -0.1200 |  |
| Jogador 5 | 3-4 | 08:36:21 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Enfeitiçador | DA_18_Yunara | 0.7300 |  |
| Jogador 5 | 3-4 | 08:36:22 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_18_Yunara | 0.3300 |  |
| Jogador 5 | 3-4 | 08:36:23 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Enfeitiçador | DA_CrimsonRaptor18 | 0.1100 |  |
| Jogador 5 | 3-4 | 08:36:23 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Enfeitiçador | DA_CrimsonRaptor18 | -0.1800 |  |
| Jogador 5 | 3-4 | 08:36:24 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Enfeitiçador | DA_CrimsonRaptor18 | -0.2600 |  |
| Jogador 5 | 3-4 | 08:36:25 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_18_Yunara | -0.4000 |  |
| Jogador 5 | 3-4 | 08:36:25 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Enfeitiçador | DA_18_Yunara | -0.6300 |  |
| Jogador 5 | 3-4 | 08:36:26 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Enfeitiçador | DA_18_Yunara | -0.7900 |  |
| Jogador 5 | 3-4 | 08:36:27 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Enfeitiçador | DA_18_Yunara | -0.8800 |  |
| Jogador 5 | 3-5 | 08:36:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Enfeitiçador | DA_18_Yunara | 0.1000 |  |
| Jogador 5 | 3-5 | 08:36:48 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Enfeitiçador | DA_18_Yunara | 0.0300 |  |
| Jogador 5 | 3-5 | 08:36:49 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Enfeitiçador | DA_18_Yunara | -0.2600 |  |
| Jogador 5 | 3-5 | 08:36:50 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Yunara | -0.4000 |  |
| Jogador 5 | 3-5 | 08:36:50 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Enfeitiçador | DA_18_Yunara | -0.3300 |  |
| Jogador 5 | 3-5 | 08:36:52 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Enfeitiçador | DA_18_Yunara | -0.4000 |  |
| Jogador 5 | 3-5 | 08:36:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Enfeitiçador | DA_18_Yunara | -0.2300 |  |
| Jogador 5 | 3-5 | 08:36:53 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Enfeitiçador | DA_18_Yunara | -0.3400 |  |
| Jogador 5 | 3-6 | 08:37:06 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Enfeitiçador | DA_18_Yunara | 0.4100 |  |
| Jogador 5 | 3-6 | 08:37:06 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_18_Yunara | 0.0400 |  |
| Jogador 5 | 3-6 | 08:37:07 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Enfeitiçador | DA_18_Yunara | -0.0300 |  |
| Jogador 5 | 3-6 | 08:37:08 | MOVE Bench -> Board: Vi (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Enfeitiçador | DA_18_Yunara | -0.3900 |  |
| Jogador 5 | 3-6 | 08:37:08 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_18_Yunara | -0.3500 |  |
| Jogador 5 | 3-6 | 08:37:09 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_Vi18 | -0.5000 |  |
| Jogador 5 | 3-6 | 08:37:10 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_Vi18 | -0.0200 |  |
| Jogador 5 | 3-6 | 08:37:10 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_Vi18 | -0.3500 |  |
| Jogador 5 | 3-6 | 08:37:11 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_Vi18 | -0.2500 |  |
| Jogador 5 | 3-7 | 08:37:24 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Enfeitiçador | DA_Vi18 | 0.9900 |  |
| Jogador 5 | 3-7 | 08:37:25 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 70 | 5 | Enfeitiçador | DA_Vi18 | 0.4200 |  |
| Jogador 5 | 3-7 | 08:37:26 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Enfeitiçador | DA_Vi18 | 0.1200 |  |
| Jogador 5 | 3-7 | 08:37:27 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Enfeitiçador | DA_Vi18 | 0.1400 |  |
| Jogador 5 | 3-7 | 08:37:27 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Enfeitiçador | DA_Vi18 | 0.1300 |  |
| Jogador 5 | 3-7 | 08:37:28 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_Vi18 | -0.1700 |  |
| Jogador 5 | 3-7 | 08:37:29 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Enfeitiçador | DA_Vi18 | -0.0300 |  |
| Jogador 5 | 3-7 | 08:37:29 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_Vi18 | -0.2700 |  |
| Jogador 5 | 4-1 | 08:37:45 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Enfeitiçador | DA_Vi18 | 0.8600 |  |
| Jogador 5 | 4-2 | 08:38:12 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Enfeitiçador | DA_Vi18 | 0.9600 |  |
| Jogador 5 | 4-2 | 08:38:12 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Enfeitiçador | DA_Vi18 | 0.2500 |  |
| Jogador 5 | 4-2 | 08:38:13 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Enfeitiçador | DA_Vi18 | 0.5600 |  |
| Jogador 5 | 4-2 | 08:38:14 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 79 | 5 | Enfeitiçador | DA_Vi18 | -0.0700 |  |
| Jogador 5 | 4-2 | 08:38:15 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Enfeitiçador | DA_Vi18 | -0.5900 |  |
| Jogador 5 | 4-2 | 08:38:16 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Karma (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Enfeitiçador | DA_Vi18 | 0.1500 |  |
| Jogador 5 | 4-2 | 08:38:17 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Karma (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Enfeitiçador | DA_Vi18 | 0.1300 |  |
| Jogador 5 | 4-2 | 08:38:17 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 80 | 5 | Enfeitiçador | DA_Vi18 | -0.0100 |  |
| Jogador 5 | 4-3 | 08:38:33 | VENDEU: Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Enfeitiçador | DA_Vi18 | 0.0200 |  |
| Jogador 5 | 4-3 | 08:38:33 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Enfeitiçador | DA_Vi18 | 0.4800 |  |
| Jogador 5 | 4-3 | 08:38:35 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Enfeitiçador | DA_Vi18 | -0.0200 |  |
| Jogador 5 | 4-3 | 08:38:36 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Enfeitiçador | DA_Vi18 | 0.3800 |  |
| Jogador 5 | 4-3 | 08:38:37 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Enfeitiçador | DA_Vi18 | -0.0300 |  |
| Jogador 5 | 4-3 | 08:38:37 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Enfeitiçador | DA_Vi18 | 0.0900 |  |
| Jogador 5 | 4-4 | 08:38:54 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Enfeitiçador | DA_Vi18 | -0.0300 |  |
| Jogador 5 | 4-4 | 08:38:55 | COMPROU: Kobuko (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Enfeitiçador | DA_Vi18 | 0.9000 |  |
| Jogador 5 | 4-4 | 08:38:56 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Enfeitiçador | DA_Vi18 | -0.0700 |  |
| Jogador 5 | 4-5 | 08:39:27 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Enfeitiçador | DA_Vi18 | 1.0300 |  |
| Jogador 5 | 4-5 | 08:39:27 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Enfeitiçador | DA_Vi18 | -0.5900 |  |
| Jogador 5 | 4-5 | 08:39:28 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Enfeitiçador | DA_Vi18 | 0.0500 |  |
| Jogador 5 | 4-5 | 08:39:29 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Enfeitiçador | DA_Vi18 | -0.0100 |  |
| Jogador 5 | 4-5 | 08:39:30 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Enfeitiçador | DA_Vi18 | -0.2100 |  |
| Jogador 5 | 4-5 | 08:39:32 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Enfeitiçador | DA_Vi18 | -0.0100 |  |
| Jogador 5 | 4-6 | 08:39:50 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Enfeitiçador | DA_Vi18 | 0.9200 |  |
| Jogador 5 | 4-6 | 08:39:50 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Enfeitiçador | DA_Vi18 | -0.0200 |  |
| Jogador 5 | 4-7 | 08:40:25 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Enfeitiçador | DA_Vi18 | 0.7600 |  |
| Jogador 5 | 4-7 | 08:40:26 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Enfeitiçador | DA_Vi18 | 0.2100 |  |
| Jogador 5 | 4-7 | 08:40:27 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Kobuko (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Enfeitiçador | DA_Vi18 | 0.1700 |  |
| Jogador 5 | 4-7 | 08:40:27 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Enfeitiçador | DA_Vi18 | -0.7700 |  |
| Jogador 5 | 4-7 | 08:40:28 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Enfeitiçador | DA_Vi18 | 0.5900 |  |
| Jogador 5 | 4-7 | 08:40:30 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Enfeitiçador | DA_Vi18 | 0.0700 |  |
| Jogador 5 | 4-7 | 08:40:31 | VENDEU: Nidalee (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Enfeitiçador | DA_Vi18 | -0.0200 |  |
| Jogador 6 | ? | 08:32:45 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 08:32:47 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | -0.1500 |  |
| Jogador 6 | ? | 08:32:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 08:32:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 08:32:52 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 08:32:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 08:32:57 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2200 |  |
| Jogador 6 | 1-2 | 08:32:59 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 6 | 1-2 | 08:33:00 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 6 | 1-2 | 08:33:00 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 08:33:01 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 08:33:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-2 | 08:33:04 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.5700 |  |
| Jogador 6 | 1-3 | 08:33:08 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0300 |  |
| Jogador 6 | 1-3 | 08:33:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 08:33:16 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 6 | 1-4 | 08:33:17 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 6 | 1-4 | 08:33:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 6 | 1-4 | 08:33:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 08:33:22 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0900 |  |
| Jogador 6 | 2-1 | 08:33:25 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-1 | 08:33:25 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-1 | 08:33:26 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-1 | 08:33:27 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-1 | 08:33:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 08:33:36 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-2 | 08:33:37 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-2 | 08:33:38 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-2 | 08:33:39 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-2 | 08:33:39 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 08:33:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 08:33:50 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-3 | 08:33:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-3 | 08:33:51 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | 0.8100 |  |
| Jogador 6 | 2-3 | 08:33:51 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 08:33:52 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-3 | 08:33:53 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-3 | 08:33:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 08:33:54 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-3 | 08:33:55 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-4 | 08:34:06 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | 0.8600 |  |
| Jogador 6 | 2-4 | 08:34:07 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-4 | 08:34:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 08:34:08 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | -0.4500 |  |
| Jogador 6 | 2-4 | 08:34:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 08:34:09 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | -0.4900 |  |
| Jogador 6 | 2-4 | 08:34:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 6 | 2-4 | 08:34:10 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.2100 |  |
| Jogador 6 | 2-4 | 08:34:11 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Yorick | -0.6300 |  |
| Jogador 6 | 2-5 | 08:34:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 2-5 | 08:34:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 6 | 2-5 | 08:34:25 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Yorick | -0.1900 |  |
| Jogador 6 | 2-5 | 08:34:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | -0.0600 |  |
| Jogador 6 | 2-5 | 08:34:26 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | 0.0100 |  |
| Jogador 6 | 2-5 | 08:34:27 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Yorick | -1.0200 |  |
| Jogador 6 | 2-5 | 08:34:28 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.1600 |  |
| Jogador 6 | 2-5 | 08:34:28 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.6000 |  |
| Jogador 6 | 2-5 | 08:34:29 | MOVE Board -> Board: Rakan (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 2-6 | 08:34:44 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 6 | 2-6 | 08:34:44 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 6 | 2-6 | 08:34:45 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 6 | 2-6 | 08:34:45 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 6 | 2-6 | 08:34:46 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Xayah | -0.1600 |  |
| Jogador 6 | 2-6 | 08:34:47 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Xayah | -0.4900 |  |
| Jogador 6 | 2-6 | 08:34:48 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Xayah | 0.1100 |  |
| Jogador 6 | 2-6 | 08:34:48 | MOVE Board -> Board: Cascalho (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 2-6 | 08:34:49 | MOVE Board -> Board: Cascalho (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 2-7 | 08:35:05 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 6 | 2-7 | 08:35:06 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 6 | 2-7 | 08:35:06 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.2400 |  |
| Jogador 6 | 2-7 | 08:35:07 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | -0.1900 |  |
| Jogador 6 | 2-7 | 08:35:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 2-7 | 08:35:09 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 6 | 2-7 | 08:35:10 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 6 | 2-7 | 08:35:11 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 6 | 3-1 | 08:35:21 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_Fiddlesticks18 | 0.8400 |  |
| Jogador 6 | 3-1 | 08:35:21 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.8200 |  |
| Jogador 6 | 3-1 | 08:35:22 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.1900 |  |
| Jogador 6 | 3-1 | 08:35:23 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.3200 |  |
| Jogador 6 | 3-1 | 08:35:23 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 6 | 3-1 | 08:35:24 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-1 | 08:35:25 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-1 | 08:35:26 | MOVE Bench -> Board: Ahri (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | 0.4100 |  |
| Jogador 6 | 3-2 | 08:35:36 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.2800 |  |
| Jogador 6 | 3-3 | 08:35:56 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_Fiddlesticks18 | 0.2000 |  |
| Jogador 6 | 3-3 | 08:35:57 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | 0.2800 |  |
| Jogador 6 | 3-3 | 08:35:57 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.2600 |  |
| Jogador 6 | 3-3 | 08:35:58 | MOVE Board -> Board: Ahri (i:8.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-3 | 08:35:59 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 3-3 | 08:35:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-4 | 08:36:21 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 6 | 3-4 | 08:36:22 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 6 | 3-4 | 08:36:23 | MOVE Board -> Board: Yorick (i:2.0) <-> Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-4 | 08:36:23 | MOVE Board -> Board: Ahri (i:8.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 3-4 | 08:36:24 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 6 | 3-4 | 08:36:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-5 | 08:36:48 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_Fiddlesticks18 | -0.2900 |  |
| Jogador 6 | 3-5 | 08:36:48 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_Fiddlesticks18 | 0.7000 |  |
| Jogador 6 | 3-5 | 08:36:49 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_Fiddlesticks18 | 0.1600 |  |
| Jogador 6 | 3-5 | 08:36:50 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 6 | 3-5 | 08:36:50 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 6 | 3-5 | 08:36:52 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_Fiddlesticks18 | 0.5000 |  |
| Jogador 6 | 3-5 | 08:36:53 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 6 | 3-5 | 08:36:53 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 6 | 3-6 | 08:37:06 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 3-6 | 08:37:06 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-6 | 08:37:07 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 6 | 3-6 | 08:37:08 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-6 | 08:37:08 | VENDEU: Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Feérico | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 6 | 3-6 | 08:37:09 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Feérico | DA_Fiddlesticks18 | -0.5100 |  |
| Jogador 6 | 3-6 | 08:37:10 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 6 | 3-6 | 08:37:10 | MOVE Board -> Board: Yorick (i:2.0) <-> Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-6 | 08:37:11 | MOVE Board -> Board: Ahri (i:8.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-7 | 08:37:24 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 6 | 3-7 | 08:37:25 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_Fiddlesticks18 | 0.2500 |  |
| Jogador 6 | 3-7 | 08:37:26 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_Fiddlesticks18 | 0.2500 |  |
| Jogador 6 | 3-7 | 08:37:27 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Feérico | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 6 | 3-7 | 08:37:27 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 6 | 3-7 | 08:37:28 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 6 | 3-7 | 08:37:29 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 6 | 3-7 | 08:37:29 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_Fiddlesticks18 | -0.3700 |  |
| Jogador 6 | 4-1 | 08:37:45 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Feérico | DA_Fiddlesticks18 | 0.4300 |  |
| Jogador 6 | 4-2 | 08:38:12 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Feérico | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 6 | 4-2 | 08:38:12 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Feérico | DA_Fiddlesticks18 | 0.0400 |  |
| Jogador 6 | 4-2 | 08:38:13 | MOVE Board -> Board: Tristana (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 4-2 | 08:38:14 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 4-2 | 08:38:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Feérico | DA_Fiddlesticks18 | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-3 | 08:38:33 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Feérico | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 4-3 | 08:38:33 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_Fiddlesticks18 | 0.3700 |  |
| Jogador 6 | 4-3 | 08:38:35 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 4-3 | 08:38:36 | MOVE Board -> Board: Rakan (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 4-3 | 08:38:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 4-3 | 08:38:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_Fiddlesticks18 | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-4 | 08:38:54 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Feérico | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 4-4 | 08:38:55 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Feérico | DA_Fiddlesticks18 | 0.0400 |  |
| Jogador 6 | 4-4 | 08:38:56 | MOVE Board -> Board: Tristana (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 4-5 | 08:39:27 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Feérico | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 6 | 4-5 | 08:39:27 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_Fiddlesticks18 | 0.8800 |  |
| Jogador 6 | 4-5 | 08:39:28 | MOVE Board -> Board: Xayah (i:2.0) <-> Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 4-5 | 08:39:29 | MOVE Board -> Board: Ahri (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 4-5 | 08:39:30 | MOVE Board -> Board: Tristana (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 4-5 | 08:39:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_Fiddlesticks18 | -0.1000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-6 | 08:39:50 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 4-6 | 08:39:50 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Feérico | DA_Fiddlesticks18 | 0.8900 |  |
| Jogador 6 | 4-7 | 08:40:25 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Xayah (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Feérico | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 6 | 4-7 | 08:40:26 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Xayah (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Feérico | DA_Fiddlesticks18 | 0.1600 |  |
| Jogador 6 | 4-7 | 08:40:27 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Feérico | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 6 | 4-7 | 08:40:27 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Feérico | DA_18_Diana | 1.0100 |  |
| Jogador 6 | 4-7 | 08:40:28 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Feérico | DA_18_Diana | 0.3500 |  |
| Jogador 6 | 4-7 | 08:40:30 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 77 | 5 | Feérico | DA_18_Diana | -0.0200 |  |
| Jogador 6 | 4-7 | 08:40:31 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 77 | 5 | Feérico | DA_18_Diana | 0.0000 |  |
| Jogador 6 | 5-1 | 08:40:49 | VENDEU: Diana (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 95 | 5 | Feérico | DA_18_Rakan | -0.6000 |  |
| Jogador 6 | 5-2 | 08:41:26 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Feérico | DA_18_Rakan | 0.9400 |  |
| Jogador 6 | 5-2 | 08:41:27 | VENDEU: Kayle (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 5-2 | 08:41:28 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Feérico | DA_18_Rakan | 1.0500 |  |
| Jogador 6 | 5-2 | 08:41:29 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rakan (i:4.0) (tabuleiro slot 26) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Feérico | DA_18_Rakan | 0.1100 |  |
| Jogador 6 | 5-2 | 08:41:30 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Rakan (i:4.0) (tabuleiro slot 26) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Feérico | DA_18_Rakan | 0.1100 |  |
| Jogador 6 | 5-2 | 08:41:31 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Feérico | DA_18_Rakan | 0.2900 |  |
| Jogador 6 | 5-3 | 08:41:52 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Feérico | DA_18_Rakan | 0.5900 |  |
| Jogador 6 | 5-3 | 08:41:53 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Tristana (i:6.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Feérico | DA_18_Rakan | 0.1600 |  |
| Jogador 6 | 5-4 | 08:42:30 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Feérico | DA_18_Rakan | 0.3800 |  |
| Jogador 6 | 5-4 | 08:42:31 | MOVE Board -> Board: Ahri (i:8.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 5-4 | 08:42:32 | MOVE Board -> Board: Tristana (i:6.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 5-4 | 08:42:33 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Feérico | DA_18_Rakan | -0.5200 |  |
| Jogador 6 | 5-5 | 08:42:57 | VENDEU: Xayah (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Feérico | DA_18_Rakan | -0.7200 |  |
| Jogador 6 | 5-5 | 08:42:58 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Feérico | DA_18_Rakan | 0.9000 |  |
| Jogador 6 | 5-6 | 08:43:41 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Ahri (i:8.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Feérico | DA_18_Rakan | 0.0900 |  |
| Jogador 6 | 5-6 | 08:43:42 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Ahri (i:8.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Feérico | DA_18_Rakan | 0.1300 |  |
| Jogador 6 | 5-6 | 08:43:43 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Ahri (i:8.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Feérico | DA_18_Rakan | 0.0900 |  |
| Jogador 6 | 5-6 | 08:43:44 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Feérico | DA_18_Rakan | -0.7200 |  |
| Jogador 6 | 5-6 | 08:43:45 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Feérico | DA_18_Rakan | 0.5300 |  |
| Jogador 6 | 5-6 | 08:43:46 | MOVE Board -> Board: Rakan (i:4.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 5-7 | 08:44:09 | EQUIP_FROM_INVENTORY: DA_18_EmblemSpellweaver -> Lillia (i:8.0) (banco slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 149 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 5-7 | 08:44:10 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Feérico | DA_18_Rakan | -0.7200 |  |
| Jogador 6 | 6-1 | 08:44:57 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 158 | 5 | Feérico | DA_18_Rakan | -0.0900 |  |
| Jogador 6 | 6-1 | 08:44:58 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 161 | 5 | Feérico | DA_18_Rakan | -0.0300 |  |
| Jogador 6 | 6-1 | 08:44:59 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 158 | 5 | Feérico | DA_18_Rakan | -0.0900 |  |
| Jogador 6 | 6-1 | 08:45:01 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 158 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | ? | 08:32:45 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 08:32:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 08:32:52 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 08:32:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 08:32:53 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-1 | 08:32:54 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-1 | 08:32:55 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 08:32:55 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 08:32:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 08:32:57 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 7 | 1-2 | 08:32:59 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 08:33:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 08:33:00 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 08:33:01 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 08:33:01 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 08:33:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 08:33:08 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-3 | 08:33:08 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-3 | 08:33:09 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 08:33:09 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2000 |  |
| Jogador 7 | 1-3 | 08:33:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 08:33:16 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8300 |  |
| Jogador 7 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-4 | 08:33:20 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 7 | 1-4 | 08:33:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 08:33:22 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4400 |  |
| Jogador 7 | 2-1 | 08:33:25 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 08:33:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-1 | 08:33:26 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 08:33:27 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 08:33:27 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 08:33:31 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6000 |  |
| Jogador 7 | 2-2 | 08:33:36 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-2 | 08:33:37 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.8400 |  |
| Jogador 7 | 2-2 | 08:33:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-3 | 08:33:50 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 7 | 2-3 | 08:33:50 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-3 | 08:33:51 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 7 | 2-3 | 08:33:51 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-3 | 08:33:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 7 | 2-3 | 08:33:53 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1200 |  |
| Jogador 7 | 2-3 | 08:33:53 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | -0.1800 |  |
| Jogador 7 | 2-3 | 08:33:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-3 | 08:33:55 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.5400 |  |
| Jogador 7 | 2-4 | 08:34:06 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | 0.3300 |  |
| Jogador 7 | 2-4 | 08:34:07 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | 0.3800 |  |
| Jogador 7 | 2-4 | 08:34:07 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Akali_AD | -0.3900 |  |
| Jogador 7 | 2-4 | 08:34:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-4 | 08:34:08 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | -0.5700 |  |
| Jogador 7 | 2-4 | 08:34:09 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | 0.0100 |  |
| Jogador 7 | 2-4 | 08:34:10 | MOVE Board -> Board: Akali (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Akali_AD | 0.0100 |  |
| Jogador 7 | 2-4 | 08:34:10 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | -0.0700 |  |
| Jogador 7 | 2-4 | 08:34:11 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Akali_AD | 0.4200 |  |
| Jogador 7 | 2-5 | 08:34:23 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | 0.3900 |  |
| Jogador 7 | 2-5 | 08:34:24 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | 0.3800 |  |
| Jogador 7 | 2-5 | 08:34:25 | MOVE Bench -> Board: Shen (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | -0.3700 |  |
| Jogador 7 | 2-5 | 08:34:26 | MOVE Board -> Board: Shen (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 2-5 | 08:34:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-5 | 08:34:29 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Akali_AD | 0.4100 |  |
| Jogador 7 | 2-6 | 08:34:44 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Akali_AD | -0.1600 |  |
| Jogador 7 | 2-6 | 08:34:44 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-6 | 08:34:45 | MOVE Board -> Board: Akali (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-6 | 08:34:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 7 | 2-6 | 08:34:46 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 2-6 | 08:34:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-7 | 08:35:05 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Inferno | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 2-7 | 08:35:06 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Inferno | DA_18_Akali_AD | 0.1100 |  |
| Jogador 7 | 2-7 | 08:35:06 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | -0.0400 |  |
| Jogador 7 | 2-7 | 08:35:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 2-7 | 08:35:08 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-7 | 08:35:09 | MOVE Board -> Board: Yorick (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 7 | 2-7 | 08:35:10 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 2-7 | 08:35:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 3-1 | 08:35:21 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Inferno | DA_18_Akali_AD | 0.5100 |  |
| Jogador 7 | 3-1 | 08:35:21 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_18_Akali_AD | 0.6700 |  |
| Jogador 7 | 3-1 | 08:35:22 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | -0.1000 |  |
| Jogador 7 | 3-1 | 08:35:23 | MOVE Board -> Board: Shen (i:4.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 3-1 | 08:35:23 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 3-1 | 08:35:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 3-2 | 08:35:36 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Akali_AD | 0.7200 |  |
| Jogador 7 | 3-3 | 08:35:56 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Inferno | DA_18_Akali_AD | 0.8200 |  |
| Jogador 7 | 3-3 | 08:35:57 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_18_Akali_AD | 0.8100 |  |
| Jogador 7 | 3-3 | 08:35:57 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 3-3 | 08:35:58 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 3-3 | 08:35:59 | MOVE Board -> Board: Rammus (i:6.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_18_Akali_AD | -0.0300 |  |
| Jogador 7 | 3-3 | 08:35:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-4 | 08:36:21 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 1 | Inferno | DA_18_Akali_AD | -0.5800 |  |
| Jogador 7 | 3-4 | 08:36:22 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_18_Akali_AD | 0.7900 |  |
| Jogador 7 | 3-4 | 08:36:23 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_18_Akali_AD | 0.0100 |  |
| Jogador 7 | 3-4 | 08:36:23 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 3-4 | 08:36:24 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 7 | 3-4 | 08:36:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_18_Akali_AD | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-5 | 08:36:48 | VENDEU: Lobo Trevoguari (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Inferno | DA_18_Akali_AD | -0.5800 |  |
| Jogador 7 | 3-5 | 08:36:48 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Inferno | DA_18_Akali_AD | 0.0200 |  |
| Jogador 7 | 3-5 | 08:36:49 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 3-5 | 08:36:50 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Inferno | DA_18_Akali_AD | 0.4900 |  |
| Jogador 7 | 3-5 | 08:36:50 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 3-5 | 08:36:52 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 7 | 3-5 | 08:36:53 | MOVE Board -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 3-5 | 08:36:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Inferno | DA_18_Akali_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-6 | 08:37:06 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 3-6 | 08:37:06 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Inferno | DA_Fiddlesticks18 | 0.8800 |  |
| Jogador 7 | 3-6 | 08:37:07 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Inferno | DA_Fiddlesticks18 | 0.2200 |  |
| Jogador 7 | 3-6 | 08:37:08 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Fiddlesticks18 | -0.2400 |  |
| Jogador 7 | 3-6 | 08:37:08 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-6 | 08:37:09 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 3-6 | 08:37:10 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-6 | 08:37:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Inferno | DA_Fiddlesticks18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-7 | 08:37:24 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Inferno | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 7 | 3-7 | 08:37:25 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Inferno | DA_Fiddlesticks18 | 0.1600 |  |
| Jogador 7 | 3-7 | 08:37:26 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 3 | Inferno | DA_18_Akali_AD | -0.5000 |  |
| Jogador 7 | 3-7 | 08:37:27 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 3 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 3-7 | 08:37:27 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 3 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 3-7 | 08:37:28 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 3 | Inferno | DA_18_Akali_AD | -0.0500 |  |
| Jogador 7 | 3-7 | 08:37:29 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 3 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 7 | 3-7 | 08:37:29 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 3 | Inferno | DA_18_Akali_AD | -0.2800 |  |
| Jogador 7 | 4-1 | 08:37:45 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Inferno | DA_18_Akali_AD | 0.0200 |  |
| Jogador 7 | 4-2 | 08:38:12 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Inferno | DA_18_Akali_AD | 0.8600 |  |
| Jogador 7 | 4-2 | 08:38:12 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 4-2 | 08:38:13 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Inferno | DA_18_Akali_AD | 0.3400 |  |
| Jogador 7 | 4-2 | 08:38:14 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Inferno | DA_18_Akali_AD | -0.0700 |  |
| Jogador 7 | 4-2 | 08:38:15 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Inferno | DA_18_Akali_AD | -0.1500 |  |
| Jogador 7 | 4-2 | 08:38:16 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 7 | 4-2 | 08:38:17 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Inferno | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 4-2 | 08:38:17 | REROLL | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Inferno | DA_18_Akali_AD | -0.1600 |  |
| Jogador 7 | 4-3 | 08:38:33 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Inferno | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 4-3 | 08:38:33 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Inferno | DA_18_Akali_AD | 0.4100 |  |
| Jogador 7 | 4-3 | 08:38:35 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Inferno | DA_18_Akali_AD | -0.5900 |  |
| Jogador 7 | 4-3 | 08:38:36 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 82 | 5 | Inferno | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 4-3 | 08:38:37 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Inferno | DA_18_Akali_AD | -0.0300 |  |
| Jogador 7 | 4-3 | 08:38:37 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Inferno | DA_18_Akali_AD | -0.0500 |  |
| Jogador 7 | 4-4 | 08:38:54 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 94 | 5 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 7 | 4-4 | 08:38:55 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 91 | 5 | Inferno | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 7 | 4-4 | 08:38:56 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Inferno | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 7 | 4-5 | 08:39:27 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 100 | 5 | Inferno | DA_KogMaw18_AD | 1.0100 |  |
| Jogador 7 | 4-5 | 08:39:27 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 98 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 4-5 | 08:39:28 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 95 | 5 | Inferno | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 4-5 | 08:39:29 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 95 | 5 | Inferno | DA_KogMaw18_AD | -0.7000 |  |
| Jogador 7 | 4-5 | 08:39:30 | MOVE Bench -> Board: Shen (i:4.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 95 | 5 | Inferno | DA_KogMaw18_AD | -0.3100 |  |
| Jogador 7 | 4-5 | 08:39:32 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 95 | 5 | Inferno | DA_KogMaw18_AD | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-6 | 08:39:50 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 103 | 5 | Inferno | DA_KogMaw18_AD | 0.3500 |  |
| Jogador 7 | 4-6 | 08:39:50 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Inferno | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 7 | 4-7 | 08:40:25 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Varus (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 112 | 5 | Inferno | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 7 | 4-7 | 08:40:26 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Varus (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 112 | 5 | Inferno | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 7 | 4-7 | 08:40:27 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 117 | 5 | Inferno | DA_KogMaw18_AD | -0.6000 |  |
| Jogador 7 | 4-7 | 08:40:27 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 115 | 5 | Inferno | DA_KogMaw18_AD | 0.8700 |  |
| Jogador 7 | 4-7 | 08:40:28 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 123 | 5 | Inferno | DA_18_Rakan | -0.6000 |  |
| Jogador 7 | 4-7 | 08:40:30 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 121 | 5 | Inferno | DA_18_Rakan | 0.3500 |  |
| Jogador 7 | 4-7 | 08:40:31 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 121 | 5 | Inferno | DA_18_Rakan | -0.2300 |  |
| Jogador 7 | 5-1 | 08:40:49 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 134 | 5 | Inferno | DA_18_Rakan | -0.0300 |  |
| Jogador 7 | 5-2 | 08:41:26 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 144 | 5 | Inferno | DA_18_Rakan | 1.0200 |  |
| Jogador 7 | 5-2 | 08:41:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 141 | 5 | Inferno | DA_18_Rakan | 0.4000 |  |
| Jogador 7 | 5-2 | 08:41:28 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 141 | 5 | Inferno | DA_18_Rakan | 0.3400 |  |
| Jogador 7 | 5-2 | 08:41:29 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 139 | 5 | Inferno | DA_18_Rakan | 0.1900 |  |
| Jogador 7 | 5-2 | 08:41:30 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 135 | 5 | Inferno | DA_18_Rakan | -0.2600 |  |
| Jogador 7 | 5-2 | 08:41:31 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 135 | 5 | Inferno | DA_18_Rakan | -0.2000 |  |
| Jogador 7 | 5-3 | 08:41:52 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 150 | 5 | Inferno | DA_18_Rakan | -0.6000 |  |
| Jogador 7 | 5-3 | 08:41:53 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 147 | 5 | Inferno | DA_18_Rakan | 0.7700 |  |
| Jogador 7 | 5-4 | 08:42:30 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 154 | 5 | Inferno | DA_18_Rakan | 0.1000 |  |
| Jogador 7 | 5-4 | 08:42:31 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 151 | 5 | Inferno | DA_18_Rakan | 0.0500 |  |
| Jogador 7 | 5-4 | 08:42:32 | MOVE Bench -> Board: Rammus (i:12.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 151 | 5 | Inferno | DA_18_Rakan | -0.7400 |  |
| Jogador 7 | 5-4 | 08:42:33 | MOVE Board -> Board: Rammus (i:12.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 151 | 5 | Inferno | DA_18_Rakan | -0.0100 |  |
| Jogador 7 | 5-4 | 08:42:34 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 151 | 5 | Inferno | DA_18_Rakan | -0.2000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 5-5 | 08:42:57 | VENDEU: Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 164 | 5 | Inferno | DA_18_Rakan | -0.0500 |  |
| Jogador 7 | 5-5 | 08:42:58 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 161 | 5 | Inferno | DA_18_Rakan | 0.9500 |  |
| Jogador 7 | 5-6 | 08:43:41 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Inferno | DA_18_Rakan | 0.0000 |  |
| Jogador 7 | 5-6 | 08:43:42 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 172 | 5 | Inferno | DA_18_Rakan | 0.6300 |  |
| Jogador 7 | 5-6 | 08:43:43 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Inferno | DA_18_Rakan | -0.0300 |  |
| Jogador 7 | 5-6 | 08:43:44 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 173 | 5 | Inferno | DA_18_Rakan | 0.4300 |  |
| Jogador 7 | 5-6 | 08:43:45 | VENDEU: Sett (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 177 | 5 | Inferno | DA_18_Rakan | 0.0100 |  |
| Jogador 7 | 5-6 | 08:43:46 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Inferno | DA_18_Rakan | 0.0600 |  |
| Jogador 7 | 5-7 | 08:44:09 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Aronguejo (i:4.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 186 | 5 | Inferno | DA_18_Rakan | 0.0900 |  |
| Jogador 7 | 5-7 | 08:44:10 | VENDEU: Kayle (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Inferno | DA_18_Rakan | -0.0200 |  |
| Jogador 8 | ? | 08:32:45 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | ? | 08:32:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | ? | 08:32:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 08:32:52 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 08:32:52 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-1 | 08:32:53 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-1 | 08:32:54 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3600 |  |
| Jogador 8 | 1-1 | 08:32:55 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-1 | 08:32:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 08:32:57 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5000 |  |
| Jogador 8 | 1-2 | 08:32:59 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 8 | 1-2 | 08:33:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 8 | 1-2 | 08:33:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 08:33:08 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-3 | 08:33:08 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 8 | 1-3 | 08:33:09 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1700 |  |
| Jogador 8 | 1-3 | 08:33:09 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 8 | 1-3 | 08:33:11 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 8 | 1-3 | 08:33:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 08:33:16 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.1100 |  |
| Jogador 8 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 1-4 | 08:33:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 1-4 | 08:33:20 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 1-4 | 08:33:20 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 1.1000 |  |
| Jogador 8 | 1-4 | 08:33:21 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 1-4 | 08:33:22 | MOVE Bench -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.4100 |  |
| Jogador 8 | 2-1 | 08:33:25 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-1 | 08:33:25 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2100 |  |
| Jogador 8 | 2-1 | 08:33:26 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 2-1 | 08:33:27 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 2-1 | 08:33:27 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 2-1 | 08:33:31 | MOVE Board -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 2-2 | 08:33:36 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | 0.9800 |  |
| Jogador 8 | 2-2 | 08:33:37 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.0500 |  |
| Jogador 8 | 2-2 | 08:33:38 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.3700 |  |
| Jogador 8 | 2-2 | 08:33:39 | MOVE Bench -> Board: Teemo (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 2-2 | 08:33:39 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.5300 |  |
| Jogador 8 | 2-2 | 08:33:40 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.3000 |  |
| Jogador 8 | 2-2 | 08:33:40 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | -0.6300 |  |
| Jogador 8 | 2-2 | 08:33:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-3 | 08:33:50 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 2-3 | 08:33:50 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 2-3 | 08:33:51 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.7200 |  |
| Jogador 8 | 2-3 | 08:33:51 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.5100 |  |
| Jogador 8 | 2-3 | 08:33:52 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-3 | 08:33:53 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 2-3 | 08:33:53 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 2-3 | 08:33:54 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.4100 |  |
| Jogador 8 | 2-3 | 08:33:55 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-4 | 08:34:06 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_Karma18 | 0.9000 |  |
| Jogador 8 | 2-4 | 08:34:07 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_Karma18 | 0.8500 |  |
| Jogador 8 | 2-4 | 08:34:07 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 2-4 | 08:34:08 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 2-4 | 08:34:08 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-4 | 08:34:09 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_Karma18 | -0.0700 |  |
| Jogador 8 | 2-4 | 08:34:10 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-4 | 08:34:10 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_Karma18 | -0.4200 |  |
| Jogador 8 | 2-4 | 08:34:11 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 2-5 | 08:34:23 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_Karma18 | 0.9800 |  |
| Jogador 8 | 2-5 | 08:34:24 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_Karma18 | 0.2300 |  |
| Jogador 8 | 2-5 | 08:34:25 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Enfeitiçador | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 2-5 | 08:34:26 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-5 | 08:34:26 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 2-5 | 08:34:27 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_Karma18 | -0.3800 |  |
| Jogador 8 | 2-5 | 08:34:28 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_Karma18 | -0.4300 |  |
| Jogador 8 | 2-5 | 08:34:28 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Enfeitiçador | DA_Karma18 | -0.1400 |  |
| Jogador 8 | 2-5 | 08:34:29 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_Karma18 | -0.9400 |  |
| Jogador 8 | 2-6 | 08:34:44 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_Karma18 | 0.2700 |  |
| Jogador 8 | 2-6 | 08:34:44 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Enfeitiçador | DA_Karma18 | 0.1500 |  |
| Jogador 8 | 2-6 | 08:34:45 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Enfeitiçador | DA_Karma18 | 0.1000 |  |
| Jogador 8 | 2-6 | 08:34:45 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 2 | Enfeitiçador | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 2-6 | 08:34:46 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Enfeitiçador | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 2-6 | 08:34:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 2 | Enfeitiçador | DA_Karma18 | -0.1200 |  |
| Jogador 8 | 2-6 | 08:34:48 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 2 | Enfeitiçador | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 2-6 | 08:34:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 2 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-6 | 08:34:49 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 2 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-7 | 08:35:05 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-7 | 08:35:06 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_Karma18 | 0.2100 |  |
| Jogador 8 | 2-7 | 08:35:06 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_Karma18 | 0.1000 |  |
| Jogador 8 | 2-7 | 08:35:07 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Feérico | DA_Karma18 | 0.3900 |  |
| Jogador 8 | 2-7 | 08:35:08 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Feérico | DA_Karma18 | 0.2200 |  |
| Jogador 8 | 2-7 | 08:35:09 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Feérico | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 2-7 | 08:35:10 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Feérico | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 2-7 | 08:35:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 1 | Feérico | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-1 | 08:35:21 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-1 | 08:35:21 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_Karma18 | -0.1600 |  |
| Jogador 8 | 3-1 | 08:35:22 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 3-1 | 08:35:23 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 3-1 | 08:35:23 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 3-1 | 08:35:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_Karma18 | -0.2100 |  |
| Jogador 8 | 3-1 | 08:35:25 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-1 | 08:35:26 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 3-2 | 08:35:36 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-3 | 08:35:56 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Feérico | DA_Karma18 | 0.8200 |  |
| Jogador 8 | 3-3 | 08:35:57 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Feérico | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-3 | 08:35:57 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Feérico | DA_Karma18 | 0.7700 |  |
| Jogador 8 | 3-3 | 08:35:58 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Feérico | DA_Karma18 | -0.4100 |  |
| Jogador 8 | 3-3 | 08:35:59 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Feérico | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-3 | 08:35:59 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Feérico | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-3 | 08:36:00 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Feérico | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-3 | 08:36:01 | MOVE Board -> Board: Karma (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Feérico | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-3 | 08:36:01 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Feérico | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 3-4 | 08:36:21 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Feérico | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-4 | 08:36:22 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Feérico | DA_Karma18 | 0.7700 |  |
| Jogador 8 | 3-4 | 08:36:23 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Feérico | DA_Karma18 | -0.8100 |  |
| Jogador 8 | 3-4 | 08:36:23 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Feérico | DA_Karma18 | 0.8500 |  |
| Jogador 8 | 3-4 | 08:36:24 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_Karma18 | 0.3600 |  |
| Jogador 8 | 3-4 | 08:36:25 | MOVE Bench -> Board: Karma (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 3-4 | 08:36:25 | VENDEU: Sejuani (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Feérico | DA_Karma18 | -0.5400 |  |
| Jogador 8 | 3-4 | 08:36:26 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Feérico | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 3-4 | 08:36:27 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Feérico | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 3-5 | 08:36:48 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Feérico | DA_Karma18 | 0.5200 |  |
| Jogador 8 | 3-5 | 08:36:48 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Feérico | DA_Karma18 | 0.2300 |  |
| Jogador 8 | 3-5 | 08:36:49 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Feérico | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 3-5 | 08:36:50 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Feérico | DA_18_Cassiopeia | 0.6500 |  |
| Jogador 8 | 3-5 | 08:36:50 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Feérico | DA_18_Cassiopeia | 0.2800 |  |
| Jogador 8 | 3-5 | 08:36:52 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Feérico | DA_18_Cassiopeia | 0.0500 |  |
| Jogador 8 | 3-5 | 08:36:53 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 3 | Feérico | DA_18_Cassiopeia | -0.2100 |  |
| Jogador 8 | 3-5 | 08:36:53 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 3 | Feérico | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 8 | 3-6 | 08:37:06 | VENDEU: Cassiopeia (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Feérico | DA_18_Xayah | 0.0200 |  |
| Jogador 8 | 3-6 | 08:37:06 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Feérico | DA_18_Xayah | 0.3300 |  |
| Jogador 8 | 3-6 | 08:37:07 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Feérico | DA_18_Xayah | -0.0300 |  |
| Jogador 8 | 3-6 | 08:37:08 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Feérico | DA_18_Xayah | -0.2400 |  |
| Jogador 8 | 3-6 | 08:37:08 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Feérico | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 3-6 | 08:37:09 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Feérico | DA_18_Xayah | -0.2700 |  |
| Jogador 8 | 3-6 | 08:37:10 | MOVE Board -> Board: Karma (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Feérico | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 3-6 | 08:37:10 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Feérico | DA_18_Xayah | -0.0300 |  |
| Jogador 8 | 3-6 | 08:37:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Feérico | DA_18_Xayah | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-7 | 08:37:24 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Feérico | DA_18_Xayah | 0.2500 |  |
| Jogador 8 | 3-7 | 08:37:25 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Feérico | DA_18_Xayah | 0.2500 |  |
| Jogador 8 | 3-7 | 08:37:26 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Feérico | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 3-7 | 08:37:27 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Feérico | DA_18_Xayah | 0.8400 |  |
| Jogador 8 | 3-7 | 08:37:27 | VENDEU: Malphite (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 4 | Feérico | DA_18_Xayah | -0.0200 |  |
| Jogador 8 | 3-7 | 08:37:28 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Feérico | DA_18_Xayah | 0.1000 |  |
| Jogador 8 | 3-7 | 08:37:29 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 4 | Feérico | DA_18_Xayah | -0.0500 |  |
| Jogador 8 | 3-7 | 08:37:29 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Feérico | DA_18_Xayah | -0.0900 |  |
| Jogador 8 | 4-1 | 08:37:45 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Feérico | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 4-2 | 08:38:12 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Feérico | DA_18_Xayah | 0.9000 |  |
| Jogador 8 | 4-2 | 08:38:12 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Feérico | DA_18_Xayah | -0.5900 |  |
| Jogador 8 | 4-2 | 08:38:13 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Feérico | DA_18_Xayah | 0.6500 |  |
| Jogador 8 | 4-2 | 08:38:14 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Feérico | DA_18_Xayah | -0.5100 |  |
| Jogador 8 | 4-2 | 08:38:15 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Feérico | DA_18_Xayah | 0.0300 |  |
| Jogador 8 | 4-2 | 08:38:16 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Feérico | DA_18_Xayah | -0.0300 |  |
| Jogador 8 | 4-2 | 08:38:17 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Feérico | DA_18_Xayah | -0.2800 |  |
| Jogador 8 | 4-2 | 08:38:17 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Feérico | DA_18_Xayah | 0.0100 |  |
| Jogador 8 | 4-3 | 08:38:33 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Feérico | DA_18_Xayah | 0.8800 |  |
| Jogador 8 | 4-3 | 08:38:33 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Feérico | DA_18_Xayah | -0.6000 |  |
| Jogador 8 | 4-3 | 08:38:35 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Feérico | DA_18_Xayah | 0.4100 |  |
| Jogador 8 | 4-3 | 08:38:36 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Feérico | DA_18_Xayah | -0.5900 |  |
| Jogador 8 | 4-3 | 08:38:37 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Feérico | DA_18_Xayah | 0.6500 |  |
| Jogador 8 | 4-3 | 08:38:37 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Feérico | DA_18_Xayah | -0.5100 |  |
| Jogador 8 | 4-4 | 08:38:54 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Feérico | DA_18_Tristana | 0.9600 |  |
| Jogador 8 | 4-4 | 08:38:55 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Feérico | DA_18_Tristana | 0.9600 |  |
| Jogador 8 | 4-4 | 08:38:56 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Feérico | DA_18_Tristana | 0.1500 |  |
| Jogador 8 | 4-5 | 08:39:27 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 8 | 4-5 | 08:39:27 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 8 | 4-5 | 08:39:28 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Feérico | DA_18_Tristana | -0.0500 |  |
| Jogador 8 | 4-5 | 08:39:29 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Feérico | DA_18_Tristana | -0.5900 |  |
| Jogador 8 | 4-5 | 08:39:30 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Xayah (i:4.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Feérico | DA_18_Tristana | 0.1300 |  |
| Jogador 8 | 4-5 | 08:39:32 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Mamãe Bicuda (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Feérico | DA_18_Tristana | 0.1600 |  |
| Jogador 8 | 4-6 | 08:39:50 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-6 | 08:39:50 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Mamãe Bicuda (i:6.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Feérico | DA_18_Tristana | 0.1200 |  |
| Jogador 8 | 4-7 | 08:40:25 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Feérico | DA_18_Tristana | 0.1600 |  |
| Jogador 8 | 4-7 | 08:40:26 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NegatronCloak -> LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Feérico | DA_18_Tristana | 0.0900 |  |
| Jogador 8 | 4-7 | 08:40:27 | VENDEU: Tristana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Feérico | DA_18_Xayah | -0.7000 |  |
| Jogador 8 | 4-7 | 08:40:27 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Feérico | DA_CrimsonRaptor18 | 1.0500 |  |
| Jogador 8 | 4-7 | 08:40:28 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Feérico | DA_CrimsonRaptor18 | 0.1500 |  |
| Jogador 8 | 4-7 | 08:40:30 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Feérico | DA_CrimsonRaptor18 | 0.0400 |  |
| Jogador 8 | 4-7 | 08:40:31 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Feérico | DA_CrimsonRaptor18 | -0.1000 |  |
| Jogador 8 | 5-1 | 08:40:49 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Feérico | DA_CrimsonRaptor18 | 0.9200 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 36 | 36 | 180 | 36 | 20 | 196 | 9 | 30 |
| Jogador 2 | 34 | 34 | 170 | 34 | 19 | 189 | 4 | 43 |
| Jogador 3 | 36 | 36 | 180 | 36 | 17 | 175 | 3 | 42 |
| Jogador 4 | 21 | 21 | 105 | 21 | 13 | 127 | 7 | 12 |
| Jogador 5 | 26 | 26 | 130 | 26 | 16 | 161 | 12 | 19 |
| Jogador 6 | 34 | 34 | 170 | 34 | 19 | 179 | 12 | 36 |
| Jogador 7 | 33 | 34 | 170 | 33 | 17 | 174 | 6 | 41 |
| Jogador 8 | 27 | 27 | 135 | 27 | 17 | 170 | 9 | 27 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 196 | 196 | 196 | 0 | 183 | 0 | 196 | 196 | 196 | 69/55 |
| Jogador 2 | 189 | 189 | 189 | 0 | 179 | 0 | 189 | 189 | 189 | 75/61 |
| Jogador 3 | 175 | 175 | 175 | 0 | 167 | 0 | 175 | 175 | 175 | 43/26 |
| Jogador 4 | 127 | 127 | 127 | 0 | 119 | 0 | 127 | 127 | 127 | 39/25 |
| Jogador 5 | 161 | 161 | 161 | 0 | 152 | 0 | 161 | 161 | 161 | 71/57 |
| Jogador 6 | 179 | 179 | 179 | 0 | 163 | 0 | 179 | 179 | 179 | 61/46 |
| Jogador 7 | 174 | 174 | 174 | 0 | 166 | 0 | 174 | 174 | 174 | 65/51 |
| Jogador 8 | 170 | 170 | 170 | 0 | 160 | 0 | 170 | 170 | 170 | 77/63 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.20922301709651947 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.25060486793518066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23841141164302826 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22248587012290955 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013312771916389465 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.425262987613678 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3475426137447357 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25197887420654297 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 28 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0387523174285889 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.031599998474121 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 39 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9796043038368225 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 49 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19132192432880402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 50 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17696425318717957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 51 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 52 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3995053470134735 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 56 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3355602025985718 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 57 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13008219003677368 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 2-2 | 58 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06002999469637871 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2757655084133148 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00807955488562584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 63 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3531228005886078 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 64 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 65 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1717279553413391 | 0.0 | 0.0 | +— / -73185d11-22d3-4a1d-803a-b37e82272098 |
| Jogador 1 | 2-3 | 66 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33252114057540894 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 67 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15526708960533142 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 1 | 2-3 | 68 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.173170804977417 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 2-3 | 69 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 70 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 72 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1169931888580322 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-4 | 73 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36417657136917114 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5049320459365845 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 75 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19668835401535034 | 0.0 | 0.0 | +7d8f4f6b-4eba-4c31-9834-bd81a3765520 / -— |
| Jogador 1 | 2-4 | 76 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0393141470849514 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 77 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 78 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03789299353957176 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 79 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006453205365687609 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 80 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014428871683776379 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 82 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30881351232528687 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 83 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | Adaptador/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3666594326496124 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 84 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | Adaptador/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 1 | 2-5 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 87 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01502055861055851 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 88 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 92 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 14.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479974746704102 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 93 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 12.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06610375642776489 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 94 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 3 | 0 | 12.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14949822425842285 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 95 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 16.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030748676508665085 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 16.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 97 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 16.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4176774024963379 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 98 | PASS | STABILIZE | 95.0 | 6 | 0 | 0 | 20.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 100 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 20.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6017404198646545 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 102 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9789759516716003 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 103 | BUY | STABILIZE | 95.0 | 6 | 5 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.04115891456604 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-7 | 104 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 4 | 0 | 20.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007588506676256657 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 105 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1304018795490265 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 106 | BUY | STABILIZE | 95.0 | 6 | 4 | 0 | 22.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3365703821182251 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 1 | 2-7 | 107 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 2 | 0 | 22.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05657071992754936 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 108 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5894687175750732 | 0.0 | 0.0 | +— / -2a286030-5984-44b5-87ff-6c948d2e672e |
| Jogador 1 | 2-7 | 109 | EQUIP_FROM_INVENTORY | STABILIZE | 95.0 | 6 | 5 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14694786071777344 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 110 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 5 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.574645459651947 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 112 | BUY | STABILIZE | 95.0 | 6 | 11 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | True | 0.5017793774604797 | 0.0 | 0.0 | +8980fd33-79c8-4825-95e9-9298680cbc6d / -— |
| Jogador 1 | 3-1 | 113 | EQUIP_FROM_INVENTORY | STABILIZE | 95.0 | 6 | 9 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.14553649723529816 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 114 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 6 | 9 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2469826638698578 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 115 | BUY | STABILIZE | 95.0 | 6 | 9 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2821922302246094 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 116 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 6 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047905001789331436 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 117 | BUY_XP | STABILIZE | 95.0 | 6 | 6 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 118 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 119 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09743154793977737 | 0.0 | 0.0 | +— / -cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 3-2 | 121 | BUY | STABILIZE | 85.0 | 6 | 8 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6451061964035034 | 0.0 | 0.0 | +5204a655-be8f-4607-8fa3-28c981ac1397 / -7d8f4f6b-4eba-4c31-9834-bd81a3765520,8980fd33-79c8-4825-95e9-9298680cbc6d |
| Jogador 1 | 3-2 | 122 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 6 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38527899980545044 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 123 | BUY | STABILIZE | 85.0 | 6 | 6 | 0 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28053149580955505 | 0.0 | 0.0 | +1e504283-c5d1-4eb3-915e-20533ec3a756 / -— |
| Jogador 1 | 3-2 | 124 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 5 | 0 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09601140022277832 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 125 | BUY_XP | STABILIZE | 85.0 | 6 | 5 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 126 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 1 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0031745308078825474 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 127 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 1 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01855708472430706 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 128 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 1 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3628235161304474 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 130 | MOVE_BENCH | STABILIZE | 74.0 | 6 | 7 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39861375093460083 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 132 | BUY | STABILIZE | 63.0 | 6 | 13 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07220908999443054 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 133 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 11 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24709226191043854 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 134 | SELL | STABILIZE | 63.0 | 6 | 11 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0963333323597908 | 0.0 | 0.0 | +— / -5204a655-be8f-4607-8fa3-28c981ac1397 |
| Jogador 1 | 3-4 | 135 | SELL | STABILIZE | 63.0 | 6 | 16 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06618645787239075 | 0.0 | 0.0 | +— / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 3-4 | 136 | BUY | STABILIZE | 63.0 | 6 | 19 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02293664589524269 | 0.0 | 0.0 | +0450963e-c7e2-4ff5-a2f5-09e65fa63527 / -— |
| Jogador 1 | 3-4 | 137 | BUY | STABILIZE | 63.0 | 6 | 17 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017659304663538933 | 0.0 | 0.0 | +7a60e1b2-fc20-4070-b163-2f9fb6f93264 / -— |
| Jogador 1 | 3-4 | 138 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 16 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0345458947122097 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 139 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 16 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03133685141801834 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 140 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 16 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016649635508656502 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 142 | BUY | STABILIZE | 63.0 | 6 | 23 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.779080331325531 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -— |
| Jogador 1 | 3-5 | 143 | BUY | STABILIZE | 63.0 | 6 | 21 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020322931930422783 | 0.0 | 0.0 | +a9184317-58b7-4804-9aef-3e2c08c20935 / -— |
| Jogador 1 | 3-5 | 144 | BUY | STABILIZE | 63.0 | 6 | 20 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3394581079483032 | 0.0 | 0.0 | +f6e6e08d-ecfe-4c84-acfa-6ad8292968ee / -— |
| Jogador 1 | 3-5 | 145 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 19 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14421811699867249 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 146 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 19 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12995602190494537 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 147 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 19 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01652541197836399 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 148 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 19 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016736330464482307 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 149 | PASS | STABILIZE | 63.0 | 6 | 19 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 152 | SELL | STABILIZE | 63.0 | 6 | 27 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002766009885817766 | 0.0 | 0.0 | +— / -7a60e1b2-fc20-4070-b163-2f9fb6f93264 |
| Jogador 1 | 3-6 | 153 | BUY | STABILIZE | 63.0 | 6 | 28 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2906942665576935 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 1 | 3-6 | 154 | SELL | STABILIZE | 63.0 | 6 | 24 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002022984903305769 | 0.0 | 0.0 | +— / -0450963e-c7e2-4ff5-a2f5-09e65fa63527 |
| Jogador 1 | 3-6 | 155 | BUY | STABILIZE | 63.0 | 6 | 26 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8364154100418091 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -9aa6122c-e49a-48a2-ba24-7adcd3b7cb56,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-6 | 156 | BUY | STABILIZE | 63.0 | 6 | 24 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2864004373550415 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 157 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 22 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.085424780845642 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 158 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 22 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12333492934703827 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 159 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 22 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14466162025928497 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 161 | BUY | STABILIZE | 53.0 | 6 | 29 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8106130957603455 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 1 | 3-7 | 162 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 25 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05744922533631325 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 163 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 25 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3556048572063446 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 164 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 25 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3936632573604584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 165 | PASS | STABILIZE | 53.0 | 6 | 25 | 2 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02250000089406967 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 171 | CRAFT_AND_EQUIP | STABILIZE | 53.0 | 6 | 32 | 3 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2415591925382614 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 172 | CRAFT_AND_EQUIP | STABILIZE | 53.0 | 6 | 32 | 3 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2474905103445053 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 173 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 32 | 3 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21815960109233856 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 174 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 32 | 3 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33949100971221924 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 175 | PASS | STABILIZE | 53.0 | 6 | 32 | 3 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037142857909202576 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 180 | SELL | STABILIZE | 42.0 | 6 | 41 | 4 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5740444660186768 | 0.0 | 0.0 | +— / -d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 4-3 | 182 | BUY | STABILIZE | 30.0 | 6 | 56 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8416510820388794 | 0.0 | 0.0 | +ea460790-b046-451d-9174-8b613e476241 / -— |
| Jogador 1 | 4-3 | 183 | SELL | STABILIZE | 30.0 | 6 | 55 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4686794579029083 | 0.0 | 0.0 | +— / -a9184317-58b7-4804-9aef-3e2c08c20935 |
| Jogador 1 | 4-3 | 184 | BUY | STABILIZE | 30.0 | 6 | 56 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7793291211128235 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -— |
| Jogador 1 | 4-3 | 185 | SELL | STABILIZE | 30.0 | 6 | 54 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024457041174173355 | 0.0 | 0.0 | +— / -f6e6e08d-ecfe-4c84-acfa-6ad8292968ee |
| Jogador 1 | 4-3 | 186 | SELL | STABILIZE | 30.0 | 6 | 55 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5427414774894714 | 0.0 | 0.0 | +— / -3fc2815d-c456-47c3-bb27-783336b3cdfa |
| Jogador 1 | 4-3 | 187 | SELL | STABILIZE | 30.0 | 6 | 57 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5302110910415649 | 0.0 | 0.0 | +— / -7c218f01-e884-46da-8a1a-2d2db27a5ff1 |
| Jogador 1 | 4-3 | 188 | SELL | STABILIZE | 30.0 | 6 | 60 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9894465208053589 | 0.0 | 0.0 | +— / -1e504283-c5d1-4eb3-915e-20533ec3a756 |
| Jogador 1 | 4-3 | 189 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 61 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3658466935157776 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 191 | BUY | STABILIZE | 30.0 | 6 | 72 | 5 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00804933626204729 | 0.0 | 0.0 | +157648c2-e9b6-4eb2-b42c-19c554a3a41e / -— |
| Jogador 1 | 4-4 | 192 | BUY | STABILIZE | 30.0 | 6 | 70 | 5 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5124532580375671 | 0.0 | 0.0 | +fcd8f4bf-7e1f-42b3-a989-5b3683394c89 / -— |
| Jogador 1 | 4-4 | 193 | SELL | STABILIZE | 30.0 | 6 | 68 | 5 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8149333596229553 | 0.0 | 0.0 | +— / -157648c2-e9b6-4eb2-b42c-19c554a3a41e |
| Jogador 1 | 4-4 | 194 | SELL | STABILIZE | 30.0 | 6 | 70 | 5 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07559999823570251 | 0.0 | 0.0 | +— / -fcd8f4bf-7e1f-42b3-a989-5b3683394c89 |
| Jogador 1 | 4-4 | 195 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 72 | 5 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.046317435801029205 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 196 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 72 | 5 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07439292222261429 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 198 | BUY | STABILIZE | 30.0 | 6 | 82 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12010528892278671 | 0.0 | 0.0 | +ddae48a6-5360-4660-9fa1-143ac35635ee / -— |
| Jogador 1 | 4-5 | 199 | BUY | STABILIZE | 30.0 | 6 | 79 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12049870193004608 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 1 | 4-5 | 200 | BUY | STABILIZE | 30.0 | 6 | 75 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20568419992923737 | 0.0 | 0.0 | +5477420d-3b98-4863-b2e7-f414d3fa1f01 / -— |
| Jogador 1 | 4-6 | 202 | BUY | ALL_IN | 19.0 | 7 | 82 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0268305540084839 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -760d5bee-7d64-4f03-abf0-6357c914a1ed,b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 1 | 4-6 | 203 | MOVE_BENCH | ALL_IN | 19.0 | 7 | 80 | 5 | 20.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14705152809619904 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 204 | MOVE_BENCH | ALL_IN | 19.0 | 7 | 80 | 5 | 22.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39919015765190125 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 205 | MOVE_BENCH | ALL_IN | 19.0 | 7 | 80 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16853001713752747 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 206 | BUY | ALL_IN | 19.0 | 7 | 80 | 5 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2295132726430893 | 0.0 | 0.0 | +715d5bfc-c8c3-4dec-a247-9e07ee2755e8 / -— |
| Jogador 1 | 4-6 | 207 | MOVE_BENCH | ALL_IN | 19.0 | 7 | 77 | 5 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4033117890357971 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 209 | BUY | ALL_IN | 19.0 | 7 | 88 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9776180386543274 | 0.0 | 0.0 | +673bda2e-1343-4894-8005-c3ee2c90f1b7 / -— |
| Jogador 1 | 4-7 | 210 | BUY | ALL_IN | 19.0 | 7 | 85 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7757362723350525 | 0.0 | 0.0 | +565ff610-fe51-470b-8452-a7eec5e31653 / -— |
| Jogador 1 | 5-1 | 212 | CRAFT_AND_EQUIP | ALL_IN | 19.0 | 7 | 92 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17469331622123718 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 213 | CRAFT_AND_EQUIP | ALL_IN | 19.0 | 7 | 92 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09596114605665207 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 214 | SELL | ALL_IN | 19.0 | 7 | 92 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6933000087738037 | 0.0 | 0.0 | +— / -8aa832ec-4c09-43bd-ae21-baf7268e468d |
| Jogador 1 | 5-1 | 215 | BUY | ALL_IN | 19.0 | 7 | 97 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0513583421707153 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -673bda2e-1343-4894-8005-c3ee2c90f1b7,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 5-1 | 216 | BUY | ALL_IN | 19.0 | 7 | 94 | 5 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18878576159477234 | 0.0 | 0.0 | +de8de4b5-48ea-4947-ae08-2b90d94b0fc1 / -— |
| Jogador 1 | 5-1 | 217 | SELL | ALL_IN | 19.0 | 7 | 91 | 5 | 30.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6972000002861023 | 0.0 | 0.0 | +— / -24b29fe6-466c-42d5-9f92-5d6114f0f98f |
| Jogador 1 | 5-1 | 218 | MOVE_BENCH | ALL_IN | 19.0 | 7 | 99 | 5 | 30.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.40741416811943054 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 220 | BUY | ALL_IN | 19.0 | 7 | 111 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7864475846290588 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -— |
| Jogador 1 | 5-3 | 222 | BUY | ALL_IN | 19.0 | 7 | 120 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.5004542469978333 | 0.0 | 0.0 | +b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 / -— |
| Jogador 1 | 5-3 | 223 | EQUIP_FROM_INVENTORY | ALL_IN | 19.0 | 7 | 119 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05549825727939606 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 224 | EQUIP_FROM_INVENTORY | ALL_IN | 19.0 | 7 | 119 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08401928842067719 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 225 | EQUIP_FROM_INVENTORY | ALL_IN | 19.0 | 7 | 119 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05982113629579544 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 226 | SELL | ALL_IN | 19.0 | 7 | 119 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -5477420d-3b98-4863-b2e7-f414d3fa1f01 |
| Jogador 1 | 5-3 | 227 | BUY | ALL_IN | 19.0 | 7 | 122 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0471301078796387 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1,9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 |
| Jogador 1 | 5-4 | 229 | BUY | ALL_IN | 19.0 | 7 | 132 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9202480316162109 | 0.0 | 0.0 | +a899fe97-90e4-4ae3-941c-af3dee48fed3 / -— |
| Jogador 1 | 5-4 | 230 | BUY | ALL_IN | 19.0 | 7 | 131 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.700018048286438 | 0.0 | 0.0 | +af404167-469a-447e-b415-dcb52033ef9b / -— |
| Jogador 1 | 5-5 | 232 | SELL | ALL_IN | 19.0 | 7 | 140 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6919582486152649 | 0.0 | 0.0 | +— / -a5deb295-89d5-4573-8ace-e370a0718266 |
| Jogador 1 | 5-5 | 233 | BUY | ALL_IN | 19.0 | 7 | 145 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13841083645820618 | 0.0 | 0.0 | +a267d973-f857-4dda-89e1-209bff42ab6f / -— |
| Jogador 1 | 5-5 | 234 | MOVE_BOARD | ALL_IN | 19.0 | 7 | 140 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00025256103253923357 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 235 | MOVE_BOARD | ALL_IN | 19.0 | 7 | 140 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014806849882006645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 236 | PASS | ALL_IN | 19.0 | 7 | 140 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5664162635803223 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 239 | SELL | ALL_IN | 19.0 | 7 | 153 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -a267d973-f857-4dda-89e1-209bff42ab6f |
| Jogador 1 | 5-6 | 240 | BUY | ALL_IN | 19.0 | 7 | 158 | 5 | 36.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.048507809638977 | 0.0 | 0.0 | +f087511a-d834-4f41-9b99-00bf0f6dc061 / -a899fe97-90e4-4ae3-941c-af3dee48fed3,ea460790-b046-451d-9174-8b613e476241 |
| Jogador 1 | 5-7 | 242 | BUY | ALL_IN | 19.0 | 7 | 171 | 5 | 40.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0423942804336548 | 0.0 | 0.0 | +caeaaabc-213a-4018-97f3-8797a0711863 / -5a6985d6-5377-425c-b4a3-c53dc138b288,ddae48a6-5360-4660-9fa1-143ac35635ee |
| Jogador 1 | 5-7 | 243 | MOVE_BENCH | ALL_IN | 19.0 | 7 | 168 | 5 | 28.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2708810567855835 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 244 | BUY | ALL_IN | 19.0 | 7 | 168 | 5 | 34.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16818544268608093 | 0.0 | 0.0 | +3ae84928-bc2a-4c1e-8663-b7ad05da4501 / -— |
| Jogador 1 | 5-7 | 245 | BUY | ALL_IN | 19.0 | 7 | 165 | 5 | 34.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03825555369257927 | 0.0 | 0.0 | +b250e22d-7193-4ea5-879d-5c7b41145719 / -— |
| Jogador 1 | 5-7 | 246 | MOVE_BOARD | ALL_IN | 19.0 | 7 | 163 | 5 | 34.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.634839438542258e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 247 | MOVE_BENCH | ALL_IN | 19.0 | 7 | 163 | 5 | 34.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4847080707550049 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 249 | BUY | ALL_IN | 19.0 | 7 | 176 | 5 | 46.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9783428907394409 | 0.0 | 0.0 | +bdee5671-864a-47c9-9576-9e0d8d2a7c6a / -— |
| Jogador 1 | 6-1 | 250 | EQUIP_FROM_INVENTORY | ALL_IN | 19.0 | 7 | 173 | 5 | 46.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.057409193366765976 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 252 | SELL | ALL_IN | 19.0 | 7 | 187 | 5 | 46.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6906999945640564 | 0.0 | 0.0 | +— / -f087511a-d834-4f41-9b99-00bf0f6dc061 |
| Jogador 1 | 6-2 | 253 | BUY | ALL_IN | 19.0 | 7 | 190 | 5 | 46.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0804517269134521 | 0.0 | 0.0 | +63c47a3f-6712-4cfa-9376-6140da170089 / -— |
| Jogador 1 | 6-2 | 254 | SELL | ALL_IN | 19.0 | 7 | 189 | 5 | 46.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -b250e22d-7193-4ea5-879d-5c7b41145719 |
| Jogador 1 | 6-2 | 255 | BUY | ALL_IN | 19.0 | 7 | 191 | 5 | 46.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1108019351959229 | 0.0 | 0.0 | +6b7f5603-ce44-4b91-8a3e-939c4fbb26ac / -715d5bfc-c8c3-4dec-a247-9e07ee2755e8,bdee5671-864a-47c9-9576-9e0d8d2a7c6a |
| Jogador 1 | 6-3 | 257 | BUY | ALL_IN | 19.0 | 7 | 202 | 5 | 46.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1108794212341309 | 0.0 | 0.0 | +e29db20a-6b71-4518-ac7d-1e5d9eb67582 / -4518ad1d-87e7-4110-830a-96183c533201,7306c9be-466e-498c-819e-274ff070c72b |
| Jogador 1 | 6-3 | 258 | BUY | ALL_IN | 19.0 | 7 | 198 | 5 | 46.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8733106255531311 | 0.0 | 0.0 | +46b04fe4-ef4d-4449-94d0-d8bc9660c4e0 / -— |
| Jogador 1 | 6-3 | 259 | BUY | ALL_IN | 19.0 | 7 | 195 | 5 | 46.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22041799128055573 | 0.0 | 0.0 | +5d95f8bc-0c01-4c67-8764-4410eb32ee93 / -— |
| Jogador 1 | 6-3 | 260 | BUY | ALL_IN | 19.0 | 7 | 193 | 5 | 46.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20553302764892578 | 0.0 | 0.0 | +5e8a73b8-846a-49a9-be41-30c3baf2cb55 / -— |
| Jogador 1 | 6-4 | 262 | SELL | ALL_IN | 1.0 | 7 | 202 | 5 | 46.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7372000217437744 | 0.0 | 0.0 | +— / -6b7f5603-ce44-4b91-8a3e-939c4fbb26ac |
| Jogador 1 | 6-4 | 263 | BUY | ALL_IN | 1.0 | 7 | 210 | 5 | 46.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5134551525115967 | 0.0 | 0.0 | +9f271ee0-c506-40b7-b3f3-bac209974ba2 / -— |
| Jogador 1 | 6-4 | 264 | SELL | ALL_IN | 1.0 | 7 | 207 | 5 | 46.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7372000217437744 | 0.0 | 0.0 | +— / -e29db20a-6b71-4518-ac7d-1e5d9eb67582 |
| Jogador 1 | 6-4 | 265 | BUY | ALL_IN | 1.0 | 7 | 218 | 5 | 46.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0832188129425049 | 0.0 | 0.0 | +de590b22-a48c-4c78-a2f3-6ef39ce948fe / -46b04fe4-ef4d-4449-94d0-d8bc9660c4e0,de8de4b5-48ea-4947-ae08-2b90d94b0fc1 |
| Jogador 1 | 6-4 | 266 | BUY | ALL_IN | 1.0 | 7 | 215 | 5 | 40.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18154194951057434 | 0.0 | 0.0 | +c55e9bf2-c9cf-4b76-a40c-6e8d73205402 / -— |
| Jogador 1 | 6-4 | 267 | MOVE_BENCH | ALL_IN | 1.0 | 7 | 211 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.427673876285553 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 269 | BUY | ALL_IN | 1.0 | 7 | 221 | 5 | 52.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08017265051603317 | 0.0 | 0.0 | +c71adf7d-8d74-439d-8863-dac0f4f20cd1 / -— |
| Jogador 1 | 6-5 | 270 | SELL | ALL_IN | 1.0 | 7 | 217 | 5 | 52.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04543333500623703 | 0.0 | 0.0 | +— / -5e8a73b8-846a-49a9-be41-30c3baf2cb55 |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29996994137763977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.16027452051639557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43195363879203796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5011208057403564 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1178072690963745 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12034329026937485 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3097630739212036 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4079780578613281 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.072244644165039 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2014729231595993 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 40 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4003281891345978 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024478765204548836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 42 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012103810906410217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 43 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0379400253295898 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 49 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1819411963224411 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 50 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2735218107700348 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 51 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26515424251556396 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 52 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14776204526424408 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04824712872505188 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19658327102661133 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 2 | 2-2 | 56 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.047971248626709 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 57 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23205779492855072 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 58 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14925861358642578 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 59 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047096773982048035 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 60 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24561917781829834 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 61 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8824999928474426 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-3 | 63 | BUY | STABILIZE | 91.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21984942257404327 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 64 | BUY_XP | STABILIZE | 91.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 65 | BUY_XP | STABILIZE | 91.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 66 | PASS | STABILIZE | 91.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 72 | BUY | STABILIZE | 91.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9689240455627441 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 2 | 2-4 | 73 | BUY | STABILIZE | 91.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33012327551841736 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 74 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006734988186508417 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 75 | SELL | STABILIZE | 91.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 |
| Jogador 2 | 2-4 | 76 | BUY | STABILIZE | 91.0 | 5 | 4 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1262308657169342 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 77 | SELL | STABILIZE | 91.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15300561487674713 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 2-4 | 78 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35532069206237793 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 79 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00261497194878757 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 80 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014858285896480083 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 82 | BUY | STABILIZE | 91.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35433661937713623 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 83 | BUY_XP | STABILIZE | 91.0 | 5 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 84 | SELL | STABILIZE | 91.0 | 5 | 0 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10716646164655685 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-5 | 85 | BUY | STABILIZE | 91.0 | 5 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03479413315653801 | 0.0 | 0.0 | +eb214f08-2367-4b33-af94-8aa504781450 / -— |
| Jogador 2 | 2-5 | 86 | SELL | STABILIZE | 91.0 | 5 | 1 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04100000113248825 | 0.0 | 0.0 | +— / -eb214f08-2367-4b33-af94-8aa504781450 |
| Jogador 2 | 2-5 | 87 | SELL | STABILIZE | 91.0 | 5 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5009605288505554 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 2-5 | 88 | BUY | STABILIZE | 91.0 | 5 | 5 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21759499609470367 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 89 | SELL | STABILIZE | 91.0 | 5 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.546072781085968 | 0.0 | 0.0 | +— / -081b684f-5d42-45c5-9a68-12127e5330a7 |
| Jogador 2 | 2-5 | 90 | BUY_XP | STABILIZE | 91.0 | 5 | 5 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 92 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21724651753902435 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 93 | SELL | STABILIZE | 85.0 | 5 | 3 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4935111105442047 | 0.0 | 0.0 | +— / -97fc5647-5995-4f21-aa03-13454546919a |
| Jogador 2 | 2-6 | 94 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06867630034685135 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 95 | BUY_XP | STABILIZE | 85.0 | 5 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 96 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 0 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5968492031097412 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 97 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0147332102060318 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 98 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014767679385840893 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 99 | PASS | STABILIZE | 85.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 102 | BUY | STABILIZE | 80.0 | 6 | 6 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36482131481170654 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 103 | BUY | STABILIZE | 80.0 | 6 | 2 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1137722060084343 | 0.0 | 0.0 | +6340ebaf-bd41-4f47-bdce-50e06faa4044 / -— |
| Jogador 2 | 2-7 | 104 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.288894004072063e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 105 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 106 | PASS | STABILIZE | 80.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 112 | BUY | STABILIZE | 80.0 | 6 | 6 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14339539408683777 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 113 | BUY | STABILIZE | 80.0 | 6 | 3 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24045820534229279 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 114 | CRAFT_AND_EQUIP | STABILIZE | 80.0 | 6 | 2 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2597065269947052 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 115 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 2 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09991125017404556 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 116 | SELL | STABILIZE | 80.0 | 6 | 2 | 0 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04147857800126076 | 0.0 | 0.0 | +— / -6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 3-1 | 117 | BUY | STABILIZE | 80.0 | 6 | 4 | 0 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05756363645195961 | 0.0 | 0.0 | +4312fba1-1471-4fb3-af6f-257248fa1437 / -— |
| Jogador 2 | 3-1 | 118 | SELL | STABILIZE | 80.0 | 6 | 2 | 0 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0689999982714653 | 0.0 | 0.0 | +— / -6340ebaf-bd41-4f47-bdce-50e06faa4044 |
| Jogador 2 | 3-1 | 119 | BUY_XP | STABILIZE | 80.0 | 6 | 4 | 0 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 121 | BUY | STABILIZE | 80.0 | 6 | 6 | 0 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8372997641563416 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -7ca9b803-76eb-4283-9648-7f98bfd81149,d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 2 | 3-2 | 122 | BUY | STABILIZE | 80.0 | 6 | 5 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6917337775230408 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 123 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 4 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5124481916427612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 124 | BUY | STABILIZE | 80.0 | 6 | 4 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22675472497940063 | 0.0 | 0.0 | +e86a4466-cd1f-48a3-a825-cab2e361b72a / -— |
| Jogador 2 | 3-2 | 125 | BUY | STABILIZE | 80.0 | 6 | 3 | 0 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2920532822608948 | 0.0 | 0.0 | +f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 / -— |
| Jogador 2 | 3-2 | 126 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 1 | 0 | 22.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.51439279661281e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 127 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 1 | 0 | 22.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015825992450118065 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 128 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 1 | 0 | 22.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014148842543363571 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 130 | SELL | STABILIZE | 80.0 | 6 | 8 | 0 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0018333332845941186 | 0.0 | 0.0 | +— / -e86a4466-cd1f-48a3-a825-cab2e361b72a |
| Jogador 2 | 3-4 | 132 | BUY | STABILIZE | 80.0 | 6 | 17 | 1 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03398800641298294 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 133 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 15 | 1 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.288516487984452e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 134 | SELL | STABILIZE | 80.0 | 6 | 15 | 1 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 |
| Jogador 2 | 3-4 | 135 | BUY | STABILIZE | 80.0 | 6 | 17 | 1 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026250135153532028 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -— |
| Jogador 2 | 3-4 | 136 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 15 | 1 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.593391400296241e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 137 | SELL | STABILIZE | 80.0 | 6 | 15 | 1 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -c4c0b136-020d-4c1e-9517-8e0bf4c5a628 |
| Jogador 2 | 3-4 | 138 | BUY | STABILIZE | 80.0 | 6 | 17 | 1 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026110243052244186 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 2 | 3-4 | 139 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 15 | 1 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.1310783267836086e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 140 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 15 | 1 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015486141666769981 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 142 | SELL | STABILIZE | 80.0 | 6 | 22 | 2 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 2 | 3-5 | 143 | BUY | STABILIZE | 80.0 | 6 | 24 | 2 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.808179497718811 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 144 | SELL | STABILIZE | 80.0 | 6 | 21 | 2 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023170411586761475 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 3-5 | 145 | BUY | STABILIZE | 80.0 | 6 | 23 | 2 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5367074012756348 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 146 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 21 | 2 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01622609980404377 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 147 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 21 | 2 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001680032699368894 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 148 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 21 | 2 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014992516487836838 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 149 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 21 | 2 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015003612264990807 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 150 | PASS | STABILIZE | 80.0 | 6 | 21 | 2 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 152 | SELL | STABILIZE | 80.0 | 6 | 30 | 3 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -d1840f93-35b0-4e88-b58e-eea7267beedc |
| Jogador 2 | 3-6 | 153 | BUY | STABILIZE | 80.0 | 6 | 33 | 3 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31470242142677307 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-6 | 154 | SELL | STABILIZE | 80.0 | 6 | 32 | 3 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5879999995231628 | 0.0 | 0.0 | +— / -f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 3-6 | 155 | BUY | STABILIZE | 80.0 | 6 | 33 | 3 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25885435938835144 | 0.0 | 0.0 | +33a860e2-992f-4355-ab24-85b4a2576f90 / -— |
| Jogador 2 | 3-6 | 156 | SELL | STABILIZE | 80.0 | 6 | 30 | 3 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4660315215587616 | 0.0 | 0.0 | +— / -4312fba1-1471-4fb3-af6f-257248fa1437 |
| Jogador 2 | 3-6 | 157 | BUY | STABILIZE | 80.0 | 6 | 32 | 3 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12295040488243103 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 158 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 29 | 2 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.116517058922909e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 159 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 29 | 2 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24230730533599854 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 161 | SELL | STABILIZE | 80.0 | 6 | 40 | 4 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02363038808107376 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 3-7 | 162 | BUY | STABILIZE | 80.0 | 6 | 42 | 4 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7539166212081909 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -— |
| Jogador 2 | 3-7 | 163 | SELL | STABILIZE | 80.0 | 6 | 39 | 3 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07783249020576477 | 0.0 | 0.0 | +— / -23157bd6-5e8f-4416-bb7f-2e5d71a06543 |
| Jogador 2 | 3-7 | 164 | BUY | STABILIZE | 80.0 | 6 | 42 | 4 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38709601759910583 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 2 | 3-7 | 165 | SELL | STABILIZE | 80.0 | 6 | 39 | 3 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.367333322763443 | 0.0 | 0.0 | +— / -33a860e2-992f-4355-ab24-85b4a2576f90 |
| Jogador 2 | 3-7 | 166 | BUY | STABILIZE | 80.0 | 6 | 42 | 4 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026249602437019348 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 2 | 3-7 | 167 | SELL | STABILIZE | 80.0 | 6 | 40 | 4 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -74b1cd6f-12f4-4287-a5f6-9d016663ccf5 |
| Jogador 2 | 3-7 | 168 | BUY | STABILIZE | 80.0 | 6 | 42 | 4 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32919788360595703 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 169 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 39 | 3 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 171 | CRAFT_AND_EQUIP | STABILIZE | 80.0 | 6 | 49 | 4 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16835162043571472 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 172 | CRAFT_AND_EQUIP | STABILIZE | 80.0 | 6 | 49 | 4 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.181045800447464 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 173 | SELL | STABILIZE | 80.0 | 6 | 49 | 4 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08250000327825546 | 0.0 | 0.0 | +— / -e0445166-70a5-4135-a45e-ff238a95b228 |
| Jogador 2 | 4-1 | 174 | BUY | STABILIZE | 80.0 | 6 | 52 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8296951651573181 | 0.0 | 0.0 | +1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 / -— |
| Jogador 2 | 4-1 | 175 | SELL | STABILIZE | 80.0 | 6 | 51 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -ed0dab77-fd87-4677-8428-7505ccd34b86 |
| Jogador 2 | 4-1 | 176 | BUY | STABILIZE | 80.0 | 6 | 54 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.054075177758932114 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 2 | 4-1 | 177 | SELL | STABILIZE | 80.0 | 6 | 52 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03141096606850624 | 0.0 | 0.0 | +— / -1be0cdcc-ee10-44dc-ad1b-de9b53b25164 |
| Jogador 2 | 4-1 | 178 | BUY | STABILIZE | 80.0 | 6 | 54 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24838878214359283 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 2 | 4-2 | 180 | SELL | STABILIZE | 80.0 | 6 | 64 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -59304448-26ee-4e38-a52e-014e22ece127 |
| Jogador 2 | 4-3 | 182 | BUY | STABILIZE | 80.0 | 6 | 82 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9636009931564331 | 0.0 | 0.0 | +104aaac3-252c-4c1b-9ad8-fc10a35c6cda / -0c15e414-bc67-46de-a087-fb7708db0dfe,392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 4-3 | 183 | BUY | STABILIZE | 80.0 | 6 | 79 | 5 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2826322913169861 | 0.0 | 0.0 | +6538f28f-845f-4f45-92bf-120931553bec / -— |
| Jogador 2 | 4-3 | 184 | BUY | STABILIZE | 80.0 | 6 | 77 | 5 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28485870361328125 | 0.0 | 0.0 | +caf1c554-2223-4090-9f96-b551e5c579ce / -— |
| Jogador 2 | 4-3 | 185 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 75 | 5 | 22.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009726370684802532 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 186 | SELL | STABILIZE | 80.0 | 6 | 75 | 5 | 22.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -104aaac3-252c-4c1b-9ad8-fc10a35c6cda |
| Jogador 2 | 4-3 | 187 | BUY | STABILIZE | 80.0 | 6 | 83 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2890828251838684 | 0.0 | 0.0 | +84886290-556f-45e9-805b-9ca86a80ba27 / -— |
| Jogador 2 | 4-3 | 188 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 82 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04512012004852295 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 189 | SELL | STABILIZE | 80.0 | 6 | 82 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -84886290-556f-45e9-805b-9ca86a80ba27 |
| Jogador 2 | 4-4 | 191 | BUY | STABILIZE | 69.0 | 6 | 93 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.046291034668684006 | 0.0 | 0.0 | +bb2e33e3-fe6f-4344-b113-aeba7ace7a2d / -— |
| Jogador 2 | 4-4 | 192 | SELL | STABILIZE | 69.0 | 6 | 91 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -6538f28f-845f-4f45-92bf-120931553bec |
| Jogador 2 | 4-4 | 193 | BUY | STABILIZE | 69.0 | 6 | 93 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08603452891111374 | 0.0 | 0.0 | +30d2995a-d9b8-4424-af46-8766734e440c / -— |
| Jogador 2 | 4-4 | 194 | SELL | STABILIZE | 69.0 | 6 | 91 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -caf1c554-2223-4090-9f96-b551e5c579ce |
| Jogador 2 | 4-4 | 195 | BUY | STABILIZE | 69.0 | 6 | 93 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.085985466837883 | 0.0 | 0.0 | +d974e68a-e978-4335-8827-a94a9219be58 / -— |
| Jogador 2 | 4-4 | 196 | SELL | STABILIZE | 69.0 | 6 | 91 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002121198922395706 | 0.0 | 0.0 | +— / -30d2995a-d9b8-4424-af46-8766734e440c |
| Jogador 2 | 4-5 | 198 | BUY | STABILIZE | 69.0 | 6 | 103 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3750147223472595 | 0.0 | 0.0 | +d1f19609-8b5f-489d-a2cf-d015fe7ed27e / -— |
| Jogador 2 | 4-5 | 199 | SELL | STABILIZE | 69.0 | 6 | 100 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004216904751956463 | 0.0 | 0.0 | +— / -d974e68a-e978-4335-8827-a94a9219be58 |
| Jogador 2 | 4-5 | 200 | BUY | STABILIZE | 69.0 | 6 | 102 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32237860560417175 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 2 | 4-6 | 202 | SELL | STABILIZE | 69.0 | 6 | 110 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0313410609960556 | 0.0 | 0.0 | +— / -bb2e33e3-fe6f-4344-b113-aeba7ace7a2d |
| Jogador 2 | 4-6 | 203 | BUY | STABILIZE | 69.0 | 6 | 112 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9611709713935852 | 0.0 | 0.0 | +83228c14-cadb-45b4-9893-2fb12c40f4a8 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-6 | 204 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 111 | 5 | 18.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21875132620334625 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 205 | BUY | STABILIZE | 69.0 | 6 | 111 | 5 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3888578414916992 | 0.0 | 0.0 | +0f5471bd-1451-4979-adc9-aced6bb63610 / -— |
| Jogador 2 | 4-6 | 206 | SELL | STABILIZE | 69.0 | 6 | 110 | 5 | 20.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -83228c14-cadb-45b4-9893-2fb12c40f4a8 |
| Jogador 2 | 4-6 | 207 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 113 | 5 | 20.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.3877246677875519 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 209 | BUY | STABILIZE | 55.0 | 6 | 123 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.07684940844774246 | 0.0 | 0.0 | +6ea982ab-292d-42fc-99e6-d67c89f9f4fe / -— |
| Jogador 2 | 4-7 | 210 | BUY | STABILIZE | 55.0 | 6 | 121 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.07541695237159729 | 0.0 | 0.0 | +84e865bc-366e-45cd-85e4-fa7314688368 / -— |
| Jogador 2 | 5-1 | 212 | CRAFT_AND_EQUIP | STABILIZE | 55.0 | 7 | 130 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.1458500325679779 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 213 | CRAFT_AND_EQUIP | STABILIZE | 55.0 | 7 | 130 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.10639187693595886 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 214 | EQUIP_FROM_INVENTORY | STABILIZE | 55.0 | 7 | 130 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09379366040229797 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 215 | EQUIP_FROM_INVENTORY | STABILIZE | 55.0 | 7 | 130 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07994672656059265 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 216 | SELL | STABILIZE | 55.0 | 7 | 130 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029863741248846054 | 0.0 | 0.0 | +— / -84e865bc-366e-45cd-85e4-fa7314688368 |
| Jogador 2 | 5-1 | 217 | BUY | STABILIZE | 55.0 | 7 | 131 | 5 | 22.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04071246460080147 | 0.0 | 0.0 | +aaebedb3-18bf-4ae6-948e-7b326b573f1c / -— |
| Jogador 2 | 5-1 | 218 | MOVE_BENCH | STABILIZE | 55.0 | 7 | 126 | 5 | 22.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4301425814628601 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 220 | BUY | STABILIZE | 41.0 | 7 | 137 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044152356684207916 | 0.0 | 0.0 | +2949d735-3c16-4a45-835b-e11a9c12b16a / -— |
| Jogador 2 | 5-3 | 222 | SELL | STABILIZE | 41.0 | 7 | 145 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -2949d735-3c16-4a45-835b-e11a9c12b16a |
| Jogador 2 | 5-3 | 223 | BUY | STABILIZE | 41.0 | 7 | 148 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7063199281692505 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -— |
| Jogador 2 | 5-3 | 224 | SELL | STABILIZE | 41.0 | 7 | 145 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02419999986886978 | 0.0 | 0.0 | +— / -aaebedb3-18bf-4ae6-948e-7b326b573f1c |
| Jogador 2 | 5-3 | 225 | BUY | STABILIZE | 41.0 | 7 | 150 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12356651574373245 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -— |
| Jogador 2 | 5-3 | 226 | SELL | STABILIZE | 41.0 | 7 | 147 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -6c338d19-b3d3-49a7-b61e-4732249ee457 |
| Jogador 2 | 5-3 | 227 | BUY | STABILIZE | 41.0 | 7 | 150 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029117338359355927 | 0.0 | 0.0 | +b3905667-bcb5-4e23-94fa-25160b14a95e / -— |
| Jogador 2 | 5-4 | 229 | SELL | STABILIZE | 41.0 | 7 | 160 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -b3905667-bcb5-4e23-94fa-25160b14a95e |
| Jogador 2 | 5-4 | 230 | BUY | STABILIZE | 41.0 | 7 | 162 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9558448791503906 | 0.0 | 0.0 | +499f10b9-47ba-4cab-add1-31b452acae6d / -— |
| Jogador 2 | 5-5 | 232 | SELL | STABILIZE | 41.0 | 7 | 172 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5075684785842896 | 0.0 | 0.0 | +— / -4688e6f1-26c5-402d-8d27-0f9bce3a9681 |
| Jogador 2 | 5-5 | 233 | BUY | STABILIZE | 41.0 | 7 | 175 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15868738293647766 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -— |
| Jogador 2 | 5-5 | 234 | SELL | STABILIZE | 41.0 | 7 | 171 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05333355441689491 | 0.0 | 0.0 | +— / -5b96c8f7-bacb-47df-8666-30d30d49549d |
| Jogador 2 | 5-5 | 235 | BUY | STABILIZE | 41.0 | 7 | 174 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16298823058605194 | 0.0 | 0.0 | +d9097eba-c1b2-4df8-9e5d-a9134dbfe52f / -— |
| Jogador 2 | 5-5 | 236 | SELL | STABILIZE | 41.0 | 7 | 171 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042399998754262924 | 0.0 | 0.0 | +— / -d9097eba-c1b2-4df8-9e5d-a9134dbfe52f |
| Jogador 2 | 5-5 | 237 | BUY | STABILIZE | 41.0 | 7 | 174 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029130222275853157 | 0.0 | 0.0 | +98991369-e5f0-4725-928c-f2fa5362bf73 / -— |
| Jogador 2 | 5-6 | 239 | SELL | STABILIZE | 41.0 | 7 | 183 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -98991369-e5f0-4725-928c-f2fa5362bf73 |
| Jogador 2 | 5-6 | 240 | BUY | STABILIZE | 41.0 | 7 | 185 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.362390398979187 | 0.0 | 0.0 | +2b89bd83-8449-4c63-9da2-62a46c68bdf5 / -— |
| Jogador 2 | 5-7 | 242 | SELL | STABILIZE | 26.0 | 7 | 191 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042399998754262924 | 0.0 | 0.0 | +— / -f6000a82-1241-4220-9362-c8d788472db0 |
| Jogador 2 | 5-7 | 243 | BUY | STABILIZE | 26.0 | 7 | 195 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0214660167694092 | 0.0 | 0.0 | +9f1c634e-13c7-4b59-838c-4b676fa059be / -cce8de69-f877-4e86-b720-6aea91e68f47,e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 5-7 | 244 | BUY | STABILIZE | 26.0 | 7 | 192 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21111012995243073 | 0.0 | 0.0 | +1bf15a91-4832-4245-9b48-382a27410263 / -— |
| Jogador 2 | 5-7 | 245 | BUY | STABILIZE | 26.0 | 7 | 189 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035112664103507996 | 0.0 | 0.0 | +864f332a-0446-4995-b7fb-76d48d293501 / -— |
| Jogador 2 | 5-7 | 246 | SELL | STABILIZE | 26.0 | 7 | 186 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -9f1c634e-13c7-4b59-838c-4b676fa059be |
| Jogador 2 | 5-7 | 247 | BUY | STABILIZE | 26.0 | 7 | 194 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01664203591644764 | 0.0 | 0.0 | +be1e11e4-dc58-4e75-a402-3a2d831ac7b3 / -— |
| Jogador 2 | 6-1 | 249 | EQUIP_FROM_INVENTORY | STABILIZE | 26.0 | 7 | 200 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10045088082551956 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 250 | SELL | STABILIZE | 26.0 | 7 | 200 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02983333356678486 | 0.0 | 0.0 | +— / -864f332a-0446-4995-b7fb-76d48d293501 |
| Jogador 2 | 6-2 | 252 | BUY | ALL_IN | 10.0 | 7 | 214 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6368586421012878 | 0.0 | 0.0 | +dc423197-9320-4651-b71d-a62086416f9d / -— |
| Jogador 2 | 6-2 | 253 | SELL | ALL_IN | 10.0 | 7 | 212 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04781223461031914 | 0.0 | 0.0 | +— / -1bf15a91-4832-4245-9b48-382a27410263 |
| Jogador 2 | 6-2 | 254 | BUY | ALL_IN | 10.0 | 7 | 215 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1593329906463623 | 0.0 | 0.0 | +aa803972-8af8-46d7-b430-079819730c36 / -— |
| Jogador 2 | 6-2 | 255 | SELL | ALL_IN | 10.0 | 7 | 212 | 5 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03274228796362877 | 0.0 | 0.0 | +— / -aa803972-8af8-46d7-b430-079819730c36 |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22444601356983185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0904720276594162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4064550995826721 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0396674871444702 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179779767990112 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009961719624698162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 28 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5901181697845459 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2275175005197525 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2126704603433609 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 41 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26552730798721313 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 49 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25187569856643677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 50 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23012398183345795 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 51 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39558812975883484 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21777497231960297 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007058049086481333 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 54 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012296375818550587 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 56 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9574238061904907 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 57 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3376427888870239 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 58 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 63 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3334202766418457 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 64 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2638690173625946 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 65 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 66 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 72 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.890145480632782 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39209920167922974 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41481155157089233 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 75 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15203921496868134 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03466760367155075 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 77 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.047020673984662e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 79 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 82 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8984101414680481 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 83 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 84 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 92 | SELL | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01022217608988285 | 0.0 | 0.0 | +— / -5ead8548-7453-4fa1-856e-674995576a48 |
| Jogador 3 | 2-6 | 93 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9474310278892517 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -c70251e8-af44-4466-808f-d49e9e5f57e9,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-6 | 94 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10645737498998642 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 95 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499595165252686 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 96 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15247750282287598 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 97 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 20.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 98 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2731267511844635 | 0.0 | 0.0 | +d97b6383-1870-48d1-a9b8-6a8ce153c9ce / -— |
| Jogador 3 | 2-6 | 99 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39864757657051086 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 100 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 24.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013072052039206028 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 102 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8915395140647888 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 103 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16894032061100006 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 104 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 4 | 0 | 24.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005551745416596532 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 105 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 24.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 106 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 24.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5329245328903198 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 107 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 108 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01587655209004879 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 109 | PASS | STABILIZE | 100.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 112 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2833555340766907 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-1 | 113 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24911634624004364 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 114 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0007920031785033643 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 115 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 116 | BUY_XP | STABILIZE | 100.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 117 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39250949025154114 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 118 | SELL | STABILIZE | 100.0 | 6 | 0 | 0 | 28.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 3-1 | 119 | BUY | STABILIZE | 100.0 | 6 | 3 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5152053236961365 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -— |
| Jogador 3 | 3-2 | 121 | BUY_XP | STABILIZE | 100.0 | 6 | 10 | 1 | 28.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 122 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 28.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 123 | SELL | STABILIZE | 100.0 | 6 | 2 | 0 | 28.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 |
| Jogador 3 | 3-2 | 124 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8261659145355225 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 3-2 | 125 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 126 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4370170533657074 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 127 | BUY | STABILIZE | 100.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017222518101334572 | 0.0 | 0.0 | +fd3ab6e7-a3e5-4a03-8aa6-a80f6c0c1f47 / -— |
| Jogador 3 | 3-2 | 128 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.316895451163873e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 130 | BUY | STABILIZE | 100.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28521040081977844 | 0.0 | 0.0 | +f0b6c16b-7610-454c-929d-7152f0a041d3 / -— |
| Jogador 3 | 3-4 | 132 | SELL | STABILIZE | 100.0 | 6 | 16 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -fd3ab6e7-a3e5-4a03-8aa6-a80f6c0c1f47 |
| Jogador 3 | 3-4 | 133 | BUY | STABILIZE | 100.0 | 6 | 18 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8036919236183167 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 3 | 3-4 | 134 | BUY_XP | STABILIZE | 100.0 | 6 | 15 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 135 | BUY_XP | STABILIZE | 100.0 | 6 | 11 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 136 | BUY_XP | STABILIZE | 100.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0609700009226799 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 137 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5925838351249695 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 138 | BUY | FAST8 | 100.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033062007278203964 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 139 | MOVE_BOARD | FAST8 | 100.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.9263898682074796e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 140 | MOVE_BOARD | FAST8 | 100.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000022016465664 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 142 | MOVE_BOARD | FAST8 | 100.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.668036351380579e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 143 | MOVE_BOARD | FAST8 | 100.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 144 | MOVE_BOARD | FAST8 | 100.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 145 | PASS | FAST8 | 100.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 152 | MOVE_BOARD | FAST8 | 100.0 | 7 | 17 | 1 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0893005608636486e-08 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 153 | MOVE_BOARD | FAST8 | 100.0 | 7 | 17 | 1 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015030981041491032 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 154 | PASS | FAST8 | 100.0 | 7 | 17 | 1 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 161 | MOVE_BOARD | FAST8 | 100.0 | 7 | 27 | 2 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004387283697724342 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 162 | MOVE_BOARD | FAST8 | 100.0 | 7 | 27 | 2 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 163 | PASS | FAST8 | 100.0 | 7 | 27 | 2 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0794999971985817 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 171 | CRAFT_AND_EQUIP | FAST8 | 100.0 | 7 | 37 | 3 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13043023645877838 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 172 | CRAFT_AND_EQUIP | FAST8 | 100.0 | 7 | 37 | 3 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19193580746650696 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 173 | MOVE_BOARD | FAST8 | 100.0 | 7 | 37 | 3 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012796848313882947 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 174 | MOVE_BOARD | FAST8 | 100.0 | 7 | 37 | 3 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013807756826281548 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 175 | PASS | FAST8 | 100.0 | 7 | 37 | 3 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18071427941322327 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 180 | MOVE_BOARD | FAST8 | 88.0 | 7 | 45 | 4 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003275378840044141 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 182 | BUY_XP | FAST8 | 88.0 | 7 | 55 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05012800171971321 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 183 | BUY_XP | FAST8 | 88.0 | 7 | 51 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05100400000810623 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 184 | BUY_XP | FAST8 | 88.0 | 7 | 47 | 4 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025696000084280968 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 185 | BUY_XP | FAST8 | 88.0 | 7 | 43 | 4 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05430399999022484 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 186 | BUY_XP | FAST8 | 88.0 | 7 | 39 | 3 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025696000084280968 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 187 | BUY_XP | FAST8 | 88.0 | 7 | 35 | 3 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025696000084280968 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 188 | BUY_XP | FAST8 | 88.0 | 7 | 31 | 3 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05430399999022484 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 189 | BUY_XP | FAST8 | 88.0 | 7 | 27 | 2 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025696000084280968 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 191 | BUY_XP | FAST8 | 88.0 | 7 | 32 | 3 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05430399999022484 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 192 | BUY_XP | FAST8 | 88.0 | 7 | 28 | 2 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09169375151395798 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 193 | MOVE_BENCH | ECON | 88.0 | 8 | 24 | 2 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4028041958808899 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 194 | BUY | ECON | 88.0 | 8 | 24 | 2 | 42.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002161390846595168 | 0.0 | 0.0 | +b5b3098f-d48c-42b8-8022-639a25225980 / -— |
| Jogador 3 | 4-4 | 195 | MOVE_BOARD | ECON | 88.0 | 8 | 21 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 196 | MOVE_BOARD | ECON | 88.0 | 8 | 21 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014915991574525833 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 198 | SELL | ECON | 88.0 | 8 | 29 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05113333463668823 | 0.0 | 0.0 | +— / -f19f9e7f-f189-47fe-b571-be5065c6eb39 |
| Jogador 3 | 4-5 | 199 | BUY | ECON | 88.0 | 8 | 31 | 3 | 42.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7433149218559265 | 0.0 | 0.0 | +3a1de7b3-af72-4024-8105-588fa4ec946b / -c3f8419e-a450-4247-bb65-8de8dba1c8ee,d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 3 | 4-5 | 200 | MOVE_BENCH | ECON | 88.0 | 8 | 28 | 2 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.919292151927948 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 202 | BUY | WINSTREAK | 88.0 | 8 | 37 | 3 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06935229152441025 | 0.0 | 0.0 | +42aa4dc8-e388-40dd-a210-4c59e358afcd / -— |
| Jogador 3 | 4-6 | 203 | BUY_XP | WINSTREAK | 88.0 | 8 | 34 | 3 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 204 | BUY_XP | WINSTREAK | 88.0 | 8 | 30 | 3 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 205 | BUY_XP | WINSTREAK | 88.0 | 8 | 26 | 2 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 206 | BUY_XP | WINSTREAK | 88.0 | 8 | 22 | 2 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 207 | MOVE_BENCH | WINSTREAK | 88.0 | 8 | 18 | 1 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40188300609588623 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 209 | BUY | WINSTREAK | 88.0 | 8 | 26 | 2 | 42.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8199408054351807 | 0.0 | 0.0 | +590d07db-5e90-4705-a7ae-96f84fd06382 / -2fa86b11-4e28-4652-890e-f00a79068223,41db1132-4e1c-48eb-8a9b-1b2c74cb22ce |
| Jogador 3 | 4-7 | 210 | BUY | WINSTREAK | 88.0 | 8 | 24 | 2 | 42.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10856356471776962 | 0.0 | 0.0 | +18e21ac6-f873-4310-95c8-bd8e62612479 / -— |
| Jogador 3 | 5-1 | 212 | BUY | WINSTREAK | 88.0 | 8 | 28 | 2 | 42.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.19974125921726227 | 0.0 | 0.0 | +ee67f5c6-559f-492e-9cc0-6bc19a203d6a / -— |
| Jogador 3 | 5-1 | 213 | CRAFT_AND_EQUIP | WINSTREAK | 88.0 | 8 | 25 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13615040481090546 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 214 | CRAFT_AND_EQUIP | WINSTREAK | 88.0 | 8 | 25 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.07235528528690338 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 215 | MOVE_BOARD | WINSTREAK | 88.0 | 8 | 25 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06362488865852356 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 216 | BUY_XP | WINSTREAK | 88.0 | 8 | 25 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020080000162124634 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 217 | BUY_XP | WINSTREAK | 88.0 | 8 | 21 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05992000177502632 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 218 | BUY_XP | WINSTREAK | 88.0 | 8 | 17 | 1 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020080000162124634 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 220 | SELL | WINSTREAK | 88.0 | 8 | 22 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09410511702299118 | 0.0 | 0.0 | +— / -590d07db-5e90-4705-a7ae-96f84fd06382 |
| Jogador 3 | 5-3 | 222 | BUY | ECON | 75.0 | 8 | 34 | 3 | 42.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6962212920188904 | 0.0 | 0.0 | +1c5a9322-14c8-4df9-937b-842dcaa1f372 / -— |
| Jogador 3 | 5-3 | 223 | BUY_XP | ECON | 75.0 | 8 | 32 | 3 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0568000003695488 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 224 | BUY_XP | ECON | 75.0 | 8 | 28 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02319999970495701 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 225 | BUY_XP | ECON | 75.0 | 8 | 24 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02319999970495701 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 226 | BUY_XP | ECON | 75.0 | 8 | 20 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0568000003695488 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 227 | BUY_XP | ECON | 75.0 | 8 | 16 | 1 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02319999970495701 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 229 | SELL | ECON | 62.0 | 8 | 19 | 1 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41019999980926514 | 0.0 | 0.0 | +— / -2d1296a3-9aa4-42ab-8b86-34661e32a63d |
| Jogador 3 | 5-4 | 230 | BUY | ECON | 62.0 | 8 | 22 | 2 | 42.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.765075147151947 | 0.0 | 0.0 | +438ec27b-d901-437b-82b5-64e6d46fccb1 / -— |
| Jogador 3 | 5-5 | 232 | MOVE_BENCH | ECON | 62.0 | 8 | 28 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13351882994174957 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 233 | SELL | ECON | 62.0 | 8 | 28 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -3a1de7b3-af72-4024-8105-588fa4ec946b |
| Jogador 3 | 5-5 | 234 | BUY | ECON | 62.0 | 8 | 36 | 3 | 42.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08607218414545059 | 0.0 | 0.0 | +8756c125-e3d6-4f40-80d2-a6bf20e7b1c7 / -— |
| Jogador 3 | 5-5 | 235 | BUY_XP | ECON | 62.0 | 8 | 31 | 3 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008124999701976776 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 236 | BUY_XP | ECON | 62.0 | 9 | 27 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 237 | MOVE_BENCH | ECON | 62.0 | 9 | 23 | 2 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5559244751930237 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 239 | BUY | ECON | 62.0 | 9 | 31 | 3 | 46.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7737900614738464 | 0.0 | 0.0 | +e978e901-0a52-4f01-ba52-a83fbcc3b439 / -79786887-d318-4836-b2f0-c0f03e86cbe5,8a68772c-3f02-4f2e-882b-4fa69fbb6750 |
| Jogador 3 | 5-6 | 240 | BUY | ECON | 62.0 | 9 | 28 | 2 | 40.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2320474237203598 | 0.0 | 0.0 | +9c07608c-00e1-40f1-9671-6d8bc584a6c9 / -— |
| Jogador 3 | 5-7 | 242 | BUY | ECON | 62.0 | 9 | 34 | 3 | 52.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7772156000137329 | 0.0 | 0.0 | +8068dc77-9528-4a1d-b4dc-5ac216e8684f / -— |
| Jogador 3 | 5-7 | 243 | SELL | ECON | 62.0 | 9 | 31 | 3 | 52.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -d97b6383-1870-48d1-a9b8-6a8ce153c9ce |
| Jogador 3 | 5-7 | 244 | BUY | ECON | 62.0 | 9 | 33 | 3 | 52.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18143115937709808 | 0.0 | 0.0 | +8faad4f9-9f15-49e8-94af-b4d28879cc0d / -— |
| Jogador 3 | 5-7 | 245 | MOVE_BOARD | ECON | 62.0 | 9 | 29 | 2 | 52.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00010520090290810913 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 246 | MOVE_BOARD | ECON | 62.0 | 9 | 29 | 2 | 52.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01504175178706646 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 247 | MOVE_BOARD | ECON | 62.0 | 9 | 29 | 2 | 52.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015034331940114498 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 249 | EQUIP_FROM_INVENTORY | ECON | 62.0 | 9 | 37 | 3 | 52.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.016114337369799614 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 250 | MOVE_BOARD | ECON | 62.0 | 9 | 37 | 3 | 52.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.806992314523086e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 252 | SELL | WINSTREAK | 62.0 | 9 | 47 | 4 | 52.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03709537908434868 | 0.0 | 0.0 | +— / -ee67f5c6-559f-492e-9cc0-6bc19a203d6a |
| Jogador 3 | 6-2 | 253 | BUY | WINSTREAK | 62.0 | 9 | 50 | 5 | 52.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.974368691444397 | 0.0 | 0.0 | +425a58b3-d906-4381-9afc-00f9852c9982 / -1c5a9322-14c8-4df9-937b-842dcaa1f372,ab6084b0-65df-4a70-8591-687b320d98b6 |
| Jogador 3 | 6-2 | 254 | MOVE_BENCH | WINSTREAK | 62.0 | 9 | 48 | 4 | 44.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26844465732574463 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 255 | BUY | WINSTREAK | 62.0 | 9 | 48 | 4 | 52.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3853788673877716 | 0.0 | 0.0 | +3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 / -— |
| Jogador 3 | 6-3 | 257 | BUY | WINSTREAK | 62.0 | 9 | 57 | 5 | 58.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9132689237594604 | 0.0 | 0.0 | +4321582a-0b45-4666-a119-7b49e92d012a / -— |
| Jogador 3 | 6-3 | 258 | MOVE_BOARD | WINSTREAK | 62.0 | 9 | 54 | 5 | 58.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005679908208549023 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 259 | MOVE_BOARD | WINSTREAK | 62.0 | 9 | 54 | 5 | 58.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 260 | PASS | WINSTREAK | 62.0 | 9 | 54 | 5 | 58.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04460920765995979 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 262 | MOVE_BOARD | WINSTREAK | 62.0 | 9 | 67 | 5 | 58.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 263 | MOVE_BOARD | WINSTREAK | 62.0 | 9 | 67 | 5 | 58.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014325442723929882 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 264 | PASS | WINSTREAK | 62.0 | 9 | 67 | 5 | 58.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05481552332639694 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 269 | MOVE_BOARD | WINSTREAK | 62.0 | 9 | 79 | 5 | 58.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 270 | MOVE_BOARD | WINSTREAK | 62.0 | 9 | 79 | 5 | 58.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2201479971408844 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09193183481693268 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4628557562828064 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16212894022464752 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0601743720471859 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 28 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.012830376625061 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3392508029937744 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 39 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9801579713821411 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 49 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18356098234653473 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 50 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21593625843524933 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 51 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 52 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3917175829410553 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 56 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9553565382957458 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 57 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 58 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 61 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42839792370796204 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 63 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.94389808177948 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 64 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0434507131576538 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 65 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3042055368423462 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 66 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Camille | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5619999766349792 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 67 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 68 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 2-3 | 69 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10034149140119553 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 70 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5416666865348816 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-4 | 72 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13742510974407196 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 73 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23768742382526398 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 74 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15833333134651184 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-4 | 75 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 76 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005146525800228119 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 77 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11433333158493042 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 78 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08100000023841858 | 0.0 | 0.0 | +— / -0b62545c-1de0-47d8-bb4c-119f7e1526b3 |
| Jogador 4 | 2-4 | 79 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25047552585601807 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 80 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9552910923957825 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 4 | 2-5 | 82 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0012850761413574 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -86c535a4-a22b-4667-bc0f-46b4843d97cc,8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-5 | 83 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3844667971134186 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 4 | 2-5 | 84 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 85 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2077624797821045 | 0.0 | 0.0 | +— / -4b07138d-44fd-4515-8b65-d7db84f4639c |
| Jogador 4 | 2-5 | 86 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21663005650043488 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 87 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39750757813453674 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 88 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5794024467468262 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 2-5 | 89 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 90 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0130336107686162 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 92 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.326031893491745 | 0.0 | 0.0 | +f71a7192-663d-46a0-93ef-b900c59c3bde / -— |
| Jogador 4 | 2-6 | 93 | BUY | STABILIZE | 90.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28372570872306824 | 0.0 | 0.0 | +814d07bd-0296-44af-9626-26a8a224d86f / -— |
| Jogador 4 | 2-6 | 94 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008337188512086868 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 95 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014826050959527493 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01666545867919922 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 97 | PASS | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 102 | BUY | STABILIZE | 84.0 | 6 | 8 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9389603734016418 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -— |
| Jogador 4 | 2-7 | 103 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3618030250072479 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 104 | BUY_XP | STABILIZE | 84.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 105 | SELL | STABILIZE | 84.0 | 6 | 0 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2590000033378601 | 0.0 | 0.0 | +— / -5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 2-7 | 106 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5897884964942932 | 0.0 | 0.0 | +— / -814d07bd-0296-44af-9626-26a8a224d86f |
| Jogador 4 | 2-7 | 107 | BUY | STABILIZE | 84.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13401184976100922 | 0.0 | 0.0 | +53a27943-148b-4522-9826-3f2e0b8a7858 / -— |
| Jogador 4 | 2-7 | 108 | SELL | STABILIZE | 84.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15007710456848145 | 0.0 | 0.0 | +— / -4a0403a3-c999-4d4c-83f0-7270e8576aed |
| Jogador 4 | 2-7 | 109 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39851123094558716 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 110 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 112 | BUY | STABILIZE | 84.0 | 6 | 9 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8029270172119141 | 0.0 | 0.0 | +8052731e-e34c-4de7-84b1-2b986cfeddaa / -— |
| Jogador 4 | 3-1 | 113 | BUY | STABILIZE | 84.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2251192033290863 | 0.0 | 0.0 | +cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 / -— |
| Jogador 4 | 3-1 | 114 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 6 | 6 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24341042339801788 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 115 | BUY_XP | STABILIZE | 84.0 | 6 | 6 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 116 | SELL | STABILIZE | 84.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11922940611839294 | 0.0 | 0.0 | +— / -cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 |
| Jogador 4 | 3-1 | 117 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -53a27943-148b-4522-9826-3f2e0b8a7858 |
| Jogador 4 | 3-1 | 118 | BUY | STABILIZE | 84.0 | 6 | 5 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04824843630194664 | 0.0 | 0.0 | +31aa0a5f-4d66-48c2-b6d4-b76ac220c752 / -— |
| Jogador 4 | 3-1 | 119 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 2 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09845808893442154 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 121 | BUY | STABILIZE | 72.0 | 6 | 8 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379963040351868 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 122 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 7 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22362366318702698 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 123 | BUY | STABILIZE | 72.0 | 6 | 7 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879989445209503 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 124 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 6 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6034010052680969 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 125 | BUY | STABILIZE | 72.0 | 6 | 6 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11924884468317032 | 0.0 | 0.0 | +421bcbcb-ecb2-4af8-88d4-7be6cd284d27 / -— |
| Jogador 4 | 3-2 | 126 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04742184281349182 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 127 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 3 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 128 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 3 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.054462119936943054 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 130 | BUY | STABILIZE | 62.0 | 6 | 9 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8347469568252563 | 0.0 | 0.0 | +52018505-08c9-471f-83b9-fd5066efe55a / -8052731e-e34c-4de7-84b1-2b986cfeddaa,c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 4 | 3-4 | 132 | BUY | STABILIZE | 52.0 | 6 | 14 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2854371666908264 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 4 | 3-4 | 133 | BUY | STABILIZE | 52.0 | 6 | 12 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19843892753124237 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 134 | BUY | STABILIZE | 52.0 | 6 | 9 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23970291018486023 | 0.0 | 0.0 | +e01be6cf-34fe-4057-aef3-c08c504794cf / -— |
| Jogador 4 | 3-4 | 135 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 7 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15811175107955933 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 136 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 7 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4215269982814789 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 137 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 7 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38180145621299744 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 138 | PASS | STABILIZE | 52.0 | 6 | 7 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 142 | BUY | STABILIZE | 52.0 | 6 | 14 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8053795695304871 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -— |
| Jogador 4 | 3-5 | 143 | BUY | STABILIZE | 52.0 | 6 | 12 | 1 | 24.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7808619141578674 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 4 | 3-5 | 144 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 10 | 1 | 24.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10877648741006851 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 145 | MOVE_BOARD | STABILIZE | 52.0 | 6 | 10 | 1 | 20.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059569984674453735 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 146 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 10 | 1 | 20.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4953823983669281 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 147 | PASS | STABILIZE | 52.0 | 6 | 10 | 1 | 24.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 152 | SELL | STABILIZE | 43.0 | 6 | 19 | 1 | 24.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -52018505-08c9-471f-83b9-fd5066efe55a |
| Jogador 4 | 3-6 | 153 | BUY | STABILIZE | 43.0 | 6 | 24 | 2 | 24.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8497047424316406 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -7fd03119-ac82-49e1-b3bb-3a0caa31011f,fe6546c3-86ef-40e1-aa7e-ff7e400fe628 |
| Jogador 4 | 3-6 | 154 | MOVE_BENCH | STABILIZE | 43.0 | 6 | 22 | 2 | 24.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24434737861156464 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 155 | BUY | STABILIZE | 43.0 | 6 | 22 | 2 | 24.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7077283263206482 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 156 | MOVE_BENCH | STABILIZE | 43.0 | 6 | 19 | 1 | 24.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060964860022068024 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 157 | MOVE_BENCH | STABILIZE | 43.0 | 6 | 19 | 1 | 20.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38278716802597046 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 158 | MOVE_BENCH | STABILIZE | 43.0 | 6 | 19 | 1 | 22.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3963581919670105 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 159 | PASS | STABILIZE | 43.0 | 6 | 19 | 1 | 24.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058746665716171265 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 161 | BUY | STABILIZE | 33.0 | 6 | 28 | 2 | 24.0 | Florescer/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7948576211929321 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -— |
| Jogador 4 | 3-7 | 162 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 25 | 2 | 24.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08261985331773758 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 163 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 25 | 2 | 20.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3904602825641632 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 164 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 25 | 2 | 22.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4103023111820221 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 165 | PASS | STABILIZE | 33.0 | 6 | 25 | 2 | 24.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02996666729450226 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 171 | CRAFT_AND_EQUIP | STABILIZE | 33.0 | 6 | 35 | 3 | 24.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1483226716518402 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 172 | CRAFT_AND_EQUIP | STABILIZE | 33.0 | 6 | 35 | 3 | 24.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1819123476743698 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 173 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 35 | 3 | 24.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06096803396940231 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 174 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 35 | 3 | 20.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3827504813671112 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 175 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 35 | 3 | 22.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4262944757938385 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 176 | PASS | STABILIZE | 33.0 | 6 | 35 | 3 | 22.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05706349387764931 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 180 | SELL | ALL_IN | 22.0 | 6 | 46 | 4 | 22.0 | Florescer/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6723999977111816 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 4-3 | 182 | BUY | ALL_IN | 8.0 | 6 | 61 | 5 | 22.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.4566153287887573 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 4 | 4-3 | 183 | EQUIP_FROM_INVENTORY | ALL_IN | 8.0 | 6 | 59 | 5 | 22.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08696256577968597 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 184 | EQUIP_FROM_INVENTORY | ALL_IN | 8.0 | 6 | 59 | 5 | 22.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09896717965602875 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 185 | EQUIP_FROM_INVENTORY | ALL_IN | 8.0 | 6 | 59 | 5 | 22.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09033390879631042 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 186 | MOVE_BENCH | ALL_IN | 8.0 | 6 | 59 | 5 | 22.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8425756096839905 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 187 | MOVE_BENCH | ALL_IN | 8.0 | 6 | 59 | 5 | 24.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06291713565587997 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 188 | MOVE_BENCH | ALL_IN | 8.0 | 6 | 59 | 5 | 20.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25267326831817627 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 189 | MOVE_BENCH | ALL_IN | 8.0 | 6 | 59 | 5 | 22.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3929506838321686 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.26577791571617126 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.24549612402915955 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12370830029249191 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11255644261837006 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17292346060276031 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012102286331355572 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42841246724128723 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2180778682231903 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 25 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33112090826034546 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2899988889694214 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 39 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.032492756843567 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 49 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1990857720375061 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 50 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21306690573692322 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 51 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40897443890571594 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22610890865325928 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 53 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 56 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9718433618545532 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 57 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 58 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 63 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0440590381622314 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 64 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12274643033742905 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 66 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24616853892803192 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 67 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43635210394859314 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 68 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1628454178571701 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 69 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03177344799041748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 70 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25741812586784363 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-4 | 72 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3107256293296814 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 73 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.217121884226799 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 74 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 75 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05810000002384186 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 76 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08837512880563736 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-4 | 77 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16730432212352753 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 78 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07833333313465118 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-4 | 79 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09800082445144653 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-4 | 80 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 82 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.290279746055603 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 83 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33951982855796814 | 0.0 | 0.0 | +2e4ab22c-62d7-425c-9528-2e1315655c24 / -— |
| Jogador 5 | 2-5 | 84 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06970000267028809 | 0.0 | 0.0 | +— / -486e92ad-4dcf-4c0e-a470-e0b87777d380 |
| Jogador 5 | 2-5 | 85 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1223333328962326 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 5 | 2-5 | 86 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31702721118927 | 0.0 | 0.0 | +28f66ef1-93d6-4cc8-a0c9-e84e844dee28 / -— |
| Jogador 5 | 2-5 | 87 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 88 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3515999913215637 | 0.0 | 0.0 | +— / -28f66ef1-93d6-4cc8-a0c9-e84e844dee28 |
| Jogador 5 | 2-5 | 89 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 90 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39711663126945496 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 92 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36481955647468567 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 93 | BUY | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09186519682407379 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 94 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06104522570967674 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 95 | BUY | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05930067598819733 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 96 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08731768280267715 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-6 | 97 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06522078812122345 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 98 | SELL | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43148890137672424 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-6 | 99 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005137315951287746 | 0.0 | 0.0 | +53312511-4e10-4904-82c0-8a8e69c039cd / -— |
| Jogador 5 | 2-6 | 100 | BUY | STABILIZE | 95.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0050762249156832695 | 0.0 | 0.0 | +b6a21130-c9dc-45ad-8ddb-9223b0ec8751 / -— |
| Jogador 5 | 2-7 | 102 | BUY | STABILIZE | 89.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34532737731933594 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 103 | BUY | STABILIZE | 89.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9630588889122009 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 104 | BUY | STABILIZE | 89.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20998093485832214 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -— |
| Jogador 5 | 2-7 | 105 | SELL | STABILIZE | 89.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034699998795986176 | 0.0 | 0.0 | +— / -53312511-4e10-4904-82c0-8a8e69c039cd |
| Jogador 5 | 2-7 | 106 | SELL | STABILIZE | 89.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03592974692583084 | 0.0 | 0.0 | +— / -b6a21130-c9dc-45ad-8ddb-9223b0ec8751 |
| Jogador 5 | 2-7 | 107 | BUY | STABILIZE | 89.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10740545392036438 | 0.0 | 0.0 | +6eee9a92-4235-46af-ae42-c38acd6847ef / -— |
| Jogador 5 | 2-7 | 108 | SELL | STABILIZE | 89.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41966667771339417 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 2-7 | 109 | SELL | STABILIZE | 89.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37566667795181274 | 0.0 | 0.0 | +— / -6eee9a92-4235-46af-ae42-c38acd6847ef |
| Jogador 5 | 2-7 | 110 | BUY | STABILIZE | 89.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00808158703148365 | 0.0 | 0.0 | +c5593e47-f48a-4362-b230-dfa3d7d36ec9 / -— |
| Jogador 5 | 3-1 | 112 | BUY | STABILIZE | 89.0 | 6 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7501031756401062 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -46838f8d-8037-485c-8c34-9639f14ada19,837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-1 | 113 | CRAFT_AND_EQUIP | STABILIZE | 89.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.190902441740036 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 114 | BUY | STABILIZE | 89.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11416009068489075 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 115 | BUY | STABILIZE | 89.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028782688081264496 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 5 | 3-1 | 116 | SELL | STABILIZE | 89.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-1 | 117 | BUY | STABILIZE | 89.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06642027199268341 | 0.0 | 0.0 | +79ed9815-7667-4e50-86a3-420599ce8c79 / -— |
| Jogador 5 | 3-1 | 118 | SELL | STABILIZE | 89.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -c5593e47-f48a-4362-b230-dfa3d7d36ec9 |
| Jogador 5 | 3-1 | 119 | SELL | STABILIZE | 89.0 | 6 | 8 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25566667318344116 | 0.0 | 0.0 | +— / -79ed9815-7667-4e50-86a3-420599ce8c79 |
| Jogador 5 | 3-2 | 121 | BUY | STABILIZE | 79.0 | 6 | 17 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6887733340263367 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 122 | BUY | STABILIZE | 79.0 | 6 | 14 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2709639072418213 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -— |
| Jogador 5 | 3-2 | 123 | SELL | STABILIZE | 79.0 | 6 | 12 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06978107988834381 | 0.0 | 0.0 | +— / -a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 |
| Jogador 5 | 3-2 | 124 | SELL | STABILIZE | 79.0 | 6 | 14 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5378907918930054 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-2 | 125 | BUY | STABILIZE | 79.0 | 6 | 17 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2366536408662796 | 0.0 | 0.0 | +35a674f6-a230-480b-a93f-f7ec76d78658 / -— |
| Jogador 5 | 3-2 | 126 | MOVE_BENCH | STABILIZE | 79.0 | 6 | 15 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09630120545625687 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 127 | SELL | STABILIZE | 79.0 | 6 | 15 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3356666564941406 | 0.0 | 0.0 | +— / -35a674f6-a230-480b-a93f-f7ec76d78658 |
| Jogador 5 | 3-2 | 128 | SELL | STABILIZE | 79.0 | 6 | 17 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09700000286102295 | 0.0 | 0.0 | +— / -df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 3-3 | 130 | BUY | STABILIZE | 79.0 | 6 | 28 | 2 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8189306855201721 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -— |
| Jogador 5 | 3-4 | 132 | BUY | STABILIZE | 67.0 | 6 | 33 | 3 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8444415330886841 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 5 | 3-4 | 133 | BUY | STABILIZE | 67.0 | 6 | 32 | 3 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49653711915016174 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -— |
| Jogador 5 | 3-4 | 134 | BUY | STABILIZE | 67.0 | 6 | 31 | 3 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055022452026605606 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 135 | SELL | STABILIZE | 67.0 | 6 | 29 | 2 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2857615649700165 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 3-4 | 136 | SELL | STABILIZE | 67.0 | 6 | 31 | 3 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5042295455932617 | 0.0 | 0.0 | +— / -ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 3-4 | 137 | SELL | STABILIZE | 67.0 | 6 | 32 | 3 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5744222402572632 | 0.0 | 0.0 | +— / -135065df-1ebc-413d-86f1-4df28bd3ee41 |
| Jogador 5 | 3-4 | 138 | SELL | STABILIZE | 67.0 | 6 | 34 | 3 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7851547002792358 | 0.0 | 0.0 | +— / -eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 3-4 | 139 | MOVE_BENCH | STABILIZE | 67.0 | 6 | 35 | 3 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0218059029430151 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 140 | SELL | STABILIZE | 67.0 | 6 | 35 | 3 | 12.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12232004851102829 | 0.0 | 0.0 | +— / -e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 3-5 | 142 | BUY | STABILIZE | 67.0 | 6 | 46 | 4 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7297977209091187 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -— |
| Jogador 5 | 3-5 | 143 | BUY | STABILIZE | 67.0 | 6 | 45 | 4 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32919439673423767 | 0.0 | 0.0 | +c3a766c4-2db6-4b3f-88e9-a855fef1e6f6 / -— |
| Jogador 5 | 3-5 | 144 | BUY | STABILIZE | 67.0 | 6 | 43 | 4 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10879375040531158 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-5 | 145 | BUY | STABILIZE | 67.0 | 6 | 40 | 4 | 12.0 | Enfeitiçador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17587600648403168 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 146 | SELL | STABILIZE | 67.0 | 6 | 37 | 3 | 12.0 | Enfeitiçador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2628953754901886 | 0.0 | 0.0 | +— / -9bbd1da9-6a26-472c-912e-165ea4031b90 |
| Jogador 5 | 3-5 | 147 | SELL | STABILIZE | 67.0 | 6 | 40 | 4 | 12.0 | Enfeitiçador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3956666588783264 | 0.0 | 0.0 | +— / -4af85188-f11e-4aca-8165-ba8e7f535670 |
| Jogador 5 | 3-5 | 148 | SELL | STABILIZE | 67.0 | 6 | 43 | 4 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6309999823570251 | 0.0 | 0.0 | +— / -c3a766c4-2db6-4b3f-88e9-a855fef1e6f6 |
| Jogador 5 | 3-5 | 149 | SELL | STABILIZE | 67.0 | 6 | 45 | 4 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7851359248161316 | 0.0 | 0.0 | +— / -ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 3-5 | 150 | SELL | STABILIZE | 67.0 | 6 | 46 | 4 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.876785159111023 | 0.0 | 0.0 | +— / -8a4e95ea-d35a-4690-9313-126b5d86773e |
| Jogador 5 | 3-6 | 152 | BUY | STABILIZE | 58.0 | 6 | 58 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09967013448476791 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -— |
| Jogador 5 | 3-6 | 153 | BUY | STABILIZE | 58.0 | 6 | 57 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03361637145280838 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-6 | 154 | BUY | STABILIZE | 58.0 | 6 | 55 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26499512791633606 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-6 | 155 | SELL | STABILIZE | 58.0 | 6 | 53 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39629998803138733 | 0.0 | 0.0 | +— / -bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 |
| Jogador 5 | 3-6 | 156 | SELL | STABILIZE | 58.0 | 6 | 54 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32760000228881836 | 0.0 | 0.0 | +— / -1457cd1e-c240-4ce5-9217-a91bddfc8807 |
| Jogador 5 | 3-6 | 157 | SELL | STABILIZE | 58.0 | 6 | 56 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4004584848880768 | 0.0 | 0.0 | +— / -750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 5 | 3-6 | 158 | BUY | STABILIZE | 58.0 | 6 | 58 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22745679318904877 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 5 | 3-6 | 159 | SELL | STABILIZE | 58.0 | 6 | 57 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3429666757583618 | 0.0 | 0.0 | +— / -82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 |
| Jogador 5 | 3-7 | 161 | BUY | STABILIZE | 58.0 | 6 | 69 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4122706949710846 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -— |
| Jogador 5 | 3-7 | 162 | BUY | STABILIZE | 58.0 | 6 | 67 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03986220806837082 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 163 | BUY | STABILIZE | 58.0 | 6 | 64 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03276446834206581 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 5 | 3-7 | 164 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 61 | 5 | 12.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39007866382598877 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 165 | SELL | STABILIZE | 58.0 | 6 | 61 | 5 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3549000024795532 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 5 | 3-7 | 166 | SELL | STABILIZE | 58.0 | 6 | 64 | 5 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4962039589881897 | 0.0 | 0.0 | +— / -4d8c374c-264c-47d9-8cfc-78cbf64ceda0 |
| Jogador 5 | 3-7 | 167 | BUY | STABILIZE | 58.0 | 6 | 66 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01631578616797924 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 168 | SELL | STABILIZE | 58.0 | 6 | 64 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34824424982070923 | 0.0 | 0.0 | +— / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 5 | 3-7 | 169 | BUY | STABILIZE | 58.0 | 6 | 66 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25179389119148254 | 0.0 | 0.0 | +9b509d0e-ae62-4bfa-a551-f46ea68c64f4 / -— |
| Jogador 5 | 4-1 | 171 | BUY | STABILIZE | 58.0 | 6 | 75 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9885290861129761 | 0.0 | 0.0 | +0c07379e-5dd1-42e9-aa7a-a764f949deee / -— |
| Jogador 5 | 4-1 | 172 | BUY | STABILIZE | 58.0 | 6 | 73 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.424236536026001 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 173 | BUY | STABILIZE | 58.0 | 6 | 70 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11605177819728851 | 0.0 | 0.0 | +f6de9b7d-1373-459e-b34a-7b878d1a1268 / -— |
| Jogador 5 | 4-1 | 174 | CRAFT_AND_EQUIP | STABILIZE | 58.0 | 6 | 69 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14272932708263397 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 175 | CRAFT_AND_EQUIP | STABILIZE | 58.0 | 6 | 69 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13275662064552307 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 176 | BUY | STABILIZE | 58.0 | 6 | 69 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16797590255737305 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 5 | 4-1 | 177 | SELL | STABILIZE | 58.0 | 6 | 66 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02630000002682209 | 0.0 | 0.0 | +— / -9b509d0e-ae62-4bfa-a551-f46ea68c64f4 |
| Jogador 5 | 4-1 | 178 | BUY | STABILIZE | 58.0 | 6 | 67 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26609545946121216 | 0.0 | 0.0 | +6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 / -— |
| Jogador 5 | 4-2 | 180 | BUY | STABILIZE | 47.0 | 6 | 76 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.862919807434082 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 5 | 4-3 | 182 | BUY | STABILIZE | 36.0 | 6 | 86 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9592413306236267 | 0.0 | 0.0 | +333b0a0b-8868-40b2-96e9-71e468c5dd1f / -02c39b42-90d5-4e01-9380-460b6c1cb993,9593a62e-442f-410a-8a0c-7d781e2487cc |
| Jogador 5 | 4-3 | 183 | BUY | STABILIZE | 36.0 | 6 | 85 | 5 | 14.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24590641260147095 | 0.0 | 0.0 | +72c247af-bdc3-410c-98dd-dd72b56f2818 / -— |
| Jogador 5 | 4-3 | 184 | MOVE_BENCH | STABILIZE | 36.0 | 6 | 82 | 5 | 14.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5645802021026611 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 185 | BUY | STABILIZE | 36.0 | 6 | 82 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07411979138851166 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 5 | 4-3 | 186 | SELL | STABILIZE | 36.0 | 6 | 79 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -333b0a0b-8868-40b2-96e9-71e468c5dd1f |
| Jogador 5 | 4-3 | 187 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 6 | 82 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14583976566791534 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 188 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 6 | 82 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12627166509628296 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 189 | BUY | STABILIZE | 36.0 | 6 | 82 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005579232703894377 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -— |
| Jogador 5 | 4-4 | 191 | SELL | ALL_IN | 23.0 | 6 | 91 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 |
| Jogador 5 | 4-4 | 192 | BUY | ALL_IN | 23.0 | 6 | 92 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48143577575683594 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -— |
| Jogador 5 | 4-4 | 193 | SELL | ALL_IN | 23.0 | 6 | 90 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021820375695824623 | 0.0 | 0.0 | +— / -f6de9b7d-1373-459e-b34a-7b878d1a1268 |
| Jogador 5 | 4-4 | 194 | BUY | ALL_IN | 23.0 | 6 | 91 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3772119879722595 | 0.0 | 0.0 | +e4764e13-e26d-4358-980a-c7c625e26726 / -— |
| Jogador 5 | 4-4 | 195 | SELL | ALL_IN | 23.0 | 6 | 90 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -27a4bd22-9c1f-4f9f-9192-06ea4933feb5 |
| Jogador 5 | 4-4 | 196 | BUY | ALL_IN | 23.0 | 6 | 93 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09111238270998001 | 0.0 | 0.0 | +b80a9778-b2ce-411b-8d08-24549c04367c / -— |
| Jogador 5 | 4-5 | 198 | SELL | ALL_IN | 23.0 | 6 | 102 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -b80a9778-b2ce-411b-8d08-24549c04367c |
| Jogador 5 | 4-5 | 199 | BUY | ALL_IN | 23.0 | 6 | 104 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8955339193344116 | 0.0 | 0.0 | +c49cf468-6fa4-4d94-bc3a-9dc8f7111626 / -— |
| Jogador 5 | 4-5 | 200 | SELL | ALL_IN | 23.0 | 6 | 103 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07135427743196487 | 0.0 | 0.0 | +— / -72c247af-bdc3-410c-98dd-dd72b56f2818 |
| Jogador 5 | 4-6 | 202 | BUY | ALL_IN | 11.0 | 6 | 117 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0331119298934937 | 0.0 | 0.0 | +738fea60-6b44-40f1-9936-43accf852bd7 / -— |
| Jogador 5 | 4-6 | 203 | SELL | ALL_IN | 11.0 | 6 | 114 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5891333222389221 | 0.0 | 0.0 | +— / -ad19ac66-9f86-4c29-8ae7-7222164aece1 |
| Jogador 5 | 4-6 | 204 | BUY | ALL_IN | 11.0 | 6 | 116 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047566551715135574 | 0.0 | 0.0 | +98b72340-a402-45bc-9493-71263e3168d6 / -— |
| Jogador 5 | 4-6 | 205 | SELL | ALL_IN | 11.0 | 6 | 113 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -d8ecc66e-097d-4caa-a657-90fcd1286c2b |
| Jogador 5 | 4-6 | 206 | BUY | ALL_IN | 11.0 | 6 | 115 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20959481596946716 | 0.0 | 0.0 | +f3e882b5-333e-44e3-ae82-cacacc8b1137 / -— |
| Jogador 5 | 4-6 | 207 | SELL | ALL_IN | 11.0 | 6 | 114 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -f3e882b5-333e-44e3-ae82-cacacc8b1137 |
| Jogador 5 | 4-7 | 209 | BUY | ALL_IN | 11.0 | 6 | 126 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9205695390701294 | 0.0 | 0.0 | +f8a93323-530e-4f9c-99d7-a5ec83b78992 / -— |
| Jogador 5 | 4-7 | 210 | SELL | ALL_IN | 11.0 | 6 | 125 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -98b72340-a402-45bc-9493-71263e3168d6 |
| Jogador 5 | 5-1 | 212 | BUY | ALL_IN | 11.0 | 7 | 139 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7632207870483398 | 0.0 | 0.0 | +ecf369a7-649e-45fe-ad90-8f29e1714fe6 / -— |
| Jogador 5 | 5-1 | 213 | CRAFT_AND_EQUIP | ALL_IN | 11.0 | 7 | 136 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20922516286373138 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 214 | CRAFT_AND_EQUIP | ALL_IN | 11.0 | 7 | 136 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17105743288993835 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 215 | MOVE_BENCH | ALL_IN | 11.0 | 7 | 136 | 5 | 20.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7733797430992126 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 216 | MOVE_BENCH | ALL_IN | 11.0 | 7 | 136 | 5 | 16.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5852563381195068 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 217 | BUY | ALL_IN | 11.0 | 7 | 136 | 5 | 22.0 | Enfeitiçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06501588970422745 | 0.0 | 0.0 | +91966802-adc2-46d2-9e7e-194283bca85c / -— |
| Jogador 5 | 5-1 | 218 | SELL | ALL_IN | 11.0 | 7 | 132 | 5 | 22.0 | Enfeitiçador/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -91966802-adc2-46d2-9e7e-194283bca85c |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | -0.15334774553775787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Sentry | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17399217188358307 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21841175854206085 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0372217893600464 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039901405572891235 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012773334980010986 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011599136516451836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 28 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5737176537513733 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0251747369766235 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 38 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 48 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1287449449300766 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 49 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15242958068847656 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 50 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2891472280025482 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 51 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 52 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09078851342201233 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 56 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2620476186275482 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 57 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24680210649967194 | 0.0 | 0.0 | +048e9074-b134-49ed-a105-88dca63d1aa3 / -— |
| Jogador 6 | 2-2 | 58 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -6a01f661-884f-4c25-9dbe-384a6fe3a5e6 |
| Jogador 6 | 2-2 | 59 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07944674044847488 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 60 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 63 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2885243594646454 | 0.0 | 0.0 | +b1ecd1fa-793c-40ad-a9e3-9d35d5030339 / -— |
| Jogador 6 | 2-3 | 64 | BUY | STABILIZE | 89.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18150849640369415 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 65 | BUY | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23913662135601044 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 66 | SELL | STABILIZE | 89.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1448529064655304 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-3 | 67 | SELL | STABILIZE | 89.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15159516036510468 | 0.0 | 0.0 | +— / -b1ecd1fa-793c-40ad-a9e3-9d35d5030339 |
| Jogador 6 | 2-3 | 68 | PASS | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 72 | BUY | STABILIZE | 85.0 | 5 | 9 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18313488364219666 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 73 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24053487181663513 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 74 | BUY | STABILIZE | 85.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8068550229072571 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 75 | BUY_XP | STABILIZE | 85.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 76 | SELL | STABILIZE | 85.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013266666792333126 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-4 | 77 | SELL | STABILIZE | 85.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1095648929476738 | 0.0 | 0.0 | +— / -048e9074-b134-49ed-a105-88dca63d1aa3 |
| Jogador 6 | 2-4 | 78 | BUY_XP | STABILIZE | 85.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 79 | SELL | STABILIZE | 85.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14383192360401154 | 0.0 | 0.0 | +— / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 |
| Jogador 6 | 2-4 | 80 | SELL | STABILIZE | 85.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.143825501203537 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-5 | 82 | BUY | STABILIZE | 85.0 | 5 | 10 | 1 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8596822023391724 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 83 | BUY | STABILIZE | 85.0 | 5 | 9 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28840115666389465 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 84 | BUY_XP | STABILIZE | 85.0 | 5 | 7 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 85 | SELL | STABILIZE | 85.0 | 5 | 3 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4522579312324524 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-5 | 86 | BUY_XP | STABILIZE | 85.0 | 5 | 5 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 87 | SELL | STABILIZE | 85.0 | 5 | 1 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49317634105682373 | 0.0 | 0.0 | +— / -a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 2-5 | 88 | BUY_XP | STABILIZE | 85.0 | 5 | 4 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 89 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 0 | 0 | 8.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21166108548641205 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 90 | SELL | STABILIZE | 85.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-6 | 92 | BUY | STABILIZE | 80.0 | 6 | 9 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32035812735557556 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 93 | BUY_XP | STABILIZE | 80.0 | 6 | 6 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 94 | SELL | STABILIZE | 80.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18617047369480133 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 2-6 | 95 | BUY_XP | STABILIZE | 80.0 | 6 | 5 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006841098889708519 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 97 | SELL | STABILIZE | 80.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-6 | 98 | BUY | STABILIZE | 80.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15727946162223816 | 0.0 | 0.0 | +2a7dd07f-3b48-489c-8822-9ec2434a01cf / -— |
| Jogador 6 | 2-6 | 99 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6007081270217896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 100 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020107917487621307 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 102 | BUY | STABILIZE | 80.0 | 6 | 6 | 0 | 12.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3116063177585602 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 103 | BUY | STABILIZE | 80.0 | 6 | 3 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3593784272670746 | 0.0 | 0.0 | +dc83202b-476c-4438-90aa-a615b764b7e4 / -— |
| Jogador 6 | 2-7 | 104 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 2 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11269524693489075 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 105 | SELL | STABILIZE | 80.0 | 6 | 2 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05471719801425934 | 0.0 | 0.0 | +— / -2a7dd07f-3b48-489c-8822-9ec2434a01cf |
| Jogador 6 | 2-7 | 106 | SELL | STABILIZE | 80.0 | 6 | 4 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16103507578372955 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 2-7 | 107 | SELL | STABILIZE | 80.0 | 6 | 7 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4934403598308563 | 0.0 | 0.0 | +— / -dc83202b-476c-4438-90aa-a615b764b7e4 |
| Jogador 6 | 2-7 | 108 | BUY | STABILIZE | 80.0 | 6 | 8 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11238756030797958 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 2-7 | 109 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 110 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007686061784625053 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 112 | BUY | STABILIZE | 80.0 | 6 | 10 | 1 | 12.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1791955679655075 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 113 | BUY | STABILIZE | 80.0 | 6 | 7 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11093812435865402 | 0.0 | 0.0 | +91f05e8c-f467-4f22-9cb0-c814ffa93198 / -— |
| Jogador 6 | 3-1 | 114 | CRAFT_AND_EQUIP | STABILIZE | 80.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2438707947731018 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 115 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18740111589431763 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 116 | BUY_XP | STABILIZE | 80.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 117 | SELL | STABILIZE | 80.0 | 6 | 1 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -91f05e8c-f467-4f22-9cb0-c814ffa93198 |
| Jogador 6 | 3-1 | 118 | SELL | STABILIZE | 80.0 | 6 | 3 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09529222548007965 | 0.0 | 0.0 | +— / -9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 3-1 | 119 | BUY | STABILIZE | 80.0 | 6 | 6 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07470742613077164 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-2 | 121 | BUY | STABILIZE | 71.0 | 6 | 7 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379749059677124 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -18934be2-4988-4f62-9f62-07ba151231f2,53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 3-2 | 122 | BUY | STABILIZE | 71.0 | 6 | 6 | 0 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8152494430541992 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 123 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 5 | 0 | 10.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19235479831695557 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 124 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31521672010421753 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 125 | BUY | STABILIZE | 71.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010253402404487133 | 0.0 | 0.0 | +4278eb73-acda-419d-bf9e-53a29ff6900d / -— |
| Jogador 6 | 3-2 | 126 | MOVE_BOARD | STABILIZE | 71.0 | 6 | 4 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002517454558983445 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 127 | BUY | STABILIZE | 71.0 | 6 | 4 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013922437094151974 | 0.0 | 0.0 | +9204a42c-6310-4b08-9bc7-8a2e786b077a / -— |
| Jogador 6 | 3-2 | 128 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 2 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4060199558734894 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 130 | BUY | STABILIZE | 61.0 | 6 | 8 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2825993597507477 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-4 | 132 | BUY | STABILIZE | 61.0 | 6 | 11 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19871605932712555 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -— |
| Jogador 6 | 3-4 | 133 | BUY | STABILIZE | 61.0 | 6 | 7 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27566537261009216 | 0.0 | 0.0 | +ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c / -— |
| Jogador 6 | 3-4 | 134 | BUY | STABILIZE | 61.0 | 6 | 4 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26013150811195374 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 6 | 3-4 | 135 | MOVE_BOARD | STABILIZE | 61.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0010989549336954951 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 136 | MOVE_BOARD | STABILIZE | 61.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02144087664783001 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 137 | PASS | STABILIZE | 61.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 142 | BUY | STABILIZE | 61.0 | 6 | 6 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03172376751899719 | 0.0 | 0.0 | +9443e3b5-f0a2-4ab7-8378-907a3d2bccaa / -— |
| Jogador 6 | 3-5 | 143 | BUY | STABILIZE | 61.0 | 6 | 4 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03857067599892616 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 144 | MOVE_BOARD | STABILIZE | 61.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013200582470744848 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 145 | MOVE_BOARD | STABILIZE | 61.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01782459020614624 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 146 | MOVE_BOARD | STABILIZE | 61.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05508087947964668 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 147 | PASS | STABILIZE | 61.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 152 | SELL | STABILIZE | 61.0 | 6 | 8 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29108887910842896 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 3-6 | 153 | BUY | STABILIZE | 61.0 | 6 | 11 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.695927619934082 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 154 | EQUIP_FROM_INVENTORY | STABILIZE | 61.0 | 6 | 8 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15578892827033997 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 155 | EQUIP_FROM_INVENTORY | STABILIZE | 61.0 | 6 | 8 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14461596310138702 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 156 | SELL | STABILIZE | 61.0 | 6 | 8 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043433334678411484 | 0.0 | 0.0 | +— / -4278eb73-acda-419d-bf9e-53a29ff6900d |
| Jogador 6 | 3-6 | 157 | BUY | STABILIZE | 61.0 | 6 | 9 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4961026906967163 | 0.0 | 0.0 | +604cc5dc-6c20-4d5a-b3a7-8862adfe1930 / -— |
| Jogador 6 | 3-6 | 158 | SELL | STABILIZE | 61.0 | 6 | 7 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03861474245786667 | 0.0 | 0.0 | +— / -9443e3b5-f0a2-4ab7-8378-907a3d2bccaa |
| Jogador 6 | 3-6 | 159 | MOVE_BOARD | STABILIZE | 61.0 | 6 | 9 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01941259205341339 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 161 | BUY | STABILIZE | 51.0 | 6 | 14 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02002842165529728 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 162 | SELL | STABILIZE | 51.0 | 6 | 10 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007366666570305824 | 0.0 | 0.0 | +— / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 |
| Jogador 6 | 3-7 | 163 | BUY | STABILIZE | 51.0 | 6 | 13 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06778868287801743 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 6 | 3-7 | 164 | SELL | STABILIZE | 51.0 | 6 | 10 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007836501463316381 | 0.0 | 0.0 | +— / -665661af-7240-4a65-bf3d-f4ecf3532a85 |
| Jogador 6 | 3-7 | 165 | SELL | STABILIZE | 51.0 | 6 | 13 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3996666669845581 | 0.0 | 0.0 | +— / -891aea62-e06a-46d4-8250-a3d4a56e847d |
| Jogador 6 | 3-7 | 166 | SELL | STABILIZE | 51.0 | 6 | 17 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5083333253860474 | 0.0 | 0.0 | +— / -604cc5dc-6c20-4d5a-b3a7-8862adfe1930 |
| Jogador 6 | 3-7 | 167 | BUY | STABILIZE | 51.0 | 6 | 19 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09187858551740646 | 0.0 | 0.0 | +3a40e3a6-b3e3-4f35-8fa0-e81c89d72db6 / -— |
| Jogador 6 | 3-7 | 168 | MOVE_BOARD | STABILIZE | 51.0 | 6 | 18 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00025248865131288767 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 169 | MOVE_BOARD | STABILIZE | 51.0 | 6 | 18 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014500446617603302 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 171 | BUY | STABILIZE | 51.0 | 6 | 24 | 2 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02284233085811138 | 0.0 | 0.0 | +78525c90-c4d2-425d-ba90-a03664c60a28 / -— |
| Jogador 6 | 4-1 | 172 | CRAFT_AND_EQUIP | STABILIZE | 51.0 | 6 | 22 | 2 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2543240189552307 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 173 | CRAFT_AND_EQUIP | STABILIZE | 51.0 | 6 | 22 | 2 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24980567395687103 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 174 | BUY | STABILIZE | 51.0 | 6 | 22 | 2 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16768597066402435 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -— |
| Jogador 6 | 4-1 | 175 | SELL | STABILIZE | 51.0 | 6 | 19 | 1 | 24.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07123333215713501 | 0.0 | 0.0 | +— / -3a40e3a6-b3e3-4f35-8fa0-e81c89d72db6 |
| Jogador 6 | 4-1 | 176 | SELL | STABILIZE | 51.0 | 6 | 20 | 2 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -9204a42c-6310-4b08-9bc7-8a2e786b077a |
| Jogador 6 | 4-1 | 177 | BUY | STABILIZE | 51.0 | 6 | 22 | 2 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08986582607030869 | 0.0 | 0.0 | +a8a8381a-f3a8-45ec-9106-293d73fca0c8 / -— |
| Jogador 6 | 4-1 | 178 | SELL | STABILIZE | 51.0 | 6 | 20 | 2 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37166666984558105 | 0.0 | 0.0 | +— / -a8a8381a-f3a8-45ec-9106-293d73fca0c8 |
| Jogador 6 | 4-2 | 180 | BUY | STABILIZE | 51.0 | 7 | 30 | 3 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43237924575805664 | 0.0 | 0.0 | +ef54ddfd-f436-4813-9585-cb652488ffa3 / -— |
| Jogador 6 | 4-3 | 182 | BUY | STABILIZE | 51.0 | 7 | 37 | 3 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04305680841207504 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -— |
| Jogador 6 | 4-3 | 183 | BUY | STABILIZE | 51.0 | 7 | 33 | 3 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.040439944714307785 | 0.0 | 0.0 | +a9588010-57fa-4baf-b226-a30f519342e7 / -— |
| Jogador 6 | 4-3 | 184 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 31 | 3 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 185 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 31 | 3 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010798065923154354 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 186 | PASS | STABILIZE | 51.0 | 7 | 31 | 3 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03642857074737549 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 191 | SELL | STABILIZE | 51.0 | 7 | 41 | 4 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -a9588010-57fa-4baf-b226-a30f519342e7 |
| Jogador 6 | 4-4 | 192 | BUY | STABILIZE | 51.0 | 7 | 43 | 4 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3723260462284088 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -— |
| Jogador 6 | 4-4 | 193 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 42 | 4 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004157864023000002 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 194 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 42 | 4 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 195 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 42 | 4 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016892902553081512 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 196 | PASS | STABILIZE | 51.0 | 7 | 42 | 4 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044285714626312256 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 198 | SELL | STABILIZE | 51.0 | 7 | 52 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 6 | 4-5 | 199 | BUY | STABILIZE | 51.0 | 7 | 55 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03531033918261528 | 0.0 | 0.0 | +8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e / -— |
| Jogador 6 | 4-5 | 200 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 54 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 202 | SELL | STABILIZE | 40.0 | 7 | 64 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02516504004597664 | 0.0 | 0.0 | +— / -8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e |
| Jogador 6 | 4-6 | 203 | BUY | STABILIZE | 40.0 | 7 | 65 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8809913396835327 | 0.0 | 0.0 | +99182042-c4b9-4801-b66a-1f4432d301f3 / -— |
| Jogador 6 | 4-6 | 204 | MOVE_BOARD | STABILIZE | 40.0 | 7 | 61 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002343412721529603 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 205 | MOVE_BOARD | STABILIZE | 40.0 | 7 | 61 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014559872448444366 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 206 | MOVE_BOARD | STABILIZE | 40.0 | 7 | 61 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015008216723799706 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 207 | PASS | STABILIZE | 40.0 | 7 | 61 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09697151929140091 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 209 | SELL | STABILIZE | 40.0 | 7 | 72 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013887758366763592 | 0.0 | 0.0 | +— / -03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 |
| Jogador 6 | 4-7 | 210 | BUY | STABILIZE | 40.0 | 7 | 76 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8871738910675049 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 6 | 5-1 | 212 | CRAFT_AND_EQUIP | STABILIZE | 40.0 | 7 | 83 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10984151065349579 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 213 | CRAFT_AND_EQUIP | STABILIZE | 40.0 | 7 | 83 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15775145590305328 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 214 | SELL | STABILIZE | 40.0 | 7 | 83 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057182177901268005 | 0.0 | 0.0 | +— / -ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c |
| Jogador 6 | 5-1 | 215 | BUY | STABILIZE | 40.0 | 7 | 86 | 5 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.014274001121521 | 0.0 | 0.0 | +811fcf1f-2023-4c36-a961-d61cb0dd68d0 / -333cdd27-0114-4d36-8ffa-e79b0f43b8e8,cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 5-1 | 216 | BUY | STABILIZE | 40.0 | 7 | 83 | 5 | 30.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34934377670288086 | 0.0 | 0.0 | +02e125a0-3563-47ec-a82a-cba5178731dd / -— |
| Jogador 6 | 5-1 | 217 | BUY | STABILIZE | 40.0 | 7 | 79 | 5 | 30.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01712491549551487 | 0.0 | 0.0 | +952ea2b4-387d-455d-b1ad-fb0de8c46e47 / -— |
| Jogador 6 | 5-1 | 218 | MOVE_BOARD | STABILIZE | 40.0 | 7 | 77 | 5 | 30.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 220 | SELL | STABILIZE | 40.0 | 7 | 87 | 5 | 30.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -811fcf1f-2023-4c36-a961-d61cb0dd68d0 |
| Jogador 6 | 5-3 | 222 | BUY | ALL_IN | 25.0 | 7 | 105 | 5 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9375255107879639 | 0.0 | 0.0 | +22f3c707-2635-41cb-a228-10d5ed1883b3 / -— |
| Jogador 6 | 5-3 | 223 | SELL | ALL_IN | 25.0 | 7 | 102 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015463006682693958 | 0.0 | 0.0 | +— / -952ea2b4-387d-455d-b1ad-fb0de8c46e47 |
| Jogador 6 | 5-3 | 224 | BUY | ALL_IN | 25.0 | 7 | 104 | 5 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.050434947013855 | 0.0 | 0.0 | +4e6b6f57-7f94-46ba-b832-c3198d4a5949 / -3cb4d077-df9a-4fd2-9a68-7301aff1b657,3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 5-3 | 225 | EQUIP_FROM_INVENTORY | ALL_IN | 25.0 | 7 | 103 | 5 | 26.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10645822435617447 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 226 | EQUIP_FROM_INVENTORY | ALL_IN | 25.0 | 7 | 103 | 5 | 26.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1126796156167984 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 227 | MOVE_BENCH | ALL_IN | 25.0 | 7 | 103 | 5 | 26.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.2947206199169159 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 229 | BUY | ALL_IN | 25.0 | 7 | 113 | 5 | 32.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.5934171080589294 | 0.0 | 0.0 | +b2517873-8317-401b-8461-1d86969edbd7 / -— |
| Jogador 6 | 5-4 | 230 | EQUIP_FROM_INVENTORY | ALL_IN | 25.0 | 7 | 109 | 5 | 32.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.16279873251914978 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 232 | BUY | ALL_IN | 25.0 | 7 | 119 | 5 | 40.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3774232268333435 | 0.0 | 0.0 | +91eb044c-6989-4b6a-a9fa-a59f75b56743 / -— |
| Jogador 6 | 5-5 | 233 | MOVE_BOARD | ALL_IN | 25.0 | 7 | 116 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0010782917961478233 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 234 | MOVE_BOARD | ALL_IN | 25.0 | 7 | 116 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013977148570120335 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 235 | PASS | ALL_IN | 25.0 | 7 | 116 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.52354496717453 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 239 | SELL | ALL_IN | 8.0 | 7 | 127 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7214999794960022 | 0.0 | 0.0 | +— / -4e6b6f57-7f94-46ba-b832-c3198d4a5949 |
| Jogador 6 | 5-6 | 240 | BUY | ALL_IN | 8.0 | 7 | 130 | 5 | 40.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.903853714466095 | 0.0 | 0.0 | +3c5f5211-f30d-44e7-ac68-0ce513a3d614 / -— |
| Jogador 6 | 5-7 | 242 | EQUIP_FROM_INVENTORY | ALL_IN | 8.0 | 7 | 138 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08674684166908264 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 243 | EQUIP_FROM_INVENTORY | ALL_IN | 8.0 | 7 | 138 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13381914794445038 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 244 | EQUIP_FROM_INVENTORY | ALL_IN | 8.0 | 7 | 138 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08622700721025467 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 245 | SELL | ALL_IN | 8.0 | 7 | 138 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7189000248908997 | 0.0 | 0.0 | +— / -e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 |
| Jogador 6 | 5-7 | 246 | BUY | ALL_IN | 8.0 | 7 | 139 | 5 | 40.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5255395770072937 | 0.0 | 0.0 | +40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b / -— |
| Jogador 6 | 5-7 | 247 | MOVE_BOARD | ALL_IN | 8.0 | 7 | 138 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.78774153534323e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 249 | EQUIP_FROM_INVENTORY | ALL_IN | 8.0 | 7 | 149 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.002940717851743102 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 250 | SELL | ALL_IN | 8.0 | 7 | 149 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7189000248908997 | 0.0 | 0.0 | +— / -40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b |
| Jogador 6 | 6-2 | 252 | BUY | ALL_IN | 8.0 | 7 | 161 | 5 | 40.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09215020388364792 | 0.0 | 0.0 | +c4ec99e0-d973-42e9-a20e-1a9e7f5bf89a / -— |
| Jogador 6 | 6-2 | 253 | SELL | ALL_IN | 8.0 | 7 | 158 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -c4ec99e0-d973-42e9-a20e-1a9e7f5bf89a |
| Jogador 6 | 6-2 | 254 | BUY | ALL_IN | 8.0 | 7 | 161 | 5 | 40.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09214986115694046 | 0.0 | 0.0 | +4b4293ce-1cca-473e-8c07-b441686985ac / -— |
| Jogador 6 | 6-2 | 255 | MOVE_BOARD | ALL_IN | 8.0 | 7 | 158 | 5 | 40.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -6.0871807363582775e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589178562164307 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2799173593521118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.143971249461174 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012334865517914295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4041116237640381 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0486204624176025 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23078222572803497 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004352054558694363 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005867671221494675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0368462800979614 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2461363673210144 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007539904909208417 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1995791792869568 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 41 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8273932933807373 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 49 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1997172236442566 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 50 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24539005756378174 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 51 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3010398745536804 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 52 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4380403161048889 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 56 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.04757559299469 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 57 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15447039902210236 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 59 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17915749549865723 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5971917510032654 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 63 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0474237203598022 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 64 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8417679667472839 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 65 | PASS | STABILIZE | 96.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 72 | BUY | STABILIZE | 96.0 | 5 | 9 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32718926668167114 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 73 | BUY_XP | STABILIZE | 96.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 74 | SELL | STABILIZE | 96.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15427015721797943 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-4 | 75 | BUY_XP | STABILIZE | 96.0 | 5 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 76 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023537367582321167 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 77 | SELL | STABILIZE | 96.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11566666513681412 | 0.0 | 0.0 | +— / -0cf5c315-d2f3-4854-a95b-07912b83ea81 |
| Jogador 7 | 2-4 | 78 | SELL | STABILIZE | 96.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17941522598266602 | 0.0 | 0.0 | +— / -2c7e844d-925a-43bb-8be8-65a71d11f964 |
| Jogador 7 | 2-4 | 79 | BUY_XP | STABILIZE | 96.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 80 | SELL | STABILIZE | 96.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5408936142921448 | 0.0 | 0.0 | +— / -dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 7 | 2-5 | 82 | BUY | STABILIZE | 96.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32548120617866516 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 83 | BUY | STABILIZE | 96.0 | 5 | 5 | 0 | 12.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37886664271354675 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 84 | SELL | STABILIZE | 96.0 | 5 | 4 | 0 | 12.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3911089301109314 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 2-5 | 85 | BUY_XP | STABILIZE | 96.0 | 5 | 5 | 0 | 12.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 86 | SELL | STABILIZE | 96.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5710421800613403 | 0.0 | 0.0 | +— / -caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 7 | 2-5 | 87 | BUY | STABILIZE | 96.0 | 5 | 2 | 0 | 12.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007893450558185577 | 0.0 | 0.0 | +bd48de5d-f06b-401c-83a0-2ca5ba1043a4 / -— |
| Jogador 7 | 2-5 | 88 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010432925075292587 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 89 | SELL | STABILIZE | 96.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0663333311676979 | 0.0 | 0.0 | +— / -bd48de5d-f06b-401c-83a0-2ca5ba1043a4 |
| Jogador 7 | 2-5 | 90 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 2 | 0 | 12.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42109689116477966 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 92 | BUY | STABILIZE | 96.0 | 6 | 9 | 0 | 14.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.393207311630249 | 0.0 | 0.0 | +a146f2d5-4da5-4c0e-bb09-de3177c72417 / -— |
| Jogador 7 | 2-6 | 93 | BUY | STABILIZE | 96.0 | 6 | 7 | 0 | 14.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3756110966205597 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 94 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 4 | 0 | 14.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3670167326927185 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 95 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 4 | 0 | 16.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 96 | PASS | STABILIZE | 96.0 | 6 | 4 | 0 | 16.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 100 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 4 | 0 | 16.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41025859117507935 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 102 | BUY | STABILIZE | 96.0 | 6 | 11 | 1 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15699231624603271 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 103 | BUY | STABILIZE | 96.0 | 6 | 8 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04985947906970978 | 0.0 | 0.0 | +ac02c0c4-a10d-497d-b6c1-d458ad7ae58c / -— |
| Jogador 7 | 2-7 | 104 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 6 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.615215822122991e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 105 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 6 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021677006036043167 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 106 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 6 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009606193751096725 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 107 | PASS | STABILIZE | 96.0 | 6 | 6 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 112 | BUY | STABILIZE | 96.0 | 6 | 12 | 1 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.19555523991584778 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 7 | 3-1 | 113 | CRAFT_AND_EQUIP | STABILIZE | 96.0 | 6 | 9 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10903526097536087 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 114 | BUY | STABILIZE | 96.0 | 6 | 9 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03624703735113144 | 0.0 | 0.0 | +5d00c8ab-55fb-42ec-b8ec-75011c7722fc / -— |
| Jogador 7 | 3-1 | 115 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013244417496025562 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 116 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005421887617558241 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 117 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015147446654736996 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 118 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01200094260275364 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 119 | PASS | STABILIZE | 96.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 121 | BUY | STABILIZE | 96.0 | 6 | 14 | 1 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5137566328048706 | 0.0 | 0.0 | +fa331d8d-1e0c-49b4-848e-8ad58859331c / -— |
| Jogador 7 | 3-2 | 122 | BUY | STABILIZE | 96.0 | 6 | 12 | 1 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6650556325912476 | 0.0 | 0.0 | +96bf8f0a-9fe1-4182-95dc-903c1e623983 / -ac02c0c4-a10d-497d-b6c1-d458ad7ae58c,fa331d8d-1e0c-49b4-848e-8ad58859331c |
| Jogador 7 | 3-2 | 123 | BUY | STABILIZE | 96.0 | 6 | 10 | 1 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09913497418165207 | 0.0 | 0.0 | +46320c4e-6bc0-49d6-b150-be378fa422cf / -— |
| Jogador 7 | 3-2 | 124 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0028309710323810577 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 125 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013163859024643898 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 126 | PASS | STABILIZE | 96.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 130 | BUY | STABILIZE | 96.0 | 6 | 15 | 1 | 22.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7178996801376343 | 0.0 | 0.0 | +652ff984-c3ac-48d7-9fb6-e95aed0a047d / -242805ca-f275-4e04-a2f5-81e0b6680dd1,7159421f-b5ea-4d10-9cc5-59186d62983d |
| Jogador 7 | 3-4 | 132 | BUY | STABILIZE | 96.0 | 6 | 24 | 2 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8168454766273499 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -— |
| Jogador 7 | 3-4 | 133 | BUY | STABILIZE | 96.0 | 6 | 21 | 2 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8067120909690857 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -— |
| Jogador 7 | 3-4 | 134 | BUY | STABILIZE | 96.0 | 6 | 20 | 2 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14255230128765106 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 7 | 3-4 | 135 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 17 | 1 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005055433604866266 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 136 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 17 | 1 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029965795576572418 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 137 | PASS | STABILIZE | 96.0 | 6 | 17 | 1 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 142 | SELL | STABILIZE | 96.0 | 6 | 26 | 2 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -652ff984-c3ac-48d7-9fb6-e95aed0a047d |
| Jogador 7 | 3-5 | 143 | BUY | STABILIZE | 96.0 | 6 | 29 | 2 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7944182753562927 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 144 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 26 | 2 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01070492621511221 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 145 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 26 | 2 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014901653863489628 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 146 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 26 | 2 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015663504600524902 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 147 | PASS | STABILIZE | 96.0 | 6 | 26 | 2 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 152 | SELL | STABILIZE | 86.0 | 6 | 33 | 3 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -96bf8f0a-9fe1-4182-95dc-903c1e623983 |
| Jogador 7 | 3-6 | 153 | BUY | STABILIZE | 86.0 | 6 | 38 | 3 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01731950417160988 | 0.0 | 0.0 | +1726bcae-3006-426c-a6c7-4e317e10b637 / -— |
| Jogador 7 | 3-6 | 154 | SELL | STABILIZE | 86.0 | 6 | 34 | 3 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -5d00c8ab-55fb-42ec-b8ec-75011c7722fc |
| Jogador 7 | 3-6 | 155 | BUY | STABILIZE | 86.0 | 6 | 36 | 3 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.489857941865921 | 0.0 | 0.0 | +a1aa0280-2379-4d0b-a475-143c1a2f6c25 / -— |
| Jogador 7 | 3-6 | 156 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 32 | 3 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0010151122696697712 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 157 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 32 | 3 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015500168316066265 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 158 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 32 | 3 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 159 | PASS | STABILIZE | 86.0 | 6 | 32 | 3 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026000000536441803 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 161 | SELL | STABILIZE | 76.0 | 6 | 41 | 4 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01029349584132433 | 0.0 | 0.0 | +— / -46320c4e-6bc0-49d6-b150-be378fa422cf |
| Jogador 7 | 3-7 | 162 | BUY | STABILIZE | 76.0 | 6 | 44 | 4 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8752994537353516 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -ad1693cd-1ab5-43a9-8164-25929b8bd68e,f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 3-7 | 163 | BUY | STABILIZE | 76.0 | 6 | 41 | 4 | 26.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21600423753261566 | 0.0 | 0.0 | +1cba4955-961e-4efd-a291-e0a70bf72841 / -— |
| Jogador 7 | 3-7 | 164 | BUY | STABILIZE | 76.0 | 6 | 39 | 3 | 26.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23516149818897247 | 0.0 | 0.0 | +06fb62e5-6766-4156-bf7d-0da443a9b20c / -— |
| Jogador 7 | 3-7 | 165 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 36 | 3 | 26.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00040724582504481077 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 166 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 36 | 3 | 26.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01567666232585907 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 167 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 36 | 3 | 26.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013324865140020847 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 168 | PASS | STABILIZE | 76.0 | 6 | 36 | 3 | 26.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 171 | CRAFT_AND_EQUIP | STABILIZE | 76.0 | 6 | 45 | 4 | 26.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18210986256599426 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 172 | CRAFT_AND_EQUIP | STABILIZE | 76.0 | 6 | 45 | 4 | 26.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16295602917671204 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 173 | SELL | STABILIZE | 76.0 | 6 | 45 | 4 | 26.0 | Inferno/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5038999915122986 | 0.0 | 0.0 | +— / -8a52858d-da47-4de9-8e91-8612788cb8fd |
| Jogador 7 | 4-1 | 174 | BUY | STABILIZE | 76.0 | 6 | 53 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0011062015546485782 | 0.0 | 0.0 | +6a30a366-c631-429d-9523-af769cdf48a4 / -— |
| Jogador 7 | 4-1 | 175 | SELL | STABILIZE | 76.0 | 6 | 51 | 5 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -6a30a366-c631-429d-9523-af769cdf48a4 |
| Jogador 7 | 4-1 | 176 | BUY | STABILIZE | 76.0 | 6 | 53 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0489821583032608 | 0.0 | 0.0 | +cc56fedc-f555-4075-af15-6b5fb93a156f / -— |
| Jogador 7 | 4-1 | 177 | SELL | STABILIZE | 76.0 | 6 | 51 | 5 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016728518530726433 | 0.0 | 0.0 | +— / -cc56fedc-f555-4075-af15-6b5fb93a156f |
| Jogador 7 | 4-1 | 178 | BUY | STABILIZE | 76.0 | 6 | 53 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27718812227249146 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 7 | 4-2 | 180 | SELL | STABILIZE | 76.0 | 6 | 62 | 5 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -97d52b06-365b-44ad-b4f9-63e0f9503c8a |
| Jogador 7 | 4-3 | 182 | BUY | STABILIZE | 65.0 | 6 | 74 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8553037643432617 | 0.0 | 0.0 | +485dab1f-b3a1-4170-8ed6-c0035072ae9b / -— |
| Jogador 7 | 4-3 | 183 | SELL | STABILIZE | 65.0 | 6 | 72 | 5 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -06fb62e5-6766-4156-bf7d-0da443a9b20c |
| Jogador 7 | 4-3 | 184 | BUY | STABILIZE | 65.0 | 6 | 75 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3404257595539093 | 0.0 | 0.0 | +c7841e00-91da-410b-b00f-62f4bf32f666 / -— |
| Jogador 7 | 4-3 | 185 | SELL | STABILIZE | 65.0 | 6 | 72 | 5 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07013333588838577 | 0.0 | 0.0 | +— / -86c1ac55-598e-426a-86ea-64249f82b085 |
| Jogador 7 | 4-3 | 186 | BUY | STABILIZE | 65.0 | 6 | 75 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1500103622674942 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 7 | 4-3 | 187 | SELL | STABILIZE | 65.0 | 6 | 71 | 5 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -80c51b33-0a85-4f21-a797-9551aa10760f |
| Jogador 7 | 4-3 | 188 | BUY | STABILIZE | 65.0 | 6 | 75 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06255996972322464 | 0.0 | 0.0 | +17d5d3f2-999d-4788-852b-bda84adb4350 / -— |
| Jogador 7 | 4-3 | 189 | REROLL | STABILIZE | 65.0 | 6 | 74 | 5 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 191 | SELL | STABILIZE | 65.0 | 6 | 83 | 5 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026666666381061077 | 0.0 | 0.0 | +— / -17d5d3f2-999d-4788-852b-bda84adb4350 |
| Jogador 7 | 4-4 | 192 | BUY | STABILIZE | 65.0 | 6 | 84 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40590378642082214 | 0.0 | 0.0 | +1f7f2a48-1318-4fc6-87cc-03d557bf69ea / -— |
| Jogador 7 | 4-4 | 193 | SELL | STABILIZE | 65.0 | 6 | 83 | 5 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -1f7f2a48-1318-4fc6-87cc-03d557bf69ea |
| Jogador 7 | 4-4 | 194 | BUY | STABILIZE | 65.0 | 6 | 84 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008244396187365055 | 0.0 | 0.0 | +84a3b0f5-c448-4fe1-b001-5ceff2ed306a / -— |
| Jogador 7 | 4-4 | 195 | SELL | STABILIZE | 65.0 | 6 | 82 | 5 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02968207187950611 | 0.0 | 0.0 | +— / -84a3b0f5-c448-4fe1-b001-5ceff2ed306a |
| Jogador 7 | 4-4 | 196 | BUY | STABILIZE | 65.0 | 6 | 84 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05367837846279144 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -— |
| Jogador 7 | 4-5 | 198 | SELL | STABILIZE | 65.0 | 6 | 91 | 5 | 26.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 |
| Jogador 7 | 4-5 | 199 | BUY | STABILIZE | 65.0 | 6 | 94 | 5 | 26.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9624406695365906 | 0.0 | 0.0 | +a72137b3-498b-40e1-938a-639f56745f08 / -6c691ca5-c042-46de-8d64-493514f2d793,cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 4-5 | 200 | BUY | STABILIZE | 65.0 | 6 | 91 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9573186039924622 | 0.0 | 0.0 | +61362365-2cf7-40e4-95f9-98e28728fd39 / -1ff50c59-5133-459e-8bf1-d449c26efabf,4e206e09-40e3-4699-81cb-8aaf01109dea |
| Jogador 7 | 4-6 | 202 | BUY | STABILIZE | 65.0 | 6 | 102 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.012072205543518 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -1cba4955-961e-4efd-a291-e0a70bf72841,485dab1f-b3a1-4170-8ed6-c0035072ae9b |
| Jogador 7 | 4-6 | 203 | BUY | STABILIZE | 65.0 | 6 | 100 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019430391490459442 | 0.0 | 0.0 | +c65dacb1-5745-49d1-b7d4-e45d8e24aa84 / -— |
| Jogador 7 | 4-6 | 204 | BUY | STABILIZE | 65.0 | 6 | 98 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06259046494960785 | 0.0 | 0.0 | +51a5a5d7-c5ea-43e2-a521-22fe0275c231 / -— |
| Jogador 7 | 4-6 | 205 | MOVE_BENCH | STABILIZE | 65.0 | 6 | 95 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7038243412971497 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 206 | MOVE_BENCH | STABILIZE | 65.0 | 6 | 95 | 5 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3117094933986664 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 207 | PASS | STABILIZE | 65.0 | 6 | 95 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11115982383489609 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 209 | BUY | STABILIZE | 54.0 | 6 | 105 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35286128520965576 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -— |
| Jogador 7 | 4-7 | 210 | BUY | STABILIZE | 54.0 | 6 | 103 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24951665103435516 | 0.0 | 0.0 | +1388df2e-8cb4-4e29-8b30-776c29406917 / -— |
| Jogador 7 | 5-1 | 212 | CRAFT_AND_EQUIP | STABILIZE | 54.0 | 6 | 112 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15802302956581116 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 213 | CRAFT_AND_EQUIP | STABILIZE | 54.0 | 6 | 112 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12736651301383972 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 214 | SELL | STABILIZE | 54.0 | 6 | 112 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -50edcbf1-13cd-4f98-bf35-d5a474fbe20c |
| Jogador 7 | 5-1 | 215 | BUY | STABILIZE | 54.0 | 6 | 117 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8696871995925903 | 0.0 | 0.0 | +18d25cfb-d559-4efa-b708-c9987987590b / -— |
| Jogador 7 | 5-1 | 216 | SELL | STABILIZE | 54.0 | 6 | 115 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -a72137b3-498b-40e1-938a-639f56745f08 |
| Jogador 7 | 5-1 | 217 | BUY | STABILIZE | 54.0 | 6 | 123 | 5 | 26.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35133373737335205 | 0.0 | 0.0 | +58cbdbde-2151-438c-8897-902bef9bcd92 / -— |
| Jogador 7 | 5-1 | 218 | MOVE_BENCH | STABILIZE | 54.0 | 6 | 121 | 5 | 26.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22882872819900513 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 220 | SELL | STABILIZE | 54.0 | 6 | 132 | 5 | 24.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03140602260828018 | 0.0 | 0.0 | +— / -c65dacb1-5745-49d1-b7d4-e45d8e24aa84 |
| Jogador 7 | 5-3 | 222 | BUY | STABILIZE | 54.0 | 7 | 146 | 5 | 24.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0189636945724487 | 0.0 | 0.0 | +f84cc827-410f-47eb-bd95-bd650acfdd4b / -18d25cfb-d559-4efa-b708-c9987987590b,3b934078-806c-40f0-b102-e9131220f70e |
| Jogador 7 | 5-3 | 223 | BUY | STABILIZE | 54.0 | 7 | 144 | 5 | 24.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4040907919406891 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -— |
| Jogador 7 | 5-3 | 224 | MOVE_BENCH | STABILIZE | 54.0 | 7 | 141 | 5 | 24.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3383576273918152 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 225 | BUY | STABILIZE | 54.0 | 7 | 141 | 5 | 30.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1850781887769699 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -— |
| Jogador 7 | 5-3 | 226 | BUY | STABILIZE | 54.0 | 7 | 139 | 5 | 30.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2624472677707672 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 7 | 5-3 | 227 | MOVE_BENCH | STABILIZE | 54.0 | 7 | 135 | 5 | 30.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19862580299377441 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 229 | SELL | STABILIZE | 39.0 | 7 | 145 | 5 | 28.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -f84cc827-410f-47eb-bd95-bd650acfdd4b |
| Jogador 7 | 5-4 | 230 | BUY | STABILIZE | 39.0 | 7 | 150 | 5 | 28.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7670579552650452 | 0.0 | 0.0 | +57ba484a-6228-4263-8171-00a8a5893bea / -584991bb-37b3-4ac1-8e29-14e0d74c5e78,c7841e00-91da-410b-b00f-62f4bf32f666 |
| Jogador 7 | 5-5 | 232 | BUY | STABILIZE | 39.0 | 7 | 157 | 5 | 28.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10379761457443237 | 0.0 | 0.0 | +0b38218d-9c50-41ac-b761-115c054bf314 / -— |
| Jogador 7 | 5-5 | 233 | BUY | STABILIZE | 39.0 | 7 | 154 | 5 | 28.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04701686277985573 | 0.0 | 0.0 | +edd2748e-d629-4a8a-8174-4c1ef3f5f852 / -— |
| Jogador 7 | 5-5 | 234 | MOVE_BENCH | STABILIZE | 39.0 | 7 | 151 | 5 | 28.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7438231706619263 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 235 | MOVE_BOARD | STABILIZE | 39.0 | 7 | 151 | 5 | 34.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 236 | PASS | STABILIZE | 39.0 | 7 | 151 | 5 | 34.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1952412873506546 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 239 | SELL | ALL_IN | 22.0 | 7 | 162 | 5 | 34.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05158473923802376 | 0.0 | 0.0 | +— / -58cbdbde-2151-438c-8897-902bef9bcd92 |
| Jogador 7 | 5-6 | 240 | BUY | ALL_IN | 22.0 | 7 | 164 | 5 | 34.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9479324817657471 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 7 | 5-7 | 242 | SELL | ALL_IN | 7.0 | 7 | 172 | 5 | 34.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00426666671410203 | 0.0 | 0.0 | +— / -51a5a5d7-c5ea-43e2-a521-22fe0275c231 |
| Jogador 7 | 5-7 | 243 | BUY | ALL_IN | 7.0 | 7 | 175 | 5 | 34.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6297346949577332 | 0.0 | 0.0 | +a37d8478-8a98-4099-bb18-3602d68764f5 / -— |
| Jogador 7 | 5-7 | 244 | SELL | ALL_IN | 7.0 | 7 | 172 | 5 | 34.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034683942794799805 | 0.0 | 0.0 | +— / -0b38218d-9c50-41ac-b761-115c054bf314 |
| Jogador 7 | 5-7 | 245 | BUY | ALL_IN | 7.0 | 7 | 175 | 5 | 34.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4285392761230469 | 0.0 | 0.0 | +6eff87be-d18f-4f46-a9c6-9ae977c887e0 / -— |
| Jogador 7 | 5-7 | 246 | SELL | ALL_IN | 7.0 | 7 | 173 | 5 | 34.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -e1055913-2340-4af0-8527-e175c8bc1ccb |
| Jogador 7 | 5-7 | 247 | BUY | ALL_IN | 7.0 | 7 | 177 | 5 | 34.0 | Inferno/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05997924134135246 | 0.0 | 0.0 | +68a0405b-6231-471f-98a5-1661d32f4ac4 / -— |
| Jogador 7 | 6-1 | 249 | EQUIP_FROM_INVENTORY | ALL_IN | 7.0 | 7 | 186 | 5 | 34.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08790818601846695 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 250 | SELL | ALL_IN | 7.0 | 7 | 186 | 5 | 34.0 | Inferno/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01722005568444729 | 0.0 | 0.0 | +— / -68a0405b-6231-471f-98a5-1661d32f4ac4 |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031589943915605545 | 0.0 | 0.0 | +88a02960-5ebe-4b20-b667-1a8ce2728578 / -— |
| Jogador 8 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16182130575180054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3620654344558716 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012301865965127945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5023400187492371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0137680768966675 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36075541377067566 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28276047110557556 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9771534204483032 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 39 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17370682954788208 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 40 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2511828541755676 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 41 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11578001827001572 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 42 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.114152431488037 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -88a02960-5ebe-4b20-b667-1a8ce2728578,dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 2-1 | 49 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2012488692998886 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 50 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17955990135669708 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 51 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057697590440511703 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1035066843032837 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 53 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12439745664596558 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40793323516845703 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 56 | BUY | STABILIZE | 94.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25710561871528625 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 57 | BUY | STABILIZE | 94.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21259894967079163 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 58 | BUY | STABILIZE | 94.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2039390504360199 | 0.0 | 0.0 | +ebe77c97-f249-4265-ae03-bc8115a4795f / -— |
| Jogador 8 | 2-2 | 59 | SELL | STABILIZE | 94.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09966666996479034 | 0.0 | 0.0 | +— / -ebe77c97-f249-4265-ae03-bc8115a4795f |
| Jogador 8 | 2-2 | 60 | BUY | STABILIZE | 94.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08021492511034012 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 61 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1110355481505394 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 63 | BUY | STABILIZE | 89.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.981306254863739 | 0.0 | 0.0 | +01f4a73c-7202-4ee3-964e-d32370c3c547 / -— |
| Jogador 8 | 2-3 | 64 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0477073192596436 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -01f4a73c-7202-4ee3-964e-d32370c3c547,64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 2-3 | 65 | BUY | STABILIZE | 89.0 | 4 | 5 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3689638078212738 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 66 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 4 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39283114671707153 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 67 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 4 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5324448943138123 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 68 | BUY | STABILIZE | 89.0 | 4 | 4 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30042025446891785 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 69 | SELL | STABILIZE | 89.0 | 4 | 1 | 0 | 14.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-3 | 70 | BUY_XP | STABILIZE | 89.0 | 4 | 4 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 72 | BUY | STABILIZE | 83.0 | 5 | 6 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20223848521709442 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 73 | BUY | STABILIZE | 83.0 | 5 | 3 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12385638058185577 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 0 | 0 | 14.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7198014855384827 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 75 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 0 | 0 | 16.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5113011002540588 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 76 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 0 | 0 | 20.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04291514307260513 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 77 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 20.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-4 | 78 | BUY | STABILIZE | 83.0 | 5 | 1 | 0 | 20.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18219029903411865 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 8 | 2-4 | 79 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 20.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4129999876022339 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 8 | 2-4 | 80 | BUY | STABILIZE | 83.0 | 5 | 1 | 0 | 20.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13772208988666534 | 0.0 | 0.0 | +3644801e-2247-403d-8b81-d2d3f15c2f55 / -— |
| Jogador 8 | 2-5 | 82 | BUY | STABILIZE | 83.0 | 5 | 6 | 0 | 20.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8992016315460205 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 83 | BUY | STABILIZE | 83.0 | 5 | 5 | 0 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8514370322227478 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 84 | BUY | STABILIZE | 83.0 | 5 | 3 | 0 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1110091283917427 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 85 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 20.0 | Enfeitiçador/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019635463133454323 | 0.0 | 0.0 | +— / -3644801e-2247-403d-8b81-d2d3f15c2f55 |
| Jogador 8 | 2-5 | 86 | SELL | STABILIZE | 83.0 | 5 | 1 | 0 | 20.0 | Enfeitiçador/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043666668236255646 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 2-5 | 87 | SELL | STABILIZE | 83.0 | 5 | 4 | 0 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-5 | 88 | SELL | STABILIZE | 83.0 | 5 | 7 | 0 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010172376409173012 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 2-5 | 89 | SELL | STABILIZE | 83.0 | 5 | 10 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4182998538017273 | 0.0 | 0.0 | +— / -2e656a3d-eed0-40bb-a831-443d972d6588 |
| Jogador 8 | 2-5 | 90 | BUY | STABILIZE | 83.0 | 5 | 13 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0817614272236824 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-6 | 92 | BUY | STABILIZE | 78.0 | 5 | 18 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9778534770011902 | 0.0 | 0.0 | +c737e99a-613e-4f1a-a50e-7a865169f90c / -— |
| Jogador 8 | 2-6 | 93 | BUY | STABILIZE | 78.0 | 5 | 17 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23466092348098755 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 94 | BUY | STABILIZE | 78.0 | 5 | 14 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19823269546031952 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 95 | SELL | STABILIZE | 78.0 | 5 | 11 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05853207781910896 | 0.0 | 0.0 | +— / -c0d8da9e-5ede-4a26-8c5c-e2a908318bfd |
| Jogador 8 | 2-6 | 96 | BUY | STABILIZE | 78.0 | 5 | 13 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0586143396794796 | 0.0 | 0.0 | +b482ecdd-cc1a-40fa-8c21-cd1cac92b594 / -— |
| Jogador 8 | 2-6 | 97 | SELL | STABILIZE | 78.0 | 5 | 12 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38100001215934753 | 0.0 | 0.0 | +— / -b482ecdd-cc1a-40fa-8c21-cd1cac92b594 |
| Jogador 8 | 2-6 | 98 | SELL | STABILIZE | 78.0 | 5 | 13 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4265354573726654 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 2-6 | 99 | SELL | STABILIZE | 78.0 | 5 | 16 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13800513744354248 | 0.0 | 0.0 | +— / -87600495-fe90-4832-ab42-9a5cb0ebe3f4 |
| Jogador 8 | 2-6 | 100 | SELL | STABILIZE | 78.0 | 5 | 19 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9430000185966492 | 0.0 | 0.0 | +— / -b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 2-7 | 102 | BUY | STABILIZE | 70.0 | 5 | 29 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.269699364900589 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 103 | BUY | STABILIZE | 70.0 | 5 | 26 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15208740532398224 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 104 | BUY | STABILIZE | 70.0 | 5 | 23 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10318872332572937 | 0.0 | 0.0 | +d731d71e-fc91-41ae-ab3f-75966dd2c428 / -— |
| Jogador 8 | 2-7 | 105 | BUY | STABILIZE | 70.0 | 5 | 22 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07535423338413239 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 106 | SELL | STABILIZE | 70.0 | 5 | 21 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3863333463668823 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 2-7 | 107 | BUY_XP | STABILIZE | 70.0 | 5 | 22 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 108 | SELL | STABILIZE | 70.0 | 5 | 18 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3943333327770233 | 0.0 | 0.0 | +— / -d731d71e-fc91-41ae-ab3f-75966dd2c428 |
| Jogador 8 | 2-7 | 109 | BUY_XP | STABILIZE | 70.0 | 5 | 19 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 110 | BUY_XP | STABILIZE | 70.0 | 5 | 15 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 112 | BUY | STABILIZE | 70.0 | 6 | 19 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.08852820843458176 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 113 | CRAFT_AND_EQUIP | STABILIZE | 70.0 | 6 | 15 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21401236951351166 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 114 | BUY | STABILIZE | 70.0 | 6 | 15 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09894019365310669 | 0.0 | 0.0 | +a5c0595b-85f9-4c71-a156-675d22a7b3c2 / -— |
| Jogador 8 | 3-1 | 115 | MOVE_BENCH | STABILIZE | 70.0 | 6 | 13 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38958653807640076 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 116 | BUY | STABILIZE | 70.0 | 6 | 13 | 1 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21691374480724335 | 0.0 | 0.0 | +5cf46feb-77cd-4cb8-9211-ffb08d88391a / -— |
| Jogador 8 | 3-1 | 117 | BUY | STABILIZE | 70.0 | 6 | 11 | 1 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01565653644502163 | 0.0 | 0.0 | +88420167-3841-43dd-b1d0-3e5ab2294c78 / -— |
| Jogador 8 | 3-1 | 118 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 9 | 0 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0076460810378193855 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 119 | BUY_XP | STABILIZE | 70.0 | 6 | 9 | 0 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 121 | SELL | STABILIZE | 70.0 | 6 | 11 | 1 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -88420167-3841-43dd-b1d0-3e5ab2294c78 |
| Jogador 8 | 3-2 | 122 | BUY | STABILIZE | 70.0 | 6 | 13 | 1 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15629152953624725 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 123 | SELL | STABILIZE | 70.0 | 6 | 9 | 0 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06970791518688202 | 0.0 | 0.0 | +— / -a5c0595b-85f9-4c71-a156-675d22a7b3c2 |
| Jogador 8 | 3-2 | 124 | BUY | STABILIZE | 70.0 | 6 | 11 | 1 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08802248537540436 | 0.0 | 0.0 | +5326031a-1b7e-4dbd-b58b-1e81029d42a1 / -— |
| Jogador 8 | 3-2 | 125 | SELL | STABILIZE | 70.0 | 6 | 9 | 0 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05654929205775261 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 3-2 | 126 | BUY | STABILIZE | 70.0 | 6 | 12 | 1 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21192969381809235 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 127 | SELL | STABILIZE | 70.0 | 6 | 11 | 1 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0018333332845941186 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-2 | 128 | BUY | STABILIZE | 70.0 | 6 | 12 | 1 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08928677439689636 | 0.0 | 0.0 | +655deca9-2d3f-4e88-827a-5f49da8f3451 / -— |
| Jogador 8 | 3-3 | 130 | SELL | STABILIZE | 60.0 | 6 | 16 | 1 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -655deca9-2d3f-4e88-827a-5f49da8f3451 |
| Jogador 8 | 3-4 | 132 | BUY | STABILIZE | 50.0 | 6 | 25 | 2 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8169966340065002 | 0.0 | 0.0 | +eb7e36f0-cef9-4a2e-979a-f8a357da73e8 / -— |
| Jogador 8 | 3-4 | 133 | SELL | STABILIZE | 50.0 | 6 | 24 | 2 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019435050198808312 | 0.0 | 0.0 | +— / -4ac49c80-f0c3-47ae-a031-96928d244e13 |
| Jogador 8 | 3-4 | 134 | BUY | STABILIZE | 50.0 | 6 | 28 | 2 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7707200050354004 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 135 | SELL | STABILIZE | 50.0 | 6 | 26 | 2 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4073333442211151 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 3-4 | 136 | BUY | STABILIZE | 50.0 | 6 | 28 | 2 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012929638847708702 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 137 | SELL | STABILIZE | 50.0 | 6 | 25 | 2 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -35e1a0f6-207d-4df2-b096-fc07962d094a |
| Jogador 8 | 3-4 | 138 | BUY | STABILIZE | 50.0 | 6 | 27 | 2 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003669943893328309 | 0.0 | 0.0 | +e8355df5-8ee7-44a3-ab88-3708c14fd5dc / -— |
| Jogador 8 | 3-4 | 139 | MOVE_BOARD | STABILIZE | 50.0 | 6 | 26 | 2 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 140 | MOVE_BOARD | STABILIZE | 50.0 | 6 | 26 | 2 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023117270320653915 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 142 | SELL | STABILIZE | 50.0 | 6 | 34 | 3 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008441878482699394 | 0.0 | 0.0 | +— / -e8355df5-8ee7-44a3-ab88-3708c14fd5dc |
| Jogador 8 | 3-5 | 143 | BUY | STABILIZE | 50.0 | 6 | 35 | 3 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7674959301948547 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 144 | SELL | STABILIZE | 50.0 | 6 | 33 | 3 | 26.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8075722455978394 | 0.0 | 0.0 | +— / -eb7e36f0-cef9-4a2e-979a-f8a357da73e8 |
| Jogador 8 | 3-5 | 145 | BUY | STABILIZE | 50.0 | 6 | 34 | 3 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8523051142692566 | 0.0 | 0.0 | +fa5dc86b-f736-4083-b9df-5cc174b726f2 / -5326031a-1b7e-4dbd-b58b-1e81029d42a1,d5848998-33f3-4632-94c0-60388a7cc6b8 |
| Jogador 8 | 3-5 | 146 | BUY | STABILIZE | 50.0 | 6 | 32 | 3 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36127325892448425 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 8 | 3-5 | 147 | MOVE_BENCH | STABILIZE | 50.0 | 6 | 29 | 2 | 26.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06867358833551407 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 148 | SELL | STABILIZE | 50.0 | 6 | 29 | 2 | 24.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.543467104434967 | 0.0 | 0.0 | +— / -fa5dc86b-f736-4083-b9df-5cc174b726f2 |
| Jogador 8 | 3-5 | 149 | BUY | STABILIZE | 50.0 | 6 | 34 | 3 | 24.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02907889150083065 | 0.0 | 0.0 | +6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 / -— |
| Jogador 8 | 3-5 | 150 | SELL | STABILIZE | 50.0 | 6 | 32 | 3 | 24.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03756776079535484 | 0.0 | 0.0 | +— / -a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 8 | 3-6 | 152 | BUY | STABILIZE | 41.0 | 6 | 43 | 4 | 24.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5202206969261169 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -— |
| Jogador 8 | 3-6 | 153 | BUY | STABILIZE | 41.0 | 6 | 41 | 4 | 24.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2258543223142624 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 154 | SELL | STABILIZE | 41.0 | 6 | 38 | 3 | 24.0 | Feérico/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38859042525291443 | 0.0 | 0.0 | +— / -6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 |
| Jogador 8 | 3-6 | 155 | BUY | STABILIZE | 41.0 | 6 | 40 | 4 | 24.0 | Feérico/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6504169702529907 | 0.0 | 0.0 | +b55260cd-3c6a-4cb8-99d0-b7c6471103ad / -9af097e2-729d-474a-9a7e-b266c665c606,b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 3-6 | 156 | MOVE_BENCH | STABILIZE | 41.0 | 6 | 37 | 3 | 18.0 | Feérico/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27777913212776184 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 157 | BUY | STABILIZE | 41.0 | 6 | 37 | 3 | 22.0 | Feérico/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0505649596452713 | 0.0 | 0.0 | +5f79a010-9e28-4a94-be40-973a17313186 / -— |
| Jogador 8 | 3-6 | 158 | BUY | STABILIZE | 41.0 | 6 | 34 | 3 | 22.0 | Feérico/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21046045422554016 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 159 | MOVE_BOARD | STABILIZE | 41.0 | 6 | 30 | 3 | 22.0 | Feérico/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 161 | SELL | STABILIZE | 41.0 | 6 | 39 | 3 | 22.0 | Feérico/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021244309842586517 | 0.0 | 0.0 | +— / -b55260cd-3c6a-4cb8-99d0-b7c6471103ad |
| Jogador 8 | 3-7 | 162 | BUY | STABILIZE | 41.0 | 6 | 47 | 4 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33381643891334534 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 8 | 3-7 | 163 | SELL | STABILIZE | 41.0 | 6 | 46 | 4 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030377022922039032 | 0.0 | 0.0 | +— / -5f79a010-9e28-4a94-be40-973a17313186 |
| Jogador 8 | 3-7 | 164 | BUY | STABILIZE | 41.0 | 6 | 49 | 4 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23625539243221283 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 165 | SELL | STABILIZE | 41.0 | 6 | 46 | 4 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002166666556149721 | 0.0 | 0.0 | +— / -849ea0fc-7f61-4907-8abb-b25c8cc82efc |
| Jogador 8 | 3-7 | 166 | BUY | STABILIZE | 41.0 | 6 | 49 | 4 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.267829954624176 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 8 | 3-7 | 167 | MOVE_BOARD | STABILIZE | 41.0 | 6 | 46 | 4 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 168 | MOVE_BOARD | STABILIZE | 41.0 | 6 | 46 | 4 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02632727473974228 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 169 | PASS | STABILIZE | 41.0 | 6 | 46 | 4 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03797777742147446 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 171 | CRAFT_AND_EQUIP | STABILIZE | 41.0 | 6 | 55 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2543240189552307 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 172 | CRAFT_AND_EQUIP | STABILIZE | 41.0 | 6 | 55 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24980567395687103 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 173 | SELL | STABILIZE | 41.0 | 6 | 55 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -112206a4-c285-4f76-878a-056248cba468 |
| Jogador 8 | 4-1 | 174 | BUY | STABILIZE | 41.0 | 6 | 58 | 5 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8399592638015747 | 0.0 | 0.0 | +88035b70-61e0-4279-9d55-e451f412f0d3 / -— |
| Jogador 8 | 4-1 | 175 | SELL | STABILIZE | 41.0 | 6 | 55 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -a23ee552-279e-4c6c-aa05-6197043e8f1d |
| Jogador 8 | 4-1 | 176 | BUY | STABILIZE | 41.0 | 6 | 59 | 5 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10145806521177292 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -— |
| Jogador 8 | 4-1 | 177 | SELL | STABILIZE | 41.0 | 6 | 58 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04672456905245781 | 0.0 | 0.0 | +— / -2faa526c-d29e-47a9-9eb3-5030750cb483 |
| Jogador 8 | 4-1 | 178 | BUY | STABILIZE | 41.0 | 6 | 59 | 5 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08552185446023941 | 0.0 | 0.0 | +2c153083-6c43-425e-90d5-23f7f2058592 / -— |
| Jogador 8 | 4-2 | 180 | SELL | STABILIZE | 41.0 | 6 | 69 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -2c153083-6c43-425e-90d5-23f7f2058592 |
| Jogador 8 | 4-3 | 182 | BUY | STABILIZE | 41.0 | 6 | 83 | 5 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9049563407897949 | 0.0 | 0.0 | +8455b875-27e0-4172-9311-5cbb3e2242b9 / -— |
| Jogador 8 | 4-3 | 183 | SELL | STABILIZE | 41.0 | 6 | 80 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -a14e4b8f-77c5-4909-a9ee-0044b836a877 |
| Jogador 8 | 4-3 | 184 | BUY | STABILIZE | 41.0 | 6 | 81 | 5 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6453437209129333 | 0.0 | 0.0 | +579b987a-fedf-45d8-92fc-634a041d3d4f / -— |
| Jogador 8 | 4-3 | 185 | SELL | STABILIZE | 41.0 | 6 | 79 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5127865076065063 | 0.0 | 0.0 | +— / -579b987a-fedf-45d8-92fc-634a041d3d4f |
| Jogador 8 | 4-3 | 186 | BUY | STABILIZE | 41.0 | 6 | 81 | 5 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032367557287216187 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 8 | 4-3 | 187 | SELL | STABILIZE | 41.0 | 6 | 78 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -1fa69553-5270-4459-986b-600f748711b7 |
| Jogador 8 | 4-3 | 188 | BUY | STABILIZE | 41.0 | 6 | 81 | 5 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27515730261802673 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 8 | 4-3 | 189 | SELL | STABILIZE | 41.0 | 6 | 79 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -e85c6ab6-f36c-40b4-88e2-b7380b4c9652 |
| Jogador 8 | 4-4 | 191 | BUY | STABILIZE | 30.0 | 6 | 91 | 5 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.875454843044281 | 0.0 | 0.0 | +167110eb-b0d0-4873-9ffe-38286dcc5ca2 / -— |
| Jogador 8 | 4-4 | 192 | SELL | STABILIZE | 30.0 | 6 | 88 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5952000021934509 | 0.0 | 0.0 | +— / -4d995451-2e5c-43c2-93f0-22e074e35ab2 |
| Jogador 8 | 4-4 | 193 | BUY | STABILIZE | 30.0 | 6 | 92 | 5 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4112982451915741 | 0.0 | 0.0 | +cc9b5fff-2223-4721-a8b2-4f70e196b851 / -— |
| Jogador 8 | 4-4 | 194 | SELL | STABILIZE | 30.0 | 6 | 91 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -cc9b5fff-2223-4721-a8b2-4f70e196b851 |
| Jogador 8 | 4-4 | 195 | BUY | STABILIZE | 30.0 | 6 | 92 | 5 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6497238874435425 | 0.0 | 0.0 | +7b49fb38-6e0e-4a72-a2ce-0527827d36a6 / -— |
| Jogador 8 | 4-4 | 196 | SELL | STABILIZE | 30.0 | 6 | 90 | 5 | 22.0 | Feérico/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5135973691940308 | 0.0 | 0.0 | +— / -7b49fb38-6e0e-4a72-a2ce-0527827d36a6 |
| Jogador 8 | 4-5 | 198 | BUY | STABILIZE | 30.0 | 6 | 102 | 5 | 22.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9637548923492432 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -8455b875-27e0-4172-9311-5cbb3e2242b9,d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 4-5 | 199 | BUY | STABILIZE | 30.0 | 6 | 99 | 5 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9612790942192078 | 0.0 | 0.0 | +31ea6d79-501d-4f2a-821d-7058334be82f / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,c737e99a-613e-4f1a-a50e-7a865169f90c |
| Jogador 8 | 4-5 | 200 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 98 | 5 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15452727675437927 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 202 | BUY | STABILIZE | 30.0 | 6 | 108 | 5 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021449554711580276 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -— |
| Jogador 8 | 4-6 | 203 | BUY | STABILIZE | 30.0 | 6 | 105 | 5 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036228571087121964 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 8 | 4-6 | 204 | BUY | STABILIZE | 30.0 | 6 | 104 | 5 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.046822093427181244 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 8 | 4-6 | 205 | SELL | STABILIZE | 30.0 | 6 | 103 | 5 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -31ea6d79-501d-4f2a-821d-7058334be82f |
| Jogador 8 | 4-6 | 206 | EQUIP_FROM_INVENTORY | STABILIZE | 30.0 | 6 | 106 | 5 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1299111694097519 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 207 | EQUIP_FROM_INVENTORY | STABILIZE | 30.0 | 6 | 106 | 5 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.16389189660549164 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 209 | BUY | ALL_IN | 17.0 | 6 | 117 | 5 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.00043510316754691303 | 0.0 | 0.0 | +d80c845d-24bc-4053-a60d-5d0122839b0c / -— |
| Jogador 8 | 4-7 | 210 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 6 | 114 | 5 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1155967265367508 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 212 | CRAFT_AND_EQUIP | ALL_IN | 17.0 | 6 | 125 | 5 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16341306269168854 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 213 | CRAFT_AND_EQUIP | ALL_IN | 17.0 | 6 | 125 | 5 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08790341764688492 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 214 | SELL | ALL_IN | 17.0 | 6 | 125 | 5 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7027999758720398 | 0.0 | 0.0 | +— / -bc0aa086-b5e5-4809-833f-193c5c0da181 |
| Jogador 8 | 5-1 | 215 | BUY | ALL_IN | 17.0 | 6 | 133 | 5 | 26.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0513256788253784 | 0.0 | 0.0 | +98b600a1-736b-437d-a69e-8a7f7235d9c3 / -82e109f9-54c8-492d-93e5-7e0dd0034b15,88035b70-61e0-4279-9d55-e451f412f0d3 |
| Jogador 8 | 5-1 | 216 | MOVE_BENCH | ALL_IN | 17.0 | 6 | 130 | 5 | 14.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14916905760765076 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 217 | BUY | ALL_IN | 17.0 | 6 | 130 | 5 | 16.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04452277347445488 | 0.0 | 0.0 | +55cd39c0-65d5-410e-917e-501f584115fa / -— |
| Jogador 8 | 5-1 | 218 | MOVE_BENCH | ALL_IN | 17.0 | 6 | 126 | 5 | 16.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09983646869659424 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 220 | BUY | ALL_IN | 1.0 | 6 | 137 | 5 | 22.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.918185293674469 | 0.0 | 0.0 | +99857cfa-b422-4167-bb01-d9fd94a55d88 / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 196 | 180 | 93 | 2 | 6 | 0 | 0 | 0 | 218 | 52.0 |
- Jogador 1 — gasto por ação: BUY: 152g, BUY_XP: 28g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 49g, stage 3: 37g, stage 4: 28g, stage 5: 29g, stage 6: 31g
| Jogador 2 | 189 | 186 | 127 | 5 | 4 | 1 | 0 | 0 | 215 | 26.0 |
- Jogador 2 — gasto por ação: BUY: 162g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 55g, stage 3: 44g, stage 4: 32g, stage 5: 43g, stage 6: 5g
| Jogador 3 | 175 | 240 | 34 | 16 | 32 | 0 | 0 | 0 | 79 | 58.0 |
- Jogador 3 — gasto por ação: BUY: 96g, BUY_XP: 144g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 46g, stage 3: 44g, stage 4: 71g, stage 5: 65g, stage 6: 7g
| Jogador 4 | 127 | 102 | 32 | 3 | 6 | 1 | 0 | 0 | 59 | 24.0 |
- Jogador 4 — gasto por ação: BUY: 70g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 58g, stage 3: 36g, stage 4: 2g
| Jogador 5 | 161 | 155 | 104 | 3 | 4 | 0 | 0 | 0 | 136 | 22.0 |
- Jogador 5 — gasto por ação: BUY: 131g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 59g, stage 3: 48g, stage 4: 34g, stage 5: 7g
| Jogador 6 | 179 | 173 | 88 | 6 | 8 | 0 | 0 | 0 | 158 | 40.0 |
- Jogador 6 — gasto por ação: BUY: 137g, BUY_XP: 36g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 65g, stage 3: 49g, stage 4: 24g, stage 5: 24g, stage 6: 6g
| Jogador 7 | 174 | 164 | 90 | 5 | 5 | 0 | 1 | 0 | 188 | 34.0 |
- Jogador 7 — gasto por ação: BUY: 142g, BUY_XP: 20g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 47g, stage 3: 39g, stage 4: 38g, stage 5: 34g, stage 6: 0g
| Jogador 8 | 170 | 175 | 112 | 7 | 5 | 0 | 0 | 0 | 136 | 22.0 |
- Jogador 8 — gasto por ação: BUY: 155g, BUY_XP: 20g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 65g, stage 3: 61g, stage 4: 34g, stage 5: 8g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 7 | 4 |
- Jogador 1 · 3-5 · step 149: PASS com 19g, HP 63, nível 6/8 (STABILIZE).
- Jogador 1 · 3-7 · step 165: PASS com 25g, HP 53, nível 6/8 (STABILIZE).
- Jogador 1 · 4-1 · step 175: PASS com 32g, HP 53, nível 6/8 (STABILIZE).
- Jogador 1 · 5-5 · step 236: PASS com 140g, HP 19, nível 7/8 (ALL_IN).
| Jogador 2 | 6 | 1 |
- Jogador 2 · 3-5 · step 150: PASS com 21g, HP 80, nível 6/8 (STABILIZE).
| Jogador 3 | 36 | 4 |
- Jogador 3 · 3-5 · step 145: PASS com 8g, HP 100, nível 7/8 (FAST8).
- Jogador 3 · 3-6 · step 154: PASS com 17g, HP 100, nível 7/8 (FAST8).
- Jogador 3 · 3-7 · step 163: PASS com 27g, HP 100, nível 7/8 (FAST8).
- Jogador 3 · 4-1 · step 175: PASS com 37g, HP 100, nível 7/8 (FAST8).
| Jogador 4 | 8 | 5 |
- Jogador 4 · 3-4 · step 138: PASS com 7g, HP 52, nível 6/8 (STABILIZE).
- Jogador 4 · 3-5 · step 147: PASS com 10g, HP 52, nível 6/8 (STABILIZE).
- Jogador 4 · 3-6 · step 159: PASS com 19g, HP 43, nível 6/8 (STABILIZE).
- Jogador 4 · 3-7 · step 165: PASS com 25g, HP 33, nível 6/8 (STABILIZE).
- Jogador 4 · 4-1 · step 176: PASS com 35g, HP 33, nível 6/8 (STABILIZE).
| Jogador 5 | 6 | 0 |
| Jogador 6 | 9 | 4 |
- Jogador 6 · 4-3 · step 186: PASS com 31g, HP 51, nível 7/8 (STABILIZE).
- Jogador 6 · 4-4 · step 196: PASS com 42g, HP 51, nível 7/8 (STABILIZE).
- Jogador 6 · 4-6 · step 207: PASS com 61g, HP 40, nível 7/8 (STABILIZE).
- Jogador 6 · 5-5 · step 235: PASS com 116g, HP 25, nível 7/8 (ALL_IN).
| Jogador 7 | 5 | 11 |
- Jogador 7 · 2-6 · step 96: PASS com 4g, HP 96, nível 6/8 (STABILIZE).
- Jogador 7 · 2-7 · step 107: PASS com 6g, HP 96, nível 6/8 (STABILIZE).
- Jogador 7 · 3-1 · step 119: PASS com 7g, HP 96, nível 6/8 (STABILIZE).
- Jogador 7 · 3-2 · step 126: PASS com 7g, HP 96, nível 6/8 (STABILIZE).
- Jogador 7 · 3-4 · step 137: PASS com 17g, HP 96, nível 6/8 (STABILIZE).
- Jogador 7 · 3-5 · step 147: PASS com 26g, HP 96, nível 6/8 (STABILIZE).
- Jogador 7 · 3-6 · step 159: PASS com 32g, HP 86, nível 6/8 (STABILIZE).
- Jogador 7 · 3-7 · step 168: PASS com 36g, HP 76, nível 6/8 (STABILIZE).
- Jogador 7 · 4-3 · step 189: REROLL com 74g, HP 65, nível 6/8 (STABILIZE).
- Jogador 7 · 4-6 · step 207: PASS com 95g, HP 65, nível 6/8 (STABILIZE).
- Jogador 7 · 5-5 · step 236: PASS com 151g, HP 39, nível 7/8 (STABILIZE).
| Jogador 8 | 5 | 1 |
- Jogador 8 · 3-7 · step 169: PASS com 46g, HP 41, nível 6/8 (STABILIZE).

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
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 2 | 2 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 196 | 52 | 45 | 99 | 0.0040 | 0.0155 | 0.0022 | 0.3434 | 0.0018 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0227 (69 ações), BUY_XP: Δ 0.0070 (7 ações), CRAFT_AND_EQUIP: Δ 0.0040 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (6 ações), MOVE_BENCH: Δ 0.0139 (38 ações), MOVE_BOARD: Δ 0.0348 (29 ações), PASS: Δ 0.0000 (11 ações), SELL: Δ 0.0253 (29 ações)
| Jogador 2 | 189 | 32 | 28 | 129 | -0.0009 | 0.0292 | -0.0015 | 0.2877 | 0.0006 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ 0.0004 (75 ações), BUY_XP: Δ 0.0162 (6 ações), CRAFT_AND_EQUIP: Δ 0.0007 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0086 (3 ações), MOVE_BENCH: Δ 0.0531 (13 ações), MOVE_BOARD: Δ -0.0453 (28 ações), PASS: Δ 0.0000 (8 ações), SELL: Δ 0.0052 (49 ações)
| Jogador 3 | 175 | 39 | 37 | 99 | -0.0013 | 0.3317 | -0.0029 | 0.2635 | 0.0016 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0357 (43 ações), BUY_XP: Δ 0.0041 (36 ações), CRAFT_AND_EQUIP: Δ 0.0106 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0186 (22 ações), MOVE_BOARD: Δ 0.0132 (41 ações), PASS: Δ 0.0000 (15 ações), SELL: Δ 0.0137 (10 ações)
| Jogador 4 | 127 | 34 | 28 | 65 | 0.0019 | -0.0180 | -0.0016 | 0.3749 | 0.0034 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0179 (39 ações), BUY_XP: Δ 0.0135 (8 ações), CRAFT_AND_EQUIP: Δ 0.0028 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0226 (32 ações), MOVE_BOARD: Δ -0.0122 (13 ações), PASS: Δ 0.0000 (12 ações), SELL: Δ 0.0167 (15 ações)
| Jogador 5 | 161 | 22 | 19 | 120 | 0.0037 | 0.1074 | 0.0017 | 0.3215 | 0.0020 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0101 (71 ações), BUY_XP: Δ 0.0162 (6 ações), CRAFT_AND_EQUIP: Δ 0.0060 (7 ações), EQUIP_FROM_INVENTORY: Δ -0.0162 (2 ações), MOVE_BENCH: Δ 0.0139 (13 ações), MOVE_BOARD: Δ 0.1224 (5 ações), PASS: Δ 0.0000 (6 ações), SELL: Δ 0.0082 (51 ações)
| Jogador 6 | 179 | 32 | 30 | 117 | 0.0036 | -0.2625 | 0.0010 | 0.4309 | 0.0026 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0055 (61 ações), BUY_XP: Δ 0.0029 (9 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0003 (9 ações), MOVE_BENCH: Δ 0.1003 (11 ações), MOVE_BOARD: Δ -0.0182 (31 ações), PASS: Δ 0.0000 (13 ações), SELL: Δ 0.0111 (38 ações)
| Jogador 7 | 174 | 29 | 37 | 108 | -0.0010 | 0.0984 | -0.0014 | 0.2915 | 0.0004 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0099 (65 ações), BUY_XP: Δ 0.0000 (5 ações), CRAFT_AND_EQUIP: Δ -0.0205 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ -0.0170 (15 ações), MOVE_BOARD: Δ 0.0155 (33 ações), PASS: Δ 0.0000 (16 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0115 (31 ações)
| Jogador 8 | 170 | 28 | 27 | 115 | -0.0059 | -0.7104 | -0.0088 | 0.4179 | 0.0030 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0004 (77 ações), BUY_XP: Δ 0.0000 (5 ações), CRAFT_AND_EQUIP: Δ 0.0030 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ -0.0856 (15 ações), MOVE_BOARD: Δ -0.0003 (11 ações), PASS: Δ 0.0000 (5 ações), SELL: Δ 0.0064 (47 ações)
- Jogador 1 — rounds avaliados: 36; correlação estrutural/combate: 0.575; posicional/combate: 0.047.
- Jogador 1 — combate positive: score estrutural prévio 0.345
  score posicional prévio 0.355
- Jogador 1 — combate negative: score estrutural prévio -0.336
  score posicional prévio 0.348
- Jogador 2 — rounds avaliados: 34; correlação estrutural/combate: 0.176; posicional/combate: -0.008.
- Jogador 2 — combate positive: score estrutural prévio 0.089
  score posicional prévio 0.250
- Jogador 2 — combate negative: score estrutural prévio -0.057
  score posicional prévio 0.254
- Jogador 3 — rounds avaliados: 36; correlação estrutural/combate: 0.373; posicional/combate: 0.204.
- Jogador 3 — combate positive: score estrutural prévio 0.371
  score posicional prévio 0.280
- Jogador 3 — combate negative: score estrutural prévio -0.106
  score posicional prévio 0.252
- Jogador 4 — rounds avaliados: 21; correlação estrutural/combate: 0.565; posicional/combate: -0.368.
- Jogador 4 — combate positive: score estrutural prévio 0.113
  score posicional prévio 0.350
- Jogador 4 — combate negative: score estrutural prévio -0.120
  score posicional prévio 0.413
- Jogador 5 — rounds avaliados: 26; correlação estrutural/combate: -0.323; posicional/combate: -0.184.
- Jogador 5 — combate positive: score estrutural prévio -0.022
  score posicional prévio 0.316
- Jogador 5 — combate negative: score estrutural prévio 0.148
  score posicional prévio 0.333
- Jogador 6 — rounds avaliados: 34; correlação estrutural/combate: 0.173; posicional/combate: -0.399.
- Jogador 6 — combate positive: score estrutural prévio 0.063
  score posicional prévio 0.332
- Jogador 6 — combate negative: score estrutural prévio -0.300
  score posicional prévio 0.465
- Jogador 7 — rounds avaliados: 33; correlação estrutural/combate: -0.066; posicional/combate: 0.088.
- Jogador 7 — combate positive: score estrutural prévio 0.120
  score posicional prévio 0.282
- Jogador 7 — combate negative: score estrutural prévio 0.153
  score posicional prévio 0.257
- Jogador 8 — rounds avaliados: 27; correlação estrutural/combate: 0.235; posicional/combate: -0.143.
- Jogador 8 — combate positive: score estrutural prévio -0.725
  score posicional prévio 0.444
- Jogador 8 — combate negative: score estrutural prévio -0.880
  score posicional prévio 0.447

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 232 | OK (232) | 8 | 0 | 0 | 0 | 8 | 3 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Bloodthirster, TFT_Item_Crownguard, TFT_Item_JeweledGauntlet, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon, TFT_Item_SteraksGage, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 222 | OK (222) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_Crownguard, TFT_Item_GargoyleStoneplate, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_RunaansHurricane; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 211 | OK (211) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_GuinsoosRageblade, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_RedBuff, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 147 | OK (147) | 5 | 0 | 0 | 1 | 5 | 3 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 186 | OK (186) | 7 | 0 | 0 | 0 | 7 | 2 |
- Jogador 5 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_IonicSpark, TFT_Item_Leviathan, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_PowerGauntlet; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 212 | OK (212) | 7 | 1 | 0 | 0 | 8 | 3 |
- Jogador 6 — IDs equipados observados: DA_18_EmblemSpellweaver, TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_HextechGunblade, TFT_Item_JeweledGauntlet, TFT_Item_RedBuff, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 206 | OK (206) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 7 — IDs equipados observados: TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 196 | OK (196) | 4 | 3 | 0 | 0 | 7 | 3 |
- Jogador 8 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_DragonsClaw, TFT_Item_HextechGunblade, TFT_Item_JeweledGauntlet, TFT_Item_LastWhisper, TFT_Item_Morellonomicon, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.110 | 0.000 |
| Jogador 1 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.001 | 0.000 |
| Jogador 1 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 1 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.012 | 0.000 |
| Jogador 1 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 6 | 5 | 4 → 4 | -0.012 | 0.366 |
| Jogador 1 | 2-2 | 7 | 2.000 | 2.000 | 0 → 0 | 3 → 3 | 14% → 18% | 6 → 7 | 7 | 4 → 5 | -0.039 | 0.359 |
| Jogador 1 | 2-3 | 9 | 0.000 | -6.000 | 0 → 0 | 3 → 3 | 18% → 18% | 7 → 7 | 11 | 5 → 5 | 0.000 | -0.264 |
| Jogador 1 | 2-4 | 10 | 4.000 | 6.000 | 0 → 0 | 3 → 2 | 18% → 18% | 7 → 6 | 6 | 5 → 5 | 0.059 | 0.000 |
| Jogador 1 | 2-5 | 8 | 0.000 | 4.000 | 0 → 0 | 2 → 2 | 18% → 18% | 6 → 7 | 8 | 5 → 6 | 0.022 | 0.327 |
| Jogador 1 | 2-6 | 9 | 10.000 | 2.000 | 0 → 1 | 2 → 1 | 18% → 21% | 7 → 7 | 7 | 6 → 6 | -0.016 | 0.293 |
| Jogador 1 | 2-7 | 10 | 4.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 7 → 11 | 5 | 6 → 6 | -0.111 | 0.000 |
| Jogador 1 | 3-1 | 9 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 21% → 21% | 11 → 8 | 9 | 6 → 6 | 0.027 | -0.304 |
| Jogador 1 | 3-2 | 9 | 2.000 | 0.000 | 1 → 2 | 2 → 1 | 21% → 21% | 8 → 7 | 7 | 6 → 6 | -0.030 | -0.308 |
| Jogador 1 | 3-3 | 2 | 2.000 | -2.000 | 2 → 2 | 1 → 1 | 21% → 21% | 7 → 13 | 0 | 6 → 6 | 0.009 | -1.413 |
| Jogador 1 | 3-4 | 10 | -4.000 | 0.000 | 2 → 1 | 1 → 1 | 21% → 21% | 13 → 23 | 5 | 6 → 6 | 0.077 | 0.000 |
| Jogador 1 | 3-5 | 9 | 0.000 | 8.000 | 1 → 1 | 1 → 3 | 21% → 21% | 23 → 27 | 4 | 6 → 6 | -0.002 | 0.307 |
| Jogador 1 | 3-6 | 9 | 0.000 | 6.000 | 1 → 1 | 3 → 2 | 21% → 21% | 27 → 29 | 8 | 6 → 6 | -0.007 | -0.298 |
| Jogador 1 | 3-7 | 6 | 0.000 | 8.000 | 1 → 1 | 2 → 3 | 21% → 21% | 29 → 32 | 4 | 6 → 6 | 0.004 | 0.000 |
| Jogador 1 | 4-1 | 6 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 21% → 21% | 32 → 41 | 0 | 6 → 6 | -0.065 | -0.446 |
| Jogador 1 | 4-2 | 2 | 0.000 | -8.000 | 1 → 1 | 3 → 3 | 21% → 21% | 41 → 56 | 0 | 6 → 6 | 0.030 | -1.432 |
| Jogador 1 | 4-3 | 9 | -2.000 | -8.000 | 1 → 1 | 3 → 3 | 21% → 21% | 56 → 72 | 3 | 6 → 6 | 0.003 | 0.307 |
| Jogador 1 | 4-4 | 7 | 2.000 | -2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 72 → 82 | 4 | 6 → 6 | 0.060 | 0.000 |
| Jogador 1 | 4-5 | 4 | 0.000 | 20.000 | 1 → 1 | 3 → 3 | 21% → 21% | 82 → 82 | 10 | 6 → 7 | 0.009 | -0.681 |
| Jogador 1 | 4-6 | 7 | 8.000 | -2.000 | 1 → 1 | 3 → 2 | 21% → 25% | 82 → 88 | 5 | 7 → 7 | 0.026 | 0.414 |
| Jogador 1 | 4-7 | 3 | 0.000 | 12.000 | 1 → 1 | 2 → 4 | 25% → 25% | 88 → 92 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-1 | 8 | 0.000 | -14.000 | 1 → 1 | 4 → 3 | 25% → 25% | 92 → 111 | 6 | 7 → 7 | 0.089 | 0.367 |
| Jogador 1 | 5-2 | 2 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 25% → 25% | 111 → 120 | 3 | 7 → 7 | 0.000 | 1.528 |
| Jogador 1 | 5-3 | 7 | 0.000 | -4.000 | 1 → 1 | 4 → 3 | 25% → 25% | 120 → 132 | 3 | 7 → 7 | -0.009 | 0.429 |
| Jogador 1 | 5-4 | 3 | 0.000 | 6.000 | 1 → 1 | 3 → 5 | 25% → 25% | 132 → 140 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-5 | 6 | 0.000 | 2.000 | 1 → 1 | 5 → 5 | 25% → 25% | 140 → 153 | 5 | 7 → 7 | -0.067 | 0.506 |
| Jogador 1 | 5-6 | 3 | 4.000 | -14.000 | 1 → 1 | 5 → 4 | 25% → 25% | 153 → 171 | 1 | 7 → 7 | -0.080 | 1.002 |
| Jogador 1 | 5-7 | 7 | 6.000 | 4.000 | 1 → 2 | 4 → 3 | 25% → 25% | 171 → 176 | 8 | 7 → 7 | 0.032 | 0.000 |
| Jogador 1 | 6-1 | 3 | 0.000 | 6.000 | 2 → 2 | 3 → 4 | 25% → 25% | 176 → 187 | 3 | 7 → 7 | 0.000 | 0.991 |
| Jogador 1 | 6-2 | 5 | 0.000 | -6.000 | 2 → 2 | 4 → 4 | 25% → 25% | 187 → 202 | 4 | 7 → 7 | -0.039 | 0.594 |
| Jogador 1 | 6-3 | 5 | 0.000 | 12.000 | 2 → 2 | 4 → 4 | 25% → 25% | 202 → 202 | 10 | 7 → 7 | -0.012 | -0.570 |
| Jogador 1 | 6-4 | 7 | 6.000 | -20.000 | 2 → 3 | 4 → 3 | 25% → 25% | 202 → 221 | 10 | 7 → 7 | 0.038 | 0.000 |
| Jogador 1 | 6-5 | 2 | 0.000 | 6.000 | 3 → 3 | 3 → 3 | 25% → 25% | 221 → 218 | 4 | 7 → 7 | 0.000 | 0.000 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 14, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 13, PAIR_POTENTIAL: 19; mudanças de composição: 0; posicionamento melhorou em 56 ações e piorou em 47.
- Jogador 1 — estado final: ouro 218, nível 7, vida 1.0, colocação None.
| Jogador 2 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.161 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.109 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 3 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 8 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 11% → 14% | 4 → 5 | 5 | 4 → 4 | -0.020 | -0.289 |
| Jogador 2 | 2-2 | 7 | 0.000 | 2.000 | 1 → 1 | 2 → 1 | 14% → 14% | 5 → 10 | 4 | 4 → 4 | -0.033 | -0.339 |
| Jogador 2 | 2-3 | 5 | 2.000 | 0.000 | 1 → 1 | 1 → 1 | 14% → 18% | 10 → 7 | 9 | 4 → 5 | 0.033 | 0.502 |
| Jogador 2 | 2-4 | 10 | 4.000 | 6.000 | 1 → 1 | 1 → 2 | 18% → 18% | 7 → 7 | 7 | 5 → 5 | 0.052 | 0.000 |
| Jogador 2 | 2-5 | 10 | 0.000 | -4.000 | 1 → 1 | 2 → 2 | 18% → 18% | 7 → 6 | 15 | 5 → 5 | 0.001 | -0.253 |
| Jogador 2 | 2-6 | 9 | 2.000 | 2.000 | 1 → 1 | 2 → 2 | 18% → 21% | 6 → 6 | 9 | 5 → 6 | 0.048 | -0.258 |
| Jogador 2 | 2-7 | 6 | 0.000 | 12.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 6 | 6 | 6 → 6 | -0.033 | 0.000 |
| Jogador 2 | 3-1 | 9 | 2.000 | 2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 6 | 10 | 6 → 6 | -0.004 | 0.307 |
| Jogador 2 | 3-2 | 9 | 2.000 | 6.000 | 1 → 2 | 2 → 2 | 21% → 21% | 6 → 8 | 5 | 6 → 6 | 0.021 | 0.324 |
| Jogador 2 | 3-3 | 2 | 0.000 | -2.000 | 2 → 2 | 2 → 2 | 21% → 21% | 8 → 17 | 0 | 6 → 6 | 0.000 | 1.406 |
| Jogador 2 | 3-4 | 10 | 0.000 | 4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 17 → 22 | 6 | 6 → 6 | -0.042 | 0.000 |
| Jogador 2 | 3-5 | 10 | 0.000 | 2.000 | 2 → 2 | 2 → 4 | 21% → 21% | 22 → 30 | 5 | 6 → 6 | 0.023 | 0.272 |
| Jogador 2 | 3-6 | 9 | 0.000 | 2.000 | 2 → 2 | 4 → 3 | 21% → 21% | 30 → 40 | 7 | 6 → 6 | -0.104 | 0.312 |
| Jogador 2 | 3-7 | 10 | 0.000 | 2.000 | 2 → 2 | 3 → 4 | 21% → 21% | 40 → 49 | 11 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 9 | 0.000 | -2.000 | 2 → 2 | 4 → 5 | 21% → 21% | 49 → 64 | 7 | 6 → 6 | 0.001 | 0.320 |
| Jogador 2 | 4-2 | 2 | 0.000 | -8.000 | 2 → 2 | 5 → 5 | 21% → 21% | 64 → 82 | 0 | 6 → 6 | 0.000 | 1.425 |
| Jogador 2 | 4-3 | 9 | 0.000 | -4.000 | 2 → 2 | 5 → 4 | 21% → 21% | 82 → 93 | 8 | 6 → 6 | -0.005 | -0.303 |
| Jogador 2 | 4-4 | 7 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 21% → 21% | 93 → 103 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-5 | 4 | 0.000 | 8.000 | 2 → 2 | 4 → 4 | 21% → 21% | 103 → 110 | 6 | 6 → 6 | 0.000 | 0.725 |
| Jogador 2 | 4-6 | 7 | 0.000 | -6.000 | 2 → 2 | 4 → 3 | 21% → 21% | 110 → 123 | 2 | 6 → 6 | 0.005 | -0.426 |
| Jogador 2 | 4-7 | 3 | 0.000 | 6.000 | 2 → 2 | 3 → 3 | 21% → 21% | 123 → 130 | 3 | 6 → 7 | 0.016 | 0.000 |
| Jogador 2 | 5-1 | 8 | 4.000 | 4.000 | 2 → 2 | 3 → 3 | 21% → 25% | 130 → 137 | 5 | 7 → 7 | 0.004 | -0.348 |
| Jogador 2 | 5-2 | 2 | 0.000 | 6.000 | 2 → 2 | 3 → 3 | 25% → 25% | 137 → 145 | 3 | 7 → 7 | 0.000 | 1.431 |
| Jogador 2 | 5-3 | 7 | 0.000 | -6.000 | 2 → 2 | 3 → 4 | 25% → 25% | 145 → 160 | 8 | 7 → 7 | 0.000 | 0.409 |
| Jogador 2 | 5-4 | 3 | 0.000 | -2.000 | 2 → 2 | 4 → 5 | 25% → 25% | 160 → 172 | 1 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-5 | 7 | 0.000 | 0.000 | 2 → 2 | 5 → 4 | 25% → 25% | 172 → 183 | 9 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-6 | 3 | 0.000 | 4.000 | 2 → 2 | 4 → 4 | 25% → 25% | 183 → 191 | 4 | 7 → 7 | 0.000 | -0.950 |
| Jogador 2 | 5-7 | 7 | 0.000 | 0.000 | 2 → 2 | 4 → 3 | 25% → 25% | 191 → 200 | 13 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 3 | 0.000 | -6.000 | 2 → 2 | 3 → 3 | 25% → 25% | 200 → 214 | 0 | 7 → 7 | 0.009 | -0.933 |
| Jogador 2 | 6-2 | 5 | -26.000 | -40.000 | 2 → 0 | 3 → 0 | 25% → 0% | 214 → 215 | 5 | 7 → 7 | -0.010 | -0.560 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 27, COMPOSITION_COMPATIBILITY: 29, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 36 ações e piorou em 29.
- Jogador 2 — estado final: ouro 215, nível 7, vida 10.0, colocação 4.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.060 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 3 | 1-4 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.002 | 0.000 |
| Jogador 3 | 2-1 | 8 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.003 | 0.327 |
| Jogador 3 | 2-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.595 |
| Jogador 3 | 2-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 8 | 7 | 4 → 5 | 0.006 | 0.502 |
| Jogador 3 | 2-4 | 9 | 6.000 | 2.000 | 1 → 1 | 1 → 2 | 14% → 18% | 8 → 6 | 8 | 5 → 5 | 0.019 | 0.000 |
| Jogador 3 | 2-5 | 4 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 18% → 18% | 6 → 8 | 5 | 5 → 5 | -0.000 | 0.628 |
| Jogador 3 | 2-6 | 10 | 6.000 | -4.000 | 1 → 2 | 3 → 1 | 18% → 18% | 8 → 8 | 9 | 5 → 5 | 0.002 | 0.246 |
| Jogador 3 | 2-7 | 9 | 6.000 | 2.000 | 2 → 2 | 1 → 2 | 18% → 21% | 8 → 7 | 8 | 5 → 6 | -0.005 | 0.000 |
| Jogador 3 | 3-1 | 9 | -2.000 | 8.000 | 2 → 1 | 2 → 3 | 21% → 21% | 7 → 10 | 9 | 6 → 6 | 0.061 | 0.337 |
| Jogador 3 | 3-2 | 9 | 2.000 | -6.000 | 1 → 2 | 3 → 2 | 21% → 21% | 10 → 9 | 15 | 6 → 6 | 0.010 | 0.328 |
| Jogador 3 | 3-3 | 2 | 0.000 | 4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 9 → 16 | 2 | 6 → 6 | -0.001 | 1.492 |
| Jogador 3 | 3-4 | 10 | 6.000 | 2.000 | 2 → 2 | 2 → 3 | 21% → 25% | 16 → 8 | 18 | 6 → 7 | 0.003 | 0.000 |
| Jogador 3 | 3-5 | 5 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 8 → 17 | 0 | 7 → 7 | 0.014 | 0.562 |
| Jogador 3 | 3-6 | 4 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 17 → 27 | 0 | 7 → 7 | -0.102 | 0.690 |
| Jogador 3 | 3-7 | 4 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 27 → 37 | 0 | 7 → 7 | -0.124 | 0.000 |
| Jogador 3 | 4-1 | 6 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 37 → 45 | 0 | 7 → 7 | -0.000 | -0.452 |
| Jogador 3 | 4-2 | 2 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 45 → 55 | 0 | 7 → 7 | -0.028 | 1.493 |
| Jogador 3 | 4-3 | 9 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 55 → 32 | 32 | 7 → 7 | 0.000 | 0.324 |
| Jogador 3 | 4-4 | 7 | 6.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 29% | 32 → 29 | 11 | 7 → 8 | 0.007 | 0.000 |
| Jogador 3 | 4-5 | 4 | -6.000 | 2.000 | 2 → 1 | 3 → 2 | 29% → 25% | 29 → 37 | 3 | 8 → 8 | -0.026 | 0.721 |
| Jogador 3 | 4-6 | 7 | 6.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 29% | 37 → 26 | 19 | 8 → 8 | -0.003 | 0.448 |
| Jogador 3 | 4-7 | 3 | 0.000 | 8.000 | 1 → 1 | 2 → 1 | 29% → 29% | 26 → 28 | 6 | 8 → 8 | -0.020 | 0.000 |
| Jogador 3 | 5-1 | 8 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 29% → 29% | 28 → 22 | 15 | 8 → 8 | -0.017 | 0.379 |
| Jogador 3 | 5-2 | 2 | 0.000 | -8.000 | 1 → 1 | 1 → 1 | 29% → 29% | 22 → 34 | 0 | 8 → 8 | -0.052 | -1.350 |
| Jogador 3 | 5-3 | 7 | 0.000 | 4.000 | 1 → 1 | 1 → 2 | 29% → 29% | 34 → 19 | 22 | 8 → 8 | 0.024 | -0.386 |
| Jogador 3 | 5-4 | 3 | 0.000 | 0.000 | 1 → 1 | 2 → 3 | 29% → 29% | 19 → 28 | 2 | 8 → 8 | 0.020 | 0.000 |
| Jogador 3 | 5-5 | 7 | 4.000 | -6.000 | 1 → 1 | 3 → 3 | 29% → 32% | 28 → 31 | 13 | 8 → 9 | 0.081 | 0.434 |
| Jogador 3 | 5-6 | 3 | 6.000 | 0.000 | 1 → 2 | 3 → 2 | 32% → 32% | 31 → 34 | 6 | 9 → 9 | -0.001 | 1.002 |
| Jogador 3 | 5-7 | 7 | 0.000 | 10.000 | 2 → 2 | 2 → 3 | 32% → 32% | 34 → 37 | 7 | 9 → 9 | 0.003 | 0.000 |
| Jogador 3 | 6-1 | 3 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 32% → 32% | 37 → 47 | 0 | 9 → 9 | 0.035 | 1.069 |
| Jogador 3 | 6-2 | 5 | 6.000 | -8.000 | 2 → 2 | 3 → 2 | 32% → 32% | 47 → 57 | 4 | 9 → 9 | -0.038 | 0.613 |
| Jogador 3 | 6-3 | 5 | 0.000 | 6.000 | 2 → 2 | 2 → 3 | 32% → 32% | 57 → 67 | 3 | 9 → 9 | -0.024 | 0.609 |
| Jogador 3 | 6-4 | 4 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 32% → 32% | 67 → 79 | 0 | 9 → 9 | 0.044 | 0.000 |
| Jogador 3 | 6-5 | 2 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 32% → 32% | 79 → 79 | 0 | 9 → 9 | 0.000 | 0.000 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 8, COMPOSITION_COMPATIBILITY: 16, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 46 ações e piorou em 37.
- Jogador 3 — estado final: ouro 79, nível 9, vida 62.0, colocação None.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 4 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.065 | 0.000 |
| Jogador 4 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 4 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.013 | 0.000 |
| Jogador 4 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 5 | 5 | 4 → 4 | -0.018 | -0.346 |
| Jogador 4 | 2-2 | 5 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 14% → 18% | 5 → 6 | 5 | 4 → 5 | 0.027 | 0.547 |
| Jogador 4 | 2-3 | 9 | 4.000 | -4.000 | 0 → 0 | 3 → 2 | 18% → 18% | 6 → 9 | 9 | 5 → 5 | 0.006 | 0.299 |
| Jogador 4 | 2-4 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 10 | 12 | 5 → 5 | -0.013 | 0.000 |
| Jogador 4 | 2-5 | 10 | 6.000 | -2.000 | 0 → 0 | 3 → 2 | 18% → 21% | 10 → 5 | 14 | 5 → 6 | -0.003 | -0.237 |
| Jogador 4 | 2-6 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 5 → 8 | 3 | 6 → 6 | 0.019 | -0.354 |
| Jogador 4 | 2-7 | 10 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 9 | 10 | 6 → 6 | 0.009 | 0.000 |
| Jogador 4 | 3-1 | 9 | -2.000 | 8.000 | 0 → 0 | 2 → 3 | 21% → 21% | 9 → 8 | 10 | 6 → 6 | -0.010 | -0.318 |
| Jogador 4 | 3-2 | 9 | 4.000 | 4.000 | 0 → 1 | 3 → 2 | 21% → 21% | 8 → 9 | 5 | 6 → 6 | -0.032 | -0.298 |
| Jogador 4 | 3-3 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 1 | 21% → 21% | 9 → 14 | 2 | 6 → 6 | -0.030 | -1.316 |
| Jogador 4 | 3-4 | 8 | 0.000 | 14.000 | 1 → 1 | 1 → 1 | 21% → 21% | 14 → 14 | 7 | 6 → 6 | 0.019 | 0.000 |
| Jogador 4 | 3-5 | 7 | 0.000 | 8.000 | 1 → 1 | 1 → 3 | 21% → 21% | 14 → 19 | 4 | 6 → 6 | -0.035 | -0.370 |
| Jogador 4 | 3-6 | 9 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 19 → 28 | 5 | 6 → 6 | 0.029 | -0.304 |
| Jogador 4 | 3-7 | 6 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 21% → 21% | 28 → 35 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-1 | 7 | -2.000 | 2.000 | 1 → 0 | 4 → 4 | 21% → 21% | 35 → 46 | 0 | 6 → 6 | -0.017 | -0.389 |
| Jogador 4 | 4-2 | 2 | 0.000 | -4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 46 → 61 | 0 | 6 → 6 | 0.030 | -1.416 |
| Jogador 4 | 4-3 | 9 | -22.000 | -46.000 | 0 → 0 | 4 → 0 | 21% → 0% | 61 → 59 | 2 | 6 → 6 | -0.028 | -0.287 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 14, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 37 ações e piorou em 29.
- Jogador 4 — estado final: ouro 59, nível 6, vida 8.0, colocação 8.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.112 | 0.000 |
| Jogador 5 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.003 | 0.000 |
| Jogador 5 | 2-1 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.000 | 0.347 |
| Jogador 5 | 2-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.641 |
| Jogador 5 | 2-3 | 9 | 6.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 9 | 7 | 4 → 5 | -0.007 | -0.264 |
| Jogador 5 | 2-4 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 9 → 6 | 15 | 5 → 5 | 0.000 | 0.000 |
| Jogador 5 | 2-5 | 10 | 2.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 6 → 6 | 13 | 5 → 6 | -0.006 | 0.269 |
| Jogador 5 | 2-6 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 9 | 7 | 6 → 6 | 0.019 | -0.258 |
| Jogador 5 | 2-7 | 10 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 9 → 11 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-1 | 9 | 0.000 | 0.000 | 0 → 0 | 2 → 1 | 21% → 21% | 11 → 17 | 9 | 6 → 6 | 0.001 | -0.304 |
| Jogador 5 | 3-2 | 9 | 0.000 | -6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 17 → 28 | 7 | 6 → 6 | 0.000 | 0.318 |
| Jogador 5 | 3-3 | 2 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 21% → 21% | 28 → 33 | 2 | 6 → 6 | 0.000 | -1.407 |
| Jogador 5 | 3-4 | 10 | -4.000 | -6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 33 → 46 | 4 | 6 → 6 | -0.002 | 0.000 |
| Jogador 5 | 3-5 | 10 | 0.000 | -4.000 | 0 → 0 | 2 → 1 | 21% → 21% | 46 → 58 | 9 | 6 → 6 | 0.000 | -0.254 |
| Jogador 5 | 3-6 | 9 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 58 → 69 | 6 | 6 → 6 | 0.000 | 0.318 |
| Jogador 5 | 3-7 | 10 | 4.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 69 → 75 | 11 | 6 → 6 | 0.064 | 0.000 |
| Jogador 5 | 4-1 | 9 | 0.000 | 18.000 | 0 → 0 | 1 → 2 | 21% → 21% | 75 → 76 | 10 | 6 → 6 | -0.039 | -0.297 |
| Jogador 5 | 4-2 | 2 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 21% → 21% | 76 → 86 | 1 | 6 → 6 | 0.000 | -1.338 |
| Jogador 5 | 4-3 | 9 | 4.000 | 8.000 | 0 → 0 | 3 → 2 | 21% → 21% | 86 → 91 | 9 | 6 → 6 | -0.008 | -0.306 |
| Jogador 5 | 4-4 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 21% → 21% | 91 → 102 | 5 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-5 | 4 | 0.000 | -8.000 | 0 → 0 | 3 → 4 | 21% → 21% | 102 → 117 | 1 | 6 → 6 | 0.000 | -0.679 |
| Jogador 5 | 4-6 | 7 | 0.000 | 4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 117 → 126 | 7 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-7 | 3 | 0.000 | -4.000 | 0 → 0 | 4 → 5 | 21% → 21% | 126 → 139 | 1 | 6 → 7 | 0.016 | 0.000 |
| Jogador 5 | 5-1 | 8 | -20.000 | -28.000 | 0 → 0 | 5 → 0 | 21% → 0% | 139 → 136 | 7 | 7 → 7 | -0.077 | -0.356 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 28, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 15; mudanças de composição: 1; posicionamento melhorou em 25 ações e piorou em 20.
- Jogador 5 — estado final: ouro 136, nível 7, vida 11.0, colocação 7.
| Jogador 6 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.163 | 0.000 |
| Jogador 6 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.039 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.018 | -0.353 |
| Jogador 6 | 2-2 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | -0.010 | -0.430 |
| Jogador 6 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 9 | 5 | 4 → 5 | -0.005 | -0.330 |
| Jogador 6 | 2-4 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 3 | 14% → 14% | 9 → 10 | 13 | 5 → 5 | 0.006 | 0.000 |
| Jogador 6 | 2-5 | 10 | 2.000 | -12.000 | 0 → 0 | 3 → 4 | 14% → 18% | 10 → 9 | 15 | 5 → 6 | 0.052 | -0.247 |
| Jogador 6 | 2-6 | 10 | 2.000 | 0.000 | 0 → 0 | 4 → 3 | 18% → 21% | 9 → 6 | 13 | 6 → 6 | 0.010 | 0.291 |
| Jogador 6 | 2-7 | 10 | 0.000 | 2.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 10 | 7 | 6 → 6 | 0.014 | 0.000 |
| Jogador 6 | 3-1 | 9 | 4.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 10 → 7 | 13 | 6 → 6 | 0.018 | -0.287 |
| Jogador 6 | 3-2 | 9 | 8.000 | -2.000 | 0 → 1 | 3 → 1 | 21% → 21% | 7 → 8 | 5 | 6 → 6 | 0.030 | -0.298 |
| Jogador 6 | 3-3 | 2 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 21% → 21% | 8 → 11 | 3 | 6 → 6 | 0.000 | 1.500 |
| Jogador 6 | 3-4 | 7 | 0.000 | 20.000 | 1 → 1 | 1 → 1 | 21% → 21% | 11 → 6 | 10 | 6 → 6 | -0.019 | 0.000 |
| Jogador 6 | 3-5 | 7 | 0.000 | 10.000 | 1 → 1 | 1 → 1 | 21% → 21% | 6 → 8 | 5 | 6 → 6 | -0.025 | 0.388 |
| Jogador 6 | 3-6 | 9 | 0.000 | 0.000 | 1 → 1 | 1 → 3 | 21% → 21% | 8 → 14 | 5 | 6 → 6 | 0.019 | -0.287 |
| Jogador 6 | 3-7 | 10 | 0.000 | -8.000 | 1 → 1 | 3 → 2 | 21% → 21% | 14 → 24 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 9 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 24 → 30 | 7 | 6 → 7 | 0.005 | 0.317 |
| Jogador 6 | 4-2 | 2 | 6.000 | -2.000 | 1 → 1 | 2 → 3 | 21% → 25% | 30 → 37 | 2 | 7 → 7 | -0.016 | 1.450 |
| Jogador 6 | 4-3 | 6 | 0.000 | 12.000 | 1 → 1 | 3 → 3 | 25% → 25% | 37 → 41 | 6 | 7 → 7 | 0.010 | 0.483 |
| Jogador 6 | 4-4 | 7 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 41 → 52 | 1 | 7 → 7 | 0.009 | 0.000 |
| Jogador 6 | 4-5 | 4 | 0.000 | -4.000 | 1 → 1 | 3 → 3 | 25% → 25% | 52 → 64 | 1 | 7 → 7 | 0.000 | -0.669 |
| Jogador 6 | 4-6 | 7 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 25% → 25% | 64 → 72 | 4 | 7 → 7 | 0.078 | 0.445 |
| Jogador 6 | 4-7 | 3 | 0.000 | -2.000 | 1 → 1 | 4 → 5 | 25% → 25% | 72 → 83 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 8 | 0.000 | 6.000 | 1 → 1 | 5 → 4 | 25% → 25% | 83 → 87 | 9 | 7 → 7 | -0.008 | 0.000 |
| Jogador 6 | 5-2 | 2 | 0.000 | -12.000 | 1 → 1 | 4 → 4 | 25% → 25% | 87 → 105 | 0 | 7 → 7 | 0.030 | -1.450 |
| Jogador 6 | 5-3 | 7 | 2.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 21% | 105 → 113 | 4 | 7 → 7 | 0.011 | 0.000 |
| Jogador 6 | 5-4 | 3 | 8.000 | 0.000 | 1 → 1 | 4 → 5 | 21% → 25% | 113 → 119 | 4 | 7 → 7 | 0.030 | 0.000 |
| Jogador 6 | 5-5 | 5 | 0.000 | 6.000 | 1 → 1 | 5 → 5 | 25% → 25% | 119 → 127 | 3 | 7 → 7 | -0.064 | -0.570 |
| Jogador 6 | 5-6 | 3 | 0.000 | 2.000 | 1 → 1 | 5 → 6 | 25% → 25% | 127 → 138 | 3 | 7 → 7 | 0.020 | 0.000 |
| Jogador 6 | 5-7 | 7 | 0.000 | 0.000 | 1 → 1 | 6 → 6 | 25% → 25% | 138 → 149 | 1 | 7 → 7 | -0.003 | 0.000 |
| Jogador 6 | 6-1 | 3 | 0.000 | -2.000 | 1 → 1 | 6 → 6 | 25% → 25% | 149 → 161 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 6-2 | 5 | -40.000 | -50.000 | 1 → 0 | 6 → 0 | 25% → 0% | 161 → 158 | 6 | 7 → 7 | -0.182 | -0.570 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 14, COMPOSITION_COMPATIBILITY: 31, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 12; mudanças de composição: 0; posicionamento melhorou em 37 ações e piorou em 32.
- Jogador 6 — estado final: ouro 158, nível 7, vida 8.0, colocação 3.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.043 | 0.000 |
| Jogador 7 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.077 | 0.000 |
| Jogador 7 | 2-1 | 7 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.014 | 0.391 |
| Jogador 7 | 2-2 | 7 | 2.000 | 4.000 | 0 → 1 | 3 → 2 | 14% → 14% | 8 → 5 | 8 | 4 → 4 | -0.029 | -0.323 |
| Jogador 7 | 2-3 | 4 | 2.000 | 0.000 | 1 → 2 | 2 → 2 | 14% → 14% | 5 → 9 | 2 | 4 → 5 | 0.123 | 0.607 |
| Jogador 7 | 2-4 | 10 | 0.000 | -12.000 | 2 → 2 | 2 → 1 | 14% → 14% | 9 → 8 | 15 | 5 → 5 | -0.006 | 0.000 |
| Jogador 7 | 2-5 | 10 | 2.000 | 2.000 | 2 → 2 | 1 → 1 | 14% → 18% | 8 → 9 | 9 | 5 → 6 | 0.012 | 0.251 |
| Jogador 7 | 2-6 | 7 | 8.000 | 2.000 | 2 → 2 | 1 → 1 | 18% → 21% | 9 → 11 | 5 | 6 → 6 | 0.021 | 0.391 |
| Jogador 7 | 2-7 | 7 | 0.000 | 10.000 | 2 → 2 | 1 → 1 | 21% → 21% | 11 → 12 | 5 | 6 → 6 | -0.004 | 0.000 |
| Jogador 7 | 3-1 | 9 | 0.000 | 10.000 | 2 → 2 | 1 → 1 | 21% → 21% | 12 → 14 | 5 | 6 → 6 | 0.033 | 0.324 |
| Jogador 7 | 3-2 | 7 | 0.000 | 10.000 | 2 → 2 | 1 → 1 | 21% → 21% | 14 → 15 | 7 | 6 → 6 | -0.024 | 0.409 |
| Jogador 7 | 3-3 | 2 | 4.000 | -4.000 | 2 → 2 | 1 → 0 | 21% → 21% | 15 → 24 | 1 | 6 → 6 | -0.031 | 1.431 |
| Jogador 7 | 3-4 | 7 | 0.000 | 14.000 | 2 → 2 | 0 → 2 | 21% → 21% | 24 → 26 | 7 | 6 → 6 | -0.031 | 0.000 |
| Jogador 7 | 3-5 | 7 | 0.000 | 2.000 | 2 → 2 | 2 → 3 | 21% → 21% | 26 → 33 | 3 | 6 → 6 | 0.031 | -0.376 |
| Jogador 7 | 3-6 | 9 | 0.000 | 4.000 | 2 → 2 | 3 → 4 | 21% → 21% | 33 → 41 | 8 | 6 → 6 | 0.011 | -0.293 |
| Jogador 7 | 3-7 | 9 | 0.000 | 4.000 | 2 → 2 | 4 → 3 | 21% → 21% | 41 → 45 | 8 | 6 → 6 | 0.010 | 0.000 |
| Jogador 7 | 4-1 | 9 | 0.000 | -8.000 | 2 → 2 | 3 → 3 | 21% → 21% | 45 → 62 | 6 | 6 → 6 | 0.007 | 0.322 |
| Jogador 7 | 4-2 | 2 | 0.000 | -4.000 | 2 → 2 | 3 → 3 | 21% → 21% | 62 → 74 | 0 | 6 → 6 | 0.000 | -1.363 |
| Jogador 7 | 4-3 | 9 | 0.000 | 0.000 | 2 → 2 | 3 → 5 | 21% → 21% | 74 → 83 | 12 | 6 → 6 | 0.000 | 0.333 |
| Jogador 7 | 4-4 | 7 | 0.000 | 4.000 | 2 → 2 | 5 → 5 | 21% → 21% | 83 → 91 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 4-5 | 4 | 2.000 | -8.000 | 2 → 3 | 5 → 3 | 21% → 21% | 91 → 102 | 4 | 6 → 6 | -0.025 | 0.713 |
| Jogador 7 | 4-6 | 7 | -2.000 | 12.000 | 3 → 3 | 3 → 2 | 21% → 21% | 102 → 105 | 7 | 6 → 6 | -0.014 | -0.389 |
| Jogador 7 | 4-7 | 3 | 0.000 | 6.000 | 3 → 3 | 2 → 2 | 21% → 21% | 105 → 112 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 5-1 | 8 | -2.000 | -10.000 | 3 → 3 | 2 → 3 | 21% → 21% | 112 → 132 | 4 | 6 → 6 | -0.054 | 0.396 |
| Jogador 7 | 5-2 | 2 | 0.000 | -4.000 | 3 → 3 | 3 → 3 | 21% → 21% | 132 → 146 | 0 | 6 → 7 | 0.024 | 1.586 |
| Jogador 7 | 5-3 | 7 | 4.000 | 14.000 | 3 → 3 | 3 → 2 | 21% → 25% | 146 → 145 | 11 | 7 → 7 | 0.026 | -0.407 |
| Jogador 7 | 5-4 | 3 | 0.000 | -8.000 | 3 → 3 | 2 → 1 | 25% → 25% | 145 → 157 | 3 | 7 → 7 | 0.100 | 0.000 |
| Jogador 7 | 5-5 | 6 | 6.000 | 6.000 | 3 → 4 | 1 → 1 | 25% → 25% | 157 → 162 | 6 | 7 → 7 | -0.036 | -0.475 |
| Jogador 7 | 5-6 | 3 | 0.000 | 2.000 | 4 → 4 | 1 → 2 | 25% → 25% | 162 → 172 | 3 | 7 → 7 | 0.000 | -0.950 |
| Jogador 7 | 5-7 | 7 | 0.000 | -6.000 | 4 → 4 | 2 → 3 | 25% → 25% | 172 → 186 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 3 | -34.000 | -54.000 | 4 → 0 | 3 → 0 | 25% → 0% | 186 → 188 | 0 | 7 → 7 | -0.140 | -1.000 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 18, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 14; mudanças de composição: 0; posicionamento melhorou em 36 ações e piorou em 39.
- Jogador 7 — estado final: ouro 188, nível 7, vida 7.0, colocação 5.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.113 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.074 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 3 | 3 → 4 | 0.007 | 0.000 |
| Jogador 8 | 2-1 | 8 | 6.000 | -2.000 | 0 → 2 | 2 → 0 | 11% → 14% | 6 → 7 | 4 | 4 → 4 | -0.003 | -0.322 |
| Jogador 8 | 2-2 | 7 | 0.000 | 12.000 | 2 → 2 | 0 → 0 | 14% → 14% | 7 → 7 | 7 | 4 → 4 | 0.019 | -0.346 |
| Jogador 8 | 2-3 | 9 | 2.000 | 4.000 | 2 → 2 | 0 → 0 | 14% → 14% | 7 → 6 | 10 | 4 → 5 | 0.003 | -0.281 |
| Jogador 8 | 2-4 | 10 | 6.000 | 6.000 | 2 → 2 | 0 → 0 | 14% → 18% | 6 → 6 | 8 | 5 → 5 | -0.021 | 0.000 |
| Jogador 8 | 2-5 | 10 | 0.000 | -10.000 | 2 → 2 | 0 → 2 | 18% → 18% | 6 → 18 | 8 | 5 → 5 | -0.022 | -0.237 |
| Jogador 8 | 2-6 | 10 | 0.000 | -4.000 | 2 → 2 | 2 → 2 | 18% → 18% | 18 → 29 | 8 | 5 → 5 | 0.000 | -0.274 |
| Jogador 8 | 2-7 | 10 | 0.000 | 12.000 | 2 → 2 | 2 → 2 | 18% → 18% | 29 → 19 | 20 | 5 → 6 | 0.005 | 0.000 |
| Jogador 8 | 3-1 | 9 | 6.000 | 14.000 | 2 → 2 | 2 → 2 | 18% → 21% | 19 → 11 | 14 | 6 → 6 | 0.003 | 0.324 |
| Jogador 8 | 3-2 | 9 | 0.000 | 2.000 | 2 → 2 | 2 → 2 | 21% → 21% | 11 → 16 | 9 | 6 → 6 | 0.000 | -0.304 |
| Jogador 8 | 3-3 | 2 | 0.000 | -4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 16 → 25 | 0 | 6 → 6 | 0.000 | -1.341 |
| Jogador 8 | 3-4 | 10 | 0.000 | -2.000 | 2 → 2 | 2 → 3 | 21% → 21% | 25 → 34 | 7 | 6 → 6 | 0.013 | 0.000 |
| Jogador 8 | 3-5 | 10 | -2.000 | 0.000 | 2 → 2 | 3 → 3 | 21% → 21% | 34 → 43 | 9 | 6 → 6 | -0.005 | -0.254 |
| Jogador 8 | 3-6 | 9 | -2.000 | 22.000 | 2 → 2 | 3 → 2 | 21% → 21% | 43 → 39 | 15 | 6 → 6 | -0.007 | 0.324 |
| Jogador 8 | 3-7 | 10 | 0.000 | -10.000 | 2 → 2 | 2 → 2 | 21% → 21% | 39 → 55 | 7 | 6 → 6 | 0.002 | 0.000 |
| Jogador 8 | 4-1 | 9 | 0.000 | -4.000 | 2 → 2 | 2 → 3 | 21% → 21% | 55 → 69 | 6 | 6 → 6 | 0.000 | 0.317 |
| Jogador 8 | 4-2 | 2 | 0.000 | -4.000 | 2 → 2 | 3 → 3 | 21% → 21% | 69 → 83 | 0 | 6 → 6 | 0.000 | 1.517 |
| Jogador 8 | 4-3 | 9 | 0.000 | 4.000 | 2 → 2 | 3 → 4 | 21% → 21% | 83 → 91 | 10 | 6 → 6 | 0.000 | -0.314 |
| Jogador 8 | 4-4 | 7 | 0.000 | -2.000 | 2 → 2 | 4 → 5 | 21% → 21% | 91 → 102 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 4 | 4.000 | -4.000 | 2 → 2 | 5 → 3 | 21% → 21% | 102 → 108 | 4 | 6 → 6 | -0.183 | 0.000 |
| Jogador 8 | 4-6 | 7 | 0.000 | 6.000 | 2 → 2 | 3 → 3 | 21% → 21% | 108 → 117 | 5 | 6 → 6 | 0.009 | -0.421 |
| Jogador 8 | 4-7 | 3 | 0.000 | 6.000 | 2 → 2 | 3 → 3 | 21% → 21% | 117 → 125 | 3 | 6 → 6 | -0.020 | 0.000 |
| Jogador 8 | 5-1 | 8 | -4.000 | 0.000 | 2 → 2 | 3 → 2 | 21% → 21% | 125 → 137 | 7 | 6 → 6 | -0.019 | -0.375 |
| Jogador 8 | 5-2 | 2 | -22.000 | -48.000 | 2 → 0 | 2 → 0 | 21% → 0% | 137 → 136 | 1 | 6 → 6 | 0.579 | -1.500 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 27, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 17; mudanças de composição: 1; posicionamento melhorou em 35 ações e piorou em 28.
- Jogador 8 — estado final: ouro 136, nível 6, vida 1.0, colocação 6.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 69 | 29 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 2 | 0 |
| Jogador 2 | 75 | 49 | 1 | 1 | 1 | 0 | 0 | 0 | 18 | 2 | 0 | 0 |
| Jogador 3 | 43 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 4 | 39 | 15 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 4 | 0 | 0 |
| Jogador 5 | 71 | 51 | 3 | 8 | 13 | 3 | 1 | 0 | 4 | 1 | 3 | 0 |
| Jogador 6 | 61 | 38 | 1 | 1 | 3 | 0 | 1 | 1 | 4 | 2 | 1 | 0 |
| Jogador 7 | 65 | 31 | 0 | 1 | 1 | 0 | 0 | 0 | 9 | 0 | 1 | 0 |
| Jogador 8 | 77 | 47 | 3 | 3 | 5 | 0 | 1 | 0 | 12 | 1 | 1 | 0 |
- Jogador 1 — venda DA_18_Ornn (2-5, step 84): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Rakan (2-7, step 108): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 1 — venda DA_18_Camille (4-3, step 183): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Sentry (4-3, step 188): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 1 — venda DA_18_Warwick (4-4, step 193): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 1 — venda DA_KogMaw18_AD (5-1, step 217): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 1 — venda DA_Nidalee18_AP (6-4, step 264): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_18_Teemo (3-6, step 156): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_CrimsonRaptor18 (3-7, step 165): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rakan (4-6, step 206): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 2 — venda DA_18_Azir (5-5, step 232): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_RekSai (5-4, step 229): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Vi18 (5-5, step 233): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Rakan (2-5, step 88): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_18_Rakan (2-7, step 106): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 5 — venda DA_18_Tristana (3-2, step 124): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_Kobuko (3-4, step 136): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (3-4, step 138): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (3-5, step 149): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Yunara (3-5, step 150): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (4-3, step 186): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Shen (4-6, step 203): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-6, step 97): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 6 — venda DA_18_Sentry (3-6, step 152): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Alistar (3-7, step 166): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Xayah (5-6, step 239): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Karma18 (2-6, step 100): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Warwick (3-4, step 135): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Karma18 (3-5, step 144): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_LeBlanc (3-6, step 154): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_LeBlanc (4-3, step 185): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_LeBlanc (4-4, step 196): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rakan (4-6, step 205): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Tristana (5-1, step 214): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.

Vendas de core/pares ignoradas antes da decisão da composição: **5**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| LOW | Jogador 1 | 2-3 | 65 | PURCHASE_SALE_REVIEW | Compra de DA_18_Shen foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 1 | 2-3 | 67 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 1 | 2-5 | 84 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-3 | 183 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-4 | 193 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Warwick) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 1 | 2-2 | 56 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 57 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 58 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 59 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 60 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 61 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-3 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-3 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-3 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-3 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-3 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 248 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 249 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 250 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 253 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 254 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 255 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 256 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 257 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 258 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 259 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 260 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 261 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-4 | 262 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-4 | 263 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 502 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-3 | 628 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 762 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-5 | 871 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 991 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-7 | 1130 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1253 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-2 | 1372 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-3 | 1408 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-4 | 1544 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-4 | 1545 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1666 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-5 | 1667 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1791 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-6 | 1792 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 1875 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-1 | 1960 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-1 | 1961 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 1999 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 2000 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-3 | 2128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-3 | 2129 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 2228 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-5 | 2289 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-6 | 2387 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-7 | 2438 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-2 | 3113 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-3 | 3189 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-4 | 3292 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| MEDIUM | Jogador 1 | 3-4 | 1643 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 3-6 | 1852 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 3-7 | 1937 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-5 | 86 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-6 | 156 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-7 | 165 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-5 | 232 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Azir' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 4-3 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-2 | 537 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-3 | 607 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-7 | 1090 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-1 | 1212 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-5 | 1653 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-6 | 1781 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-7 | 1921 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-7 | 1922 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-1 | 2046 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-1 | 2047 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-2 | 2085 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-2 | 2086 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2211 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-3 | 2212 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 2314 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-4 | 2315 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2378 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-5 | 2379 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 2484 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-6 | 2485 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 2535 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-7 | 2536 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 2650 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-1 | 2651 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 2690 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-2 | 2691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-3 | 2791 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-3 | 2792 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-4 | 2845 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-4 | 2846 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-5 | 2946 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-5 | 2947 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-6 | 2998 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-6 | 2999 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-7 | 3102 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-7 | 3103 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-1 | 3155 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-1 | 3156 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-2 | 3236 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 6-2 | 3237 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 3-4 | 1630 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 3 | 5-4 | 229 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 5-5 | 233 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-4 | 701 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-5 | 759 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-6 | 890 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 1010 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1131 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1248 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-3 | 1284 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1413 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1486 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 1545 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 1606 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-7 | 1607 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 1694 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-2 | 1731 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-2 | 1732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-3 | 1845 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-3 | 1846 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-4 | 1941 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-4 | 1942 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-5 | 2003 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-5 | 2004 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-6 | 2099 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-6 | 2100 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-7 | 2149 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-7 | 2150 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-1 | 2259 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-1 | 2260 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-2 | 2298 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-2 | 2299 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-3 | 2392 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-3 | 2393 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-4 | 2444 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-4 | 2445 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-5 | 2541 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-6 | 2595 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-7 | 2699 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-1 | 2750 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 6-1 | 2751 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-2 | 2830 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-3 | 2906 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-4 | 2969 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| MEDIUM | Jogador 3 | 4-3 | 1870 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-2 | 2325 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-2 | 2336 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-2 | 2347 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-2 | 2358 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-2 | 2369 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-4 | 2495 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-4 | 2506 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 4 | 3-5 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-5 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-5 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-5 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-5 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-5 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 3-5 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-2 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 4-3 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 3-2 | 1346 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-3 | 1383 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-4 | 1491 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-5 | 1588 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-5 | 1589 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-6 | 1709 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 1793 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-1 | 1894 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 1933 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-3 | 2061 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-3 | 2062 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 3-4 | 1565 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-5 | 1686 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-6 | 1770 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-7 | 1871 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-4 | 78 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 96 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 97 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Elise) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-7 | 108 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rakan) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-7 | 109 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Scuttlecrab18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-1 | 119 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Elise) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-2 | 127 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 3-4 | 135 | PURCHASE_SALE_REVIEW | Compra de DA_18_Teemo foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 3-4 | 136 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-4 | 138 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 3-5 | 146 | PURCHASE_SALE_REVIEW | Compra de DA_Krug18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 3-5 | 147 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_CrimsonRaptor18) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-5 | 149 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-5 | 150 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-6 | 155 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rakan) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-6 | 156 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Murkwolf18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-6 | 157 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-6 | 159 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-7 | 165 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rengar) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 3-7 | 168 | PURCHASE_SALE_REVIEW | Compra de DA_Scuttlecrab18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 5 | 4-3 | 186 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-6 | 203 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Shen' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 2-1 | 52 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 53 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 55 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 56 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 57 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 58 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 68 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 69 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 70 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 75 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 76 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 77 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 78 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 79 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 100 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 107 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 108 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 109 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 110 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 148 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 149 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 169 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 170 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 179 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 207 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 208 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 209 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 210 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 217 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 218 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 219 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-3 | 547 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 679 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 812 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 946 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-7 | 1081 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-1 | 1204 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1325 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-3 | 1361 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-4 | 1496 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1632 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1754 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2182 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-4 | 2283 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-5 | 2348 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 2446 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-7 | 2496 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 2608 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-1 | 2609 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 2-3 | 67 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 3-1 | 117 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Alistar) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 6 | 3-6 | 152 | SOLD_CORE_UNIT | Venda de 'DA_18_Sentry' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 3-7 | 165 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Sentinel18) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 3-7 | 166 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 4-1 | 178 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Elise) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 6 | 5-6 | 239 | SOLD_CORE_UNIT | Venda de 'DA_18_Xayah' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 2-2 | 56 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 57 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 58 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 59 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 60 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 68 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 75 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 76 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 77 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 78 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 79 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-3 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-4 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-5 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-6 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 169 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 170 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 179 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 207 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 208 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 209 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 210 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 217 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 218 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 5-1 | 219 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-3 | 223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-4 | 270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-1 | 367 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-2 | 451 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 549 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 684 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-5 | 817 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-6 | 949 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1087 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1209 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1340 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1377 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1479 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1581 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-6 | 1709 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1848 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 1972 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 2010 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 2100 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 2200 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-5 | 2265 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 2365 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-7 | 2415 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 2531 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-2 | 2570 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-3 | 2673 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-4 | 2725 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-5 | 2803 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-6 | 2857 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-7 | 2963 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 6-1 | 3016 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 6-2 | 3092 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 6-2 | 3093 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 4-2 | 2077 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-3 | 2177 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-5 | 2342 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 7 | 2-5 | 86 | PURCHASE_SALE_REVIEW | Compra de DA_18_Xayah foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 7 | 2-5 | 89 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Veigar) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 7 | 3-7 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 170 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 207 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 208 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 209 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 210 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 441 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 541 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-3 | 601 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 2-4 | 732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 2-5 | 868 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 2-6 | 966 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-6 | 967 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 2-7 | 1064 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-7 | 1065 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 3-1 | 1191 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1293 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1333 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1431 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1534 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1661 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 1787 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 1915 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 1953 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2079 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2180 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2243 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2346 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2396 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 2509 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-1 | 2510 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-2 | 2549 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-2 | 2550 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-3 | 2650 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-3 | 2651 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-4 | 2703 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-4 | 2704 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-5 | 2791 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-5 | 2792 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-6 | 2842 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-6 | 2843 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-7 | 2945 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-7 | 2946 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-1 | 2999 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 6-1 | 3000 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 3-3 | 1408 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-4 | 1511 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-5 | 1638 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-6 | 1764 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-5 | 2323 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 5-4 | 2768 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 8 | 1-4 | 41 | PURCHASE_SALE_REVIEW | Compra de DA_18_RekSai foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-2 | 59 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kobuko) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-6 | 97 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_RekSai) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-6 | 98 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Diana) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-6 | 100 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Karma18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 2-7 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-7 | 108 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Varus) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-4 | 135 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-3 | 185 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_LeBlanc' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-4 | 196 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_LeBlanc' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-6 | 205 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 3-6 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 3-6 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-3 | 224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-4 | 321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 433 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-2 | 531 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 790 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-5 | 924 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-6 | 1066 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1198 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1319 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-2 | 1443 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1479 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-4 | 1614 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-5 | 1750 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-6 | 1876 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 2009 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 2132 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-2 | 2169 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 2298 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-4 | 2408 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-5 | 2471 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-6 | 2577 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-7 | 2627 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-1 | 2741 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-2 | 2780 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 5-2 | 2781 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 3-6 | 1986 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
