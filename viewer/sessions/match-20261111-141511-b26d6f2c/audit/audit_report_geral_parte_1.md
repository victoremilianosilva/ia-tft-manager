# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4214**
- Achados: **636**
- CRITICAL: 0 | HIGH: 6 | MEDIUM: 23 | LOW: 607

## Metadados da sessão

- Match ID: b26d6f2c-a8f2-40df-aba8-30b2b7945d61
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 3d63262fb93d7504bfc05b4e6efd43b7d3bf9e722c0407b8e8b1bd7903bc856d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **3659**
- Entradas posteriores à eliminação ignoradas: **555**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 124 | 7 | 6 | 3 | 47 | 2 | 1 | não/inconclusivo | 0 |
| Jogador 6 | 123 | 7 | 13 | 0 | 48 | 4 | 2 | não/inconclusivo | 0 |
| Jogador 7 | 232 | 7 | 8 | 1 | 65 | 5 | 0 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 163 | 68 | 35 | 8 | 0 | 7 | 34 | 0.1493 | 9 | 42 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::SELL: 2, FAST8::BUY: 18, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 2, FAST8::SELL: 13, STABILIZE::BUY: 48, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 10, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 17, STABILIZE::PASS: 7, STABILIZE::SELL: 20
- Jogador 1 — recompensas por ação: BUY: média 0.3828 (n=68), BUY_XP: média -0.0413 (n=8), ITEM: média 0.1818 (n=11), MOVE_BENCH: média 0.2341 (n=17), MOVE_BOARD: média 0.0100 (n=17), PASS: média -0.0086 (n=7), SELL: média -0.2129 (n=35)
| Jogador 2 | 105 | 47 | 26 | 2 | 1 | 5 | 19 | 0.1192 | 2 | 5 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 5, ALL_IN::MOVE_BENCH: 2, ALL_IN::SELL: 4, STABILIZE::BUY: 42, STABILIZE::BUY_XP: 2, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 8, STABILIZE::MOVE_BOARD: 9, STABILIZE::PASS: 5, STABILIZE::REROLL: 1, STABILIZE::SELL: 22
- Jogador 2 — recompensas por ação: BUY: média 0.3515 (n=47), BUY_XP: média 0.0050 (n=2), ITEM: média 0.2040 (n=5), MOVE_BENCH: média 0.2810 (n=10), MOVE_BOARD: média -0.0233 (n=9), PASS: média 0.0000 (n=5), REROLL: média -0.1300 (n=1), SELL: média -0.2885 (n=26)
| Jogador 3 | 130 | 53 | 23 | 2 | 0 | 6 | 38 | 0.1548 | 3 | 15 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 5, ALL_IN::ITEM: 1, ALL_IN::SELL: 2, STABILIZE::BUY: 48, STABILIZE::BUY_XP: 2, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 17, STABILIZE::MOVE_BOARD: 21, STABILIZE::PASS: 6, STABILIZE::SELL: 21
- Jogador 3 — recompensas por ação: BUY: média 0.3672 (n=53), BUY_XP: média -0.0500 (n=2), ITEM: média 0.1825 (n=8), MOVE_BENCH: média 0.1888 (n=17), MOVE_BOARD: média -0.0019 (n=21), PASS: média 0.0000 (n=6), SELL: média -0.1683 (n=23)
| Jogador 4 | 118 | 47 | 20 | 6 | 2 | 7 | 29 | 0.1603 | 7 | 19 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 10, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 9, STABILIZE::BUY: 37, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 15, STABILIZE::PASS: 7, STABILIZE::SELL: 11
- Jogador 4 — recompensas por ação: BUY: média 0.4381 (n=47), BUY_XP: média -0.0500 (n=6), ITEM: média 0.2143 (n=7), MOVE_BENCH: média 0.2914 (n=14), MOVE_BOARD: média -0.0020 (n=15), PASS: média -0.0129 (n=7), REROLL: média -0.0700 (n=2), SELL: média -0.3350 (n=20)
| Jogador 5 | 142 | 64 | 40 | 4 | 1 | 6 | 17 | 0.1329 | 7 | 21 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 5, ALL_IN::ITEM: 1, ALL_IN::SELL: 6, STABILIZE::BUY: 59, STABILIZE::BUY_XP: 4, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 12, STABILIZE::MOVE_BOARD: 5, STABILIZE::PASS: 6, STABILIZE::REROLL: 1, STABILIZE::SELL: 34
- Jogador 5 — recompensas por ação: BUY: média 0.3617 (n=64), BUY_XP: média -0.0250 (n=4), ITEM: média 0.1480 (n=10), MOVE_BENCH: média 0.1842 (n=12), MOVE_BOARD: média 0.0400 (n=5), PASS: média 0.0000 (n=6), REROLL: média -0.1600 (n=1), SELL: média -0.1978 (n=40)
| Jogador 6 | 126 | 48 | 24 | 13 | 0 | 7 | 25 | 0.1020 | 8 | 34 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 3, ALL_IN::MOVE_BENCH: 4, ALL_IN::SELL: 1, STABILIZE::BUY: 45, STABILIZE::BUY_XP: 13, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 8, STABILIZE::PASS: 7, STABILIZE::SELL: 23
- Jogador 6 — recompensas por ação: BUY: média 0.3656 (n=48), BUY_XP: média -0.0423 (n=13), ITEM: média 0.1500 (n=9), MOVE_BENCH: média 0.1294 (n=17), MOVE_BOARD: média -0.0088 (n=8), PASS: média 0.0000 (n=7), SELL: média -0.3179 (n=24)
| Jogador 7 | 168 | 65 | 28 | 8 | 0 | 7 | 38 | 0.1648 | 8 | 54 |
- Jogador 7 — ações por estratégia: STABILIZE::BUY: 65, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 22, STABILIZE::MOVE_BENCH: 16, STABILIZE::MOVE_BOARD: 22, STABILIZE::PASS: 7, STABILIZE::SELL: 28
- Jogador 7 — recompensas por ação: BUY: média 0.4618 (n=65), BUY_XP: média -0.0475 (n=8), ITEM: média 0.1059 (n=22), MOVE_BENCH: média 0.2712 (n=16), MOVE_BOARD: média 0.0014 (n=22), PASS: média -0.0057 (n=7), SELL: média -0.3075 (n=28)
| Jogador 8 | 141 | 71 | 35 | 0 | 0 | 4 | 21 | 0.1998 | 5 | 36 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 11, ALL_IN::SELL: 8, STABILIZE::BUY: 60, STABILIZE::ITEM: 10, STABILIZE::MOVE_BENCH: 16, STABILIZE::MOVE_BOARD: 5, STABILIZE::PASS: 4, STABILIZE::SELL: 27
- Jogador 8 — recompensas por ação: BUY: média 0.4213 (n=71), ITEM: média 0.1420 (n=10), MOVE_BENCH: média 0.1588 (n=16), MOVE_BOARD: média -0.0020 (n=5), PASS: média 0.0000 (n=4), SELL: média -0.1626 (n=35)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 14:15:15 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | ? | 14:15:17 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | ? | 14:15:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 14:15:22 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 14:15:23 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 14:15:23 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-1 | 14:15:25 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 14:15:25 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 14:15:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 14:15:28 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 1-2 | 14:15:30 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-2 | 14:15:31 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 14:15:31 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 14:15:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-2 | 14:15:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 14:15:38 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 14:15:39 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 14:15:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 14:15:47 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 14:15:49 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-4 | 14:15:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 14:15:52 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 2-1 | 14:15:59 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 14:15:59 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.1300 |  |
| Jogador 1 | 2-1 | 14:16:00 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 14:16:01 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-1 | 14:16:01 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.2800 |  |
| Jogador 1 | 2-1 | 14:16:02 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 14:16:03 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1700 |  |
| Jogador 1 | 2-1 | 14:16:04 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-2 | 14:16:09 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 1 | 2-2 | 14:16:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 14:16:11 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-2 | 14:16:12 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1800 |  |
| Jogador 1 | 2-2 | 14:16:13 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 1 | 2-2 | 14:16:13 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 14:16:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 14:16:20 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 2-3 | 14:16:25 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3600 |  |
| Jogador 1 | 2-3 | 14:16:26 | MOVE Bench -> Board: Ornn (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.5400 |  |
| Jogador 1 | 2-4 | 14:16:33 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Ornn | 1.0200 |  |
| Jogador 1 | 2-4 | 14:16:33 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_18_Ornn | -0.6300 |  |
| Jogador 1 | 2-4 | 14:16:34 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_18_Ornn | 0.3400 |  |
| Jogador 1 | 2-4 | 14:16:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_18_Ornn | -0.0400 |  |
| Jogador 1 | 2-4 | 14:16:36 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_18_Ornn | -0.4500 |  |
| Jogador 1 | 2-4 | 14:16:37 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Ornn | -1.0200 |  |
| Jogador 1 | 2-4 | 14:16:38 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Ornn | 0.1300 |  |
| Jogador 1 | 2-5 | 14:16:50 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Ornn | 1.0600 |  |
| Jogador 1 | 2-5 | 14:16:51 | MOVE Bench -> Board: Shen (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Ornn | -0.3200 |  |
| Jogador 1 | 2-5 | 14:16:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Ornn | -0.0600 |  |
| Jogador 1 | 2-5 | 14:16:54 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Ornn | -0.4200 |  |
| Jogador 1 | 2-5 | 14:16:55 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Ornn | -0.0900 |  |
| Jogador 1 | 2-5 | 14:16:56 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Ornn | -0.0900 |  |
| Jogador 1 | 2-6 | 14:17:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 2-6 | 14:17:05 | MOVE Bench -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Ornn | -0.4000 |  |
| Jogador 1 | 2-7 | 14:17:20 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Ornn | 0.2600 |  |
| Jogador 1 | 2-7 | 14:17:21 | MOVE Bench -> Board: Shen (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Ornn | 0.0900 |  |
| Jogador 1 | 2-7 | 14:17:22 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-7 | 14:17:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_18_Ornn | -0.0300 |  |
| Jogador 1 | 2-7 | 14:17:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Ornn | -0.1100 |  |
| Jogador 1 | 2-7 | 14:17:25 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_18_Ornn | 0.4000 |  |
| Jogador 1 | 3-1 | 14:17:35 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_18_Ornn | 0.2600 |  |
| Jogador 1 | 3-1 | 14:17:36 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 3-2 | 14:17:53 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_18_Ornn | 0.2700 |  |
| Jogador 1 | 3-2 | 14:17:54 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 3-2 | 14:17:55 | MOVE Board -> Board: Ornn (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_18_Ornn | -0.0200 |  |
| Jogador 1 | 3-2 | 14:17:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_18_Ornn | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-3 | 14:18:09 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Inferno | DA_18_Ornn | -0.0900 |  |
| Jogador 1 | 3-3 | 14:18:10 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Inferno | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 3-4 | 14:18:30 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Inferno | DA_18_Ornn | 0.8000 |  |
| Jogador 1 | 3-4 | 14:18:31 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Inferno | DA_18_Ornn | 0.1500 |  |
| Jogador 1 | 3-4 | 14:18:32 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Inferno | DA_18_Ornn | 0.3900 |  |
| Jogador 1 | 3-4 | 14:18:34 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Inferno | DA_18_Ornn | -0.0400 |  |
| Jogador 1 | 3-4 | 14:18:35 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Inferno | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 3-4 | 14:18:36 | MOVE Board -> Board: Xayah (i:2.0) <-> Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Inferno | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 3-5 | 14:18:47 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Inferno | DA_18_Ornn | 0.8400 |  |
| Jogador 1 | 3-5 | 14:18:48 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Inferno | DA_18_Ornn | 0.3200 |  |
| Jogador 1 | 3-6 | 14:19:10 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Inferno | DA_18_Ornn | 0.0300 |  |
| Jogador 1 | 3-6 | 14:19:12 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Inferno | DA_18_Ornn | -0.0700 |  |
| Jogador 1 | 3-6 | 14:19:13 | MOVE Board -> Board: Ornn (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Inferno | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 3-6 | 14:19:14 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Inferno | DA_18_Ornn | -0.5000 |  |
| Jogador 1 | 3-6 | 14:19:15 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Inferno | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 3-7 | 14:19:27 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Inferno | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 3-7 | 14:19:28 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Inferno | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 3-7 | 14:19:29 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Inferno | DA_18_Ornn | 0.0900 |  |
| Jogador 1 | 4-1 | 14:19:51 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Inferno | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 4-1 | 14:19:52 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Inferno | DA_18_Ornn | 0.9600 |  |
| Jogador 1 | 4-1 | 14:19:53 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 5 | Inferno | DA_18_Ornn | -0.2500 |  |
| Jogador 1 | 4-1 | 14:19:54 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Inferno | DA_18_Ornn | -0.5900 |  |
| Jogador 1 | 4-1 | 14:19:56 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Inferno | DA_18_Ornn | 0.4700 |  |
| Jogador 1 | 4-2 | 14:20:09 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 70 | 5 | Inferno | DA_18_Ornn | 0.8800 |  |
| Jogador 1 | 4-2 | 14:20:10 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Inferno | DA_18_Ornn | 0.3800 |  |
| Jogador 1 | 4-2 | 14:20:11 | EQUIP_FROM_INVENTORY: TFT_Item_RapidFireCannon -> Rakan (i:4.0) (tabuleiro slot 23) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Inferno | DA_18_Ornn | 0.1500 |  |
| Jogador 1 | 4-3 | 14:20:34 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Ornn (i:4.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Inferno | DA_18_Ornn | 0.1700 |  |
| Jogador 1 | 4-3 | 14:20:35 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Ornn (i:4.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Inferno | DA_18_Ornn | 0.1700 |  |
| Jogador 1 | 4-3 | 14:20:36 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 82 | 5 | Inferno | DA_18_Ornn | 0.0100 |  |
| Jogador 1 | 4-3 | 14:20:37 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Inferno | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 4-3 | 14:20:39 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Inferno | DA_18_Ornn | -0.0300 |  |
| Jogador 1 | 4-4 | 14:20:52 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 87 | 5 | Inferno | DA_18_Ornn | -0.1100 |  |
| Jogador 1 | 4-4 | 14:20:53 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Inferno | DA_18_Ornn | -0.1200 |  |
| Jogador 1 | 4-4 | 14:20:55 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Inferno | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 4-5 | 14:21:20 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 98 | 5 | Inferno | DA_18_Ornn | 0.0200 |  |
| Jogador 1 | 4-5 | 14:21:21 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 95 | 5 | Inferno | DA_18_Ornn | 0.8500 |  |
| Jogador 1 | 4-5 | 14:21:23 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 98 | 5 | Inferno | DA_18_Ornn | -0.0300 |  |
| Jogador 1 | 4-5 | 14:21:24 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 95 | 5 | Inferno | DA_18_Ornn | 0.8400 |  |
| Jogador 1 | 4-5 | 14:21:25 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 95 | 5 | Inferno | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 4-6 | 14:21:40 | VENDEU: Malphite (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Inferno | DA_18_Ornn | -0.0200 |  |
| Jogador 1 | 4-6 | 14:21:41 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 108 | 5 | Inferno | DA_18_Ornn | -0.0600 |  |
| Jogador 1 | 4-6 | 14:21:43 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Inferno | DA_18_Ornn | -0.0300 |  |
| Jogador 1 | 4-7 | 14:22:10 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 119 | 5 | Inferno | DA_18_Hecarim | 1.0200 |  |
| Jogador 1 | 4-7 | 14:22:12 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 116 | 5 | Inferno | DA_18_Hecarim | -0.0700 |  |
| Jogador 1 | 4-7 | 14:22:13 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Ornn (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 116 | 5 | Inferno | DA_18_Hecarim | 0.1400 |  |
| Jogador 1 | 4-7 | 14:22:15 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 116 | 5 | Inferno | DA_18_Hecarim | 0.1800 |  |
| Jogador 1 | 4-7 | 14:22:16 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 116 | 5 | Inferno | DA_18_Hecarim | 0.5600 |  |
| Jogador 1 | 5-1 | 14:22:32 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Inferno | DA_18_Hecarim | -0.1700 |  |
| Jogador 1 | 5-1 | 14:22:34 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 127 | 5 | Inferno | DA_18_Hecarim | -0.0100 |  |
| Jogador 1 | 5-1 | 14:22:35 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Inferno | DA_18_Hecarim | -0.1700 |  |
| Jogador 1 | 5-2 | 14:23:04 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 137 | 5 | Inferno | DA_18_Hecarim | -0.0100 |  |
| Jogador 1 | 5-2 | 14:23:05 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 135 | 5 | Inferno | DA_18_Hecarim | 0.9500 |  |
| Jogador 1 | 5-2 | 14:23:07 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 131 | 5 | Inferno | DA_18_Hecarim | 0.3700 |  |
| Jogador 1 | 5-2 | 14:23:09 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 131 | 5 | Inferno | DA_18_Hecarim | 0.5900 |  |
| Jogador 1 | 5-3 | 14:23:25 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 141 | 5 | Inferno | DA_18_Hecarim | 0.9500 |  |
| Jogador 1 | 5-3 | 14:23:26 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 139 | 5 | Inferno | DA_18_Hecarim | 0.3600 |  |
| Jogador 1 | 5-3 | 14:23:28 | VENDEU: Xayah (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 142 | 5 | Inferno | DA_18_Hecarim | -0.5900 |  |
| Jogador 1 | 5-3 | 14:23:29 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 140 | 5 | Inferno | DA_18_Hecarim | 0.6000 |  |
| Jogador 1 | 5-4 | 14:24:02 | COMPROU: Lux (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 145 | 5 | Inferno | DA_18_Hecarim | -0.1800 |  |
| Jogador 1 | 5-4 | 14:24:04 | VENDEU: Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 149 | 5 | Inferno | DA_18_Hecarim | -0.0200 |  |
| Jogador 1 | 5-4 | 14:24:06 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Inferno | DA_18_Hecarim | 0.0400 |  |
| Jogador 1 | 5-4 | 14:24:07 | VENDEU: LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 149 | 5 | Inferno | DA_18_Hecarim | -0.0300 |  |
| Jogador 1 | 5-5 | 14:24:26 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 158 | 5 | Inferno | DA_18_Hecarim | 0.0800 |  |
| Jogador 1 | 5-5 | 14:24:28 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 161 | 5 | Inferno | DA_18_Hecarim | -0.0400 |  |
| Jogador 1 | 5-5 | 14:24:30 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 158 | 5 | Inferno | DA_18_Hecarim | -0.1500 |  |
| Jogador 1 | 5-5 | 14:24:31 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 161 | 5 | Inferno | DA_18_Hecarim | -0.0100 |  |
| Jogador 1 | 5-6 | 14:25:03 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 170 | 5 | Inferno | DA_18_Hecarim | -0.1500 |  |
| Jogador 1 | 5-6 | 14:25:05 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 173 | 5 | Inferno | DA_18_Hecarim | -0.0100 |  |
| Jogador 1 | 5-6 | 14:25:06 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 170 | 5 | Inferno | DA_18_Hecarim | -0.2000 |  |
| Jogador 1 | 5-6 | 14:25:08 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 173 | 5 | Inferno | DA_18_Hecarim | 0.0000 |  |
| Jogador 1 | 5-7 | 14:25:26 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 182 | 5 | Inferno | DA_18_Hecarim | 0.9300 |  |
| Jogador 1 | 5-7 | 14:25:28 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Shen (i:8.0) (tabuleiro slot 24) | FAST8 | FAST8: composição planejada exige nível 8 | 182 | 5 | Inferno | DA_18_Hecarim | 0.0800 |  |
| Jogador 1 | 5-7 | 14:25:29 | VENDEU: Lux (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 187 | 5 | Inferno | DA_18_Hecarim | -0.0100 |  |
| Jogador 1 | 5-7 | 14:25:31 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 184 | 5 | Inferno | DA_18_Hecarim | 1.0000 |  |
| Jogador 1 | 6-1 | 14:26:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 195 | 5 | Inferno | DA_18_Hecarim | 0.4200 |  |
| Jogador 1 | 6-1 | 14:26:06 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 194 | 5 | Inferno | DA_18_Hecarim | 0.3800 |  |
| Jogador 1 | 6-1 | 14:26:08 | VENDEU: Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 195 | 5 | Inferno | DA_18_Hecarim | -0.5400 |  |
| Jogador 1 | 6-1 | 14:26:09 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 192 | 5 | Inferno | DA_18_Hecarim | 0.0500 |  |
| Jogador 1 | 6-2 | 14:26:28 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 208 | 5 | Inferno | DA_18_Hecarim | -0.0300 |  |
| Jogador 1 | 6-2 | 14:26:29 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 204 | 5 | Inferno | DA_18_Hecarim | 0.5800 |  |
| Jogador 1 | 6-2 | 14:26:31 | VENDEU: Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 205 | 5 | Inferno | DA_18_Hecarim | -0.5900 |  |
| Jogador 1 | 6-2 | 14:26:33 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 202 | 5 | Inferno | DA_18_Hecarim | -0.2100 |  |
| Jogador 1 | 6-3 | 14:27:07 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 215 | 5 | Inferno | DA_18_Hecarim | -0.0100 |  |
| Jogador 1 | 6-3 | 14:27:09 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 212 | 5 | Inferno | DA_18_Hecarim | 0.9000 |  |
| Jogador 1 | 6-3 | 14:27:11 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 213 | 5 | Inferno | DA_18_Hecarim | -0.5900 |  |
| Jogador 1 | 6-3 | 14:27:12 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 210 | 5 | Inferno | DA_18_Hecarim | 1.0700 |  |
| Jogador 1 | 6-4 | 14:27:32 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 216 | 5 | Inferno | DA_18_Hecarim | 0.1500 |  |
| Jogador 1 | 6-4 | 14:27:34 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 212 | 5 | Inferno | DA_18_Hecarim | -0.1200 |  |
| Jogador 1 | 6-4 | 14:27:35 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 220 | 5 | Inferno | DA_18_Hecarim | -0.5900 |  |
| Jogador 1 | 6-4 | 14:27:37 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 218 | 5 | Inferno | DA_18_Hecarim | 0.0600 |  |
| Jogador 1 | 6-5 | 14:28:14 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 231 | 5 | Inferno | DA_18_Hecarim | -0.0200 |  |
| Jogador 1 | 6-5 | 14:28:16 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 230 | 5 | Inferno | DA_18_Hecarim | 0.5200 |  |
| Jogador 1 | 6-5 | 14:28:17 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 234 | 5 | Inferno | DA_18_Hecarim | -0.0200 |  |
| Jogador 1 | 6-5 | 14:28:19 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 231 | 5 | Inferno | DA_18_Hecarim | 0.4500 |  |
| Jogador 2 | ? | 14:15:15 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | ? | 14:15:17 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | ? | 14:15:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 14:15:22 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 14:15:23 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 14:15:23 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 1-1 | 14:15:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 14:15:28 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 1-2 | 14:15:30 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 14:15:31 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 14:15:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 14:15:35 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 14:15:38 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 14:15:39 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 14:15:39 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-3 | 14:15:40 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-3 | 14:15:41 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 14:15:41 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 14:15:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 14:15:47 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 14:15:49 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 1-4 | 14:15:50 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 1-4 | 14:15:51 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 1-4 | 14:15:51 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-4 | 14:15:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-1 | 14:15:59 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 2-1 | 14:15:59 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 2-1 | 14:16:00 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-1 | 14:16:01 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 2-1 | 14:16:01 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-1 | 14:16:02 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 14:16:03 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-1 | 14:16:04 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-2 | 14:16:09 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-2 | 14:16:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-2 | 14:16:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 14:16:14 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 2-3 | 14:16:20 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.9700 |  |
| Jogador 2 | 2-3 | 14:16:25 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.3300 |  |
| Jogador 2 | 2-3 | 14:16:26 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-4 | 14:16:33 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.3200 |  |
| Jogador 2 | 2-4 | 14:16:33 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 2-4 | 14:16:34 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 2-4 | 14:16:35 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 2-4 | 14:16:36 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-4 | 14:16:37 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-4 | 14:16:38 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-5 | 14:16:50 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 2-5 | 14:16:51 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_Veigar | -0.3700 |  |
| Jogador 2 | 2-5 | 14:16:53 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Feérico | DA_18_Veigar | -0.4200 |  |
| Jogador 2 | 2-5 | 14:16:54 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-5 | 14:16:55 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Feérico | DA_18_Veigar | -0.3700 |  |
| Jogador 2 | 2-5 | 14:16:56 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-6 | 14:17:04 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Veigar | 0.9600 |  |
| Jogador 2 | 2-6 | 14:17:05 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-7 | 14:17:20 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Feérico | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 2-7 | 14:17:21 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-7 | 14:17:22 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Feérico | DA_18_Veigar | -0.3100 |  |
| Jogador 2 | 2-7 | 14:17:23 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Feérico | DA_18_Veigar | -0.5700 |  |
| Jogador 2 | 2-7 | 14:17:25 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Feérico | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 2-7 | 14:17:25 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Feérico | DA_18_Veigar | -1.0200 |  |
| Jogador 2 | 3-1 | 14:17:35 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Feérico | DA_18_Veigar | 0.9100 |  |
| Jogador 2 | 3-1 | 14:17:36 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Feérico | DA_18_Veigar | 0.8400 |  |
| Jogador 2 | 3-2 | 14:17:53 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 3-2 | 14:17:54 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Feérico | DA_18_Veigar | -0.3300 |  |
| Jogador 2 | 3-2 | 14:17:55 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Feérico | DA_18_Veigar | -0.5500 |  |
| Jogador 2 | 3-2 | 14:17:56 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Feérico | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 3-2 | 14:17:57 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-2 | 14:17:58 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Feérico | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 3-3 | 14:18:09 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 3-3 | 14:18:10 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-4 | 14:18:30 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Feérico | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 3-4 | 14:18:31 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Feérico | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 3-4 | 14:18:32 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Feérico | DA_18_Veigar | -0.3700 |  |
| Jogador 2 | 3-4 | 14:18:34 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Feérico | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 3-4 | 14:18:35 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 71 | 5 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-4 | 14:18:36 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 71 | 5 | Feérico | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 3-5 | 14:18:47 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 82 | 5 | Feérico | DA_18_Veigar | 0.4500 |  |
| Jogador 2 | 3-5 | 14:18:48 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 79 | 5 | Feérico | DA_18_Veigar | 0.4400 |  |
| Jogador 2 | 3-6 | 14:19:10 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 86 | 5 | Feérico | DA_18_Veigar | 0.4200 |  |
| Jogador 2 | 3-6 | 14:19:12 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 83 | 5 | Feérico | DA_18_Veigar | -0.2100 |  |
| Jogador 2 | 3-6 | 14:19:13 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 80 | 5 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 3-6 | 14:19:14 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 78 | 5 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 3-6 | 14:19:15 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 76 | 5 | Feérico | DA_18_Veigar | -0.1300 |  |
| Jogador 2 | 3-7 | 14:19:27 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Kobuko (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Feérico | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 3-7 | 14:19:28 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Feérico | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 3-7 | 14:19:29 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-1 | 14:19:51 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Feérico | DA_18_Veigar | 0.9000 |  |
| Jogador 2 | 4-1 | 14:19:52 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-1 | 14:19:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Feérico | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 4-1 | 14:19:54 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-1 | 14:19:56 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Feérico | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 4-2 | 14:20:09 | VENDEU: Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-2 | 14:20:10 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Feérico | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 4-2 | 14:20:11 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-3 | 14:20:34 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Feérico | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 4-3 | 14:20:35 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Feérico | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 4-3 | 14:20:36 | MOVE Bench -> Board: Tristana (i:6.0) <-> Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Feérico | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 4-3 | 14:20:37 | VENDEU: Rek'Sai (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Feérico | DA_18_Veigar | -0.7100 |  |
| Jogador 2 | 4-3 | 14:20:39 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 4-4 | 14:20:52 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Feérico | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 4-4 | 14:20:53 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Feérico | DA_18_Veigar | 1.0600 |  |
| Jogador 2 | 4-4 | 14:20:55 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Feérico | DA_18_Veigar | 0.0200 |  |
| Jogador 3 | ? | 14:15:15 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | ? | 14:15:17 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | ? | 14:15:18 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | ? | 14:15:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 14:15:22 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 14:15:23 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 14:15:23 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-1 | 14:15:25 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 1-1 | 14:15:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 14:15:28 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-2 | 14:15:30 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 14:15:31 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 14:15:31 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 14:15:32 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-2 | 14:15:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 14:15:35 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 1-3 | 14:15:38 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 14:15:39 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 14:15:39 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 14:15:40 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 14:15:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 14:15:47 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 14:15:49 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 14:15:50 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 14:15:51 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 1-4 | 14:15:51 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-4 | 14:15:52 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-1 | 14:15:59 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-1 | 14:15:59 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 14:16:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 14:16:09 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-2 | 14:16:10 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 2-2 | 14:16:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-2 | 14:16:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 14:16:20 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-3 | 14:16:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 2-3 | 14:16:26 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 2-4 | 14:16:33 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 2-4 | 14:16:33 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-4 | 14:16:34 | MOVE Bench -> Board: Diana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.7100 |  |
| Jogador 3 | 2-4 | 14:16:35 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.4700 |  |
| Jogador 3 | 2-4 | 14:16:36 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-4 | 14:16:37 | MOVE Bench -> Board: Akali (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 2-4 | 14:16:38 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 2-5 | 14:16:50 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 14:16:51 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-5 | 14:16:53 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.6300 |  |
| Jogador 3 | 2-5 | 14:16:54 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 14:16:55 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 14:16:56 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 2-6 | 14:17:04 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Akali_AD | 0.8200 |  |
| Jogador 3 | 2-6 | 14:17:05 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | -0.5000 |  |
| Jogador 3 | 2-7 | 14:17:20 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | 0.8400 |  |
| Jogador 3 | 2-7 | 14:17:21 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 2-7 | 14:17:22 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | 0.4300 |  |
| Jogador 3 | 2-7 | 14:17:23 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-7 | 14:17:25 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 2-7 | 14:17:25 | MOVE Board -> Board: Diana (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-1 | 14:17:35 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Devastador | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 3-1 | 14:17:36 | MOVE Board -> Board: Yorick (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-2 | 14:17:53 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Akali_AD | -0.4200 |  |
| Jogador 3 | 3-2 | 14:17:54 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Devastador | DA_18_Akali_AD | 0.3000 |  |
| Jogador 3 | 3-2 | 14:17:55 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-2 | 14:17:56 | MOVE Bench -> Board: Vi (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Devastador | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 3-2 | 14:17:57 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-2 | 14:17:58 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Devastador | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 3-3 | 14:18:09 | MOVE Bench -> Board: Sivir (i:8.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Devastador | DA_18_Akali_AD | -0.7200 |  |
| Jogador 3 | 3-3 | 14:18:10 | MOVE Bench -> Board: Akali (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Devastador | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 3-4 | 14:18:30 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Devastador | DA_18_Akali_AD | 0.5800 |  |
| Jogador 3 | 3-4 | 14:18:31 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Devastador | DA_18_Akali_AD | 0.5100 |  |
| Jogador 3 | 3-4 | 14:18:32 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 14:18:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Devastador | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 3-4 | 14:18:35 | MOVE Board -> Board: Diana (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 14:18:36 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-5 | 14:18:47 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Devastador | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 3-5 | 14:18:48 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Devastador | DA_18_Akali_AD | 0.8400 |  |
| Jogador 3 | 3-6 | 14:19:10 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Devastador | DA_18_Akali_AD | -0.2300 |  |
| Jogador 3 | 3-6 | 14:19:12 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Devastador | DA_18_Akali_AD | 0.7300 |  |
| Jogador 3 | 3-6 | 14:19:13 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Devastador | DA_18_Akali_AD | 0.4300 |  |
| Jogador 3 | 3-6 | 14:19:14 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 3-6 | 14:19:15 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 5 | Devastador | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 3-7 | 14:19:27 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Devastador | DA_18_Akali_AD | 0.1800 |  |
| Jogador 3 | 3-7 | 14:19:28 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Devastador | DA_18_Akali_AD | 0.1200 |  |
| Jogador 3 | 3-7 | 14:19:29 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Devastador | DA_18_Akali_AD | -0.1200 |  |
| Jogador 3 | 4-1 | 14:19:51 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Devastador | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 4-1 | 14:19:52 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 14:19:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Devastador | DA_18_Akali_AD | 0.8600 |  |
| Jogador 3 | 4-1 | 14:19:54 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 87 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 14:19:56 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 4-2 | 14:20:09 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-2 | 14:20:10 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Devastador | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 4-2 | 14:20:11 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-3 | 14:20:34 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 108 | 5 | Devastador | DA_18_Akali_AD | -0.2500 |  |
| Jogador 3 | 4-3 | 14:20:35 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 14:20:36 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 109 | 5 | Devastador | DA_18_Akali_AD | -0.2800 |  |
| Jogador 3 | 4-3 | 14:20:37 | MOVE Board -> Board: Camille (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 109 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 14:20:39 | MOVE Board -> Board: Akali (i:4.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 109 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 14:20:52 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 122 | 5 | Devastador | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-4 | 14:20:53 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 120 | 5 | Devastador | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 4-4 | 14:20:55 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 122 | 5 | Devastador | DA_18_Akali_AD | -0.5000 |  |
| Jogador 3 | 4-5 | 14:21:20 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 133 | 5 | Devastador | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 4-5 | 14:21:21 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 135 | 5 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-5 | 14:21:23 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 133 | 5 | Devastador | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 4-5 | 14:21:24 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 135 | 5 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-5 | 14:21:25 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 132 | 5 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 4-6 | 14:21:40 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 145 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-6 | 14:21:41 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 143 | 5 | Devastador | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 4-6 | 14:21:43 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 141 | 5 | Devastador | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 4-7 | 14:22:10 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Camille (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 151 | 5 | Devastador | DA_18_Akali_AD | 0.1800 |  |
| Jogador 3 | 4-7 | 14:22:12 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Yorick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 151 | 5 | Devastador | DA_18_Akali_AD | 0.1200 |  |
| Jogador 3 | 4-7 | 14:22:13 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 149 | 5 | Devastador | DA_18_Akali_AD | -0.0800 |  |
| Jogador 3 | 4-7 | 14:22:15 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 148 | 5 | Devastador | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 4-7 | 14:22:16 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 147 | 5 | Devastador | DA_18_Akali_AD | -0.2700 |  |
| Jogador 3 | 5-1 | 14:22:32 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 163 | 5 | Devastador | DA_18_Akali_AD | -0.6000 |  |
| Jogador 3 | 5-1 | 14:22:34 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 162 | 5 | Devastador | DA_18_Akali_AD | 0.9100 |  |
| Jogador 3 | 5-1 | 14:22:35 | VENDEU: Lobo Trevoguari (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 167 | 5 | Devastador | DA_18_Akali_AD | -0.6000 |  |
| Jogador 3 | 5-2 | 14:23:04 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 175 | 5 | Devastador | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 5-2 | 14:23:05 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 176 | 5 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 5-2 | 14:23:07 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 173 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 5-2 | 14:23:09 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 175 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 5-3 | 14:23:25 | COMPROU: Camille (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 184 | 5 | Devastador | DA_18_Akali_AD | 1.0500 |  |
| Jogador 3 | 5-3 | 14:23:26 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 182 | 5 | Devastador | DA_18_Akali_AD | 0.4300 |  |
| Jogador 3 | 5-3 | 14:23:28 | VENDEU: Camille (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 185 | 5 | Devastador | DA_18_Akali_AD | -0.7100 |  |
| Jogador 3 | 5-3 | 14:23:29 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Akali (i:2.0) (tabuleiro slot 21) | ALL_IN | HP crítico: gastar para sobreviver | 185 | 5 | Devastador | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 5-4 | 14:24:02 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 192 | 5 | Devastador | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | 5-4 | 14:24:04 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Devastador | DA_18_Akali_AD | -0.1900 |  |
| Jogador 3 | 5-4 | 14:24:06 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 191 | 5 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 5-4 | 14:24:07 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 189 | 5 | Devastador | DA_18_Akali_AD | -0.2700 |  |
| Jogador 4 | ? | 14:15:15 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | ? | 14:15:17 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | ? | 14:15:18 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | ? | 14:15:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 14:15:22 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 14:15:23 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 14:15:23 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-1 | 14:15:25 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 1-1 | 14:15:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 14:15:28 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4600 |  |
| Jogador 4 | 1-2 | 14:15:30 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 14:15:31 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 14:15:31 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 14:15:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-2 | 14:15:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 14:15:38 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 14:15:39 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 14:15:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 14:15:47 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 4 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-4 | 14:15:49 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 1-4 | 14:15:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 14:15:52 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3900 |  |
| Jogador 4 | 2-1 | 14:15:59 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 2-1 | 14:15:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 2-1 | 14:16:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-1 | 14:16:04 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4300 |  |
| Jogador 4 | 2-2 | 14:16:09 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 4 | 2-2 | 14:16:10 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-2 | 14:16:11 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-2 | 14:16:12 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-2 | 14:16:13 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 14:16:13 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 14:16:14 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 14:16:14 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 4 | 2-3 | 14:16:20 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-3 | 14:16:25 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 2-3 | 14:16:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-4 | 14:16:33 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3500 |  |
| Jogador 4 | 2-4 | 14:16:33 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | -0.5700 |  |
| Jogador 4 | 2-4 | 14:16:34 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 4 | 2-4 | 14:16:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-4 | 14:16:36 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.6200 |  |
| Jogador 4 | 2-4 | 14:16:37 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_18_Akali_AD | -0.6300 |  |
| Jogador 4 | 2-4 | 14:16:38 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-5 | 14:16:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Florescer | DA_18_Akali_AD | 1.0500 |  |
| Jogador 4 | 2-5 | 14:16:51 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_18_Akali_AD | 0.3200 |  |
| Jogador 4 | 2-5 | 14:16:53 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Florescer | DA_18_Akali_AD | -0.5000 |  |
| Jogador 4 | 2-5 | 14:16:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_18_Akali_AD | -0.1400 |  |
| Jogador 4 | 2-5 | 14:16:55 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_18_Akali_AD | -1.0200 |  |
| Jogador 4 | 2-5 | 14:16:56 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-6 | 14:17:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Rakan | 1.1200 |  |
| Jogador 4 | 2-6 | 14:17:05 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Rakan | 0.2800 |  |
| Jogador 4 | 2-7 | 14:17:20 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | 2-7 | 14:17:21 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Rakan | 0.0100 |  |
| Jogador 4 | 2-7 | 14:17:22 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | 2-7 | 14:17:23 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Rakan | 0.4200 |  |
| Jogador 4 | 2-7 | 14:17:25 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 4 | 2-7 | 14:17:25 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_18_Rakan | 0.0200 |  |
| Jogador 4 | 3-1 | 14:17:35 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Rakan | 0.8400 |  |
| Jogador 4 | 3-1 | 14:17:36 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | 3-2 | 14:17:53 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Rakan | 0.8700 |  |
| Jogador 4 | 3-2 | 14:17:54 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Rakan | 0.5800 |  |
| Jogador 4 | 3-2 | 14:17:55 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Rakan | 0.2100 |  |
| Jogador 4 | 3-2 | 14:17:56 | MOVE Bench -> Board: Yorick (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Rakan | 0.1100 |  |
| Jogador 4 | 3-2 | 14:17:57 | MOVE Bench -> Board: Rakan (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Rakan | 0.0800 |  |
| Jogador 4 | 3-2 | 14:17:58 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Rakan | 0.1500 |  |
| Jogador 4 | 3-3 | 14:18:09 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_18_Rakan | 0.6900 |  |
| Jogador 4 | 3-3 | 14:18:10 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Rakan | 0.3000 |  |
| Jogador 4 | 3-4 | 14:18:30 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Colosso | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | 3-4 | 14:18:31 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Colosso | DA_18_Rakan | 0.5700 |  |
| Jogador 4 | 3-4 | 14:18:32 | MOVE Board -> Board: Yorick (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 3-4 | 14:18:34 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 2 | Colosso | DA_18_Rakan | -0.0900 |  |
| Jogador 4 | 3-4 | 14:18:35 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 2 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 3-4 | 14:18:36 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 2 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 3-5 | 14:18:47 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Colosso | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 3-5 | 14:18:48 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_18_Rakan | 0.0300 |  |
| Jogador 4 | 3-6 | 14:19:10 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_18_Rakan | 0.7200 |  |
| Jogador 4 | 3-6 | 14:19:12 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Colosso | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 3-6 | 14:19:13 | MOVE Board -> Board: Yorick (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 3-6 | 14:19:14 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Colosso | DA_18_Rakan | -0.1100 |  |
| Jogador 4 | 3-6 | 14:19:15 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Colosso | DA_18_Rakan | 0.4600 |  |
| Jogador 4 | 3-7 | 14:19:27 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Rakan | 0.2000 |  |
| Jogador 4 | 3-7 | 14:19:28 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Rakan | 0.2300 |  |
| Jogador 4 | 3-7 | 14:19:29 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_18_Rakan | 0.8900 |  |
| Jogador 4 | 4-1 | 14:19:51 | VENDEU: Master Yi (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 4 | Colosso | DA_18_Rakan | -0.1300 |  |
| Jogador 4 | 4-1 | 14:19:52 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Colosso | DA_18_Rakan | 0.3200 |  |
| Jogador 4 | 4-1 | 14:19:53 | MOVE Board -> Board: Sejuani (i:4.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 4-1 | 14:19:54 | MOVE Board -> Board: Yorick (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 4-1 | 14:19:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Colosso | DA_18_Rakan | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-2 | 14:20:09 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Colosso | DA_18_Rakan | -0.5900 |  |
| Jogador 4 | 4-2 | 14:20:10 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Colosso | DA_18_Rakan | 0.8800 |  |
| Jogador 4 | 4-2 | 14:20:11 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Colosso | DA_18_Rakan | 0.0100 |  |
| Jogador 4 | 4-3 | 14:20:34 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Colosso | DA_18_Rakan | -0.6700 |  |
| Jogador 4 | 4-3 | 14:20:35 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 4 | 4-3 | 14:20:36 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 4-3 | 14:20:37 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 4 | 4-3 | 14:20:39 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 4-4 | 14:20:52 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Colosso | DA_18_Rakan | 0.8600 |  |
| Jogador 4 | 4-4 | 14:20:53 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Colosso | DA_18_Rakan | -0.5200 |  |
| Jogador 4 | 4-4 | 14:20:55 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 4-5 | 14:21:20 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 4-5 | 14:21:21 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Colosso | DA_18_Rakan | 0.2300 |  |
| Jogador 4 | 4-5 | 14:21:23 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 4-5 | 14:21:24 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Colosso | DA_18_Rakan | -0.2400 |  |
| Jogador 4 | 4-5 | 14:21:25 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Colosso | DA_18_Rakan | -0.0700 |  |
| Jogador 4 | 4-6 | 14:21:40 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 4-6 | 14:21:41 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Colosso | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 4-6 | 14:21:43 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Colosso | DA_18_Rakan | -0.0700 |  |
| Jogador 4 | 4-7 | 14:22:10 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Colosso | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | 4-7 | 14:22:12 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_TearOfTheGoddess -> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Colosso | DA_18_Rakan | 0.1900 |  |
| Jogador 4 | 4-7 | 14:22:13 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Colosso | DA_18_Rakan | -0.7300 |  |
| Jogador 4 | 4-7 | 14:22:15 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 4-7 | 14:22:16 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Colosso | DA_18_Rakan | 0.5800 |  |
| Jogador 4 | 5-1 | 14:22:32 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Colosso | DA_18_Rakan | 0.9000 |  |
| Jogador 4 | 5-1 | 14:22:34 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 5-1 | 14:22:35 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Colosso | DA_18_Rakan | -0.0700 |  |
| Jogador 5 | ? | 14:15:15 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | ? | 14:15:17 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 5 | ? | 14:15:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 14:15:22 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 14:15:23 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 14:15:23 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-1 | 14:15:25 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 14:15:25 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 14:15:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 14:15:28 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4300 |  |
| Jogador 5 | 1-2 | 14:15:30 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 1-2 | 14:15:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 14:15:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 14:15:39 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 14:15:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 14:15:47 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 5 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 5 | 1-4 | 14:15:49 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 5 | 1-4 | 14:15:50 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 14:15:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 14:15:59 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-1 | 14:15:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 14:16:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 14:16:09 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 5 | 2-2 | 14:16:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 2-2 | 14:16:11 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 5 | 2-2 | 14:16:12 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 14:16:13 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 5 | 2-2 | 14:16:13 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 14:16:14 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0300 |  |
| Jogador 5 | 2-2 | 14:16:14 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-3 | 14:16:20 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 2-3 | 14:16:25 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-3 | 14:16:26 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-4 | 14:16:33 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.2700 |  |
| Jogador 5 | 2-4 | 14:16:33 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.2500 |  |
| Jogador 5 | 2-4 | 14:16:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 14:16:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 14:16:36 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 14:16:37 | MOVE Bench -> Board: Rammus (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.3200 |  |
| Jogador 5 | 2-4 | 14:16:38 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0500 |  |
| Jogador 5 | 2-5 | 14:16:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.1900 |  |
| Jogador 5 | 2-5 | 14:16:51 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.7000 |  |
| Jogador 5 | 2-5 | 14:16:53 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-5 | 14:16:54 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.8100 |  |
| Jogador 5 | 2-5 | 14:16:55 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-5 | 14:16:56 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.6300 |  |
| Jogador 5 | 2-6 | 14:17:04 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_18_Cassiopeia | 1.1200 |  |
| Jogador 5 | 2-6 | 14:17:05 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Cassiopeia | 1.0200 |  |
| Jogador 5 | 2-7 | 14:17:20 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Enfeitiçador | DA_18_Cassiopeia | 0.0900 |  |
| Jogador 5 | 2-7 | 14:17:21 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Enfeitiçador | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-7 | 14:17:22 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Enfeitiçador | DA_18_Cassiopeia | 0.1400 |  |
| Jogador 5 | 2-7 | 14:17:23 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Enfeitiçador | DA_18_Cassiopeia | -0.3700 |  |
| Jogador 5 | 2-7 | 14:17:25 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Enfeitiçador | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 2-7 | 14:17:25 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 2 | Enfeitiçador | DA_18_Cassiopeia | 0.4000 |  |
| Jogador 5 | 3-1 | 14:17:35 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Enfeitiçador | DA_18_Cassiopeia | 0.7400 |  |
| Jogador 5 | 3-1 | 14:17:36 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Cassiopeia | 0.4200 |  |
| Jogador 5 | 3-2 | 14:17:53 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_18_Cassiopeia | 0.8300 |  |
| Jogador 5 | 3-2 | 14:17:54 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Enfeitiçador | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 3-2 | 14:17:55 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Yunara | 0.6200 |  |
| Jogador 5 | 3-2 | 14:17:56 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 3-2 | 14:17:57 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_Tristana | -0.0600 |  |
| Jogador 5 | 3-2 | 14:17:58 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Enfeitiçador | DA_18_Tristana | -0.1700 |  |
| Jogador 5 | 3-3 | 14:18:09 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_18_Tristana | 0.3100 |  |
| Jogador 5 | 3-3 | 14:18:10 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Enfeitiçador | DA_18_Tristana | 0.8500 |  |
| Jogador 5 | 3-4 | 14:18:30 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Tristana | 0.3300 |  |
| Jogador 5 | 3-4 | 14:18:31 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Enfeitiçador | DA_18_Tristana | -0.1500 |  |
| Jogador 5 | 3-4 | 14:18:32 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Tristana | 0.0500 |  |
| Jogador 5 | 3-4 | 14:18:34 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Enfeitiçador | DA_18_Tristana | -0.1800 |  |
| Jogador 5 | 3-4 | 14:18:35 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Tristana | 0.0800 |  |
| Jogador 5 | 3-4 | 14:18:36 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Enfeitiçador | DA_18_Tristana | -0.6400 |  |
| Jogador 5 | 3-5 | 14:18:47 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Enfeitiçador | DA_18_Tristana | 0.1300 |  |
| Jogador 5 | 3-5 | 14:18:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_18_Tristana | 0.1700 |  |
| Jogador 5 | 3-6 | 14:19:10 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 71 | 5 | Enfeitiçador | DA_18_Tristana | -0.0500 |  |
| Jogador 5 | 3-6 | 14:19:12 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Enfeitiçador | DA_18_Tristana | 0.8400 |  |
| Jogador 5 | 3-6 | 14:19:13 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 71 | 5 | Enfeitiçador | DA_18_Tristana | -0.0400 |  |
| Jogador 5 | 3-6 | 14:19:14 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 3-6 | 14:19:15 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 71 | 5 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-7 | 14:19:27 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Enfeitiçador | DA_18_Tristana | 0.3900 |  |
| Jogador 5 | 3-7 | 14:19:28 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Enfeitiçador | DA_18_Tristana | 0.2000 |  |
| Jogador 5 | 3-7 | 14:19:29 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Enfeitiçador | DA_18_Tristana | 0.1900 |  |
| Jogador 5 | 4-1 | 14:19:51 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Enfeitiçador | DA_18_Tristana | -0.1000 |  |
| Jogador 5 | 4-1 | 14:19:52 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 92 | 5 | Enfeitiçador | DA_18_Tristana | 0.3600 |  |
| Jogador 5 | 4-1 | 14:19:53 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Enfeitiçador | DA_18_Tristana | -0.5900 |  |
| Jogador 5 | 4-1 | 14:19:54 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 89 | 5 | Enfeitiçador | DA_18_Tristana | -0.1500 |  |
| Jogador 5 | 4-1 | 14:19:56 | MOVE Bench -> Board: Karma (i:2.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 89 | 5 | Enfeitiçador | DA_18_Tristana | 0.0500 |  |
| Jogador 5 | 4-2 | 14:20:09 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 104 | 5 | Enfeitiçador | DA_18_Tristana | -0.5400 |  |
| Jogador 5 | 4-2 | 14:20:10 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 101 | 5 | Enfeitiçador | DA_18_Tristana | 0.1300 |  |
| Jogador 5 | 4-2 | 14:20:11 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 101 | 5 | Enfeitiçador | DA_18_Tristana | -0.7300 |  |
| Jogador 5 | 4-3 | 14:20:34 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 114 | 5 | Enfeitiçador | DA_18_Tristana | -0.5900 |  |
| Jogador 5 | 4-3 | 14:20:35 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Enfeitiçador | DA_18_Tristana | 0.3400 |  |
| Jogador 5 | 4-3 | 14:20:36 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Rammus (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Enfeitiçador | DA_18_Tristana | 0.1300 |  |
| Jogador 5 | 4-3 | 14:20:37 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Rammus (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Enfeitiçador | DA_18_Tristana | 0.1300 |  |
| Jogador 5 | 4-3 | 14:20:39 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 116 | 5 | Enfeitiçador | DA_18_Tristana | -0.0700 |  |
| Jogador 5 | 4-4 | 14:20:52 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 125 | 5 | Enfeitiçador | DA_18_Tristana | 0.9600 |  |
| Jogador 5 | 4-4 | 14:20:53 | MOVE Bench -> Board: Soraka (i:8.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 125 | 5 | Enfeitiçador | DA_18_Tristana | 0.4400 |  |
| Jogador 5 | 4-4 | 14:20:55 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 124 | 5 | Enfeitiçador | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 4-5 | 14:21:20 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 132 | 5 | Enfeitiçador | DA_18_Tristana | 0.9200 |  |
| Jogador 5 | 4-5 | 14:21:21 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 135 | 5 | Enfeitiçador | DA_18_Tristana | -0.5900 |  |
| Jogador 5 | 4-5 | 14:21:23 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 134 | 5 | Enfeitiçador | DA_18_Tristana | 0.3100 |  |
| Jogador 5 | 4-5 | 14:21:24 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 135 | 5 | Enfeitiçador | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 4-5 | 14:21:25 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 132 | 5 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 4-6 | 14:21:40 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 144 | 5 | Enfeitiçador | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 4-6 | 14:21:41 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 140 | 5 | Enfeitiçador | DA_18_Tristana | 0.0700 |  |
| Jogador 5 | 4-6 | 14:21:43 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 143 | 5 | Enfeitiçador | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 4-7 | 14:22:10 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 151 | 5 | Enfeitiçador | DA_18_Tristana | 0.0600 |  |
| Jogador 5 | 4-7 | 14:22:12 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NeedlesslyLargeRod -> Rammus (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 151 | 5 | Enfeitiçador | DA_18_Tristana | 0.0700 |  |
| Jogador 5 | 4-7 | 14:22:13 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Soraka (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 151 | 5 | Enfeitiçador | DA_18_Tristana | 0.1100 |  |
| Jogador 5 | 4-7 | 14:22:15 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 154 | 5 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 4-7 | 14:22:16 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 152 | 5 | Enfeitiçador | DA_18_Tristana | 0.0300 |  |
| Jogador 5 | 5-1 | 14:22:32 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 165 | 5 | Enfeitiçador | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 5-1 | 14:22:34 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 164 | 5 | Enfeitiçador | DA_18_Tristana | 0.7300 |  |
| Jogador 5 | 5-1 | 14:22:35 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 165 | 5 | Enfeitiçador | DA_18_Tristana | -0.5100 |  |
| Jogador 5 | 5-2 | 14:23:04 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 173 | 5 | Enfeitiçador | DA_18_Tristana | 1.0200 |  |
| Jogador 5 | 5-2 | 14:23:05 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 171 | 5 | Enfeitiçador | DA_18_Tristana | 0.1400 |  |
| Jogador 5 | 5-2 | 14:23:07 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 169 | 5 | Enfeitiçador | DA_18_Tristana | 0.0300 |  |
| Jogador 5 | 5-2 | 14:23:09 | REROLL | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 167 | 5 | Enfeitiçador | DA_18_Tristana | -0.1600 |  |
| Jogador 5 | 5-3 | 14:23:25 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 184 | 5 | Enfeitiçador | DA_18_Tristana | -0.6000 |  |
| Jogador 5 | 5-3 | 14:23:26 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 180 | 5 | Enfeitiçador | DA_18_Tristana | 0.4100 |  |
| Jogador 5 | 5-3 | 14:23:28 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 182 | 5 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 5-3 | 14:23:29 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 179 | 5 | Enfeitiçador | DA_18_Tristana | 0.0600 |  |
| Jogador 5 | 5-4 | 14:24:02 | MOVE Bench -> Board: Ahri (i:8.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 190 | 5 | Enfeitiçador | DA_18_Tristana | 0.5300 |  |
| Jogador 5 | 5-4 | 14:24:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 189 | 5 | Enfeitiçador | DA_18_Tristana | 0.1900 |  |
| Jogador 5 | 5-4 | 14:24:06 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 190 | 5 | Enfeitiçador | DA_18_Tristana | -0.0500 |  |
| Jogador 5 | 5-4 | 14:24:07 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 188 | 5 | Enfeitiçador | DA_18_Tristana | 0.1400 |  |
| Jogador 5 | 5-5 | 14:24:26 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Enfeitiçador | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 5-5 | 14:24:28 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 199 | 5 | Enfeitiçador | DA_18_Tristana | 0.8400 |  |
| Jogador 5 | 5-5 | 14:24:30 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 201 | 5 | Enfeitiçador | DA_18_Tristana | -0.0400 |  |
| Jogador 5 | 5-5 | 14:24:31 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 198 | 5 | Enfeitiçador | DA_18_Tristana | 0.5300 |  |
| Jogador 5 | 5-6 | 14:25:03 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 212 | 5 | Enfeitiçador | DA_18_Tristana | -0.5800 |  |
| Jogador 5 | 5-6 | 14:25:05 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Enfeitiçador | DA_18_Tristana | 0.4000 |  |
| Jogador 5 | 5-6 | 14:25:06 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 212 | 5 | Enfeitiçador | DA_18_Tristana | -0.1100 |  |
| Jogador 5 | 5-6 | 14:25:08 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 208 | 5 | Enfeitiçador | DA_18_Tristana | 0.0800 |  |
| Jogador 5 | 5-7 | 14:25:26 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Soraka (i:8.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 219 | 5 | Enfeitiçador | DA_18_Tristana | 0.1000 |  |
| Jogador 5 | 5-7 | 14:25:28 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 222 | 5 | Enfeitiçador | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 5-7 | 14:25:29 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 218 | 5 | Enfeitiçador | DA_18_Tristana | 0.8000 |  |
| Jogador 5 | 5-7 | 14:25:31 | VENDEU: Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 222 | 5 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 6-1 | 14:26:04 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 230 | 5 | Enfeitiçador | DA_18_Tristana | 0.2800 |  |
| Jogador 5 | 6-1 | 14:26:06 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 233 | 5 | Enfeitiçador | DA_18_Tristana | -0.0700 |  |
| Jogador 5 | 6-1 | 14:26:08 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 229 | 5 | Enfeitiçador | DA_18_Tristana | 0.1800 |  |
| Jogador 5 | 6-1 | 14:26:09 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 233 | 5 | Enfeitiçador | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | ? | 14:15:15 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 14:15:17 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | -0.1500 |  |
| Jogador 6 | ? | 14:15:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 14:15:22 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 14:15:23 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 14:15:23 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 14:15:28 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2200 |  |
| Jogador 6 | 1-2 | 14:15:30 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 6 | 1-2 | 14:15:31 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 6 | 1-2 | 14:15:31 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 14:15:32 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 14:15:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-2 | 14:15:35 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.5700 |  |
| Jogador 6 | 1-3 | 14:15:38 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0300 |  |
| Jogador 6 | 1-3 | 14:15:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 14:15:47 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 6 | 1-4 | 14:15:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 6 | 1-4 | 14:15:49 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 6 | 1-4 | 14:15:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 14:15:52 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0900 |  |
| Jogador 6 | 2-1 | 14:15:59 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-1 | 14:15:59 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-1 | 14:16:00 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-1 | 14:16:01 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-1 | 14:16:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 14:16:09 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-2 | 14:16:10 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-2 | 14:16:11 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-2 | 14:16:12 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-2 | 14:16:13 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 14:16:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 14:16:20 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-3 | 14:16:25 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-3 | 14:16:26 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.4100 |  |
| Jogador 6 | 2-4 | 14:16:33 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | 0.7300 |  |
| Jogador 6 | 2-4 | 14:16:33 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Tristana | 0.8800 |  |
| Jogador 6 | 2-4 | 14:16:34 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Feérico | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-4 | 14:16:35 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-4 | 14:16:36 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Feérico | DA_18_Tristana | -0.5400 |  |
| Jogador 6 | 2-4 | 14:16:37 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Feérico | DA_18_Tristana | -0.1000 |  |
| Jogador 6 | 2-4 | 14:16:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-5 | 14:16:50 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Tristana | 0.9300 |  |
| Jogador 6 | 2-5 | 14:16:51 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Feérico | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-5 | 14:16:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-5 | 14:16:54 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Feérico | DA_18_Tristana | -0.1600 |  |
| Jogador 6 | 2-5 | 14:16:55 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Feérico | DA_18_Tristana | -0.6300 |  |
| Jogador 6 | 2-5 | 14:16:56 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Tristana | -0.5000 |  |
| Jogador 6 | 2-6 | 14:17:04 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-6 | 14:17:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_18_Tristana | -0.1200 |  |
| Jogador 6 | 2-7 | 14:17:20 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Feérico | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-7 | 14:17:21 | MOVE Bench -> Board: Yorick (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Feérico | DA_18_Tristana | -0.2600 |  |
| Jogador 6 | 2-7 | 14:17:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 2-7 | 14:17:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-7 | 14:17:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 2-7 | 14:17:25 | MOVE Bench -> Board: Kayle (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Fumegante | DA_18_Tristana | 0.3800 |  |
| Jogador 6 | 3-1 | 14:17:35 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Fumegante | DA_18_Tristana | 0.8300 |  |
| Jogador 6 | 3-1 | 14:17:36 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Fumegante | DA_18_Tristana | -0.4200 |  |
| Jogador 6 | 3-2 | 14:17:53 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Fumegante | DA_18_Tristana | 0.7700 |  |
| Jogador 6 | 3-2 | 14:17:54 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Kog'Maw (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Fumegante | DA_18_Tristana | 0.0700 |  |
| Jogador 6 | 3-2 | 14:17:55 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Kog'Maw (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Fumegante | DA_18_Tristana | 0.0600 |  |
| Jogador 6 | 3-2 | 14:17:56 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Fumegante | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 3-2 | 14:17:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-2 | 14:17:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 2 | Fumegante | DA_18_Tristana | -0.0900 |  |
| Jogador 6 | 3-3 | 14:18:09 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Fumegante | DA_18_Tristana | 0.3100 |  |
| Jogador 6 | 3-3 | 14:18:10 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Fumegante | DA_18_Tristana | -0.0500 |  |
| Jogador 6 | 3-4 | 14:18:30 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Fumegante | DA_18_Tristana | 0.7700 |  |
| Jogador 6 | 3-4 | 14:18:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-4 | 14:18:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 2 | Fumegante | DA_18_Tristana | 0.1000 |  |
| Jogador 6 | 3-4 | 14:18:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 2 | Fumegante | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 3-4 | 14:18:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 2 | Fumegante | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 3-4 | 14:18:36 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 2 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-5 | 14:18:47 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Fumegante | DA_18_Tristana | 0.1300 |  |
| Jogador 6 | 3-5 | 14:18:48 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Fumegante | DA_18_Tristana | 0.0100 |  |
| Jogador 6 | 3-6 | 14:19:10 | COMPROU: Gnar (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Fumegante | DA_18_GnarSmall | 0.1000 |  |
| Jogador 6 | 3-6 | 14:19:12 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Fumegante | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-6 | 14:19:13 | VENDEU: Gnar (i:10.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Fumegante | DA_18_Tristana | -0.1300 |  |
| Jogador 6 | 3-6 | 14:19:14 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Fumegante | DA_18_Tristana | -1.0200 |  |
| Jogador 6 | 3-6 | 14:19:15 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Fumegante | DA_18_Tristana | 0.1700 |  |
| Jogador 6 | 3-7 | 14:19:27 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Fumegante | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 3-7 | 14:19:28 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Fumegante | DA_18_Tristana | 0.2200 |  |
| Jogador 6 | 3-7 | 14:19:29 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Fumegante | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 4-1 | 14:19:51 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Fumegante | DA_18_Tristana | 0.6300 |  |
| Jogador 6 | 4-1 | 14:19:52 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Fumegante | DA_18_Tristana | -0.4900 |  |
| Jogador 6 | 4-1 | 14:19:53 | VENDEU: Zyra (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Fumegante | DA_18_Tristana | -0.4900 |  |
| Jogador 6 | 4-1 | 14:19:54 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Fumegante | DA_18_Tristana | -0.9600 |  |
| Jogador 6 | 4-1 | 14:19:56 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Fumegante | DA_18_Tristana | -1.0200 |  |
| Jogador 6 | 4-2 | 14:20:09 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Fumegante | DA_18_Tristana | 0.9900 |  |
| Jogador 6 | 4-2 | 14:20:10 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 4-2 | 14:20:11 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 4-3 | 14:20:34 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Fumegante | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 4-3 | 14:20:35 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Fumegante | DA_18_Tristana | 0.1100 |  |
| Jogador 6 | 4-3 | 14:20:36 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Fumegante | DA_18_Tristana | -0.2500 |  |
| Jogador 6 | 4-3 | 14:20:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 4-3 | 14:20:39 | MOVE Board -> Board: Tristana (i:6.0) <-> Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Fumegante | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 4-4 | 14:20:52 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 70 | 5 | Fumegante | DA_18_Tristana | 0.3600 |  |
| Jogador 6 | 4-4 | 14:20:53 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Fumegante | DA_18_Tristana | 0.0700 |  |
| Jogador 6 | 4-4 | 14:20:55 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Fumegante | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 4-5 | 14:21:20 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Fumegante | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 4-5 | 14:21:21 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Fumegante | DA_18_Tristana | -0.0500 |  |
| Jogador 6 | 4-5 | 14:21:23 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Fumegante | DA_18_Tristana | 0.0400 |  |
| Jogador 6 | 4-5 | 14:21:24 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Fumegante | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 4-5 | 14:21:25 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Fumegante | DA_18_Tristana | -0.0700 |  |
| Jogador 6 | 4-6 | 14:21:40 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 4-6 | 14:21:41 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Fumegante | DA_18_Tristana | 0.9600 |  |
| Jogador 6 | 4-6 | 14:21:43 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Fumegante | DA_18_Tristana | 0.2800 |  |
| Jogador 6 | 4-7 | 14:22:10 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Fumegante | DA_18_Tristana | 1.0200 |  |
| Jogador 6 | 4-7 | 14:22:12 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Fumegante | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 4-7 | 14:22:13 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Fumegante | DA_18_Tristana | 0.1300 |  |
| Jogador 6 | 4-7 | 14:22:15 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 89 | 5 | Fumegante | DA_18_Tristana | 0.4100 |  |
| Jogador 6 | 4-7 | 14:22:16 | MOVE Bench -> Board: Kayle (i:8.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 89 | 5 | Fumegante | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 5-1 | 14:22:32 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Fumegante | DA_18_Tristana | 0.5400 |  |
| Jogador 6 | 5-1 | 14:22:34 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Fumegante | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 5-1 | 14:22:35 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Fumegante | DA_18_Tristana | 0.1100 |  |
| Jogador 6 | 5-2 | 14:23:04 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Fumegante | DA_18_Tristana | 1.0200 |  |
| Jogador 6 | 5-2 | 14:23:05 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Fumegante | DA_18_Tristana | 1.0200 |  |
| Jogador 6 | 5-2 | 14:23:07 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Fumegante | DA_18_Tristana | 0.1100 |  |
| Jogador 6 | 5-2 | 14:23:09 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Fumegante | DA_18_Tristana | 0.1300 |  |
| Jogador 6 | 5-3 | 14:23:25 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Fumegante | DA_18_Tristana | 0.4100 |  |
| Jogador 6 | 5-3 | 14:23:26 | MOVE Bench -> Board: Mamãe Bicuda (i:12.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Fumegante | DA_18_Tristana | 0.1000 |  |
| Jogador 6 | 5-3 | 14:23:28 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Fumegante | DA_18_Tristana | -0.4100 |  |
| Jogador 6 | 5-3 | 14:23:29 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Fumegante | DA_18_Tristana | -0.6600 |  |
| Jogador 6 | 5-4 | 14:24:02 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Fumegante | DA_18_Tristana | -0.2500 |  |
| Jogador 6 | 5-4 | 14:24:04 | VENDEU: Tristana (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Fumegante | DA_CrimsonRaptor18 | -0.5800 |  |
| Jogador 6 | 5-4 | 14:24:06 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.3100 |  |
| Jogador 6 | 5-4 | 14:24:07 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Fumegante | DA_CrimsonRaptor18 | 0.4000 |  |
| Jogador 7 | ? | 14:15:15 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 14:15:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 14:15:22 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 14:15:23 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 14:15:23 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-1 | 14:15:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-1 | 14:15:25 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 14:15:26 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 14:15:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 14:15:28 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 7 | 1-2 | 14:15:30 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 14:15:31 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 14:15:31 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 14:15:32 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 14:15:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 14:15:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 14:15:38 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-3 | 14:15:39 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-3 | 14:15:39 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 14:15:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2000 |  |
| Jogador 7 | 1-3 | 14:15:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 14:15:47 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8300 |  |
| Jogador 7 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-4 | 14:15:49 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 7 | 1-4 | 14:15:50 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 14:15:52 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4400 |  |
| Jogador 7 | 2-1 | 14:15:59 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 14:15:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-1 | 14:16:00 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 14:16:01 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 14:16:01 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 14:16:02 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-1 | 14:16:03 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | -0.6300 |  |
| Jogador 7 | 2-1 | 14:16:04 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.4400 |  |
| Jogador 7 | 2-2 | 14:16:09 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 1.0500 |  |
| Jogador 7 | 2-2 | 14:16:10 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.6800 |  |
| Jogador 7 | 2-2 | 14:16:11 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1400 |  |
| Jogador 7 | 2-2 | 14:16:12 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 2-2 | 14:16:13 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 14:16:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-2 | 14:16:14 | MOVE Bench -> Board: Varus (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.5500 |  |
| Jogador 7 | 2-3 | 14:16:20 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.3100 |  |
| Jogador 7 | 2-3 | 14:16:25 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 2-3 | 14:16:26 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Sentinel18 | 0.4100 |  |
| Jogador 7 | 2-4 | 14:16:33 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | 0.2900 |  |
| Jogador 7 | 2-4 | 14:16:33 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Sentinel18 | -0.1300 |  |
| Jogador 7 | 2-4 | 14:16:34 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 14:16:35 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 0.3600 |  |
| Jogador 7 | 2-4 | 14:16:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 14:16:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 14:16:38 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 14:16:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Sentinel18 | 0.9100 |  |
| Jogador 7 | 2-5 | 14:16:51 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.8800 |  |
| Jogador 7 | 2-5 | 14:16:53 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.4600 |  |
| Jogador 7 | 2-5 | 14:16:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 14:16:55 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 14:16:56 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.6300 |  |
| Jogador 7 | 2-6 | 14:17:04 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Sentinel18 | -0.2800 |  |
| Jogador 7 | 2-6 | 14:17:05 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-7 | 14:17:20 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Sentinel18 | 0.2200 |  |
| Jogador 7 | 2-7 | 14:17:21 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 0.2000 |  |
| Jogador 7 | 2-7 | 14:17:22 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 0.4000 |  |
| Jogador 7 | 2-7 | 14:17:23 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 2-7 | 14:17:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-7 | 14:17:25 | MOVE Board -> Board: Rammus (i:6.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-1 | 14:17:35 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.8000 |  |
| Jogador 7 | 3-1 | 14:17:36 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 3-2 | 14:17:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Sentinel18 | 0.2800 |  |
| Jogador 7 | 3-2 | 14:17:54 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 3-2 | 14:17:55 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Sentinel18 | 0.2000 |  |
| Jogador 7 | 3-2 | 14:17:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 3-2 | 14:17:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-2 | 14:17:58 | MOVE Board -> Board: Varus (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-3 | 14:18:09 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 3-3 | 14:18:10 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_Sentinel18 | 0.7200 |  |
| Jogador 7 | 3-4 | 14:18:30 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Colosso | DA_Sentinel18 | -0.5200 |  |
| Jogador 7 | 3-4 | 14:18:31 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_Sentinel18 | 0.2800 |  |
| Jogador 7 | 3-4 | 14:18:32 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-4 | 14:18:34 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Colosso | DA_Sentinel18 | -0.5200 |  |
| Jogador 7 | 3-4 | 14:18:35 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 3-4 | 14:18:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 3-5 | 14:18:47 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 3-5 | 14:18:48 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_Sentinel18 | 0.7200 |  |
| Jogador 7 | 3-6 | 14:19:10 | VENDEU: Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_KogMaw18_AD | -0.5300 |  |
| Jogador 7 | 3-6 | 14:19:12 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_KogMaw18_AD | 0.4800 |  |
| Jogador 7 | 3-6 | 14:19:13 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_KogMaw18_AD | -0.4400 |  |
| Jogador 7 | 3-6 | 14:19:14 | MOVE Board -> Board: Hecarim (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-6 | 14:19:15 | MOVE Board -> Board: Rammus (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-7 | 14:19:27 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 7 | 3-7 | 14:19:28 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 7 | 3-7 | 14:19:29 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 7 | 4-1 | 14:19:51 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 4-1 | 14:19:52 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Colosso | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 7 | 4-1 | 14:19:53 | MOVE Board -> Board: Yorick (i:2.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-1 | 14:19:54 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 4-1 | 14:19:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Colosso | DA_KogMaw18_AD | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-2 | 14:20:09 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Colosso | DA_KogMaw18_AD | -0.5300 |  |
| Jogador 7 | 4-2 | 14:20:10 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 7 | 4-2 | 14:20:11 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-3 | 14:20:34 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Colosso | DA_CrimsonRaptor18 | 0.9600 |  |
| Jogador 7 | 4-3 | 14:20:35 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Colosso | DA_CrimsonRaptor18 | 0.4800 |  |
| Jogador 7 | 4-3 | 14:20:36 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 51 | 4 | Colosso | DA_CrimsonRaptor18 | 0.1900 |  |
| Jogador 7 | 4-3 | 14:20:37 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Colosso | DA_CrimsonRaptor18 | -0.0700 |  |
| Jogador 7 | 4-3 | 14:20:39 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Colosso | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 7 | 4-4 | 14:20:52 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Colosso | DA_CrimsonRaptor18 | 0.0700 |  |
| Jogador 7 | 4-4 | 14:20:53 | MOVE Board -> Board: Hecarim (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Colosso | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 7 | 4-4 | 14:20:55 | MOVE Board -> Board: Rammus (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Colosso | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 7 | 4-5 | 14:21:20 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Colosso | DA_KogMaw18_AD | -0.6000 |  |
| Jogador 7 | 4-5 | 14:21:21 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Colosso | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 7 | 4-5 | 14:21:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Colosso | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 7 | 4-5 | 14:21:24 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Colosso | DA_KogMaw18_AD | 0.9500 |  |
| Jogador 7 | 4-5 | 14:21:25 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Colosso | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 7 | 4-6 | 14:21:40 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 7 | 4-6 | 14:21:41 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_KogMaw18_AD | -0.7300 |  |
| Jogador 7 | 4-6 | 14:21:43 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_KogMaw18_AD | 0.4700 |  |
| Jogador 7 | 4-7 | 14:22:10 | COMPROU: Ashe (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 80 | 5 | Colosso | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 7 | 4-7 | 14:22:12 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Colosso | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 7 | 4-7 | 14:22:13 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 7 | 4-7 | 14:22:15 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 7 | 4-7 | 14:22:16 | MOVE Bench -> Board: Ashe (i:10.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Colosso | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 7 | 5-1 | 14:22:32 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Colosso | DA_KogMaw18_AD | 0.7300 |  |
| Jogador 7 | 5-1 | 14:22:34 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Colosso | DA_KogMaw18_AD | 0.6300 |  |
| Jogador 7 | 5-1 | 14:22:35 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_NegatronCloak -> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 82 | 5 | Colosso | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 7 | 5-2 | 14:23:04 | VENDEU: Hecarim (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Colosso | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 7 | 5-2 | 14:23:05 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Master Yi (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Colosso | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 7 | 5-2 | 14:23:07 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Ashe (i:10.0) (tabuleiro slot 23) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Colosso | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 7 | 5-2 | 14:23:09 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Colosso | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 7 | 5-3 | 14:23:25 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 116 | 5 | Colosso | DA_KogMaw18_AD | -0.5900 |  |
| Jogador 7 | 5-3 | 14:23:26 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 114 | 5 | Colosso | DA_KogMaw18_AD | 0.4100 |  |
| Jogador 7 | 5-3 | 14:23:28 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Ashe (i:10.0) (tabuleiro slot 23) | STABILIZE | STABILIZE: pressão de vida | 114 | 5 | Colosso | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 7 | 5-3 | 14:23:29 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Ashe (i:10.0) (tabuleiro slot 23) | STABILIZE | STABILIZE: pressão de vida | 114 | 5 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 5-4 | 14:24:02 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Rammus (i:6.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 5-4 | 14:24:04 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Colosso | DA_Scuttlecrab18 | -0.6000 |  |
| Jogador 7 | 5-4 | 14:24:06 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 130 | 5 | Colosso | DA_Scuttlecrab18 | 0.3700 |  |
| Jogador 7 | 5-4 | 14:24:07 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 130 | 5 | Colosso | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 7 | 5-5 | 14:24:26 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 144 | 5 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 7 | 5-5 | 14:24:28 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 141 | 5 | Colosso | DA_Scuttlecrab18 | 1.0200 |  |
| Jogador 7 | 5-5 | 14:24:30 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 138 | 5 | Colosso | DA_Scuttlecrab18 | 0.1200 |  |
| Jogador 7 | 5-5 | 14:24:31 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 138 | 5 | Colosso | DA_Scuttlecrab18 | 0.4100 |  |
| Jogador 7 | 5-6 | 14:25:03 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 149 | 5 | Colosso | DA_Scuttlecrab18 | 0.4000 |  |
| Jogador 7 | 5-6 | 14:25:05 | VENDEU: Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 157 | 5 | Colosso | DA_Scuttlecrab18 | -0.6000 |  |
| Jogador 7 | 5-6 | 14:25:06 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Colosso | DA_Scuttlecrab18 | 0.8800 |  |
| Jogador 7 | 5-6 | 14:25:08 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 151 | 5 | Colosso | DA_Scuttlecrab18 | 0.2400 |  |
| Jogador 7 | 5-7 | 14:25:26 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 162 | 5 | Colosso | DA_Scuttlecrab18 | 1.0800 |  |
| Jogador 7 | 5-7 | 14:25:28 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 159 | 5 | Colosso | DA_Scuttlecrab18 | 0.7300 |  |
| Jogador 7 | 5-7 | 14:25:29 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 157 | 5 | Colosso | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 7 | 5-7 | 14:25:31 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Master Yi (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 157 | 5 | Colosso | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 7 | 6-1 | 14:26:04 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Master Yi (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 170 | 5 | Colosso | DA_Scuttlecrab18 | 0.0700 |  |
| Jogador 7 | 6-1 | 14:26:06 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Master Yi (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 170 | 5 | Colosso | DA_Scuttlecrab18 | 0.1000 |  |
| Jogador 7 | 6-1 | 14:26:08 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Aronguejo (i:8.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 170 | 5 | Colosso | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 7 | 6-1 | 14:26:09 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 178 | 5 | Colosso | DA_Scuttlecrab18 | -0.0800 |  |
| Jogador 7 | 6-2 | 14:26:28 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 188 | 5 | Colosso | DA_Scuttlecrab18 | 0.9200 |  |
| Jogador 7 | 6-2 | 14:26:29 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Aronguejo (i:8.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 188 | 5 | Colosso | DA_Scuttlecrab18 | 0.1400 |  |
| Jogador 7 | 6-2 | 14:26:31 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 193 | 5 | Colosso | DA_Scuttlecrab18 | -0.6000 |  |
| Jogador 7 | 6-2 | 14:26:33 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 190 | 5 | Colosso | DA_Scuttlecrab18 | 0.7800 |  |
| Jogador 7 | 6-3 | 14:27:07 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 206 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 7 | 6-3 | 14:27:09 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 203 | 5 | Colosso | DA_Scuttlecrab18 | 1.0800 |  |
| Jogador 7 | 6-3 | 14:27:11 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Colosso | DA_Scuttlecrab18 | 0.3900 |  |
| Jogador 7 | 6-3 | 14:27:12 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Colosso | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 7 | 6-4 | 14:27:32 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 211 | 5 | Colosso | DA_Scuttlecrab18 | 0.3500 |  |
| Jogador 7 | 6-4 | 14:27:34 | VENDEU: Master Yi (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 219 | 5 | Colosso | DA_Scuttlecrab18 | -0.5900 |  |
| Jogador 7 | 6-4 | 14:27:35 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 216 | 5 | Colosso | DA_Scuttlecrab18 | -0.1900 |  |
| Jogador 7 | 6-4 | 14:27:37 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Fiddlesticks (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 216 | 5 | Colosso | DA_Scuttlecrab18 | 0.0500 |  |
| Jogador 7 | 6-5 | 14:28:14 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Fiddlesticks (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 230 | 5 | Colosso | DA_Scuttlecrab18 | 0.0900 |  |
| Jogador 7 | 6-5 | 14:28:16 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Fiddlesticks (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 230 | 5 | Colosso | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 7 | 6-5 | 14:28:17 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 233 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 7 | 6-5 | 14:28:19 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 232 | 5 | Colosso | DA_Scuttlecrab18 | 1.0800 |  |
| Jogador 8 | ? | 14:15:15 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | ? | 14:15:17 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | ? | 14:15:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 14:15:22 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 14:15:23 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-1 | 14:15:23 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-1 | 14:15:25 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3600 |  |
| Jogador 8 | 1-1 | 14:15:25 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-1 | 14:15:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 14:15:28 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5000 |  |
| Jogador 8 | 1-2 | 14:15:30 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 8 | 1-2 | 14:15:31 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 8 | 1-2 | 14:15:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 14:15:38 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-3 | 14:15:39 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 8 | 1-3 | 14:15:39 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1700 |  |
| Jogador 8 | 1-3 | 14:15:40 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 8 | 1-3 | 14:15:41 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 8 | 1-3 | 14:15:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 14:15:47 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.1100 |  |
| Jogador 8 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 1-4 | 14:15:48 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 1-4 | 14:15:49 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 1-4 | 14:15:50 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 1.1000 |  |
| Jogador 8 | 1-4 | 14:15:51 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 1-4 | 14:15:51 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 1-4 | 14:15:52 | MOVE Bench -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.4100 |  |
| Jogador 8 | 2-1 | 14:15:59 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-1 | 14:15:59 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.2100 |  |
| Jogador 8 | 2-1 | 14:16:00 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 2-1 | 14:16:01 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 2-1 | 14:16:01 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 2-1 | 14:16:02 | MOVE Board -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 2-1 | 14:16:03 | MOVE Bench -> Board: Teemo (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.5200 |  |
| Jogador 8 | 2-1 | 14:16:04 | MOVE Bench -> Board: Karma (i:4.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-2 | 14:16:09 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.9800 |  |
| Jogador 8 | 2-2 | 14:16:10 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.9500 |  |
| Jogador 8 | 2-2 | 14:16:11 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.3300 |  |
| Jogador 8 | 2-2 | 14:16:12 | MOVE Bench -> Board: Xayah (i:4.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.1900 |  |
| Jogador 8 | 2-2 | 14:16:13 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.1600 |  |
| Jogador 8 | 2-2 | 14:16:13 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.2700 |  |
| Jogador 8 | 2-2 | 14:16:14 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.4300 |  |
| Jogador 8 | 2-2 | 14:16:14 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.2300 |  |
| Jogador 8 | 2-3 | 14:16:20 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.8600 |  |
| Jogador 8 | 2-3 | 14:16:25 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-3 | 14:16:26 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 2-4 | 14:16:33 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | 0.8200 |  |
| Jogador 8 | 2-4 | 14:16:33 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | -0.5000 |  |
| Jogador 8 | 2-4 | 14:16:34 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_Karma18 | 0.8500 |  |
| Jogador 8 | 2-4 | 14:16:35 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 2-4 | 14:16:36 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_Karma18 | 0.9400 |  |
| Jogador 8 | 2-4 | 14:16:37 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_Karma18 | 0.3300 |  |
| Jogador 8 | 2-4 | 14:16:38 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 2-5 | 14:16:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | 0.8900 |  |
| Jogador 8 | 2-5 | 14:16:51 | MOVE Bench -> Board: Rammus (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 2-5 | 14:16:53 | MOVE Bench -> Board: Kobuko (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | 0.4100 |  |
| Jogador 8 | 2-5 | 14:16:54 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | 0.0400 |  |
| Jogador 8 | 2-5 | 14:16:55 | MOVE Board -> Board: Kobuko (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 2-5 | 14:16:56 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 2-6 | 14:17:04 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_Karma18 | 0.8800 |  |
| Jogador 8 | 2-6 | 14:17:05 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-7 | 14:17:20 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_Karma18 | 0.2300 |  |
| Jogador 8 | 2-7 | 14:17:21 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-7 | 14:17:22 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Enfeitiçador | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 2-7 | 14:17:23 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-7 | 14:17:25 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-7 | 14:17:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 3-1 | 14:17:35 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-1 | 14:17:36 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | 0.7900 |  |
| Jogador 8 | 3-2 | 14:17:53 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_Karma18 | -0.5500 |  |
| Jogador 8 | 3-2 | 14:17:54 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Enfeitiçador | DA_Karma18 | 0.8700 |  |
| Jogador 8 | 3-2 | 14:17:55 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Enfeitiçador | DA_Karma18 | 0.2700 |  |
| Jogador 8 | 3-2 | 14:17:56 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-2 | 14:17:57 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Enfeitiçador | DA_Karma18 | -0.5000 |  |
| Jogador 8 | 3-2 | 14:17:58 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Enfeitiçador | DA_Karma18 | -0.3200 |  |
| Jogador 8 | 3-3 | 14:18:09 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Enfeitiçador | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 3-3 | 14:18:10 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Enfeitiçador | DA_Karma18 | 0.8800 |  |
| Jogador 8 | 3-4 | 14:18:30 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Enfeitiçador | DA_Karma18 | 0.8600 |  |
| Jogador 8 | 3-4 | 14:18:31 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_Karma18 | 0.8000 |  |
| Jogador 8 | 3-4 | 14:18:32 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_Karma18 | -0.8500 |  |
| Jogador 8 | 3-4 | 14:18:34 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Enfeitiçador | DA_Karma18 | 0.8900 |  |
| Jogador 8 | 3-4 | 14:18:35 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Enfeitiçador | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 3-4 | 14:18:36 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Enfeitiçador | DA_Karma18 | -0.3700 |  |
| Jogador 8 | 3-5 | 14:18:47 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 4 | Enfeitiçador | DA_Karma18 | -0.1400 |  |
| Jogador 8 | 3-5 | 14:18:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 4 | Enfeitiçador | DA_Karma18 | 0.9000 |  |
| Jogador 8 | 3-6 | 14:19:10 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Enfeitiçador | DA_Karma18 | 0.2500 |  |
| Jogador 8 | 3-6 | 14:19:12 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 70 | 5 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 3-6 | 14:19:13 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 73 | 5 | Enfeitiçador | DA_Karma18 | -0.4900 |  |
| Jogador 8 | 3-6 | 14:19:14 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Kobuko (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 73 | 5 | Enfeitiçador | DA_Karma18 | 0.1300 |  |
| Jogador 8 | 3-6 | 14:19:15 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Kobuko (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 73 | 5 | Enfeitiçador | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 3-7 | 14:19:27 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 82 | 5 | Enfeitiçador | DA_Karma18 | 0.9600 |  |
| Jogador 8 | 3-7 | 14:19:28 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Enfeitiçador | DA_Karma18 | 0.3800 |  |
| Jogador 8 | 3-7 | 14:19:29 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_SparringGloves -> Kobuko (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Enfeitiçador | DA_Karma18 | 0.1600 |  |
| Jogador 8 | 4-1 | 14:19:51 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Enfeitiçador | DA_Karma18 | -0.2400 |  |
| Jogador 8 | 4-1 | 14:19:52 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Enfeitiçador | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 4-1 | 14:19:53 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Rammus (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Enfeitiçador | DA_Karma18 | 0.1000 |  |
| Jogador 8 | 4-1 | 14:19:54 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Enfeitiçador | DA_Karma18 | 0.4000 |  |
| Jogador 8 | 4-1 | 14:19:56 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Enfeitiçador | DA_Karma18 | -0.2200 |  |
| Jogador 8 | 4-2 | 14:20:09 | VENDEU: Warwick (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Enfeitiçador | DA_Karma18 | -0.5200 |  |
| Jogador 8 | 4-2 | 14:20:10 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Enfeitiçador | DA_Karma18 | 0.7500 |  |
| Jogador 8 | 4-2 | 14:20:11 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 4-3 | 14:20:34 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Enfeitiçador | DA_Karma18 | 0.3900 |  |
| Jogador 8 | 4-3 | 14:20:35 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 110 | 5 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 4-3 | 14:20:36 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Enfeitiçador | DA_Karma18 | 0.3300 |  |
| Jogador 8 | 4-3 | 14:20:37 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 110 | 5 | Enfeitiçador | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 4-3 | 14:20:39 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 4-4 | 14:20:52 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 121 | 5 | Enfeitiçador | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 4-4 | 14:20:53 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 119 | 5 | Enfeitiçador | DA_Karma18 | 0.8500 |  |
| Jogador 8 | 4-4 | 14:20:55 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 122 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-5 | 14:21:20 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 131 | 5 | Enfeitiçador | DA_18_Cassiopeia | 0.9600 |  |
| Jogador 8 | 4-5 | 14:21:21 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 130 | 5 | Enfeitiçador | DA_18_Cassiopeia | 0.1000 |  |
| Jogador 8 | 4-5 | 14:21:23 | VENDEU: Cassiopeia (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 138 | 5 | Enfeitiçador | DA_18_Sivir | -0.6000 |  |
| Jogador 8 | 4-5 | 14:21:24 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 136 | 5 | Enfeitiçador | DA_18_Sivir | -0.2600 |  |
| Jogador 8 | 4-5 | 14:21:25 | MOVE Bench -> Board: Sivir (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 136 | 5 | Enfeitiçador | DA_18_Sivir | 0.4000 |  |
| Jogador 8 | 4-6 | 14:21:40 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 145 | 5 | Enfeitiçador | DA_18_Sivir | 0.0300 |  |
| Jogador 8 | 4-6 | 14:21:41 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 146 | 5 | Enfeitiçador | DA_18_Sivir | -0.0300 |  |
| Jogador 8 | 4-6 | 14:21:43 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 144 | 5 | Enfeitiçador | DA_18_Sivir | 0.0500 |  |
| Jogador 8 | 4-7 | 14:22:10 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 155 | 5 | Enfeitiçador | DA_18_Sivir | 0.1000 |  |
| Jogador 8 | 4-7 | 14:22:12 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NegatronCloak -> Karma (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 155 | 5 | Enfeitiçador | DA_18_Sivir | 0.1500 |  |
| Jogador 8 | 4-7 | 14:22:13 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 157 | 5 | Enfeitiçador | DA_18_Sivir | 0.0000 |  |
| Jogador 8 | 4-7 | 14:22:15 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Enfeitiçador | DA_18_Sivir | 0.9000 |  |
| Jogador 8 | 4-7 | 14:22:16 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 156 | 5 | Enfeitiçador | DA_18_Sivir | -0.0300 |  |
| Jogador 8 | 5-1 | 14:22:32 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Enfeitiçador | DA_18_Sivir | 0.9900 |  |
| Jogador 8 | 5-1 | 14:22:34 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Enfeitiçador | DA_18_Sivir | 0.0000 |  |
| Jogador 8 | 5-1 | 14:22:35 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 164 | 5 | Enfeitiçador | DA_18_Sivir | 0.1600 |  |
| Jogador 8 | 5-2 | 14:23:04 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 177 | 5 | Enfeitiçador | DA_18_Sivir | -0.0300 |  |
| Jogador 8 | 5-2 | 14:23:05 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 176 | 5 | Enfeitiçador | DA_18_Sivir | 0.1400 |  |
| Jogador 8 | 5-2 | 14:23:07 | VENDEU: Ornn (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 177 | 5 | Enfeitiçador | DA_18_Sivir | -0.0300 |  |
| Jogador 8 | 5-2 | 14:23:09 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Enfeitiçador | DA_18_Sivir | 0.0100 |  |
| Jogador 8 | 5-3 | 14:23:25 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 187 | 5 | Enfeitiçador | DA_18_Sivir | 0.0000 |  |
| Jogador 8 | 5-3 | 14:23:26 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 184 | 5 | Enfeitiçador | DA_18_Sivir | 0.4500 |  |
| Jogador 8 | 5-3 | 14:23:28 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 186 | 5 | Enfeitiçador | DA_18_Sivir | -0.7500 |  |
| Jogador 8 | 5-3 | 14:23:29 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 184 | 5 | Enfeitiçador | DA_18_Sivir | 0.0100 |  |
| Jogador 8 | 5-4 | 14:24:02 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 196 | 5 | Enfeitiçador | DA_18_Sivir | 0.0000 |  |
| Jogador 8 | 5-4 | 14:24:04 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 195 | 5 | Enfeitiçador | DA_18_Sivir | 1.0200 |  |
| Jogador 8 | 5-4 | 14:24:06 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 197 | 5 | Enfeitiçador | DA_18_Sivir | -0.1200 |  |
| Jogador 8 | 5-4 | 14:24:07 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 196 | 5 | Enfeitiçador | DA_18_Sivir | 0.1300 |  |
| Jogador 8 | 5-5 | 14:24:26 | VENDEU: Ornn (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 208 | 5 | Enfeitiçador | DA_18_Sivir | -0.0300 |  |
| Jogador 8 | 5-5 | 14:24:28 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 207 | 5 | Enfeitiçador | DA_18_Sivir | 1.1000 |  |
| Jogador 8 | 5-5 | 14:24:30 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 206 | 5 | Enfeitiçador | DA_18_Sivir | 0.5300 |  |
| Jogador 8 | 5-5 | 14:24:31 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 204 | 5 | Enfeitiçador | DA_18_Sivir | 0.4200 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 37 | 37 | 185 | 37 | 19 | 163 | 9 | 42 |
| Jogador 2 | 23 | 24 | 120 | 23 | 14 | 105 | 2 | 5 |
| Jogador 3 | 30 | 30 | 150 | 30 | 16 | 130 | 3 | 15 |
| Jogador 4 | 27 | 29 | 145 | 27 | 16 | 118 | 7 | 19 |
| Jogador 5 | 34 | 35 | 175 | 34 | 17 | 142 | 7 | 21 |
| Jogador 6 | 30 | 30 | 150 | 30 | 17 | 126 | 8 | 34 |
| Jogador 7 | 37 | 37 | 185 | 37 | 23 | 168 | 8 | 54 |
| Jogador 8 | 31 | 31 | 155 | 31 | 18 | 141 | 5 | 36 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 163 | 163 | 163 | 0 | 152 | 0 | 163 | 163 | 163 | 68/53 |
| Jogador 2 | 105 | 105 | 105 | 0 | 100 | 0 | 105 | 105 | 105 | 47/36 |
| Jogador 3 | 130 | 130 | 130 | 0 | 122 | 0 | 130 | 130 | 130 | 53/39 |
| Jogador 4 | 118 | 118 | 118 | 0 | 111 | 0 | 118 | 118 | 118 | 47/32 |
| Jogador 5 | 142 | 142 | 142 | 0 | 132 | 0 | 142 | 142 | 142 | 64/50 |
| Jogador 6 | 126 | 126 | 126 | 0 | 117 | 0 | 126 | 126 | 126 | 48/34 |
| Jogador 7 | 168 | 168 | 168 | 0 | 146 | 0 | 168 | 168 | 168 | 65/52 |
| Jogador 8 | 141 | 141 | 141 | 0 | 131 | 0 | 141 | 141 | 141 | 71/57 |

