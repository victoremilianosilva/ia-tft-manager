# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4900**
- Achados: **756**
- CRITICAL: 0 | HIGH: 9 | MEDIUM: 60 | LOW: 687

## Metadados da sessão

- Match ID: 76868b78-d6f1-4d86-a5ea-2855ce203c85
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: b4bc7f3515fcec275410f077fa9caa611452922ad7529a55673266ea2a775a4d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4103**
- Entradas posteriores à eliminação ignoradas: **797**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 113 | 6 | 1 | 13 | 28 | 1 | 1 | não/inconclusivo | 0 |
| Jogador 6 | 119 | 6 | 2 | 16 | 38 | 1 | 0 | não/inconclusivo | 0 |
| Jogador 7 | 209 | 8 | 16 | 16 | 54 | 2 | 4 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 235 | 56 | 23 | 7 | 6 | 27 | 106 | 0.0575 | 8 | 49 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 5, ALL_IN::MOVE_BENCH: 7, ALL_IN::PASS: 1, ALL_IN::SELL: 1, FAST8::BUY: 28, FAST8::BUY_XP: 4, FAST8::ITEM: 5, FAST8::MOVE_BENCH: 17, FAST8::MOVE_BOARD: 42, FAST8::PASS: 16, FAST8::REROLL: 6, FAST8::SELL: 19, STABILIZE::BUY: 23, STABILIZE::BUY_XP: 3, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 22, STABILIZE::MOVE_BOARD: 18, STABILIZE::PASS: 10, STABILIZE::SELL: 3
- Jogador 1 — recompensas por ação: BUY: média 0.4464 (n=56), BUY_XP: média 0.0429 (n=7), ITEM: média 0.1680 (n=10), MOVE_BENCH: média -0.0585 (n=46), MOVE_BOARD: média -0.0072 (n=60), PASS: média -0.1267 (n=27), REROLL: média -0.2500 (n=6), SELL: média -0.2365 (n=23)
| Jogador 2 | 205 | 54 | 18 | 14 | 4 | 25 | 79 | 0.1102 | 6 | 46 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 10, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 3, ALL_IN::MOVE_BOARD: 4, ALL_IN::REROLL: 4, ALL_IN::SELL: 4, FAST8::BUY: 22, FAST8::BUY_XP: 8, FAST8::ITEM: 7, FAST8::MOVE_BENCH: 4, FAST8::MOVE_BOARD: 37, FAST8::PASS: 14, FAST8::SELL: 8, STABILIZE::BUY: 22, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 2, STABILIZE::MOVE_BENCH: 10, STABILIZE::MOVE_BOARD: 21, STABILIZE::PASS: 11, STABILIZE::SELL: 6
- Jogador 2 — recompensas por ação: BUY: média 0.5126 (n=54), BUY_XP: média -0.0264 (n=14), ITEM: média 0.1591 (n=11), MOVE_BENCH: média 0.1629 (n=17), MOVE_BOARD: média -0.0045 (n=62), PASS: média -0.0552 (n=25), REROLL: média -0.0700 (n=4), SELL: média -0.4056 (n=18)
| Jogador 3 | 176 | 39 | 13 | 1 | 0 | 29 | 85 | 0.0475 | 4 | 23 |
- Jogador 3 — ações por estratégia: ALL_IN::MOVE_BENCH: 3, ALL_IN::PASS: 1, FAST8::BUY: 11, FAST8::ITEM: 6, FAST8::MOVE_BENCH: 24, FAST8::MOVE_BOARD: 15, FAST8::PASS: 9, FAST8::SELL: 9, STABILIZE::BUY: 28, STABILIZE::BUY_XP: 1, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 25, STABILIZE::PASS: 19, STABILIZE::SELL: 4
- Jogador 3 — recompensas por ação: BUY: média 0.5249 (n=39), BUY_XP: média 0.0200 (n=1), ITEM: média 0.1789 (n=9), MOVE_BENCH: média -0.0998 (n=45), MOVE_BOARD: média -0.0085 (n=40), PASS: média -0.1359 (n=29), SELL: média -0.3823 (n=13)
| Jogador 4 | 108 | 28 | 4 | 1 | 0 | 17 | 52 | 0.1312 | 4 | 16 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 3, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 5, ALL_IN::MOVE_BOARD: 3, ALL_IN::PASS: 3, ALL_IN::SELL: 2, LOSS_STREAK::BUY: 2, LOSS_STREAK::BUY_XP: 1, LOSS_STREAK::MOVE_BENCH: 1, LOSS_STREAK::MOVE_BOARD: 2, STABILIZE::BUY: 23, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 23, STABILIZE::PASS: 14, STABILIZE::SELL: 2
- Jogador 4 — recompensas por ação: BUY: média 0.5989 (n=28), BUY_XP: média 0.0400 (n=1), ITEM: média 0.1867 (n=6), MOVE_BENCH: média 0.0542 (n=24), MOVE_BOARD: média -0.0079 (n=28), PASS: média -0.1218 (n=17), SELL: média -0.6925 (n=4)
| Jogador 5 | 287 | 82 | 45 | 11 | 12 | 27 | 96 | 0.0613 | 11 | 54 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 25, ALL_IN::ITEM: 4, ALL_IN::MOVE_BENCH: 22, ALL_IN::MOVE_BOARD: 7, ALL_IN::OTHER: 1, ALL_IN::PASS: 7, ALL_IN::REROLL: 11, ALL_IN::SELL: 17, FAST8::BUY: 6, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 10, FAST8::PASS: 4, FAST8::SELL: 5, STABILIZE::BUY: 51, STABILIZE::BUY_XP: 11, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 22, STABILIZE::MOVE_BOARD: 33, STABILIZE::PASS: 16, STABILIZE::REROLL: 1, STABILIZE::SELL: 23
- Jogador 5 — recompensas por ação: BUY: média 0.4154 (n=82), BUY_XP: média 0.0109 (n=11), ITEM: média 0.1361 (n=13), MOVE_BENCH: média -0.0428 (n=46), MOVE_BOARD: média -0.0130 (n=50), OTHER: média -0.0200 (n=1), PASS: média -0.2067 (n=27), REROLL: média -0.0775 (n=12), SELL: média -0.2044 (n=45)
| Jogador 6 | 135 | 38 | 10 | 2 | 2 | 20 | 57 | 0.1039 | 11 | 28 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::ITEM: 1, ALL_IN::MOVE_BENCH: 2, ALL_IN::MOVE_BOARD: 7, ALL_IN::PASS: 3, ALL_IN::REROLL: 2, ALL_IN::SELL: 4, FAST8::BUY: 3, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 5, FAST8::MOVE_BOARD: 8, FAST8::PASS: 3, STABILIZE::BUY: 28, STABILIZE::BUY_XP: 2, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 22, STABILIZE::PASS: 14, STABILIZE::SELL: 6
- Jogador 6 — recompensas por ação: BUY: média 0.4934 (n=38), BUY_XP: média -0.0600 (n=2), ITEM: média 0.2100 (n=6), MOVE_BENCH: média 0.0655 (n=20), MOVE_BOARD: média -0.0116 (n=37), PASS: média -0.1310 (n=20), REROLL: média -0.0700 (n=2), SELL: média -0.3980 (n=10)
| Jogador 7 | 249 | 54 | 18 | 16 | 0 | 31 | 116 | 0.0398 | 4 | 46 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 1, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 7, ALL_IN::PASS: 2, ALL_IN::SELL: 1, FAST8::BUY: 20, FAST8::BUY_XP: 8, FAST8::ITEM: 5, FAST8::MOVE_BENCH: 31, FAST8::MOVE_BOARD: 30, FAST8::PASS: 16, FAST8::SELL: 7, STABILIZE::BUY: 27, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 19, STABILIZE::PASS: 10, STABILIZE::SELL: 7, WINSTREAK::BUY: 6, WINSTREAK::ITEM: 1, WINSTREAK::MOVE_BENCH: 12, WINSTREAK::MOVE_BOARD: 4, WINSTREAK::PASS: 3, WINSTREAK::SELL: 3
- Jogador 7 — recompensas por ação: BUY: média 0.5354 (n=54), BUY_XP: média -0.0156 (n=16), ITEM: média 0.1000 (n=14), MOVE_BENCH: média -0.1378 (n=63), MOVE_BOARD: média -0.0077 (n=53), PASS: média -0.1274 (n=31), SELL: média -0.3944 (n=18)
| Jogador 8 | 180 | 55 | 22 | 16 | 0 | 20 | 59 | 0.0912 | 6 | 37 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 1, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 8, ALL_IN::PASS: 3, FAST8::BUY: 15, FAST8::BUY_XP: 6, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 3, FAST8::MOVE_BOARD: 21, FAST8::PASS: 10, FAST8::SELL: 5, STABILIZE::BUY: 39, STABILIZE::BUY_XP: 10, STABILIZE::ITEM: 4, STABILIZE::MOVE_BENCH: 8, STABILIZE::MOVE_BOARD: 19, STABILIZE::PASS: 7, STABILIZE::SELL: 17
- Jogador 8 — recompensas por ação: BUY: média 0.4014 (n=55), BUY_XP: média -0.0144 (n=16), ITEM: média 0.1625 (n=8), MOVE_BENCH: média -0.0258 (n=19), MOVE_BOARD: média -0.0060 (n=40), PASS: média -0.0600 (n=20), SELL: média -0.2182 (n=22)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 10:05:44 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.5100 |  |
| Jogador 1 | ? | 10:05:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 10:05:50 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 10:05:51 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 10:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 10:05:56 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 10:05:58 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2900 |  |
| Jogador 1 | 1-2 | 10:05:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 10:06:03 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.4100 |  |
| Jogador 1 | 1-3 | 10:06:05 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 10:06:06 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 10:06:06 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 1-3 | 10:06:07 | MOVE Board -> Board: Akali (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 1-3 | 10:06:07 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 1 | 1-3 | 10:06:09 | MOVE Board -> Board: Ornn (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 1-3 | 10:06:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 10:06:13 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 1-4 | 10:06:14 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 0.3600 |  |
| Jogador 1 | 1-4 | 10:06:16 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-4 | 10:06:16 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-4 | 10:06:17 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | 1-4 | 10:06:17 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 0.1200 |  |
| Jogador 1 | 1-4 | 10:06:18 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Ornn | 0.1900 |  |
| Jogador 1 | 1-4 | 10:06:18 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Ornn | 0.4900 |  |
| Jogador 1 | 1-4 | 10:06:19 | MOVE Board -> Board: Akali (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-4 | 10:06:19 | MOVE Board -> Board: Akali (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-1 | 10:06:22 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Ornn | 0.8000 |  |
| Jogador 1 | 2-1 | 10:06:24 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.3300 |  |
| Jogador 1 | 2-1 | 10:06:25 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-1 | 10:06:26 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | -0.1700 |  |
| Jogador 1 | 2-1 | 10:06:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-2 | 10:06:31 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Ornn | 0.9600 |  |
| Jogador 1 | 2-2 | 10:06:31 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Ornn | 0.8300 |  |
| Jogador 1 | 2-2 | 10:06:34 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.3200 |  |
| Jogador 1 | 2-2 | 10:06:35 | MOVE Bench -> Board: Ornn (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | -0.2900 |  |
| Jogador 1 | 2-2 | 10:06:36 | MOVE Bench -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.0400 |  |
| Jogador 1 | 2-2 | 10:06:36 | MOVE Board -> Board: Xayah (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.1500 |  |
| Jogador 1 | 2-2 | 10:06:37 | MOVE Board -> Board: Akali (i:2.0) <-> Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 10:06:40 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Ornn | 0.3300 |  |
| Jogador 1 | 2-3 | 10:06:41 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Ornn | 0.3000 |  |
| Jogador 1 | 2-3 | 10:06:41 | MOVE Board -> Board: Ornn (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-3 | 10:06:42 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 10:06:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-4 | 10:06:51 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Ornn | 0.7900 |  |
| Jogador 1 | 2-4 | 10:06:52 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Ornn | -0.7400 |  |
| Jogador 1 | 2-4 | 10:06:52 | VENDEU: Sejuani (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_18_Ornn | 0.0400 |  |
| Jogador 1 | 2-4 | 10:06:53 | MOVE Bench -> Board: Akali (i:2.0) <-> Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_18_Ornn | 0.0400 |  |
| Jogador 1 | 2-4 | 10:06:53 | MOVE Bench -> Board: Ornn (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_18_Ornn | 0.4200 |  |
| Jogador 1 | 2-4 | 10:06:54 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_18_Ornn | -0.4100 |  |
| Jogador 1 | 2-4 | 10:06:54 | MOVE Bench -> Board: Akali (i:2.0) <-> Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_18_Ornn | 0.0800 |  |
| Jogador 1 | 2-4 | 10:06:54 | MOVE Bench -> Board: Ornn (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Inferno | DA_18_Ornn | 0.1000 |  |
| Jogador 1 | 2-5 | 10:07:03 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Inferno | DA_18_Ornn | 0.9500 |  |
| Jogador 1 | 2-5 | 10:07:04 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Inferno | DA_18_Ornn | 0.4700 |  |
| Jogador 1 | 2-5 | 10:07:04 | MOVE Bench -> Board: Varus (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Inferno | DA_18_Ornn | -0.5400 |  |
| Jogador 1 | 2-5 | 10:07:05 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Inferno | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 2-5 | 10:07:05 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_18_Ornn | -0.0700 |  |
| Jogador 1 | 2-5 | 10:07:05 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_18_Ornn | -0.4000 |  |
| Jogador 1 | 2-5 | 10:07:06 | MOVE Bench -> Board: Ornn (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_18_Ornn | -0.2300 |  |
| Jogador 1 | 2-5 | 10:07:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_18_Ornn | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 2-6 | 10:07:17 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Inferno | DA_18_Ornn | 0.9000 |  |
| Jogador 1 | 2-6 | 10:07:18 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Inferno | DA_18_Ornn | -0.2300 |  |
| Jogador 1 | 2-6 | 10:07:18 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Inferno | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-6 | 10:07:19 | MOVE Board -> Board: Xayah (i:2.0) <-> Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Inferno | DA_18_Ornn | -0.1000 |  |
| Jogador 1 | 2-6 | 10:07:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Inferno | DA_18_Ornn | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 2-7 | 10:07:34 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_SparringGloves -> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 2-7 | 10:07:34 | MOVE Board -> Board: Ornn (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_18_Ornn | 0.1000 |  |
| Jogador 1 | 2-7 | 10:07:35 | MOVE Board -> Board: Ornn (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-7 | 10:07:36 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_18_Ornn | -0.1700 |  |
| Jogador 1 | 2-7 | 10:07:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_18_Ornn | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-1 | 10:07:50 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Inferno | DA_18_Ornn | -0.3300 |  |
| Jogador 1 | 3-1 | 10:07:51 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Inferno | DA_18_Ornn | -0.5800 |  |
| Jogador 1 | 3-1 | 10:07:51 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Ornn (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Inferno | DA_18_Ornn | 0.1300 |  |
| Jogador 1 | 3-1 | 10:07:52 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Ornn (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Inferno | DA_18_Ornn | 0.1400 |  |
| Jogador 1 | 3-1 | 10:07:53 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Inferno | DA_18_Ornn | 0.0900 |  |
| Jogador 1 | 3-1 | 10:07:53 | MOVE Bench -> Board: Caitlyn (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Inferno | DA_18_Ornn | -0.3400 |  |
| Jogador 1 | 3-1 | 10:07:54 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Inferno | DA_18_Ornn | -0.6900 |  |
| Jogador 1 | 3-1 | 10:07:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Inferno | DA_18_Ornn | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-2 | 10:08:09 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Inferno | DA_18_Ezreal | -0.5800 |  |
| Jogador 1 | 3-2 | 10:08:10 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Inferno | DA_18_Ezreal | -0.1800 |  |
| Jogador 1 | 3-2 | 10:08:10 | MOVE Bench -> Board: Rengar (i:6.0) <-> Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Inferno | DA_18_Ezreal | 0.1600 |  |
| Jogador 1 | 3-2 | 10:08:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Inferno | DA_18_Ezreal | -0.0700 |  |
| Jogador 1 | 3-2 | 10:08:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Inferno | DA_18_Ezreal | 0.0100 |  |
| Jogador 1 | 3-2 | 10:08:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 3 | Inferno | DA_18_Ezreal | 0.1600 |  |
| Jogador 1 | 3-2 | 10:08:13 | MOVE Bench -> Board: Caitlyn (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 3 | Inferno | DA_18_Ezreal | 0.4000 |  |
| Jogador 1 | 3-2 | 10:08:13 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 3 | Inferno | DA_18_Ezreal | -0.0900 |  |
| Jogador 1 | 3-2 | 10:08:13 | MOVE Board -> Board: Caitlyn (i:4.0) <-> Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 3 | Inferno | DA_18_Ezreal | -0.2300 |  |
| Jogador 1 | 3-3 | 10:08:30 | MOVE Board -> Board: Ornn (i:2.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Inferno | DA_18_Ezreal | 0.1900 |  |
| Jogador 1 | 3-3 | 10:08:30 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Inferno | DA_18_Ezreal | 0.0200 |  |
| Jogador 1 | 3-3 | 10:08:31 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Inferno | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-3 | 10:08:31 | MOVE Board -> Board: Rengar (i:6.0) <-> Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Inferno | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-3 | 10:08:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Inferno | DA_18_Ezreal | -0.0300 |  |
| Jogador 1 | 3-4 | 10:08:52 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Inferno | DA_18_Ezreal | 0.0000 |  |
| Jogador 1 | 3-4 | 10:08:52 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Inferno | DA_18_Ezreal | 0.8100 |  |
| Jogador 1 | 3-4 | 10:08:53 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Inferno | DA_18_Ezreal | 0.6000 |  |
| Jogador 1 | 3-4 | 10:08:53 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Inferno | DA_18_Ezreal | 0.0000 |  |
| Jogador 1 | 3-4 | 10:08:54 | MOVE Board -> Board: Shen (i:8.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Inferno | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-4 | 10:08:54 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Caitlyn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Inferno | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-4 | 10:08:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Inferno | DA_18_Ezreal | -0.1300 |  |
| Jogador 1 | 3-5 | 10:09:15 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Inferno | DA_18_Ezreal | 0.2700 |  |
| Jogador 1 | 3-5 | 10:09:15 | VENDEU: Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Inferno | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-5 | 10:09:16 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Inferno | DA_18_Ezreal | 0.7900 |  |
| Jogador 1 | 3-5 | 10:09:17 | MOVE Board -> Board: Caitlyn (i:4.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Inferno | DA_18_Ezreal | 0.0100 |  |
| Jogador 1 | 3-5 | 10:09:17 | MOVE Board -> Board: Rengar (i:6.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Inferno | DA_18_Ezreal | -0.0100 |  |
| Jogador 1 | 3-5 | 10:09:18 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Inferno | DA_18_Ezreal | -0.0200 |  |
| Jogador 1 | 3-5 | 10:09:19 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Inferno | DA_18_Ezreal | -0.0600 |  |
| Jogador 1 | 3-6 | 10:09:43 | VENDEU: Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-6 | 10:09:43 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Inferno | DA_18_Shen | 0.6100 |  |
| Jogador 1 | 3-6 | 10:09:44 | MOVE Board -> Board: Ornn (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Inferno | DA_18_Shen | -0.1400 |  |
| Jogador 1 | 3-6 | 10:09:44 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Inferno | DA_18_Shen | 0.0200 |  |
| Jogador 1 | 3-6 | 10:09:45 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Caitlyn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Inferno | DA_18_Shen | 0.1300 |  |
| Jogador 1 | 3-6 | 10:09:45 | MOVE Board -> Board: Caitlyn (i:4.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 3-6 | 10:09:46 | MOVE Board -> Board: Rengar (i:6.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 3-6 | 10:09:46 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Inferno | DA_18_Shen | -0.1600 |  |
| Jogador 1 | 3-7 | 10:10:07 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_18_Shen | 0.1800 |  |
| Jogador 1 | 3-7 | 10:10:08 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_18_Shen | 0.2300 |  |
| Jogador 1 | 3-7 | 10:10:08 | MOVE Board -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-7 | 10:10:09 | MOVE Bench -> Board: Shen (i:4.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_18_Shen | -0.5300 |  |
| Jogador 1 | 3-7 | 10:10:09 | MOVE Bench -> Board: Shen (i:8.0) <-> Caitlyn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_18_Shen | 0.0900 |  |
| Jogador 1 | 3-7 | 10:10:10 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-7 | 10:10:10 | MOVE Board -> Board: Ornn (i:2.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 3-7 | 10:10:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Inferno | DA_18_Shen | -0.0900 |  |
| Jogador 1 | 4-1 | 10:10:33 | VENDEU: Caitlyn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Inferno | DA_18_Shen | -0.4400 |  |
| Jogador 1 | 4-1 | 10:10:34 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Inferno | DA_18_Shen | 0.3100 |  |
| Jogador 1 | 4-1 | 10:10:34 | MOVE Board -> Board: Shen (i:8.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-1 | 10:10:35 | MOVE Board -> Board: Rengar (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-1 | 10:10:36 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Inferno | DA_18_Shen | -0.1000 |  |
| Jogador 1 | 4-2 | 10:11:01 | VENDEU: Caitlyn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 4-2 | 10:11:02 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Inferno | DA_18_Shen | 0.8900 |  |
| Jogador 1 | 4-2 | 10:11:02 | COMPROU: Ornn (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Inferno | DA_18_Shen | 0.8000 |  |
| Jogador 1 | 4-2 | 10:11:03 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Inferno | DA_18_Shen | 0.6000 |  |
| Jogador 1 | 4-2 | 10:11:03 | MOVE Board -> Board: Akali (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-2 | 10:11:04 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-2 | 10:11:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Inferno | DA_18_Shen | -0.2500 |  |
| Jogador 1 | 4-3 | 10:11:29 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 4-3 | 10:11:30 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-3 | 10:11:30 | MOVE Board -> Board: Akali (i:2.0) <-> Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-3 | 10:11:31 | MOVE Board -> Board: Ornn (i:2.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-3 | 10:11:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Inferno | DA_18_Shen | -0.1300 |  |
| Jogador 1 | 4-4 | 10:11:58 | VENDEU: Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 115 | 5 | Inferno | DA_18_Shen | -0.8500 |  |
| Jogador 1 | 4-4 | 10:11:58 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Inferno | DA_18_Shen | 0.7800 |  |
| Jogador 1 | 4-4 | 10:11:59 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 114 | 5 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 4-4 | 10:11:59 | COMPROU: Malphite (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 110 | 5 | Inferno | DA_18_Shen | -0.1000 |  |
| Jogador 1 | 4-4 | 10:12:00 | MOVE Bench -> Board: Malphite (i:8.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 110 | 5 | Inferno | DA_18_Shen | 0.0400 |  |
| Jogador 1 | 4-4 | 10:12:00 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 110 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-4 | 10:12:00 | MOVE Board -> Board: Shen (i:8.0) <-> Malphite (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 110 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-4 | 10:12:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 110 | 5 | Inferno | DA_18_Shen | -0.1400 |  |
| Jogador 1 | 4-5 | 10:12:26 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 123 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-5 | 10:12:27 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 120 | 5 | Inferno | DA_18_Shen | -0.0500 |  |
| Jogador 1 | 4-5 | 10:12:27 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 123 | 5 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 4-5 | 10:12:28 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-5 | 10:12:28 | MOVE Board -> Board: Malphite (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-5 | 10:12:29 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 117 | 5 | Inferno | DA_18_Shen | 0.0600 |  |
| Jogador 1 | 4-5 | 10:12:29 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 113 | 5 | Inferno | DA_18_Shen | 0.0600 |  |
| Jogador 1 | 4-5 | 10:12:29 | MOVE Board -> Board: Malphite (i:8.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 113 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-5 | 10:12:30 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 113 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-6 | 10:12:58 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 125 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-6 | 10:12:59 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Inferno | DA_18_Shen | 0.4500 |  |
| Jogador 1 | 4-6 | 10:12:59 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 125 | 5 | Inferno | DA_18_Shen | -0.4500 |  |
| Jogador 1 | 4-6 | 10:13:00 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Inferno | DA_18_Shen | 0.0900 |  |
| Jogador 1 | 4-6 | 10:13:00 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-6 | 10:13:01 | MOVE Board -> Board: Akali (i:2.0) <-> Malphite (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-6 | 10:13:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Inferno | DA_18_Shen | -0.1500 |  |
| Jogador 1 | 4-7 | 10:13:34 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Inferno | DA_18_Shen | 0.1400 |  |
| Jogador 1 | 4-7 | 10:13:34 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Inferno | DA_18_Shen | 0.1700 |  |
| Jogador 1 | 4-7 | 10:13:35 | VENDEU: Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 135 | 5 | Inferno | DA_18_Shen | -0.0400 |  |
| Jogador 1 | 4-7 | 10:13:35 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Inferno | DA_18_Shen | 0.8600 |  |
| Jogador 1 | 4-7 | 10:13:36 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Inferno | DA_18_Shen | 0.5800 |  |
| Jogador 1 | 4-7 | 10:13:36 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 129 | 5 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 4-7 | 10:13:37 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 129 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-7 | 10:13:38 | MOVE Board -> Board: Akali (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 129 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-7 | 10:13:39 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Malphite (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 129 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 5-1 | 10:14:09 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 143 | 5 | Inferno | DA_18_Shen | -0.0400 |  |
| Jogador 1 | 5-1 | 10:14:09 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 140 | 5 | Inferno | DA_18_Diana | 0.9500 |  |
| Jogador 1 | 5-1 | 10:14:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 139 | 5 | Inferno | DA_18_Diana | 0.8200 |  |
| Jogador 1 | 5-1 | 10:14:10 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Inferno | DA_18_Diana | 0.3200 |  |
| Jogador 1 | 5-1 | 10:14:11 | MOVE Board -> Board: Malphite (i:8.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Inferno | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 5-1 | 10:14:11 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Inferno | DA_18_Diana | -0.0200 |  |
| Jogador 1 | 5-1 | 10:14:12 | MOVE Board -> Board: Shen (i:8.0) <-> Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Inferno | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 5-1 | 10:14:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Inferno | DA_18_Diana | -0.1800 |  |
| Jogador 1 | 5-2 | 10:14:43 | VENDEU: Diana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 156 | 5 | Inferno | DA_18_Shen | -0.6000 |  |
| Jogador 1 | 5-2 | 10:14:43 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Inferno | DA_18_Shen | 0.8900 |  |
| Jogador 1 | 5-2 | 10:14:44 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 158 | 5 | Inferno | DA_18_Shen | -0.5900 |  |
| Jogador 1 | 5-2 | 10:14:44 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Inferno | DA_18_Shen | 0.3200 |  |
| Jogador 1 | 5-2 | 10:14:45 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-2 | 10:14:45 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Inferno | DA_18_Shen | 0.0800 |  |
| Jogador 1 | 5-2 | 10:14:45 | MOVE Board -> Board: Ornn (i:2.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 5-2 | 10:14:46 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 5-2 | 10:14:46 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Inferno | DA_18_Shen | -0.1900 |  |
| Jogador 1 | 5-3 | 10:15:18 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 169 | 5 | Inferno | DA_18_Shen | 0.0200 |  |
| Jogador 1 | 5-3 | 10:15:19 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Inferno | DA_18_Shen | 0.3400 |  |
| Jogador 1 | 5-3 | 10:15:19 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 169 | 5 | Inferno | DA_18_Shen | -0.5900 |  |
| Jogador 1 | 5-3 | 10:15:20 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Inferno | DA_18_Shen | 0.9500 |  |
| Jogador 1 | 5-3 | 10:15:20 | MOVE Board -> Board: Akali (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 5-3 | 10:15:21 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Malphite (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 5-3 | 10:15:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Inferno | DA_18_Shen | -0.3600 |  |
| Jogador 1 | 5-4 | 10:15:57 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 177 | 5 | Inferno | DA_18_Shen | 0.0600 |  |
| Jogador 1 | 5-4 | 10:15:57 | COMPROU: Lux (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Inferno | DA_18_Shen | -0.1900 |  |
| Jogador 1 | 5-4 | 10:15:58 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Inferno | DA_18_Shen | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 1 | 5-4 | 10:15:58 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Inferno | DA_18_Shen | 0.0600 |  |
| Jogador 1 | 5-4 | 10:15:59 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Inferno | DA_18_Shen | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 1 | 5-4 | 10:15:59 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Inferno | DA_18_Shen | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 1 | 5-4 | 10:16:00 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Inferno | DA_18_Shen | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 1 | 5-4 | 10:16:00 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Inferno | DA_18_Shen | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 1 | 5-4 | 10:16:00 | REROLL | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Inferno | DA_18_Shen | -0.2500 | FAST8_REROLL_REVIEW |
| Jogador 1 | 5-5 | 10:16:35 | VENDEU: Xayah (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 182 | 5 | Inferno | DA_18_Shen | -0.5900 |  |
| Jogador 1 | 5-5 | 10:16:35 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 179 | 5 | Inferno | DA_18_Shen | 0.3000 |  |
| Jogador 1 | 5-5 | 10:16:36 | MOVE Bench -> Board: Akali (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 179 | 5 | Inferno | DA_18_Shen | 0.1100 |  |
| Jogador 1 | 5-5 | 10:16:36 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 179 | 5 | Inferno | DA_18_Shen | -0.6000 |  |
| Jogador 1 | 5-5 | 10:16:36 | MOVE Bench -> Board: Varus (i:2.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 179 | 5 | Inferno | DA_18_Shen | -0.4000 |  |
| Jogador 1 | 5-5 | 10:16:37 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 179 | 5 | Inferno | DA_18_Shen | -0.2100 |  |
| Jogador 1 | 5-6 | 10:17:12 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 193 | 5 | Inferno | DA_18_Shen | -0.0500 |  |
| Jogador 1 | 5-6 | 10:17:14 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 190 | 5 | Inferno | DA_18_Shen | 0.8200 |  |
| Jogador 1 | 5-6 | 10:17:14 | MOVE Bench -> Board: Akali (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 190 | 5 | Inferno | DA_18_Shen | 0.0900 |  |
| Jogador 1 | 5-6 | 10:17:15 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 190 | 5 | Inferno | DA_18_Shen | -0.5800 |  |
| Jogador 1 | 5-6 | 10:17:15 | MOVE Bench -> Board: Varus (i:2.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 190 | 5 | Inferno | DA_18_Shen | -0.3700 |  |
| Jogador 1 | 5-6 | 10:17:16 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 190 | 5 | Inferno | DA_18_Shen | -0.2300 |  |
| Jogador 1 | 5-7 | 10:18:02 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Malphite (i:8.0) (tabuleiro slot 24) | FAST8 | FAST8: composição planejada exige nível 8 | 201 | 5 | Inferno | DA_18_Shen | 0.0400 |  |
| Jogador 1 | 5-7 | 10:18:02 | MOVE Bench -> Board: Akali (i:2.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 201 | 5 | Inferno | DA_18_Shen | 0.1100 |  |
| Jogador 1 | 5-7 | 10:18:02 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 201 | 5 | Inferno | DA_18_Shen | -0.5800 |  |
| Jogador 1 | 5-7 | 10:18:03 | MOVE Bench -> Board: Varus (i:2.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 201 | 5 | Inferno | DA_18_Shen | -0.7500 |  |
| Jogador 1 | 5-7 | 10:18:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 201 | 5 | Inferno | DA_18_Shen | -0.2600 |  |
| Jogador 1 | 6-1 | 10:18:45 | MOVE Bench -> Board: Shen (i:8.0) <-> Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Inferno | DA_18_Shen | 0.1300 |  |
| Jogador 1 | 6-1 | 10:18:45 | VENDEU: Lux (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 216 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 6-1 | 10:18:46 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 215 | 5 | Inferno | DA_18_Shen | 1.1100 |  |
| Jogador 1 | 6-1 | 10:18:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 214 | 5 | Inferno | DA_18_Shen | 1.1100 |  |
| Jogador 1 | 6-1 | 10:18:47 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 214 | 5 | Inferno | DA_18_Shen | 0.5900 |  |
| Jogador 1 | 6-1 | 10:18:47 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Inferno | DA_18_Shen | 0.1300 |  |
| Jogador 1 | 6-1 | 10:18:48 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 207 | 5 | Inferno | DA_18_Shen | -0.1400 |  |
| Jogador 1 | 6-1 | 10:18:48 | MOVE Bench -> Board: Soraka (i:8.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 207 | 5 | Inferno | DA_18_Shen | -0.6500 |  |
| Jogador 1 | 6-1 | 10:18:48 | MOVE Bench -> Board: Rakan (i:4.0) <-> Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 207 | 5 | Inferno | DA_18_Shen | -0.4100 |  |
| Jogador 1 | 6-2 | 10:19:29 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 214 | 5 | Inferno | DA_18_Shen | 0.1800 |  |
| Jogador 1 | 6-2 | 10:19:29 | MOVE Bench -> Board: Shen (i:8.0) <-> Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 214 | 5 | Inferno | DA_18_Shen | 0.1100 |  |
| Jogador 1 | 6-2 | 10:19:29 | MOVE Bench -> Board: Soraka (i:8.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 214 | 5 | Inferno | DA_18_Shen | -0.4100 |  |
| Jogador 1 | 6-2 | 10:19:30 | MOVE Bench -> Board: Rakan (i:4.0) <-> Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 214 | 5 | Inferno | DA_18_Shen | -0.4000 |  |
| Jogador 1 | 6-2 | 10:19:30 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 214 | 5 | Inferno | DA_18_Shen | -0.7000 |  |
| Jogador 2 | ? | 10:05:44 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | ? | 10:05:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 10:05:50 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 10:05:51 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 10:05:51 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-1 | 10:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 10:05:56 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5700 |  |
| Jogador 2 | 1-2 | 10:05:58 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 10:05:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 10:06:03 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.4700 |  |
| Jogador 2 | 1-3 | 10:06:05 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 10:06:06 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 10:06:06 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 1-3 | 10:06:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-3 | 10:06:11 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.5500 |  |
| Jogador 2 | 1-4 | 10:06:13 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 10:06:14 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-4 | 10:06:16 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 1-4 | 10:06:16 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.2500 |  |
| Jogador 2 | 1-4 | 10:06:17 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 1-4 | 10:06:17 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 1-4 | 10:06:18 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 1-4 | 10:06:18 | MOVE Board -> Board: Veigar (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 10:06:19 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 1-4 | 10:06:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 10:06:22 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 2-1 | 10:06:24 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -1.1500 |  |
| Jogador 2 | 2-1 | 10:06:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-1 | 10:06:26 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.3200 |  |
| Jogador 2 | 2-1 | 10:06:26 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 2-1 | 10:06:27 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.5800 |  |
| Jogador 2 | 2-1 | 10:06:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 10:06:31 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | 0.2500 |  |
| Jogador 2 | 2-2 | 10:06:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 2-2 | 10:06:34 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | -0.1400 |  |
| Jogador 2 | 2-2 | 10:06:35 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 2-2 | 10:06:36 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-2 | 10:06:36 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-2 | 10:06:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 10:06:40 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Veigar | 0.3200 |  |
| Jogador 2 | 2-3 | 10:06:41 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-3 | 10:06:41 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | — | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-3 | 10:06:42 | MOVE Board -> Board: Veigar (i:4.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | — | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-3 | 10:06:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 2-4 | 10:06:51 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 2-4 | 10:06:52 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Colosso | DA_18_Veigar | 0.3700 |  |
| Jogador 2 | 2-4 | 10:06:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Colosso | DA_18_Veigar | -0.1400 |  |
| Jogador 2 | 2-4 | 10:06:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 1 | Colosso | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-4 | 10:06:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 1 | Colosso | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-4 | 10:06:54 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Colosso | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 2-4 | 10:06:54 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 1 | Colosso | DA_18_Veigar | -0.5500 |  |
| Jogador 2 | 2-4 | 10:06:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 1 | Colosso | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-5 | 10:07:03 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 2-5 | 10:07:04 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 2-5 | 10:07:04 | MOVE Board -> Board: Tristana (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-5 | 10:07:05 | MOVE Board -> Board: Veigar (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.2200 |  |
| Jogador 2 | 2-5 | 10:07:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-6 | 10:07:17 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 2-6 | 10:07:18 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-6 | 10:07:18 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 2-6 | 10:07:19 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-6 | 10:07:19 | MOVE Board -> Board: Veigar (i:4.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-6 | 10:07:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-7 | 10:07:34 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 2-7 | 10:07:34 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Veigar | 0.2100 |  |
| Jogador 2 | 2-7 | 10:07:35 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 2-7 | 10:07:36 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 10:07:36 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-7 | 10:07:37 | MOVE Board -> Board: Vi (i:6.0) <-> Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 10:07:37 | MOVE Board -> Board: Veigar (i:4.0) <-> LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-7 | 10:07:37 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-1 | 10:07:50 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Veigar | 0.7400 |  |
| Jogador 2 | 3-1 | 10:07:51 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-1 | 10:07:51 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 10:07:52 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-2 | 10:08:09 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Veigar | 0.6500 |  |
| Jogador 2 | 3-2 | 10:08:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 10:08:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 10:08:11 | MOVE Board -> Board: Tristana (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-2 | 10:08:12 | MOVE Board -> Board: Vi (i:6.0) <-> Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 10:08:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-3 | 10:08:30 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 3-3 | 10:08:30 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Veigar | 0.6800 |  |
| Jogador 2 | 3-3 | 10:08:31 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-3 | 10:08:31 | MOVE Board -> Board: Veigar (i:4.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 10:08:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-4 | 10:08:52 | MOVE Board -> Board: Tristana (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-4 | 10:08:52 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 3-4 | 10:08:53 | MOVE Board -> Board: Vi (i:6.0) <-> LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-4 | 10:08:53 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-4 | 10:08:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-5 | 10:09:15 | VENDEU: Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-5 | 10:09:15 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_18_Veigar | 0.7300 |  |
| Jogador 2 | 3-5 | 10:09:16 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Colosso | DA_18_Veigar | -0.3900 |  |
| Jogador 2 | 3-5 | 10:09:17 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Colosso | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 3-5 | 10:09:17 | MOVE Board -> Board: Tristana (i:6.0) <-> Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-5 | 10:09:18 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-5 | 10:09:19 | MOVE Board -> Board: Veigar (i:4.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-5 | 10:09:19 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-6 | 10:09:43 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 3-6 | 10:09:43 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Tristana | 0.7800 |  |
| Jogador 2 | 3-6 | 10:09:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Tristana | -0.0500 |  |
| Jogador 2 | 3-6 | 10:09:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_18_Tristana | 0.3400 |  |
| Jogador 2 | 3-6 | 10:09:45 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 3-6 | 10:09:45 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 3-6 | 10:09:46 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_18_Tristana | -0.0600 |  |
| Jogador 2 | 3-7 | 10:10:07 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Tristana | 0.1700 |  |
| Jogador 2 | 3-7 | 10:10:08 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Tristana | 0.2200 |  |
| Jogador 2 | 3-7 | 10:10:08 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 3-7 | 10:10:09 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 3-7 | 10:10:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_18_Tristana | -0.1100 |  |
| Jogador 2 | 4-1 | 10:10:33 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Colosso | DA_18_Tristana | 0.3700 |  |
| Jogador 2 | 4-1 | 10:10:34 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 4-1 | 10:10:34 | MOVE Board -> Board: Vi (i:6.0) <-> Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 4-1 | 10:10:35 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Colosso | DA_18_Tristana | -0.1800 |  |
| Jogador 2 | 4-2 | 10:11:01 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Colosso | DA_18_Tristana | 0.7400 |  |
| Jogador 2 | 4-2 | 10:11:02 | MOVE Board -> Board: Veigar (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 4-2 | 10:11:02 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 4-2 | 10:11:03 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 4-2 | 10:11:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Colosso | DA_18_Tristana | -0.0400 |  |
| Jogador 2 | 4-3 | 10:11:29 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_18_Tristana | -0.1400 |  |
| Jogador 2 | 4-3 | 10:11:30 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 4-3 | 10:11:30 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 4-3 | 10:11:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Colosso | DA_18_Tristana | -0.0500 |  |
| Jogador 2 | 4-4 | 10:11:58 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Colosso | DA_18_Tristana | 0.2800 |  |
| Jogador 2 | 4-4 | 10:11:58 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Colosso | DA_18_Tristana | 0.1000 |  |
| Jogador 2 | 4-4 | 10:11:59 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 4-4 | 10:11:59 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 4-4 | 10:12:00 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 47 | 4 | Colosso | DA_18_Tristana | -0.0500 |  |
| Jogador 2 | 4-5 | 10:12:26 | VENDEU: Elise (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 4 | Colosso | DA_18_Tristana | -0.4800 |  |
| Jogador 2 | 4-5 | 10:12:27 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 4 | Colosso | DA_18_Tristana | 0.8300 |  |
| Jogador 2 | 4-5 | 10:12:27 | VENDEU: Tristana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 4 | Colosso | DA_18_Veigar | -0.5900 |  |
| Jogador 2 | 4-5 | 10:12:28 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 4 | Colosso | DA_18_Veigar | 0.8900 |  |
| Jogador 2 | 4-5 | 10:12:28 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 4 | Colosso | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 4-5 | 10:12:29 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 4 | Colosso | DA_18_Veigar | 0.8800 |  |
| Jogador 2 | 4-5 | 10:12:29 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 4 | Colosso | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 4-5 | 10:12:29 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 4 | Colosso | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-5 | 10:12:30 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 4 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-6 | 10:12:58 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Colosso | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 4-6 | 10:12:59 | VENDEU: Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Colosso | DA_18_Veigar | -0.5900 |  |
| Jogador 2 | 4-6 | 10:12:59 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Aronguejo (i:4.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Colosso | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 4-6 | 10:13:00 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Aronguejo (i:4.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Colosso | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 4-6 | 10:13:00 | VENDEU: LeBlanc (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Colosso | DA_18_Veigar | -0.6400 |  |
| Jogador 2 | 4-6 | 10:13:01 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Colosso | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 4-6 | 10:13:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Colosso | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-6 | 10:13:01 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Colosso | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-6 | 10:13:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Colosso | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 4-7 | 10:13:34 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Colosso | DA_18_Veigar | 0.2500 |  |
| Jogador 2 | 4-7 | 10:13:34 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Colosso | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 4-7 | 10:13:35 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Malphite (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Colosso | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 4-7 | 10:13:35 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 74 | 5 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-7 | 10:13:36 | COMPROU: Lux (Sabugueiro) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Colosso | DA_18_Veigar | -0.2100 |  |
| Jogador 2 | 4-7 | 10:13:36 | MOVE Bench -> Board: Lux (Sabugueiro) (i:10.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Colosso | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 4-7 | 10:13:37 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-7 | 10:13:38 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Colosso | DA_18_Veigar | -0.1700 |  |
| Jogador 2 | 4-7 | 10:13:39 | MOVE Board -> Board: Lux (Sabugueiro) (i:10.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 66 | 5 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-1 | 10:14:09 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-1 | 10:14:09 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-1 | 10:14:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Colosso | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 5-2 | 10:14:43 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Colosso | DA_18_Veigar | 0.8900 |  |
| Jogador 2 | 5-2 | 10:14:43 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-2 | 10:14:44 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Colosso | DA_18_Veigar | 0.6100 |  |
| Jogador 2 | 5-2 | 10:14:44 | MOVE Board -> Board: Warwick (i:4.0) <-> Lux (Sabugueiro) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-2 | 10:14:45 | MOVE Board -> Board: Lux (Sabugueiro) (i:10.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-2 | 10:14:45 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Colosso | DA_18_Veigar | -0.1500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-3 | 10:15:18 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Colosso | DA_18_Veigar | -0.4800 |  |
| Jogador 2 | 5-3 | 10:15:19 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Colosso | DA_18_Veigar | 1.0200 |  |
| Jogador 2 | 5-3 | 10:15:19 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Colosso | DA_18_Veigar | 1.0200 |  |
| Jogador 2 | 5-3 | 10:15:20 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Colosso | DA_18_Veigar | 0.6700 |  |
| Jogador 2 | 5-3 | 10:15:20 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-3 | 10:15:21 | MOVE Board -> Board: Vi (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-3 | 10:15:21 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Colosso | DA_18_Veigar | -0.3100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-4 | 10:15:57 | MOVE Board -> Board: Veigar (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Colosso | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 5-4 | 10:15:57 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Colosso | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 5-4 | 10:15:58 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Colosso | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 5-4 | 10:15:58 | MOVE Board -> Board: Lux (Sabugueiro) (i:10.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-4 | 10:15:59 | MOVE Board -> Board: Warwick (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-4 | 10:15:59 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Colosso | DA_18_Veigar | -0.3200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-5 | 10:16:35 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Colosso | DA_18_Veigar | 0.9300 |  |
| Jogador 2 | 5-5 | 10:16:35 | VENDEU: Veigar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Colosso | DA_18_Veigar | -0.9500 |  |
| Jogador 2 | 5-5 | 10:16:36 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Colosso | DA_18_Azir | 1.0500 |  |
| Jogador 2 | 5-5 | 10:16:36 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Colosso | DA_18_Azir | -0.0700 |  |
| Jogador 2 | 5-5 | 10:16:36 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Colosso | DA_18_Azir | 0.4300 |  |
| Jogador 2 | 5-5 | 10:16:37 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_18_Azir | -0.0600 |  |
| Jogador 2 | 5-5 | 10:16:37 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Colosso | DA_18_Azir | -0.0700 |  |
| Jogador 2 | 5-5 | 10:16:38 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Colosso | DA_18_Azir | -0.0700 |  |
| Jogador 2 | 5-5 | 10:16:38 | VENDEU: Yorick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Colosso | DA_18_Azir | -0.7000 |  |
| Jogador 2 | 5-6 | 10:17:12 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Colosso | DA_18_Azir | 0.9800 |  |
| Jogador 2 | 5-6 | 10:17:14 | VENDEU: Azir (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Colosso | DA_18_Azir | -0.7400 |  |
| Jogador 2 | 5-6 | 10:17:14 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_Vi18 | 1.1000 |  |
| Jogador 2 | 5-6 | 10:17:15 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_Vi18 | 0.4300 |  |
| Jogador 2 | 5-6 | 10:17:15 | MOVE Bench -> Board: Vi (i:12.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_Vi18 | 0.6000 |  |
| Jogador 2 | 5-6 | 10:17:16 | MOVE Board -> Board: Vi (i:12.0) <-> Lux (Sabugueiro) (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 2 | 5-6 | 10:17:16 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Colosso | DA_Vi18 | 0.0600 |  |
| Jogador 2 | 5-6 | 10:17:17 | MOVE Board -> Board: Lux (Sabugueiro) (i:10.0) <-> Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Colosso | DA_Vi18 | 0.0100 |  |
| Jogador 2 | 5-6 | 10:17:17 | MOVE Board -> Board: Warwick (i:4.0) <-> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 2 | 5-7 | 10:18:02 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Colosso | DA_Vi18 | 0.9500 |  |
| Jogador 2 | 5-7 | 10:18:02 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Aronguejo (i:4.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Colosso | DA_Vi18 | 0.1100 |  |
| Jogador 2 | 5-7 | 10:18:02 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 2 | 5-7 | 10:18:03 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Colosso | DA_Vi18 | -0.0300 |  |
| Jogador 2 | 5-7 | 10:18:03 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Colosso | DA_Vi18 | 1.0000 |  |
| Jogador 2 | 5-7 | 10:18:04 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Colosso | DA_Vi18 | -0.0700 |  |
| Jogador 2 | 5-7 | 10:18:04 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_Vi18 | 1.1100 |  |
| Jogador 2 | 5-7 | 10:18:05 | MOVE Bench -> Board: Ahri (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_Vi18 | 0.2300 |  |
| Jogador 2 | 5-7 | 10:18:05 | EQUIP_FROM_INVENTORY: TFT_Item_BrambleVest -> Vi (i:12.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Colosso | DA_Vi18 | 0.1100 |  |
| Jogador 3 | ? | 10:05:44 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | ? | 10:05:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 10:05:50 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 10:05:51 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 10:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 10:05:56 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 1-2 | 10:05:58 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 10:05:58 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 10:05:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 10:06:03 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 1-3 | 10:06:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 10:06:11 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.7100 |  |
| Jogador 3 | 1-4 | 10:06:13 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 3 | 1-4 | 10:06:14 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 1-4 | 10:06:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 10:06:18 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 2-1 | 10:06:22 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 2-1 | 10:06:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 10:06:31 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | 2-2 | 10:06:31 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | 2-2 | 10:06:34 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 2-2 | 10:06:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 2-3 | 10:06:40 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_Akali_AD | 1.1100 |  |
| Jogador 3 | 2-3 | 10:06:41 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 2-3 | 10:06:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | — | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 2-3 | 10:06:42 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 2-3 | 10:06:46 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 2-4 | 10:06:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Devastador | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 2-4 | 10:06:52 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Devastador | DA_18_Akali_AD | 0.2800 |  |
| Jogador 3 | 2-4 | 10:06:52 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 10:06:53 | MOVE Board -> Board: Diana (i:6.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-4 | 10:06:53 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-4 | 10:06:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Devastador | DA_18_Akali_AD | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 2-5 | 10:07:03 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Devastador | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 2-5 | 10:07:04 | MOVE Board -> Board: Shen (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 10:07:04 | MOVE Board -> Board: Diana (i:6.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-5 | 10:07:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Devastador | DA_18_Akali_AD | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 2-6 | 10:07:17 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Devastador | DA_18_Akali_AD | 0.9800 |  |
| Jogador 3 | 2-6 | 10:07:18 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Devastador | DA_18_Akali_AD | 0.3600 |  |
| Jogador 3 | 2-6 | 10:07:18 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-6 | 10:07:19 | MOVE Board -> Board: Tristana (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 10:07:19 | MOVE Board -> Board: Shen (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 10:07:20 | MOVE Board -> Board: Diana (i:6.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 10:07:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Devastador | DA_18_Akali_AD | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 2-7 | 10:07:34 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Devastador | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 2-7 | 10:07:34 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Akali_AD | 0.3100 |  |
| Jogador 3 | 2-7 | 10:07:35 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 10:07:36 | MOVE Board -> Board: Diana (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-7 | 10:07:36 | MOVE Board -> Board: Tristana (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Akali_AD | -0.2900 |  |
| Jogador 3 | 2-7 | 10:07:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Akali_AD | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-1 | 10:07:50 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Devastador | DA_18_Akali_AD | 0.8500 |  |
| Jogador 3 | 3-1 | 10:07:51 | MOVE Board -> Board: Shen (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 10:07:51 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Devastador | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 3-1 | 10:07:52 | MOVE Board -> Board: Tristana (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-1 | 10:07:53 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 3-1 | 10:07:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Devastador | DA_18_Akali_AD | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-2 | 10:08:09 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Devastador | DA_18_Akali_AD | 0.3600 |  |
| Jogador 3 | 3-2 | 10:08:10 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Devastador | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 3-2 | 10:08:10 | MOVE Board -> Board: Diana (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-2 | 10:08:11 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-2 | 10:08:12 | MOVE Board -> Board: Tristana (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 10:08:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Devastador | DA_18_Akali_AD | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-3 | 10:08:30 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Devastador | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 3-3 | 10:08:30 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 10:08:31 | MOVE Board -> Board: Diana (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 10:08:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Devastador | DA_18_Akali_AD | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-4 | 10:08:52 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 75 | 5 | Devastador | DA_18_Akali_AD | -0.4500 |  |
| Jogador 3 | 3-4 | 10:08:52 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Devastador | DA_18_Akali_AD | 0.3200 |  |
| Jogador 3 | 3-4 | 10:08:53 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 10:08:53 | MOVE Board -> Board: Tristana (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-4 | 10:08:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Devastador | DA_18_Akali_AD | -0.0700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-5 | 10:09:15 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 85 | 5 | Devastador | DA_18_Akali_AD | -0.5900 |  |
| Jogador 3 | 3-5 | 10:09:15 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 84 | 5 | Devastador | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 3-5 | 10:09:16 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 86 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-5 | 10:09:17 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 85 | 5 | Devastador | DA_18_Akali_AD | 0.8500 |  |
| Jogador 3 | 3-5 | 10:09:17 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 85 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 10:09:18 | MOVE Board -> Board: Diana (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 85 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-5 | 10:09:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 85 | 5 | Devastador | DA_18_Akali_AD | -0.0700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-6 | 10:09:43 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Devastador | DA_18_Akali_AD | 0.4400 |  |
| Jogador 3 | 3-6 | 10:09:43 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Devastador | DA_18_Akali_AD | -0.2200 |  |
| Jogador 3 | 3-6 | 10:09:44 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 10:09:44 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-6 | 10:09:45 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Devastador | DA_18_Akali_AD | -0.0800 |  |
| Jogador 3 | 3-7 | 10:10:07 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Devastador | DA_18_Akali_AD | 0.0600 |  |
| Jogador 3 | 3-7 | 10:10:08 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_TearOfTheGoddess -> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Devastador | DA_18_Akali_AD | 0.1800 |  |
| Jogador 3 | 3-7 | 10:10:08 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 106 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-7 | 10:10:09 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Devastador | DA_18_Akali_AD | 0.8000 |  |
| Jogador 3 | 3-7 | 10:10:09 | MOVE Board -> Board: Tristana (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-7 | 10:10:10 | MOVE Board -> Board: Diana (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-7 | 10:10:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Devastador | DA_18_Akali_AD | -0.1200 |  |
| Jogador 3 | 4-1 | 10:10:33 | VENDEU: Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 114 | 5 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 4-1 | 10:10:34 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Devastador | DA_18_Akali_AD | 0.8200 |  |
| Jogador 3 | 4-1 | 10:10:34 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 114 | 5 | Devastador | DA_18_Akali_AD | -0.4000 |  |
| Jogador 3 | 4-1 | 10:10:35 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Devastador | DA_18_Akali_AD | 0.6300 |  |
| Jogador 3 | 4-1 | 10:10:36 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 10:10:36 | MOVE Board -> Board: Shen (i:4.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-1 | 10:10:37 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-1 | 10:10:37 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Devastador | DA_18_Akali_AD | -0.1200 |  |
| Jogador 3 | 4-2 | 10:11:01 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 125 | 5 | Devastador | DA_18_Akali_AD | -0.5100 |  |
| Jogador 3 | 4-2 | 10:11:02 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | -0.1300 |  |
| Jogador 3 | 4-2 | 10:11:02 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 4-2 | 10:11:03 | MOVE Bench -> Board: Warwick (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | 0.3500 |  |
| Jogador 3 | 4-2 | 10:11:03 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 4-2 | 10:11:04 | MOVE Bench -> Board: Tristana (i:6.0) <-> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | -1.0700 |  |
| Jogador 3 | 4-2 | 10:11:04 | MOVE Bench -> Board: Warwick (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | 0.3500 |  |
| Jogador 3 | 4-2 | 10:11:04 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | 0.0400 |  |
| Jogador 3 | 4-2 | 10:11:05 | MOVE Bench -> Board: Tristana (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | -0.7900 |  |
| Jogador 3 | 4-3 | 10:11:29 | MOVE Bench -> Board: Diana (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Devastador | DA_18_Akali_AD | 0.1900 |  |
| Jogador 3 | 4-3 | 10:11:30 | MOVE Bench -> Board: Shen (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Devastador | DA_18_Akali_AD | -0.7600 |  |
| Jogador 3 | 4-3 | 10:11:30 | MOVE Bench -> Board: Diana (i:6.0) <-> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Devastador | DA_18_Akali_AD | 0.0400 |  |
| Jogador 3 | 4-3 | 10:11:31 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 137 | 5 | Devastador | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-3 | 10:11:31 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Devastador | DA_18_Akali_AD | -0.2800 |  |
| Jogador 3 | 4-3 | 10:11:32 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 10:11:32 | MOVE Board -> Board: Tristana (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-3 | 10:11:32 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-3 | 10:11:33 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Devastador | DA_18_Akali_AD | -0.1400 |  |
| Jogador 3 | 4-4 | 10:11:58 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 148 | 5 | Devastador | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-4 | 10:11:58 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 146 | 5 | Devastador | DA_18_Akali_AD | 0.8200 |  |
| Jogador 3 | 4-4 | 10:11:59 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Devastador | DA_18_Akali_AD | -0.9600 |  |
| Jogador 3 | 4-4 | 10:11:59 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 144 | 5 | Devastador | DA_KogMaw18_AD | 0.8900 |  |
| Jogador 3 | 4-4 | 10:12:00 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Devastador | DA_KogMaw18_AD | 0.4900 |  |
| Jogador 3 | 4-4 | 10:12:00 | MOVE Board -> Board: Warwick (i:4.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Devastador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 10:12:00 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Devastador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 10:12:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Devastador | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 3 | 4-5 | 10:12:26 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 153 | 5 | Devastador | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 3 | 4-5 | 10:12:27 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 150 | 5 | Devastador | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 3 | 4-5 | 10:12:27 | MOVE Board -> Board: Diana (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 150 | 5 | Devastador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 3 | 4-5 | 10:12:28 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 150 | 5 | Devastador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 4-5 | 10:12:28 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 150 | 5 | Devastador | DA_KogMaw18_AD | -0.6500 |  |
| Jogador 3 | 4-5 | 10:12:29 | MOVE Bench -> Board: Shen (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 150 | 5 | Devastador | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 3 | 4-5 | 10:12:29 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 150 | 5 | Devastador | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 3 | 4-6 | 10:12:58 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 169 | 5 | Devastador | DA_18_Akali_AD | -0.6000 |  |
| Jogador 3 | 4-6 | 10:12:59 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 167 | 5 | Devastador | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 4-6 | 10:12:59 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Devastador | DA_18_Akali_AD | 0.6000 |  |
| Jogador 3 | 4-6 | 10:13:00 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Akali (i:2.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Devastador | DA_18_Akali_AD | 0.1700 |  |
| Jogador 3 | 4-6 | 10:13:00 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Akali (i:2.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Devastador | DA_18_Akali_AD | 0.1200 |  |
| Jogador 3 | 4-6 | 10:13:01 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 164 | 5 | Devastador | DA_18_Akali_AD | -0.2200 |  |
| Jogador 3 | 4-6 | 10:13:01 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 164 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-6 | 10:13:01 | MOVE Bench -> Board: Rengar (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 164 | 5 | Devastador | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | 4-6 | 10:13:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 164 | 5 | Devastador | DA_18_Akali_AD | -0.1700 |  |
| Jogador 3 | 4-7 | 10:13:34 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Devastador | DA_18_Akali_AD | 0.3500 |  |
| Jogador 3 | 4-7 | 10:13:34 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Devastador | DA_18_Akali_AD | 0.2000 |  |
| Jogador 3 | 4-7 | 10:13:35 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Devastador | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 4-7 | 10:13:35 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Devastador | DA_18_Akali_AD | -0.6400 |  |
| Jogador 3 | 4-7 | 10:13:36 | MOVE Bench -> Board: Shen (i:4.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Devastador | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 4-7 | 10:13:36 | MOVE Bench -> Board: Rengar (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Devastador | DA_18_Akali_AD | -0.2000 |  |
| Jogador 3 | 4-7 | 10:13:37 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Devastador | DA_18_Akali_AD | -0.6500 |  |
| Jogador 3 | 4-7 | 10:13:38 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 172 | 5 | Devastador | DA_18_Akali_AD | -0.1900 |  |
| Jogador 3 | 5-1 | 10:14:09 | MOVE Bench -> Board: Diana (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 182 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 5-1 | 10:14:09 | VENDEU: Lobo Trevoguari (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 187 | 5 | Devastador | DA_18_Akali_AD | -0.6000 |  |
| Jogador 3 | 5-1 | 10:14:10 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 185 | 5 | Devastador | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 5-1 | 10:14:10 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 185 | 5 | Devastador | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 5-1 | 10:14:11 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 185 | 5 | Devastador | DA_18_Akali_AD | -0.6500 |  |
| Jogador 3 | 5-1 | 10:14:11 | MOVE Bench -> Board: Shen (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 185 | 5 | Devastador | DA_18_Akali_AD | -0.7200 |  |
| Jogador 3 | 5-1 | 10:14:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 185 | 5 | Devastador | DA_18_Akali_AD | -0.3700 |  |
| Jogador 3 | 5-2 | 10:14:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 193 | 5 | Devastador | DA_18_Akali_AD | 0.6300 |  |
| Jogador 3 | 5-2 | 10:14:43 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 193 | 5 | Devastador | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 5-2 | 10:14:44 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 193 | 5 | Devastador | DA_18_Akali_AD | -0.7200 |  |
| Jogador 3 | 5-2 | 10:14:44 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 193 | 5 | Devastador | DA_18_Akali_AD | -0.4200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 5-3 | 10:15:18 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 202 | 5 | Devastador | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 5-3 | 10:15:19 | VENDEU: Warwick (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 207 | 5 | Devastador | DA_18_Akali_AD | -0.5900 |  |
| Jogador 3 | 5-3 | 10:15:19 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 205 | 5 | Devastador | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 5-3 | 10:15:20 | MOVE Bench -> Board: Shen (i:4.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 205 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 5-3 | 10:15:20 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 205 | 5 | Devastador | DA_18_Akali_AD | -0.1200 |  |
| Jogador 3 | 5-3 | 10:15:21 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 205 | 5 | Devastador | DA_18_Akali_AD | -0.7500 |  |
| Jogador 3 | 5-3 | 10:15:21 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 205 | 5 | Devastador | DA_18_Akali_AD | -0.4300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 5-4 | 10:15:57 | MOVE Bench -> Board: Shen (i:4.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 216 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 5-4 | 10:15:57 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 216 | 5 | Devastador | DA_18_Akali_AD | -0.1200 |  |
| Jogador 3 | 5-4 | 10:15:58 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 216 | 5 | Devastador | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 5-4 | 10:15:58 | MOVE Bench -> Board: Rengar (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 216 | 5 | Devastador | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 5-4 | 10:15:59 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 216 | 5 | Devastador | DA_18_Akali_AD | -0.7500 |  |
| Jogador 3 | 5-4 | 10:15:59 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 216 | 5 | Devastador | DA_18_Akali_AD | -0.2900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 5-5 | 10:16:35 | MOVE Bench -> Board: Shen (i:4.0) <-> Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 227 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 5-5 | 10:16:35 | MOVE Bench -> Board: Rengar (i:6.0) <-> Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 227 | 5 | Devastador | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 5-5 | 10:16:36 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 227 | 5 | Devastador | DA_18_Akali_AD | -0.7500 |  |
| Jogador 3 | 5-5 | 10:16:36 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 227 | 5 | Devastador | DA_18_Akali_AD | -0.6600 |  |
| Jogador 4 | ? | 10:05:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5900 |  |
| Jogador 4 | ? | 10:05:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 10:05:50 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 10:05:51 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 10:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 10:05:56 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1700 |  |
| Jogador 4 | 1-2 | 10:05:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 10:06:03 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4000 |  |
| Jogador 4 | 1-3 | 10:06:05 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 10:06:06 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 10:06:06 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 10:06:07 | MOVE Board -> Board: Yorick (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-3 | 10:06:07 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-3 | 10:06:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 10:06:13 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 4 | 1-4 | 10:06:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 10:06:18 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | -0.0700 |  |
| Jogador 4 | 2-1 | 10:06:22 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 4 | 2-1 | 10:06:24 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-1 | 10:06:25 | MOVE Board -> Board: Camille (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 2-1 | 10:06:26 | MOVE Board -> Board: Camille (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 2-1 | 10:06:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-2 | 10:06:31 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Camille | 1.1100 |  |
| Jogador 4 | 2-2 | 10:06:31 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Camille | 0.2200 |  |
| Jogador 4 | 2-2 | 10:06:34 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Camille | 0.1800 |  |
| Jogador 4 | 2-2 | 10:06:35 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Camille | 0.0000 |  |
| Jogador 4 | 2-2 | 10:06:36 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Camille | 0.7600 |  |
| Jogador 4 | 2-2 | 10:06:36 | MOVE Bench -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Camille | 0.4000 |  |
| Jogador 4 | 2-2 | 10:06:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Camille | -0.0100 |  |
| Jogador 4 | 2-3 | 10:06:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 20 | 1 | — | DA_18_Camille | 0.0000 |  |
| Jogador 4 | 2-3 | 10:06:41 | COMPROU: Diana (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 17 | 1 | — | DA_18_Camille | 0.1500 |  |
| Jogador 4 | 2-3 | 10:06:41 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 17 | 1 | — | DA_18_Camille | 0.0000 |  |
| Jogador 4 | 2-3 | 10:06:42 | BUY XP | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 13 | 1 | — | DA_18_Camille | 0.0400 |  |
| Jogador 4 | 2-3 | 10:06:46 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 13 | 1 | — | DA_18_Camille | 0.4000 |  |
| Jogador 4 | 2-4 | 10:06:51 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 17 | 1 | Colosso | DA_18_Camille | 0.1500 |  |
| Jogador 4 | 2-4 | 10:06:52 | MOVE Board -> Board: Diana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Camille | 0.0000 |  |
| Jogador 4 | 2-4 | 10:06:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Camille | -0.0100 |  |
| Jogador 4 | 2-4 | 10:06:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Camille | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 2-5 | 10:07:03 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Camille | 0.0000 |  |
| Jogador 4 | 2-5 | 10:07:04 | MOVE Board -> Board: Yorick (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Camille | -0.0200 |  |
| Jogador 4 | 2-5 | 10:07:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Camille | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 2-6 | 10:07:17 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_18_Camille | 1.0200 |  |
| Jogador 4 | 2-6 | 10:07:18 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-6 | 10:07:18 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_18_Camille | 0.2800 |  |
| Jogador 4 | 2-6 | 10:07:19 | MOVE Board -> Board: Diana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_18_Camille | 0.0000 |  |
| Jogador 4 | 2-6 | 10:07:19 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_18_Camille | -0.0100 |  |
| Jogador 4 | 2-6 | 10:07:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_18_Camille | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 2-7 | 10:07:34 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Colosso | DA_18_Camille | 0.8900 |  |
| Jogador 4 | 2-7 | 10:07:34 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Colosso | DA_18_Camille | 0.2400 |  |
| Jogador 4 | 2-7 | 10:07:35 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Colosso | DA_18_Camille | 0.4500 |  |
| Jogador 4 | 2-7 | 10:07:36 | MOVE Board -> Board: Camille (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Colosso | DA_18_Camille | -0.0100 |  |
| Jogador 4 | 2-7 | 10:07:36 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Colosso | DA_18_Camille | -0.0300 |  |
| Jogador 4 | 2-7 | 10:07:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Colosso | DA_18_Camille | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-1 | 10:07:50 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_18_Camille | 0.8500 |  |
| Jogador 4 | 3-1 | 10:07:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_18_Camille | 0.9000 |  |
| Jogador 4 | 3-1 | 10:07:51 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 3-1 | 10:07:52 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_18_Camille | 0.5900 |  |
| Jogador 4 | 3-1 | 10:07:53 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_18_Camille | 0.3500 |  |
| Jogador 4 | 3-1 | 10:07:53 | MOVE Board -> Board: Rakan (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_18_Camille | 0.0000 |  |
| Jogador 4 | 3-1 | 10:07:54 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_18_Camille | -0.0200 |  |
| Jogador 4 | 3-1 | 10:07:54 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_18_Camille | -0.0100 |  |
| Jogador 4 | 3-1 | 10:07:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_18_Camille | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-2 | 10:08:09 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Colosso | DA_18_Camille | 0.3400 |  |
| Jogador 4 | 3-2 | 10:08:10 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Colosso | DA_18_Camille | 0.3200 |  |
| Jogador 4 | 3-2 | 10:08:10 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Colosso | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 3-2 | 10:08:11 | MOVE Board -> Board: Camille (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Colosso | DA_18_Camille | 0.0000 |  |
| Jogador 4 | 3-2 | 10:08:12 | MOVE Board -> Board: Rakan (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Colosso | DA_18_Camille | -0.0200 |  |
| Jogador 4 | 3-2 | 10:08:12 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Colosso | DA_18_Camille | -0.0100 |  |
| Jogador 4 | 3-2 | 10:08:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Colosso | DA_18_Camille | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-3 | 10:08:30 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Colosso | DA_18_Camille | 0.8500 |  |
| Jogador 4 | 3-3 | 10:08:30 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Colosso | DA_18_Camille | -0.0100 |  |
| Jogador 4 | 3-3 | 10:08:31 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Colosso | DA_18_Camille | -0.7200 |  |
| Jogador 4 | 3-3 | 10:08:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Colosso | DA_18_Camille | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-4 | 10:08:52 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Colosso | DA_18_Camille | -0.5900 |  |
| Jogador 4 | 3-4 | 10:08:52 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Colosso | DA_18_Camille | 0.9000 |  |
| Jogador 4 | 3-4 | 10:08:53 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Colosso | DA_18_Camille | 0.4000 |  |
| Jogador 4 | 3-4 | 10:08:53 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Colosso | DA_18_Camille | -0.5000 |  |
| Jogador 4 | 3-4 | 10:08:54 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Colosso | DA_18_Camille | 0.5800 |  |
| Jogador 4 | 3-4 | 10:08:54 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Colosso | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 3-4 | 10:08:55 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 3-4 | 10:08:55 | MOVE Bench -> Board: Rakan (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_18_Camille | 0.0800 |  |
| Jogador 4 | 3-4 | 10:08:55 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_18_Camille | -0.0100 |  |
| Jogador 4 | 3-5 | 10:09:15 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Colosso | DA_18_Camille | -0.8100 |  |
| Jogador 4 | 3-5 | 10:09:15 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_18_Camille | 0.9000 |  |
| Jogador 4 | 3-5 | 10:09:16 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_18_Camille | -0.4000 |  |
| Jogador 4 | 3-5 | 10:09:17 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_18_Camille | 0.0800 |  |
| Jogador 4 | 3-5 | 10:09:17 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_18_Camille | -0.1800 |  |
| Jogador 4 | 3-5 | 10:09:18 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_18_Camille | -0.4100 |  |
| Jogador 4 | 3-5 | 10:09:19 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_18_Camille | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-6 | 10:09:43 | MOVE Bench -> Board: Rakan (i:2.0) <-> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Colosso | DA_18_Camille | 0.1000 |  |
| Jogador 4 | 3-6 | 10:09:43 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Colosso | DA_18_Camille | -0.1100 |  |
| Jogador 4 | 3-6 | 10:09:44 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Colosso | DA_18_Camille | 0.8800 |  |
| Jogador 4 | 3-6 | 10:09:44 | MOVE Bench -> Board: Vi (i:6.0) <-> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Colosso | DA_18_Camille | -0.0300 |  |
| Jogador 4 | 3-6 | 10:09:45 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Colosso | DA_18_Camille | -0.4100 |  |
| Jogador 4 | 3-6 | 10:09:45 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Colosso | DA_18_Camille | -0.5300 |  |
| Jogador 4 | 3-7 | 10:10:07 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Colosso | DA_18_Camille | 0.1400 |  |
| Jogador 4 | 3-7 | 10:10:08 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Colosso | DA_18_Camille | 0.1800 |  |
| Jogador 4 | 3-7 | 10:10:08 | VENDEU: Yorick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Colosso | DA_18_Camille | -0.6900 |  |
| Jogador 4 | 3-7 | 10:10:09 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Colosso | DA_18_Camille | 0.9900 |  |
| Jogador 4 | 3-7 | 10:10:09 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Rakan (i:4.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Colosso | DA_18_Camille | 0.1600 |  |
| Jogador 4 | 3-7 | 10:10:10 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Colosso | DA_18_Camille | 0.0000 |  |
| Jogador 4 | 3-7 | 10:10:10 | MOVE Board -> Board: Rakan (i:4.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Colosso | DA_18_Camille | -0.0100 |  |
| Jogador 4 | 3-7 | 10:10:11 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Colosso | DA_18_Camille | -0.5000 |  |
| Jogador 4 | 4-1 | 10:10:33 | VENDEU: Camille (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Colosso | DA_18_Rakan | -0.6800 |  |
| Jogador 4 | 4-1 | 10:10:34 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Colosso | DA_18_Rakan | 0.2800 |  |
| Jogador 4 | 4-1 | 10:10:34 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 4-1 | 10:10:35 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Colosso | DA_18_Rakan | -0.4100 |  |
| Jogador 4 | 4-1 | 10:10:36 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Colosso | DA_18_Rakan | -0.5400 |  |
| Jogador 5 | ? | 10:05:44 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.5700 |  |
| Jogador 5 | ? | 10:05:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 10:05:50 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 10:05:51 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 10:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 10:05:56 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1800 |  |
| Jogador 5 | 1-2 | 10:05:58 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1900 |  |
| Jogador 5 | 1-2 | 10:05:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-2 | 10:06:03 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4000 |  |
| Jogador 5 | 1-3 | 10:06:05 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 10:06:06 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 10:06:06 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0400 |  |
| Jogador 5 | 1-3 | 10:06:07 | MOVE Board -> Board: Veigar (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-3 | 10:06:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 10:06:13 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 10:06:14 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.1900 |  |
| Jogador 5 | 1-4 | 10:06:16 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2400 |  |
| Jogador 5 | 1-4 | 10:06:16 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2100 |  |
| Jogador 5 | 1-4 | 10:06:17 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.4300 |  |
| Jogador 5 | 1-4 | 10:06:17 | MOVE Board -> Board: Sejuani (i:4.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0200 |  |
| Jogador 5 | 1-4 | 10:06:18 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.1300 |  |
| Jogador 5 | 1-4 | 10:06:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 10:06:22 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9300 |  |
| Jogador 5 | 2-1 | 10:06:24 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-1 | 10:06:25 | MOVE Board -> Board: Yorick (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | -0.0200 |  |
| Jogador 5 | 2-1 | 10:06:26 | MOVE Board -> Board: Sejuani (i:4.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-1 | 10:06:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 10:06:31 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 0.9300 |  |
| Jogador 5 | 2-2 | 10:06:31 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 0.1400 |  |
| Jogador 5 | 2-2 | 10:06:34 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 5 | 2-2 | 10:06:35 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 5 | 2-2 | 10:06:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.0400 |  |
| Jogador 5 | 2-2 | 10:06:36 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.2300 |  |
| Jogador 5 | 2-2 | 10:06:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0500 |  |
| Jogador 5 | 2-3 | 10:06:40 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.2700 |  |
| Jogador 5 | 2-3 | 10:06:41 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Cassiopeia | -0.0500 |  |
| Jogador 5 | 2-3 | 10:06:41 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | 0.2000 |  |
| Jogador 5 | 2-3 | 10:06:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-3 | 10:06:46 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.4000 |  |
| Jogador 5 | 2-4 | 10:06:51 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-4 | 10:06:52 | MOVE Board -> Board: Kobuko (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-4 | 10:06:52 | MOVE Board -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 2-4 | 10:06:53 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 10:06:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-5 | 10:07:03 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-5 | 10:07:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0500 |  |
| Jogador 5 | 2-5 | 10:07:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.5500 |  |
| Jogador 5 | 2-5 | 10:07:05 | MOVE Board -> Board: Yunara (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-5 | 10:07:05 | MOVE Board -> Board: Sejuani (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 2-5 | 10:07:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 2-6 | 10:07:17 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Enfeitiçador | DA_18_Cassiopeia | -0.0200 |  |
| Jogador 5 | 2-6 | 10:07:18 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_Cassiopeia | 0.9100 |  |
| Jogador 5 | 2-6 | 10:07:18 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-6 | 10:07:19 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Enfeitiçador | DA_18_Cassiopeia | 0.8100 |  |
| Jogador 5 | 2-6 | 10:07:19 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Enfeitiçador | DA_18_Yunara | -0.0200 |  |
| Jogador 5 | 2-6 | 10:07:20 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_18_RekSai | 0.9400 |  |
| Jogador 5 | 2-6 | 10:07:21 | MOVE Board -> Board: Kobuko (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_18_RekSai | 0.0000 |  |
| Jogador 5 | 2-6 | 10:07:21 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_18_RekSai | -0.0300 |  |
| Jogador 5 | 2-6 | 10:07:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_18_RekSai | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 2-7 | 10:07:34 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_RekSai | 0.8500 |  |
| Jogador 5 | 2-7 | 10:07:34 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_RekSai | 0.1100 |  |
| Jogador 5 | 2-7 | 10:07:35 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_RekSai | 0.4400 |  |
| Jogador 5 | 2-7 | 10:07:36 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_RekSai | -0.0600 |  |
| Jogador 5 | 2-7 | 10:07:36 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_RekSai | -0.2600 |  |
| Jogador 5 | 2-7 | 10:07:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_RekSai | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-1 | 10:07:50 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_18_RekSai | 0.8400 |  |
| Jogador 5 | 3-1 | 10:07:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_18_RekSai | 0.8700 |  |
| Jogador 5 | 3-1 | 10:07:51 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_18_RekSai | 0.5700 |  |
| Jogador 5 | 3-1 | 10:07:52 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_RekSai | 0.0700 |  |
| Jogador 5 | 3-1 | 10:07:53 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_RekSai | 0.0400 |  |
| Jogador 5 | 3-1 | 10:07:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_RekSai | -0.0100 |  |
| Jogador 5 | 3-1 | 10:07:54 | MOVE Board -> Board: Kobuko (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_RekSai | -0.0100 |  |
| Jogador 5 | 3-1 | 10:07:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_RekSai | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-2 | 10:08:09 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Enfeitiçador | DA_18_RekSai | 0.2100 |  |
| Jogador 5 | 3-2 | 10:08:10 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Enfeitiçador | DA_18_RekSai | 0.2900 |  |
| Jogador 5 | 3-2 | 10:08:10 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Enfeitiçador | DA_18_RekSai | -0.5100 |  |
| Jogador 5 | 3-2 | 10:08:11 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Enfeitiçador | DA_18_RekSai | 0.2900 |  |
| Jogador 5 | 3-2 | 10:08:12 | MOVE Bench -> Board: Yunara (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Enfeitiçador | DA_18_RekSai | -0.5400 |  |
| Jogador 5 | 3-2 | 10:08:12 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Enfeitiçador | DA_18_RekSai | 0.5700 |  |
| Jogador 5 | 3-2 | 10:08:13 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Enfeitiçador | DA_18_RekSai | 0.0700 |  |
| Jogador 5 | 3-2 | 10:08:13 | MOVE Board -> Board: Sejuani (i:4.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Enfeitiçador | DA_18_RekSai | -0.2400 |  |
| Jogador 5 | 3-2 | 10:08:13 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Enfeitiçador | DA_18_RekSai | 0.2500 |  |
| Jogador 5 | 3-3 | 10:08:30 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_18_RekSai | 0.8800 |  |
| Jogador 5 | 3-3 | 10:08:30 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Enfeitiçador | DA_18_RekSai | 0.6300 |  |
| Jogador 5 | 3-3 | 10:08:31 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Enfeitiçador | DA_18_RekSai | 0.6600 |  |
| Jogador 5 | 3-3 | 10:08:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Enfeitiçador | DA_18_RekSai | -0.0200 |  |
| Jogador 5 | 3-3 | 10:08:32 | MOVE Board -> Board: Kobuko (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Enfeitiçador | DA_18_RekSai | -0.3000 |  |
| Jogador 5 | 3-3 | 10:08:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Enfeitiçador | DA_18_RekSai | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-4 | 10:08:52 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Enfeitiçador | DA_18_Yorick | -0.5100 |  |
| Jogador 5 | 3-4 | 10:08:52 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 3-4 | 10:08:53 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Yorick | -0.5900 |  |
| Jogador 5 | 3-4 | 10:08:53 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Yorick | -0.1200 |  |
| Jogador 5 | 3-4 | 10:08:54 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Yorick | -0.0300 |  |
| Jogador 5 | 3-4 | 10:08:54 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Yorick | -0.0300 |  |
| Jogador 5 | 3-4 | 10:08:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Yorick | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-5 | 10:09:15 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Ahri | -0.5900 |  |
| Jogador 5 | 3-5 | 10:09:15 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_18_Ahri | 0.8700 |  |
| Jogador 5 | 3-5 | 10:09:16 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_18_Ahri | 0.4100 |  |
| Jogador 5 | 3-5 | 10:09:17 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Warwick (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_18_Ahri | 0.0800 |  |
| Jogador 5 | 3-5 | 10:09:17 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Warwick (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_18_Ahri | 0.1100 |  |
| Jogador 5 | 3-5 | 10:09:18 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Enfeitiçador | DA_18_Ahri | 0.1400 |  |
| Jogador 5 | 3-5 | 10:09:19 | MOVE Board -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Enfeitiçador | DA_18_Ahri | 0.0600 |  |
| Jogador 5 | 3-5 | 10:09:19 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Ahri | -0.1900 |  |
| Jogador 5 | 3-5 | 10:09:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Enfeitiçador | DA_18_Ahri | 0.0200 |  |
| Jogador 5 | 3-6 | 10:09:43 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 70 | 5 | Enfeitiçador | DA_18_Ahri | 0.8400 |  |
| Jogador 5 | 3-6 | 10:09:43 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Enfeitiçador | DA_18_Ahri | 0.0800 |  |
| Jogador 5 | 3-6 | 10:09:44 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Enfeitiçador | DA_18_Ahri | -0.0300 |  |
| Jogador 5 | 3-6 | 10:09:44 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Ahri | -0.1700 |  |
| Jogador 5 | 3-6 | 10:09:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Enfeitiçador | DA_18_Ahri | 0.0300 |  |
| Jogador 5 | 3-6 | 10:09:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 5 | Enfeitiçador | DA_18_Ahri | 0.0300 |  |
| Jogador 5 | 3-6 | 10:09:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 5 | Enfeitiçador | DA_18_Ahri | 0.0300 |  |
| Jogador 5 | 3-6 | 10:09:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 5 | Enfeitiçador | DA_18_Ahri | -0.0600 |  |
| Jogador 5 | 3-6 | 10:09:47 | MOVE Board -> Board: Sejuani (i:4.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 5 | Enfeitiçador | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 3-7 | 10:10:07 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Enfeitiçador | DA_18_Ahri | 0.1600 |  |
| Jogador 5 | 3-7 | 10:10:08 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Enfeitiçador | DA_18_Ahri | 0.1200 |  |
| Jogador 5 | 3-7 | 10:10:08 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Enfeitiçador | DA_18_Ahri | -0.0300 |  |
| Jogador 5 | 3-7 | 10:10:09 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Enfeitiçador | DA_18_Ahri | 0.9600 |  |
| Jogador 5 | 3-7 | 10:10:09 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Enfeitiçador | DA_18_Ahri | 0.3700 |  |
| Jogador 5 | 3-7 | 10:10:10 | MOVE Bench -> Board: LeBlanc (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Enfeitiçador | DA_18_Ahri | 0.6100 |  |
| Jogador 5 | 3-7 | 10:10:10 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Ahri | 0.1300 |  |
| Jogador 5 | 3-7 | 10:10:11 | MOVE Board -> Board: LeBlanc (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Ahri | 0.0800 |  |
| Jogador 5 | 3-7 | 10:10:11 | MOVE Board -> Board: Warwick (i:4.0) <-> LeBlanc (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Ahri | 0.0400 |  |
| Jogador 5 | 4-1 | 10:10:33 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Ahri | -0.0300 |  |
| Jogador 5 | 4-1 | 10:10:34 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Enfeitiçador | DA_18_Ahri | 0.1800 |  |
| Jogador 5 | 4-1 | 10:10:34 | MOVE Bench -> Board: Soraka (i:8.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Enfeitiçador | DA_18_Ahri | -0.2100 |  |
| Jogador 5 | 4-1 | 10:10:35 | MOVE Board -> Board: LeBlanc (i:8.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Enfeitiçador | DA_18_Ahri | -0.0200 |  |
| Jogador 5 | 4-1 | 10:10:36 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Enfeitiçador | DA_18_Ahri | -0.0900 |  |
| Jogador 5 | 4-2 | 10:11:01 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Enfeitiçador | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 4-2 | 10:11:02 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Enfeitiçador | DA_18_Ahri | 0.8400 |  |
| Jogador 5 | 4-2 | 10:11:02 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Enfeitiçador | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 4-2 | 10:11:03 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Enfeitiçador | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 4-2 | 10:11:03 | MOVE Board -> Board: Sejuani (i:4.0) <-> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Enfeitiçador | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 4-2 | 10:11:04 | MOVE Board -> Board: Kobuko (i:2.0) <-> Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Enfeitiçador | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 4-2 | 10:11:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Enfeitiçador | DA_18_Ahri | -0.0900 |  |
| Jogador 5 | 4-3 | 10:11:29 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Enfeitiçador | DA_18_Ahri | -0.0200 |  |
| Jogador 5 | 4-3 | 10:11:30 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Enfeitiçador | DA_18_Ahri | 0.1600 |  |
| Jogador 5 | 4-3 | 10:11:30 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Enfeitiçador | DA_18_Ahri | 0.5900 |  |
| Jogador 5 | 4-3 | 10:11:31 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Enfeitiçador | DA_18_Ahri | -0.1300 |  |
| Jogador 5 | 4-3 | 10:11:31 | MOVE Board -> Board: Veigar (i:2.0) <-> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Enfeitiçador | DA_18_Ahri | 0.0100 |  |
| Jogador 5 | 4-3 | 10:11:32 | MOVE Board -> Board: Warwick (i:4.0) <-> LeBlanc (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Enfeitiçador | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 4-3 | 10:11:32 | MOVE Board -> Board: LeBlanc (i:8.0) <-> Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Enfeitiçador | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 4-3 | 10:11:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Enfeitiçador | DA_18_Ahri | -0.1000 |  |
| Jogador 5 | 4-4 | 10:11:58 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Enfeitiçador | DA_18_Ahri | -0.0300 |  |
| Jogador 5 | 4-4 | 10:11:58 | COMPROU: Karma (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Enfeitiçador | DA_18_Ahri | 0.2900 |  |
| Jogador 5 | 4-4 | 10:11:59 | MOVE Board -> Board: Soraka (i:8.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Enfeitiçador | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 4-4 | 10:11:59 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Enfeitiçador | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 4-4 | 10:12:00 | COMPROU: Leona (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Enfeitiçador | DA_18_Ahri | 0.1900 |  |
| Jogador 5 | 4-4 | 10:12:00 | MOVE Board -> Board: Sejuani (i:4.0) <-> Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Enfeitiçador | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 4-4 | 10:12:00 | MOVE Board -> Board: Yunara (i:4.0) <-> Kobuko (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Enfeitiçador | DA_18_Ahri | -0.0200 |  |
| Jogador 5 | 4-4 | 10:12:01 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Enfeitiçador | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 4-4 | 10:12:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Enfeitiçador | DA_18_Ahri | -0.1100 |  |
| Jogador 5 | 4-5 | 10:12:26 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Enfeitiçador | DA_18_Ahri | -0.0300 |  |
| Jogador 5 | 4-5 | 10:12:27 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Enfeitiçador | DA_18_Ahri | -0.1100 |  |
| Jogador 5 | 4-5 | 10:12:27 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Enfeitiçador | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 4-5 | 10:12:28 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Enfeitiçador | DA_18_Ahri | -0.1600 |  |
| Jogador 5 | 4-5 | 10:12:28 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Enfeitiçador | DA_18_Ahri | 0.0400 |  |
| Jogador 5 | 4-5 | 10:12:29 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 95 | 5 | Enfeitiçador | DA_18_Ahri | 0.0400 |  |
| Jogador 5 | 4-5 | 10:12:29 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Enfeitiçador | DA_18_Ahri | 0.0400 |  |
| Jogador 5 | 4-5 | 10:12:29 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Enfeitiçador | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 4-5 | 10:12:30 | MOVE Board -> Board: Veigar (i:2.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Enfeitiçador | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 4-6 | 10:12:58 | VENDEU: Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Enfeitiçador | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 4-6 | 10:12:59 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Enfeitiçador | DA_18_Ahri | 0.8500 |  |
| Jogador 5 | 4-6 | 10:12:59 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Enfeitiçador | DA_18_Ahri | -0.1400 |  |
| Jogador 5 | 4-6 | 10:13:00 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Enfeitiçador | DA_18_Ahri | 0.1400 |  |
| Jogador 5 | 4-6 | 10:13:00 | MOVE Bench -> Board: Leona (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Enfeitiçador | DA_18_Ahri | -0.3800 |  |
| Jogador 5 | 4-6 | 10:13:01 | MOVE Bench -> Board: Yunara (i:4.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Enfeitiçador | DA_18_Ahri | -0.4100 |  |
| Jogador 5 | 4-6 | 10:13:01 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Enfeitiçador | DA_18_Ahri | -0.1400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-7 | 10:13:34 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 116 | 5 | Enfeitiçador | DA_18_Ahri | 0.1600 |  |
| Jogador 5 | 4-7 | 10:13:34 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> LeBlanc (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 116 | 5 | Enfeitiçador | DA_18_Ahri | 0.1900 |  |
| Jogador 5 | 4-7 | 10:13:35 | MOVE Bench -> Board: Veigar (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 116 | 5 | Enfeitiçador | DA_18_Ahri | 0.0800 |  |
| Jogador 5 | 4-7 | 10:13:35 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Enfeitiçador | DA_18_Ahri | -0.0300 |  |
| Jogador 5 | 4-7 | 10:13:36 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 114 | 5 | Enfeitiçador | DA_18_Ahri | 0.1700 |  |
| Jogador 5 | 4-7 | 10:13:36 | MOVE Bench -> Board: Azir (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 114 | 5 | Enfeitiçador | DA_18_Ahri | -0.3300 |  |
| Jogador 5 | 4-7 | 10:13:37 | MOVE Bench -> Board: Leona (i:2.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 114 | 5 | Enfeitiçador | DA_18_Ahri | -0.4000 |  |
| Jogador 5 | 4-7 | 10:13:38 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 114 | 5 | Enfeitiçador | DA_18_Ahri | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 5-1 | 10:14:09 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 129 | 5 | Enfeitiçador | DA_18_Ahri | -0.0300 |  |
| Jogador 5 | 5-1 | 10:14:09 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Enfeitiçador | DA_18_Ahri | 0.4200 |  |
| Jogador 5 | 5-1 | 10:14:10 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 127 | 5 | Enfeitiçador | DA_18_Ahri | -0.4400 |  |
| Jogador 5 | 5-1 | 10:14:10 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Enfeitiçador | DA_18_Ahri | 0.5300 |  |
| Jogador 5 | 5-1 | 10:14:11 | MOVE Bench -> Board: Azir (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Enfeitiçador | DA_18_Ahri | 0.1000 |  |
| Jogador 5 | 5-1 | 10:14:11 | MOVE Bench -> Board: Yunara (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Enfeitiçador | DA_18_Ahri | -0.5100 |  |
| Jogador 5 | 5-1 | 10:14:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 124 | 5 | Enfeitiçador | DA_18_Ahri | -0.1600 |  |
| Jogador 5 | 5-1 | 10:14:12 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 125 | 5 | Enfeitiçador | DA_18_Ahri | -0.4400 |  |
| Jogador 5 | 5-1 | 10:14:12 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 122 | 5 | Enfeitiçador | DA_18_Ahri | 0.1500 |  |
| Jogador 5 | 5-2 | 10:14:43 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 137 | 5 | Enfeitiçador | DA_18_Ahri | -0.0300 |  |
| Jogador 5 | 5-2 | 10:14:43 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 134 | 5 | Enfeitiçador | DA_18_Ahri | 0.9200 |  |
| Jogador 5 | 5-2 | 10:14:44 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 136 | 5 | Enfeitiçador | DA_18_Ahri | -0.4800 |  |
| Jogador 5 | 5-2 | 10:14:44 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Enfeitiçador | DA_18_Ahri | 0.1600 |  |
| Jogador 5 | 5-2 | 10:14:45 | MOVE Bench -> Board: Leona (i:2.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Enfeitiçador | DA_18_Ahri | -0.4000 |  |
| Jogador 5 | 5-2 | 10:14:45 | MOVE Bench -> Board: Veigar (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Enfeitiçador | DA_18_Ahri | 0.0700 |  |
| Jogador 5 | 5-2 | 10:14:45 | MOVE Bench -> Board: Yunara (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Enfeitiçador | DA_18_Ahri | -0.5600 |  |
| Jogador 5 | 5-2 | 10:14:46 | MOVE Bench -> Board: Leona (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Enfeitiçador | DA_18_Ahri | -0.4000 |  |
| Jogador 5 | 5-2 | 10:14:46 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 133 | 5 | Enfeitiçador | DA_18_Ahri | -0.1800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 5-3 | 10:15:18 | MOVE Bench -> Board: Veigar (i:2.0) <-> Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Enfeitiçador | DA_18_Ahri | 0.1000 |  |
| Jogador 5 | 5-3 | 10:15:19 | MOVE Bench -> Board: Yunara (i:4.0) <-> Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Enfeitiçador | DA_18_Ahri | -0.5800 |  |
| Jogador 5 | 5-3 | 10:15:19 | MOVE Bench -> Board: Leona (i:2.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Enfeitiçador | DA_18_Ahri | -0.6100 |  |
| Jogador 5 | 5-3 | 10:15:20 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Enfeitiçador | DA_18_Ahri | -0.5600 |  |
| Jogador 5 | 5-4 | 10:15:57 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 153 | 5 | Enfeitiçador | DA_18_Ahri | -0.3400 |  |
| Jogador 5 | 5-4 | 10:15:57 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Enfeitiçador | DA_18_Ahri | -0.0300 |  |
| Jogador 5 | 5-4 | 10:15:58 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Enfeitiçador | DA_18_Ahri | 0.9000 |  |
| Jogador 5 | 5-4 | 10:15:58 | MOVE Bench -> Board: Yunara (i:4.0) <-> Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Enfeitiçador | DA_18_Ahri | -0.3900 |  |
| Jogador 5 | 5-4 | 10:15:59 | MOVE Bench -> Board: Veigar (i:2.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Enfeitiçador | DA_18_Ahri | 0.0400 |  |
| Jogador 5 | 5-4 | 10:15:59 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Enfeitiçador | DA_18_Ahri | -0.3600 |  |
| Jogador 5 | 5-4 | 10:16:00 | MOVE Bench -> Board: Yunara (i:4.0) <-> Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Enfeitiçador | DA_18_Ahri | -0.4000 |  |
| Jogador 5 | 5-4 | 10:16:00 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Enfeitiçador | DA_18_Ahri | -0.5700 |  |
| Jogador 5 | 5-5 | 10:16:35 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Enfeitiçador | DA_18_Ahri | -0.6800 |  |
| Jogador 5 | 5-5 | 10:16:35 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Enfeitiçador | DA_18_Ahri | -0.1100 |  |
| Jogador 5 | 5-5 | 10:16:36 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 166 | 5 | Enfeitiçador | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 5-5 | 10:16:36 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Enfeitiçador | DA_18_Ahri | -0.1100 |  |
| Jogador 5 | 5-5 | 10:16:36 | MOVE Bench -> Board: Veigar (i:2.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Enfeitiçador | DA_18_Ahri | 0.0900 |  |
| Jogador 5 | 5-5 | 10:16:37 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Enfeitiçador | DA_18_Ahri | -0.3900 |  |
| Jogador 5 | 5-5 | 10:16:37 | MOVE Bench -> Board: Yunara (i:4.0) <-> Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Enfeitiçador | DA_18_Ahri | -0.4100 |  |
| Jogador 5 | 5-5 | 10:16:38 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 163 | 5 | Enfeitiçador | DA_18_Ahri | -0.5800 |  |
| Jogador 5 | 5-6 | 10:17:12 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 176 | 5 | Enfeitiçador | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 5-6 | 10:17:14 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Enfeitiçador | DA_18_Ahri | 0.4400 |  |
| Jogador 5 | 5-6 | 10:17:14 | MOVE Bench -> Board: Veigar (i:2.0) <-> Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Enfeitiçador | DA_18_Ahri | 0.0500 |  |
| Jogador 5 | 5-6 | 10:17:15 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Enfeitiçador | DA_18_Ahri | -0.3600 |  |
| Jogador 5 | 5-6 | 10:17:15 | MOVE Bench -> Board: Yunara (i:4.0) <-> Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Enfeitiçador | DA_18_Ahri | -0.4000 |  |
| Jogador 5 | 5-6 | 10:17:16 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 175 | 5 | Enfeitiçador | DA_18_Ahri | -0.5900 |  |
| Jogador 5 | 5-7 | 10:18:02 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Soraka (i:8.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 185 | 5 | Enfeitiçador | DA_18_Ahri | 0.1000 |  |
| Jogador 5 | 5-7 | 10:18:02 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 186 | 5 | Enfeitiçador | DA_18_Ahri | -0.6800 |  |
| Jogador 5 | 5-7 | 10:18:02 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 182 | 5 | Enfeitiçador | DA_18_Ahri | 0.1300 |  |
| Jogador 5 | 5-7 | 10:18:03 | VENDEU: Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 186 | 5 | Enfeitiçador | DA_18_Ahri | -0.0400 |  |
| Jogador 5 | 5-7 | 10:18:03 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 182 | 5 | Enfeitiçador | DA_18_Ahri | -0.1800 |  |
| Jogador 5 | 5-7 | 10:18:04 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 180 | 5 | Enfeitiçador | DA_18_Ahri | -0.0700 |  |
| Jogador 5 | 5-7 | 10:18:04 | VENDEU: Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 184 | 5 | Enfeitiçador | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 5-7 | 10:18:05 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 181 | 5 | Enfeitiçador | DA_18_Azir | 1.1100 |  |
| Jogador 5 | 5-7 | 10:18:05 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 179 | 5 | Enfeitiçador | DA_18_Azir | 1.1100 |  |
| Jogador 5 | 6-1 | 10:18:45 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Enfeitiçador | DA_18_Azir | 0.5200 |  |
| Jogador 5 | 6-1 | 10:18:45 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 186 | 5 | Enfeitiçador | DA_18_Azir | 0.5000 |  |
| Jogador 5 | 6-1 | 10:18:46 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 186 | 5 | Enfeitiçador | DA_18_Azir | 0.5700 |  |
| Jogador 5 | 6-1 | 10:18:46 | MOVE Bench -> Board: Yunara (i:8.0) <-> Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 186 | 5 | Enfeitiçador | DA_18_Azir | -0.3500 |  |
| Jogador 5 | 6-1 | 10:18:47 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 183 | 5 | Enfeitiçador | DA_18_Azir | 0.1900 |  |
| Jogador 5 | 6-1 | 10:18:47 | MOVE Bench -> Board: Diana (i:6.0) <-> Yunara (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 183 | 5 | Enfeitiçador | DA_18_Azir | -0.4000 |  |
| Jogador 5 | 6-1 | 10:18:48 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 181 | 5 | Enfeitiçador | DA_18_Azir | -0.0700 |  |
| Jogador 5 | 6-1 | 10:18:48 | VENDEU: Yunara (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 186 | 5 | Enfeitiçador | DA_18_Azir | -0.6800 |  |
| Jogador 5 | 6-1 | 10:18:48 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 184 | 5 | Enfeitiçador | DA_18_Azir | 1.1100 |  |
| Jogador 5 | 6-2 | 10:19:29 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 192 | 5 | Enfeitiçador | DA_18_Azir | 0.7900 |  |
| Jogador 5 | 6-2 | 10:19:29 | MOVE Bench -> Board: Sejuani (i:8.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 192 | 5 | Enfeitiçador | DA_18_Azir | 0.0900 |  |
| Jogador 5 | 6-2 | 10:19:29 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 192 | 5 | Enfeitiçador | DA_18_Azir | 0.4000 |  |
| Jogador 5 | 6-2 | 10:19:30 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 189 | 5 | Enfeitiçador | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 6-2 | 10:19:30 | MOVE Board -> Board: Diana (i:6.0) <-> Kobuko (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 189 | 5 | Enfeitiçador | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 6-2 | 10:19:31 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 189 | 5 | Enfeitiçador | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 6-2 | 10:19:31 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 189 | 5 | Enfeitiçador | DA_18_Azir | -0.6300 |  |
| Jogador 5 | 6-3 | 10:20:14 | VENDEU: Azir (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 209 | 5 | Enfeitiçador | DA_18_Azir | -0.6800 |  |
| Jogador 5 | 6-3 | 10:20:15 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 207 | 5 | Enfeitiçador | DA_18_Azir | 0.4600 |  |
| Jogador 5 | 6-3 | 10:20:15 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 205 | 5 | Enfeitiçador | DA_18_Azir | -0.0700 |  |
| Jogador 5 | 6-3 | 10:20:16 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 208 | 5 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 6-3 | 10:20:16 | COMPROU: Alune (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 203 | 5 | Enfeitiçador | DA_18_Alune | 0.4900 |  |
| Jogador 5 | 6-3 | 10:20:16 | MOVE Bench -> Board: Alune (i:10.0) <-> Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 203 | 5 | Enfeitiçador | DA_18_Alune | -0.2800 |  |
| Jogador 5 | 6-3 | 10:20:17 | MOVE Bench -> Board: Sejuani (i:8.0) <-> Kobuko (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 203 | 5 | Enfeitiçador | DA_18_Alune | 0.0800 |  |
| Jogador 5 | 6-3 | 10:20:17 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 201 | 5 | Enfeitiçador | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-3 | 10:20:18 | VENDEU: Kobuko (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 202 | 5 | Enfeitiçador | DA_18_Alune | 0.0200 |  |
| Jogador 5 | 6-4 | 10:21:03 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 209 | 5 | Enfeitiçador | DA_18_Alune | -0.0200 |  |
| Jogador 5 | 6-4 | 10:21:03 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Alune (i:10.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 209 | 5 | Enfeitiçador | DA_18_Alune | 0.1200 |  |
| Jogador 5 | 6-4 | 10:21:04 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Alune (i:10.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 209 | 5 | Enfeitiçador | DA_18_Alune | 0.0700 |  |
| Jogador 5 | 6-4 | 10:21:04 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Alune (i:10.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 209 | 5 | Enfeitiçador | DA_18_Alune | 0.1000 |  |
| Jogador 5 | 6-4 | 10:21:04 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 207 | 5 | Enfeitiçador | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-4 | 10:21:05 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Enfeitiçador | DA_18_Alune | -0.0300 |  |
| Jogador 5 | 6-4 | 10:21:05 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 209 | 5 | Enfeitiçador | DA_18_Alune | 0.5700 |  |
| Jogador 5 | 6-4 | 10:21:05 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 207 | 5 | Enfeitiçador | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-4 | 10:21:06 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 209 | 5 | Enfeitiçador | DA_18_Alune | -0.5800 |  |
| Jogador 5 | 6-5 | 10:21:48 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 217 | 5 | Enfeitiçador | DA_18_Alune | -0.1800 |  |
| Jogador 5 | 6-5 | 10:21:48 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 215 | 5 | Enfeitiçador | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-5 | 10:21:49 | VENDEU: Sett (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 219 | 5 | Enfeitiçador | DA_18_Alune | 0.0100 |  |
| Jogador 5 | 6-5 | 10:21:49 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 217 | 5 | Enfeitiçador | DA_18_Alune | 0.5700 |  |
| Jogador 5 | 6-5 | 10:21:50 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 215 | 5 | Enfeitiçador | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-5 | 10:21:50 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 213 | 5 | Enfeitiçador | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-5 | 10:21:50 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Enfeitiçador | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-5 | 10:21:51 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 213 | 5 | Enfeitiçador | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-5 | 10:21:51 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 212 | 5 | Enfeitiçador | DA_18_Alune | 1.0400 |  |
| Jogador 5 | 6-6 | 10:22:34 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 227 | 5 | Enfeitiçador | DA_18_Alune | -0.6800 |  |
| Jogador 5 | 6-6 | 10:22:34 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 226 | 5 | Enfeitiçador | DA_18_Alune | 0.6700 |  |
| Jogador 5 | 6-6 | 10:22:34 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 224 | 5 | Enfeitiçador | DA_18_Alune | -0.0700 |  |
| Jogador 5 | 6-6 | 10:22:35 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 225 | 5 | Enfeitiçador | DA_18_Alune | -0.5900 |  |
| Jogador 5 | 6-6 | 10:22:35 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 223 | 5 | Enfeitiçador | DA_18_Alune | 1.1100 |  |
| Jogador 5 | 6-6 | 10:22:35 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 223 | 5 | Enfeitiçador | DA_18_Alune | 0.6000 |  |
| Jogador 5 | 6-6 | 10:22:36 | MOVE Board -> Board: Veigar (i:2.0) <-> Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 223 | 5 | Enfeitiçador | DA_18_Alune | -0.0100 |  |
| Jogador 5 | 6-6 | 10:22:36 | MOVE Board -> Board: Sejuani (i:8.0) <-> LeBlanc (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 223 | 5 | Enfeitiçador | DA_18_Alune | -0.0200 |  |
| Jogador 5 | 6-6 | 10:22:37 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 223 | 5 | Enfeitiçador | DA_18_Alune | -0.8200 |  |
| Jogador 5 | 6-7 | 10:23:19 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 233 | 5 | Enfeitiçador | DA_18_Alune | 0.5000 |  |
| Jogador 5 | 6-7 | 10:23:20 | EQUIP_FROM_INVENTORY: DA_18_EmblemSlayer -> Diana (i:6.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 233 | 5 | Enfeitiçador | DA_18_Alune | -0.0200 |  |
| Jogador 5 | 6-7 | 10:23:20 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 231 | 5 | Enfeitiçador | DA_18_Alune | 0.2700 |  |
| Jogador 5 | 6-7 | 10:23:21 | MOVE Board -> Board: LeBlanc (i:8.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 231 | 5 | Enfeitiçador | DA_18_Alune | 0.0000 |  |
| Jogador 5 | 6-7 | 10:23:21 | MOVE Board -> Board: Diana (i:6.0) <-> Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 231 | 5 | Enfeitiçador | DA_18_Alune | -0.0100 |  |
| Jogador 5 | 6-7 | 10:23:22 | MOVE Board -> Board: Soraka (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 231 | 5 | Enfeitiçador | DA_18_Alune | -0.0100 |  |
| Jogador 5 | 6-7 | 10:23:24 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 231 | 5 | Enfeitiçador | DA_18_Alune | -0.6700 |  |
| Jogador 6 | ? | 10:05:44 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 10:05:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 10:05:50 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 10:05:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.9900 |  |
| Jogador 6 | 1-1 | 10:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-1 | 10:05:56 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4500 |  |
| Jogador 6 | 1-2 | 10:05:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-2 | 10:06:03 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.5800 |  |
| Jogador 6 | 1-3 | 10:06:05 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 1.0200 |  |
| Jogador 6 | 1-3 | 10:06:06 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 6 | 1-3 | 10:06:06 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | -0.2400 |  |
| Jogador 6 | 1-3 | 10:06:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-4 | 10:06:13 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 6 | 1-4 | 10:06:14 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 6 | 1-4 | 10:06:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0600 |  |
| Jogador 6 | 1-4 | 10:06:16 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 6 | 1-4 | 10:06:17 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 6 | 1-4 | 10:06:17 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0100 |  |
| Jogador 6 | 1-4 | 10:06:18 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.1500 |  |
| Jogador 6 | 1-4 | 10:06:18 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.0700 |  |
| Jogador 6 | 1-4 | 10:06:19 | MOVE Board -> Board: Cascalho (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 1-4 | 10:06:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-1 | 10:06:22 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | 0.1300 |  |
| Jogador 6 | 2-1 | 10:06:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-1 | 10:06:25 | MOVE Board -> Board: Yorick (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.3600 |  |
| Jogador 6 | 2-1 | 10:06:26 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-1 | 10:06:26 | MOVE Board -> Board: Cascalho (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-1 | 10:06:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 10:06:31 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Tristana | 0.3000 |  |
| Jogador 6 | 2-2 | 10:06:31 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2700 |  |
| Jogador 6 | 2-2 | 10:06:34 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | -0.1000 |  |
| Jogador 6 | 2-2 | 10:06:35 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-2 | 10:06:36 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-2 | 10:06:36 | MOVE Board -> Board: Cascalho (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Yorick | -0.3500 |  |
| Jogador 6 | 2-2 | 10:06:37 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Yorick | -0.1300 |  |
| Jogador 6 | 2-3 | 10:06:40 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | — | DA_Karma18 | 1.1100 |  |
| Jogador 6 | 2-3 | 10:06:41 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | — | DA_Karma18 | 0.2300 |  |
| Jogador 6 | 2-3 | 10:06:41 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_Karma18 | 0.9400 |  |
| Jogador 6 | 2-3 | 10:06:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | — | DA_Karma18 | -0.0600 |  |
| Jogador 6 | 2-3 | 10:06:46 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | — | DA_Karma18 | 0.5300 |  |
| Jogador 6 | 2-4 | 10:06:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Karma18 | 1.1200 |  |
| Jogador 6 | 2-4 | 10:06:52 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Karma18 | 0.2500 |  |
| Jogador 6 | 2-4 | 10:06:52 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_Karma18 | 0.1900 |  |
| Jogador 6 | 2-4 | 10:06:53 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Colosso | DA_Karma18 | 0.0200 |  |
| Jogador 6 | 2-4 | 10:06:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Colosso | DA_Karma18 | -0.0100 |  |
| Jogador 6 | 2-4 | 10:06:54 | MOVE Board -> Board: Cascalho (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Colosso | DA_Karma18 | -0.0100 |  |
| Jogador 6 | 2-4 | 10:06:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Colosso | DA_Karma18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 2-5 | 10:07:03 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Karma18 | 0.3100 |  |
| Jogador 6 | 2-5 | 10:07:04 | MOVE Board -> Board: Yorick (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Karma18 | 0.0000 |  |
| Jogador 6 | 2-5 | 10:07:04 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Karma18 | -0.0700 |  |
| Jogador 6 | 2-5 | 10:07:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Karma18 | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 2-6 | 10:07:17 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_Karma18 | 0.9700 |  |
| Jogador 6 | 2-6 | 10:07:18 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Emanador | DA_Karma18 | 0.2900 |  |
| Jogador 6 | 2-6 | 10:07:18 | MOVE Board -> Board: Cascalho (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Emanador | DA_Karma18 | 0.2400 |  |
| Jogador 6 | 2-6 | 10:07:19 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Emanador | DA_Karma18 | -0.0100 |  |
| Jogador 6 | 2-6 | 10:07:19 | MOVE Board -> Board: Yorick (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Emanador | DA_Karma18 | -0.1000 |  |
| Jogador 6 | 2-6 | 10:07:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Emanador | DA_Karma18 | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 2-7 | 10:07:34 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Emanador | DA_Karma18 | 0.2900 |  |
| Jogador 6 | 2-7 | 10:07:34 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Emanador | DA_Karma18 | 0.2600 |  |
| Jogador 6 | 2-7 | 10:07:35 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Emanador | DA_Karma18 | 0.2400 |  |
| Jogador 6 | 2-7 | 10:07:36 | MOVE Board -> Board: Karma (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Emanador | DA_Karma18 | -0.0500 |  |
| Jogador 6 | 2-7 | 10:07:36 | MOVE Board -> Board: Rakan (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Emanador | DA_Karma18 | 0.0000 |  |
| Jogador 6 | 2-7 | 10:07:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Emanador | DA_Karma18 | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 3-1 | 10:07:50 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Emanador | DA_Karma18 | 0.7900 |  |
| Jogador 6 | 3-1 | 10:07:51 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Emanador | DA_Karma18 | 0.8500 |  |
| Jogador 6 | 3-1 | 10:07:51 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Emanador | DA_Karma18 | 0.1500 |  |
| Jogador 6 | 3-1 | 10:07:52 | MOVE Bench -> Board: Cascalho (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Emanador | DA_Karma18 | -0.0600 |  |
| Jogador 6 | 3-1 | 10:07:53 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Emanador | DA_Karma18 | -0.0400 |  |
| Jogador 6 | 3-1 | 10:07:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Emanador | DA_Karma18 | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 3-2 | 10:08:09 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Emanador | DA_Karma18 | 0.8300 |  |
| Jogador 6 | 3-2 | 10:08:10 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Emanador | DA_Karma18 | -0.2600 |  |
| Jogador 6 | 3-2 | 10:08:10 | MOVE Board -> Board: Grompe (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Emanador | DA_Karma18 | 0.0000 |  |
| Jogador 6 | 3-2 | 10:08:11 | MOVE Board -> Board: Karma (i:4.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Emanador | DA_Karma18 | -0.0400 |  |
| Jogador 6 | 3-2 | 10:08:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Emanador | DA_Karma18 | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 3-3 | 10:08:30 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Emanador | DA_Karma18 | 0.7400 |  |
| Jogador 6 | 3-3 | 10:08:30 | MOVE Bench -> Board: Rengar (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Emanador | DA_Karma18 | -0.4000 |  |
| Jogador 6 | 3-3 | 10:08:31 | MOVE Board -> Board: Rengar (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Emanador | DA_Karma18 | -0.0100 |  |
| Jogador 6 | 3-3 | 10:08:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Emanador | DA_Karma18 | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 3-4 | 10:08:52 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Emanador | DA_Karma18 | 0.8800 |  |
| Jogador 6 | 3-4 | 10:08:52 | MOVE Bench -> Board: Yorick (i:4.0) <-> Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Emanador | DA_Karma18 | -0.1300 |  |
| Jogador 6 | 3-4 | 10:08:53 | MOVE Bench -> Board: Cascalho (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Emanador | DA_Karma18 | 0.3600 |  |
| Jogador 6 | 3-4 | 10:08:53 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Cascalho (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Emanador | DA_Karma18 | -0.3700 |  |
| Jogador 6 | 3-4 | 10:08:54 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Emanador | DA_Karma18 | 0.1600 |  |
| Jogador 6 | 3-4 | 10:08:54 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Emanador | DA_Karma18 | 0.0100 |  |
| Jogador 6 | 3-4 | 10:08:55 | MOVE Bench -> Board: Grompe (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Emanador | DA_Karma18 | 0.4800 |  |
| Jogador 6 | 3-4 | 10:08:55 | MOVE Board -> Board: Grompe (i:8.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Emanador | DA_Karma18 | 0.0100 |  |
| Jogador 6 | 3-4 | 10:08:55 | MOVE Board -> Board: Rengar (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Emanador | DA_Karma18 | -0.0100 |  |
| Jogador 6 | 3-5 | 10:09:15 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Karma (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Emanador | DA_Karma18 | 0.0000 |  |
| Jogador 6 | 3-5 | 10:09:15 | MOVE Board -> Board: Karma (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Emanador | DA_Karma18 | -0.0100 |  |
| Jogador 6 | 3-5 | 10:09:16 | MOVE Board -> Board: Yorick (i:4.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Emanador | DA_Karma18 | -0.0100 |  |
| Jogador 6 | 3-5 | 10:09:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Emanador | DA_Karma18 | -0.1500 |  |
| Jogador 6 | 3-6 | 10:09:43 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 5 | Emanador | DA_Karma18 | 0.2700 |  |
| Jogador 6 | 3-6 | 10:09:43 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 5 | Emanador | DA_Karma18 | 0.1000 |  |
| Jogador 6 | 3-6 | 10:09:44 | MOVE Board -> Board: Azuporã (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 5 | Emanador | DA_Karma18 | -0.0100 |  |
| Jogador 6 | 3-6 | 10:09:44 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Grompe (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 5 | Emanador | DA_Karma18 | -0.0300 |  |
| Jogador 6 | 3-6 | 10:09:45 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 5 | Emanador | DA_Karma18 | -0.1600 |  |
| Jogador 6 | 3-7 | 10:10:07 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Emanador | DA_Karma18 | 0.2200 |  |
| Jogador 6 | 3-7 | 10:10:08 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Grompe (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Emanador | DA_Karma18 | 0.2200 |  |
| Jogador 6 | 3-7 | 10:10:08 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Emanador | DA_Karma18 | 0.6700 |  |
| Jogador 6 | 3-7 | 10:10:09 | MOVE Bench -> Board: Shen (i:4.0) <-> Grompe (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Emanador | DA_Karma18 | -0.3900 |  |
| Jogador 6 | 3-7 | 10:10:09 | MOVE Bench -> Board: Grompe (i:8.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Emanador | DA_Karma18 | -0.6900 |  |
| Jogador 6 | 3-7 | 10:10:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Emanador | DA_Karma18 | -0.1000 |  |
| Jogador 6 | 4-1 | 10:10:33 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Emanador | DA_Karma18 | -0.5900 |  |
| Jogador 6 | 4-1 | 10:10:34 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Emanador | DA_18_MasterYi_AD | 0.9600 |  |
| Jogador 6 | 4-1 | 10:10:34 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Emanador | DA_18_MasterYi_AD | 0.3800 |  |
| Jogador 6 | 4-1 | 10:10:35 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Emanador | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 6 | 4-1 | 10:10:36 | MOVE Board -> Board: Azuporã (i:8.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Emanador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 6 | 4-1 | 10:10:36 | MOVE Board -> Board: Yorick (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Emanador | DA_18_MasterYi_AD | -0.2200 |  |
| Jogador 6 | 4-1 | 10:10:37 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Emanador | DA_18_MasterYi_AD | -0.2600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-2 | 10:11:01 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Emanador | DA_18_MasterYi_AD | 0.1700 |  |
| Jogador 6 | 4-2 | 10:11:02 | MOVE Bench -> Board: Rengar (i:6.0) <-> Karma (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Emanador | DA_18_MasterYi_AD | -0.2100 |  |
| Jogador 6 | 4-2 | 10:11:02 | MOVE Board -> Board: Rengar (i:6.0) <-> Grompe (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Emanador | DA_18_MasterYi_AD | -0.0600 |  |
| Jogador 6 | 4-2 | 10:11:03 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Emanador | DA_18_MasterYi_AD | -0.4800 |  |
| Jogador 6 | 4-3 | 10:11:29 | VENDEU: Karma (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Emanador | DA_18_MasterYi_AD | -0.6900 |  |
| Jogador 6 | 4-3 | 10:11:30 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Emanador | DA_18_MasterYi_AD | 0.4100 |  |
| Jogador 6 | 4-3 | 10:11:30 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Emanador | DA_18_MasterYi_AD | -0.0700 |  |
| Jogador 6 | 4-3 | 10:11:31 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Emanador | DA_18_MasterYi_AD | -0.0700 |  |
| Jogador 6 | 4-3 | 10:11:31 | VENDEU: Cascalho (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Emanador | DA_18_MasterYi_AD | -0.7200 |  |
| Jogador 6 | 4-3 | 10:11:32 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Emanador | DA_18_MasterYi_AD | 0.4700 |  |
| Jogador 6 | 4-3 | 10:11:32 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Grompe (i:8.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Emanador | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 6 | 4-3 | 10:11:32 | MOVE Board -> Board: Grompe (i:8.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Emanador | DA_18_MasterYi_AD | 0.0200 |  |
| Jogador 6 | 4-3 | 10:11:33 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Emanador | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 6 | 4-4 | 10:11:58 | VENDEU: Master Yi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Emanador | DA_Sentinel18 | -0.7300 |  |
| Jogador 6 | 4-4 | 10:11:58 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Emanador | DA_KogMaw18_AD | 1.0800 |  |
| Jogador 6 | 4-4 | 10:11:59 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Emanador | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 6 | 4-4 | 10:11:59 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Emanador | DA_KogMaw18_AD | 0.4300 |  |
| Jogador 6 | 4-4 | 10:12:00 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Emanador | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 6 | 4-4 | 10:12:00 | MOVE Board -> Board: Rakan (i:2.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Emanador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-4 | 10:12:00 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Azuporã (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Emanador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-4 | 10:12:01 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Emanador | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 6 | 4-5 | 10:12:26 | VENDEU: Kog'Maw (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Emanador | DA_Sentinel18 | -0.7300 |  |
| Jogador 6 | 4-5 | 10:12:27 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 4-5 | 10:12:27 | MOVE Board -> Board: Azuporã (i:8.0) <-> Yorick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Emanador | DA_Sentinel18 | 0.0000 |  |
| Jogador 6 | 4-5 | 10:12:28 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Emanador | DA_Sentinel18 | -0.0100 |  |
| Jogador 6 | 4-5 | 10:12:28 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Emanador | DA_Sentinel18 | -0.5600 |  |
| Jogador 7 | ? | 10:05:44 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 10:05:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 10:05:50 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 10:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 10:05:56 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 7 | 1-2 | 10:05:58 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 10:05:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 10:06:03 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.5200 |  |
| Jogador 7 | 1-3 | 10:06:05 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 7 | 1-3 | 10:06:06 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-3 | 10:06:06 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 7 | 1-3 | 10:06:07 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-3 | 10:06:07 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 7 | 1-3 | 10:06:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 10:06:13 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-4 | 10:06:14 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1100 |  |
| Jogador 7 | 1-4 | 10:06:16 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 7 | 1-4 | 10:06:16 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 1-4 | 10:06:17 | MOVE Board -> Board: Camille (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 10:06:17 | MOVE Board -> Board: Akali (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-4 | 10:06:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 10:06:22 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 10:06:24 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 10:06:25 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1700 |  |
| Jogador 7 | 2-1 | 10:06:26 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 7 | 2-1 | 10:06:26 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 7 | 2-1 | 10:06:27 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 7 | 2-1 | 10:06:27 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1100 |  |
| Jogador 7 | 2-1 | 10:06:27 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 7 | 2-2 | 10:06:31 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-2 | 10:06:31 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 7 | 2-2 | 10:06:34 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.3200 |  |
| Jogador 7 | 2-2 | 10:06:35 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.4300 |  |
| Jogador 7 | 2-2 | 10:06:36 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 2-2 | 10:06:36 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 7 | 2-2 | 10:06:37 | MOVE Board -> Board: Camille (i:2.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-3 | 10:06:40 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3200 |  |
| Jogador 7 | 2-3 | 10:06:41 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.3100 |  |
| Jogador 7 | 2-3 | 10:06:41 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 7 | 2-3 | 10:06:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-3 | 10:06:46 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5700 |  |
| Jogador 7 | 2-4 | 10:06:51 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 2-4 | 10:06:52 | VENDEU: Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Sabugueiro | DA_18_Akali_AD | -0.5800 |  |
| Jogador 7 | 2-4 | 10:06:52 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Hecarim (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Sabugueiro | DA_18_Akali_AD | 0.1100 |  |
| Jogador 7 | 2-4 | 10:06:53 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Hecarim (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Sabugueiro | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 2-4 | 10:06:53 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_18_Akali_AD | -0.1200 |  |
| Jogador 7 | 2-4 | 10:06:54 | MOVE Board -> Board: Hecarim (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-4 | 10:06:54 | MOVE Board -> Board: Shen (i:4.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_18_Akali_AD | -0.3000 |  |
| Jogador 7 | 2-4 | 10:06:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-5 | 10:07:03 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.5800 |  |
| Jogador 7 | 2-5 | 10:07:04 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.9000 |  |
| Jogador 7 | 2-5 | 10:07:04 | MOVE Bench -> Board: Alistar (i:4.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 7 | 2-5 | 10:07:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 7 | 2-5 | 10:07:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 7 | 2-5 | 10:07:05 | MOVE Board -> Board: Alistar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 7 | 2-5 | 10:07:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 7 | 2-5 | 10:07:07 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 2-5 | 10:07:07 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 7 | 2-6 | 10:07:17 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.8200 |  |
| Jogador 7 | 2-6 | 10:07:18 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0400 |  |
| Jogador 7 | 2-6 | 10:07:18 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 2-6 | 10:07:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 7 | 2-6 | 10:07:19 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.4400 |  |
| Jogador 7 | 2-6 | 10:07:20 | MOVE Board -> Board: Rammus (i:6.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 2-6 | 10:07:21 | MOVE Board -> Board: Alistar (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 2-6 | 10:07:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 2-7 | 10:07:34 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.7200 |  |
| Jogador 7 | 2-7 | 10:07:34 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.8400 |  |
| Jogador 7 | 2-7 | 10:07:35 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 7 | 2-7 | 10:07:36 | MOVE Board -> Board: Shen (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 2-7 | 10:07:36 | MOVE Board -> Board: Camille (i:2.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 2-7 | 10:07:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-1 | 10:07:50 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.2900 |  |
| Jogador 7 | 3-1 | 10:07:51 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-1 | 10:07:51 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-1 | 10:07:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 3-1 | 10:07:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-1 | 10:07:53 | MOVE Board -> Board: Camille (i:2.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-1 | 10:07:54 | MOVE Board -> Board: Alistar (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-1 | 10:07:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-2 | 10:08:09 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.7200 |  |
| Jogador 7 | 3-2 | 10:08:10 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.5000 |  |
| Jogador 7 | 3-2 | 10:08:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.8100 |  |
| Jogador 7 | 3-2 | 10:08:11 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 3-2 | 10:08:12 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.8400 |  |
| Jogador 7 | 3-2 | 10:08:12 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.3500 |  |
| Jogador 7 | 3-2 | 10:08:13 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 3-2 | 10:08:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 7 | 3-2 | 10:08:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 7 | 3-3 | 10:08:30 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 7 | 3-3 | 10:08:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 7 | 3-3 | 10:08:31 | VENDEU: Camille (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.5800 |  |
| Jogador 7 | 3-3 | 10:08:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 3-3 | 10:08:32 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.1600 |  |
| Jogador 7 | 3-3 | 10:08:32 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-3 | 10:08:32 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-3 | 10:08:33 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-4 | 10:08:52 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.7400 |  |
| Jogador 7 | 3-4 | 10:08:52 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.7300 |  |
| Jogador 7 | 3-4 | 10:08:53 | MOVE Board -> Board: Alistar (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-4 | 10:08:53 | MOVE Board -> Board: Shen (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 3-4 | 10:08:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-5 | 10:09:15 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-5 | 10:09:15 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-5 | 10:09:16 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-5 | 10:09:17 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-5 | 10:09:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-6 | 10:09:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.5300 |  |
| Jogador 7 | 3-6 | 10:09:43 | MOVE Board -> Board: Alistar (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-6 | 10:09:44 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-6 | 10:09:44 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-7 | 10:10:07 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 7 | 3-7 | 10:10:08 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 7 | 3-7 | 10:10:08 | VENDEU: Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.4700 |  |
| Jogador 7 | 3-7 | 10:10:09 | COMPROU: Ornn (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.7400 |  |
| Jogador 7 | 3-7 | 10:10:09 | VENDEU: Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 7 | 3-7 | 10:10:10 | COMPROU: Ornn (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.7700 |  |
| Jogador 7 | 3-7 | 10:10:10 | MOVE Board -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-7 | 10:10:11 | MOVE Board -> Board: Shen (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-7 | 10:10:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 4-1 | 10:10:33 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 4-1 | 10:10:34 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 4-1 | 10:10:34 | MOVE Board -> Board: Alistar (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Sabugueiro | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 4-1 | 10:10:35 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Sabugueiro | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 7 | 4-2 | 10:11:01 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Sabugueiro | DA_Fiddlesticks18 | 0.7500 |  |
| Jogador 7 | 4-2 | 10:11:02 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Sabugueiro | DA_Fiddlesticks18 | 0.7600 |  |
| Jogador 7 | 4-2 | 10:11:02 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Sabugueiro | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 4-2 | 10:11:03 | MOVE Board -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Sabugueiro | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 4-2 | 10:11:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 2 | Sabugueiro | DA_Fiddlesticks18 | -0.1100 |  |
| Jogador 7 | 4-3 | 10:11:29 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Sabugueiro | DA_18_Hecarim | 0.8200 |  |
| Jogador 7 | 4-3 | 10:11:30 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Sabugueiro | DA_18_Hecarim | 0.6000 |  |
| Jogador 7 | 4-3 | 10:11:30 | MOVE Board -> Board: Hecarim (i:12.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Sabugueiro | DA_18_Hecarim | -0.0200 |  |
| Jogador 7 | 4-3 | 10:11:31 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Sabugueiro | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-3 | 10:11:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Sabugueiro | DA_18_Hecarim | -0.1800 |  |
| Jogador 7 | 4-4 | 10:11:58 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Sabugueiro | DA_18_Hecarim | 0.1700 |  |
| Jogador 7 | 4-4 | 10:11:58 | MOVE Board -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Sabugueiro | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-4 | 10:11:59 | MOVE Board -> Board: Shen (i:4.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Sabugueiro | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-4 | 10:11:59 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Sabugueiro | DA_18_Hecarim | -0.1800 |  |
| Jogador 7 | 4-5 | 10:12:26 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Sabugueiro | DA_18_Hecarim | 0.6700 |  |
| Jogador 7 | 4-5 | 10:12:27 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Sabugueiro | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-5 | 10:12:27 | MOVE Board -> Board: Rammus (i:6.0) <-> Hecarim (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Sabugueiro | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-5 | 10:12:28 | MOVE Board -> Board: Hecarim (i:12.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Sabugueiro | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-5 | 10:12:28 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Sabugueiro | DA_18_Hecarim | -0.1900 |  |
| Jogador 7 | 4-6 | 10:12:58 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Sabugueiro | DA_18_Hecarim | 0.3200 |  |
| Jogador 7 | 4-6 | 10:12:59 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Sabugueiro | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-6 | 10:12:59 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Sabugueiro | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-6 | 10:13:00 | MOVE Board -> Board: Shen (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Sabugueiro | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-6 | 10:13:00 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Sabugueiro | DA_18_Hecarim | -0.0900 |  |
| Jogador 7 | 4-7 | 10:13:34 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Sabugueiro | DA_18_Hecarim | 0.0900 |  |
| Jogador 7 | 4-7 | 10:13:34 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Sabugueiro | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 4-7 | 10:13:35 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Sabugueiro | DA_18_Hecarim | -0.4000 |  |
| Jogador 7 | 4-7 | 10:13:35 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Hecarim (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Sabugueiro | DA_18_Hecarim | -0.3900 |  |
| Jogador 7 | 4-7 | 10:13:36 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Sabugueiro | DA_18_Hecarim | -0.1000 |  |
| Jogador 7 | 5-1 | 10:14:09 | MOVE Bench -> Board: Ornn (i:4.0) <-> Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 83 | 5 | Sabugueiro | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 5-1 | 10:14:09 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 83 | 5 | Sabugueiro | DA_18_Hecarim | -0.4100 |  |
| Jogador 7 | 5-1 | 10:14:10 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Ornn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 83 | 5 | Sabugueiro | DA_18_Hecarim | -0.3800 |  |
| Jogador 7 | 5-1 | 10:14:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 83 | 5 | Sabugueiro | DA_18_Hecarim | -0.1100 |  |
| Jogador 7 | 5-2 | 10:14:43 | VENDEU: Ornn (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 97 | 5 | Sabugueiro | DA_18_Hecarim | -0.5900 |  |
| Jogador 7 | 5-2 | 10:14:43 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Sabugueiro | DA_18_Hecarim | 0.9500 |  |
| Jogador 7 | 5-2 | 10:14:44 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Sabugueiro | DA_18_Hecarim | 0.9400 |  |
| Jogador 7 | 5-2 | 10:14:44 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Sabugueiro | DA_18_Hecarim | 0.2600 |  |
| Jogador 7 | 5-2 | 10:14:45 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Sabugueiro | DA_18_Hecarim | 0.5600 |  |
| Jogador 7 | 5-2 | 10:14:45 | MOVE Board -> Board: Hecarim (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Sabugueiro | DA_18_Hecarim | -0.0200 |  |
| Jogador 7 | 5-2 | 10:14:45 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Sabugueiro | DA_18_Hecarim | 0.3800 |  |
| Jogador 7 | 5-2 | 10:14:46 | MOVE Board -> Board: Shen (i:8.0) <-> Hecarim (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Sabugueiro | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 5-2 | 10:14:46 | MOVE Board -> Board: Hecarim (i:12.0) <-> Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Sabugueiro | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 5-3 | 10:15:18 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 97 | 5 | Sabugueiro | DA_18_Hecarim | 0.2900 |  |
| Jogador 7 | 5-3 | 10:15:19 | MOVE Board -> Board: Ezreal (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 97 | 5 | Sabugueiro | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 5-3 | 10:15:19 | MOVE Bench -> Board: Shen (i:4.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 97 | 5 | Sabugueiro | DA_18_Hecarim | -0.7700 |  |
| Jogador 7 | 5-3 | 10:15:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 97 | 5 | Sabugueiro | DA_18_Hecarim | -0.2800 |  |
| Jogador 7 | 5-4 | 10:15:57 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 104 | 5 | Sabugueiro | DA_18_Hecarim | 0.8100 |  |
| Jogador 7 | 5-4 | 10:15:57 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Sabugueiro | DA_18_Hecarim | -0.5800 |  |
| Jogador 7 | 5-4 | 10:15:58 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 110 | 5 | Sabugueiro | DA_18_Hecarim | 0.3700 |  |
| Jogador 7 | 5-4 | 10:15:58 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Hecarim (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 110 | 5 | Sabugueiro | DA_18_Hecarim | -0.3600 |  |
| Jogador 7 | 5-4 | 10:15:59 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 110 | 5 | Sabugueiro | DA_18_Hecarim | 0.0700 |  |
| Jogador 7 | 5-4 | 10:15:59 | MOVE Bench -> Board: Shen (i:4.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 110 | 5 | Sabugueiro | DA_18_Hecarim | -0.7700 |  |
| Jogador 7 | 5-4 | 10:16:00 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Hecarim (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 110 | 5 | Sabugueiro | DA_18_Hecarim | -0.3700 |  |
| Jogador 7 | 5-4 | 10:16:00 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 110 | 5 | Sabugueiro | DA_18_Hecarim | -0.1400 |  |
| Jogador 7 | 5-5 | 10:16:35 | VENDEU: LeBlanc (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 126 | 5 | Sabugueiro | DA_18_Hecarim | -0.6000 |  |
| Jogador 7 | 5-5 | 10:16:35 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Sabugueiro | DA_18_Hecarim | 0.8600 |  |
| Jogador 7 | 5-5 | 10:16:36 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Sabugueiro | DA_18_Hecarim | 0.0800 |  |
| Jogador 7 | 5-5 | 10:16:36 | MOVE Bench -> Board: Shen (i:4.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Sabugueiro | DA_18_Hecarim | -0.7700 |  |
| Jogador 7 | 5-5 | 10:16:36 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Hecarim (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Sabugueiro | DA_18_Hecarim | -0.3700 |  |
| Jogador 7 | 5-5 | 10:16:37 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Sabugueiro | DA_18_Hecarim | -0.1500 |  |
| Jogador 7 | 5-6 | 10:17:12 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Sabugueiro | DA_18_Hecarim | 0.0800 |  |
| Jogador 7 | 5-6 | 10:17:14 | MOVE Bench -> Board: Shen (i:4.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Sabugueiro | DA_18_Hecarim | -0.7700 |  |
| Jogador 7 | 5-6 | 10:17:14 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Sabugueiro | DA_18_Hecarim | 0.0700 |  |
| Jogador 7 | 5-6 | 10:17:15 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Hecarim (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Sabugueiro | DA_18_Hecarim | -0.4200 |  |
| Jogador 7 | 5-6 | 10:17:15 | MOVE Bench -> Board: Alistar (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Sabugueiro | DA_18_Hecarim | 0.0600 |  |
| Jogador 7 | 5-6 | 10:17:16 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Sabugueiro | DA_18_Hecarim | -0.3900 |  |
| Jogador 7 | 5-6 | 10:17:16 | MOVE Bench -> Board: Shen (i:4.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Sabugueiro | DA_18_Hecarim | 0.0700 |  |
| Jogador 7 | 5-6 | 10:17:17 | MOVE Bench -> Board: Alistar (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Sabugueiro | DA_18_Hecarim | 0.0600 |  |
| Jogador 7 | 5-6 | 10:17:17 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 136 | 5 | Sabugueiro | DA_18_Hecarim | -0.3900 |  |
| Jogador 7 | 5-7 | 10:18:02 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Rammus (i:6.0) (tabuleiro slot 24) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Sabugueiro | DA_18_Hecarim | 0.0900 |  |
| Jogador 7 | 5-7 | 10:18:02 | MOVE Bench -> Board: Shen (i:4.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Sabugueiro | DA_18_Hecarim | -0.7500 |  |
| Jogador 7 | 5-7 | 10:18:02 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Sabugueiro | DA_18_Hecarim | 0.0900 |  |
| Jogador 7 | 5-7 | 10:18:03 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Sabugueiro | DA_18_Hecarim | -0.3500 |  |
| Jogador 7 | 5-7 | 10:18:03 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 150 | 5 | Sabugueiro | DA_18_Hecarim | -0.5900 |  |
| Jogador 7 | 5-7 | 10:18:04 | COMPROU: Ezreal (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 146 | 5 | Sabugueiro | DA_18_Hecarim | 0.8800 |  |
| Jogador 7 | 5-7 | 10:18:04 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 146 | 5 | Sabugueiro | DA_18_Hecarim | 0.0900 |  |
| Jogador 7 | 5-7 | 10:18:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 142 | 5 | Sabugueiro | DA_18_Hecarim | 0.0600 |  |
| Jogador 7 | 5-7 | 10:18:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 138 | 5 | Sabugueiro | DA_18_Hecarim | 0.0600 |  |
| Jogador 7 | 6-1 | 10:18:45 | VENDEU: Alistar (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 152 | 5 | Sabugueiro | DA_18_Hecarim | -0.5700 |  |
| Jogador 7 | 6-1 | 10:18:45 | COMPROU: Shen (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 150 | 5 | Sabugueiro | DA_18_Hecarim | 0.9400 |  |
| Jogador 7 | 6-1 | 10:18:46 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 150 | 5 | Sabugueiro | DA_18_Hecarim | 0.4100 |  |
| Jogador 7 | 6-1 | 10:18:46 | COMPROU: Diana (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 147 | 5 | Sabugueiro | DA_18_Hecarim | 0.0900 |  |
| Jogador 7 | 6-1 | 10:18:47 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Shen (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 147 | 5 | Sabugueiro | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 6-1 | 10:18:47 | MOVE Board -> Board: Shen (i:8.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 147 | 5 | Sabugueiro | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 6-1 | 10:18:48 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Ezreal (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 147 | 5 | Sabugueiro | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 6-1 | 10:18:48 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 147 | 5 | Sabugueiro | DA_18_Hecarim | -0.1800 |  |
| Jogador 7 | 6-2 | 10:19:29 | VENDEU: Diana (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 162 | 5 | Sabugueiro | DA_18_Hecarim | -0.0300 |  |
| Jogador 7 | 6-2 | 10:19:29 | COMPROU: Rammus (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 159 | 5 | Sabugueiro | DA_18_Hecarim | 0.4500 |  |
| Jogador 7 | 6-2 | 10:19:29 | VENDEU: Alistar (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 161 | 5 | Sabugueiro | DA_18_Hecarim | -0.0900 |  |
| Jogador 7 | 6-2 | 10:19:30 | COMPROU: Rammus (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 158 | 5 | Sabugueiro | DA_18_Hecarim | 0.8700 |  |
| Jogador 7 | 6-2 | 10:19:30 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Kog'Maw (i:6.0) (tabuleiro slot 19) | WINSTREAK | WINSTREAK: preservar vantagem atual | 158 | 5 | Sabugueiro | DA_18_Hecarim | 0.0900 |  |
| Jogador 7 | 6-2 | 10:19:31 | COMPROU: Azuporã (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 154 | 5 | Sabugueiro | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 6-2 | 10:19:31 | MOVE Bench -> Board: Rammus (i:12.0) <-> Ezreal (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 154 | 5 | Sabugueiro | DA_18_Hecarim | -0.0900 |  |
| Jogador 7 | 6-2 | 10:19:32 | MOVE Board -> Board: Rammus (i:12.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 154 | 5 | Sabugueiro | DA_18_Hecarim | -0.0200 |  |
| Jogador 7 | 6-2 | 10:19:32 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 154 | 5 | Sabugueiro | DA_18_Hecarim | -0.1900 |  |
| Jogador 7 | 6-3 | 10:20:14 | COMPROU: Alistar (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 163 | 5 | Sabugueiro | DA_18_Hecarim | 0.3800 |  |
| Jogador 7 | 6-3 | 10:20:15 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Hecarim (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 163 | 5 | Sabugueiro | DA_18_Hecarim | -0.6500 |  |
| Jogador 7 | 6-3 | 10:20:15 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Shen (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 163 | 5 | Sabugueiro | DA_18_Hecarim | 0.0600 |  |
| Jogador 7 | 6-3 | 10:20:16 | MOVE Bench -> Board: Shen (i:8.0) <-> Azuporã (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 163 | 5 | Sabugueiro | DA_18_Hecarim | 0.0800 |  |
| Jogador 7 | 6-3 | 10:20:16 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Hecarim (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 163 | 5 | Sabugueiro | DA_18_Hecarim | -0.6600 |  |
| Jogador 7 | 6-3 | 10:20:16 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Shen (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 163 | 5 | Sabugueiro | DA_18_Hecarim | 0.0500 |  |
| Jogador 7 | 6-3 | 10:20:17 | MOVE Bench -> Board: Shen (i:8.0) <-> Shen (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 163 | 5 | Sabugueiro | DA_18_Hecarim | 0.0500 |  |
| Jogador 7 | 6-3 | 10:20:17 | MOVE Bench -> Board: Shen (i:4.0) <-> Hecarim (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 163 | 5 | Sabugueiro | DA_18_Hecarim | -0.7200 |  |
| Jogador 7 | 6-3 | 10:20:18 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Azuporã (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 163 | 5 | Sabugueiro | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 6-4 | 10:21:03 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Shen (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 174 | 5 | Sabugueiro | DA_18_Hecarim | -0.4000 |  |
| Jogador 7 | 6-4 | 10:21:03 | MOVE Bench -> Board: Shen (i:4.0) <-> Hecarim (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 174 | 5 | Sabugueiro | DA_18_Hecarim | -0.7400 |  |
| Jogador 7 | 6-4 | 10:21:04 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 174 | 5 | Sabugueiro | DA_18_Hecarim | -0.2100 |  |
| Jogador 7 | 6-5 | 10:21:48 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 184 | 5 | Sabugueiro | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 6-5 | 10:21:48 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Shen (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 184 | 5 | Sabugueiro | DA_18_Hecarim | -0.4100 |  |
| Jogador 7 | 6-5 | 10:21:49 | MOVE Bench -> Board: Shen (i:8.0) <-> Hecarim (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 184 | 5 | Sabugueiro | DA_18_Hecarim | -0.7000 |  |
| Jogador 7 | 6-5 | 10:21:49 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 184 | 5 | Sabugueiro | DA_18_Hecarim | -0.2600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 6-6 | 10:22:34 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 195 | 5 | Sabugueiro | DA_18_Hecarim | 0.0800 |  |
| Jogador 7 | 6-6 | 10:22:34 | MOVE Bench -> Board: Shen (i:4.0) <-> Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 195 | 5 | Sabugueiro | DA_18_Hecarim | -0.5300 |  |
| Jogador 7 | 6-6 | 10:22:34 | VENDEU: Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 200 | 5 | Sabugueiro | DA_18_Hecarim | -0.7000 |  |
| Jogador 7 | 6-6 | 10:22:35 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 197 | 5 | Sabugueiro | DA_18_Hecarim | 0.2300 |  |
| Jogador 7 | 6-6 | 10:22:35 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Kog'Maw (i:6.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 197 | 5 | Sabugueiro | DA_18_Hecarim | 0.0700 |  |
| Jogador 7 | 6-6 | 10:22:35 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Kog'Maw (i:6.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 197 | 5 | Sabugueiro | DA_18_Hecarim | 0.0700 |  |
| Jogador 7 | 6-6 | 10:22:36 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 197 | 5 | Sabugueiro | DA_18_Hecarim | -0.6300 |  |
| Jogador 7 | 6-6 | 10:22:36 | MOVE Bench -> Board: Shen (i:4.0) <-> Hecarim (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 197 | 5 | Sabugueiro | DA_18_Hecarim | -0.7600 |  |
| Jogador 7 | 6-6 | 10:22:37 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 197 | 5 | Sabugueiro | DA_18_Hecarim | -0.6500 |  |
| Jogador 7 | 6-7 | 10:23:19 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Xayah (i:2.0) (tabuleiro slot 23) | ALL_IN | HP crítico: gastar para sobreviver | 208 | 5 | Sabugueiro | DA_18_Hecarim | 0.0900 |  |
| Jogador 7 | 6-7 | 10:23:20 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 208 | 5 | Sabugueiro | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 6-7 | 10:23:20 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 208 | 5 | Sabugueiro | DA_18_Hecarim | -0.6500 |  |
| Jogador 7 | 6-7 | 10:23:21 | MOVE Bench -> Board: Shen (i:4.0) <-> Hecarim (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 208 | 5 | Sabugueiro | DA_18_Hecarim | -0.7600 |  |
| Jogador 7 | 6-7 | 10:23:21 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 208 | 5 | Sabugueiro | DA_18_Hecarim | -0.8200 |  |
| Jogador 8 | ? | 10:05:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5900 |  |
| Jogador 8 | ? | 10:05:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 10:05:50 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 10:05:51 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0100 |  |
| Jogador 8 | 1-1 | 10:05:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 10:05:56 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-2 | 10:05:58 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | 1-2 | 10:05:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-2 | 10:06:03 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.4100 |  |
| Jogador 8 | 1-3 | 10:06:05 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.9300 |  |
| Jogador 8 | 1-3 | 10:06:06 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 10:06:06 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.3000 |  |
| Jogador 8 | 1-3 | 10:06:07 | MOVE Board -> Board: Veigar (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.2500 |  |
| Jogador 8 | 1-3 | 10:06:07 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | 1-3 | 10:06:09 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9900 |  |
| Jogador 8 | 1-3 | 10:06:09 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 10:06:10 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-3 | 10:06:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 10:06:13 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Xayah | 1.0300 |  |
| Jogador 8 | 1-4 | 10:06:14 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 1.0900 |  |
| Jogador 8 | 1-4 | 10:06:16 | MOVE Bench -> Board: Leona (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.4400 |  |
| Jogador 8 | 1-4 | 10:06:16 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.2700 |  |
| Jogador 8 | 1-4 | 10:06:17 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.1400 |  |
| Jogador 8 | 1-4 | 10:06:17 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.1400 |  |
| Jogador 8 | 1-4 | 10:06:18 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 8 | 1-4 | 10:06:18 | MOVE Board -> Board: Leona (i:4.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0200 |  |
| Jogador 8 | 1-4 | 10:06:19 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 8 | 1-4 | 10:06:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 2-1 | 10:06:22 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Xayah | 0.2700 |  |
| Jogador 8 | 2-1 | 10:06:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.2000 |  |
| Jogador 8 | 2-1 | 10:06:25 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 2-1 | 10:06:26 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Leona | -0.2100 |  |
| Jogador 8 | 2-1 | 10:06:26 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | -0.0700 |  |
| Jogador 8 | 2-1 | 10:06:27 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 0.0900 |  |
| Jogador 8 | 2-1 | 10:06:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Leona | -0.0400 |  |
| Jogador 8 | 2-1 | 10:06:27 | MOVE Board -> Board: Rakan (i:2.0) <-> Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-2 | 10:06:31 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 0.9800 |  |
| Jogador 8 | 2-2 | 10:06:31 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Leona | 0.9100 |  |
| Jogador 8 | 2-2 | 10:06:34 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Leona | 0.2400 |  |
| Jogador 8 | 2-2 | 10:06:35 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Leona | -0.0800 |  |
| Jogador 8 | 2-2 | 10:06:36 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Leona | -0.0500 |  |
| Jogador 8 | 2-2 | 10:06:36 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 0.2600 |  |
| Jogador 8 | 2-2 | 10:06:37 | MOVE Board -> Board: Leona (i:4.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-3 | 10:06:40 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Leona | 0.0900 |  |
| Jogador 8 | 2-3 | 10:06:41 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Leona | 0.1300 |  |
| Jogador 8 | 2-3 | 10:06:41 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Leona | -0.0400 |  |
| Jogador 8 | 2-3 | 10:06:42 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Leona | 0.4000 |  |
| Jogador 8 | 2-3 | 10:06:46 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Leona | -0.0200 |  |
| Jogador 8 | 2-4 | 10:06:51 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Leona | 0.8500 |  |
| Jogador 8 | 2-4 | 10:06:52 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 2-4 | 10:06:52 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Leona | 0.9500 |  |
| Jogador 8 | 2-4 | 10:06:53 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Leona | 0.0100 |  |
| Jogador 8 | 2-4 | 10:06:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 2-4 | 10:06:54 | MOVE Board -> Board: Leona (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 2-4 | 10:06:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-5 | 10:07:03 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Leona | 0.9000 |  |
| Jogador 8 | 2-5 | 10:07:04 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Leona | -0.0400 |  |
| Jogador 8 | 2-5 | 10:07:04 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Leona | -0.5000 |  |
| Jogador 8 | 2-5 | 10:07:05 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Leona | -0.0400 |  |
| Jogador 8 | 2-5 | 10:07:05 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-5 | 10:07:05 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Leona | -0.0200 |  |
| Jogador 8 | 2-5 | 10:07:06 | MOVE Board -> Board: Rakan (i:2.0) <-> Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Leona | -0.0100 |  |
| Jogador 8 | 2-5 | 10:07:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-6 | 10:07:17 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Enfeitiçador | DA_18_Leona | -0.0500 |  |
| Jogador 8 | 2-6 | 10:07:18 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_18_Leona | 0.8300 |  |
| Jogador 8 | 2-6 | 10:07:18 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Enfeitiçador | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-6 | 10:07:19 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Leona | -0.0400 |  |
| Jogador 8 | 2-6 | 10:07:19 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Leona | -0.0300 |  |
| Jogador 8 | 2-6 | 10:07:20 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Leona | 0.1300 |  |
| Jogador 8 | 2-6 | 10:07:21 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Colosso | DA_18_Leona | -0.5100 |  |
| Jogador 8 | 2-6 | 10:07:21 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Leona | 0.0800 |  |
| Jogador 8 | 2-6 | 10:07:21 | MOVE Board -> Board: Leona (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-7 | 10:07:34 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Leona | 0.2600 |  |
| Jogador 8 | 2-7 | 10:07:34 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Leona | -0.0200 |  |
| Jogador 8 | 2-7 | 10:07:35 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Leona | 0.2900 |  |
| Jogador 8 | 2-7 | 10:07:36 | MOVE Bench -> Board: Varus (i:2.0) <-> Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Leona | -0.4100 |  |
| Jogador 8 | 2-7 | 10:07:36 | VENDEU: Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_18_Tristana | -0.3700 |  |
| Jogador 8 | 2-7 | 10:07:37 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_18_Tristana | 0.0500 |  |
| Jogador 8 | 2-7 | 10:07:37 | MOVE Bench -> Board: Lillia (i:8.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_18_Tristana | -0.3700 |  |
| Jogador 8 | 2-7 | 10:07:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 2-7 | 10:07:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-1 | 10:07:50 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Tristana | 0.0100 |  |
| Jogador 8 | 3-1 | 10:07:51 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Tristana | 0.7900 |  |
| Jogador 8 | 3-1 | 10:07:51 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_18_Tristana | -0.5300 |  |
| Jogador 8 | 3-1 | 10:07:52 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Tristana | 0.2800 |  |
| Jogador 8 | 3-1 | 10:07:53 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_18_Tristana | -0.5300 |  |
| Jogador 8 | 3-1 | 10:07:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Tristana | 0.0600 |  |
| Jogador 8 | 3-1 | 10:07:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Colosso | DA_18_Tristana | 0.0800 |  |
| Jogador 8 | 3-1 | 10:07:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Colosso | DA_18_Tristana | -0.1100 |  |
| Jogador 8 | 3-1 | 10:07:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 1 | Colosso | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 3-2 | 10:08:09 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Tristana | -0.3100 |  |
| Jogador 8 | 3-2 | 10:08:10 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Tristana | 0.8300 |  |
| Jogador 8 | 3-2 | 10:08:10 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Tristana | 0.3400 |  |
| Jogador 8 | 3-2 | 10:08:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 3-2 | 10:08:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 3-2 | 10:08:12 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Tristana | -0.0800 |  |
| Jogador 8 | 3-2 | 10:08:13 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-2 | 10:08:13 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-3 | 10:08:30 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Tristana | 0.2000 |  |
| Jogador 8 | 3-3 | 10:08:30 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Tristana | 0.0200 |  |
| Jogador 8 | 3-3 | 10:08:31 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-3 | 10:08:31 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-3 | 10:08:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-4 | 10:08:52 | VENDEU: Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Tristana | -0.5000 |  |
| Jogador 8 | 3-4 | 10:08:52 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Tristana | 0.6500 |  |
| Jogador 8 | 3-4 | 10:08:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-4 | 10:08:53 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-4 | 10:08:54 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-4 | 10:08:54 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-4 | 10:08:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-5 | 10:09:15 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Tristana | 0.0700 |  |
| Jogador 8 | 3-5 | 10:09:15 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Tristana | 0.1100 |  |
| Jogador 8 | 3-5 | 10:09:16 | MOVE Board -> Board: Yorick (i:2.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-5 | 10:09:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-5 | 10:09:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Tristana | 0.0800 |  |
| Jogador 8 | 3-5 | 10:09:18 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Tristana | -0.0600 |  |
| Jogador 8 | 3-5 | 10:09:19 | MOVE Board -> Board: Sejuani (i:4.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-5 | 10:09:19 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-6 | 10:09:43 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Tristana | 0.1500 |  |
| Jogador 8 | 3-6 | 10:09:43 | MOVE Board -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-6 | 10:09:44 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-6 | 10:09:44 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-7 | 10:10:07 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Tristana | 0.1700 |  |
| Jogador 8 | 3-7 | 10:10:08 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Tristana | 0.1100 |  |
| Jogador 8 | 3-7 | 10:10:08 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Tristana | 0.0300 |  |
| Jogador 8 | 3-7 | 10:10:09 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Tristana | 0.6500 |  |
| Jogador 8 | 3-7 | 10:10:09 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-7 | 10:10:10 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-7 | 10:10:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-1 | 10:10:33 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 0 | Colosso | DA_18_Tristana | -0.0700 |  |
| Jogador 8 | 4-1 | 10:10:34 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_18_Tristana | 0.7600 |  |
| Jogador 8 | 4-1 | 10:10:34 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-1 | 10:10:35 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 4-1 | 10:10:36 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_18_Tristana | -0.1000 |  |
| Jogador 8 | 4-2 | 10:11:01 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_18_Tristana | 0.7100 |  |
| Jogador 8 | 4-2 | 10:11:02 | COMPROU: Soraka (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Colosso | DA_18_Tristana | -0.1000 |  |
| Jogador 8 | 4-2 | 10:11:02 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 1 | Colosso | DA_18_Tristana | -0.0800 |  |
| Jogador 8 | 4-2 | 10:11:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 1 | Colosso | DA_18_Tristana | -0.0900 |  |
| Jogador 8 | 4-2 | 10:11:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 1 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 4-2 | 10:11:04 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 1 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 4-2 | 10:11:04 | MOVE Board -> Board: Yorick (i:2.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 1 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-2 | 10:11:04 | MOVE Board -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 1 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 4-2 | 10:11:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 1 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-3 | 10:11:29 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Tristana | 0.3400 |  |
| Jogador 8 | 4-3 | 10:11:30 | VENDEU: Diana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Tristana | -0.4900 |  |
| Jogador 8 | 4-3 | 10:11:30 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Tristana | 0.5400 |  |
| Jogador 8 | 4-3 | 10:11:31 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-3 | 10:11:31 | MOVE Board -> Board: Sejuani (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 4-3 | 10:11:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-4 | 10:11:58 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_18_Tristana | 0.7700 |  |
| Jogador 8 | 4-4 | 10:11:58 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Tristana | 0.2100 |  |
| Jogador 8 | 4-4 | 10:11:59 | MOVE Bench -> Board: LeBlanc (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Tristana | 0.4400 |  |
| Jogador 8 | 4-4 | 10:11:59 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Tristana | -0.0700 |  |
| Jogador 8 | 4-4 | 10:12:00 | MOVE Board -> Board: LeBlanc (i:8.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Tristana | 0.0100 |  |
| Jogador 8 | 4-4 | 10:12:00 | MOVE Board -> Board: Yorick (i:2.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 4-4 | 10:12:00 | MOVE Board -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 4-4 | 10:12:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-5 | 10:12:26 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Colosso | DA_18_Tristana | 0.8000 |  |
| Jogador 8 | 4-5 | 10:12:27 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Colosso | DA_18_Tristana | -0.5800 |  |
| Jogador 8 | 4-5 | 10:12:27 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Colosso | DA_18_Tristana | 0.8300 |  |
| Jogador 8 | 4-5 | 10:12:28 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_Tristana | 0.1800 |  |
| Jogador 8 | 4-5 | 10:12:28 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> LeBlanc (i:8.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_Tristana | 0.1300 |  |
| Jogador 8 | 4-5 | 10:12:29 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-5 | 10:12:29 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-5 | 10:12:29 | MOVE Bench -> Board: Soraka (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Tristana | -0.3700 |  |
| Jogador 8 | 4-5 | 10:12:30 | MOVE Board -> Board: Soraka (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 4-6 | 10:12:58 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Colosso | DA_18_Tristana | -0.4000 |  |
| Jogador 8 | 4-6 | 10:12:59 | MOVE Bench -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Colosso | DA_18_Tristana | -0.5600 |  |
| Jogador 8 | 4-6 | 10:12:59 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 7 | 0 | Colosso | DA_18_Tristana | -0.3200 |  |
| Jogador 8 | 4-7 | 10:13:34 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Colosso | DA_18_Tristana | 0.8700 |  |
| Jogador 8 | 4-7 | 10:13:34 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> LeBlanc (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Colosso | DA_18_Tristana | 0.1700 |  |
| Jogador 8 | 4-7 | 10:13:35 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> LeBlanc (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Colosso | DA_18_Tristana | 0.1700 |  |
| Jogador 8 | 4-7 | 10:13:35 | MOVE Bench -> Board: Veigar (i:2.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Colosso | DA_18_Tristana | 0.1000 |  |
| Jogador 8 | 4-7 | 10:13:36 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Colosso | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 4-7 | 10:13:36 | MOVE Bench -> Board: Lillia (i:8.0) <-> Veigar (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Colosso | DA_18_Tristana | -0.4100 |  |
| Jogador 8 | 4-7 | 10:13:37 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 10 | 0 | Colosso | DA_18_Tristana | -0.3200 |  |
| Jogador 8 | 5-1 | 10:14:09 | MOVE Bench -> Board: Veigar (i:2.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Colosso | DA_18_Tristana | 0.0900 |  |
| Jogador 8 | 5-1 | 10:14:09 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Lillia (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Colosso | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 5-1 | 10:14:10 | MOVE Bench -> Board: Lillia (i:8.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Colosso | DA_18_Tristana | -0.4100 |  |
| Jogador 8 | 5-1 | 10:14:10 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 17 | 1 | Colosso | DA_18_Tristana | -0.4600 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 35 | 41 | 205 | 35 | 17 | 235 | 8 | 49 |
| Jogador 2 | 33 | 37 | 185 | 33 | 17 | 205 | 6 | 46 |
| Jogador 3 | 31 | 31 | 155 | 31 | 21 | 176 | 4 | 23 |
| Jogador 4 | 20 | 20 | 100 | 20 | 13 | 108 | 4 | 16 |
| Jogador 5 | 40 | 52 | 260 | 40 | 19 | 287 | 11 | 54 |
| Jogador 6 | 24 | 26 | 130 | 24 | 15 | 135 | 11 | 28 |
| Jogador 7 | 40 | 40 | 200 | 40 | 19 | 249 | 4 | 46 |
| Jogador 8 | 27 | 27 | 135 | 27 | 16 | 180 | 6 | 37 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 235 | 235 | 235 | 0 | 225 | 0 | 235 | 235 | 235 | 56/41 |
| Jogador 2 | 205 | 205 | 205 | 0 | 194 | 0 | 205 | 205 | 205 | 54/42 |
| Jogador 3 | 176 | 176 | 176 | 0 | 167 | 0 | 176 | 176 | 176 | 39/25 |
| Jogador 4 | 108 | 108 | 108 | 0 | 102 | 0 | 108 | 108 | 108 | 28/14 |
| Jogador 5 | 287 | 287 | 287 | 0 | 273 | 0 | 287 | 287 | 287 | 82/67 |
| Jogador 6 | 135 | 135 | 135 | 0 | 129 | 0 | 135 | 135 | 135 | 38/24 |
| Jogador 7 | 249 | 249 | 249 | 0 | 235 | 0 | 249 | 249 | 249 | 54/38 |
| Jogador 8 | 180 | 180 | 180 | 0 | 172 | 0 | 180 | 180 | 180 | 55/42 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.511091411113739 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23841141164302826 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25075557827949524 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2877546548843384 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 34 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4132702946662903 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 46 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0389703512191772 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 47 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0380680561065674 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03983444347977638 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016042277216911316 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1456615924835205 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 51 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 52 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1169661283493042 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.35619786381721497 | 0.0 | 0.0 | +57652644-f861-47bc-addd-90760a272b22 / -— |
| Jogador 1 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 4.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.21774645149707794 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 62 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22148685157299042 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 63 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20731906592845917 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1227799654006958 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 65 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1904938966035843 | 0.0 | 0.0 | +3a74be8d-bf7c-4449-9f1b-d76521e73e6f / -— |
| Jogador 1 | 2-1 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49191227555274963 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2546391785144806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 68 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 70 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8030749559402466 | 0.0 | 0.0 | +7aea963f-f0a4-4fa2-8da0-cc5eb260f665 / -— |
| Jogador 1 | 2-2 | 71 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33169129490852356 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 72 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 73 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16752178966999054 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 74 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 79 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9566535353660583 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 80 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8294900059700012 | 0.0 | 0.0 | +ff10e482-7085-4e73-8a0c-fdd3f4938128 / -3a74be8d-bf7c-4449-9f1b-d76521e73e6f,7aea963f-f0a4-4fa2-8da0-cc5eb260f665 |
| Jogador 1 | 2-3 | 81 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3163377344608307 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 82 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29275092482566833 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 83 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03715073689818382 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 84 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14899574220180511 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 85 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 87 | BUY | STABILIZE | 95.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33024102449417114 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -— |
| Jogador 1 | 2-4 | 88 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2979823648929596 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 89 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013912511989474297 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 91 | PASS | STABILIZE | 95.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7949658632278442 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 94 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 8 | 0 | 10.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7445265650749207 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 4 | 8 | 0 | 14.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039799999445676804 | 0.0 | 0.0 | +— / -ff10e482-7085-4e73-8a0c-fdd3f4938128 |
| Jogador 1 | 2-5 | 96 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 13 | 1 | 14.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.044577665627002716 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 13 | 1 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41878819465637207 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 98 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 13 | 1 | 10.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4107769727706909 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 13 | 1 | 14.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07778894901275635 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 13 | 1 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10035765171051025 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 102 | BUY | STABILIZE | 90.0 | 5 | 19 | 1 | 10.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499941468238831 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 18 | 1 | 6.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4731622040271759 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 18 | 1 | 8.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5391775369644165 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 105 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 18 | 1 | 8.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24029980599880219 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 106 | BUY | STABILIZE | 90.0 | 5 | 18 | 1 | 10.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07133190333843231 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 107 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 15 | 1 | 10.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4003496468067169 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 108 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 15 | 1 | 14.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23196035623550415 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 109 | PASS | STABILIZE | 90.0 | 5 | 15 | 1 | 14.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 112 | BUY | STABILIZE | 85.0 | 5 | 22 | 2 | 18.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.897922694683075 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -— |
| Jogador 1 | 2-7 | 113 | BUY | STABILIZE | 85.0 | 5 | 21 | 2 | 18.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23479942977428436 | 0.0 | 0.0 | +07130d94-c79f-4052-b3e9-7f867421f01b / -— |
| Jogador 1 | 2-7 | 114 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 19 | 1 | 18.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 19 | 1 | 18.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10272783786058426 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 116 | PASS | STABILIZE | 85.0 | 5 | 19 | 1 | 18.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 85.0 | 5 | 26 | 2 | 18.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2242061346769333 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 123 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 26 | 2 | 18.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09955193102359772 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 124 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 26 | 2 | 18.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011223400942981243 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 26 | 2 | 18.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1689412146806717 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 126 | PASS | STABILIZE | 85.0 | 5 | 26 | 2 | 18.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 132 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 34 | 3 | 18.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3342956602573395 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 133 | SELL | STABILIZE | 73.0 | 5 | 34 | 3 | 22.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -af132466-c7bd-40ad-9848-b79d59a5915c |
| Jogador 1 | 3-2 | 134 | EQUIP_FROM_INVENTORY | STABILIZE | 73.0 | 5 | 37 | 3 | 22.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13117896020412445 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 135 | EQUIP_FROM_INVENTORY | STABILIZE | 73.0 | 5 | 37 | 3 | 22.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14237388968467712 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 136 | BUY | STABILIZE | 73.0 | 5 | 37 | 3 | 22.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09056029468774796 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 137 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 33 | 3 | 22.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3402438163757324 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 138 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 33 | 3 | 20.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6911530494689941 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 139 | PASS | STABILIZE | 73.0 | 5 | 33 | 3 | 22.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026499999687075615 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 142 | SELL | STABILIZE | 63.0 | 5 | 42 | 4 | 22.0 | Inferno/DA_18_Ornn | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -c448b2c1-7854-4c8c-a51b-eca2791eb639 |
| Jogador 1 | 3-3 | 143 | BUY | STABILIZE | 63.0 | 5 | 45 | 4 | 22.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18095050752162933 | 0.0 | 0.0 | +bb3be648-cee1-4b75-b472-59653324b9bd / -— |
| Jogador 1 | 3-3 | 144 | MOVE_BENCH | STABILIZE | 63.0 | 5 | 42 | 4 | 22.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1582224816083908 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 145 | BUY_XP | STABILIZE | 63.0 | 5 | 42 | 4 | 24.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06588699668645859 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 146 | BUY_XP | STABILIZE | 63.0 | 5 | 38 | 3 | 24.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01411299966275692 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 147 | BUY_XP | STABILIZE | 63.0 | 5 | 34 | 3 | 24.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1575849950313568 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 148 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 30 | 3 | 24.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40192022919654846 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 149 | BUY | FAST8 | 63.0 | 6 | 30 | 3 | 28.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09367422759532928 | 0.0 | 0.0 | +45450b46-63b4-488f-9469-3348c6da8f4b / -— |
| Jogador 1 | 3-3 | 150 | MOVE_BOARD | FAST8 | 63.0 | 6 | 28 | 2 | 28.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22837364673614502 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 152 | MOVE_BOARD | FAST8 | 63.0 | 6 | 36 | 3 | 28.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18926887214183807 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 153 | MOVE_BOARD | FAST8 | 63.0 | 6 | 36 | 3 | 28.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02418285422027111 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 154 | MOVE_BOARD | FAST8 | 63.0 | 6 | 36 | 3 | 28.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013008544221520424 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 155 | MOVE_BOARD | FAST8 | 63.0 | 6 | 36 | 3 | 28.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 156 | PASS | FAST8 | 63.0 | 6 | 36 | 3 | 28.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 162 | SELL | FAST8 | 63.0 | 6 | 44 | 4 | 28.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017540173139423132 | 0.0 | 0.0 | +— / -45450b46-63b4-488f-9469-3348c6da8f4b |
| Jogador 1 | 3-5 | 163 | BUY | FAST8 | 63.0 | 6 | 46 | 4 | 28.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8109135627746582 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 44 | 4 | 24.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6044808626174927 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 165 | BUY | FAST8 | 63.0 | 6 | 44 | 4 | 32.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0022913666907697916 | 0.0 | 0.0 | +a9184317-58b7-4804-9aef-3e2c08c20935 / -— |
| Jogador 1 | 3-5 | 166 | MOVE_BOARD | FAST8 | 63.0 | 6 | 43 | 4 | 32.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009271083399653435 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 167 | MOVE_BOARD | FAST8 | 63.0 | 6 | 43 | 4 | 32.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 168 | PASS | FAST8 | 63.0 | 6 | 43 | 4 | 32.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12950000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 172 | BUY | FAST8 | 63.0 | 6 | 54 | 5 | 32.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2710726261138916 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -— |
| Jogador 1 | 3-6 | 173 | SELL | FAST8 | 63.0 | 6 | 52 | 5 | 32.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010333333164453506 | 0.0 | 0.0 | +— / -a9184317-58b7-4804-9aef-3e2c08c20935 |
| Jogador 1 | 3-6 | 174 | BUY | FAST8 | 63.0 | 6 | 53 | 5 | 32.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7914958596229553 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 175 | MOVE_BOARD | FAST8 | 63.0 | 6 | 51 | 5 | 32.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00915546715259552 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 176 | MOVE_BOARD | FAST8 | 63.0 | 6 | 51 | 5 | 32.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012431678362190723 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 177 | MOVE_BOARD | FAST8 | 63.0 | 6 | 51 | 5 | 32.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015011620707809925 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 178 | PASS | FAST8 | 63.0 | 6 | 51 | 5 | 32.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05633125081658363 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 182 | SELL | FAST8 | 53.0 | 6 | 61 | 5 | 32.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015218311920762062 | 0.0 | 0.0 | +— / -145f7470-8c0f-4957-b8d6-97939ddaeba1 |
| Jogador 1 | 3-7 | 183 | BUY | FAST8 | 53.0 | 6 | 65 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6064096093177795 | 0.0 | 0.0 | +c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 / -— |
| Jogador 1 | 3-7 | 184 | MOVE_BOARD | FAST8 | 53.0 | 6 | 63 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13536594808101654 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 185 | BUY_XP | FAST8 | 53.0 | 6 | 63 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022210000082850456 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 186 | MOVE_BOARD | FAST8 | 53.0 | 6 | 59 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13484534621238708 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 187 | MOVE_BOARD | FAST8 | 53.0 | 6 | 59 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014859398826956749 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 188 | MOVE_BOARD | FAST8 | 53.0 | 6 | 59 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 189 | PASS | FAST8 | 53.0 | 6 | 59 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1577138602733612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 53.0 | 6 | 69 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1791875958442688 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 53.0 | 6 | 69 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22964052855968475 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 194 | MOVE_BOARD | FAST8 | 53.0 | 6 | 69 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0003435914986766875 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 195 | MOVE_BENCH | FAST8 | 53.0 | 6 | 69 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5330690741539001 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 196 | MOVE_BENCH | FAST8 | 53.0 | 6 | 69 | 5 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08501937240362167 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 197 | MOVE_BOARD | FAST8 | 53.0 | 6 | 69 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015010697767138481 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 198 | MOVE_BOARD | FAST8 | 53.0 | 6 | 69 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 199 | PASS | FAST8 | 53.0 | 6 | 69 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09206952899694443 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 202 | SELL | FAST8 | 53.0 | 6 | 80 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.436599999666214 | 0.0 | 0.0 | +— / -07130d94-c79f-4052-b3e9-7f867421f01b |
| Jogador 1 | 4-2 | 203 | BUY | FAST8 | 53.0 | 6 | 82 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3106820285320282 | 0.0 | 0.0 | +6fa83356-562b-4a26-a77d-3e989089e70a / -— |
| Jogador 1 | 4-2 | 204 | MOVE_BOARD | FAST8 | 53.0 | 6 | 81 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 205 | MOVE_BOARD | FAST8 | 53.0 | 6 | 81 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014994652941823006 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 206 | PASS | FAST8 | 53.0 | 6 | 81 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.100680410861969 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 212 | SELL | FAST8 | 53.0 | 6 | 93 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 |
| Jogador 1 | 4-3 | 213 | BUY | FAST8 | 53.0 | 6 | 95 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8925724625587463 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8,d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 4-3 | 214 | BUY | FAST8 | 53.0 | 6 | 93 | 5 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8027691841125488 | 0.0 | 0.0 | +ba7f039a-929c-4537-9eb6-f1dc4563cca8 / -— |
| Jogador 1 | 4-3 | 215 | MOVE_BENCH | FAST8 | 53.0 | 6 | 92 | 5 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5958033800125122 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 216 | MOVE_BOARD | FAST8 | 53.0 | 6 | 92 | 5 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019272541627287865 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 217 | MOVE_BOARD | FAST8 | 53.0 | 6 | 92 | 5 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010735224932432175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 218 | PASS | FAST8 | 53.0 | 6 | 92 | 5 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24888254702091217 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 222 | BUY | FAST8 | 41.0 | 6 | 102 | 5 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027681076899170876 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 1 | 4-4 | 223 | MOVE_BOARD | FAST8 | 41.0 | 6 | 100 | 5 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.766717317281291e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 224 | MOVE_BOARD | FAST8 | 41.0 | 6 | 100 | 5 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01505246851593256 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 225 | MOVE_BOARD | FAST8 | 41.0 | 6 | 100 | 5 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014921956695616245 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 226 | PASS | FAST8 | 41.0 | 6 | 100 | 5 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12809984385967255 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 232 | SELL | FAST8 | 41.0 | 6 | 110 | 5 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8500000238418579 | 0.0 | 0.0 | +— / -5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 |
| Jogador 1 | 4-5 | 233 | BUY | FAST8 | 41.0 | 6 | 115 | 5 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7810869812965393 | 0.0 | 0.0 | +ddae48a6-5360-4660-9fa1-143ac35635ee / -— |
| Jogador 1 | 4-5 | 234 | SELL | FAST8 | 41.0 | 6 | 112 | 5 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -e85c6ab6-f36c-40b4-88e2-b7380b4c9652 |
| Jogador 1 | 4-5 | 235 | BUY | FAST8 | 41.0 | 6 | 114 | 5 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1001637727022171 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 1 | 4-5 | 236 | MOVE_BENCH | FAST8 | 41.0 | 6 | 110 | 5 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03690497204661369 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 237 | MOVE_BOARD | FAST8 | 41.0 | 6 | 110 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999941922724247 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 238 | MOVE_BOARD | FAST8 | 41.0 | 6 | 110 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 239 | PASS | FAST8 | 41.0 | 6 | 110 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13707011938095093 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 242 | SELL | FAST8 | 41.0 | 6 | 120 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -bb3be648-cee1-4b75-b472-59653324b9bd |
| Jogador 1 | 4-6 | 243 | BUY | FAST8 | 41.0 | 6 | 123 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04724441468715668 | 0.0 | 0.0 | +84981e98-bfb7-4c49-a020-51cf6d864881 / -— |
| Jogador 1 | 4-6 | 244 | SELL | FAST8 | 41.0 | 6 | 120 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025066666305065155 | 0.0 | 0.0 | +— / -84981e98-bfb7-4c49-a020-51cf6d864881 |
| Jogador 1 | 4-6 | 245 | BUY | FAST8 | 41.0 | 6 | 123 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014958694577217102 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -— |
| Jogador 1 | 4-6 | 246 | MOVE_BOARD | FAST8 | 41.0 | 6 | 121 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.0589209270838182e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 247 | BUY_XP | FAST8 | 41.0 | 6 | 121 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055743999779224396 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 248 | BUY_XP | FAST8 | 41.0 | 6 | 117 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055743999779224396 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 249 | MOVE_BOARD | FAST8 | 41.0 | 6 | 113 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.8037662307033315e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 250 | MOVE_BOARD | FAST8 | 41.0 | 6 | 113 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014966407790780067 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 252 | SELL | FAST8 | 41.0 | 6 | 123 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01604883372783661 | 0.0 | 0.0 | +— / -8aa832ec-4c09-43bd-ae21-baf7268e468d |
| Jogador 1 | 4-7 | 253 | BUY | FAST8 | 41.0 | 6 | 125 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.450765997171402 | 0.0 | 0.0 | +565ff610-fe51-470b-8452-a7eec5e31653 / -— |
| Jogador 1 | 4-7 | 254 | SELL | FAST8 | 41.0 | 6 | 122 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45190000534057617 | 0.0 | 0.0 | +— / -565ff610-fe51-470b-8452-a7eec5e31653 |
| Jogador 1 | 4-7 | 255 | BUY | FAST8 | 41.0 | 6 | 125 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0857032835483551 | 0.0 | 0.0 | +5c43307a-6d61-4493-a1ed-cb428d79a254 / -— |
| Jogador 1 | 4-7 | 256 | MOVE_BOARD | FAST8 | 41.0 | 6 | 124 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.131350455187203e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 257 | MOVE_BOARD | FAST8 | 41.0 | 6 | 124 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000934712588787 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 258 | PASS | FAST8 | 41.0 | 6 | 124 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14984488487243652 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 41.0 | 7 | 134 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13767467439174652 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 41.0 | 7 | 134 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17112162709236145 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 264 | SELL | FAST8 | 41.0 | 7 | 134 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -5c43307a-6d61-4493-a1ed-cb428d79a254 |
| Jogador 1 | 5-1 | 265 | BUY | FAST8 | 41.0 | 7 | 135 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8590729236602783 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -— |
| Jogador 1 | 5-1 | 266 | MOVE_BENCH | FAST8 | 41.0 | 7 | 132 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5826109647750854 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 267 | BUY | FAST8 | 41.0 | 7 | 132 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013865564949810505 | 0.0 | 0.0 | +943437ce-e190-4790-986b-4e66e49637a7 / -— |
| Jogador 1 | 5-1 | 268 | MOVE_BOARD | FAST8 | 41.0 | 7 | 129 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.818060839781538e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 269 | MOVE_BOARD | FAST8 | 41.0 | 7 | 129 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014963384717702866 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 270 | MOVE_BOARD | FAST8 | 41.0 | 7 | 129 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015007329173386097 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 272 | SELL | FAST8 | 41.0 | 7 | 140 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -943437ce-e190-4790-986b-4e66e49637a7 |
| Jogador 1 | 5-2 | 273 | BUY | FAST8 | 41.0 | 7 | 143 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9516098499298096 | 0.0 | 0.0 | +58cbdbde-2151-438c-8897-902bef9bcd92 / -3a43ff36-dccd-49a7-92d8-0b01e739ea89,ddae48a6-5360-4660-9fa1-143ac35635ee |
| Jogador 1 | 5-2 | 274 | BUY | FAST8 | 41.0 | 7 | 140 | 5 | 34.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8151999711990356 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 1 | 5-2 | 275 | BUY | FAST8 | 41.0 | 7 | 139 | 5 | 34.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31967946887016296 | 0.0 | 0.0 | +ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 / -— |
| Jogador 1 | 5-2 | 276 | MOVE_BOARD | FAST8 | 41.0 | 7 | 136 | 5 | 34.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002612645330373198 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 277 | MOVE_BOARD | FAST8 | 41.0 | 7 | 136 | 5 | 34.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01754201389849186 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 278 | MOVE_BOARD | FAST8 | 41.0 | 7 | 136 | 5 | 34.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 279 | PASS | FAST8 | 41.0 | 7 | 136 | 5 | 34.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17561016976833344 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 282 | SELL | FAST8 | 41.0 | 7 | 148 | 5 | 34.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -58cbdbde-2151-438c-8897-902bef9bcd92 |
| Jogador 1 | 5-3 | 283 | BUY | FAST8 | 41.0 | 7 | 156 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8850309252738953 | 0.0 | 0.0 | +c8706680-2712-4914-b6c0-59bf92a2796d / -— |
| Jogador 1 | 5-3 | 284 | SELL | FAST8 | 41.0 | 7 | 155 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5894232988357544 | 0.0 | 0.0 | +— / -ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 |
| Jogador 1 | 5-3 | 285 | BUY | FAST8 | 41.0 | 7 | 158 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32385942339897156 | 0.0 | 0.0 | +4432f76a-94cc-4a96-b72b-1cf35b310dca / -— |
| Jogador 1 | 5-3 | 286 | MOVE_BOARD | FAST8 | 41.0 | 7 | 154 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.094800973078236e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 287 | MOVE_BENCH | FAST8 | 41.0 | 7 | 154 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08489494025707245 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 288 | MOVE_BOARD | FAST8 | 41.0 | 7 | 154 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01583891548216343 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 289 | MOVE_BOARD | FAST8 | 41.0 | 7 | 154 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026950547471642494 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 290 | PASS | FAST8 | 41.0 | 7 | 154 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1918593943119049 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 292 | SELL | FAST8 | 41.0 | 7 | 166 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -15893185-b1a5-4725-9e46-964e149ec287 |
| Jogador 1 | 5-4 | 293 | BUY | FAST8 | 41.0 | 7 | 169 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34281492233276367 | 0.0 | 0.0 | +4b1f1146-d580-41e9-987f-c32b1eb98b75 / -— |
| Jogador 1 | 5-4 | 294 | SELL | FAST8 | 41.0 | 7 | 167 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5925999879837036 | 0.0 | 0.0 | +— / -4b1f1146-d580-41e9-987f-c32b1eb98b75 |
| Jogador 1 | 5-4 | 295 | BUY | FAST8 | 41.0 | 7 | 169 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9475695490837097 | 0.0 | 0.0 | +f84cc827-410f-47eb-bd95-bd650acfdd4b / -cfc9d52e-f119-4fc9-8ced-569ac7071cb6,d381c462-a17f-4192-b694-66a7c3aaee4f |
| Jogador 1 | 5-4 | 296 | MOVE_BOARD | FAST8 | 41.0 | 7 | 168 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008373255841434002 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 297 | MOVE_BOARD | FAST8 | 41.0 | 7 | 168 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01469973661005497 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 298 | PASS | FAST8 | 41.0 | 7 | 168 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35869690775871277 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 302 | BUY | FAST8 | 41.0 | 7 | 179 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056063733994960785 | 0.0 | 0.0 | +95eba9e8-10f5-48d5-86de-3d9a446b2e65 / -— |
| Jogador 1 | 5-5 | 303 | BUY | FAST8 | 41.0 | 7 | 177 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19309918582439423 | 0.0 | 0.0 | +0c96798c-ee23-488b-974f-74e8e3da6aa6 / -— |
| Jogador 1 | 5-5 | 304 | REROLL | FAST8 | 41.0 | 7 | 172 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 305 | BUY_XP | FAST8 | 41.0 | 7 | 172 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05511999875307083 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 306 | REROLL | FAST8 | 41.0 | 7 | 168 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 307 | REROLL | FAST8 | 41.0 | 7 | 168 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 308 | REROLL | FAST8 | 41.0 | 7 | 168 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 309 | REROLL | FAST8 | 41.0 | 7 | 168 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 310 | REROLL | FAST8 | 41.0 | 7 | 168 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 312 | SELL | FAST8 | 41.0 | 7 | 179 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -f84cc827-410f-47eb-bd95-bd650acfdd4b |
| Jogador 1 | 5-6 | 313 | BUY | FAST8 | 41.0 | 7 | 182 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2990607023239136 | 0.0 | 0.0 | +0b38218d-9c50-41ac-b761-115c054bf314 / -— |
| Jogador 1 | 5-6 | 314 | MOVE_BENCH | FAST8 | 41.0 | 7 | 179 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10631132870912552 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 315 | MOVE_BENCH | FAST8 | 41.0 | 7 | 179 | 5 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5965574383735657 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 316 | MOVE_BENCH | FAST8 | 41.0 | 7 | 179 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40241801738739014 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 317 | PASS | FAST8 | 41.0 | 7 | 179 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21489204466342926 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 322 | SELL | FAST8 | 41.0 | 7 | 191 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050200000405311584 | 0.0 | 0.0 | +— / -95eba9e8-10f5-48d5-86de-3d9a446b2e65 |
| Jogador 1 | 5-7 | 323 | BUY | FAST8 | 41.0 | 7 | 193 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8181408047676086 | 0.0 | 0.0 | +27079fe2-8808-47b7-8b10-9fb2834bb6ed / -— |
| Jogador 1 | 5-7 | 324 | MOVE_BENCH | FAST8 | 41.0 | 7 | 190 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08731874823570251 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 325 | MOVE_BENCH | FAST8 | 41.0 | 7 | 190 | 5 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.58474200963974 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 326 | MOVE_BENCH | FAST8 | 41.0 | 7 | 190 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36920610070228577 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 327 | PASS | FAST8 | 41.0 | 7 | 190 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22517459094524384 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 332 | EQUIP_FROM_INVENTORY | FAST8 | 41.0 | 7 | 201 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.03782931715250015 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 333 | MOVE_BENCH | FAST8 | 41.0 | 7 | 201 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10550636053085327 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 334 | MOVE_BENCH | FAST8 | 41.0 | 7 | 201 | 5 | 30.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.584071934223175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 335 | MOVE_BENCH | FAST8 | 41.0 | 7 | 201 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7486539483070374 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 336 | PASS | FAST8 | 41.0 | 7 | 201 | 5 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25695091485977173 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 342 | MOVE_BENCH | ALL_IN | 25.0 | 7 | 211 | 5 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13245868682861328 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 343 | SELL | ALL_IN | 25.0 | 7 | 211 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012333333725109696 | 0.0 | 0.0 | +— / -0c96798c-ee23-488b-974f-74e8e3da6aa6 |
| Jogador 1 | 6-2 | 344 | BUY | ALL_IN | 25.0 | 7 | 216 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1099821329116821 | 0.0 | 0.0 | +3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 / -6fa83356-562b-4a26-a77d-3e989089e70a,c8706680-2712-4914-b6c0-59bf92a2796d |
| Jogador 1 | 6-2 | 345 | BUY | ALL_IN | 25.0 | 7 | 215 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1086713075637817 | 0.0 | 0.0 | +a810e10d-e7ef-4ece-8fb2-8b6471b557ec / -2a286030-5984-44b5-87ff-6c948d2e672e,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 6-2 | 346 | MOVE_BENCH | ALL_IN | 25.0 | 7 | 214 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5925909876823425 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 347 | BUY | ALL_IN | 25.0 | 7 | 214 | 5 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12910737097263336 | 0.0 | 0.0 | +2ac6d717-87f1-4421-929e-1934a9317e72 / -— |
| Jogador 1 | 6-2 | 348 | BUY | ALL_IN | 25.0 | 7 | 211 | 5 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14241185784339905 | 0.0 | 0.0 | +ae9da355-52b7-402c-be6e-41fa1148a550 / -— |
| Jogador 1 | 6-2 | 349 | MOVE_BENCH | ALL_IN | 25.0 | 7 | 207 | 5 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6464236378669739 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 350 | MOVE_BENCH | ALL_IN | 25.0 | 7 | 207 | 5 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41304251551628113 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 352 | BUY | ALL_IN | 7.0 | 7 | 218 | 5 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17532704770565033 | 0.0 | 0.0 | +de590b22-a48c-4c78-a2f3-6ef39ce948fe / -— |
| Jogador 1 | 6-3 | 353 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 214 | 5 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11022797971963882 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 354 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 214 | 5 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41377758979797363 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 355 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 214 | 5 | 40.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4045487642288208 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 356 | PASS | ALL_IN | 7.0 | 7 | 214 | 5 | 36.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7037519812583923 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.21754200756549835 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17793168127536774 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.574481725692749 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1177990436553955 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 34 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4685917794704437 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 46 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.40516209602355957 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 47 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0718140602111816 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0884234756231308 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 49 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.553705632686615 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0374016761779785 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2008957713842392 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 61 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2349439263343811 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 62 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24890121817588806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28669169545173645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05065726116299629 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 65 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22442719340324402 | 0.0 | 0.0 | +18082e05-51e8-4142-b541-c3d7d781b878 / -— |
| Jogador 2 | 2-1 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10190032422542572 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 68 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 70 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.117882251739502 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 71 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1491501331329346 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 72 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29847556352615356 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 73 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3161023259162903 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 74 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07575041800737381 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 75 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5755904912948608 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 76 | PASS | STABILIZE | 95.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 79 | BUY | STABILIZE | 95.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2476724088191986 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 80 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022606980055570602 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 81 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1355125606060028 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 82 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23556382954120636 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 83 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015855180099606514 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 84 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005373288877308369 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 85 | PASS | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 87 | BUY | STABILIZE | 90.0 | 4 | 14 | 1 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32351154088974 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 2 | 2-4 | 88 | SELL | STABILIZE | 90.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8824999928474426 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-4 | 89 | SELL | STABILIZE | 90.0 | 4 | 16 | 1 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12104494869709015 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 17 | 1 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005565065424889326 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 91 | BUY_XP | STABILIZE | 90.0 | 4 | 17 | 1 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 93 | BUY | STABILIZE | 90.0 | 5 | 19 | 1 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3624104857444763 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 94 | BUY | STABILIZE | 90.0 | 5 | 16 | 1 | 16.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36906030774116516 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 95 | BUY_XP | STABILIZE | 90.0 | 5 | 13 | 1 | 16.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14300000667572021 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 96 | BUY_XP | STABILIZE | 90.0 | 5 | 9 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 97 | BUY_XP | STABILIZE | 90.0 | 5 | 5 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 98 | SELL | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1477913111448288 | 0.0 | 0.0 | +— / -d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 2 | 2-5 | 99 | SELL | STABILIZE | 90.0 | 5 | 2 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5490656495094299 | 0.0 | 0.0 | +— / -081b684f-5d42-45c5-9a68-12127e5330a7 |
| Jogador 2 | 2-5 | 100 | BUY_XP | STABILIZE | 90.0 | 5 | 5 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 102 | BUY | STABILIZE | 85.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27423790097236633 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 103 | BUY | STABILIZE | 85.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07420964539051056 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0034390613436698914 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2215137630701065 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 106 | PASS | STABILIZE | 85.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 112 | BUY | FAST8 | 80.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1371583491563797 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 113 | MOVE_BOARD | FAST8 | 80.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.020562075079397e-17 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 114 | MOVE_BOARD | FAST8 | 80.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21570466458797455 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 115 | MOVE_BOARD | FAST8 | 80.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01697400026023388 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 116 | MOVE_BOARD | FAST8 | 80.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 117 | PASS | FAST8 | 80.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 122 | BUY | FAST8 | 80.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2937016785144806 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 123 | BUY | FAST8 | 80.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.21499279141426086 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 124 | CRAFT_AND_EQUIP | FAST8 | 80.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2392899990081787 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 125 | BUY_XP | FAST8 | 80.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 126 | MOVE_BOARD | FAST8 | 80.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003101822454482317 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 127 | MOVE_BOARD | FAST8 | 80.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014505147002637386 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 128 | MOVE_BOARD | FAST8 | 80.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015082387253642082 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 129 | PASS | FAST8 | 80.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 132 | BUY | FAST8 | 80.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7363477945327759 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 133 | MOVE_BOARD | FAST8 | 80.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 134 | MOVE_BOARD | FAST8 | 80.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014993973076343536 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 135 | PASS | FAST8 | 80.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 142 | BUY | FAST8 | 80.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6516861915588379 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 143 | BUY_XP | FAST8 | 80.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 144 | BUY_XP | FAST8 | 80.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 145 | MOVE_BOARD | FAST8 | 80.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007053285371512175 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 146 | MOVE_BOARD | FAST8 | 80.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014610201120376587 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 147 | PASS | FAST8 | 80.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 152 | BUY | FAST8 | 80.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1647881716489792 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 2 | 3-4 | 153 | BUY | FAST8 | 80.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6789579391479492 | 0.0 | 0.0 | +a15ff9dc-bf8a-49e0-9893-f92a212263d8 / -— |
| Jogador 2 | 3-4 | 154 | MOVE_BOARD | FAST8 | 80.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001488039386458695 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 155 | MOVE_BOARD | FAST8 | 80.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013158122077584267 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 156 | PASS | FAST8 | 80.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 162 | MOVE_BOARD | FAST8 | 80.0 | 6 | 10 | 1 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0004568017611745745 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 163 | BUY_XP | FAST8 | 80.0 | 6 | 10 | 1 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 164 | MOVE_BOARD | FAST8 | 80.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.361870247113984e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 165 | MOVE_BOARD | FAST8 | 80.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026752030476927757 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 166 | PASS | FAST8 | 80.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 172 | SELL | FAST8 | 80.0 | 6 | 13 | 1 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005764373112469912 | 0.0 | 0.0 | +— / -729ccd5b-adc5-4bca-9523-dcb532e93ecb |
| Jogador 2 | 3-6 | 173 | BUY | FAST8 | 80.0 | 6 | 17 | 1 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7338698506355286 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 174 | SELL | FAST8 | 80.0 | 6 | 14 | 1 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38866665959358215 | 0.0 | 0.0 | +— / -6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 3-6 | 175 | BUY | FAST8 | 80.0 | 6 | 17 | 1 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21777980029582977 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-6 | 176 | MOVE_BOARD | FAST8 | 80.0 | 6 | 16 | 1 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0066538481041789055 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 177 | MOVE_BOARD | FAST8 | 80.0 | 6 | 16 | 1 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017820389941334724 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 178 | MOVE_BOARD | FAST8 | 80.0 | 6 | 16 | 1 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 179 | PASS | FAST8 | 80.0 | 6 | 16 | 1 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 182 | SELL | FAST8 | 70.0 | 6 | 22 | 2 | 30.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 3-7 | 183 | BUY | FAST8 | 70.0 | 6 | 25 | 2 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7780457735061646 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -0c15e414-bc67-46de-a087-fb7708db0dfe,e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-7 | 184 | BUY_XP | STABILIZE | 70.0 | 6 | 22 | 2 | 24.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047449998557567596 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 185 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 18 | 1 | 24.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3432193398475647 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 186 | MOVE_BOARD | FAST8 | 70.0 | 7 | 18 | 1 | 26.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005448484793305397 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 187 | MOVE_BOARD | FAST8 | 70.0 | 7 | 18 | 1 | 26.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009167016483843327 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 188 | PASS | FAST8 | 70.0 | 7 | 18 | 1 | 26.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057500001043081284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 70.0 | 7 | 24 | 2 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1719283163547516 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 70.0 | 7 | 24 | 2 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21647658944129944 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 194 | MOVE_BOARD | FAST8 | 70.0 | 7 | 24 | 2 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 195 | MOVE_BOARD | FAST8 | 70.0 | 7 | 24 | 2 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014331398531794548 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 196 | PASS | FAST8 | 70.0 | 7 | 24 | 2 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11142857372760773 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 202 | BUY | FAST8 | 70.0 | 7 | 32 | 3 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37263745069503784 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -— |
| Jogador 2 | 4-2 | 203 | MOVE_BOARD | FAST8 | 70.0 | 7 | 30 | 3 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 204 | MOVE_BOARD | FAST8 | 70.0 | 7 | 30 | 3 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006764302495867014 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 205 | PASS | FAST8 | 70.0 | 7 | 30 | 3 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17571428418159485 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 212 | BUY | FAST8 | 70.0 | 7 | 40 | 4 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.739343523979187 | 0.0 | 0.0 | +6538f28f-845f-4f45-92bf-120931553bec / -a15ff9dc-bf8a-49e0-9893-f92a212263d8,ff0d9869-c346-4210-be85-1e802a25dd8b |
| Jogador 2 | 4-3 | 213 | MOVE_BOARD | FAST8 | 70.0 | 7 | 38 | 3 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.651617473427905e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 214 | MOVE_BOARD | FAST8 | 70.0 | 7 | 38 | 3 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014967096969485283 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 215 | MOVE_BOARD | FAST8 | 70.0 | 7 | 38 | 3 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0149907935410738 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 216 | PASS | FAST8 | 70.0 | 7 | 38 | 3 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041428569704294205 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 222 | BUY | FAST8 | 58.0 | 7 | 46 | 4 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13801629841327667 | 0.0 | 0.0 | +2357a4df-3c61-4957-83c3-572bbb99ac5a / -— |
| Jogador 2 | 4-4 | 223 | MOVE_BOARD | FAST8 | 58.0 | 7 | 43 | 4 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00010260710405418649 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 224 | MOVE_BOARD | FAST8 | 58.0 | 7 | 43 | 4 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 225 | PASS | FAST8 | 58.0 | 7 | 43 | 4 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 232 | BUY | FAST8 | 58.0 | 7 | 52 | 5 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2770044803619385 | 0.0 | 0.0 | +11b28280-bb53-4ca7-81b7-5ce8705303a5 / -— |
| Jogador 2 | 4-5 | 233 | BUY | FAST8 | 58.0 | 7 | 50 | 5 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09998701512813568 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 2 | 4-5 | 234 | MOVE_BOARD | FAST8 | 58.0 | 7 | 47 | 4 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.016329719685018e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 235 | MOVE_BOARD | FAST8 | 58.0 | 7 | 47 | 4 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014876436442136765 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 236 | PASS | FAST8 | 58.0 | 7 | 47 | 4 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047857142984867096 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 242 | SELL | FAST8 | 58.0 | 7 | 57 | 5 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4770576059818268 | 0.0 | 0.0 | +— / -6538f28f-845f-4f45-92bf-120931553bec |
| Jogador 2 | 4-6 | 243 | BUY | FAST8 | 58.0 | 7 | 62 | 5 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8277961015701294 | 0.0 | 0.0 | +0f5471bd-1451-4979-adc9-aced6bb63610 / -— |
| Jogador 2 | 4-6 | 244 | SELL | FAST8 | 58.0 | 7 | 61 | 5 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5896512269973755 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 4-6 | 245 | BUY | FAST8 | 58.0 | 7 | 69 | 5 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.891209602355957 | 0.0 | 0.0 | +83228c14-cadb-45b4-9893-2fb12c40f4a8 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-6 | 246 | MOVE_BENCH | FAST8 | 58.0 | 7 | 68 | 5 | 28.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31368470191955566 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 247 | BUY | FAST8 | 58.0 | 7 | 68 | 5 | 30.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8833932280540466 | 0.0 | 0.0 | +fe12befc-b473-4f91-9e51-558a03efa3ad / -18082e05-51e8-4142-b541-c3d7d781b878,23793b7b-2dab-48f0-a8ba-db85fc14c1c5 |
| Jogador 2 | 4-6 | 248 | MOVE_BENCH | FAST8 | 58.0 | 7 | 66 | 5 | 26.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3985244333744049 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 249 | BUY_XP | FAST8 | 58.0 | 7 | 66 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024639999493956566 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 250 | MOVE_BOARD | FAST8 | 58.0 | 7 | 62 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 252 | BUY | FAST8 | 47.0 | 7 | 72 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09297842532396317 | 0.0 | 0.0 | +6ea982ab-292d-42fc-99e6-d67c89f9f4fe / -— |
| Jogador 2 | 4-7 | 253 | SELL | FAST8 | 47.0 | 7 | 70 | 5 | 28.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -83228c14-cadb-45b4-9893-2fb12c40f4a8 |
| Jogador 2 | 4-7 | 254 | EQUIP_FROM_INVENTORY | FAST8 | 47.0 | 7 | 73 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13016682863235474 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 255 | EQUIP_FROM_INVENTORY | FAST8 | 47.0 | 7 | 73 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0744963064789772 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 256 | SELL | FAST8 | 47.0 | 7 | 73 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6414999961853027 | 0.0 | 0.0 | +— / -fe12befc-b473-4f91-9e51-558a03efa3ad |
| Jogador 2 | 4-7 | 257 | BUY | FAST8 | 47.0 | 7 | 78 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11684391647577286 | 0.0 | 0.0 | +84e865bc-366e-45cd-85e4-fa7314688368 / -— |
| Jogador 2 | 4-7 | 258 | BUY_XP | FAST8 | 47.0 | 7 | 77 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024639999493956566 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 259 | BUY_XP | FAST8 | 47.0 | 7 | 73 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024639999493956566 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 260 | BUY_XP | FAST8 | 47.0 | 7 | 69 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024639999493956566 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 262 | BUY | FAST8 | 47.0 | 7 | 75 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24681170284748077 | 0.0 | 0.0 | +b70671f9-0d78-4ae8-bd13-0267c96e7207 / -— |
| Jogador 2 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 47.0 | 7 | 73 | 5 | 28.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13979527354240417 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 264 | CRAFT_AND_EQUIP | FAST8 | 47.0 | 7 | 73 | 5 | 28.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08474066108465195 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 265 | SELL | FAST8 | 47.0 | 7 | 73 | 5 | 28.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008567147888243198 | 0.0 | 0.0 | +— / -84e865bc-366e-45cd-85e4-fa7314688368 |
| Jogador 2 | 5-1 | 266 | BUY | FAST8 | 47.0 | 7 | 74 | 5 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2134687453508377 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -— |
| Jogador 2 | 5-1 | 267 | MOVE_BENCH | FAST8 | 47.0 | 7 | 69 | 5 | 28.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15011529624462128 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 268 | MOVE_BOARD | FAST8 | 47.0 | 7 | 69 | 5 | 38.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 269 | BUY | FAST8 | 47.0 | 7 | 69 | 5 | 38.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16777929663658142 | 0.0 | 0.0 | +d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 / -— |
| Jogador 2 | 5-1 | 270 | MOVE_BOARD | FAST8 | 47.0 | 7 | 66 | 5 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 272 | MOVE_BOARD | FAST8 | 47.0 | 7 | 77 | 5 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 273 | MOVE_BOARD | FAST8 | 47.0 | 7 | 77 | 5 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000218525528908 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 274 | PASS | FAST8 | 47.0 | 7 | 77 | 5 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10872932523488998 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 282 | BUY | STABILIZE | 32.0 | 7 | 87 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8935480713844299 | 0.0 | 0.0 | +7a48aa2d-a43b-4e49-8230-77f4f2860cb2 / -— |
| Jogador 2 | 5-3 | 283 | SELL | STABILIZE | 32.0 | 7 | 84 | 5 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02156376652419567 | 0.0 | 0.0 | +— / -2357a4df-3c61-4957-83c3-572bbb99ac5a |
| Jogador 2 | 5-3 | 284 | BUY | STABILIZE | 32.0 | 7 | 87 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6108173131942749 | 0.0 | 0.0 | +b701c6c1-2e19-44b9-ad6e-e5d64e1d364c / -— |
| Jogador 2 | 5-3 | 285 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 84 | 5 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.8797904785024e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 286 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 84 | 5 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 287 | PASS | STABILIZE | 32.0 | 7 | 84 | 5 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14757966995239258 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 292 | SELL | STABILIZE | 32.0 | 7 | 95 | 5 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47723332047462463 | 0.0 | 0.0 | +— / -d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 |
| Jogador 2 | 5-4 | 293 | BUY | STABILIZE | 32.0 | 7 | 98 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0212643146514893 | 0.0 | 0.0 | +af404167-469a-447e-b415-dcb52033ef9b / -0f5471bd-1451-4979-adc9-aced6bb63610,f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 5-4 | 294 | BUY | STABILIZE | 32.0 | 7 | 97 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0211002826690674 | 0.0 | 0.0 | +a899fe97-90e4-4ae3-941c-af3dee48fed3 / -584e7960-a541-4d45-8ea1-8a75e288c387,a0ebc646-2e71-4b07-9208-401aa0cda6bb |
| Jogador 2 | 5-4 | 295 | BUY | STABILIZE | 32.0 | 7 | 96 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6676552295684814 | 0.0 | 0.0 | +a1357716-abf4-4d4f-abb8-34f2681f16dd / -— |
| Jogador 2 | 5-4 | 296 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 93 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 297 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 93 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018991846591234207 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 298 | PASS | STABILIZE | 32.0 | 7 | 93 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3113780915737152 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 302 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 103 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1459389477968216 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 303 | BUY | STABILIZE | 32.0 | 7 | 103 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12172858417034149 | 0.0 | 0.0 | +76fcc4d0-4988-4e99-8ac0-c251f0b99dcd / -— |
| Jogador 2 | 5-5 | 304 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 99 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13169081509113312 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 305 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 99 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013042181730270386 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 306 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 99 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018757237121462822 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 307 | PASS | STABILIZE | 32.0 | 7 | 99 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3179999589920044 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 312 | BUY | ALL_IN | 17.0 | 7 | 109 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9346836805343628 | 0.0 | 0.0 | +f087511a-d834-4f41-9b99-00bf0f6dc061 / -— |
| Jogador 2 | 5-6 | 313 | SELL | ALL_IN | 17.0 | 7 | 105 | 5 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9498000144958496 | 0.0 | 0.0 | +— / -af404167-469a-447e-b415-dcb52033ef9b |
| Jogador 2 | 5-6 | 314 | BUY | ALL_IN | 17.0 | 7 | 108 | 5 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0501388311386108 | 0.0 | 0.0 | +150a2da3-f559-4a40-a058-005e9c74e11f / -5b96c8f7-bacb-47df-8666-30d30d49549d,7a48aa2d-a43b-4e49-8230-77f4f2860cb2 |
| Jogador 2 | 5-6 | 315 | REROLL | ALL_IN | 17.0 | 7 | 105 | 5 | 42.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 316 | BUY | ALL_IN | 17.0 | 7 | 103 | 5 | 42.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4297134280204773 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 2 | 5-6 | 317 | BUY | ALL_IN | 17.0 | 7 | 100 | 5 | 42.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055260371416807175 | 0.0 | 0.0 | +d4c27edc-9b7e-4a31-a967-3aa80766b470 / -— |
| Jogador 2 | 5-6 | 318 | REROLL | ALL_IN | 17.0 | 7 | 97 | 5 | 42.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 319 | REROLL | ALL_IN | 17.0 | 7 | 95 | 5 | 42.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 320 | SELL | ALL_IN | 17.0 | 7 | 93 | 5 | 42.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6963000297546387 | 0.0 | 0.0 | +— / -a899fe97-90e4-4ae3-941c-af3dee48fed3 |
| Jogador 2 | 5-7 | 322 | BUY | ALL_IN | 2.0 | 7 | 107 | 5 | 42.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9828686118125916 | 0.0 | 0.0 | +40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b / -— |
| Jogador 2 | 5-7 | 323 | SELL | ALL_IN | 2.0 | 7 | 105 | 5 | 42.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7447999715805054 | 0.0 | 0.0 | +— / -150a2da3-f559-4a40-a058-005e9c74e11f |
| Jogador 2 | 5-7 | 324 | BUY | ALL_IN | 2.0 | 7 | 113 | 5 | 42.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1025869846343994 | 0.0 | 0.0 | +c2bf43be-e6e1-47ed-bcb4-606e37f26671 / -23157bd6-5e8f-4416-bb7f-2e5d71a06543,3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 5-7 | 325 | MOVE_BENCH | ALL_IN | 2.0 | 7 | 110 | 5 | 30.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4328513741493225 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 326 | MOVE_BENCH | ALL_IN | 2.0 | 7 | 110 | 5 | 34.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6025986671447754 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 327 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 110 | 5 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 328 | BUY | ALL_IN | 2.0 | 7 | 110 | 5 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05749441683292389 | 0.0 | 0.0 | +7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 / -— |
| Jogador 2 | 5-7 | 329 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 106 | 5 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007510242983698845 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 330 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 106 | 5 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 332 | BUY | ALL_IN | 2.0 | 7 | 117 | 5 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9516224265098572 | 0.0 | 0.0 | +93581e04-3f00-4430-8e5b-c953196bc1de / -— |
| Jogador 2 | 6-1 | 333 | EQUIP_FROM_INVENTORY | ALL_IN | 2.0 | 7 | 114 | 5 | 46.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10995525121688843 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 334 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 114 | 5 | 46.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006008829222992063 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 335 | SELL | ALL_IN | 2.0 | 7 | 114 | 5 | 46.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -d4c27edc-9b7e-4a31-a967-3aa80766b470 |
| Jogador 2 | 6-1 | 336 | BUY | ALL_IN | 2.0 | 7 | 117 | 5 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0032392740249634 | 0.0 | 0.0 | +d632ff66-a7c4-43d3-afb3-b83c174cda35 / -a1357716-abf4-4d4f-abb8-34f2681f16dd,b701c6c1-2e19-44b9-ad6e-e5d64e1d364c |
| Jogador 2 | 6-1 | 337 | REROLL | ALL_IN | 2.0 | 7 | 114 | 5 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 338 | BUY | ALL_IN | 2.0 | 7 | 112 | 5 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1107300519943237 | 0.0 | 0.0 | +5098782d-1ec1-4a5b-a435-f3c84ab1be0d / -11b28280-bb53-4ca7-81b7-5ce8705303a5,40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b |
| Jogador 2 | 6-1 | 339 | MOVE_BENCH | ALL_IN | 2.0 | 7 | 110 | 5 | 38.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.231623575091362 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 340 | EQUIP_FROM_INVENTORY | ALL_IN | 2.0 | 7 | 110 | 5 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10921332240104675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5923603177070618 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1582871973514557 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0395511388778687 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 34 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179660558700562 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 35 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.269970566034317 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 46 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7075631618499756 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.027385950088501 | 0.0 | 0.0 | +584812e9-d314-4de0-97e2-604c5c69466c / -— |
| Jogador 3 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26482003927230835 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 61 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.061585672199726105 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 70 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2532767951488495 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 71 | PASS | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 79 | BUY | STABILIZE | 96.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.292176216840744 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 80 | CRAFT_AND_EQUIP | STABILIZE | 96.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24110403656959534 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 81 | CRAFT_AND_EQUIP | STABILIZE | 96.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2193719446659088 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 82 | PASS | STABILIZE | 96.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 87 | BUY | STABILIZE | 91.0 | 4 | 17 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.108987808227539 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -584812e9-d314-4de0-97e2-604c5c69466c,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 2-4 | 88 | MOVE_BENCH | STABILIZE | 91.0 | 4 | 16 | 1 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2615843713283539 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 89 | BUY_XP | STABILIZE | 91.0 | 4 | 16 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 90 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 12 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1493697166442871 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 91 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 12 | 1 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39537733793258667 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 93 | BUY | STABILIZE | 91.0 | 5 | 19 | 1 | 20.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0368038415908813 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 94 | BUY | STABILIZE | 91.0 | 5 | 18 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27774786949157715 | 0.0 | 0.0 | +cdb48eea-209d-4833-9a68-79df61990332 / -— |
| Jogador 3 | 2-5 | 95 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 15 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0015908856876194477 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 15 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014474377036094666 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 97 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 15 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011480128392577171 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 98 | PASS | STABILIZE | 91.0 | 5 | 15 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019999999552965164 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 102 | BUY | STABILIZE | 91.0 | 5 | 22 | 2 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.115592122077942 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 103 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 21 | 2 | 18.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 21 | 2 | 18.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015029225498437881 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 105 | PASS | STABILIZE | 91.0 | 5 | 21 | 2 | 18.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021071428433060646 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 112 | BUY | STABILIZE | 91.0 | 5 | 30 | 3 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9780557155609131 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 113 | BUY | STABILIZE | 91.0 | 5 | 27 | 2 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35650914907455444 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 114 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 26 | 2 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01637800969183445 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 26 | 2 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004821776412427425 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 26 | 2 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 26 | 2 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014994991943240166 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 118 | PASS | STABILIZE | 91.0 | 5 | 26 | 2 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021964285522699356 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 91.0 | 5 | 34 | 3 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2631056606769562 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 123 | BUY | STABILIZE | 91.0 | 5 | 34 | 3 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3135058283805847 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -— |
| Jogador 3 | 3-1 | 124 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 33 | 3 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.729884181462694e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 33 | 3 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014914867468178272 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 33 | 3 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28637418150901794 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 127 | PASS | STABILIZE | 91.0 | 5 | 33 | 3 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12449999898672104 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 132 | BUY | STABILIZE | 91.0 | 5 | 43 | 4 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8459558486938477 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -— |
| Jogador 3 | 3-2 | 133 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 42 | 4 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0018481328152120113 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 134 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 42 | 4 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2529890537261963 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 135 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 42 | 4 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012022358365356922 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 42 | 4 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028532829135656357 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 137 | PASS | STABILIZE | 91.0 | 5 | 42 | 4 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1289999932050705 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 142 | BUY | STABILIZE | 91.0 | 5 | 53 | 5 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3637603223323822 | 0.0 | 0.0 | +e8b0d22c-35bc-459e-a90c-7db13fcbe34f / -— |
| Jogador 3 | 3-3 | 143 | BUY | STABILIZE | 91.0 | 5 | 51 | 5 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16015203297138214 | 0.0 | 0.0 | +ffdee27e-2d30-40b5-9937-92be68ab1390 / -— |
| Jogador 3 | 3-3 | 144 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 49 | 4 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013415553607046604 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 49 | 4 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01786036603152752 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 49 | 4 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012022358365356922 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 147 | PASS | STABILIZE | 91.0 | 5 | 49 | 4 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13249999284744263 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 152 | BUY | STABILIZE | 91.0 | 5 | 62 | 5 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25093114376068115 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 153 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 60 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013532829470932484 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 154 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 60 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015844464069232345 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 155 | PASS | STABILIZE | 91.0 | 5 | 60 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06017022207379341 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 162 | SELL | STABILIZE | 91.0 | 5 | 72 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4450654983520508 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 3-5 | 163 | BUY | STABILIZE | 91.0 | 5 | 75 | 5 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32272911071777344 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 164 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 72 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015114685520529747 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 72 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01342680398374796 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 166 | PASS | STABILIZE | 91.0 | 5 | 72 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06592714041471481 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 172 | SELL | STABILIZE | 81.0 | 5 | 82 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63 |
| Jogador 3 | 3-6 | 173 | BUY | STABILIZE | 81.0 | 5 | 85 | 5 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3266829252243042 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -— |
| Jogador 3 | 3-6 | 174 | SELL | STABILIZE | 81.0 | 5 | 84 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016806410625576973 | 0.0 | 0.0 | +— / -ffdee27e-2d30-40b5-9937-92be68ab1390 |
| Jogador 3 | 3-6 | 175 | BUY | STABILIZE | 81.0 | 5 | 86 | 5 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8465693593025208 | 0.0 | 0.0 | +1489b596-9339-407a-b49f-d01ecfdd6f78 / -— |
| Jogador 3 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 85 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004016036633402109 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 85 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011017844080924988 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 178 | PASS | STABILIZE | 81.0 | 5 | 85 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07254375517368317 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 182 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 96 | 5 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43761560320854187 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 183 | BUY | FAST8 | 81.0 | 6 | 96 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21806871891021729 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 184 | MOVE_BOARD | FAST8 | 81.0 | 6 | 93 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0006900941953063011 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 185 | MOVE_BOARD | FAST8 | 81.0 | 6 | 93 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013686653226613998 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 186 | PASS | FAST8 | 81.0 | 6 | 93 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07674792408943176 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 81.0 | 6 | 103 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06474632024765015 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 81.0 | 6 | 103 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17692704498767853 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 194 | SELL | FAST8 | 81.0 | 6 | 103 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -9028d514-586b-4d0e-b042-07389323c8cf |
| Jogador 3 | 4-1 | 195 | BUY | FAST8 | 81.0 | 6 | 106 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7959632277488708 | 0.0 | 0.0 | +f64919a5-eb2c-4e23-91ed-0067b3d90951 / -— |
| Jogador 3 | 4-1 | 196 | MOVE_BOARD | FAST8 | 81.0 | 6 | 103 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0008245771168731153 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 197 | MOVE_BOARD | FAST8 | 81.0 | 6 | 103 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014182972721755505 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 198 | PASS | FAST8 | 81.0 | 6 | 103 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11730480194091797 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 202 | SELL | FAST8 | 70.0 | 6 | 113 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24141110479831696 | 0.0 | 0.0 | +— / -e2f28d51-690c-476e-b097-e5c69258f933 |
| Jogador 3 | 4-2 | 203 | BUY | FAST8 | 70.0 | 6 | 114 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8154918551445007 | 0.0 | 0.0 | +974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 / -— |
| Jogador 3 | 4-2 | 204 | SELL | FAST8 | 70.0 | 6 | 112 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.403186559677124 | 0.0 | 0.0 | +— / -f5c14a50-b095-4a36-995f-2a8514e46f1c |
| Jogador 3 | 4-2 | 205 | BUY | FAST8 | 70.0 | 6 | 114 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6265668272972107 | 0.0 | 0.0 | +0534477f-2ff8-47a7-b71b-1a1d5430589e / -— |
| Jogador 3 | 4-2 | 206 | MOVE_BOARD | FAST8 | 70.0 | 6 | 111 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.1852561594168947e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 207 | MOVE_BOARD | FAST8 | 70.0 | 6 | 111 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499699056148529 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 208 | MOVE_BOARD | FAST8 | 70.0 | 6 | 111 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999245293438435 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 209 | PASS | FAST8 | 70.0 | 6 | 111 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12354357540607452 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 212 | SELL | FAST8 | 70.0 | 6 | 122 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5105666518211365 | 0.0 | 0.0 | +— / -0534477f-2ff8-47a7-b71b-1a1d5430589e |
| Jogador 3 | 4-3 | 213 | BUY | FAST8 | 70.0 | 6 | 125 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.131320983171463 | 0.0 | 0.0 | +2001a193-3868-4a3f-8a71-3a9f95c04a02 / -— |
| Jogador 3 | 4-3 | 214 | MOVE_BENCH | FAST8 | 70.0 | 6 | 122 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24128161370754242 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 215 | MOVE_BENCH | FAST8 | 70.0 | 6 | 122 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3543553352355957 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 216 | MOVE_BENCH | FAST8 | 70.0 | 6 | 122 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08118712157011032 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 217 | MOVE_BENCH | FAST8 | 70.0 | 6 | 122 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0655826330184937 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 218 | MOVE_BENCH | FAST8 | 70.0 | 6 | 122 | 5 | 32.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3535207211971283 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 219 | MOVE_BENCH | FAST8 | 70.0 | 6 | 122 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035582173615694046 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 220 | MOVE_BENCH | FAST8 | 70.0 | 6 | 122 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.786193311214447 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 222 | MOVE_BENCH | FAST8 | 70.0 | 6 | 134 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1932765245437622 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 223 | MOVE_BENCH | FAST8 | 70.0 | 6 | 134 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.761874794960022 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 224 | MOVE_BENCH | FAST8 | 70.0 | 6 | 134 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038016706705093384 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 225 | SELL | FAST8 | 70.0 | 6 | 134 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -2001a193-3868-4a3f-8a71-3a9f95c04a02 |
| Jogador 3 | 4-4 | 226 | BUY | FAST8 | 70.0 | 6 | 137 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27823588252067566 | 0.0 | 0.0 | +157648c2-e9b6-4eb2-b42c-19c554a3a41e / -— |
| Jogador 3 | 4-4 | 227 | MOVE_BOARD | FAST8 | 70.0 | 6 | 134 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.513555126730353e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 228 | MOVE_BOARD | FAST8 | 70.0 | 6 | 134 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015011336654424667 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 229 | MOVE_BOARD | FAST8 | 70.0 | 6 | 134 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015002517029643059 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 230 | PASS | FAST8 | 70.0 | 6 | 134 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1419110894203186 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 232 | SELL | FAST8 | 70.0 | 6 | 145 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -157648c2-e9b6-4eb2-b42c-19c554a3a41e |
| Jogador 3 | 4-5 | 233 | BUY | FAST8 | 70.0 | 6 | 148 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8152981400489807 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -— |
| Jogador 3 | 4-5 | 234 | SELL | FAST8 | 70.0 | 6 | 146 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9589666724205017 | 0.0 | 0.0 | +— / -2fa86b11-4e28-4652-890e-f00a79068223 |
| Jogador 3 | 4-5 | 235 | BUY | FAST8 | 70.0 | 6 | 147 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8907930850982666 | 0.0 | 0.0 | +a58767a1-d7c1-48e9-94ae-df46a364ef92 / -aaa84ce8-7919-4ec3-92eb-cc03a9decca9,f64919a5-eb2c-4e23-91ed-0067b3d90951 |
| Jogador 3 | 4-5 | 236 | MOVE_BENCH | STABILIZE | 70.0 | 6 | 144 | 5 | 24.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48765695095062256 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 237 | MOVE_BOARD | FAST8 | 70.0 | 6 | 144 | 5 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 238 | MOVE_BOARD | FAST8 | 70.0 | 6 | 144 | 5 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01498036552220583 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 239 | PASS | FAST8 | 70.0 | 6 | 144 | 5 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1500651240348816 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 242 | BUY | FAST8 | 58.0 | 6 | 154 | 5 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3412967622280121 | 0.0 | 0.0 | +a11208a9-96bf-468e-ab92-2ead6308be26 / -— |
| Jogador 3 | 4-6 | 243 | BUY | FAST8 | 58.0 | 6 | 153 | 5 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07455344498157501 | 0.0 | 0.0 | +ded275a3-9551-4816-8112-f0a25524412c / -— |
| Jogador 3 | 4-6 | 244 | MOVE_BOARD | FAST8 | 58.0 | 6 | 150 | 5 | 28.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0155181884765625 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 245 | MOVE_BOARD | FAST8 | 58.0 | 6 | 150 | 5 | 28.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005719122709706426 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 246 | MOVE_BENCH | FAST8 | 58.0 | 6 | 150 | 5 | 28.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6531352400779724 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 247 | MOVE_BENCH | FAST8 | 58.0 | 6 | 150 | 5 | 30.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4146801233291626 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 248 | PASS | FAST8 | 58.0 | 6 | 150 | 5 | 28.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1550000011920929 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 252 | SELL | FAST8 | 58.0 | 6 | 161 | 5 | 28.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -a58767a1-d7c1-48e9-94ae-df46a364ef92 |
| Jogador 3 | 4-7 | 253 | BUY | FAST8 | 58.0 | 6 | 169 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8921521902084351 | 0.0 | 0.0 | +590d07db-5e90-4705-a7ae-96f84fd06382 / -41db1132-4e1c-48eb-8a9b-1b2c74cb22ce,5f9e16e2-0766-403f-a85a-f6a735c04261 |
| Jogador 3 | 4-7 | 254 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 167 | 5 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.5998023748397827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 255 | EQUIP_FROM_INVENTORY | FAST8 | 58.0 | 6 | 167 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1690795123577118 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 256 | EQUIP_FROM_INVENTORY | FAST8 | 58.0 | 6 | 167 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12454521656036377 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 257 | BUY | FAST8 | 58.0 | 6 | 167 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22278349101543427 | 0.0 | 0.0 | +27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 / -— |
| Jogador 3 | 4-7 | 258 | MOVE_BOARD | FAST8 | 58.0 | 6 | 164 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.114534143198398e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 259 | MOVE_BENCH | FAST8 | 58.0 | 6 | 164 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2101423144340515 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 260 | PASS | FAST8 | 58.0 | 6 | 164 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1666276603937149 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 262 | BUY | FAST8 | 58.0 | 6 | 174 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.347361296415329 | 0.0 | 0.0 | +0fd34229-b814-4580-8651-59e712d5657f / -— |
| Jogador 3 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 58.0 | 6 | 172 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20405320823192596 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 264 | CRAFT_AND_EQUIP | FAST8 | 58.0 | 6 | 172 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15775145590305328 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 265 | MOVE_BENCH | FAST8 | 58.0 | 6 | 172 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6401661038398743 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 266 | MOVE_BENCH | FAST8 | 58.0 | 6 | 172 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08419169485569 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 267 | MOVE_BENCH | FAST8 | 58.0 | 6 | 172 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20362488925457 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 268 | MOVE_BENCH | FAST8 | 58.0 | 6 | 172 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6549953818321228 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 269 | PASS | FAST8 | 58.0 | 6 | 172 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19067145884037018 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 272 | MOVE_BENCH | FAST8 | 43.0 | 6 | 182 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09998507052659988 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 273 | SELL | FAST8 | 43.0 | 6 | 182 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -590d07db-5e90-4705-a7ae-96f84fd06382 |
| Jogador 3 | 5-2 | 274 | BUY | FAST8 | 43.0 | 6 | 187 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9522873163223267 | 0.0 | 0.0 | +50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de / -974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0,e8b0d22c-35bc-459e-a90c-7db13fcbe34f |
| Jogador 3 | 5-2 | 275 | MOVE_BENCH | STABILIZE | 43.0 | 6 | 185 | 5 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4020133316516876 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 276 | MOVE_BENCH | FAST8 | 43.0 | 6 | 185 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6497247815132141 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 277 | MOVE_BENCH | FAST8 | 43.0 | 6 | 185 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7246665954589844 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 278 | PASS | FAST8 | 43.0 | 6 | 185 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3683791756629944 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 282 | BUY | STABILIZE | 29.0 | 6 | 196 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6327385306358337 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -— |
| Jogador 3 | 5-3 | 283 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 193 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 284 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 193 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7196349501609802 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 285 | PASS | STABILIZE | 29.0 | 6 | 193 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41865992546081543 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 292 | BUY | STABILIZE | 29.0 | 6 | 204 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8945368528366089 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -— |
| Jogador 3 | 5-4 | 293 | SELL | STABILIZE | 29.0 | 6 | 202 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5899999737739563 | 0.0 | 0.0 | +— / -50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de |
| Jogador 3 | 5-4 | 294 | BUY | STABILIZE | 29.0 | 6 | 207 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8858789801597595 | 0.0 | 0.0 | +64215569-2a69-410d-a2f9-172544bef858 / -— |
| Jogador 3 | 5-4 | 295 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 205 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.09861364215612411 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 296 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 205 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.11500000208616257 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 297 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 205 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.7482954263687134 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 298 | PASS | STABILIZE | 29.0 | 6 | 205 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.4299927055835724 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 302 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 216 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.09861502051353455 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 303 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 216 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.11500000208616257 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 304 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 216 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.06597200781106949 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 305 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 216 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.09857619553804398 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 306 | MOVE_BENCH | STABILIZE | 29.0 | 6 | 216 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.7474441528320312 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 307 | PASS | STABILIZE | 29.0 | 6 | 216 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.2864586412906647 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 312 | MOVE_BENCH | ALL_IN | 14.0 | 6 | 227 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.09986260533332825 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 313 | MOVE_BENCH | ALL_IN | 14.0 | 6 | 227 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.09859967231750488 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 314 | MOVE_BENCH | ALL_IN | 14.0 | 6 | 227 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.7473916411399841 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 315 | PASS | ALL_IN | 14.0 | 6 | 227 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.6628275513648987 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5923603177070618 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16613417863845825 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 33 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4014523923397064 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 46 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0139820575714111 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 47 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.339042603969574 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003144908230751753 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014524636790156364 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 51 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.038104772567749 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 60 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07230526953935623 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 70 | BUY | STABILIZE | 94.0 | 4 | 11 | 1 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2534292936325073 | 0.0 | 0.0 | +e989a0cc-848a-4c45-b153-315877aee8f7 / -— |
| Jogador 4 | 2-2 | 71 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.00033756293123587966 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 72 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 73 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 74 | PASS | STABILIZE | 94.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 79 | BUY | STABILIZE | 88.0 | 4 | 15 | 1 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1146832704544067 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 80 | CRAFT_AND_EQUIP | STABILIZE | 88.0 | 4 | 14 | 1 | 4.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22088637948036194 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 81 | CRAFT_AND_EQUIP | STABILIZE | 88.0 | 4 | 14 | 1 | 4.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18019449710845947 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 82 | MOVE_BENCH | STABILIZE | 88.0 | 4 | 14 | 1 | 4.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0025882793124765158 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 83 | BUY | STABILIZE | 88.0 | 4 | 14 | 1 | 6.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7593218684196472 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 84 | MOVE_BENCH | STABILIZE | 88.0 | 4 | 13 | 1 | 6.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3970573842525482 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 85 | MOVE_BOARD | STABILIZE | 88.0 | 4 | 13 | 1 | 10.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012821548618376255 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 87 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 20 | 2 | 10.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012187825050204992 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 88 | BUY | LOSS_STREAK | 83.0 | 4 | 20 | 2 | 10.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1549133062362671 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 89 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 17 | 1 | 10.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007076205802150071 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 90 | BUY_XP | LOSS_STREAK | 83.0 | 4 | 17 | 1 | 10.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03759999945759773 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 91 | MOVE_BENCH | LOSS_STREAK | 83.0 | 5 | 13 | 1 | 10.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4025293290615082 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 93 | BUY | LOSS_STREAK | 83.0 | 5 | 20 | 2 | 16.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14761191606521606 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 94 | MOVE_BOARD | LOSS_STREAK | 83.0 | 5 | 17 | 1 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 95 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 17 | 1 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013044172897934914 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 96 | PASS | STABILIZE | 83.0 | 5 | 17 | 1 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020357143133878708 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 102 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 24 | 2 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 103 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 24 | 2 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016177233308553696 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 104 | PASS | STABILIZE | 77.0 | 5 | 24 | 2 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021607141941785812 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 112 | BUY | STABILIZE | 77.0 | 5 | 32 | 3 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0179905891418457 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -— |
| Jogador 4 | 2-7 | 113 | BUY | STABILIZE | 77.0 | 5 | 31 | 3 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0402880907058716 | 0.0 | 0.0 | +764470bb-9820-4e49-98f9-5a5f0ce5ca8f / -eddd35aa-7d38-4d71-8984-e4768f06379e,ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-7 | 114 | BUY | STABILIZE | 77.0 | 5 | 30 | 3 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27789315581321716 | 0.0 | 0.0 | +3d4fca52-8f58-4464-8cec-752fa99dbb3c / -— |
| Jogador 4 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 29 | 2 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 29 | 2 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01467826496809721 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 117 | PASS | STABILIZE | 77.0 | 5 | 29 | 2 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02250000089406967 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 122 | BUY | STABILIZE | 77.0 | 5 | 36 | 3 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8867460489273071 | 0.0 | 0.0 | +cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 / -4a0403a3-c999-4d4c-83f0-7270e8576aed,9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 77.0 | 5 | 35 | 3 | 14.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24370227754116058 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 124 | MOVE_BENCH | STABILIZE | 77.0 | 5 | 35 | 3 | 14.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44552531838417053 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 35 | 3 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 35 | 3 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03271310031414032 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 127 | PASS | STABILIZE | 77.0 | 5 | 35 | 3 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12549999356269836 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 132 | BUY | STABILIZE | 66.0 | 5 | 43 | 4 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8503053784370422 | 0.0 | 0.0 | +3f253868-2de5-4189-95a0-705f62682958 / -— |
| Jogador 4 | 3-2 | 133 | BUY | STABILIZE | 66.0 | 5 | 42 | 4 | 16.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9017417430877686 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 66.0 | 5 | 41 | 4 | 12.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2954992353916168 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 135 | MOVE_BENCH | STABILIZE | 66.0 | 5 | 41 | 4 | 14.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5894433856010437 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 136 | BUY | STABILIZE | 66.0 | 5 | 41 | 4 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34667643904685974 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 66.0 | 5 | 40 | 4 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00042953103547915816 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 66.0 | 5 | 40 | 4 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01584542542695999 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 139 | MOVE_BOARD | STABILIZE | 66.0 | 5 | 40 | 4 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 140 | PASS | STABILIZE | 66.0 | 5 | 40 | 4 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 142 | BUY | STABILIZE | 56.0 | 5 | 50 | 5 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3383111357688904 | 0.0 | 0.0 | +e2ed7625-f3aa-43f0-936b-7322cb9d16f1 / -— |
| Jogador 4 | 3-3 | 143 | BUY | STABILIZE | 56.0 | 5 | 49 | 4 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3210733234882355 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 144 | BUY | STABILIZE | 56.0 | 5 | 48 | 4 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29659682512283325 | 0.0 | 0.0 | +58c38a13-23c5-4ac1-8601-f0636aeb33ab / -— |
| Jogador 4 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 45 | 4 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004924684180878103 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 45 | 4 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015076574869453907 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 147 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 45 | 4 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014206070452928543 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 148 | PASS | STABILIZE | 56.0 | 5 | 45 | 4 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032499998807907104 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 152 | BUY | STABILIZE | 44.0 | 5 | 55 | 5 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.845583438873291 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -— |
| Jogador 4 | 3-4 | 153 | MOVE_BOARD | STABILIZE | 44.0 | 5 | 54 | 5 | 18.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012100349180400372 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 44.0 | 5 | 54 | 5 | 18.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7205219268798828 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 155 | PASS | STABILIZE | 44.0 | 5 | 54 | 5 | 20.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0589904822409153 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 162 | SELL | STABILIZE | 44.0 | 5 | 65 | 5 | 20.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -764470bb-9820-4e49-98f9-5a5f0ce5ca8f |
| Jogador 4 | 3-5 | 163 | BUY | STABILIZE | 44.0 | 5 | 68 | 5 | 20.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9004473090171814 | 0.0 | 0.0 | +661b176a-5963-4715-b9dd-aca29f552fa9 / -3d4fca52-8f58-4464-8cec-752fa99dbb3c,3f253868-2de5-4189-95a0-705f62682958 |
| Jogador 4 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 44.0 | 5 | 67 | 5 | 16.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39697322249412537 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 165 | MOVE_BENCH | STABILIZE | 44.0 | 5 | 67 | 5 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49946343898773193 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 44.0 | 5 | 67 | 5 | 18.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5799520015716553 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 167 | BUY | STABILIZE | 44.0 | 5 | 67 | 5 | 20.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3020050525665283 | 0.0 | 0.0 | +62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 / -— |
| Jogador 4 | 3-5 | 168 | BUY | STABILIZE | 44.0 | 5 | 65 | 5 | 20.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30226999521255493 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 4 | 3-5 | 169 | MOVE_BENCH | STABILIZE | 44.0 | 5 | 63 | 5 | 20.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07544398307800293 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 170 | MOVE_BOARD | STABILIZE | 44.0 | 5 | 63 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011699603870511055 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 172 | SELL | STABILIZE | 34.0 | 5 | 74 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8129804134368896 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 3-6 | 173 | BUY | STABILIZE | 34.0 | 5 | 77 | 5 | 22.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8979824185371399 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -— |
| Jogador 4 | 3-6 | 174 | MOVE_BENCH | STABILIZE | 34.0 | 5 | 76 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3983255922794342 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 175 | MOVE_BENCH | STABILIZE | 34.0 | 5 | 76 | 5 | 24.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0830342173576355 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 176 | MOVE_BENCH | STABILIZE | 34.0 | 5 | 76 | 5 | 20.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18491502106189728 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 177 | MOVE_BENCH | STABILIZE | 34.0 | 5 | 76 | 5 | 20.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41327688097953796 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 178 | PASS | STABILIZE | 34.0 | 5 | 76 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08550126850605011 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 182 | MOVE_BENCH | ALL_IN | 21.0 | 6 | 88 | 5 | 22.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09830746799707413 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 183 | MOVE_BENCH | ALL_IN | 21.0 | 6 | 88 | 5 | 20.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10638459026813507 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 184 | BUY | ALL_IN | 21.0 | 6 | 88 | 5 | 24.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8843432664871216 | 0.0 | 0.0 | +59f588eb-e3f3-4907-ab23-af073a26bd6a / -— |
| Jogador 4 | 3-7 | 185 | MOVE_BENCH | ALL_IN | 21.0 | 6 | 86 | 5 | 24.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03311626613140106 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 186 | MOVE_BENCH | ALL_IN | 21.0 | 6 | 86 | 5 | 26.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41267505288124084 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 187 | PASS | ALL_IN | 21.0 | 6 | 86 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5306751132011414 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 192 | CRAFT_AND_EQUIP | ALL_IN | 21.0 | 6 | 98 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13947509229183197 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 193 | CRAFT_AND_EQUIP | ALL_IN | 21.0 | 6 | 98 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17986346781253815 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 194 | SELL | ALL_IN | 21.0 | 6 | 98 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6851000189781189 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 4-1 | 195 | BUY | ALL_IN | 21.0 | 6 | 101 | 5 | 28.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9888163805007935 | 0.0 | 0.0 | +465ecc70-f5da-47f4-a7c0-2005a8ed24c1 / -— |
| Jogador 4 | 4-1 | 196 | EQUIP_FROM_INVENTORY | ALL_IN | 21.0 | 6 | 100 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.16194897890090942 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 197 | MOVE_BOARD | ALL_IN | 21.0 | 6 | 100 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 198 | MOVE_BOARD | ALL_IN | 21.0 | 6 | 100 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 199 | PASS | ALL_IN | 21.0 | 6 | 100 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4969887435436249 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 202 | SELL | ALL_IN | 9.0 | 6 | 113 | 5 | 28.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6832401156425476 | 0.0 | 0.0 | +— / -661b176a-5963-4715-b9dd-aca29f552fa9 |
| Jogador 4 | 4-2 | 203 | BUY | ALL_IN | 9.0 | 6 | 116 | 5 | 28.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2809699773788452 | 0.0 | 0.0 | +090f2ba6-5514-49ba-a80d-a0711cd06245 / -— |
| Jogador 4 | 4-2 | 204 | MOVE_BOARD | ALL_IN | 9.0 | 6 | 113 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 205 | MOVE_BENCH | ALL_IN | 9.0 | 6 | 113 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 206 | PASS | ALL_IN | 9.0 | 6 | 113 | 5 | 28.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5435565710067749 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5658670663833618 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12370830029249191 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11255644261837006 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17693054676055908 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18797899782657623 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 34 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39719316363334656 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 46 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3289370536804199 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 47 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28694817423820496 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03815691918134689 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 50 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.030136227607727 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.19029659032821655 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 61 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2362193614244461 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 62 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20553089678287506 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42583656311035156 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016959741711616516 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 65 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1319151669740677 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 66 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 70 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9294894933700562 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 71 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31650495529174805 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 72 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02233724668622017 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 73 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09882453083992004 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 74 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 79 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9301755428314209 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 80 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14172352850437164 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 81 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03952138498425484 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 82 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28756648302078247 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 83 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 84 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23286740481853485 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 85 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 87 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2746686041355133 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 88 | SELL | STABILIZE | 100.0 | 5 | 5 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045099999755620956 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 89 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20181095600128174 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 90 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 91 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4026402235031128 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 93 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3165363371372223 | 0.0 | 0.0 | +2e4ab22c-62d7-425c-9528-2e1315655c24 / -— |
| Jogador 5 | 2-5 | 94 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.692130717856344e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 95 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014960680156946182 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04406837746500969 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 97 | PASS | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 102 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 12 | 1 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028993409126996994 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 103 | BUY | STABILIZE | 100.0 | 5 | 12 | 1 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04777180403470993 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 104 | BUY | STABILIZE | 100.0 | 5 | 11 | 1 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5514004230499268 | 0.0 | 0.0 | +b6a21130-c9dc-45ad-8ddb-9223b0ec8751 / -— |
| Jogador 5 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004266899544745684 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013763166032731533 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 107 | PASS | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 112 | SELL | STABILIZE | 94.0 | 5 | 16 | 1 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023897485807538033 | 0.0 | 0.0 | +— / -68cd8ae3-399f-461f-89a8-189d7b0a6b59 |
| Jogador 5 | 2-7 | 113 | BUY | STABILIZE | 94.0 | 5 | 19 | 1 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9067155718803406 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 114 | SELL | STABILIZE | 94.0 | 5 | 18 | 1 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056166667491197586 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 5 | 2-7 | 115 | BUY | STABILIZE | 94.0 | 5 | 21 | 2 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.813282310962677 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 116 | SELL | STABILIZE | 94.0 | 5 | 19 | 1 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01836666651070118 | 0.0 | 0.0 | +— / -df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 2-7 | 117 | BUY | STABILIZE | 94.0 | 5 | 22 | 2 | 14.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9429404735565186 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -02c39b42-90d5-4e01-9380-460b6c1cb993,eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 2-7 | 118 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 21 | 2 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 21 | 2 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02846306934952736 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 120 | PASS | STABILIZE | 94.0 | 5 | 21 | 2 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 122 | BUY | STABILIZE | 94.0 | 5 | 28 | 2 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8487902283668518 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -7098795b-11bf-4b73-837a-87f5d8aece4c,837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 5 | 26 | 2 | 10.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11367479711771011 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 124 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 26 | 2 | 10.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44266802072525024 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 26 | 2 | 12.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05739628151059151 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 26 | 2 | 12.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26420101523399353 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 127 | PASS | STABILIZE | 94.0 | 5 | 26 | 2 | 12.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07900000363588333 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 132 | BUY | STABILIZE | 94.0 | 5 | 34 | 3 | 12.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8371850252151489 | 0.0 | 0.0 | +1662b43d-12f4-45d6-b1bf-3733d5214808 / -— |
| Jogador 5 | 3-2 | 133 | BUY | STABILIZE | 94.0 | 5 | 33 | 3 | 12.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8679676651954651 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -46838f8d-8037-485c-8c34-9639f14ada19,f9c418e0-f8aa-4492-8b97-8855ce3af370 |
| Jogador 5 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 32 | 3 | 10.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5719900727272034 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 135 | BUY | STABILIZE | 94.0 | 5 | 32 | 3 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07001014053821564 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 30 | 3 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04198087751865387 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 30 | 3 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 30 | 3 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 139 | PASS | STABILIZE | 94.0 | 5 | 30 | 3 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12300000339746475 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 142 | BUY | STABILIZE | 94.0 | 6 | 40 | 4 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21426540613174438 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 143 | BUY | STABILIZE | 94.0 | 6 | 36 | 3 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2891223728656769 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -— |
| Jogador 5 | 3-3 | 144 | SELL | STABILIZE | 94.0 | 6 | 34 | 3 | 14.0 | Enfeitiçador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5111260414123535 | 0.0 | 0.0 | +— / -ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-3 | 145 | BUY | STABILIZE | 94.0 | 6 | 39 | 3 | 14.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29352277517318726 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 146 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 36 | 3 | 14.0 | Enfeitiçador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5385141372680664 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 147 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 36 | 3 | 14.0 | Enfeitiçador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5691454410552979 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 148 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 36 | 3 | 18.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0687636286020279 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 36 | 3 | 18.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2428918331861496 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 36 | 3 | 18.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2458425909280777 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 152 | BUY | STABILIZE | 84.0 | 6 | 44 | 4 | 18.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8826557993888855 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -1662b43d-12f4-45d6-b1bf-3733d5214808,2e4ab22c-62d7-425c-9528-2e1315655c24 |
| Jogador 5 | 3-4 | 153 | BUY | STABILIZE | 84.0 | 6 | 43 | 4 | 18.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6301238536834717 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 154 | BUY | STABILIZE | 84.0 | 6 | 41 | 4 | 18.0 | Enfeitiçador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6580983400344849 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -— |
| Jogador 5 | 3-4 | 155 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 40 | 4 | 18.0 | Enfeitiçador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016294024884700775 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 156 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 40 | 4 | 18.0 | Enfeitiçador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30005910992622375 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 157 | PASS | STABILIZE | 84.0 | 6 | 40 | 4 | 18.0 | Enfeitiçador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 162 | SELL | STABILIZE | 84.0 | 6 | 49 | 4 | 18.0 | Enfeitiçador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5105999708175659 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 3-5 | 163 | BUY | STABILIZE | 84.0 | 6 | 52 | 5 | 18.0 | Enfeitiçador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22477038204669952 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -— |
| Jogador 5 | 3-5 | 164 | SELL | STABILIZE | 84.0 | 6 | 51 | 5 | 18.0 | Enfeitiçador/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -6084e8d8-82f2-47e3-b8e1-4077ad70efe5 |
| Jogador 5 | 3-5 | 165 | BUY | STABILIZE | 84.0 | 6 | 54 | 5 | 18.0 | Enfeitiçador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11679260432720184 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 51 | 5 | 18.0 | Enfeitiçador/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0332334004342556 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 51 | 5 | 18.0 | Enfeitiçador/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033030297607183456 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 168 | PASS | STABILIZE | 84.0 | 6 | 51 | 5 | 18.0 | Enfeitiçador/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05633125081658363 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 172 | SELL | STABILIZE | 73.0 | 6 | 62 | 5 | 18.0 | Enfeitiçador/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -4d8c374c-264c-47d9-8cfc-78cbf64ceda0 |
| Jogador 5 | 3-6 | 173 | BUY | STABILIZE | 73.0 | 6 | 65 | 5 | 18.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8682665824890137 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -135065df-1ebc-413d-86f1-4df28bd3ee41,b6a21130-c9dc-45ad-8ddb-9223b0ec8751 |
| Jogador 5 | 3-6 | 174 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 64 | 5 | 16.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.40902629494667053 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 175 | EQUIP_FROM_INVENTORY | STABILIZE | 73.0 | 6 | 64 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08150964975357056 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 176 | EQUIP_FROM_INVENTORY | STABILIZE | 73.0 | 6 | 64 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10941193252801895 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 177 | BUY | STABILIZE | 73.0 | 6 | 64 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1438649445772171 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 62 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05510983243584633 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 179 | SELL | STABILIZE | 73.0 | 6 | 62 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1874532848596573 | 0.0 | 0.0 | +— / -bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 |
| Jogador 5 | 3-6 | 180 | BUY_XP | STABILIZE | 73.0 | 6 | 65 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016540000215172768 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 182 | BUY | STABILIZE | 73.0 | 6 | 72 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8431724905967712 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -— |
| Jogador 5 | 3-7 | 183 | BUY | STABILIZE | 73.0 | 6 | 70 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0790269747376442 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 184 | SELL | STABILIZE | 73.0 | 6 | 67 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029656553640961647 | 0.0 | 0.0 | +— / -ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 3-7 | 185 | BUY | STABILIZE | 73.0 | 6 | 68 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17135141789913177 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 5 | 3-7 | 186 | BUY_XP | STABILIZE | 73.0 | 6 | 65 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031408000737428665 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 187 | BUY_XP | STABILIZE | 73.0 | 6 | 61 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031408000737428665 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 188 | BUY_XP | STABILIZE | 73.0 | 6 | 57 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031408000737428665 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 189 | BUY_XP | STABILIZE | 73.0 | 6 | 53 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05844400078058243 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 49 | 4 | 20.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 73.0 | 6 | 58 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1556459665298462 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 73.0 | 6 | 58 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12188414484262466 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 194 | SELL | STABILIZE | 73.0 | 6 | 58 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03001110628247261 | 0.0 | 0.0 | +— / -750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 5 | 4-1 | 195 | BUY | STABILIZE | 73.0 | 6 | 60 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9618372321128845 | 0.0 | 0.0 | +0c07379e-5dd1-42e9-aa7a-a764f949deee / -691cde76-cf1b-4a60-b818-65f790e312ec,b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 4-1 | 196 | BUY | STABILIZE | 73.0 | 6 | 58 | 5 | 16.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36809664964675903 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 197 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 55 | 5 | 16.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6052247285842896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 198 | BUY | STABILIZE | 73.0 | 6 | 55 | 5 | 24.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12828610837459564 | 0.0 | 0.0 | +f6de9b7d-1373-459e-b34a-7b878d1a1268 / -— |
| Jogador 5 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 54 | 5 | 24.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08024420589208603 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 54 | 5 | 24.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04446350410580635 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 202 | SELL | STABILIZE | 63.0 | 6 | 64 | 5 | 24.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -f6de9b7d-1373-459e-b34a-7b878d1a1268 |
| Jogador 5 | 4-2 | 203 | BUY | STABILIZE | 63.0 | 6 | 65 | 5 | 24.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1830393522977829 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 5 | 4-2 | 204 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 61 | 5 | 24.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21461763978004456 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 205 | MOVE_BOARD | FAST8 | 63.0 | 6 | 61 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01779213920235634 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 206 | PASS | FAST8 | 63.0 | 6 | 61 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08661596477031708 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 212 | SELL | FAST8 | 51.0 | 6 | 72 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 5 | 4-3 | 213 | BUY | FAST8 | 51.0 | 6 | 75 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8411133885383606 | 0.0 | 0.0 | +7bcf9a7f-a7c9-44a7-9d12-e1ba998b23ed / -— |
| Jogador 5 | 4-3 | 214 | SELL | FAST8 | 51.0 | 6 | 72 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -4af85188-f11e-4aca-8165-ba8e7f535670 |
| Jogador 5 | 4-3 | 215 | BUY | FAST8 | 51.0 | 6 | 75 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004087300505489111 | 0.0 | 0.0 | +7b3e8122-3b51-46b5-94a8-68fb77156e0e / -— |
| Jogador 5 | 4-3 | 216 | MOVE_BOARD | FAST8 | 51.0 | 6 | 72 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 217 | MOVE_BOARD | FAST8 | 51.0 | 6 | 72 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 218 | PASS | FAST8 | 51.0 | 6 | 72 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09418163448572159 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 222 | SELL | FAST8 | 51.0 | 7 | 83 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 |
| Jogador 5 | 4-4 | 223 | BUY | FAST8 | 51.0 | 7 | 86 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16106373071670532 | 0.0 | 0.0 | +30d2995a-d9b8-4424-af46-8766734e440c / -— |
| Jogador 5 | 4-4 | 224 | MOVE_BENCH | FAST8 | 51.0 | 7 | 85 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5877242684364319 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 225 | BUY | FAST8 | 51.0 | 7 | 85 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12971711158752441 | 0.0 | 0.0 | +f4173576-aa2e-4a93-94ec-ecd49d90d2b7 / -— |
| Jogador 5 | 4-4 | 226 | MOVE_BOARD | FAST8 | 51.0 | 7 | 82 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009271646849811077 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 227 | MOVE_BOARD | FAST8 | 51.0 | 7 | 82 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010919439606368542 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 228 | MOVE_BOARD | FAST8 | 51.0 | 7 | 82 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014966603368520737 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 229 | PASS | FAST8 | 51.0 | 7 | 82 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10141540318727493 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 232 | SELL | FAST8 | 51.0 | 7 | 92 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030082788318395615 | 0.0 | 0.0 | +— / -30d2995a-d9b8-4424-af46-8766734e440c |
| Jogador 5 | 4-5 | 233 | BUY | FAST8 | 51.0 | 7 | 93 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2899160385131836 | 0.0 | 0.0 | +c49cf468-6fa4-4d94-bc3a-9dc8f7111626 / -— |
| Jogador 5 | 4-5 | 234 | MOVE_BOARD | FAST8 | 51.0 | 7 | 92 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 235 | SELL | FAST8 | 51.0 | 7 | 92 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010333333164453506 | 0.0 | 0.0 | +— / -f4173576-aa2e-4a93-94ec-ecd49d90d2b7 |
| Jogador 5 | 4-5 | 236 | BUY | FAST8 | 51.0 | 7 | 95 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19006682932376862 | 0.0 | 0.0 | +226f36b1-cb9a-464a-a10a-3f21ebd41f24 / -— |
| Jogador 5 | 4-5 | 237 | MOVE_BOARD | FAST8 | 51.0 | 7 | 94 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.77410662319744e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 238 | MOVE_BOARD | FAST8 | 51.0 | 7 | 94 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015026405453681946 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 239 | MOVE_BOARD | FAST8 | 51.0 | 7 | 94 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014995870180428028 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 240 | PASS | FAST8 | 51.0 | 7 | 94 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11039899289608002 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 242 | SELL | STABILIZE | 38.0 | 7 | 104 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -7b3e8122-3b51-46b5-94a8-68fb77156e0e |
| Jogador 5 | 4-6 | 243 | BUY | STABILIZE | 38.0 | 7 | 107 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11238717287778854 | 0.0 | 0.0 | +98b72340-a402-45bc-9493-71263e3168d6 / -— |
| Jogador 5 | 4-6 | 244 | SELL | STABILIZE | 38.0 | 7 | 104 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -98b72340-a402-45bc-9493-71263e3168d6 |
| Jogador 5 | 4-6 | 245 | BUY | STABILIZE | 38.0 | 7 | 107 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16371962428092957 | 0.0 | 0.0 | +738fea60-6b44-40f1-9936-43accf852bd7 / -— |
| Jogador 5 | 4-6 | 246 | BUY_XP | STABILIZE | 38.0 | 7 | 103 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038895998150110245 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 247 | BUY_XP | STABILIZE | 38.0 | 7 | 99 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038895998150110245 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 248 | BUY_XP | STABILIZE | 38.0 | 7 | 95 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038895998150110245 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 249 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 91 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0006128131062723696 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 250 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 91 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014757310040295124 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 252 | SELL | STABILIZE | 38.0 | 7 | 102 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0025333333760499954 | 0.0 | 0.0 | +— / -738fea60-6b44-40f1-9936-43accf852bd7 |
| Jogador 5 | 4-7 | 253 | BUY | STABILIZE | 38.0 | 7 | 106 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.847148060798645 | 0.0 | 0.0 | +d1bc6c5b-74a5-46db-b00f-e91265546f5d / -— |
| Jogador 5 | 4-7 | 254 | SELL | STABILIZE | 38.0 | 7 | 104 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1390102207660675 | 0.0 | 0.0 | +— / -60255a84-4f78-49f0-a4f1-d598704c7ee7 |
| Jogador 5 | 4-7 | 255 | BUY | STABILIZE | 38.0 | 7 | 107 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14489176869392395 | 0.0 | 0.0 | +f8a93323-530e-4f9c-99d7-a5ec83b78992 / -— |
| Jogador 5 | 4-7 | 256 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 106 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3757322132587433 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 257 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 106 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4127291440963745 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 258 | PASS | STABILIZE | 38.0 | 7 | 106 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1410384625196457 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 7 | 116 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1638985574245453 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 7 | 116 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1918746680021286 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 264 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 116 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146204054355621 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 265 | SELL | STABILIZE | 38.0 | 7 | 116 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02972332201898098 | 0.0 | 0.0 | +— / -f8a93323-530e-4f9c-99d7-a5ec83b78992 |
| Jogador 5 | 5-1 | 266 | BUY | STABILIZE | 38.0 | 7 | 117 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16611790657043457 | 0.0 | 0.0 | +d6a929d8-6d7c-4bcd-880d-d819daca2ae0 / -— |
| Jogador 5 | 5-1 | 267 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 114 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32740750908851624 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 268 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 114 | 5 | 36.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3999848961830139 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 269 | PASS | STABILIZE | 38.0 | 7 | 114 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.163448303937912 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 272 | SELL | STABILIZE | 38.0 | 7 | 126 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028288178145885468 | 0.0 | 0.0 | +— / -d6a929d8-6d7c-4bcd-880d-d819daca2ae0 |
| Jogador 5 | 5-2 | 273 | BUY | STABILIZE | 38.0 | 7 | 129 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42103928327560425 | 0.0 | 0.0 | +2949d735-3c16-4a45-835b-e11a9c12b16a / -— |
| Jogador 5 | 5-2 | 274 | SELL | STABILIZE | 38.0 | 7 | 126 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4448487460613251 | 0.0 | 0.0 | +— / -ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 5-2 | 275 | BUY | STABILIZE | 38.0 | 7 | 127 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5303745269775391 | 0.0 | 0.0 | +0d120db3-34e2-47e3-a57c-0d65dcc56342 / -— |
| Jogador 5 | 5-2 | 276 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 126 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09917338937520981 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 277 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 126 | 5 | 34.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5097013115882874 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 278 | REROLL | STABILIZE | 38.0 | 7 | 126 | 5 | 36.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 279 | SELL | STABILIZE | 38.0 | 7 | 124 | 5 | 36.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44470152258872986 | 0.0 | 0.0 | +— / -0d120db3-34e2-47e3-a57c-0d65dcc56342 |
| Jogador 5 | 5-2 | 280 | BUY | STABILIZE | 38.0 | 7 | 125 | 5 | 36.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1542544960975647 | 0.0 | 0.0 | +45ae38c5-7e69-41bb-9a93-f14db3af3587 / -— |
| Jogador 5 | 5-3 | 282 | SELL | STABILIZE | 38.0 | 7 | 134 | 5 | 36.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -45ae38c5-7e69-41bb-9a93-f14db3af3587 |
| Jogador 5 | 5-3 | 283 | BUY | STABILIZE | 38.0 | 7 | 137 | 5 | 36.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.921033501625061 | 0.0 | 0.0 | +e9bb05f6-3838-423a-bfd2-3791379b479e / -— |
| Jogador 5 | 5-3 | 284 | SELL | STABILIZE | 38.0 | 7 | 134 | 5 | 36.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.475588321685791 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 5-3 | 285 | BUY | STABILIZE | 38.0 | 7 | 136 | 5 | 36.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15689179301261902 | 0.0 | 0.0 | +1c5a9322-14c8-4df9-937b-842dcaa1f372 / -— |
| Jogador 5 | 5-3 | 286 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 133 | 5 | 36.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39959150552749634 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 287 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 133 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07202019542455673 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 288 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 133 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5589824914932251 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 289 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 133 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39753830432891846 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 290 | PASS | STABILIZE | 38.0 | 7 | 133 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18209980428218842 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 292 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 143 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09767989814281464 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 293 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 143 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5823656916618347 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 294 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 143 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6076030731201172 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 295 | PASS | ALL_IN | 22.0 | 7 | 143 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5599479675292969 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 302 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 153 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3430462181568146 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 303 | SELL | ALL_IN | 22.0 | 7 | 153 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -1c5a9322-14c8-4df9-937b-842dcaa1f372 |
| Jogador 5 | 5-5 | 304 | BUY | ALL_IN | 22.0 | 7 | 156 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9027383923530579 | 0.0 | 0.0 | +3faf4ab2-44b3-4779-985b-658c64791c28 / -— |
| Jogador 5 | 5-5 | 305 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 154 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3947712182998657 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 306 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 154 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03734978660941124 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 307 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 154 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36067381501197815 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 308 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 154 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39800551533699036 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 309 | PASS | ALL_IN | 22.0 | 7 | 154 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5699149370193481 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 312 | SELL | ALL_IN | 22.0 | 7 | 165 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6797000169754028 | 0.0 | 0.0 | +— / -c49cf468-6fa4-4d94-bc3a-9dc8f7111626 |
| Jogador 5 | 5-6 | 313 | BUY | ALL_IN | 22.0 | 7 | 166 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10809684544801712 | 0.0 | 0.0 | +e5f61076-ec13-419b-a4e8-d91b9975cfd6 / -— |
| Jogador 5 | 5-6 | 314 | SELL | ALL_IN | 22.0 | 7 | 163 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -e5f61076-ec13-419b-a4e8-d91b9975cfd6 |
| Jogador 5 | 5-6 | 315 | BUY | ALL_IN | 22.0 | 7 | 166 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10816454142332077 | 0.0 | 0.0 | +83a3ef65-b342-4ec8-b2d1-be99c3602f81 / -— |
| Jogador 5 | 5-6 | 316 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 163 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09216393530368805 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 317 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 163 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38561928272247314 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 318 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 163 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4090327024459839 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 319 | PASS | ALL_IN | 22.0 | 7 | 163 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.578149139881134 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 322 | SELL | ALL_IN | 22.0 | 7 | 173 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -83a3ef65-b342-4ec8-b2d1-be99c3602f81 |
| Jogador 5 | 5-7 | 323 | BUY | ALL_IN | 22.0 | 7 | 176 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4365484416484833 | 0.0 | 0.0 | +a37d8478-8a98-4099-bb18-3602d68764f5 / -— |
| Jogador 5 | 5-7 | 324 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 175 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05215857923030853 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 325 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 175 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3622390627861023 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 326 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 175 | 5 | 30.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39784082770347595 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 327 | PASS | ALL_IN | 22.0 | 7 | 175 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5892298221588135 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 7 | 185 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10366027802228928 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 333 | SELL | ALL_IN | 22.0 | 7 | 185 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6797000169754028 | 0.0 | 0.0 | +— / -a37d8478-8a98-4099-bb18-3602d68764f5 |
| Jogador 5 | 6-1 | 334 | BUY | ALL_IN | 22.0 | 7 | 186 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12875069677829742 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -— |
| Jogador 5 | 6-1 | 335 | SELL | ALL_IN | 22.0 | 7 | 182 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -4261ad99-2607-4d90-978c-9e9abffd6d95 |
| Jogador 5 | 6-1 | 336 | BUY | ALL_IN | 22.0 | 7 | 186 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17740820348262787 | 0.0 | 0.0 | +920ec426-49cf-489f-aad8-3f5461b93be6 / -— |
| Jogador 5 | 6-1 | 337 | REROLL | ALL_IN | 22.0 | 7 | 182 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 338 | SELL | ALL_IN | 22.0 | 7 | 180 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -920ec426-49cf-489f-aad8-3f5461b93be6 |
| Jogador 5 | 6-1 | 339 | BUY | ALL_IN | 22.0 | 7 | 184 | 5 | 32.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1113468408584595 | 0.0 | 0.0 | +dc423197-9320-4651-b71d-a62086416f9d / -1d7b6420-388f-4cb1-b25c-2e5a3dfec742,7bcf9a7f-a7c9-44a7-9d12-e1ba998b23ed |
| Jogador 5 | 6-1 | 340 | BUY | ALL_IN | 22.0 | 7 | 181 | 5 | 32.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1095020771026611 | 0.0 | 0.0 | +92bac611-1820-42eb-8243-499f20058673 / -3faf4ab2-44b3-4779-985b-658c64791c28,8a4e95ea-d35a-4690-9313-126b5d86773e |
| Jogador 5 | 6-2 | 342 | BUY | ALL_IN | 22.0 | 7 | 191 | 5 | 28.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5205978751182556 | 0.0 | 0.0 | +4b4293ce-1cca-473e-8c07-b441686985ac / -— |
| Jogador 5 | 6-2 | 343 | BUY | ALL_IN | 22.0 | 7 | 188 | 5 | 28.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4987710118293762 | 0.0 | 0.0 | +8025eaf5-b02b-4f94-b381-b94321bca206 / -— |
| Jogador 5 | 6-2 | 344 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 186 | 5 | 28.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5660894513130188 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 345 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 186 | 5 | 30.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35314545035362244 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 346 | BUY | ALL_IN | 22.0 | 7 | 186 | 5 | 36.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1906733512878418 | 0.0 | 0.0 | +c4ec99e0-d973-42e9-a20e-1a9e7f5bf89a / -— |
| Jogador 5 | 6-2 | 347 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 183 | 5 | 36.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39962756633758545 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 348 | REROLL | ALL_IN | 22.0 | 7 | 183 | 5 | 34.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 349 | SELL | ALL_IN | 22.0 | 7 | 181 | 5 | 34.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6848999857902527 | 0.0 | 0.0 | +— / -92bac611-1820-42eb-8243-499f20058673 |
| Jogador 5 | 6-2 | 350 | BUY | ALL_IN | 22.0 | 7 | 186 | 5 | 34.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1096714735031128 | 0.0 | 0.0 | +4321582a-0b45-4666-a119-7b49e92d012a / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb,d1bc6c5b-74a5-46db-b00f-e91265546f5d |
| Jogador 5 | 6-3 | 352 | BUY | ALL_IN | 22.0 | 7 | 195 | 5 | 30.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.792091965675354 | 0.0 | 0.0 | +249d7b90-0660-4e4f-885a-7791c1cac21a / -— |
| Jogador 5 | 6-3 | 353 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 192 | 5 | 30.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08588522672653198 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 354 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 192 | 5 | 32.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4016573429107666 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 355 | BUY | ALL_IN | 22.0 | 7 | 192 | 5 | 38.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0018694588216021657 | 0.0 | 0.0 | +07080859-42b2-498e-9c11-257fea02f14b / -— |
| Jogador 5 | 6-3 | 356 | MOVE_BOARD | ALL_IN | 22.0 | 7 | 189 | 5 | 38.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 357 | MOVE_BOARD | ALL_IN | 22.0 | 7 | 189 | 5 | 38.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014989125542342663 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 358 | PASS | ALL_IN | 22.0 | 7 | 189 | 5 | 38.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6279548406600952 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 362 | SELL | ALL_IN | 22.0 | 7 | 201 | 5 | 38.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6783999800682068 | 0.0 | 0.0 | +— / -dc423197-9320-4651-b71d-a62086416f9d |
| Jogador 5 | 6-4 | 363 | BUY | ALL_IN | 22.0 | 7 | 209 | 5 | 38.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46304190158843994 | 0.0 | 0.0 | +ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 / -— |
| Jogador 5 | 6-4 | 364 | REROLL | ALL_IN | 22.0 | 7 | 207 | 5 | 38.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07000000029802322 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 365 | SELL | ALL_IN | 22.0 | 7 | 205 | 5 | 38.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02983333356678486 | 0.0 | 0.0 | +— / -07080859-42b2-498e-9c11-257fea02f14b |
| Jogador 5 | 6-4 | 366 | BUY | ALL_IN | 22.0 | 7 | 208 | 5 | 38.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49154525995254517 | 0.0 | 0.0 | +6875f839-cf68-443f-9776-887087b375d3 / -— |
| Jogador 5 | 6-4 | 367 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 203 | 5 | 38.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2793302536010742 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 368 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 203 | 5 | 40.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08422204107046127 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 369 | REROLL | ALL_IN | 22.0 | 7 | 203 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07000000029802322 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 370 | SELL | ALL_IN | 22.0 | 7 | 201 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019999999552965164 | 0.0 | 0.0 | +— / -5627d898-cff3-4664-87d1-40a8f3656ab3 |
| Jogador 5 | 6-5 | 372 | BUY | ALL_IN | 22.0 | 7 | 213 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.016932375729084015 | 0.0 | 0.0 | +910b14c4-57bc-44ce-b925-30a6d92a7651 / -— |
| Jogador 5 | 6-5 | 373 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 7 | 209 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12416131794452667 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 374 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 7 | 209 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.072174072265625 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 375 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 7 | 209 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09838799387216568 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 376 | REROLL | ALL_IN | 22.0 | 7 | 209 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07000000029802322 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 377 | SELL | ALL_IN | 22.0 | 7 | 207 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -910b14c4-57bc-44ce-b925-30a6d92a7651 |
| Jogador 5 | 6-5 | 378 | BUY | ALL_IN | 22.0 | 7 | 211 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5738939642906189 | 0.0 | 0.0 | +e903e009-8dae-4fc9-b0ec-bc028c3f9f3e / -— |
| Jogador 5 | 6-5 | 379 | REROLL | ALL_IN | 22.0 | 7 | 209 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07000000029802322 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 380 | SELL | ALL_IN | 22.0 | 7 | 207 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5817843675613403 | 0.0 | 0.0 | +— / -e903e009-8dae-4fc9-b0ec-bc028c3f9f3e |
| Jogador 5 | 6-6 | 382 | BUY | ALL_IN | 22.0 | 7 | 221 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18392875790596008 | 0.0 | 0.0 | +14f6071d-5085-47a5-b657-04043b21adce / -— |
| Jogador 5 | 6-6 | 383 | REROLL | ALL_IN | 22.0 | 7 | 217 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07000000029802322 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 384 | SELL | ALL_IN | 22.0 | 7 | 215 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0061333333142101765 | 0.0 | 0.0 | +— / -14f6071d-5085-47a5-b657-04043b21adce |
| Jogador 5 | 6-6 | 385 | BUY | ALL_IN | 22.0 | 7 | 219 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5738946199417114 | 0.0 | 0.0 | +28a07a1f-a937-42e3-b3c3-27738ce56c4f / -— |
| Jogador 5 | 6-6 | 386 | REROLL | ALL_IN | 22.0 | 7 | 217 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07000000029802322 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 387 | REROLL | ALL_IN | 22.0 | 7 | 215 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07000000029802322 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 388 | REROLL | ALL_IN | 22.0 | 7 | 213 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07000000029802322 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 389 | SELL | ALL_IN | 22.0 | 7 | 211 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06753333657979965 | 0.0 | 0.0 | +— / -ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 |
| Jogador 5 | 6-6 | 390 | BUY | ALL_IN | 22.0 | 7 | 213 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0389642715454102 | 0.0 | 0.0 | +bdee88f4-e5b5-48fb-9ae5-1fd155982995 / -— |
| Jogador 5 | 6-7 | 392 | SELL | ALL_IN | 22.0 | 7 | 225 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6783999800682068 | 0.0 | 0.0 | +— / -8025eaf5-b02b-4f94-b381-b94321bca206 |
| Jogador 5 | 6-7 | 393 | BUY | ALL_IN | 22.0 | 7 | 227 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6717413067817688 | 0.0 | 0.0 | +fe772b41-d367-4385-b35f-eb5c07754a32 / -— |
| Jogador 5 | 6-7 | 394 | REROLL | ALL_IN | 22.0 | 7 | 226 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07000000029802322 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-7 | 395 | SELL | ALL_IN | 22.0 | 7 | 224 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5857333540916443 | 0.0 | 0.0 | +— / -fe772b41-d367-4385-b35f-eb5c07754a32 |
| Jogador 5 | 6-7 | 396 | BUY | ALL_IN | 22.0 | 7 | 225 | 5 | 46.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1075869798660278 | 0.0 | 0.0 | +84250843-db6c-4e91-9c6f-b12e36fc31cb / -28a07a1f-a937-42e3-b3c3-27738ce56c4f,68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 6-7 | 397 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 223 | 5 | 42.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5965278744697571 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-7 | 398 | MOVE_BOARD | ALL_IN | 22.0 | 7 | 223 | 5 | 44.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014902016147971153 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-7 | 399 | MOVE_BOARD | ALL_IN | 22.0 | 7 | 223 | 5 | 44.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015160731971263885 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-7 | 400 | PASS | ALL_IN | 22.0 | 7 | 223 | 5 | 44.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8199999928474426 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-1 | 402 | BUY | ALL_IN | 22.0 | 7 | 235 | 5 | 44.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.4977709949016571 | 0.0 | 0.0 | +86aa0b8f-5eb2-483d-ab0f-033bebb928e3 / -— |
| Jogador 5 | 7-1 | 403 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 7 | 233 | 5 | 44.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.020431358367204666 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-1 | 404 | BUY | ALL_IN | 22.0 | 7 | 233 | 5 | 44.0 | Enfeitiçador/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2721971869468689 | 0.0 | 0.0 | +b1e5b3b9-fda8-4d4a-9368-94fd558da4f7 / -— |
| Jogador 5 | 7-1 | 405 | MOVE_BOARD | ALL_IN | 22.0 | 7 | 231 | 5 | 44.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00013482928625307977 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-1 | 406 | MOVE_BOARD | ALL_IN | 22.0 | 7 | 231 | 5 | 44.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-1 | 407 | MOVE_BOARD | ALL_IN | 22.0 | 7 | 231 | 5 | 44.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014952262863516808 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-1 | 408 | PASS | ALL_IN | 22.0 | 7 | 231 | 5 | 44.0 | Enfeitiçador/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6715244650840759 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Sentry | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9946255087852478 | 0.0 | 0.0 | +425b1e77-5887-40b3-875e-c1f60dc6c513 / -— |
| Jogador 6 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4511662721633911 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 33 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5818290710449219 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 46 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0226738452911377 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 47 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29404357075691223 | 0.0 | 0.0 | +72aa8420-8dc2-4e9b-a10a-bd2a36f26656 / -— |
| Jogador 6 | 1-4 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23709449172019958 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 49 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0259007215499878 | 0.0 | 0.0 | +97d28b21-b7a0-47f5-b9ee-78377ad4c7d8 / -— |
| Jogador 6 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2670624256134033 | 0.0 | 0.0 | +c8b72b14-11a4-48e6-8135-41efdbc347cb / -— |
| Jogador 6 | 2-1 | 61 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 62 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21214060485363007 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 63 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20030145347118378 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00969630666077137 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 65 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15218128263950348 | 0.0 | 0.0 | +— / -c8b72b14-11a4-48e6-8135-41efdbc347cb |
| Jogador 6 | 2-1 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06564632803201675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023661794140934944 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 68 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 70 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12802888453006744 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 71 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17737601697444916 | 0.0 | 0.0 | +f82eae62-dfe9-41bc-b346-71bf2c7cca02 / -— |
| Jogador 6 | 2-2 | 72 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35526958107948303 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 73 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014476965181529522 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 74 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 75 | PASS | STABILIZE | 96.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 79 | BUY | STABILIZE | 96.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.301959753036499 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 80 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.271212100982666 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 81 | SELL | STABILIZE | 96.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -f82eae62-dfe9-41bc-b346-71bf2c7cca02 |
| Jogador 6 | 2-3 | 82 | SELL | STABILIZE | 96.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14222100377082825 | 0.0 | 0.0 | +— / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 |
| Jogador 6 | 2-3 | 83 | SELL | STABILIZE | 96.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004999999888241291 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-3 | 84 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 11 | 1 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3529147803783417 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 85 | SELL | STABILIZE | 96.0 | 4 | 11 | 1 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12618064880371094 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-4 | 87 | BUY | STABILIZE | 90.0 | 5 | 19 | 1 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.111709713935852 | 0.0 | 0.0 | +77d51a33-bfc7-4b8b-b460-8a4a45391474 / -72aa8420-8dc2-4e9b-a10a-bd2a36f26656,97d28b21-b7a0-47f5-b9ee-78377ad4c7d8 |
| Jogador 6 | 2-4 | 88 | BUY | STABILIZE | 90.0 | 5 | 18 | 1 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2331717312335968 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 89 | BUY | STABILIZE | 90.0 | 5 | 17 | 1 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9427397847175598 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 90 | BUY_XP | STABILIZE | 90.0 | 5 | 16 | 1 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 91 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 12 | 1 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5337590575218201 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 93 | BUY | STABILIZE | 90.0 | 5 | 18 | 1 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1175222396850586 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -425b1e77-5887-40b3-875e-c1f60dc6c513,908afab9-748c-4057-a2a9-d2686c5d52e0 |
| Jogador 6 | 2-5 | 94 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 17 | 1 | 8.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24926821887493134 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 95 | BUY | STABILIZE | 90.0 | 5 | 17 | 1 | 10.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18501301109790802 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 96 | BUY | STABILIZE | 90.0 | 5 | 15 | 1 | 10.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020993297919631004 | 0.0 | 0.0 | +0023f061-5310-4e39-849a-22ad49993d8c / -— |
| Jogador 6 | 2-5 | 97 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 13 | 1 | 10.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005158385261893272 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 98 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 13 | 1 | 10.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 99 | PASS | STABILIZE | 90.0 | 5 | 13 | 1 | 10.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 102 | BUY | STABILIZE | 90.0 | 5 | 20 | 2 | 14.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30789002776145935 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 103 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 17 | 1 | 14.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 17 | 1 | 14.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07296731323003769 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 105 | PASS | STABILIZE | 90.0 | 5 | 17 | 1 | 14.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020357143133878708 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 112 | BUY | STABILIZE | 84.0 | 5 | 23 | 2 | 14.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9737855195999146 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 113 | BUY | STABILIZE | 84.0 | 5 | 20 | 2 | 14.0 | Colosso/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29376474022865295 | 0.0 | 0.0 | +a2f987f8-01d6-4463-9ab4-f96c9b6f067b / -— |
| Jogador 6 | 2-7 | 114 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 19 | 1 | 14.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24120260775089264 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 19 | 1 | 14.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 19 | 1 | 14.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09647087752819061 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 117 | PASS | STABILIZE | 84.0 | 5 | 19 | 1 | 14.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020714284852147102 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 122 | BUY | STABILIZE | 84.0 | 5 | 25 | 2 | 14.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2865656912326813 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 5 | 22 | 2 | 14.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2555924654006958 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 124 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 22 | 2 | 14.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24476344883441925 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 22 | 2 | 14.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04546266794204712 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 22 | 2 | 14.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003905561985448003 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 127 | PASS | STABILIZE | 84.0 | 5 | 22 | 2 | 14.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05950000137090683 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 132 | BUY | STABILIZE | 72.0 | 5 | 30 | 3 | 14.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7879750728607178 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 133 | BUY | STABILIZE | 72.0 | 5 | 29 | 2 | 10.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8510215282440186 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -18934be2-4988-4f62-9f62-07ba151231f2,53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 28 | 2 | 8.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15000693500041962 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 135 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 28 | 2 | 12.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05842085927724838 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 136 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 28 | 2 | 12.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03998624160885811 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 137 | PASS | STABILIZE | 72.0 | 5 | 28 | 2 | 16.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024000000208616257 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 142 | BUY | STABILIZE | 61.0 | 5 | 36 | 3 | 22.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8335039615631104 | 0.0 | 0.0 | +25b16126-6e41-4649-a47f-42656ffc7a08 / -— |
| Jogador 6 | 3-3 | 143 | BUY | STABILIZE | 61.0 | 5 | 34 | 3 | 22.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2644606828689575 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 144 | MOVE_BOARD | STABILIZE | 61.0 | 5 | 31 | 3 | 22.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 61.0 | 5 | 31 | 3 | 22.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037586942315101624 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 146 | PASS | STABILIZE | 61.0 | 5 | 31 | 3 | 22.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12349999696016312 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 152 | BUY | STABILIZE | 52.0 | 5 | 40 | 4 | 22.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.735737681388855 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 6 | 3-4 | 153 | MOVE_BENCH | STABILIZE | 52.0 | 5 | 37 | 3 | 22.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3979668915271759 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 154 | MOVE_BOARD | STABILIZE | 52.0 | 5 | 37 | 3 | 24.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 155 | PASS | STABILIZE | 52.0 | 5 | 37 | 3 | 24.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1264999955892563 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 162 | BUY | STABILIZE | 52.0 | 6 | 46 | 4 | 24.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8796941041946411 | 0.0 | 0.0 | +506f7312-07d8-4165-bd67-f7a69cf9a19c / -25b16126-6e41-4649-a47f-42656ffc7a08,c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 3-5 | 163 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 44 | 4 | 20.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1309075802564621 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 44 | 4 | 20.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3562927842140198 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 165 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 44 | 4 | 24.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37420785427093506 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 166 | BUY | FAST8 | 52.0 | 6 | 44 | 4 | 26.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15842054784297943 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 167 | MOVE_BOARD | FAST8 | 52.0 | 6 | 41 | 4 | 26.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01059259008616209 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 168 | MOVE_BENCH | FAST8 | 52.0 | 6 | 41 | 4 | 26.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4809408485889435 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 169 | MOVE_BOARD | FAST8 | 52.0 | 6 | 41 | 4 | 34.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006346242036670446 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 170 | MOVE_BOARD | FAST8 | 52.0 | 6 | 41 | 4 | 34.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 172 | MOVE_BOARD | FAST8 | 52.0 | 6 | 51 | 5 | 34.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.7931895601795986e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 173 | MOVE_BOARD | FAST8 | 52.0 | 6 | 51 | 5 | 34.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01399148814380169 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 174 | MOVE_BOARD | FAST8 | 52.0 | 6 | 51 | 5 | 34.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014968053437769413 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 175 | PASS | FAST8 | 52.0 | 6 | 51 | 5 | 34.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1543312519788742 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 182 | BUY | FAST8 | 42.0 | 6 | 61 | 5 | 34.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2682296931743622 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 183 | MOVE_BENCH | FAST8 | 42.0 | 6 | 57 | 5 | 34.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09995424002408981 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 184 | MOVE_BOARD | FAST8 | 42.0 | 6 | 57 | 5 | 36.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 185 | MOVE_BOARD | FAST8 | 42.0 | 6 | 57 | 5 | 36.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030335303395986557 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 186 | PASS | FAST8 | 42.0 | 6 | 57 | 5 | 36.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16107286512851715 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 42.0 | 6 | 67 | 5 | 36.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2218843698501587 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 42.0 | 6 | 67 | 5 | 36.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2187643200159073 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 194 | BUY | FAST8 | 42.0 | 6 | 67 | 5 | 36.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.668906569480896 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -— |
| Jogador 6 | 4-1 | 195 | MOVE_BENCH | FAST8 | 42.0 | 6 | 64 | 5 | 36.0 | Emanador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3854736089706421 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 196 | MOVE_BENCH | FAST8 | 42.0 | 6 | 64 | 5 | 32.0 | Emanador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6853238940238953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 197 | PASS | FAST8 | 42.0 | 6 | 64 | 5 | 32.0 | Emanador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09545251727104187 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 202 | SELL | STABILIZE | 31.0 | 6 | 75 | 5 | 32.0 | Emanador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -e29364db-c484-4e4d-954d-7f4940131ffc |
| Jogador 6 | 4-2 | 203 | BUY | STABILIZE | 31.0 | 6 | 78 | 5 | 32.0 | Emanador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9632014632225037 | 0.0 | 0.0 | +7fd8b302-97aa-4373-94f4-adfcad477ed2 / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4,f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 6 | 4-2 | 204 | BUY | STABILIZE | 31.0 | 6 | 75 | 5 | 32.0 | Emanador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.375975638628006 | 0.0 | 0.0 | +93f7279f-b03b-407b-b623-c0a2bd88f877 / -— |
| Jogador 6 | 4-2 | 205 | MOVE_BENCH | STABILIZE | 31.0 | 6 | 72 | 5 | 32.0 | Emanador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1007123813033104 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 31.0 | 6 | 72 | 5 | 36.0 | Emanador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013349766843020916 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 31.0 | 6 | 72 | 5 | 36.0 | Emanador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21611717343330383 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 208 | PASS | STABILIZE | 31.0 | 6 | 72 | 5 | 36.0 | Emanador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2646438479423523 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 212 | BUY | ALL_IN | 19.0 | 6 | 83 | 5 | 36.0 | Emanador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16692401468753815 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 6 | 4-3 | 213 | MOVE_BENCH | ALL_IN | 19.0 | 6 | 82 | 5 | 36.0 | Emanador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21044059097766876 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 214 | MOVE_BOARD | ALL_IN | 19.0 | 6 | 82 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0582432895898819 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 215 | PASS | ALL_IN | 19.0 | 6 | 82 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4808642864227295 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 222 | SELL | ALL_IN | 7.0 | 6 | 93 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6873562335968018 | 0.0 | 0.0 | +— / -77d51a33-bfc7-4b8b-b460-8a4a45391474 |
| Jogador 6 | 4-4 | 223 | BUY | ALL_IN | 7.0 | 6 | 96 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4129268229007721 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 6 | 4-4 | 224 | REROLL | ALL_IN | 7.0 | 6 | 95 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 225 | REROLL | ALL_IN | 7.0 | 6 | 93 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 226 | SELL | ALL_IN | 7.0 | 6 | 91 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7243000268936157 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 4-4 | 227 | BUY | ALL_IN | 7.0 | 6 | 94 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.4739117920398712 | 0.0 | 0.0 | +bae633d7-8337-461a-9a84-9c9758392bb6 / -— |
| Jogador 6 | 4-4 | 228 | EQUIP_FROM_INVENTORY | ALL_IN | 7.0 | 6 | 93 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15469065308570862 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 229 | MOVE_BOARD | ALL_IN | 7.0 | 6 | 93 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01996532641351223 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 230 | MOVE_BOARD | ALL_IN | 7.0 | 6 | 93 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014917734079062939 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 232 | SELL | ALL_IN | 7.0 | 6 | 104 | 5 | 38.0 | Emanador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7307999730110168 | 0.0 | 0.0 | +— / -7fd8b302-97aa-4373-94f4-adfcad477ed2 |
| Jogador 6 | 4-5 | 233 | BUY | ALL_IN | 7.0 | 6 | 112 | 5 | 38.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0807501077651978 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede,fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 4-5 | 234 | BUY | ALL_IN | 7.0 | 6 | 109 | 5 | 32.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06354248523712158 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 6 | 4-5 | 235 | MOVE_BENCH | ALL_IN | 7.0 | 6 | 106 | 5 | 32.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43157169222831726 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 236 | BUY | ALL_IN | 7.0 | 6 | 106 | 5 | 34.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.092671699821949 | 0.0 | 0.0 | +477a3c7c-70fe-4f67-ab00-8c9c397365bf / -— |
| Jogador 6 | 4-5 | 237 | MOVE_BOARD | ALL_IN | 7.0 | 6 | 103 | 5 | 34.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.8585362226986035e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 238 | MOVE_BOARD | ALL_IN | 7.0 | 6 | 103 | 5 | 34.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 239 | PASS | ALL_IN | 7.0 | 6 | 103 | 5 | 34.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5352470278739929 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 242 | SELL | ALL_IN | 7.0 | 6 | 114 | 5 | 34.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7307999730110168 | 0.0 | 0.0 | +— / -b1efce8c-0cb0-47fc-a361-c50a76c0f9de |
| Jogador 6 | 4-6 | 243 | BUY | ALL_IN | 7.0 | 6 | 122 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08254203200340271 | 0.0 | 0.0 | +772bccc4-15f4-4de2-95f8-82d0ed9a72d2 / -— |
| Jogador 6 | 4-6 | 244 | MOVE_BOARD | ALL_IN | 7.0 | 6 | 119 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.2809297206549672e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 245 | MOVE_BOARD | ALL_IN | 7.0 | 6 | 119 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499984785914421 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 246 | PASS | ALL_IN | 7.0 | 6 | 119 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5569804906845093 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3525073230266571 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 33 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0485689640045166 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 34 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.516175389289856 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 46 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.03251051902771 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13629421591758728 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 48 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1526176929473877 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 49 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15163356065750122 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0888063907623291 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 51 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26248931884765625 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11197851598262787 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.346617728471756 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 62 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04870440065860748 | 0.0 | 0.0 | +42f4384d-5499-4441-aa3b-d37e50926071 / -— |
| Jogador 7 | 2-1 | 63 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 65 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 70 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0478655099868774 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 71 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 6 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1468200534582138 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 72 | BUY | STABILIZE | 96.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.17021889984607697 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 73 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4133191704750061 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 74 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09254232048988342 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 75 | CRAFT_AND_EQUIP | STABILIZE | 96.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16018249094486237 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 76 | CRAFT_AND_EQUIP | STABILIZE | 96.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1100221499800682 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 77 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09919990599155426 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 79 | BUY | STABILIZE | 96.0 | 4 | 9 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0477375984191895 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 80 | BUY | STABILIZE | 96.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9770193099975586 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 81 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3186865746974945 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 82 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4292396903038025 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 83 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 84 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27209946513175964 | 0.0 | 0.0 | +4367c039-e64e-4a3c-a49f-57cb2674a08f / -— |
| Jogador 7 | 2-3 | 85 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005156854167580605 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 87 | BUY | STABILIZE | 96.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31888172030448914 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 88 | BUY | STABILIZE | 96.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30614417791366577 | 0.0 | 0.0 | +22c1a0b0-5d27-406a-b3e1-9e0272a18947 / -— |
| Jogador 7 | 2-4 | 89 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009762140922248363 | 0.0 | 0.0 | +2acae3f1-fe55-41b3-9880-d7a2eed8edbb / -— |
| Jogador 7 | 2-4 | 90 | BUY_XP | STABILIZE | 96.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 91 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5673761963844299 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 93 | BUY | STABILIZE | 96.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13538555800914764 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 94 | SELL | STABILIZE | 96.0 | 5 | 5 | 0 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -3394d5fc-ee48-4a08-8669-05984c804b53 |
| Jogador 7 | 2-5 | 95 | EQUIP_FROM_INVENTORY | STABILIZE | 96.0 | 5 | 8 | 0 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11096227169036865 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 96 | EQUIP_FROM_INVENTORY | STABILIZE | 96.0 | 5 | 8 | 0 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13591322302818298 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 97 | BUY | STABILIZE | 96.0 | 5 | 8 | 0 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1158975139260292 | 0.0 | 0.0 | +1d709136-338f-4fef-90fc-b2aa1b83d879 / -— |
| Jogador 7 | 2-5 | 98 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 5 | 0 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 99 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 5 | 0 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29982027411460876 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 100 | PASS | STABILIZE | 96.0 | 5 | 5 | 0 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 102 | SELL | STABILIZE | 96.0 | 5 | 12 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-6 | 103 | BUY | STABILIZE | 96.0 | 5 | 15 | 1 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8952210545539856 | 0.0 | 0.0 | +a146f2d5-4da5-4c0e-bb09-de3177c72417 / -— |
| Jogador 7 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 13 | 1 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573597639799118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 105 | BUY_XP | STABILIZE | 96.0 | 5 | 13 | 1 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 106 | BUY_XP | STABILIZE | 96.0 | 5 | 9 | 0 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 5 | 0 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039173029363155365 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 108 | BUY_XP | STABILIZE | 96.0 | 5 | 5 | 0 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 109 | SELL | STABILIZE | 96.0 | 5 | 1 | 0 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011166666634380817 | 0.0 | 0.0 | +— / -242805ca-f275-4e04-a2f5-81e0b6680dd1 |
| Jogador 7 | 2-6 | 110 | SELL | STABILIZE | 96.0 | 5 | 2 | 0 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07269427180290222 | 0.0 | 0.0 | +— / -2acae3f1-fe55-41b3-9880-d7a2eed8edbb |
| Jogador 7 | 2-7 | 112 | BUY | STABILIZE | 96.0 | 5 | 10 | 1 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8235121369361877 | 0.0 | 0.0 | +536c157d-bb9f-4be0-9847-040530c052fd / -— |
| Jogador 7 | 2-7 | 113 | SELL | STABILIZE | 96.0 | 5 | 9 | 0 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03500000014901161 | 0.0 | 0.0 | +— / -1d709136-338f-4fef-90fc-b2aa1b83d879 |
| Jogador 7 | 2-7 | 114 | BUY | STABILIZE | 96.0 | 5 | 12 | 1 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015709348022937775 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 115 | BUY_XP | STABILIZE | 96.0 | 5 | 9 | 0 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 116 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 5 | 0 | 18.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43714839220046997 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 5 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 118 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 5 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 119 | PASS | STABILIZE | 96.0 | 6 | 5 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 122 | BUY | STABILIZE | 96.0 | 6 | 11 | 1 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7233226299285889 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 7 | 3-1 | 123 | BUY | STABILIZE | 96.0 | 6 | 8 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8378668427467346 | 0.0 | 0.0 | +c114a849-aa3b-4b7f-bc26-b5b699914f0b / -22c1a0b0-5d27-406a-b3e1-9e0272a18947,536c157d-bb9f-4be0-9847-040530c052fd |
| Jogador 7 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 96.0 | 6 | 7 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10031075030565262 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 7 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00016959365166258067 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 7 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01319409441202879 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 127 | PASS | STABILIZE | 96.0 | 6 | 7 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 132 | BUY | STABILIZE | 96.0 | 6 | 15 | 1 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879396677017212 | 0.0 | 0.0 | +8043a64c-a04d-4399-b52d-2246fe74e470 / -— |
| Jogador 7 | 3-2 | 133 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 14 | 1 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0017633989918977022 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 134 | BUY_XP | STABILIZE | 96.0 | 6 | 14 | 1 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 135 | BUY_XP | STABILIZE | 96.0 | 6 | 10 | 1 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 136 | BUY_XP | STABILIZE | 96.0 | 6 | 6 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 2 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0006940555758774281 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 2 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 139 | PASS | STABILIZE | 96.0 | 6 | 2 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 142 | BUY | STABILIZE | 96.0 | 6 | 11 | 1 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7237704992294312 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 143 | SELL | STABILIZE | 96.0 | 6 | 8 | 0 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -c114a849-aa3b-4b7f-bc26-b5b699914f0b |
| Jogador 7 | 3-3 | 144 | BUY | STABILIZE | 96.0 | 6 | 11 | 1 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8075520992279053 | 0.0 | 0.0 | +652ff984-c3ac-48d7-9fb6-e95aed0a047d / -— |
| Jogador 7 | 3-3 | 145 | SELL | STABILIZE | 96.0 | 6 | 10 | 1 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023386502638459206 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 7 | 3-3 | 146 | BUY | STABILIZE | 96.0 | 6 | 13 | 1 | 24.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8364349007606506 | 0.0 | 0.0 | +ac1c8000-a262-4fb1-9cfb-9ac071e5e10f / -bb7ed7a4-035a-4798-a9b2-44893057ab84,dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 7 | 3-3 | 147 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 12 | 1 | 20.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34801945090293884 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 148 | MOVE_BOARD | FAST8 | 96.0 | 6 | 12 | 1 | 26.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015526067465543747 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 149 | BUY_XP | FAST8 | 96.0 | 6 | 12 | 1 | 26.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 150 | BUY_XP | FAST8 | 96.0 | 6 | 8 | 0 | 26.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 152 | BUY | FAST8 | 85.0 | 6 | 9 | 0 | 26.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026317859068512917 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -— |
| Jogador 7 | 3-4 | 153 | BUY_XP | FAST8 | 85.0 | 6 | 6 | 0 | 26.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 154 | SELL | FAST8 | 85.0 | 6 | 2 | 0 | 26.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -ac1c8000-a262-4fb1-9cfb-9ac071e5e10f |
| Jogador 7 | 3-4 | 155 | BUY_XP | FAST8 | 85.0 | 6 | 5 | 0 | 26.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04650000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 156 | MOVE_BENCH | FAST8 | 85.0 | 7 | 1 | 0 | 26.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15597805380821228 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 157 | MOVE_BOARD | FAST8 | 85.0 | 7 | 1 | 0 | 32.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014933466911315918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 158 | MOVE_BOARD | FAST8 | 85.0 | 7 | 1 | 0 | 32.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 159 | PASS | FAST8 | 85.0 | 7 | 1 | 0 | 32.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 162 | BUY | FAST8 | 85.0 | 7 | 6 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7355091571807861 | 0.0 | 0.0 | +2074e6ec-81e7-41c9-be7e-a0d9310fbafa / -— |
| Jogador 7 | 3-5 | 163 | BUY | FAST8 | 85.0 | 7 | 4 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7298119068145752 | 0.0 | 0.0 | +7c8b3027-1434-4346-95b3-5463e8a4aa9b / -— |
| Jogador 7 | 3-5 | 164 | MOVE_BOARD | FAST8 | 85.0 | 7 | 2 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0002188041980843991 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 165 | MOVE_BOARD | FAST8 | 85.0 | 7 | 2 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015671953558921814 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 166 | PASS | FAST8 | 85.0 | 7 | 2 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 172 | BUY_XP | FAST8 | 85.0 | 7 | 8 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 173 | BUY_XP | FAST8 | 85.0 | 7 | 4 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 174 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007679456030018628 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 175 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 176 | PASS | FAST8 | 85.0 | 7 | 0 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 182 | BUY | FAST8 | 85.0 | 7 | 7 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.531018853187561 | 0.0 | 0.0 | +06fb62e5-6766-4156-bf7d-0da443a9b20c / -— |
| Jogador 7 | 3-7 | 183 | MOVE_BOARD | FAST8 | 85.0 | 7 | 4 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 184 | MOVE_BOARD | FAST8 | 85.0 | 7 | 4 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013596992939710617 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 185 | PASS | FAST8 | 85.0 | 7 | 4 | 0 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 85.0 | 7 | 10 | 1 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08704677224159241 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 85.0 | 7 | 10 | 1 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08361823856830597 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 194 | SELL | FAST8 | 85.0 | 7 | 10 | 1 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47284674644470215 | 0.0 | 0.0 | +— / -06fb62e5-6766-4156-bf7d-0da443a9b20c |
| Jogador 7 | 4-1 | 195 | BUY | FAST8 | 85.0 | 7 | 13 | 1 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7374922633171082 | 0.0 | 0.0 | +626c50be-ec88-444f-84bb-9b8d41100085 / -— |
| Jogador 7 | 4-1 | 196 | SELL | FAST8 | 85.0 | 7 | 12 | 1 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6006666421890259 | 0.0 | 0.0 | +— / -7c8b3027-1434-4346-95b3-5463e8a4aa9b |
| Jogador 7 | 4-1 | 197 | BUY | FAST8 | 85.0 | 7 | 14 | 1 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7677999138832092 | 0.0 | 0.0 | +ddf39480-6ce0-46d0-ac45-57114245ffba / -626c50be-ec88-444f-84bb-9b8d41100085,8043a64c-a04d-4399-b52d-2246fe74e470 |
| Jogador 7 | 4-1 | 198 | MOVE_BOARD | FAST8 | 85.0 | 7 | 13 | 1 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 199 | MOVE_BOARD | FAST8 | 85.0 | 7 | 13 | 1 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014631533063948154 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 200 | PASS | FAST8 | 85.0 | 7 | 13 | 1 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 202 | MOVE_BOARD | FAST8 | 85.0 | 7 | 21 | 2 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00016705023881513625 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 203 | MOVE_BOARD | FAST8 | 85.0 | 7 | 21 | 2 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 204 | MOVE_BOARD | FAST8 | 85.0 | 7 | 21 | 2 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015057390555739403 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 205 | PASS | FAST8 | 85.0 | 7 | 21 | 2 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10928571224212646 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 212 | BUY | FAST8 | 85.0 | 7 | 30 | 3 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.745800256729126 | 0.0 | 0.0 | +a9588010-57fa-4baf-b226-a30f519342e7 / -2074e6ec-81e7-41c9-be7e-a0d9310fbafa,42f4384d-5499-4441-aa3b-d37e50926071 |
| Jogador 7 | 4-3 | 213 | BUY | FAST8 | 85.0 | 7 | 28 | 2 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7605240941047668 | 0.0 | 0.0 | +840740a6-45be-4107-a4b7-b10cefe1a667 / -— |
| Jogador 7 | 4-3 | 214 | MOVE_BOARD | FAST8 | 85.0 | 7 | 26 | 2 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0001646640885155648 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 215 | MOVE_BOARD | FAST8 | 85.0 | 7 | 26 | 2 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 216 | PASS | FAST8 | 85.0 | 7 | 26 | 2 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1128571406006813 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 222 | BUY | FAST8 | 85.0 | 7 | 36 | 3 | 34.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8236847519874573 | 0.0 | 0.0 | +b26a039f-581c-4de2-8a75-f7e8a4ef0e4a / -0cf5c315-d2f3-4854-a95b-07912b83ea81,f116ca4e-dbe8-457e-83a5-958525aa384a |
| Jogador 7 | 4-4 | 223 | MOVE_BENCH | FAST8 | 85.0 | 7 | 33 | 3 | 28.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5955842137336731 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 224 | MOVE_BOARD | FAST8 | 85.0 | 7 | 33 | 3 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020158927887678146 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 225 | MOVE_BOARD | FAST8 | 85.0 | 7 | 33 | 3 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010300295427441597 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 226 | PASS | FAST8 | 85.0 | 7 | 33 | 3 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1778571456670761 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 232 | BUY | FAST8 | 85.0 | 7 | 43 | 4 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1699230670928955 | 0.0 | 0.0 | +a72137b3-498b-40e1-938a-639f56745f08 / -— |
| Jogador 7 | 4-5 | 233 | MOVE_BOARD | FAST8 | 85.0 | 7 | 39 | 3 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 234 | MOVE_BOARD | FAST8 | 85.0 | 7 | 39 | 3 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 235 | PASS | FAST8 | 85.0 | 7 | 39 | 3 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18214285373687744 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 242 | BUY | FAST8 | 85.0 | 7 | 52 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6695534586906433 | 0.0 | 0.0 | +241a8a03-6e6f-4a9a-8550-e9154f3e1e76 / -— |
| Jogador 7 | 4-6 | 243 | MOVE_BOARD | FAST8 | 85.0 | 7 | 49 | 4 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.000519186956807971 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 244 | MOVE_BOARD | FAST8 | 85.0 | 7 | 49 | 4 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 245 | MOVE_BOARD | FAST8 | 85.0 | 7 | 49 | 4 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01465074997395277 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 246 | PASS | FAST8 | 85.0 | 7 | 49 | 4 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18928571045398712 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 252 | BUY | FAST8 | 85.0 | 7 | 63 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31549882888793945 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 7 | 4-7 | 253 | MOVE_BOARD | FAST8 | 85.0 | 7 | 60 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.9091325965709984e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 254 | MOVE_BOARD | FAST8 | 85.0 | 7 | 60 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014883494935929775 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 255 | MOVE_BOARD | FAST8 | 85.0 | 7 | 60 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 256 | PASS | FAST8 | 85.0 | 7 | 60 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08595746010541916 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 85.0 | 7 | 73 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09456901997327805 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 85.0 | 7 | 73 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11107267439365387 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 264 | MOVE_BENCH | FAST8 | 85.0 | 7 | 73 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3996431529521942 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 265 | MOVE_BENCH | FAST8 | 85.0 | 7 | 73 | 5 | 42.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3946937620639801 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 266 | PASS | FAST8 | 85.0 | 7 | 73 | 5 | 36.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10438153147697449 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 272 | MOVE_BENCH | FAST8 | 70.0 | 7 | 83 | 5 | 36.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09852093458175659 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 273 | MOVE_BENCH | FAST8 | 70.0 | 7 | 83 | 5 | 32.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4140509366989136 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 274 | MOVE_BENCH | FAST8 | 70.0 | 7 | 83 | 5 | 34.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3803262412548065 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 275 | PASS | FAST8 | 70.0 | 7 | 83 | 5 | 36.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11236796528100967 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 282 | SELL | FAST8 | 70.0 | 7 | 94 | 5 | 36.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -ddf39480-6ce0-46d0-ac45-57114245ffba |
| Jogador 7 | 5-3 | 283 | BUY | FAST8 | 70.0 | 7 | 97 | 5 | 36.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.951371431350708 | 0.0 | 0.0 | +45b96060-6eda-4d0b-9012-e80db31b71d2 / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef,a146f2d5-4da5-4c0e-bb09-de3177c72417 |
| Jogador 7 | 5-3 | 284 | BUY | FAST8 | 70.0 | 7 | 95 | 5 | 32.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9428043365478516 | 0.0 | 0.0 | +b6883c6a-7149-4088-8506-20bd8dfed6a5 / -241a8a03-6e6f-4a9a-8550-e9154f3e1e76,cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 5-3 | 285 | MOVE_BENCH | FAST8 | 70.0 | 7 | 92 | 5 | 26.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2646361291408539 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 286 | MOVE_BENCH | FAST8 | 70.0 | 7 | 92 | 5 | 34.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5614974498748779 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 287 | MOVE_BOARD | FAST8 | 70.0 | 7 | 92 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015001237392425537 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 288 | BUY | FAST8 | 70.0 | 7 | 92 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3839718997478485 | 0.0 | 0.0 | +22f3c707-2635-41cb-a228-10d5ed1883b3 / -— |
| Jogador 7 | 5-3 | 289 | MOVE_BOARD | FAST8 | 70.0 | 7 | 90 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 290 | MOVE_BOARD | FAST8 | 70.0 | 7 | 90 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 292 | BUY | FAST8 | 55.0 | 7 | 100 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2946010231971741 | 0.0 | 0.0 | +64d87de4-68df-4a72-8b8d-f78039ae4ce5 / -— |
| Jogador 7 | 5-4 | 293 | MOVE_BOARD | FAST8 | 55.0 | 7 | 97 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.6347786842961796e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 294 | MOVE_BENCH | FAST8 | 55.0 | 7 | 97 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7718043327331543 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 295 | PASS | FAST8 | 55.0 | 7 | 97 | 5 | 44.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27795520424842834 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 302 | BUY | FAST8 | 55.0 | 7 | 107 | 5 | 44.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8148573040962219 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -— |
| Jogador 7 | 5-5 | 303 | SELL | FAST8 | 55.0 | 7 | 104 | 5 | 44.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5780666470527649 | 0.0 | 0.0 | +— / -b6883c6a-7149-4088-8506-20bd8dfed6a5 |
| Jogador 7 | 5-5 | 304 | BUY | FAST8 | 55.0 | 7 | 112 | 5 | 44.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3653709590435028 | 0.0 | 0.0 | +91eb044c-6989-4b6a-a9fa-a59f75b56743 / -— |
| Jogador 7 | 5-5 | 305 | MOVE_BENCH | FAST8 | 55.0 | 7 | 110 | 5 | 44.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35709086060523987 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 306 | MOVE_BENCH | FAST8 | 55.0 | 7 | 110 | 5 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0677117258310318 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 307 | MOVE_BENCH | FAST8 | 55.0 | 7 | 110 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7694018483161926 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 308 | MOVE_BENCH | FAST8 | 55.0 | 7 | 110 | 5 | 44.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37035641074180603 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 309 | PASS | FAST8 | 55.0 | 7 | 110 | 5 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13503490388393402 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 312 | SELL | FAST8 | 55.0 | 7 | 121 | 5 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -a9588010-57fa-4baf-b226-a30f519342e7 |
| Jogador 7 | 5-6 | 313 | BUY | FAST8 | 55.0 | 7 | 126 | 5 | 38.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8628209829330444 | 0.0 | 0.0 | +08731924-b808-4070-8c85-2c747847d835 / -— |
| Jogador 7 | 5-6 | 314 | MOVE_BENCH | FAST8 | 55.0 | 7 | 124 | 5 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07942311465740204 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 315 | MOVE_BENCH | FAST8 | 55.0 | 7 | 124 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7694334387779236 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 316 | MOVE_BENCH | FAST8 | 55.0 | 7 | 124 | 5 | 44.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36885589361190796 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 317 | PASS | FAST8 | 55.0 | 7 | 124 | 5 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14723914861679077 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 322 | MOVE_BENCH | FAST8 | 55.0 | 7 | 136 | 5 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08137870579957962 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 323 | MOVE_BENCH | FAST8 | 55.0 | 7 | 136 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7695101499557495 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 324 | MOVE_BENCH | FAST8 | 55.0 | 7 | 136 | 5 | 44.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07205242663621902 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 325 | MOVE_BENCH | FAST8 | 55.0 | 7 | 136 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41691896319389343 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 326 | MOVE_BENCH | FAST8 | 55.0 | 7 | 136 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055816419422626495 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 327 | MOVE_BENCH | FAST8 | 55.0 | 7 | 136 | 5 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38648104667663574 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 328 | MOVE_BENCH | FAST8 | 55.0 | 7 | 136 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06609582901000977 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 329 | MOVE_BENCH | FAST8 | 55.0 | 7 | 136 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06355612725019455 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 330 | MOVE_BENCH | FAST8 | 55.0 | 7 | 136 | 5 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38725733757019043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 332 | EQUIP_FROM_INVENTORY | FAST8 | 55.0 | 7 | 147 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0879456177353859 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 333 | MOVE_BENCH | FAST8 | 55.0 | 7 | 147 | 5 | 40.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7545769810676575 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 334 | MOVE_BENCH | FAST8 | 55.0 | 7 | 147 | 5 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08729966729879379 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 335 | MOVE_BENCH | FAST8 | 55.0 | 7 | 147 | 5 | 38.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3523010313510895 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 336 | SELL | FAST8 | 55.0 | 7 | 147 | 5 | 44.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 7 | 6-1 | 337 | BUY | FAST8 | 55.0 | 7 | 150 | 5 | 44.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8802217841148376 | 0.0 | 0.0 | +bfe7ca8a-6e89-4673-b142-262e012398a9 / -— |
| Jogador 7 | 6-1 | 338 | MOVE_BENCH | FAST8 | 55.0 | 7 | 146 | 5 | 44.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08692818135023117 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 339 | BUY_XP | FAST8 | 55.0 | 7 | 146 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05761599913239479 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 340 | BUY_XP | FAST8 | 55.0 | 7 | 142 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05761599913239479 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 342 | SELL | WINSTREAK | 55.0 | 8 | 150 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5739333629608154 | 0.0 | 0.0 | +— / -840740a6-45be-4107-a4b7-b10cefe1a667 |
| Jogador 7 | 6-2 | 343 | BUY | WINSTREAK | 55.0 | 8 | 152 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9350322484970093 | 0.0 | 0.0 | +e29db20a-6b71-4518-ac7d-1e5d9eb67582 / -— |
| Jogador 7 | 6-2 | 344 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 150 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.408705472946167 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 345 | BUY | WINSTREAK | 55.0 | 8 | 150 | 5 | 52.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08948508650064468 | 0.0 | 0.0 | +5d95f8bc-0c01-4c67-8764-4410eb32ee93 / -— |
| Jogador 7 | 6-2 | 346 | MOVE_BOARD | WINSTREAK | 55.0 | 8 | 147 | 5 | 52.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.199805723852478e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 347 | MOVE_BOARD | WINSTREAK | 55.0 | 8 | 147 | 5 | 52.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 348 | MOVE_BOARD | WINSTREAK | 55.0 | 8 | 147 | 5 | 52.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 349 | PASS | WINSTREAK | 55.0 | 8 | 147 | 5 | 52.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1830344945192337 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 352 | SELL | WINSTREAK | 55.0 | 8 | 159 | 5 | 52.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -5d95f8bc-0c01-4c67-8764-4410eb32ee93 |
| Jogador 7 | 6-3 | 353 | BUY | WINSTREAK | 55.0 | 8 | 162 | 5 | 52.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4526773989200592 | 0.0 | 0.0 | +5184a53b-fca3-448c-b5ab-7daa37b0c259 / -— |
| Jogador 7 | 6-3 | 354 | SELL | WINSTREAK | 55.0 | 8 | 159 | 5 | 52.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09427204728126526 | 0.0 | 0.0 | +— / -4367c039-e64e-4a3c-a49f-57cb2674a08f |
| Jogador 7 | 6-3 | 355 | BUY | WINSTREAK | 55.0 | 8 | 161 | 5 | 52.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8721958994865417 | 0.0 | 0.0 | +c71adf7d-8d74-439d-8863-dac0f4f20cd1 / -5184a53b-fca3-448c-b5ab-7daa37b0c259,584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 6-3 | 356 | EQUIP_FROM_INVENTORY | WINSTREAK | 55.0 | 8 | 158 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0877438560128212 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 357 | BUY | WINSTREAK | 55.0 | 8 | 158 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11010951548814774 | 0.0 | 0.0 | +f1ece814-0986-421f-b5df-0b457ebaa484 / -— |
| Jogador 7 | 6-3 | 358 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 154 | 5 | 46.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.088264599442482 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 359 | MOVE_BOARD | WINSTREAK | 55.0 | 8 | 154 | 5 | 50.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015032238326966763 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 360 | PASS | WINSTREAK | 55.0 | 8 | 154 | 5 | 50.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1899678260087967 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 362 | BUY | WINSTREAK | 55.0 | 8 | 165 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3761143982410431 | 0.0 | 0.0 | +13169f05-0cd0-4012-89a6-7b47246b475e / -— |
| Jogador 7 | 6-4 | 363 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 163 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6466138958930969 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 364 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 163 | 5 | 50.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05653998255729675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 365 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 163 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08480025827884674 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 366 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 163 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6615985035896301 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 367 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 163 | 5 | 50.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04838426411151886 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 368 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 163 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.046275947242975235 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 369 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 163 | 5 | 58.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7234856486320496 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 370 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 163 | 5 | 50.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09997184574604034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 372 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 174 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3989729583263397 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 373 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 174 | 5 | 58.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7439183592796326 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 374 | PASS | WINSTREAK | 55.0 | 8 | 174 | 5 | 50.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21002665162086487 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 382 | MOVE_BENCH | STABILIZE | 36.0 | 8 | 184 | 5 | 50.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09994329512119293 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 383 | MOVE_BENCH | STABILIZE | 36.0 | 8 | 184 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4146876633167267 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 384 | MOVE_BENCH | STABILIZE | 36.0 | 8 | 184 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6969578266143799 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 385 | PASS | STABILIZE | 36.0 | 8 | 184 | 5 | 50.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2561817467212677 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-7 | 392 | MOVE_BENCH | ALL_IN | 17.0 | 8 | 195 | 5 | 50.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08446167409420013 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-7 | 393 | MOVE_BENCH | ALL_IN | 17.0 | 8 | 195 | 5 | 58.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5330577492713928 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-7 | 394 | SELL | ALL_IN | 17.0 | 8 | 195 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6988999843597412 | 0.0 | 0.0 | +— / -45b96060-6eda-4d0b-9012-e80db31b71d2 |
| Jogador 7 | 6-7 | 395 | BUY | ALL_IN | 17.0 | 8 | 200 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.23364342749118805 | 0.0 | 0.0 | +df0a5d1f-d42d-43eb-b505-cfd00e3dcea8 / -— |
| Jogador 7 | 6-7 | 396 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 8 | 197 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06775031983852386 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-7 | 397 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 8 | 197 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06794045865535736 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-7 | 398 | MOVE_BENCH | ALL_IN | 17.0 | 8 | 197 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6325004696846008 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-7 | 399 | MOVE_BENCH | ALL_IN | 17.0 | 8 | 197 | 5 | 56.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7597190141677856 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-7 | 400 | PASS | ALL_IN | 17.0 | 8 | 197 | 5 | 48.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6528298258781433 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 402 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 8 | 208 | 5 | 48.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08734419196844101 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 403 | MOVE_BENCH | ALL_IN | 17.0 | 8 | 208 | 5 | 48.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09910057485103607 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 404 | MOVE_BENCH | ALL_IN | 17.0 | 8 | 208 | 5 | 54.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6466184258460999 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 405 | MOVE_BENCH | ALL_IN | 17.0 | 8 | 208 | 5 | 56.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7558333277702332 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 406 | PASS | ALL_IN | 17.0 | 8 | 208 | 5 | 48.0 | Sabugueiro/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8199999928474426 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5923603177070618 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01241401955485344 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15755267441272736 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28994128108024597 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 34 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4052838385105133 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 46 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9338529109954834 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -— |
| Jogador 8 | 1-4 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0015356456860899925 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30273380875587463 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24634358286857605 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23690515756607056 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 51 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9878858923912048 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015884392196312547 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 53 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012339143082499504 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 54 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0267044305801392 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0916093587875366 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -64f24363-3325-4538-972e-a6d8260b3787,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.44034039974212646 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 62 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2667955458164215 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -— |
| Jogador 8 | 2-1 | 63 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14427603781223297 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 64 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13658009469509125 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 65 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15069587528705597 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016819367185235023 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005078555084764957 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 68 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 70 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2685607969760895 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 71 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1971120536327362 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 72 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 73 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21301157772541046 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-2 | 74 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07456666976213455 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-2 | 75 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0872073769569397 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 76 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 77 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 79 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.980607807636261 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 80 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9128124117851257 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 81 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.236699178814888 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 82 | SELL | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07833333313465118 | 0.0 | 0.0 | +— / -a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 8 | 2-3 | 83 | SELL | STABILIZE | 96.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04543333500623703 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 2-3 | 84 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2617338299751282 | 0.0 | 0.0 | +01f4a73c-7202-4ee3-964e-d32370c3c547 / -— |
| Jogador 8 | 2-3 | 85 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003927753306925297 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 87 | BUY | STABILIZE | 96.0 | 5 | 10 | 1 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09320086240768433 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 88 | BUY | STABILIZE | 96.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12690599262714386 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 89 | BUY | STABILIZE | 96.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04345778748393059 | 0.0 | 0.0 | +fb186a97-59a4-4b3a-be2f-dadd2670dc95 / -— |
| Jogador 8 | 2-4 | 90 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Leona | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40128812193870544 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 91 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021668417379260063 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 93 | BUY | STABILIZE | 96.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8475176692008972 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 94 | SELL | STABILIZE | 96.0 | 5 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011366666294634342 | 0.0 | 0.0 | +— / -fb186a97-59a4-4b3a-be2f-dadd2670dc95 |
| Jogador 8 | 2-5 | 95 | BUY | STABILIZE | 96.0 | 5 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9497045278549194 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -5de56114-806a-4f58-8241-b3b8434a2154,76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc |
| Jogador 8 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012111124582588673 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 97 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 98 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014983674511313438 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 99 | PASS | STABILIZE | 96.0 | 5 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 102 | BUY | STABILIZE | 91.0 | 5 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.90105801820755 | 0.0 | 0.0 | +c737e99a-613e-4f1a-a50e-7a865169f90c / -— |
| Jogador 8 | 2-6 | 103 | BUY | STABILIZE | 91.0 | 5 | 10 | 1 | 16.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03651125729084015 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 104 | SELL | STABILIZE | 91.0 | 5 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 2-6 | 105 | BUY | STABILIZE | 91.0 | 5 | 10 | 1 | 16.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042720992118120193 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.302549395011738e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016560638323426247 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 109 | PASS | STABILIZE | 91.0 | 5 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 112 | SELL | STABILIZE | 91.0 | 5 | 13 | 1 | 16.0 | Enfeitiçador/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04611464589834213 | 0.0 | 0.0 | +— / -01f4a73c-7202-4ee3-964e-d32370c3c547 |
| Jogador 8 | 2-7 | 113 | BUY | STABILIZE | 91.0 | 5 | 14 | 1 | 16.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8311870694160461 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 114 | SELL | STABILIZE | 91.0 | 5 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0030333332251757383 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 2-7 | 115 | BUY | STABILIZE | 91.0 | 5 | 14 | 1 | 16.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04435349628329277 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 116 | SELL | STABILIZE | 91.0 | 5 | 11 | 1 | 16.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02671940065920353 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-7 | 117 | BUY | STABILIZE | 91.0 | 5 | 14 | 1 | 16.0 | Colosso/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13371601700782776 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 118 | SELL | STABILIZE | 91.0 | 5 | 13 | 1 | 16.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5143116116523743 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 2-7 | 119 | BUY | STABILIZE | 91.0 | 5 | 15 | 1 | 16.0 | Colosso/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07629165053367615 | 0.0 | 0.0 | +d731d71e-fc91-41ae-ab3f-75966dd2c428 / -— |
| Jogador 8 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 14 | 1 | 16.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013730754144489765 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 91.0 | 5 | 20 | 2 | 16.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2646680474281311 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 123 | SELL | STABILIZE | 91.0 | 5 | 20 | 2 | 16.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02200241945683956 | 0.0 | 0.0 | +— / -35e1a0f6-207d-4df2-b096-fc07962d094a |
| Jogador 8 | 3-1 | 124 | BUY | STABILIZE | 91.0 | 5 | 22 | 2 | 16.0 | Colosso/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2893276810646057 | 0.0 | 0.0 | +a5c0595b-85f9-4c71-a156-675d22a7b3c2 / -— |
| Jogador 8 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 20 | 2 | 16.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4129360020160675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 126 | SELL | STABILIZE | 91.0 | 5 | 20 | 2 | 14.0 | Colosso/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3710888922214508 | 0.0 | 0.0 | +— / -630d9254-3856-4d88-b981-43a8270b4b3d |
| Jogador 8 | 3-1 | 127 | BUY | STABILIZE | 91.0 | 5 | 23 | 2 | 14.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050071295350790024 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 128 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 19 | 1 | 14.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3749659061431885 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 129 | BUY_XP | STABILIZE | 91.0 | 5 | 19 | 1 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 130 | BUY_XP | STABILIZE | 91.0 | 5 | 15 | 1 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 132 | SELL | STABILIZE | 81.0 | 5 | 17 | 1 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014633333310484886 | 0.0 | 0.0 | +— / -d731d71e-fc91-41ae-ab3f-75966dd2c428 |
| Jogador 8 | 3-2 | 133 | BUY | STABILIZE | 81.0 | 5 | 18 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7885512709617615 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 134 | SELL | STABILIZE | 81.0 | 5 | 17 | 1 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5294222235679626 | 0.0 | 0.0 | +— / -a5c0595b-85f9-4c71-a156-675d22a7b3c2 |
| Jogador 8 | 3-2 | 135 | BUY | STABILIZE | 81.0 | 5 | 19 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2827063798904419 | 0.0 | 0.0 | +5326031a-1b7e-4dbd-b58b-1e81029d42a1 / -— |
| Jogador 8 | 3-2 | 136 | SELL | STABILIZE | 81.0 | 5 | 17 | 1 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5294222235679626 | 0.0 | 0.0 | +— / -5326031a-1b7e-4dbd-b58b-1e81029d42a1 |
| Jogador 8 | 3-2 | 137 | BUY | STABILIZE | 81.0 | 5 | 19 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06201862916350365 | 0.0 | 0.0 | +ece93d63-49d6-472c-9a10-7ece135feacc / -— |
| Jogador 8 | 3-2 | 138 | BUY_XP | STABILIZE | 81.0 | 5 | 17 | 1 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07806999981403351 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 139 | BUY_XP | STABILIZE | 81.0 | 6 | 13 | 1 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 140 | BUY_XP | STABILIZE | 81.0 | 6 | 9 | 0 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 142 | SELL | STABILIZE | 69.0 | 6 | 11 | 1 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3120444416999817 | 0.0 | 0.0 | +— / -ece93d63-49d6-472c-9a10-7ece135feacc |
| Jogador 8 | 3-3 | 143 | BUY | STABILIZE | 69.0 | 6 | 13 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8302161693572998 | 0.0 | 0.0 | +3bf8af53-85e7-4e5b-8cf8-b7198a955e8d / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c,f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 3-3 | 144 | BUY | STABILIZE | 69.0 | 6 | 12 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33522236347198486 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 145 | BUY_XP | STABILIZE | 69.0 | 6 | 9 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 146 | BUY_XP | STABILIZE | 69.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 147 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08142875134944916 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 148 | MOVE_BOARD | FAST8 | 69.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 149 | PASS | FAST8 | 69.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 152 | BUY | FAST8 | 69.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19748598337173462 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 153 | BUY | FAST8 | 69.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01529897190630436 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 154 | MOVE_BOARD | FAST8 | 69.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 155 | MOVE_BOARD | FAST8 | 69.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 156 | PASS | FAST8 | 69.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 162 | SELL | FAST8 | 69.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -3bf8af53-85e7-4e5b-8cf8-b7198a955e8d |
| Jogador 8 | 3-5 | 163 | BUY | FAST8 | 69.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6521663665771484 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 8 | 3-5 | 164 | BUY_XP | FAST8 | 69.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 165 | MOVE_BOARD | FAST8 | 69.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.711074143415317e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 166 | MOVE_BOARD | FAST8 | 69.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499991025775671 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 167 | MOVE_BOARD | FAST8 | 69.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 168 | PASS | FAST8 | 69.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 172 | SELL | FAST8 | 59.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06916666775941849 | 0.0 | 0.0 | +— / -82e109f9-54c8-492d-93e5-7e0dd0034b15 |
| Jogador 8 | 3-6 | 173 | BUY | FAST8 | 59.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10865087807178497 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 174 | MOVE_BOARD | FAST8 | 59.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -6.425197511816805e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 175 | BUY_XP | FAST8 | 59.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 176 | BUY_XP | FAST8 | 59.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07959999889135361 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 177 | MOVE_BENCH | FAST8 | 59.0 | 7 | 0 | 0 | 26.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059838175773620605 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 178 | MOVE_BOARD | FAST8 | 59.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 179 | PASS | FAST8 | 59.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 182 | BUY | FAST8 | 59.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14998766779899597 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 183 | MOVE_BOARD | FAST8 | 59.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 184 | MOVE_BOARD | FAST8 | 59.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 185 | PASS | FAST8 | 59.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 59.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17018930613994598 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 59.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10527077317237854 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 194 | SELL | FAST8 | 59.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.033248420804739 | 0.0 | 0.0 | +— / -849ea0fc-7f61-4907-8abb-b25c8cc82efc |
| Jogador 8 | 4-1 | 195 | BUY | FAST8 | 59.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6478361487388611 | 0.0 | 0.0 | +2c153083-6c43-425e-90d5-23f7f2058592 / -— |
| Jogador 8 | 4-1 | 196 | MOVE_BOARD | FAST8 | 59.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 197 | MOVE_BOARD | FAST8 | 59.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014719256199896336 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 198 | PASS | FAST8 | 59.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 202 | SELL | FAST8 | 59.0 | 7 | 15 | 1 | 30.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06716666370630264 | 0.0 | 0.0 | +— / -23366968-ed3f-43d0-9f24-bb7691bf5d45 |
| Jogador 8 | 4-2 | 203 | BUY | FAST8 | 59.0 | 7 | 18 | 1 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7636836171150208 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -87600495-fe90-4832-ab42-9a5cb0ebe3f4,d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 4-2 | 204 | MOVE_BOARD | FAST8 | 59.0 | 7 | 15 | 1 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 205 | MOVE_BOARD | FAST8 | 59.0 | 7 | 15 | 1 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014956778846681118 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 206 | PASS | FAST8 | 59.0 | 7 | 15 | 1 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10499999672174454 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 212 | BUY | FAST8 | 47.0 | 7 | 21 | 2 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7127707600593567 | 0.0 | 0.0 | +c7841e00-91da-410b-b00f-62f4bf32f666 / -2c153083-6c43-425e-90d5-23f7f2058592,6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 4-3 | 213 | BUY | FAST8 | 47.0 | 7 | 18 | 1 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10144674777984619 | 0.0 | 0.0 | +485dab1f-b3a1-4170-8ed6-c0035072ae9b / -— |
| Jogador 8 | 4-3 | 214 | BUY | FAST8 | 47.0 | 7 | 14 | 1 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.082110695540905 | 0.0 | 0.0 | +17d5d3f2-999d-4788-852b-bda84adb4350 / -— |
| Jogador 8 | 4-3 | 215 | BUY_XP | FAST8 | 47.0 | 7 | 12 | 1 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 216 | BUY_XP | FAST8 | 47.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 217 | BUY_XP | FAST8 | 47.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 218 | MOVE_BOARD | FAST8 | 47.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.3330760137178e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 219 | MOVE_BOARD | FAST8 | 47.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 220 | PASS | FAST8 | 47.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 222 | BUY | FAST8 | 47.0 | 7 | 5 | 0 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3415915369987488 | 0.0 | 0.0 | +677ea844-e1bf-4c68-a0b0-136abb86ba7b / -— |
| Jogador 8 | 4-4 | 223 | SELL | FAST8 | 47.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -c7841e00-91da-410b-b00f-62f4bf32f666 |
| Jogador 8 | 4-4 | 224 | BUY | FAST8 | 47.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5438390374183655 | 0.0 | 0.0 | +5b6dec85-6970-4575-b364-21c3123995a5 / -17d5d3f2-999d-4788-852b-bda84adb4350,677ea844-e1bf-4c68-a0b0-136abb86ba7b |
| Jogador 8 | 4-4 | 225 | MOVE_BOARD | FAST8 | 47.0 | 7 | 9 | 0 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 226 | MOVE_BOARD | FAST8 | 47.0 | 7 | 9 | 0 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 227 | PASS | FAST8 | 47.0 | 7 | 9 | 0 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 232 | BUY | FAST8 | 47.0 | 7 | 14 | 1 | 30.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7679963707923889 | 0.0 | 0.0 | +31ea6d79-501d-4f2a-821d-7058334be82f / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,c737e99a-613e-4f1a-a50e-7a865169f90c |
| Jogador 8 | 4-5 | 233 | BUY | FAST8 | 47.0 | 7 | 13 | 1 | 28.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21395163238048553 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -— |
| Jogador 8 | 4-5 | 234 | MOVE_BENCH | FAST8 | 47.0 | 7 | 10 | 1 | 28.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.441196084022522 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 235 | BUY | FAST8 | 47.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07148955017328262 | 0.0 | 0.0 | +d6a00f0c-4823-44d6-b326-67595876998d / -— |
| Jogador 8 | 4-5 | 236 | MOVE_BOARD | FAST8 | 47.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005442943423986435 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 237 | MOVE_BOARD | FAST8 | 47.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015058519318699837 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 238 | MOVE_BOARD | FAST8 | 47.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 239 | PASS | FAST8 | 47.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 242 | BUY | STABILIZE | 35.0 | 7 | 13 | 1 | 36.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7970864176750183 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 8 | 4-6 | 243 | SELL | STABILIZE | 35.0 | 7 | 11 | 1 | 36.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -31ea6d79-501d-4f2a-821d-7058334be82f |
| Jogador 8 | 4-6 | 244 | BUY | STABILIZE | 35.0 | 7 | 14 | 1 | 36.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8322140574455261 | 0.0 | 0.0 | +3bfc4626-3226-44b6-a401-ff9c18761448 / -6fb9f857-4ee1-4b52-8825-57f514dc2d0f,d5848998-33f3-4632-94c0-60388a7cc6b8 |
| Jogador 8 | 4-6 | 245 | BUY | STABILIZE | 35.0 | 7 | 12 | 1 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.18134349584579468 | 0.0 | 0.0 | +20821a31-3317-4f82-bbb2-b70cdebdd893 / -— |
| Jogador 8 | 4-6 | 246 | EQUIP_FROM_INVENTORY | STABILIZE | 35.0 | 7 | 9 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13426391780376434 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 247 | BUY_XP | STABILIZE | 35.0 | 7 | 9 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 248 | BUY_XP | STABILIZE | 35.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 249 | MOVE_BENCH | STABILIZE | 35.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36555561423301697 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 250 | MOVE_BOARD | STABILIZE | 35.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014995524659752846 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 252 | MOVE_BENCH | ALL_IN | 21.0 | 7 | 7 | 0 | 40.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4006587266921997 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 253 | MOVE_BENCH | ALL_IN | 21.0 | 7 | 7 | 0 | 44.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5554198622703552 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 254 | PASS | ALL_IN | 21.0 | 7 | 7 | 0 | 44.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3199999928474426 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 262 | BUY | ALL_IN | 21.0 | 7 | 13 | 1 | 44.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8676614761352539 | 0.0 | 0.0 | +952ea2b4-387d-455d-b1ad-fb0de8c46e47 / -57903c42-49ca-43e1-8f86-42429c189fb5,bd4236f8-c8ff-4536-934a-b12b71012724 |
| Jogador 8 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 21.0 | 7 | 10 | 1 | 44.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1665484607219696 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 264 | CRAFT_AND_EQUIP | ALL_IN | 21.0 | 7 | 10 | 1 | 44.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1663045585155487 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 265 | MOVE_BENCH | ALL_IN | 21.0 | 7 | 10 | 1 | 44.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09818410873413086 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 266 | MOVE_BENCH | ALL_IN | 21.0 | 7 | 10 | 1 | 40.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02057531289756298 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 267 | MOVE_BENCH | ALL_IN | 21.0 | 7 | 10 | 1 | 38.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4133201241493225 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 268 | PASS | ALL_IN | 21.0 | 7 | 10 | 1 | 44.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3199999928474426 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 272 | MOVE_BENCH | ALL_IN | 5.0 | 7 | 17 | 1 | 44.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09165200591087341 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 273 | MOVE_BENCH | ALL_IN | 5.0 | 7 | 17 | 1 | 40.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028152426704764366 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 274 | MOVE_BENCH | ALL_IN | 5.0 | 7 | 17 | 1 | 38.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41012969613075256 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 275 | PASS | ALL_IN | 5.0 | 7 | 17 | 1 | 44.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4553232789039612 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 235 | 147 | 70 | 4 | 6 | 0 | 6 | 0 | 214 | 36.0 |
- Jogador 1 — gasto por ação: BUY: 119g, BUY_XP: 28g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 5g, stage 2: 27g, stage 3: 34g, stage 4: 30g, stage 5: 38g, stage 6: 13g
| Jogador 2 | 205 | 188 | 63 | 7 | 12 | 1 | 4 | 0 | 110 | 46.0 |
- Jogador 2 — gasto por ação: BUY: 124g, BUY_XP: 56g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 8g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 5g, stage 2: 46g, stage 3: 39g, stage 4: 35g, stage 5: 53g, stage 6: 10g
| Jogador 3 | 176 | 81 | 42 | 3 | 0 | 0 | 0 | 0 | 227 | 30.0 |
- Jogador 3 — gasto por ação: BUY: 77g, BUY_XP: 4g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 4g, stage 2: 22g, stage 3: 16g, stage 4: 28g, stage 5: 11g
| Jogador 4 | 108 | 44 | 12 | 5 | 0 | 0 | 0 | 0 | 113 | 28.0 |
- Jogador 4 — gasto por ação: BUY: 40g, BUY_XP: 4g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 4g, stage 2: 18g, stage 3: 18g, stage 4: 4g
| Jogador 5 | 287 | 245 | 122 | 3 | 10 | 1 | 12 | 0 | 231 | 44.0 |
- Jogador 5 — gasto por ação: BUY: 177g, BUY_XP: 44g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 24g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 35g, stage 3: 54g, stage 4: 44g, stage 5: 27g, stage 6: 74g, stage 7: 4g
| Jogador 6 | 135 | 88 | 35 | 4 | 2 | 0 | 2 | 0 | 119 | 34.0 |
- Jogador 6 — gasto por ação: BUY: 76g, BUY_XP: 8g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 4g, stage 2: 34g, stage 3: 22g, stage 4: 28g
| Jogador 7 | 249 | 179 | 56 | 10 | 13 | 0 | 0 | 0 | 208 | 48.0 |
- Jogador 7 — gasto por ação: BUY: 115g, BUY_XP: 64g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 4g, stage 2: 51g, stage 3: 56g, stage 4: 19g, stage 5: 17g, stage 6: 32g, stage 7: 0g
| Jogador 8 | 180 | 177 | 57 | 14 | 14 | 1 | 0 | 0 | 17 | 44.0 |
- Jogador 8 — gasto por ação: BUY: 113g, BUY_XP: 64g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 6g, stage 2: 46g, stage 3: 69g, stage 4: 53g, stage 5: 3g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 7 | 28 |
- Jogador 1 · 2-4 · step 91: PASS com 5g, HP 95, nível 4/8 (STABILIZE).
- Jogador 1 · 2-6 · step 109: PASS com 15g, HP 90, nível 5/8 (STABILIZE).
- Jogador 1 · 2-7 · step 116: PASS com 19g, HP 85, nível 5/8 (STABILIZE).
- Jogador 1 · 3-1 · step 126: PASS com 26g, HP 85, nível 5/8 (STABILIZE).
- Jogador 1 · 3-2 · step 139: PASS com 33g, HP 73, nível 5/8 (STABILIZE).
- Jogador 1 · 3-4 · step 156: PASS com 36g, HP 63, nível 6/8 (FAST8).
- Jogador 1 · 3-5 · step 168: PASS com 43g, HP 63, nível 6/8 (FAST8).
- Jogador 1 · 3-6 · step 178: PASS com 51g, HP 63, nível 6/8 (FAST8).
- Jogador 1 · 3-7 · step 189: PASS com 59g, HP 53, nível 6/8 (FAST8).
- Jogador 1 · 4-1 · step 199: PASS com 69g, HP 53, nível 6/8 (FAST8).
- Jogador 1 · 4-2 · step 206: PASS com 81g, HP 53, nível 6/8 (FAST8).
- Jogador 1 · 4-3 · step 218: PASS com 92g, HP 53, nível 6/8 (FAST8).
- Jogador 1 · 4-4 · step 226: PASS com 100g, HP 41, nível 6/8 (FAST8).
- Jogador 1 · 4-5 · step 239: PASS com 110g, HP 41, nível 6/8 (FAST8).
- Jogador 1 · 4-7 · step 258: PASS com 124g, HP 41, nível 6/8 (FAST8).
- Jogador 1 · 5-2 · step 279: PASS com 136g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 5-3 · step 290: PASS com 154g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 5-4 · step 298: PASS com 168g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 5-5 · step 304: REROLL com 172g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 5-5 · step 306: REROLL com 168g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 5-5 · step 307: REROLL com 168g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 5-5 · step 308: REROLL com 168g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 5-5 · step 309: REROLL com 168g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 5-5 · step 310: REROLL com 168g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 5-6 · step 317: PASS com 179g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 5-7 · step 327: PASS com 190g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 6-1 · step 336: PASS com 201g, HP 41, nível 7/8 (FAST8).
- Jogador 1 · 6-3 · step 356: PASS com 214g, HP 7, nível 7/8 (ALL_IN).
| Jogador 2 | 14 | 20 |
- Jogador 2 · 2-2 · step 76: PASS com 4g, HP 95, nível 4/8 (STABILIZE).
- Jogador 2 · 2-3 · step 85: PASS com 9g, HP 95, nível 4/8 (STABILIZE).
- Jogador 2 · 3-2 · step 135: PASS com 5g, HP 80, nível 6/8 (FAST8).
- Jogador 2 · 3-4 · step 156: PASS com 4g, HP 80, nível 6/8 (FAST8).
- Jogador 2 · 3-5 · step 166: PASS com 6g, HP 80, nível 6/8 (FAST8).
- Jogador 2 · 3-6 · step 179: PASS com 16g, HP 80, nível 6/8 (FAST8).
- Jogador 2 · 3-7 · step 188: PASS com 18g, HP 70, nível 7/8 (FAST8).
- Jogador 2 · 4-1 · step 196: PASS com 24g, HP 70, nível 7/8 (FAST8).
- Jogador 2 · 4-2 · step 205: PASS com 30g, HP 70, nível 7/8 (FAST8).
- Jogador 2 · 4-3 · step 216: PASS com 38g, HP 70, nível 7/8 (FAST8).
- Jogador 2 · 4-4 · step 225: PASS com 43g, HP 58, nível 7/8 (FAST8).
- Jogador 2 · 4-5 · step 236: PASS com 47g, HP 58, nível 7/8 (FAST8).
- Jogador 2 · 5-2 · step 274: PASS com 77g, HP 47, nível 7/8 (FAST8).
- Jogador 2 · 5-3 · step 287: PASS com 84g, HP 32, nível 7/8 (STABILIZE).
- Jogador 2 · 5-4 · step 298: PASS com 93g, HP 32, nível 7/8 (STABILIZE).
- Jogador 2 · 5-5 · step 307: PASS com 99g, HP 32, nível 7/8 (STABILIZE).
- Jogador 2 · 5-6 · step 315: REROLL com 105g, HP 17, nível 7/8 (ALL_IN).
- Jogador 2 · 5-6 · step 318: REROLL com 97g, HP 17, nível 7/8 (ALL_IN).
- Jogador 2 · 5-6 · step 319: REROLL com 95g, HP 17, nível 7/8 (ALL_IN).
- Jogador 2 · 6-1 · step 337: REROLL com 114g, HP 2, nível 7/8 (ALL_IN).
| Jogador 3 | 1 | 25 |
- Jogador 3 · 2-1 · step 61: PASS com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 3 · 2-2 · step 71: PASS com 7g, HP 100, nível 4/8 (STABILIZE).
- Jogador 3 · 2-3 · step 82: PASS com 10g, HP 96, nível 4/8 (STABILIZE).
- Jogador 3 · 2-5 · step 98: PASS com 15g, HP 91, nível 5/8 (STABILIZE).
- Jogador 3 · 2-6 · step 105: PASS com 21g, HP 91, nível 5/8 (STABILIZE).
- Jogador 3 · 2-7 · step 118: PASS com 26g, HP 91, nível 5/8 (STABILIZE).
- Jogador 3 · 3-1 · step 127: PASS com 33g, HP 91, nível 5/8 (STABILIZE).
- Jogador 3 · 3-2 · step 137: PASS com 42g, HP 91, nível 5/8 (STABILIZE).
- Jogador 3 · 3-3 · step 147: PASS com 49g, HP 91, nível 5/8 (STABILIZE).
- Jogador 3 · 3-4 · step 155: PASS com 60g, HP 91, nível 5/8 (STABILIZE).
- Jogador 3 · 3-5 · step 166: PASS com 72g, HP 91, nível 5/8 (STABILIZE).
- Jogador 3 · 3-6 · step 178: PASS com 85g, HP 81, nível 5/8 (STABILIZE).
- Jogador 3 · 3-7 · step 186: PASS com 93g, HP 81, nível 6/8 (FAST8).
- Jogador 3 · 4-1 · step 198: PASS com 103g, HP 81, nível 6/8 (FAST8).
- Jogador 3 · 4-2 · step 209: PASS com 111g, HP 70, nível 6/8 (FAST8).
- Jogador 3 · 4-4 · step 230: PASS com 134g, HP 70, nível 6/8 (FAST8).
- Jogador 3 · 4-5 · step 239: PASS com 144g, HP 70, nível 6/8 (FAST8).
- Jogador 3 · 4-6 · step 248: PASS com 150g, HP 58, nível 6/8 (FAST8).
- Jogador 3 · 4-7 · step 260: PASS com 164g, HP 58, nível 6/8 (FAST8).
- Jogador 3 · 5-1 · step 269: PASS com 172g, HP 58, nível 6/8 (FAST8).
- Jogador 3 · 5-2 · step 278: PASS com 185g, HP 43, nível 6/8 (FAST8).
- Jogador 3 · 5-3 · step 285: PASS com 193g, HP 29, nível 6/8 (STABILIZE).
- Jogador 3 · 5-4 · step 298: PASS com 205g, HP 29, nível 6/8 (STABILIZE).
- Jogador 3 · 5-5 · step 307: PASS com 216g, HP 29, nível 6/8 (STABILIZE).
- Jogador 3 · 5-6 · step 315: PASS com 227g, HP 14, nível 6/8 (ALL_IN).
| Jogador 4 | 1 | 13 |
- Jogador 4 · 2-1 · step 60: PASS com 6g, HP 100, nível 4/8 (STABILIZE).
- Jogador 4 · 2-2 · step 74: PASS com 9g, HP 94, nível 4/8 (STABILIZE).
- Jogador 4 · 2-5 · step 96: PASS com 17g, HP 83, nível 5/8 (STABILIZE).
- Jogador 4 · 2-6 · step 104: PASS com 24g, HP 77, nível 5/8 (STABILIZE).
- Jogador 4 · 2-7 · step 117: PASS com 29g, HP 77, nível 5/8 (STABILIZE).
- Jogador 4 · 3-1 · step 127: PASS com 35g, HP 77, nível 5/8 (STABILIZE).
- Jogador 4 · 3-2 · step 140: PASS com 40g, HP 66, nível 5/8 (STABILIZE).
- Jogador 4 · 3-3 · step 148: PASS com 45g, HP 56, nível 5/8 (STABILIZE).
- Jogador 4 · 3-4 · step 155: PASS com 54g, HP 44, nível 5/8 (STABILIZE).
- Jogador 4 · 3-6 · step 178: PASS com 76g, HP 34, nível 5/8 (STABILIZE).
- Jogador 4 · 3-7 · step 187: PASS com 86g, HP 21, nível 6/8 (ALL_IN).
- Jogador 4 · 4-1 · step 199: PASS com 100g, HP 21, nível 6/8 (ALL_IN).
- Jogador 4 · 4-2 · step 206: PASS com 113g, HP 9, nível 6/8 (ALL_IN).
| Jogador 5 | 11 | 33 |
- Jogador 5 · 2-5 · step 97: PASS com 5g, HP 100, nível 5/8 (STABILIZE).
- Jogador 5 · 2-6 · step 107: PASS com 10g, HP 100, nível 5/8 (STABILIZE).
- Jogador 5 · 2-7 · step 120: PASS com 21g, HP 94, nível 5/8 (STABILIZE).
- Jogador 5 · 3-1 · step 127: PASS com 26g, HP 94, nível 5/8 (STABILIZE).
- Jogador 5 · 3-2 · step 139: PASS com 30g, HP 94, nível 5/8 (STABILIZE).
- Jogador 5 · 3-4 · step 157: PASS com 40g, HP 84, nível 6/8 (STABILIZE).
- Jogador 5 · 3-5 · step 168: PASS com 51g, HP 84, nível 6/8 (STABILIZE).
- Jogador 5 · 4-2 · step 206: PASS com 61g, HP 63, nível 6/8 (FAST8).
- Jogador 5 · 4-3 · step 218: PASS com 72g, HP 51, nível 6/8 (FAST8).
- Jogador 5 · 4-4 · step 229: PASS com 82g, HP 51, nível 7/8 (FAST8).
- Jogador 5 · 4-5 · step 240: PASS com 94g, HP 51, nível 7/8 (FAST8).
- Jogador 5 · 4-7 · step 258: PASS com 106g, HP 38, nível 7/8 (STABILIZE).
- Jogador 5 · 5-1 · step 269: PASS com 114g, HP 38, nível 7/8 (STABILIZE).
- Jogador 5 · 5-2 · step 278: REROLL com 126g, HP 38, nível 7/8 (STABILIZE).
- Jogador 5 · 5-3 · step 290: PASS com 133g, HP 38, nível 7/8 (STABILIZE).
- Jogador 5 · 5-4 · step 295: PASS com 143g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 5-5 · step 309: PASS com 154g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 5-6 · step 319: PASS com 163g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 5-7 · step 327: PASS com 175g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-1 · step 337: REROLL com 182g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-2 · step 348: REROLL com 183g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-3 · step 358: PASS com 189g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-4 · step 364: REROLL com 207g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-4 · step 369: REROLL com 203g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-5 · step 376: REROLL com 209g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-5 · step 379: REROLL com 209g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-6 · step 383: REROLL com 217g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-6 · step 386: REROLL com 217g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-6 · step 387: REROLL com 215g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-6 · step 388: REROLL com 213g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-7 · step 394: REROLL com 226g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 6-7 · step 400: PASS com 223g, HP 22, nível 7/8 (ALL_IN).
- Jogador 5 · 7-1 · step 408: PASS com 231g, HP 22, nível 7/8 (ALL_IN).
| Jogador 6 | 2 | 16 |
- Jogador 6 · 2-5 · step 99: PASS com 13g, HP 90, nível 5/8 (STABILIZE).
- Jogador 6 · 2-6 · step 105: PASS com 17g, HP 90, nível 5/8 (STABILIZE).
- Jogador 6 · 2-7 · step 117: PASS com 19g, HP 84, nível 5/8 (STABILIZE).
- Jogador 6 · 3-1 · step 127: PASS com 22g, HP 84, nível 5/8 (STABILIZE).
- Jogador 6 · 3-2 · step 137: PASS com 28g, HP 72, nível 5/8 (STABILIZE).
- Jogador 6 · 3-3 · step 146: PASS com 31g, HP 61, nível 5/8 (STABILIZE).
- Jogador 6 · 3-4 · step 155: PASS com 37g, HP 52, nível 5/8 (STABILIZE).
- Jogador 6 · 3-6 · step 175: PASS com 51g, HP 52, nível 6/8 (FAST8).
- Jogador 6 · 3-7 · step 186: PASS com 57g, HP 42, nível 6/8 (FAST8).
- Jogador 6 · 4-1 · step 197: PASS com 64g, HP 42, nível 6/8 (FAST8).
- Jogador 6 · 4-2 · step 208: PASS com 72g, HP 31, nível 6/8 (STABILIZE).
- Jogador 6 · 4-3 · step 215: PASS com 82g, HP 19, nível 6/8 (ALL_IN).
- Jogador 6 · 4-4 · step 224: REROLL com 95g, HP 7, nível 6/8 (ALL_IN).
- Jogador 6 · 4-4 · step 225: REROLL com 93g, HP 7, nível 6/8 (ALL_IN).
- Jogador 6 · 4-5 · step 239: PASS com 103g, HP 7, nível 6/8 (ALL_IN).
- Jogador 6 · 4-6 · step 246: PASS com 119g, HP 7, nível 6/8 (ALL_IN).
| Jogador 7 | 16 | 16 |
- Jogador 7 · 2-5 · step 100: PASS com 5g, HP 96, nível 5/8 (STABILIZE).
- Jogador 7 · 2-7 · step 119: PASS com 5g, HP 96, nível 6/8 (STABILIZE).
- Jogador 7 · 3-1 · step 127: PASS com 7g, HP 96, nível 6/8 (STABILIZE).
- Jogador 7 · 3-7 · step 185: PASS com 4g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 4-1 · step 200: PASS com 13g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 4-2 · step 205: PASS com 21g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 4-3 · step 216: PASS com 26g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 4-4 · step 226: PASS com 33g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 4-5 · step 235: PASS com 39g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 4-6 · step 246: PASS com 49g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 4-7 · step 256: PASS com 60g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 5-1 · step 266: PASS com 73g, HP 85, nível 7/8 (FAST8).
- Jogador 7 · 5-2 · step 275: PASS com 83g, HP 70, nível 7/8 (FAST8).
- Jogador 7 · 5-4 · step 295: PASS com 97g, HP 55, nível 7/8 (FAST8).
- Jogador 7 · 5-5 · step 309: PASS com 110g, HP 55, nível 7/8 (FAST8).
- Jogador 7 · 5-6 · step 317: PASS com 124g, HP 55, nível 7/8 (FAST8).
| Jogador 8 | 16 | 9 |
- Jogador 8 · 2-5 · step 99: PASS com 6g, HP 96, nível 5/8 (STABILIZE).
- Jogador 8 · 2-6 · step 109: PASS com 7g, HP 91, nível 5/8 (STABILIZE).
- Jogador 8 · 4-1 · step 198: PASS com 8g, HP 59, nível 7/8 (FAST8).
- Jogador 8 · 4-2 · step 206: PASS com 15g, HP 59, nível 7/8 (FAST8).
- Jogador 8 · 4-4 · step 227: PASS com 9g, HP 47, nível 7/8 (FAST8).
- Jogador 8 · 4-5 · step 239: PASS com 7g, HP 47, nível 7/8 (FAST8).
- Jogador 8 · 4-7 · step 254: PASS com 7g, HP 21, nível 7/8 (ALL_IN).
- Jogador 8 · 5-1 · step 268: PASS com 10g, HP 21, nível 7/8 (ALL_IN).
- Jogador 8 · 5-2 · step 275: PASS com 17g, HP 5, nível 7/8 (ALL_IN).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 2 | 2 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 2 | 2 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 235 | 67 | 71 | 97 | -0.0009 | 0.1798 | -0.0027 | 0.3374 | 0.0018 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0556 (56 ações), BUY_XP: Δ 0.0613 (7 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0065 (3 ações), MOVE_BENCH: Δ 0.0270 (46 ações), MOVE_BOARD: Δ 0.0142 (60 ações), PASS: Δ 0.0141 (27 ações), REROLL: Δ -0.1267 (6 ações), SELL: Δ 0.0322 (23 ações)
| Jogador 2 | 205 | 49 | 38 | 118 | 0.0016 | 0.1864 | 0.0002 | 0.3234 | 0.0014 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0060 (54 ações), BUY_XP: Δ 0.0070 (14 ações), CRAFT_AND_EQUIP: Δ 0.0020 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (4 ações), MOVE_BENCH: Δ -0.0190 (17 ações), MOVE_BOARD: Δ 0.0063 (62 ações), PASS: Δ 0.0000 (25 ações), REROLL: Δ 0.0000 (4 ações), SELL: Δ 0.0267 (18 ações)
| Jogador 3 | 176 | 55 | 48 | 73 | 0.0033 | 0.4093 | 0.0012 | 0.3043 | 0.0021 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0427 (39 ações), BUY_XP: Δ 0.0477 (1 ações), CRAFT_AND_EQUIP: Δ 0.0322 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0064 (45 ações), MOVE_BOARD: Δ 0.0345 (40 ações), PASS: Δ 0.0000 (29 ações), SELL: Δ 0.0234 (13 ações)
| Jogador 4 | 108 | 30 | 25 | 53 | 0.0044 | 0.2361 | 0.0021 | 0.2123 | 0.0023 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0122 (28 ações), BUY_XP: Δ 0.0310 (1 ações), CRAFT_AND_EQUIP: Δ 0.0301 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0209 (24 ações), MOVE_BOARD: Δ -0.0037 (28 ações), PASS: Δ 0.0000 (17 ações), SELL: Δ 0.0600 (4 ações)
| Jogador 5 | 287 | 63 | 53 | 171 | 0.0031 | 0.2513 | 0.0019 | 0.3295 | 0.0012 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0206 (82 ações), BUY_XP: Δ 0.0043 (11 ações), CRAFT_AND_EQUIP: Δ 0.0005 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0043 (7 ações), MOVE_BENCH: Δ 0.0441 (46 ações), MOVE_BOARD: Δ -0.0026 (50 ações), PASS: Δ 0.0000 (27 ações), REROLL: Δ 0.0100 (12 ações), SELL: Δ 0.0107 (45 ações)
| Jogador 6 | 135 | 36 | 36 | 63 | 0.0063 | -0.1837 | 0.0032 | 0.3486 | 0.0031 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ 0.0009 (38 ações), BUY_XP: Δ 0.0000 (2 ações), CRAFT_AND_EQUIP: Δ 0.0000 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0399 (20 ações), MOVE_BOARD: Δ -0.0109 (37 ações), PASS: Δ 0.0000 (20 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0420 (10 ações)
| Jogador 7 | 249 | 65 | 65 | 119 | 0.0040 | 0.2674 | 0.0025 | 0.3565 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0293 (54 ações), BUY_XP: Δ 0.0034 (16 ações), CRAFT_AND_EQUIP: Δ 0.0251 (7 ações), EQUIP_FROM_INVENTORY: Δ -0.0035 (7 ações), MOVE_BENCH: Δ 0.0184 (63 ações), MOVE_BOARD: Δ 0.0126 (53 ações), PASS: Δ 0.0000 (31 ações), SELL: Δ 0.0300 (18 ações)
| Jogador 8 | 180 | 42 | 35 | 103 | 0.0038 | 0.3717 | 0.0024 | 0.3027 | 0.0014 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0175 (55 ações), BUY_XP: Δ 0.0061 (16 ações), CRAFT_AND_EQUIP: Δ -0.0995 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0290 (19 ações), MOVE_BOARD: Δ 0.0297 (40 ações), PASS: Δ 0.0000 (20 ações), SELL: Δ 0.0234 (22 ações)
- Jogador 1 — rounds avaliados: 35; correlação estrutural/combate: 0.321; posicional/combate: 0.074.
- Jogador 1 — combate positive: score estrutural prévio 0.279
  score posicional prévio 0.328
- Jogador 1 — combate negative: score estrutural prévio -0.029
  score posicional prévio 0.314
- Jogador 2 — rounds avaliados: 33; correlação estrutural/combate: 0.211; posicional/combate: 0.106.
- Jogador 2 — combate positive: score estrutural prévio 0.361
  score posicional prévio 0.342
- Jogador 2 — combate negative: score estrutural prévio 0.146
  score posicional prévio 0.325
- Jogador 3 — rounds avaliados: 31; correlação estrutural/combate: -0.119; posicional/combate: -0.132.
- Jogador 3 — combate positive: score estrutural prévio 0.303
  score posicional prévio 0.267
- Jogador 3 — combate negative: score estrutural prévio 0.388
  score posicional prévio 0.304
- Jogador 4 — rounds avaliados: 20; correlação estrutural/combate: -0.217; posicional/combate: -0.323.
- Jogador 4 — combate positive: score estrutural prévio 0.240
  score posicional prévio 0.156
- Jogador 4 — combate negative: score estrutural prévio 0.265
  score posicional prévio 0.219
- Jogador 5 — rounds avaliados: 40; correlação estrutural/combate: 0.047; posicional/combate: -0.036.
- Jogador 5 — combate positive: score estrutural prévio 0.255
  score posicional prévio 0.323
- Jogador 5 — combate negative: score estrutural prévio 0.214
  score posicional prévio 0.317
- Jogador 6 — rounds avaliados: 24; correlação estrutural/combate: 0.170; posicional/combate: 0.084.
- Jogador 6 — combate positive: score estrutural prévio 0.075
  score posicional prévio 0.365
- Jogador 6 — combate negative: score estrutural prévio -0.251
  score posicional prévio 0.336
- Jogador 7 — rounds avaliados: 40; correlação estrutural/combate: 0.027; posicional/combate: 0.057.
- Jogador 7 — combate positive: score estrutural prévio 0.271
  score posicional prévio 0.379
- Jogador 7 — combate negative: score estrutural prévio 0.270
  score posicional prévio 0.392
- Jogador 8 — rounds avaliados: 27; correlação estrutural/combate: -0.015; posicional/combate: -0.117.
- Jogador 8 — combate positive: score estrutural prévio 0.451
  score posicional prévio 0.291
- Jogador 8 — combate negative: score estrutural prévio 0.438
  score posicional prévio 0.315

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 269 | OK (269) | 4 | 4 | 0 | 0 | 8 | 2 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Bloodthirster, TFT_Item_InfinityEdge, TFT_Item_Morellonomicon, TFT_Item_RabadonsDeathcap, TFT_Item_RapidFireCannon, TFT_Item_RedBuff, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 237 | OK (237) | 5 | 3 | 0 | 0 | 8 | 2 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_GargoyleStoneplate, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 206 | OK (206) | 6 | 0 | 1 | 0 | 7 | 2 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_RedBuff, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 127 | OK (127) | 3 | 2 | 0 | 1 | 5 | 1 |
- Jogador 4 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Bloodthirster, TFT_Item_Leviathan, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 326 | OK (326) | 6 | 3 | 0 | 0 | 9 | 3 |
- Jogador 5 — IDs equipados observados: DA_18_EmblemSlayer, TFT_Item_GargoyleStoneplate, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_Leviathan, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 158 | OK (158) | 5 | 0 | 0 | 1 | 5 | 1 |
- Jogador 6 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_HextechGunblade, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 289 | OK (289) | 7 | 2 | 0 | 0 | 9 | 2 |
- Jogador 7 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_NightHarvester, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_RunaansHurricane, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 206 | OK (206) | 7 | 0 | 0 | 0 | 7 | 1 |
- Jogador 8 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_HextechGunblade, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.147 | 0.000 |
| Jogador 1 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.006 | 0.000 |
| Jogador 1 | 1-3 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 4 | 1 | 3 → 3 | -0.017 | 0.000 |
| Jogador 1 | 1-4 | 8 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 4 → 6 | 2 | 3 → 4 | -0.033 | 0.000 |
| Jogador 1 | 2-1 | 11 | 2.000 | 4.000 | 0 → 0 | 2 → 1 | 11% → 14% | 6 → 8 | 4 | 4 → 4 | 0.016 | 0.249 |
| Jogador 1 | 2-2 | 6 | 0.000 | 10.000 | 0 → 0 | 1 → 2 | 14% → 14% | 8 → 8 | 5 | 4 → 4 | -0.051 | -0.395 |
| Jogador 1 | 2-3 | 8 | 2.000 | 4.000 | 0 → 1 | 2 → 2 | 14% → 14% | 8 → 9 | 5 | 4 → 4 | 0.058 | 0.308 |
| Jogador 1 | 2-4 | 6 | 0.000 | 8.000 | 1 → 1 | 2 → 2 | 14% → 14% | 9 → 10 | 4 | 4 → 4 | 0.003 | 0.000 |
| Jogador 1 | 2-5 | 9 | 0.000 | -4.000 | 1 → 1 | 2 → 3 | 14% → 14% | 10 → 19 | 2 | 4 → 5 | 0.006 | -0.269 |
| Jogador 1 | 2-6 | 9 | 8.000 | -2.000 | 1 → 1 | 3 → 2 | 14% → 18% | 19 → 22 | 4 | 5 → 5 | -0.021 | -0.258 |
| Jogador 1 | 2-7 | 6 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 18% → 18% | 22 → 26 | 3 | 5 → 5 | -0.035 | 0.000 |
| Jogador 1 | 3-1 | 6 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 18% → 18% | 26 → 34 | 0 | 5 → 5 | -0.010 | -0.477 |
| Jogador 1 | 3-2 | 9 | 4.000 | 0.000 | 1 → 0 | 3 → 3 | 18% → 18% | 34 → 42 | 4 | 5 → 5 | -0.017 | -0.298 |
| Jogador 1 | 3-3 | 10 | 6.000 | 0.000 | 0 → 0 | 3 → 3 | 18% → 21% | 42 → 36 | 17 | 5 → 6 | 0.006 | 0.282 |
| Jogador 1 | 3-4 | 6 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 36 → 44 | 0 | 6 → 6 | 0.087 | 0.000 |
| Jogador 1 | 3-5 | 8 | 4.000 | -6.000 | 0 → 1 | 3 → 2 | 21% → 21% | 44 → 54 | 3 | 6 → 6 | -0.015 | 0.358 |
| Jogador 1 | 3-6 | 8 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 21% → 21% | 54 → 61 | 4 | 6 → 6 | 0.083 | -0.329 |
| Jogador 1 | 3-7 | 9 | 0.000 | -4.000 | 1 → 1 | 3 → 4 | 21% → 21% | 61 → 69 | 6 | 6 → 6 | -0.035 | 0.000 |
| Jogador 1 | 4-1 | 9 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 21% → 21% | 69 → 80 | 0 | 6 → 6 | 0.032 | 0.328 |
| Jogador 1 | 4-2 | 6 | 0.000 | -2.000 | 1 → 1 | 4 → 3 | 21% → 21% | 80 → 93 | 1 | 6 → 6 | 0.005 | 0.481 |
| Jogador 1 | 4-3 | 8 | -2.000 | 0.000 | 1 → 1 | 3 → 3 | 21% → 21% | 93 → 102 | 3 | 6 → 6 | -0.010 | -0.352 |
| Jogador 1 | 4-4 | 6 | 0.000 | 4.000 | 1 → 1 | 3 → 3 | 21% → 21% | 102 → 110 | 2 | 6 → 6 | 0.045 | 0.000 |
| Jogador 1 | 4-5 | 9 | 2.000 | 0.000 | 1 → 1 | 3 → 4 | 21% → 21% | 110 → 120 | 7 | 6 → 6 | 0.008 | 0.000 |
| Jogador 1 | 4-6 | 10 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 120 → 123 | 13 | 6 → 6 | -0.015 | 0.000 |
| Jogador 1 | 4-7 | 8 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 123 → 134 | 4 | 6 → 7 | 0.003 | 0.000 |
| Jogador 1 | 5-1 | 10 | 2.000 | 8.000 | 1 → 1 | 4 → 5 | 21% → 25% | 134 → 140 | 6 | 7 → 7 | -0.010 | 0.296 |
| Jogador 1 | 5-2 | 9 | 0.000 | 2.000 | 1 → 1 | 5 → 5 | 25% → 25% | 140 → 148 | 7 | 7 → 7 | -0.027 | 0.328 |
| Jogador 1 | 5-3 | 10 | 0.000 | -8.000 | 1 → 1 | 5 → 6 | 25% → 25% | 148 → 166 | 5 | 7 → 7 | -0.013 | 0.296 |
| Jogador 1 | 5-4 | 8 | 0.000 | -6.000 | 1 → 1 | 6 → 5 | 25% → 25% | 166 → 179 | 3 | 7 → 7 | -0.007 | 0.000 |
| Jogador 1 | 5-5 | 10 | 0.000 | 14.000 | 1 → 1 | 5 → 5 | 25% → 25% | 179 → 179 | 11 | 7 → 7 | -0.038 | 0.000 |
| Jogador 1 | 5-6 | 7 | 0.000 | 2.000 | 1 → 1 | 5 → 5 | 25% → 25% | 179 → 191 | 3 | 7 → 7 | 0.063 | 0.436 |
| Jogador 1 | 5-7 | 7 | 0.000 | 2.000 | 1 → 1 | 5 → 6 | 25% → 25% | 191 → 201 | 3 | 7 → 7 | -0.054 | 0.000 |
| Jogador 1 | 6-1 | 6 | -6.000 | 6.000 | 1 → 0 | 6 → 6 | 25% → 25% | 201 → 211 | 0 | 7 → 7 | -0.031 | -0.467 |
| Jogador 1 | 6-2 | 10 | 8.000 | -4.000 | 0 → 1 | 6 → 4 | 25% → 25% | 211 → 218 | 9 | 7 → 7 | 0.018 | -0.285 |
| Jogador 1 | 6-3 | 6 | -36.000 | -42.000 | 1 → 0 | 4 → 0 | 25% → 0% | 218 → 214 | 4 | 7 → 7 | -0.047 | -0.475 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 15, COMPOSITION_COMPATIBILITY: 17, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 15; mudanças de composição: 0; posicionamento melhorou em 72 ações e piorou em 72.
- Jogador 1 — estado final: ouro 214, nível 7, vida 7.0, colocação 3.
| Jogador 2 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.214 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.050 | 0.000 |
| Jogador 2 | 1-3 | 4 | 0.000 | 0.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 4 | 1 | 3 → 3 | 0.111 | 0.000 |
| Jogador 2 | 1-4 | 6 | 2.000 | 2.000 | 1 → 1 | 0 → 1 | 7% → 11% | 4 → 6 | 2 | 3 → 4 | 0.041 | 0.000 |
| Jogador 2 | 2-1 | 11 | 2.000 | 10.000 | 1 → 1 | 1 → 2 | 11% → 14% | 6 → 5 | 6 | 4 → 4 | -0.051 | -0.220 |
| Jogador 2 | 2-2 | 8 | 6.000 | -6.000 | 1 → 1 | 2 → 1 | 14% → 14% | 5 → 10 | 1 | 4 → 4 | 0.028 | 0.314 |
| Jogador 2 | 2-3 | 8 | 0.000 | 2.000 | 1 → 1 | 1 → 1 | 14% → 14% | 10 → 14 | 1 | 4 → 4 | 0.043 | -0.290 |
| Jogador 2 | 2-4 | 6 | 0.000 | -4.000 | 1 → 1 | 1 → 1 | 14% → 14% | 14 → 19 | 5 | 4 → 5 | 0.081 | 0.000 |
| Jogador 2 | 2-5 | 9 | 6.000 | -2.000 | 1 → 1 | 1 → 1 | 14% → 18% | 19 → 7 | 22 | 5 → 6 | 0.000 | -0.264 |
| Jogador 2 | 2-6 | 6 | 8.000 | 6.000 | 1 → 1 | 1 → 1 | 18% → 21% | 7 → 6 | 7 | 6 → 6 | -0.150 | -0.395 |
| Jogador 2 | 2-7 | 7 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | 0.074 | 0.000 |
| Jogador 2 | 3-1 | 9 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 21% → 21% | 8 → 6 | 8 | 6 → 6 | 0.042 | 0.343 |
| Jogador 2 | 3-2 | 5 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 21% → 21% | 6 → 12 | 1 | 6 → 6 | 0.001 | 0.607 |
| Jogador 2 | 3-3 | 7 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 21% → 21% | 12 → 8 | 11 | 6 → 6 | -0.023 | 0.441 |
| Jogador 2 | 3-4 | 6 | 0.000 | 8.000 | 1 → 1 | 4 → 5 | 21% → 21% | 8 → 10 | 4 | 6 → 6 | 0.037 | 0.000 |
| Jogador 2 | 3-5 | 6 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 21% → 21% | 10 → 13 | 4 | 6 → 6 | -0.095 | 0.469 |
| Jogador 2 | 3-6 | 9 | 0.000 | -6.000 | 1 → 1 | 5 → 5 | 21% → 21% | 13 → 22 | 4 | 6 → 6 | 0.004 | -0.293 |
| Jogador 2 | 3-7 | 8 | 2.000 | -8.000 | 1 → 1 | 5 → 4 | 21% → 25% | 22 → 24 | 7 | 6 → 7 | -0.003 | 0.000 |
| Jogador 2 | 4-1 | 6 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 24 → 32 | 0 | 7 → 7 | 0.004 | 0.475 |
| Jogador 2 | 4-2 | 5 | 0.000 | 4.000 | 1 → 1 | 4 → 5 | 25% → 25% | 32 → 40 | 2 | 7 → 7 | 0.097 | 0.577 |
| Jogador 2 | 4-3 | 6 | 0.000 | 0.000 | 1 → 1 | 5 → 4 | 25% → 25% | 40 → 46 | 2 | 7 → 7 | -0.002 | -0.444 |
| Jogador 2 | 4-4 | 5 | 0.000 | 6.000 | 1 → 1 | 4 → 4 | 25% → 25% | 46 → 52 | 3 | 7 → 7 | -0.018 | 0.000 |
| Jogador 2 | 4-5 | 6 | 0.000 | 10.000 | 1 → 1 | 4 → 4 | 25% → 25% | 52 → 57 | 5 | 7 → 7 | 0.013 | 0.477 |
| Jogador 2 | 4-6 | 10 | -4.000 | -14.000 | 1 → 1 | 4 → 3 | 25% → 18% | 57 → 72 | 8 | 7 → 7 | 0.007 | -0.268 |
| Jogador 2 | 4-7 | 10 | 0.000 | -6.000 | 1 → 1 | 3 → 3 | 18% → 18% | 72 → 75 | 15 | 7 → 7 | 0.012 | 0.000 |
| Jogador 2 | 5-1 | 10 | 10.000 | 8.000 | 1 → 1 | 3 → 3 | 18% → 21% | 75 → 77 | 10 | 7 → 7 | 0.017 | 0.316 |
| Jogador 2 | 5-2 | 4 | 4.000 | -4.000 | 1 → 1 | 3 → 3 | 21% → 25% | 77 → 87 | 0 | 7 → 7 | -0.013 | -0.712 |
| Jogador 2 | 5-3 | 7 | 0.000 | 6.000 | 1 → 1 | 3 → 5 | 25% → 25% | 87 → 95 | 6 | 7 → 7 | -0.013 | 0.453 |
| Jogador 2 | 5-4 | 8 | 0.000 | 0.000 | 1 → 1 | 5 → 3 | 25% → 25% | 95 → 103 | 5 | 7 → 7 | -0.076 | 0.000 |
| Jogador 2 | 5-5 | 7 | 0.000 | 8.000 | 1 → 1 | 3 → 3 | 25% → 25% | 103 → 109 | 4 | 7 → 7 | -0.024 | -0.393 |
| Jogador 2 | 5-6 | 10 | 0.000 | 12.000 | 1 → 1 | 3 → 3 | 25% → 25% | 109 → 107 | 19 | 7 → 7 | 0.006 | -0.280 |
| Jogador 2 | 5-7 | 10 | 4.000 | -4.000 | 1 → 2 | 3 → 3 | 25% → 25% | 107 → 117 | 9 | 7 → 7 | 0.003 | 0.000 |
| Jogador 2 | 6-1 | 10 | -46.000 | -52.000 | 2 → 0 | 3 → 0 | 25% → 0% | 117 → 110 | 10 | 7 → 7 | -0.038 | -0.280 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 8, COMPOSITION_COMPATIBILITY: 18, IMMEDIATE_UPGRADE: 12, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 52 ações e piorou em 42.
- Jogador 2 — estado final: ouro 110, nível 7, vida 2.0, colocação 4.
| Jogador 3 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.150 | 0.000 |
| Jogador 3 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.007 | 0.000 |
| Jogador 3 | 1-3 | 5 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 7% → 7% | 2 → 3 | 2 | 3 → 3 | -0.092 | 0.000 |
| Jogador 3 | 1-4 | 3 | 4.000 | -4.000 | 0 → 1 | 0 → 0 | 7% → 11% | 3 → 7 | 0 | 3 → 4 | 0.065 | 0.000 |
| Jogador 3 | 2-1 | 5 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 11% → 14% | 7 → 10 | 3 | 4 → 4 | -0.014 | 0.476 |
| Jogador 3 | 2-2 | 3 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 10 → 12 | 3 | 4 → 4 | -0.020 | -0.754 |
| Jogador 3 | 2-3 | 5 | 0.000 | 4.000 | 1 → 1 | 1 → 1 | 14% → 14% | 12 → 17 | 2 | 4 → 4 | 0.025 | -0.484 |
| Jogador 3 | 2-4 | 6 | 10.000 | -10.000 | 1 → 1 | 1 → 0 | 14% → 18% | 17 → 19 | 5 | 4 → 5 | 0.050 | 0.000 |
| Jogador 3 | 2-5 | 7 | 0.000 | 8.000 | 1 → 1 | 0 → 1 | 18% → 18% | 19 → 22 | 4 | 5 → 5 | 0.019 | 0.352 |
| Jogador 3 | 2-6 | 5 | 4.000 | -4.000 | 1 → 1 | 1 → 0 | 18% → 18% | 22 → 30 | 1 | 5 → 5 | -0.026 | 0.502 |
| Jogador 3 | 2-7 | 8 | 0.000 | 8.000 | 1 → 1 | 0 → 1 | 18% → 18% | 30 → 34 | 4 | 5 → 5 | 0.038 | 0.000 |
| Jogador 3 | 3-1 | 7 | 0.000 | 2.000 | 1 → 1 | 1 → 1 | 18% → 18% | 34 → 43 | 1 | 5 → 5 | -0.124 | 0.429 |
| Jogador 3 | 3-2 | 7 | 0.000 | 2.000 | 1 → 1 | 1 → 2 | 18% → 18% | 43 → 53 | 1 | 5 → 5 | 0.062 | 0.409 |
| Jogador 3 | 3-3 | 7 | 0.000 | 8.000 | 1 → 1 | 2 → 2 | 18% → 18% | 53 → 62 | 4 | 5 → 5 | 0.094 | 0.409 |
| Jogador 3 | 3-4 | 5 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 18% → 18% | 62 → 72 | 2 | 5 → 5 | -0.038 | 0.000 |
| Jogador 3 | 3-5 | 6 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 18% → 18% | 72 → 82 | 3 | 5 → 5 | 0.043 | -0.439 |
| Jogador 3 | 3-6 | 8 | 0.000 | -4.000 | 1 → 1 | 2 → 3 | 18% → 18% | 82 → 96 | 2 | 5 → 6 | -0.011 | 0.358 |
| Jogador 3 | 3-7 | 6 | 6.000 | 0.000 | 1 → 1 | 3 → 3 | 18% → 21% | 96 → 103 | 3 | 6 → 6 | 0.044 | 0.000 |
| Jogador 3 | 4-1 | 8 | 0.000 | 0.000 | 1 → 1 | 3 → 4 | 21% → 21% | 103 → 113 | 3 | 6 → 6 | -0.021 | -0.334 |
| Jogador 3 | 4-2 | 9 | 0.000 | 4.000 | 1 → 1 | 4 → 6 | 21% → 21% | 113 → 122 | 5 | 6 → 6 | 0.007 | 0.335 |
| Jogador 3 | 4-3 | 10 | 0.000 | 0.000 | 1 → 1 | 6 → 5 | 21% → 21% | 122 → 134 | 3 | 6 → 6 | -0.102 | 0.298 |
| Jogador 3 | 4-4 | 10 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 21% → 21% | 134 → 145 | 3 | 6 → 6 | 0.091 | 0.000 |
| Jogador 3 | 4-5 | 9 | -2.000 | -2.000 | 1 → 1 | 5 → 4 | 21% → 21% | 145 → 154 | 5 | 6 → 6 | -0.016 | -0.307 |
| Jogador 3 | 4-6 | 8 | 0.000 | 8.000 | 1 → 1 | 4 → 4 | 21% → 21% | 154 → 161 | 4 | 6 → 6 | 0.029 | 0.356 |
| Jogador 3 | 4-7 | 10 | -2.000 | -4.000 | 1 → 1 | 4 → 3 | 21% → 21% | 161 → 174 | 5 | 6 → 6 | -0.001 | 0.000 |
| Jogador 3 | 5-1 | 9 | 2.000 | 2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 174 → 182 | 2 | 6 → 6 | -0.004 | -0.333 |
| Jogador 3 | 5-2 | 8 | 0.000 | -8.000 | 1 → 1 | 3 → 2 | 21% → 21% | 182 → 196 | 2 | 6 → 6 | -0.046 | -0.348 |
| Jogador 3 | 5-3 | 5 | 2.000 | 4.000 | 1 → 1 | 2 → 3 | 21% → 21% | 196 → 204 | 3 | 6 → 6 | -0.010 | 0.000 |
| Jogador 3 | 5-4 | 8 | 0.000 | 0.000 | 1 → 1 | 3 → 5 | 21% → 21% | 204 → 216 | 4 | 6 → 6 | 0.007 | 0.000 |
| Jogador 3 | 5-5 | 7 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 21% → 21% | 216 → 227 | 0 | 6 → 6 | -0.001 | -0.407 |
| Jogador 3 | 5-6 | 5 | -30.000 | -34.000 | 1 → 0 | 5 → 0 | 21% → 0% | 227 → 227 | 0 | 6 → 6 | -0.136 | -0.580 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 11, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 60 ações e piorou em 51.
- Jogador 3 — estado final: ouro 227, nível 6, vida 14.0, colocação 5.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.150 | 0.000 |
| Jogador 4 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 4 | 1-3 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 5 | 0 | 3 → 3 | -0.006 | 0.000 |
| Jogador 4 | 1-4 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 5 → 7 | 2 | 3 → 4 | 0.030 | 0.000 |
| Jogador 4 | 2-1 | 4 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 7 → 11 | 1 | 4 → 4 | -0.024 | -0.645 |
| Jogador 4 | 2-2 | 6 | 0.000 | 4.000 | 0 → 0 | 2 → 2 | 14% → 14% | 11 → 15 | 2 | 4 → 4 | -0.007 | -0.422 |
| Jogador 4 | 2-3 | 8 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 14% → 14% | 15 → 20 | 2 | 4 → 4 | -0.011 | -0.296 |
| Jogador 4 | 2-4 | 6 | 6.000 | 0.000 | 0 → 0 | 2 → 2 | 14% → 18% | 20 → 20 | 7 | 4 → 5 | -0.007 | 0.000 |
| Jogador 4 | 2-5 | 5 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 18% | 20 → 24 | 3 | 5 → 5 | 0.007 | -0.486 |
| Jogador 4 | 2-6 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 24 → 32 | 0 | 5 → 5 | -0.005 | 0.616 |
| Jogador 4 | 2-7 | 7 | 0.000 | 4.000 | 0 → 0 | 2 → 2 | 18% → 18% | 32 → 36 | 3 | 5 → 5 | -0.008 | 0.000 |
| Jogador 4 | 3-1 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 1 | 18% → 18% | 36 → 43 | 1 | 5 → 5 | -0.009 | -0.404 |
| Jogador 4 | 3-2 | 10 | 2.000 | 2.000 | 0 → 1 | 1 → 1 | 18% → 18% | 43 → 50 | 3 | 5 → 5 | 0.020 | -0.263 |
| Jogador 4 | 3-3 | 8 | 0.000 | 10.000 | 1 → 1 | 1 → 1 | 18% → 18% | 50 → 55 | 5 | 5 → 5 | 0.006 | -0.364 |
| Jogador 4 | 3-4 | 5 | 2.000 | 0.000 | 1 → 0 | 1 → 2 | 18% → 18% | 55 → 65 | 1 | 5 → 5 | -0.074 | 0.000 |
| Jogador 4 | 3-5 | 10 | 2.000 | 2.000 | 0 → 1 | 2 → 1 | 18% → 18% | 65 → 74 | 5 | 5 → 5 | 0.026 | -0.268 |
| Jogador 4 | 3-6 | 8 | 0.000 | -2.000 | 1 → 1 | 1 → 2 | 18% → 18% | 74 → 88 | 1 | 5 → 6 | 0.014 | -0.350 |
| Jogador 4 | 3-7 | 7 | 6.000 | -2.000 | 1 → 1 | 2 → 3 | 18% → 21% | 88 → 98 | 2 | 6 → 6 | -0.005 | 0.000 |
| Jogador 4 | 4-1 | 9 | 0.000 | -2.000 | 1 → 1 | 3 → 4 | 21% → 21% | 98 → 113 | 1 | 6 → 6 | 0.023 | -0.307 |
| Jogador 4 | 4-2 | 6 | -28.000 | -26.000 | 1 → 0 | 4 → 0 | 21% → 0% | 113 → 113 | 3 | 6 → 6 | -0.116 | -0.475 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 1, COMPOSITION_COMPATIBILITY: 13, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 9; mudanças de composição: 0; posicionamento melhorou em 33 ações e piorou em 27.
- Jogador 4 — estado final: ouro 113, nível 6, vida 9.0, colocação 8.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.149 | 0.000 |
| Jogador 5 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.014 | 0.000 |
| Jogador 5 | 1-4 | 6 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.018 | 0.000 |
| Jogador 5 | 2-1 | 9 | 4.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.017 | 0.285 |
| Jogador 5 | 2-2 | 6 | 0.000 | 8.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 9 | 4 | 4 → 4 | -0.020 | 0.405 |
| Jogador 5 | 2-3 | 8 | 0.000 | 0.000 | 0 → 0 | 2 → 1 | 14% → 14% | 9 → 8 | 11 | 4 → 5 | 0.106 | 0.320 |
| Jogador 5 | 2-4 | 6 | 2.000 | 6.000 | 0 → 0 | 1 → 1 | 14% → 18% | 8 → 6 | 9 | 5 → 5 | 0.005 | 0.000 |
| Jogador 5 | 2-5 | 6 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 12 | 1 | 5 → 5 | -0.092 | 0.419 |
| Jogador 5 | 2-6 | 7 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 18% → 18% | 12 → 16 | 2 | 5 → 5 | 0.033 | -0.340 |
| Jogador 5 | 2-7 | 10 | 0.000 | -12.000 | 0 → 0 | 2 → 3 | 18% → 18% | 16 → 28 | 4 | 5 → 5 | -0.018 | 0.000 |
| Jogador 5 | 3-1 | 7 | -2.000 | 2.000 | 0 → 0 | 3 → 2 | 18% → 18% | 28 → 34 | 2 | 5 → 5 | -0.066 | 0.402 |
| Jogador 5 | 3-2 | 9 | 2.000 | 4.000 | 0 → 0 | 2 → 2 | 18% → 18% | 34 → 40 | 4 | 5 → 6 | 0.008 | 0.312 |
| Jogador 5 | 3-3 | 10 | 4.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 21% | 40 → 44 | 9 | 6 → 6 | 0.038 | -0.268 |
| Jogador 5 | 3-4 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 3 | 21% → 21% | 44 → 49 | 4 | 6 → 6 | -0.078 | 0.000 |
| Jogador 5 | 3-5 | 8 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 49 → 62 | 4 | 6 → 6 | -0.003 | -0.347 |
| Jogador 5 | 3-6 | 10 | 2.000 | -6.000 | 0 → 0 | 3 → 2 | 21% → 21% | 62 → 72 | 7 | 6 → 6 | 0.018 | 0.281 |
| Jogador 5 | 3-7 | 10 | 0.000 | 14.000 | 0 → 0 | 2 → 3 | 21% → 21% | 72 → 58 | 24 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 10 | 4.000 | 0.000 | 0 → 1 | 3 → 2 | 21% → 21% | 58 → 64 | 6 | 6 → 6 | 0.010 | -0.258 |
| Jogador 5 | 4-2 | 6 | 6.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 64 → 72 | 4 | 6 → 6 | 0.082 | -0.452 |
| Jogador 5 | 4-3 | 8 | 0.000 | 0.000 | 1 → 1 | 2 → 3 | 21% → 21% | 72 → 83 | 6 | 6 → 7 | 0.005 | 0.373 |
| Jogador 5 | 4-4 | 9 | 2.000 | 0.000 | 1 → 1 | 3 → 3 | 21% → 25% | 83 → 92 | 4 | 7 → 7 | 0.060 | 0.000 |
| Jogador 5 | 4-5 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 3 | 25% → 25% | 92 → 104 | 2 | 7 → 7 | -0.010 | -0.270 |
| Jogador 5 | 4-6 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 104 → 102 | 19 | 7 → 7 | -0.028 | 0.299 |
| Jogador 5 | 4-7 | 8 | 0.000 | -8.000 | 1 → 1 | 3 → 4 | 25% → 25% | 102 → 116 | 3 | 7 → 7 | 0.075 | 0.000 |
| Jogador 5 | 5-1 | 9 | 0.000 | 4.000 | 1 → 1 | 4 → 4 | 25% → 25% | 116 → 126 | 3 | 7 → 7 | -0.000 | 0.336 |
| Jogador 5 | 5-2 | 10 | 4.000 | 0.000 | 1 → 1 | 4 → 3 | 25% → 25% | 126 → 134 | 9 | 7 → 7 | -0.059 | 0.294 |
| Jogador 5 | 5-3 | 10 | -4.000 | 6.000 | 1 → 1 | 3 → 3 | 25% → 25% | 134 → 143 | 6 | 7 → 7 | 0.059 | -0.300 |
| Jogador 5 | 5-4 | 5 | -2.000 | 2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 143 → 153 | 0 | 7 → 7 | -0.154 | 0.000 |
| Jogador 5 | 5-5 | 9 | 2.000 | -4.000 | 1 → 1 | 3 → 4 | 25% → 25% | 153 → 165 | 2 | 7 → 7 | 0.048 | 0.334 |
| Jogador 5 | 5-6 | 9 | 0.000 | 4.000 | 1 → 1 | 4 → 4 | 25% → 25% | 165 → 173 | 6 | 7 → 7 | 0.038 | 0.000 |
| Jogador 5 | 5-7 | 7 | 0.000 | -4.000 | 1 → 1 | 4 → 4 | 25% → 25% | 173 → 185 | 1 | 7 → 7 | -0.048 | 0.000 |
| Jogador 5 | 6-1 | 10 | -4.000 | 2.000 | 1 → 1 | 4 → 2 | 25% → 21% | 185 → 191 | 15 | 7 → 7 | -0.007 | 0.297 |
| Jogador 5 | 6-2 | 10 | 2.000 | 6.000 | 1 → 1 | 2 → 1 | 21% → 21% | 191 → 195 | 12 | 7 → 7 | -0.005 | 0.000 |
| Jogador 5 | 6-3 | 8 | 8.000 | 4.000 | 1 → 2 | 1 → 2 | 21% → 25% | 195 → 201 | 6 | 7 → 7 | 0.040 | 0.379 |
| Jogador 5 | 6-4 | 10 | 8.000 | -14.000 | 2 → 2 | 2 → 2 | 25% → 25% | 201 → 213 | 11 | 7 → 7 | 0.009 | 0.000 |
| Jogador 5 | 6-5 | 10 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 25% → 25% | 213 → 221 | 10 | 7 → 7 | 0.000 | 0.296 |
| Jogador 5 | 6-6 | 10 | 0.000 | 2.000 | 2 → 2 | 2 → 4 | 25% → 25% | 221 → 225 | 15 | 7 → 7 | 0.012 | 0.296 |
| Jogador 5 | 6-7 | 10 | -2.000 | -2.000 | 2 → 2 | 4 → 3 | 25% → 25% | 225 → 235 | 5 | 7 → 7 | -0.059 | 0.000 |
| Jogador 5 | 7-1 | 8 | -44.000 | -42.000 | 2 → 0 | 3 → 0 | 25% → 0% | 235 → 231 | 4 | 7 → 7 | -0.094 | -0.350 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 25, COMPOSITION_COMPATIBILITY: 27, IMMEDIATE_UPGRADE: 11, PAIR_POTENTIAL: 19; mudanças de composição: 0; posicionamento melhorou em 67 ações e piorou em 54.
- Jogador 5 — estado final: ouro 231, nível 7, vida 22.0, colocação 2.
| Jogador 6 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.014 | 0.000 |
| Jogador 6 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.023 | 0.000 |
| Jogador 6 | 1-3 | 3 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 7% → 11% | 2 → 5 | 0 | 3 → 3 | -0.000 | 0.000 |
| Jogador 6 | 1-4 | 5 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 5 → 7 | 2 | 3 → 4 | -0.100 | 0.000 |
| Jogador 6 | 2-1 | 11 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 11% → 14% | 7 → 7 | 7 | 4 → 4 | -0.005 | -0.206 |
| Jogador 6 | 2-2 | 7 | 0.000 | 8.000 | 0 → 0 | 3 → 3 | 14% → 14% | 7 → 9 | 4 | 4 → 4 | 0.148 | 0.384 |
| Jogador 6 | 2-3 | 8 | 0.000 | -8.000 | 0 → 0 | 3 → 3 | 14% → 14% | 9 → 19 | 4 | 4 → 5 | -0.110 | -0.316 |
| Jogador 6 | 2-4 | 6 | 4.000 | 0.000 | 0 → 1 | 3 → 3 | 14% → 18% | 19 → 18 | 7 | 5 → 5 | 0.029 | 0.000 |
| Jogador 6 | 2-5 | 8 | 2.000 | 6.000 | 1 → 2 | 3 → 2 | 18% → 18% | 18 → 20 | 5 | 5 → 5 | 0.009 | 0.320 |
| Jogador 6 | 2-6 | 5 | 0.000 | 6.000 | 2 → 2 | 2 → 2 | 18% → 18% | 20 → 23 | 3 | 5 → 5 | -0.064 | -0.496 |
| Jogador 6 | 2-7 | 7 | 0.000 | 8.000 | 2 → 2 | 2 → 3 | 18% → 18% | 23 → 25 | 4 | 5 → 5 | 0.055 | 0.000 |
| Jogador 6 | 3-1 | 7 | 0.000 | 6.000 | 2 → 2 | 3 → 3 | 18% → 18% | 25 → 30 | 3 | 5 → 5 | 0.043 | -0.416 |
| Jogador 6 | 3-2 | 7 | 8.000 | -8.000 | 2 → 3 | 3 → 1 | 18% → 18% | 30 → 36 | 2 | 5 → 5 | -0.070 | -0.396 |
| Jogador 6 | 3-3 | 6 | 0.000 | 10.000 | 3 → 3 | 1 → 2 | 18% → 18% | 36 → 40 | 5 | 5 → 5 | -0.075 | -0.440 |
| Jogador 6 | 3-4 | 5 | 2.000 | 4.000 | 3 → 2 | 2 → 3 | 18% → 18% | 40 → 46 | 3 | 5 → 6 | 0.040 | 0.000 |
| Jogador 6 | 3-5 | 10 | 10.000 | -4.000 | 2 → 3 | 3 → 2 | 18% → 21% | 46 → 51 | 5 | 6 → 6 | 0.102 | 0.295 |
| Jogador 6 | 3-6 | 5 | 0.000 | 0.000 | 3 → 3 | 2 → 2 | 21% → 21% | 51 → 61 | 0 | 6 → 6 | 0.036 | -0.537 |
| Jogador 6 | 3-7 | 6 | 2.000 | 6.000 | 3 → 3 | 2 → 2 | 21% → 21% | 61 → 67 | 4 | 6 → 6 | -0.072 | 0.000 |
| Jogador 6 | 4-1 | 7 | -4.000 | 10.000 | 3 → 3 | 2 → 3 | 21% → 21% | 67 → 75 | 3 | 6 → 6 | 0.012 | -0.396 |
| Jogador 6 | 4-2 | 8 | 4.000 | -2.000 | 3 → 3 | 3 → 2 | 21% → 21% | 75 → 83 | 6 | 6 → 6 | -0.053 | -0.339 |
| Jogador 6 | 4-3 | 5 | 2.000 | 0.000 | 3 → 2 | 2 → 2 | 21% → 21% | 83 → 93 | 1 | 6 → 6 | 0.038 | -0.563 |
| Jogador 6 | 4-4 | 10 | 0.000 | -4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 93 → 104 | 6 | 6 → 6 | 0.060 | 0.000 |
| Jogador 6 | 4-5 | 9 | -4.000 | 4.000 | 2 → 2 | 2 → 1 | 21% → 21% | 104 → 114 | 9 | 6 → 6 | 0.054 | 0.326 |
| Jogador 6 | 4-6 | 6 | -34.000 | -46.000 | 2 → 0 | 1 → 0 | 21% → 0% | 114 → 119 | 3 | 6 → 6 | -0.207 | -0.438 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 14, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 8; mudanças de composição: 1; posicionamento melhorou em 42 ações e piorou em 38.
- Jogador 6 — estado final: ouro 119, nível 6, vida 7.0, colocação 7.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.044 | 0.000 |
| Jogador 7 | 1-3 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 11% | 3 → 5 | 1 | 3 → 3 | -0.020 | 0.000 |
| Jogador 7 | 1-4 | 7 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 5 → 7 | 2 | 3 → 4 | 0.023 | 0.000 |
| Jogador 7 | 2-1 | 8 | 2.000 | 8.000 | 0 → 0 | 2 → 2 | 11% → 14% | 7 → 7 | 5 | 4 → 4 | -0.017 | -0.283 |
| Jogador 7 | 2-2 | 9 | 6.000 | 0.000 | 0 → 0 | 2 → 1 | 14% → 14% | 7 → 9 | 4 | 4 → 4 | 0.101 | 0.264 |
| Jogador 7 | 2-3 | 8 | 2.000 | 10.000 | 0 → 0 | 1 → 1 | 14% → 14% | 9 → 9 | 7 | 4 → 4 | -0.046 | 0.336 |
| Jogador 7 | 2-4 | 6 | 2.000 | 8.000 | 0 → 0 | 1 → 1 | 14% → 18% | 9 → 6 | 9 | 4 → 5 | -0.007 | 0.000 |
| Jogador 7 | 2-5 | 9 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 12 | 4 | 5 → 5 | -0.076 | 0.287 |
| Jogador 7 | 2-6 | 10 | 0.000 | -4.000 | 0 → 0 | 1 → 2 | 18% → 18% | 12 → 10 | 14 | 5 → 5 | 0.033 | 0.254 |
| Jogador 7 | 2-7 | 9 | 6.000 | -4.000 | 0 → 0 | 2 → 3 | 18% → 21% | 10 → 11 | 8 | 5 → 6 | 0.029 | 0.000 |
| Jogador 7 | 3-1 | 7 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 11 → 15 | 4 | 6 → 6 | -0.005 | 0.433 |
| Jogador 7 | 3-2 | 9 | 0.000 | 2.000 | 0 → 0 | 3 → 3 | 21% → 21% | 15 → 11 | 13 | 6 → 6 | 0.002 | 0.328 |
| Jogador 7 | 3-3 | 10 | 2.000 | -4.000 | 0 → 0 | 3 → 4 | 21% → 18% | 11 → 9 | 13 | 6 → 6 | 0.012 | -0.268 |
| Jogador 7 | 3-4 | 9 | 8.000 | -6.000 | 0 → 0 | 4 → 4 | 18% → 25% | 9 → 6 | 11 | 6 → 7 | 0.034 | 0.000 |
| Jogador 7 | 3-5 | 6 | 0.000 | 8.000 | 0 → 0 | 4 → 6 | 25% → 25% | 6 → 8 | 4 | 7 → 7 | -0.044 | 0.469 |
| Jogador 7 | 3-6 | 6 | 0.000 | 0.000 | 0 → 0 | 6 → 6 | 25% → 25% | 8 → 7 | 8 | 7 → 7 | -0.010 | 0.469 |
| Jogador 7 | 3-7 | 5 | 0.000 | 6.000 | 0 → 0 | 6 → 7 | 25% → 25% | 7 → 10 | 3 | 7 → 7 | 0.034 | 0.000 |
| Jogador 7 | 4-1 | 10 | 0.000 | -8.000 | 0 → 0 | 7 → 5 | 25% → 25% | 10 → 21 | 2 | 7 → 7 | 0.004 | 0.293 |
| Jogador 7 | 4-2 | 5 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 25% → 25% | 21 → 30 | 0 | 7 → 7 | 0.014 | 0.577 |
| Jogador 7 | 4-3 | 6 | 0.000 | 4.000 | 0 → 0 | 5 → 5 | 25% → 25% | 30 → 36 | 4 | 7 → 7 | -0.020 | 0.472 |
| Jogador 7 | 4-4 | 6 | 6.000 | -6.000 | 0 → 1 | 5 → 4 | 25% → 25% | 36 → 43 | 3 | 7 → 7 | -0.017 | 0.000 |
| Jogador 7 | 4-5 | 5 | 0.000 | 8.000 | 1 → 1 | 4 → 4 | 25% → 25% | 43 → 52 | 4 | 7 → 7 | 0.000 | 0.577 |
| Jogador 7 | 4-6 | 6 | 0.000 | 6.000 | 1 → 1 | 4 → 5 | 25% → 25% | 52 → 63 | 3 | 7 → 7 | 0.032 | 0.467 |
| Jogador 7 | 4-7 | 6 | 0.000 | 6.000 | 1 → 1 | 5 → 5 | 25% → 25% | 63 → 73 | 3 | 7 → 7 | 0.027 | 0.000 |
| Jogador 7 | 5-1 | 6 | -4.000 | 4.000 | 1 → 0 | 5 → 5 | 25% → 25% | 73 → 83 | 0 | 7 → 7 | -0.014 | -0.467 |
| Jogador 7 | 5-2 | 5 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 25% → 25% | 83 → 94 | 0 | 7 → 7 | 0.000 | 0.601 |
| Jogador 7 | 5-3 | 10 | 10.000 | -10.000 | 0 → 2 | 5 → 3 | 25% → 25% | 94 → 100 | 7 | 7 → 7 | 0.008 | -0.280 |
| Jogador 7 | 5-4 | 5 | -2.000 | 8.000 | 2 → 2 | 3 → 3 | 25% → 25% | 100 → 107 | 3 | 7 → 7 | -0.031 | 0.000 |
| Jogador 7 | 5-5 | 9 | -6.000 | 4.000 | 2 → 1 | 3 → 4 | 25% → 25% | 107 → 121 | 5 | 7 → 7 | -0.001 | 0.323 |
| Jogador 7 | 5-6 | 7 | 0.000 | -4.000 | 1 → 1 | 4 → 5 | 25% → 25% | 121 → 136 | 2 | 7 → 7 | 0.009 | 0.422 |
| Jogador 7 | 5-7 | 10 | 2.000 | -2.000 | 1 → 1 | 5 → 5 | 25% → 25% | 136 → 147 | 0 | 7 → 7 | -0.030 | 0.000 |
| Jogador 7 | 6-1 | 10 | 6.000 | -4.000 | 1 → 2 | 5 → 6 | 25% → 25% | 147 → 150 | 12 | 7 → 8 | 0.047 | 0.299 |
| Jogador 7 | 6-2 | 9 | 6.000 | 0.000 | 2 → 2 | 6 → 6 | 25% → 29% | 150 → 159 | 5 | 8 → 8 | 0.003 | 0.339 |
| Jogador 7 | 6-3 | 10 | 2.000 | 2.000 | 2 → 3 | 6 → 6 | 29% → 29% | 159 → 165 | 10 | 8 → 8 | -0.019 | 0.000 |
| Jogador 7 | 6-4 | 10 | 0.000 | 4.000 | 3 → 3 | 6 → 6 | 29% → 29% | 165 → 174 | 2 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 6-5 | 4 | -4.000 | 4.000 | 3 → 2 | 6 → 6 | 29% → 29% | 174 → 184 | 0 | 8 → 8 | -0.013 | -0.688 |
| Jogador 7 | 6-6 | 5 | 0.000 | 0.000 | 2 → 2 | 6 → 6 | 29% → 29% | 184 → 195 | 0 | 8 → 8 | 0.000 | -0.550 |
| Jogador 7 | 6-7 | 10 | -2.000 | 0.000 | 2 → 1 | 6 → 6 | 29% → 29% | 195 → 208 | 3 | 8 → 8 | -0.008 | 0.000 |
| Jogador 7 | 7-1 | 6 | 0.000 | 0.000 | 1 → 1 | 6 → 6 | 29% → 29% | 208 → 209 | 0 | 8 → 8 | 0.000 | 0.504 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 11, COMPOSITION_COMPATIBILITY: 14, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 19; mudanças de composição: 0; posicionamento melhorou em 68 ações e piorou em 67.
- Jogador 7 — estado final: ouro 209, nível 8, vida 17.0, colocação 1.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.150 | 0.000 |
| Jogador 8 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 8 | 1-3 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 4 | 1 | 3 → 3 | 0.003 | 0.000 |
| Jogador 8 | 1-4 | 10 | 0.000 | 6.000 | 0 → 0 | 0 → 2 | 11% → 11% | 4 → 5 | 3 | 3 → 4 | 0.050 | 0.000 |
| Jogador 8 | 2-1 | 11 | 4.000 | 2.000 | 0 → 1 | 2 → 0 | 11% → 14% | 5 → 6 | 5 | 4 → 4 | -0.044 | 0.216 |
| Jogador 8 | 2-2 | 9 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 14% → 14% | 6 → 5 | 10 | 4 → 4 | -0.000 | -0.257 |
| Jogador 8 | 2-3 | 8 | 0.000 | 2.000 | 1 → 1 | 0 → 2 | 14% → 14% | 5 → 10 | 6 | 4 → 5 | 0.062 | 0.314 |
| Jogador 8 | 2-4 | 6 | 6.000 | 8.000 | 1 → 1 | 2 → 2 | 14% → 18% | 10 → 8 | 7 | 5 → 5 | -0.082 | 0.000 |
| Jogador 8 | 2-5 | 8 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 18% → 18% | 8 → 11 | 3 | 5 → 5 | 0.045 | -0.290 |
| Jogador 8 | 2-6 | 9 | 0.000 | 10.000 | 1 → 1 | 2 → 3 | 18% → 18% | 11 → 13 | 7 | 5 → 5 | -0.024 | 0.293 |
| Jogador 8 | 2-7 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 18% → 18% | 13 → 20 | 8 | 5 → 5 | 0.020 | 0.000 |
| Jogador 8 | 3-1 | 10 | 4.000 | 0.000 | 1 → 0 | 3 → 3 | 18% → 18% | 20 → 17 | 14 | 5 → 5 | 0.014 | -0.263 |
| Jogador 8 | 3-2 | 10 | 0.000 | 0.000 | 0 → 0 | 3 → 4 | 18% → 18% | 17 → 11 | 17 | 5 → 6 | 0.005 | -0.286 |
| Jogador 8 | 3-3 | 9 | 6.000 | -4.000 | 0 → 0 | 4 → 4 | 18% → 21% | 11 → 7 | 12 | 6 → 6 | -0.012 | 0.317 |
| Jogador 8 | 3-4 | 6 | 0.000 | 10.000 | 0 → 0 | 4 → 4 | 21% → 21% | 7 → 7 | 5 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-5 | 8 | 0.000 | 2.000 | 0 → 0 | 4 → 5 | 21% → 21% | 7 → 8 | 7 | 6 → 6 | 0.053 | -0.329 |
| Jogador 8 | 3-6 | 9 | 4.000 | -4.000 | 0 → 0 | 5 → 5 | 21% → 25% | 8 → 6 | 11 | 6 → 7 | -0.003 | 0.329 |
| Jogador 8 | 3-7 | 5 | 0.000 | 6.000 | 0 → 0 | 5 → 5 | 25% → 25% | 6 → 8 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-1 | 8 | 0.000 | 0.000 | 0 → 0 | 5 → 6 | 25% → 25% | 8 → 15 | 3 | 7 → 7 | -0.076 | 0.345 |
| Jogador 8 | 4-2 | 6 | 0.000 | -6.000 | 0 → 0 | 6 → 5 | 25% → 25% | 15 → 21 | 3 | 7 → 7 | 0.012 | -0.452 |
| Jogador 8 | 4-3 | 10 | 0.000 | 12.000 | 0 → 0 | 5 → 4 | 25% → 25% | 21 → 5 | 21 | 7 → 7 | -0.013 | 0.000 |
| Jogador 8 | 4-4 | 7 | 0.000 | -8.000 | 0 → 0 | 4 → 4 | 25% → 25% | 5 → 14 | 4 | 7 → 7 | 0.009 | 0.000 |
| Jogador 8 | 4-5 | 9 | 6.000 | 6.000 | 0 → 1 | 4 → 3 | 25% → 25% | 14 → 13 | 7 | 7 → 7 | 0.022 | -0.302 |
| Jogador 8 | 4-6 | 10 | 4.000 | 2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 13 → 7 | 15 | 7 → 7 | -0.035 | -0.283 |
| Jogador 8 | 4-7 | 4 | 4.000 | -4.000 | 1 → 1 | 3 → 3 | 25% → 25% | 7 → 13 | 0 | 7 → 7 | -0.015 | 0.000 |
| Jogador 8 | 5-1 | 8 | 0.000 | 0.000 | 1 → 1 | 3 → 2 | 25% → 25% | 13 → 17 | 3 | 7 → 7 | 0.008 | -0.356 |
| Jogador 8 | 5-2 | 5 | -44.000 | -48.000 | 1 → 0 | 2 → 0 | 25% → 0% | 17 → 17 | 0 | 7 → 7 | -0.096 | -0.560 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 15, COMPOSITION_COMPATIBILITY: 17, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 13; mudanças de composição: 1; posicionamento melhorou em 45 ações e piorou em 37.
- Jogador 8 — estado final: ouro 17, nível 7, vida 5.0, colocação 6.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 56 | 23 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| Jogador 2 | 54 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 3 | 39 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 4 | 28 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 5 | 82 | 45 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 |
| Jogador 6 | 38 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| Jogador 7 | 54 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 8 | 55 | 22 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |
- Jogador 1 — venda DA_18_Akali_AD (3-2, step 133): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Caitlyn (4-2, step 202): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Shen (4-5, step 232): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Cassiopeia (4-7, step 254): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_MasterYi_AD (3-6, step 174): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rakan (4-7, step 253): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_LeBlanc (4-7, step 256): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Diana (5-4, step 292): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_18_Veigar (5-6, step 313): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_18_Yorick (4-2, step 202): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Tristana (4-3, step 212): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 3 — venda DA_18_RekSai (4-5, step 234): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Camille (3-6, step 172): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_18_Camille (4-2, step 202): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (3-5, step 162): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Yorick (3-6, step 172): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Kobuko (5-2, step 274): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_Kobuko (5-2, step 279): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Warwick (5-3, step 284): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Warwick (6-5, step 380): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Leona (6-7, step 395): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 6 — venda DA_18_Sentry (4-4, step 226): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Varus (2-5, step 94): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Akali_AD (2-6, step 102): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Camille (3-4, step 154): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 7 — venda DA_18_Rammus (4-1, step 194): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 7 — venda DA_18_Alistar (4-1, step 196): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_18_Alistar (6-2, step 342): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_18_Warwick (2-7, step 118): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Leona (3-1, step 126): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_18_Rakan (4-6, step 243): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.

Vendas de core/pares ignoradas antes da decisão da composição: **1**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 3-2 | 133 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-2 | 202 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-5 | 232 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Shen' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-7 | 254 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 3-3 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-3 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-3 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-3 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-3 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-3 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-3 | 148 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-3 | 149 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-3 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-3 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-4 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-4 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-4 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-4 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-4 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-4 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-5 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-5 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-5 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-5 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-5 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-5 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-5 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-5 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-2 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 217 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 218 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 226 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 238 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 239 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 248 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 249 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 250 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 253 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 254 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 255 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 256 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 257 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 258 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 261 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 262 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 263 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 264 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 265 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 266 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 1 | 5-2 | 279 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 1 | 5-4 | 301 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 302 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 303 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 304 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 305 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 306 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 307 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 308 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 309 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 310 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 311 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 312 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 313 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 314 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 315 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 316 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 317 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 321 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 322 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 323 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 324 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 325 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 326 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 327 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 331 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 332 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 333 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 334 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 335 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 336 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 341 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 342 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 343 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 344 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 345 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 346 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 347 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 348 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 349 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 350 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 351 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 352 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 353 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 354 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 355 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 356 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 361 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 1-4 | 282 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 966 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1051 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1137 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1138 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1262 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-2 | 1263 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1394 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-3 | 1395 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1482 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-4 | 1483 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1592 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-5 | 1593 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1702 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-6 | 1703 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 1825 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-7 | 1826 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 1958 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-1 | 1959 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 2047 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 2048 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-3 | 2158 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-3 | 2159 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 2248 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 2372 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-6 | 2504 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-6 | 2505 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-7 | 2614 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-7 | 2615 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-1 | 2755 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-2 | 2881 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-2 | 2882 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-3 | 3024 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-3 | 3025 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-4 | 3136 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-4 | 3137 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-5 | 3271 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-5 | 3272 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-6 | 3373 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-6 | 3374 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-7 | 3471 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-7 | 3472 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-1 | 3560 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-1 | 3561 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-2 | 3704 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-2 | 3705 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-3 | 3796 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 6-3 | 3797 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 2-5 | 943 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 2-6 | 1028 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 2-7 | 1114 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 3-1 | 1239 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-4 | 3176 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-4 | 3199 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-4 | 3211 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-4 | 3223 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-4 | 3235 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-4 | 3247 | FAST8_REROLL_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-6 | 174 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 4-7 | 253 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 4-7 | 256 | SOLD_CORE_UNIT | Venda de 'DA_18_LeBlanc' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 2 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 45 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-3 | 187 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 2-1 | 419 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-2 | 528 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-6 | 927 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-6 | 928 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 2-7 | 1027 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-7 | 1028 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-1 | 1152 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-1 | 1153 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-2 | 1224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-2 | 1225 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-3 | 1321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-4 | 1409 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-5 | 1491 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-5 | 1492 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-6 | 1620 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-6 | 1621 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-7 | 1732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-7 | 1733 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-1 | 1822 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-1 | 1823 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-2 | 1899 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-2 | 1900 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 1986 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-3 | 1987 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 2063 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-4 | 2064 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2149 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-5 | 2150 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 2288 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 2424 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 2561 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 2624 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-3 | 2724 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-4 | 2840 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-5 | 2941 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-5 | 2942 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-6 | 3079 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-6 | 3080 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-7 | 3219 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-7 | 3220 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-1 | 3365 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 6-1 | 3366 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 5-2 | 2701 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-3 | 2817 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-4 | 2918 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 3 | 4-2 | 202 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
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
| LOW | Jogador 3 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 248 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-3 | 186 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 1-4 | 233 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-1 | 304 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-2 | 351 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-3 | 425 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-6 | 674 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 877 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-1 | 878 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 975 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-3 | 1070 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1142 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1225 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 1337 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 1420 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 1532 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-1 | 1533 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 1657 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-3 | 1790 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-4 | 1923 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-5 | 2048 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-6 | 2889 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 5-6 | 2890 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 2-2 | 402 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-4 | 580 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-5 | 651 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-6 | 758 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-7 | 854 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-1 | 952 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-2 | 1047 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-3 | 1119 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-4 | 1202 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-5 | 1314 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-2 | 2584 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-3 | 2697 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 5-4 | 2793 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 4 | 4-2 | 202 | SOLD_CORE_UNIT | Venda de 'DA_18_Camille' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 2-3 | 515 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 2-4 | 601 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 2-5 | 676 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 2-6 | 735 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 2-7 | 835 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-1 | 937 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-2 | 1077 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-3 | 1190 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-4 | 1266 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-5 | 1407 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-6 | 1518 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 1615 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-1 | 1749 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 1838 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-2 | 1839 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 2-4 | 653 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-5 | 712 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-6 | 812 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-7 | 914 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-1 | 1054 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-2 | 1167 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-3 | 1243 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-5 | 1495 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 5 | 3-5 | 162 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-2 | 279 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-3 | 284 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 6-5 | 380 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 2-1 | 60 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 61 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 69 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 70 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 78 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 79 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 107 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-4 | 366 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-4 | 367 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-4 | 368 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-4 | 369 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-4 | 370 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-4 | 371 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-5 | 372 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-5 | 373 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-5 | 374 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-5 | 375 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-5 | 376 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-5 | 377 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-5 | 378 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-5 | 379 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-5 | 380 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-5 | 381 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-6 | 382 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-6 | 383 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-6 | 384 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-6 | 385 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-6 | 386 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-6 | 387 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-6 | 388 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-6 | 389 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-6 | 390 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-6 | 391 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-7 | 392 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-7 | 393 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-7 | 394 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-7 | 395 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-7 | 396 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-7 | 397 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-7 | 398 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-7 | 399 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-7 | 400 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-7 | 401 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 7-1 | 402 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 7-1 | 403 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 7-1 | 404 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 7-1 | 405 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 7-1 | 406 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 7-1 | 407 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 7-1 | 408 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 7-1 | 411 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-1 | 380 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-1 | 381 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-2 | 467 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 746 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-1 | 1075 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1202 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1203 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-3 | 1338 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-3 | 1339 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-4 | 1441 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-4 | 1442 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-5 | 1553 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1554 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-6 | 1695 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1696 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-7 | 1828 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-1 | 1966 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 2052 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 2053 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-3 | 2167 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2168 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-4 | 2295 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-4 | 2296 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-5 | 2434 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-5 | 2435 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 2571 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-6 | 2572 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-7 | 2683 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-7 | 2684 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 2808 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-1 | 2809 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-2 | 2947 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-2 | 2948 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 3085 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-3 | 3086 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-4 | 3159 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-4 | 3160 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-5 | 3281 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-5 | 3282 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-6 | 3407 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-6 | 3408 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-7 | 3507 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-7 | 3508 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-1 | 3645 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-2 | 3782 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-3 | 3897 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-4 | 4039 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-5 | 4176 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-6 | 4312 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-7 | 4452 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 6-7 | 4453 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 7-1 | 4572 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 7-1 | 4573 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 2-5 | 819 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-6 | 956 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-7 | 1052 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-1 | 1179 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-3 | 1418 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-4 | 1530 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-6 | 2660 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-7 | 2785 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 5-2 | 3062 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 2-3 | 82 | PURCHASE_SALE_REVIEW | Compra de DA_Gromp18_AP foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 6 | 4-4 | 226 | SOLD_CORE_UNIT | Venda de 'DA_18_Sentry' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 2-2 | 70 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 75 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 78 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 79 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 207 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 208 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 238 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 239 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 1-2 | 115 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 1-3 | 162 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 1-4 | 234 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-1 | 382 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 589 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 673 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-5 | 784 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-6 | 858 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 959 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1160 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1247 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1322 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1323 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-5 | 1463 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1464 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-7 | 1623 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1624 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-1 | 1726 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 1727 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 1840 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 1841 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 1917 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 1918 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 2059 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-5 | 2180 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-6 | 2270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 4-6 | 2271 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 2-4 | 761 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-5 | 835 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-6 | 936 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-7 | 1035 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-1 | 1137 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-2 | 1224 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-3 | 1299 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-1 | 1817 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 7 | 2-5 | 94 | SOLD_CORE_UNIT | Venda de 'DA_18_Varus' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 2-6 | 102 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-2 | 103 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-3 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 259 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 366 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 489 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-3 | 602 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-4 | 687 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-5 | 813 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-5 | 814 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-6 | 944 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-7 | 1064 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1287 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1419 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1539 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1626 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1710 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-6 | 1711 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 1785 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-7 | 1786 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 1923 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2000 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2089 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2182 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-4 | 2183 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2258 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-5 | 2259 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2348 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2436 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 2525 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-2 | 2599 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-3 | 2748 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-4 | 2822 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-5 | 2957 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-6 | 3061 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-7 | 3208 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-7 | 3209 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-1 | 3349 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-2 | 3478 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-3 | 3622 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-4 | 3774 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-5 | 3838 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-6 | 3918 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-7 | 4066 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 7-1 | 4156 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| MEDIUM | Jogador 7 | 6-5 | 3895 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-7 | 118 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 2-1 | 59 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-1 | 60 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-1 | 61 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-1 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-1 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-1 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-1 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-1 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-1 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-1 | 68 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-1 | 69 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-2 | 70 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-2 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 2-2 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 2-1 | 456 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-2 | 575 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 776 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 2-5 | 885 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 2-6 | 1014 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-6 | 1015 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 2-7 | 1148 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1149 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-1 | 1282 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1283 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-2 | 1415 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-2 | 1416 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-3 | 1536 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1537 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-4 | 1621 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-4 | 1622 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-5 | 1736 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-6 | 1855 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-7 | 1928 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 2043 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 2044 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2132 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-2 | 2133 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2268 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 2269 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 2367 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-4 | 2368 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 2496 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-5 | 2497 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-6 | 2634 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-6 | 2635 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-7 | 2698 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-7 | 2699 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-1 | 2816 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-2 | 2896 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 5-2 | 2897 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
