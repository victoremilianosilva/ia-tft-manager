# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **5321**
- Achados: **859**
- CRITICAL: 0 | HIGH: 13 | MEDIUM: 76 | LOW: 770

## Metadados da sessão

- Match ID: b971a2dd-826d-4aad-95f8-46efc2e514f5
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 3d63262fb93d7504bfc05b4e6efd43b7d3bf9e722c0407b8e8b1bd7903bc856d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4470**
- Entradas posteriores à eliminação ignoradas: **851**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 86 | 7 | 8 | 8 | 73 | 3 | 2 | não/inconclusivo | 0 |
| Jogador 6 | 78 | 7 | 12 | 4 | 71 | 3 | 1 | não/inconclusivo | 0 |
| Jogador 7 | 190 | 7 | 12 | 16 | 70 | 4 | 2 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 183 | 62 | 35 | 8 | 1 | 15 | 57 | 0.0796 | 7 | 28 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 13, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 4, ALL_IN::PASS: 1, ALL_IN::SELL: 8, STABILIZE::BUY: 49, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 38, STABILIZE::PASS: 14, STABILIZE::REROLL: 1, STABILIZE::SELL: 27
- Jogador 1 — recompensas por ação: BUY: média 0.2586 (n=62), BUY_XP: média -0.0350 (n=8), ITEM: média 0.2040 (n=5), MOVE_BENCH: média 0.1487 (n=15), MOVE_BOARD: média 0.0033 (n=42), PASS: média -0.0320 (n=15), REROLL: média -0.1600 (n=1), SELL: média -0.1126 (n=35)
| Jogador 2 | 332 | 125 | 89 | 24 | 0 | 17 | 63 | 0.0543 | 13 | 36 |
- Jogador 2 — ações por estratégia: STABILIZE::BUY: 125, STABILIZE::BUY_XP: 24, STABILIZE::ITEM: 14, STABILIZE::MOVE_BENCH: 20, STABILIZE::MOVE_BOARD: 43, STABILIZE::PASS: 17, STABILIZE::SELL: 89
- Jogador 2 — recompensas por ação: BUY: média 0.2643 (n=125), BUY_XP: média -0.0033 (n=24), ITEM: média 0.1450 (n=14), MOVE_BENCH: média 0.1580 (n=20), MOVE_BOARD: média -0.0095 (n=43), PASS: média -0.0359 (n=17), SELL: média -0.2145 (n=89)
| Jogador 3 | 272 | 79 | 39 | 16 | 0 | 31 | 98 | 0.0806 | 4 | 47 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 6, ALL_IN::ITEM: 1, ALL_IN::MOVE_BOARD: 3, ALL_IN::PASS: 1, ALL_IN::SELL: 6, FAST8::BUY: 21, FAST8::BUY_XP: 4, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 10, FAST8::MOVE_BOARD: 33, FAST8::PASS: 14, FAST8::SELL: 10, STABILIZE::BUY: 52, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 4, STABILIZE::MOVE_BENCH: 20, STABILIZE::MOVE_BOARD: 32, STABILIZE::PASS: 16, STABILIZE::SELL: 23
- Jogador 3 — recompensas por ação: BUY: média 0.3230 (n=79), BUY_XP: média -0.0294 (n=16), ITEM: média 0.1756 (n=9), MOVE_BENCH: média 0.0717 (n=30), MOVE_BOARD: média -0.0050 (n=68), PASS: média -0.0800 (n=31), SELL: média -0.1036 (n=39)
| Jogador 4 | 196 | 73 | 39 | 8 | 4 | 13 | 46 | 0.1006 | 8 | 29 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 6, ALL_IN::ITEM: 5, ALL_IN::MOVE_BENCH: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 4, STABILIZE::BUY: 67, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 30, STABILIZE::PASS: 13, STABILIZE::REROLL: 2, STABILIZE::SELL: 35
- Jogador 4 — recompensas por ação: BUY: média 0.3663 (n=73), BUY_XP: média -0.0288 (n=8), ITEM: média 0.1585 (n=13), MOVE_BENCH: média 0.1062 (n=16), MOVE_BOARD: média -0.0070 (n=30), PASS: média -0.0100 (n=13), REROLL: média -0.1350 (n=4), SELL: média -0.2480 (n=39)
| Jogador 5 | 186 | 84 | 58 | 6 | 4 | 8 | 21 | 0.0660 | 10 | 17 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 13, ALL_IN::MOVE_BENCH: 1, ALL_IN::REROLL: 3, ALL_IN::SELL: 10, STABILIZE::BUY: 71, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 7, STABILIZE::PASS: 8, STABILIZE::REROLL: 1, STABILIZE::SELL: 48
- Jogador 5 — recompensas por ação: BUY: média 0.2556 (n=84), BUY_XP: média -0.0183 (n=6), ITEM: média 0.1820 (n=5), MOVE_BENCH: média 0.1579 (n=14), MOVE_BOARD: média 0.0543 (n=7), PASS: média -0.0075 (n=8), REROLL: média -0.0925 (n=4), SELL: média -0.2097 (n=58)
| Jogador 6 | 202 | 71 | 44 | 12 | 2 | 15 | 45 | 0.0642 | 13 | 35 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 9, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 1, ALL_IN::SELL: 6, STABILIZE::BUY: 62, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 11, STABILIZE::MOVE_BENCH: 12, STABILIZE::MOVE_BOARD: 32, STABILIZE::PASS: 15, STABILIZE::REROLL: 2, STABILIZE::SELL: 38
- Jogador 6 — recompensas por ação: BUY: média 0.2496 (n=71), BUY_XP: média -0.0408 (n=12), ITEM: média 0.1423 (n=13), MOVE_BENCH: média 0.0808 (n=13), MOVE_BOARD: média -0.0050 (n=32), PASS: média -0.0060 (n=15), REROLL: média -0.1850 (n=2), SELL: média -0.1489 (n=44)
| Jogador 7 | 243 | 70 | 33 | 12 | 2 | 29 | 87 | 0.0903 | 5 | 28 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 9, ALL_IN::MOVE_BENCH: 2, ALL_IN::MOVE_BOARD: 1, ALL_IN::REROLL: 1, ALL_IN::SELL: 5, FAST8::BUY: 28, FAST8::ITEM: 5, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 50, FAST8::PASS: 19, FAST8::SELL: 13, STABILIZE::BUY: 33, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 8, STABILIZE::MOVE_BOARD: 24, STABILIZE::PASS: 10, STABILIZE::REROLL: 1, STABILIZE::SELL: 15
- Jogador 7 — recompensas por ação: BUY: média 0.4243 (n=70), BUY_XP: média -0.0308 (n=12), ITEM: média 0.1390 (n=10), MOVE_BENCH: média 0.2633 (n=12), MOVE_BOARD: média -0.0059 (n=75), PASS: média -0.0579 (n=29), REROLL: média -0.1150 (n=2), SELL: média -0.2903 (n=33)
| Jogador 8 | 205 | 83 | 55 | 4 | 2 | 10 | 41 | 0.0466 | 3 | 44 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 12, ALL_IN::ITEM: 2, ALL_IN::MOVE_BOARD: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 10, STABILIZE::BUY: 71, STABILIZE::BUY_XP: 4, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 27, STABILIZE::MOVE_BOARD: 13, STABILIZE::PASS: 10, STABILIZE::SELL: 45
- Jogador 8 — recompensas por ação: BUY: média 0.2670 (n=83), BUY_XP: média -0.0350 (n=4), ITEM: média 0.1810 (n=10), MOVE_BENCH: média -0.0500 (n=27), MOVE_BOARD: média -0.0186 (n=14), PASS: média -0.0450 (n=10), REROLL: média -0.0700 (n=2), SELL: média -0.2196 (n=55)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 12:12:44 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | ? | 12:12:46 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | ? | 12:12:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 12:12:51 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 12:12:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 12:12:52 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-1 | 12:12:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 12:12:54 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 12:12:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 12:12:56 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 1-2 | 12:12:59 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-2 | 12:12:59 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 12:13:00 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 12:13:00 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-2 | 12:13:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 12:13:07 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 12:13:07 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 12:13:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 12:13:17 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 12:13:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-4 | 12:13:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-1 | 12:13:26 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 12:13:26 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.1300 |  |
| Jogador 1 | 2-1 | 12:13:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 12:13:28 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-1 | 12:13:28 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.2800 |  |
| Jogador 1 | 2-1 | 12:13:28 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 12:13:29 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1700 |  |
| Jogador 1 | 2-1 | 12:13:29 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-1 | 12:13:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-2 | 12:13:36 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 1 | 2-2 | 12:13:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 12:13:37 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-2 | 12:13:38 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1800 |  |
| Jogador 1 | 2-2 | 12:13:38 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 1 | 2-2 | 12:13:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 12:13:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 12:13:49 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 2-3 | 12:13:49 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3600 |  |
| Jogador 1 | 2-3 | 12:13:50 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 2-3 | 12:13:51 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 12:13:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 12:13:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-4 | 12:14:03 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Ornn | 1.0200 |  |
| Jogador 1 | 2-4 | 12:14:03 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Ornn | 0.3300 |  |
| Jogador 1 | 2-4 | 12:14:04 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 1 | 2-4 | 12:14:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 2-4 | 12:14:05 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 12:14:06 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 2-4 | 12:14:06 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 12:14:06 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 2-4 | 12:14:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 12:14:18 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 2-5 | 12:14:19 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 2-5 | 12:14:19 | MOVE Bench -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 1 | 2-5 | 12:14:20 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 1 | 2-5 | 12:14:20 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 2-5 | 12:14:21 | MOVE Board -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 12:14:21 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 12:14:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 12:14:35 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 2-6 | 12:14:35 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 1 | 2-6 | 12:14:36 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 1 | 2-6 | 12:14:36 | MOVE Bench -> Board: Shen (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 1 | 2-6 | 12:14:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 12:14:53 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | 0.2600 |  |
| Jogador 1 | 2-7 | 12:14:54 | MOVE Bench -> Board: Shen (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 1 | 2-7 | 12:14:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 1 | 2-7 | 12:14:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 2-7 | 12:14:55 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 12:14:56 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 2-7 | 12:14:56 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 2-7 | 12:14:57 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-7 | 12:14:57 | MOVE Board -> Board: Akali (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-1 | 12:15:13 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-1 | 12:15:14 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 12:15:14 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 3-1 | 12:15:15 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 3-1 | 12:15:15 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 12:15:16 | MOVE Board -> Board: Shen (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 12:15:16 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 12:15:17 | MOVE Board -> Board: Shen (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-1 | 12:15:17 | MOVE Board -> Board: Rakan (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 12:15:34 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-2 | 12:15:35 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-2 | 12:15:35 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 12:15:36 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 3-2 | 12:15:36 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.1800 |  |
| Jogador 1 | 3-2 | 12:15:36 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-2 | 12:15:37 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-2 | 12:15:37 | MOVE Board -> Board: Akali (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 3-2 | 12:15:38 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-3 | 12:15:57 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-3 | 12:15:57 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 12:15:58 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 12:15:59 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 3-3 | 12:15:59 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-3 | 12:15:59 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.3700 |  |
| Jogador 1 | 3-3 | 12:16:00 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 12:16:00 | MOVE Board -> Board: Akali (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 12:16:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-4 | 12:16:22 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Inferno | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 1 | 3-4 | 12:16:23 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Inferno | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 1 | 3-4 | 12:16:24 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-4 | 12:16:24 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.4400 |  |
| Jogador 1 | 3-4 | 12:16:25 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 1 | 3-4 | 12:16:25 | MOVE Board -> Board: Grompe (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-4 | 12:16:26 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 3-4 | 12:16:26 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 3-4 | 12:16:26 | MOVE Board -> Board: Grompe (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-5 | 12:16:50 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 1 | 3-5 | 12:16:51 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Inferno | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 1 | 3-5 | 12:16:51 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 1 | 3-5 | 12:16:52 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-5 | 12:16:52 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Inferno | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 1 | 3-5 | 12:16:53 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-5 | 12:16:54 | MOVE Board -> Board: Akali (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-5 | 12:16:54 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-5 | 12:16:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-6 | 12:17:21 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-6 | 12:17:22 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-6 | 12:17:22 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-6 | 12:17:23 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-6 | 12:17:23 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-6 | 12:17:24 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-6 | 12:17:24 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-6 | 12:17:24 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 3-6 | 12:17:25 | MOVE Board -> Board: Grompe (i:4.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-7 | 12:17:54 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Inferno | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 1 | 3-7 | 12:17:55 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Inferno | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 1 | 3-7 | 12:17:56 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-7 | 12:17:56 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-7 | 12:17:57 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 3-7 | 12:17:57 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 3-7 | 12:17:59 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Inferno | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 3-7 | 12:17:59 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Inferno | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 3-7 | 12:18:00 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Inferno | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 1 | 4-1 | 12:18:34 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Inferno | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 1 | 4-1 | 12:18:35 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 4-1 | 12:18:36 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Inferno | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 4-1 | 12:18:37 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Inferno | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 4-1 | 12:18:37 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Inferno | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 1 | 4-1 | 12:18:38 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 12:18:38 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-1 | 12:18:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Inferno | DA_KogMaw18_AD | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-2 | 12:19:19 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Inferno | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 4-2 | 12:19:20 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 52 | 4 | Inferno | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 1 | 4-2 | 12:19:21 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 49 | 4 | Inferno | DA_KogMaw18_AD | -0.3100 |  |
| Jogador 1 | 4-2 | 12:19:21 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 48 | 4 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-2 | 12:19:22 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Inferno | DA_KogMaw18_AD | -0.5100 |  |
| Jogador 1 | 4-2 | 12:19:22 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 52 | 4 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 4-2 | 12:19:23 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-2 | 12:19:23 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Inferno | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 1 | 4-2 | 12:19:24 | REROLL | STABILIZE | STABILIZE: pressão de vida | 52 | 4 | Inferno | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 1 | 4-3 | 12:20:00 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Inferno | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 1 | 4-3 | 12:20:00 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 4-3 | 12:20:01 | VENDEU: Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 59 | 5 | Inferno | DA_KogMaw18_AD | -0.5500 |  |
| Jogador 1 | 4-3 | 12:20:02 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 55 | 5 | Inferno | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 1 | 4-3 | 12:20:02 | MOVE Bench -> Board: Malphite (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 55 | 5 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 4-3 | 12:20:03 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 5 | Inferno | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 1 | 4-3 | 12:20:04 | MOVE Board -> Board: Malphite (i:8.0) <-> Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-3 | 12:20:04 | MOVE Board -> Board: Grompe (i:4.0) <-> Akali (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 51 | 5 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-3 | 12:20:05 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 51 | 5 | Inferno | DA_KogMaw18_AD | -0.4400 |  |
| Jogador 1 | 4-4 | 12:20:49 | VENDEU: Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 4-4 | 12:20:50 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Inferno | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 1 | 4-4 | 12:20:51 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-4 | 12:20:51 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 4-4 | 12:20:52 | VENDEU: Kayle (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-4 | 12:20:52 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Inferno | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 1 | 4-4 | 12:20:53 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Inferno | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 4-4 | 12:20:53 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Inferno | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 1 | 4-4 | 12:20:54 | MOVE Board -> Board: Akali (i:4.0) <-> Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-5 | 12:21:48 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-5 | 12:21:48 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Inferno | DA_KogMaw18_AD | 0.5400 |  |
| Jogador 1 | 4-5 | 12:21:49 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-5 | 12:21:49 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Inferno | DA_KogMaw18_AD | 0.8200 |  |
| Jogador 1 | 4-5 | 12:21:50 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Inferno | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 1 | 4-5 | 12:21:51 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Inferno | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 1 | 4-5 | 12:21:51 | VENDEU: Rengar (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Inferno | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 4-5 | 12:21:52 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Inferno | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 1 | 4-5 | 12:21:52 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 2 | ? | 12:12:44 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | ? | 12:12:46 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | ? | 12:12:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 12:12:51 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 12:12:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 12:12:52 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 1-1 | 12:12:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 12:12:56 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 1-2 | 12:12:59 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 12:12:59 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 12:13:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 12:13:04 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 12:13:07 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 12:13:07 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 12:13:09 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-3 | 12:13:09 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-3 | 12:13:10 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 12:13:10 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 12:13:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 12:13:17 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 12:13:18 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 12:13:18 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 1-4 | 12:13:19 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 1-4 | 12:13:19 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-4 | 12:13:20 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 1-4 | 12:13:20 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 12:13:26 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 2-1 | 12:13:26 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 2-1 | 12:13:27 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-1 | 12:13:28 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-1 | 12:13:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 12:13:28 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 12:13:29 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-1 | 12:13:29 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-1 | 12:13:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 12:13:36 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-2 | 12:13:36 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 2-2 | 12:13:37 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-2 | 12:13:38 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-2 | 12:13:38 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-2 | 12:13:39 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-2 | 12:13:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-2 | 12:13:40 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 2-2 | 12:13:40 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 12:13:49 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 2-3 | 12:13:49 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1400 |  |
| Jogador 2 | 2-3 | 12:13:50 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 12:13:51 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 12:13:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-4 | 12:14:03 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.3400 |  |
| Jogador 2 | 2-4 | 12:14:03 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 2-4 | 12:14:04 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-4 | 12:14:04 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.3400 |  |
| Jogador 2 | 2-4 | 12:14:05 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 2-4 | 12:14:06 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 12:14:06 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.6400 |  |
| Jogador 2 | 2-4 | 12:14:06 | MOVE Bench -> Board: Vi (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 2-4 | 12:14:07 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.4100 |  |
| Jogador 2 | 2-5 | 12:14:18 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.9000 |  |
| Jogador 2 | 2-5 | 12:14:19 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 2-5 | 12:14:19 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-5 | 12:14:20 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 12:14:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 12:14:21 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-5 | 12:14:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 12:14:22 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 12:14:22 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.3400 |  |
| Jogador 2 | 2-6 | 12:14:35 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | 0.6300 |  |
| Jogador 2 | 2-6 | 12:14:35 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 2-6 | 12:14:36 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 2-6 | 12:14:36 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-6 | 12:14:37 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-6 | 12:14:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-6 | 12:14:38 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 2-6 | 12:14:38 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-6 | 12:14:39 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 12:14:53 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 2-7 | 12:14:54 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 2-7 | 12:14:54 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 2-7 | 12:14:55 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 2-7 | 12:14:55 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 2-7 | 12:14:56 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.4600 |  |
| Jogador 2 | 2-7 | 12:14:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 12:14:57 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 2-7 | 12:14:57 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 3-1 | 12:15:13 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 3-1 | 12:15:14 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 3-1 | 12:15:14 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-1 | 12:15:15 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 12:15:15 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.4300 |  |
| Jogador 2 | 3-1 | 12:15:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 12:15:16 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-1 | 12:15:17 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.2100 |  |
| Jogador 2 | 3-1 | 12:15:17 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 3-2 | 12:15:34 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-2 | 12:15:35 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-2 | 12:15:35 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-2 | 12:15:36 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 3-2 | 12:15:36 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 3-2 | 12:15:36 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | -0.3500 |  |
| Jogador 2 | 3-2 | 12:15:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 12:15:37 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.4900 |  |
| Jogador 2 | 3-2 | 12:15:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 12:15:57 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 12:15:57 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.4500 |  |
| Jogador 2 | 3-3 | 12:15:58 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.2600 |  |
| Jogador 2 | 3-3 | 12:15:59 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-3 | 12:15:59 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | -0.7900 |  |
| Jogador 2 | 3-3 | 12:15:59 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-3 | 12:16:00 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 12:16:00 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Veigar | -0.5700 |  |
| Jogador 2 | 3-3 | 12:16:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-4 | 12:16:22 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-4 | 12:16:23 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 3-4 | 12:16:24 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 3-4 | 12:16:24 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-4 | 12:16:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-4 | 12:16:25 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 3-4 | 12:16:26 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 3-4 | 12:16:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-4 | 12:16:26 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -1.0200 |  |
| Jogador 2 | 3-5 | 12:16:50 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-5 | 12:16:51 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 3-5 | 12:16:51 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-5 | 12:16:52 | VENDEU: Zyra (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-5 | 12:16:52 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 3-5 | 12:16:53 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 3-5 | 12:16:54 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-5 | 12:16:54 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-5 | 12:16:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-6 | 12:17:21 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Tristana | 0.8300 |  |
| Jogador 2 | 3-6 | 12:17:22 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Tristana | 0.2900 |  |
| Jogador 2 | 3-6 | 12:17:22 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Veigar | -0.5400 |  |
| Jogador 2 | 3-6 | 12:17:23 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | 0.6300 |  |
| Jogador 2 | 3-6 | 12:17:23 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-6 | 12:17:24 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 3-6 | 12:17:24 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 3-6 | 12:17:24 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 3-6 | 12:17:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 3-7 | 12:17:54 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_CrimsonRaptor18 | 0.7900 |  |
| Jogador 2 | 3-7 | 12:17:55 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_CrimsonRaptor18 | -0.0700 |  |
| Jogador 2 | 3-7 | 12:17:56 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_CrimsonRaptor18 | 0.1800 |  |
| Jogador 2 | 3-7 | 12:17:56 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_CrimsonRaptor18 | 0.2200 |  |
| Jogador 2 | 3-7 | 12:17:57 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_CrimsonRaptor18 | 0.4000 |  |
| Jogador 2 | 3-7 | 12:17:57 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 2 | 3-7 | 12:17:59 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Veigar | -0.5600 |  |
| Jogador 2 | 3-7 | 12:17:59 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 3-7 | 12:18:00 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Veigar | -0.2800 |  |
| Jogador 2 | 4-1 | 12:18:34 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Veigar | 0.8700 |  |
| Jogador 2 | 4-1 | 12:18:35 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 4-1 | 12:18:36 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_Veigar | 0.3200 |  |
| Jogador 2 | 4-1 | 12:18:37 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_Veigar | 0.2500 |  |
| Jogador 2 | 4-1 | 12:18:37 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | -0.1900 |  |
| Jogador 2 | 4-1 | 12:18:38 | MOVE Board -> Board: Ezreal (i:8.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-1 | 12:18:38 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-1 | 12:18:39 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-1 | 12:18:39 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | 0.5900 |  |
| Jogador 2 | 4-2 | 12:19:19 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_Veigar | 0.7800 |  |
| Jogador 2 | 4-2 | 12:19:20 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Veigar | 0.2800 |  |
| Jogador 2 | 4-2 | 12:19:21 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_Veigar | -0.5800 |  |
| Jogador 2 | 4-2 | 12:19:21 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Kobuko (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 4-2 | 12:19:22 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Kobuko (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 4-2 | 12:19:22 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Veigar (i:4.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_Veigar | 0.1700 |  |
| Jogador 2 | 4-2 | 12:19:23 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Veigar | 0.6100 |  |
| Jogador 2 | 4-2 | 12:19:23 | MOVE Board -> Board: Sejuani (i:4.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-2 | 12:19:24 | MOVE Board -> Board: Veigar (i:4.0) <-> Ezreal (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-3 | 12:20:00 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 4-3 | 12:20:00 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_Veigar | 0.3800 |  |
| Jogador 2 | 4-3 | 12:20:01 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 4-3 | 12:20:02 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 4-3 | 12:20:02 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 4-3 | 12:20:03 | MOVE Board -> Board: Ezreal (i:8.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-3 | 12:20:04 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 4-3 | 12:20:04 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-4 | 12:20:49 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 4-4 | 12:20:50 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_18_Veigar | 0.7200 |  |
| Jogador 2 | 4-4 | 12:20:51 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_18_Veigar | -0.3800 |  |
| Jogador 2 | 4-4 | 12:20:51 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 4-4 | 12:20:52 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 4-4 | 12:20:52 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 4-4 | 12:20:53 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-4 | 12:20:53 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-4 | 12:20:54 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-5 | 12:21:48 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 4-5 | 12:21:48 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 4-5 | 12:21:49 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-5 | 12:21:49 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_Veigar | 0.2100 |  |
| Jogador 2 | 4-5 | 12:21:50 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_18_Veigar | -0.5100 |  |
| Jogador 2 | 4-5 | 12:21:51 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Veigar | -0.2700 |  |
| Jogador 2 | 4-5 | 12:21:51 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 4-5 | 12:21:52 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 4-5 | 12:21:52 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-6 | 12:22:40 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Veigar | 0.1700 |  |
| Jogador 2 | 4-6 | 12:22:41 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 4-6 | 12:22:41 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 4-6 | 12:22:42 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 4-6 | 12:22:43 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 4-6 | 12:22:43 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 4-6 | 12:22:44 | MOVE Bench -> Board: Rengar (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 4-6 | 12:22:45 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 4-6 | 12:22:45 | MOVE Board -> Board: Rengar (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 4-7 | 12:23:35 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 4-7 | 12:23:36 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 4-7 | 12:23:37 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Colosso | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 4-7 | 12:23:37 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_CrimsonRaptor18 | 0.7500 |  |
| Jogador 2 | 4-7 | 12:23:38 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_CrimsonRaptor18 | 0.3100 |  |
| Jogador 2 | 4-7 | 12:23:38 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_CrimsonRaptor18 | -0.0800 |  |
| Jogador 2 | 4-7 | 12:23:39 | MOVE Board -> Board: Sejuani (i:4.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 2 | 4-7 | 12:23:40 | MOVE Board -> Board: Veigar (i:4.0) <-> Ezreal (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 2 | 4-7 | 12:23:40 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 2 | 5-1 | 12:24:34 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 0 | Colosso | DA_18_Veigar | -0.4800 |  |
| Jogador 2 | 5-1 | 12:24:34 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Colosso | DA_18_Veigar | 0.2800 |  |
| Jogador 2 | 5-1 | 12:24:35 | MOVE Board -> Board: Ezreal (i:8.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-1 | 12:24:35 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 0 | Colosso | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 5-1 | 12:24:36 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 5-1 | 12:24:36 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-1 | 12:24:37 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-1 | 12:24:37 | MOVE Board -> Board: Veigar (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-1 | 12:24:38 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 14 | 0 | Colosso | DA_18_Veigar | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-2 | 12:25:24 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 1 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-2 | 12:25:25 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 25 | 1 | Colosso | DA_18_Veigar | 0.8800 |  |
| Jogador 2 | 5-2 | 12:25:25 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 22 | 1 | Colosso | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 5-2 | 12:25:26 | VENDEU: Sejuani (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 1 | Colosso | DA_18_Veigar | -0.5800 |  |
| Jogador 2 | 5-2 | 12:25:26 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Colosso | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 5-2 | 12:25:26 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Colosso | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 5-2 | 12:25:27 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-2 | 12:25:27 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 11 | 1 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-2 | 12:25:28 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 11 | 1 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-3 | 12:26:22 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 22 | 1 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-3 | 12:26:22 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Colosso | DA_18_Veigar | 0.7300 |  |
| Jogador 2 | 5-3 | 12:26:22 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 22 | 1 | Colosso | DA_18_Veigar | -0.3200 |  |
| Jogador 2 | 5-3 | 12:26:23 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 21 | 1 | Colosso | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 5-3 | 12:26:23 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 22 | 1 | Colosso | DA_18_Veigar | -0.5900 |  |
| Jogador 2 | 5-3 | 12:26:24 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 21 | 1 | Colosso | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 5-3 | 12:26:24 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 21 | 1 | Colosso | DA_18_Veigar | 0.5700 |  |
| Jogador 2 | 5-3 | 12:26:25 | COMPROU: Alune (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Colosso | DA_18_Veigar | 0.1700 |  |
| Jogador 2 | 5-3 | 12:26:25 | MOVE Board -> Board: Diana (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-4 | 12:27:15 | VENDEU: Alune (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 1 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 5-4 | 12:27:17 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 1 | Colosso | DA_18_Veigar | 0.7000 |  |
| Jogador 2 | 5-4 | 12:27:18 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 1 | Colosso | DA_18_Veigar | -0.3200 |  |
| Jogador 2 | 5-4 | 12:27:18 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 1 | Colosso | DA_CrimsonRaptor18 | 0.8400 |  |
| Jogador 2 | 5-4 | 12:27:19 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Colosso | DA_CrimsonRaptor18 | 0.1200 |  |
| Jogador 2 | 5-4 | 12:27:19 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Colosso | DA_CrimsonRaptor18 | 0.0100 |  |
| Jogador 2 | 5-4 | 12:27:20 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Colosso | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 2 | 5-4 | 12:27:20 | MOVE Board -> Board: Veigar (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Colosso | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 2 | 5-4 | 12:27:20 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Colosso | DA_CrimsonRaptor18 | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-5 | 12:28:21 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 2 | Colosso | DA_18_Veigar | -0.5600 |  |
| Jogador 2 | 5-5 | 12:28:21 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Colosso | DA_18_Veigar | 0.2800 |  |
| Jogador 2 | 5-5 | 12:28:22 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 2 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-5 | 12:28:22 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Colosso | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 5-5 | 12:28:23 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-5 | 12:28:23 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-5 | 12:28:23 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Colosso | DA_18_Veigar | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-6 | 12:29:28 | VENDEU: Malphite (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 3 | Colosso | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 5-6 | 12:29:29 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Colosso | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 5-6 | 12:29:29 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 3 | Colosso | DA_18_Veigar | 0.0200 |  |
| Jogador 2 | 5-6 | 12:29:30 | COMPROU: Lux (Lunar) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Colosso | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 5-6 | 12:29:30 | VENDEU: Lux (Lunar) (i:10.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 3 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 5-6 | 12:29:30 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Colosso | DA_18_Veigar | 0.1000 |  |
| Jogador 2 | 5-6 | 12:29:31 | MOVE Board -> Board: Kobuko (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-6 | 12:29:31 | MOVE Board -> Board: Diana (i:6.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-6 | 12:29:32 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 47 | 3 | Colosso | DA_18_Veigar | -0.0700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-7 | 12:30:26 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Kha'Zix (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 59 | 4 | Colosso | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 5-7 | 12:30:26 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 4 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 5-7 | 12:30:27 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 58 | 4 | Colosso | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 5-7 | 12:30:27 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 4 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 5-7 | 12:30:28 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 4 | Colosso | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 5-7 | 12:30:28 | MOVE Board -> Board: Rengar (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 4 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 5-7 | 12:30:28 | MOVE Board -> Board: Veigar (i:4.0) <-> Ezreal (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 4 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 5-7 | 12:30:29 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 59 | 4 | Colosso | DA_18_Veigar | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 6-1 | 12:32:00 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 6-1 | 12:32:00 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Colosso | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 6-1 | 12:32:01 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 6-1 | 12:32:01 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Colosso | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 6-1 | 12:32:02 | MOVE Board -> Board: Ezreal (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 6-1 | 12:32:02 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Colosso | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 6-1 | 12:32:02 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Colosso | DA_18_Veigar | -0.1400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 6-2 | 12:33:37 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Colosso | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 6-2 | 12:33:38 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Colosso | DA_18_Veigar | 0.9100 |  |
| Jogador 2 | 6-2 | 12:33:38 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Colosso | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 6-2 | 12:33:38 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Colosso | DA_18_Veigar | 0.3800 |  |
| Jogador 2 | 6-2 | 12:33:39 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Colosso | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 6-2 | 12:33:39 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Colosso | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 6-2 | 12:33:39 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 6-2 | 12:33:40 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Colosso | DA_18_Veigar | -0.1800 |  |
| Jogador 2 | 6-2 | 12:33:40 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 6-3 | 12:35:02 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Colosso | DA_18_Veigar | 0.9100 |  |
| Jogador 2 | 6-3 | 12:35:02 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Colosso | DA_18_Veigar | -0.5900 |  |
| Jogador 2 | 6-3 | 12:35:02 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Colosso | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 6-3 | 12:35:03 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Colosso | DA_18_Veigar | -0.0700 |  |
| Jogador 2 | 6-3 | 12:35:03 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Colosso | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 6-3 | 12:35:04 | MOVE Bench -> Board: Zyra (i:8.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Colosso | DA_18_Veigar | -0.3900 |  |
| Jogador 2 | 6-3 | 12:35:04 | MOVE Bench -> Board: Vi (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Colosso | DA_18_Veigar | -0.3900 |  |
| Jogador 2 | 6-3 | 12:35:05 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Colosso | DA_18_Veigar | -0.1700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 6-4 | 12:36:38 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Colosso | DA_18_Zyra | -0.5900 |  |
| Jogador 2 | 6-4 | 12:36:38 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Colosso | DA_18_Zyra | 0.5900 |  |
| Jogador 2 | 6-4 | 12:36:39 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Ezreal (i:8.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Colosso | DA_18_Zyra | 0.1000 |  |
| Jogador 2 | 6-4 | 12:36:39 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Ezreal (i:8.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Colosso | DA_18_Zyra | 0.1200 |  |
| Jogador 2 | 6-4 | 12:36:40 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Colosso | DA_18_Zyra | -0.0400 |  |
| Jogador 2 | 6-4 | 12:36:40 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 110 | 5 | Colosso | DA_18_Zyra | 0.2900 |  |
| Jogador 2 | 6-4 | 12:36:41 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Colosso | DA_18_Zyra | -0.4000 |  |
| Jogador 2 | 6-4 | 12:36:41 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 110 | 5 | Colosso | DA_18_Zyra | 0.2500 |  |
| Jogador 2 | 6-4 | 12:36:42 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Colosso | DA_18_Zyra | -0.0600 |  |
| Jogador 2 | 6-5 | 12:37:44 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 123 | 5 | Colosso | DA_18_Zyra | 0.1300 |  |
| Jogador 2 | 6-5 | 12:37:45 | VENDEU: Sivir (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 127 | 5 | Colosso | DA_18_Zyra | -0.0200 |  |
| Jogador 2 | 6-5 | 12:37:47 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 123 | 5 | Colosso | DA_18_Zyra | 0.1300 |  |
| Jogador 2 | 6-5 | 12:37:47 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 127 | 5 | Colosso | DA_18_Zyra | -0.0200 |  |
| Jogador 2 | 6-5 | 12:37:48 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Colosso | DA_18_Zyra | 0.1000 |  |
| Jogador 2 | 6-5 | 12:37:48 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 127 | 5 | Colosso | DA_18_Zyra | -0.0300 |  |
| Jogador 2 | 6-5 | 12:37:48 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Colosso | DA_18_Zyra | 0.1000 |  |
| Jogador 2 | 6-5 | 12:37:49 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 127 | 5 | Colosso | DA_18_Zyra | -0.0100 |  |
| Jogador 2 | 6-5 | 12:37:49 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 124 | 5 | Colosso | DA_18_Zyra | -0.2100 |  |
| Jogador 2 | 6-6 | 12:38:54 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 141 | 5 | Colosso | DA_18_Zyra | 0.0200 |  |
| Jogador 2 | 6-6 | 12:38:55 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 137 | 5 | Colosso | DA_18_Zyra | 0.3900 |  |
| Jogador 2 | 6-6 | 12:38:55 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 140 | 5 | Colosso | DA_18_Zyra | -0.4500 |  |
| Jogador 2 | 6-6 | 12:38:56 | COMPROU: Morgana (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 136 | 5 | Colosso | DA_18_Zyra | -0.1400 |  |
| Jogador 2 | 6-6 | 12:38:56 | VENDEU: Morgana (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 140 | 5 | Colosso | DA_18_Zyra | 0.0000 |  |
| Jogador 2 | 6-6 | 12:38:57 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 138 | 5 | Colosso | DA_18_Zyra | 0.1200 |  |
| Jogador 2 | 6-6 | 12:38:57 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 140 | 5 | Colosso | DA_18_Zyra | -0.0100 |  |
| Jogador 2 | 6-6 | 12:38:57 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 139 | 5 | Colosso | DA_18_Zyra | -0.0300 |  |
| Jogador 2 | 6-6 | 12:38:58 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 140 | 5 | Colosso | DA_18_Zyra | -0.0200 |  |
| Jogador 2 | 6-7 | 12:39:54 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 150 | 5 | Colosso | DA_18_Diana | 1.0800 |  |
| Jogador 2 | 6-7 | 12:39:54 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 147 | 5 | Colosso | DA_18_Diana | 0.3000 |  |
| Jogador 2 | 6-7 | 12:39:55 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Ezreal (i:8.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 147 | 5 | Colosso | DA_18_Diana | 0.1100 |  |
| Jogador 2 | 6-7 | 12:39:55 | VENDEU: Diana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 155 | 5 | Colosso | DA_18_Zyra | -0.5900 |  |
| Jogador 2 | 6-7 | 12:39:56 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 151 | 5 | Colosso | DA_18_Zyra | 0.1100 |  |
| Jogador 2 | 6-7 | 12:39:56 | MOVE Bench -> Board: Lillia (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 151 | 5 | Colosso | DA_18_Zyra | 0.4100 |  |
| Jogador 2 | 6-7 | 12:39:56 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 147 | 5 | Colosso | DA_18_Zyra | 0.7700 |  |
| Jogador 2 | 6-7 | 12:39:57 | MOVE Board -> Board: Lillia (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 147 | 5 | Colosso | DA_18_Zyra | 0.0000 |  |
| Jogador 2 | 6-7 | 12:39:57 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 147 | 5 | Colosso | DA_18_Zyra | -0.0200 |  |
| Jogador 3 | ? | 12:12:44 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | ? | 12:12:46 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | ? | 12:12:47 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | ? | 12:12:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 12:12:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 12:12:52 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 12:12:52 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-1 | 12:12:53 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 1-1 | 12:12:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 12:12:56 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-2 | 12:12:59 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 12:12:59 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 12:13:00 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 12:13:00 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-2 | 12:13:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 12:13:04 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 1-3 | 12:13:07 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 12:13:07 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 12:13:09 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 12:13:09 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 12:13:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 12:13:17 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 12:13:18 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 12:13:18 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 12:13:19 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 1-4 | 12:13:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-1 | 12:13:26 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-1 | 12:13:26 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 12:13:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 12:13:36 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-2 | 12:13:36 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 2-2 | 12:13:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-2 | 12:13:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 12:13:49 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-3 | 12:13:49 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 2-3 | 12:13:50 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 2-3 | 12:13:51 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 2-3 | 12:13:52 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-3 | 12:13:52 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 2-3 | 12:13:53 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-3 | 12:13:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 12:14:03 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 2-4 | 12:14:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-4 | 12:14:04 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-4 | 12:14:04 | MOVE Bench -> Board: Diana (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.3800 |  |
| Jogador 3 | 2-4 | 12:14:05 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 2-4 | 12:14:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 12:14:18 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 12:14:19 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 2-5 | 12:14:19 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 12:14:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 2-5 | 12:14:20 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 12:14:21 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-5 | 12:14:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 12:14:35 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.8100 |  |
| Jogador 3 | 2-6 | 12:14:35 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-6 | 12:14:36 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.1700 |  |
| Jogador 3 | 2-6 | 12:14:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 2-6 | 12:14:37 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 2-6 | 12:14:37 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-6 | 12:14:38 | MOVE Board -> Board: Grompe (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 12:14:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 12:14:53 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.7000 |  |
| Jogador 3 | 2-7 | 12:14:54 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 2-7 | 12:14:54 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | -0.5800 |  |
| Jogador 3 | 2-7 | 12:14:55 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.2800 |  |
| Jogador 3 | 2-7 | 12:14:55 | MOVE Bench -> Board: Vi (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | -0.5000 |  |
| Jogador 3 | 2-7 | 12:14:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-7 | 12:14:56 | MOVE Bench -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 2-7 | 12:14:57 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.6500 |  |
| Jogador 3 | 2-7 | 12:14:57 | MOVE Bench -> Board: Vi (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.4900 |  |
| Jogador 3 | 3-1 | 12:15:13 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-1 | 12:15:14 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Akali_AD | 0.8200 |  |
| Jogador 3 | 3-1 | 12:15:14 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Akali_AD | 0.4600 |  |
| Jogador 3 | 3-1 | 12:15:15 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 3-1 | 12:15:15 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 12:15:16 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-1 | 12:15:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-2 | 12:15:34 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Akali_AD | 0.7400 |  |
| Jogador 3 | 3-2 | 12:15:35 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_18_Akali_AD | -0.3400 |  |
| Jogador 3 | 3-2 | 12:15:35 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 3-2 | 12:15:36 | MOVE Board -> Board: Grompe (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 12:15:36 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 12:15:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-3 | 12:15:57 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-3 | 12:15:57 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_18_Akali_AD | 0.8100 |  |
| Jogador 3 | 3-3 | 12:15:58 | MOVE Bench -> Board: Vi (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 3-3 | 12:15:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-3 | 12:15:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-3 | 12:15:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 12:16:00 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Colosso | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-3 | 12:16:00 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 12:16:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 1 | Colosso | DA_18_Akali_AD | 0.0600 |  |
| Jogador 3 | 3-4 | 12:16:22 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 3-4 | 12:16:23 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.7600 |  |
| Jogador 3 | 3-4 | 12:16:24 | MOVE Bench -> Board: Vi (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Akali_AD | 0.4300 |  |
| Jogador 3 | 3-4 | 12:16:24 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Akali_AD | 0.1800 |  |
| Jogador 3 | 3-4 | 12:16:25 | MOVE Bench -> Board: Zyra (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 3-4 | 12:16:25 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Akali_AD | -0.6700 |  |
| Jogador 3 | 3-4 | 12:16:26 | MOVE Bench -> Board: Vi (i:12.0) <-> Zyra (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 3-4 | 12:16:26 | MOVE Bench -> Board: Zyra (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 3-4 | 12:16:26 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Akali_AD | -0.6700 |  |
| Jogador 3 | 3-5 | 12:16:50 | VENDEU: Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 0 | Colosso | DA_18_Akali_AD | -0.5700 |  |
| Jogador 3 | 3-5 | 12:16:51 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Colosso | DA_18_Akali_AD | 0.7700 |  |
| Jogador 3 | 3-5 | 12:16:51 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_18_Akali_AD | 0.1400 |  |
| Jogador 3 | 3-5 | 12:16:52 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Colosso | DA_18_Akali_AD | 0.0400 |  |
| Jogador 3 | 3-5 | 12:16:52 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Akali_AD | -0.1100 |  |
| Jogador 3 | 3-5 | 12:16:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 3-5 | 12:16:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 3-5 | 12:16:54 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 3-5 | 12:16:55 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-6 | 12:17:21 | VENDEU: Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-6 | 12:17:22 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_18_Akali_AD | 0.6300 |  |
| Jogador 3 | 3-6 | 12:17:22 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 3-6 | 12:17:23 | MOVE Board -> Board: Diana (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 12:17:23 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Akali_AD | -0.2900 |  |
| Jogador 3 | 3-6 | 12:17:24 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-6 | 12:17:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-7 | 12:17:54 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.7100 |  |
| Jogador 3 | 3-7 | 12:17:55 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.2900 |  |
| Jogador 3 | 3-7 | 12:17:56 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 3 | 3-7 | 12:17:56 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_TearOfTheGoddess -> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 3 | 3-7 | 12:17:57 | MOVE Board -> Board: Akali (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 3-7 | 12:17:57 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 3 | 3-7 | 12:17:59 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 12:18:34 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 3 | 4-1 | 12:18:35 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 12:18:36 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 3 | 4-1 | 12:18:37 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 12:19:19 | MOVE Board -> Board: Diana (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 12:19:20 | MOVE Board -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 3 | 4-2 | 12:19:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 12:20:00 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 12:20:00 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 3 | 4-3 | 12:20:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 3 | 4-4 | 12:20:49 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 3 | 4-4 | 12:20:50 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 12:20:51 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Colosso | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 3 | 4-5 | 12:21:48 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 2 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-5 | 12:21:48 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Colosso | DA_Scuttlecrab18 | 0.7700 |  |
| Jogador 3 | 4-5 | 12:21:49 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 2 | Colosso | DA_Scuttlecrab18 | 0.1500 |  |
| Jogador 3 | 4-5 | 12:21:49 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Colosso | DA_Scuttlecrab18 | 0.2700 |  |
| Jogador 3 | 4-5 | 12:21:50 | MOVE Board -> Board: Grompe (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-5 | 12:21:51 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-5 | 12:21:51 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 4-5 | 12:21:52 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Colosso | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 4-6 | 12:22:40 | COMPROU: Sivir (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Colosso | DA_Scuttlecrab18 | 0.6900 |  |
| Jogador 3 | 4-6 | 12:22:41 | MOVE Board -> Board: Diana (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-6 | 12:22:41 | MOVE Board -> Board: Grompe (i:4.0) <-> Diana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-6 | 12:22:42 | MOVE Board -> Board: Diana (i:12.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-6 | 12:22:43 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Colosso | DA_Scuttlecrab18 | -0.1900 |  |
| Jogador 3 | 4-7 | 12:23:35 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 4 | Colosso | DA_Scuttlecrab18 | 0.2200 |  |
| Jogador 3 | 4-7 | 12:23:36 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 4 | Colosso | DA_Scuttlecrab18 | 0.1500 |  |
| Jogador 3 | 4-7 | 12:23:37 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 4 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 4-7 | 12:23:37 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 4 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 4-7 | 12:23:38 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 4 | Colosso | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 5-1 | 12:24:34 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Colosso | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 3 | 5-1 | 12:24:34 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_Scuttlecrab18 | 0.8600 |  |
| Jogador 3 | 5-1 | 12:24:35 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-1 | 12:24:35 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 5-1 | 12:24:36 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 3 | 5-2 | 12:25:24 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Colosso | DA_Scuttlecrab18 | -0.5900 |  |
| Jogador 3 | 5-2 | 12:25:25 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Colosso | DA_Scuttlecrab18 | 0.1300 |  |
| Jogador 3 | 5-2 | 12:25:25 | MOVE Board -> Board: Grompe (i:4.0) <-> Diana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-2 | 12:25:26 | MOVE Board -> Board: Diana (i:12.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-2 | 12:25:26 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-2 | 12:25:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Colosso | DA_Scuttlecrab18 | -0.1100 |  |
| Jogador 3 | 5-3 | 12:26:22 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Colosso | DA_Scuttlecrab18 | -0.0500 |  |
| Jogador 3 | 5-3 | 12:26:22 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 91 | 5 | Colosso | DA_Scuttlecrab18 | 0.3800 |  |
| Jogador 3 | 5-3 | 12:26:22 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Colosso | DA_Scuttlecrab18 | -0.5900 |  |
| Jogador 3 | 5-3 | 12:26:23 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 91 | 5 | Colosso | DA_Scuttlecrab18 | 0.8400 |  |
| Jogador 3 | 5-3 | 12:26:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_Scuttlecrab18 | 0.1300 |  |
| Jogador 3 | 5-3 | 12:26:24 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-3 | 12:26:24 | MOVE Board -> Board: Grompe (i:4.0) <-> Diana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-3 | 12:26:25 | MOVE Board -> Board: Diana (i:12.0) <-> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-3 | 12:26:25 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_Scuttlecrab18 | -0.1200 |  |
| Jogador 3 | 5-4 | 12:27:15 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Colosso | DA_Scuttlecrab18 | 0.6400 |  |
| Jogador 3 | 5-4 | 12:27:17 | VENDEU: Lobo Trevoguari (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Colosso | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 5-4 | 12:27:18 | COMPROU: Lux (Espinhos Negros) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Colosso | DA_Scuttlecrab18 | -0.1200 |  |
| Jogador 3 | 5-4 | 12:27:18 | VENDEU: Lux (Espinhos Negros) (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 101 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 5-4 | 12:27:19 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Colosso | DA_Scuttlecrab18 | -0.0600 |  |
| Jogador 3 | 5-4 | 12:27:19 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-4 | 12:27:20 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-4 | 12:27:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Colosso | DA_Scuttlecrab18 | -0.1200 |  |
| Jogador 3 | 5-5 | 12:28:21 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 5-5 | 12:28:21 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Colosso | DA_Scuttlecrab18 | 0.9300 |  |
| Jogador 3 | 5-5 | 12:28:22 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 106 | 5 | Colosso | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 3 | 5-5 | 12:28:22 | COMPROU: Ahri (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_Scuttlecrab18 | -0.2600 |  |
| Jogador 3 | 5-5 | 12:28:23 | MOVE Board -> Board: Akali (i:4.0) <-> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-5 | 12:28:23 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 5-5 | 12:28:23 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_Scuttlecrab18 | -0.1400 |  |
| Jogador 3 | 5-6 | 12:29:28 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 121 | 5 | Colosso | DA_Scuttlecrab18 | -0.1200 |  |
| Jogador 3 | 5-6 | 12:29:29 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 120 | 5 | Colosso | DA_Scuttlecrab18 | 0.9500 |  |
| Jogador 3 | 5-6 | 12:29:29 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 123 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 5-6 | 12:29:30 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 120 | 5 | Colosso | DA_Scuttlecrab18 | 0.7700 |  |
| Jogador 3 | 5-6 | 12:29:30 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Colosso | DA_Scuttlecrab18 | -0.0900 |  |
| Jogador 3 | 5-6 | 12:29:30 | MOVE Bench -> Board: Kha'Zix (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Colosso | DA_Scuttlecrab18 | 0.4000 |  |
| Jogador 3 | 5-6 | 12:29:31 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 115 | 5 | Colosso | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 5-6 | 12:29:31 | MOVE Board -> Board: Kha'Zix (i:12.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 115 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-6 | 12:29:32 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 115 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-7 | 12:30:26 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Aronguejo (i:8.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 126 | 5 | Colosso | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 5-7 | 12:30:26 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 128 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-7 | 12:30:27 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 124 | 5 | Colosso | DA_Scuttlecrab18 | 0.2700 |  |
| Jogador 3 | 5-7 | 12:30:27 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 127 | 5 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 5-7 | 12:30:28 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 124 | 5 | Colosso | DA_Scuttlecrab18 | 0.1200 |  |
| Jogador 3 | 5-7 | 12:30:28 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 127 | 5 | Colosso | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 5-7 | 12:30:28 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 124 | 5 | Colosso | DA_Scuttlecrab18 | 0.1800 |  |
| Jogador 3 | 5-7 | 12:30:29 | MOVE Board -> Board: Akali (i:4.0) <-> Kha'Zix (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 124 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-7 | 12:30:29 | MOVE Board -> Board: Kha'Zix (i:12.0) <-> Diana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 124 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-1 | 12:32:00 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 138 | 5 | Colosso | DA_Scuttlecrab18 | -0.0700 |  |
| Jogador 3 | 6-1 | 12:32:00 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 134 | 5 | Colosso | DA_Scuttlecrab18 | 1.0700 |  |
| Jogador 3 | 6-1 | 12:32:01 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 130 | 5 | Colosso | DA_Scuttlecrab18 | -0.1300 |  |
| Jogador 3 | 6-1 | 12:32:01 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 128 | 5 | Colosso | DA_Scuttlecrab18 | -0.2700 |  |
| Jogador 3 | 6-1 | 12:32:02 | VENDEU: Sivir (i:16.0) | STABILIZE | STABILIZE: pressão de vida | 139 | 5 | Colosso | DA_Scuttlecrab18 | -0.5800 |  |
| Jogador 3 | 6-1 | 12:32:02 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 138 | 5 | Colosso | DA_Scuttlecrab18 | -0.2400 |  |
| Jogador 3 | 6-1 | 12:32:02 | MOVE Board -> Board: Diana (i:12.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 138 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 6-1 | 12:32:03 | MOVE Board -> Board: Grompe (i:4.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 138 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 6-1 | 12:32:03 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 138 | 5 | Colosso | DA_Scuttlecrab18 | -0.2400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 6-2 | 12:33:37 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 147 | 5 | Colosso | DA_Scuttlecrab18 | 0.3500 |  |
| Jogador 3 | 6-2 | 12:33:38 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 148 | 5 | Colosso | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 6-2 | 12:33:38 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 145 | 5 | Colosso | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 6-2 | 12:33:38 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 147 | 5 | Colosso | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 3 | 6-2 | 12:33:39 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 145 | 5 | Colosso | DA_Scuttlecrab18 | -0.1700 |  |
| Jogador 3 | 6-2 | 12:33:39 | MOVE Board -> Board: Soraka (i:8.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 145 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 6-2 | 12:33:39 | MOVE Board -> Board: Akali (i:4.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 145 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-2 | 12:33:40 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 145 | 5 | Colosso | DA_Scuttlecrab18 | -0.2500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 6-3 | 12:35:02 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 158 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-3 | 12:35:02 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-3 | 12:35:02 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 157 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 6-3 | 12:35:03 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 6-3 | 12:35:03 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 157 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 6-3 | 12:35:04 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 6-3 | 12:35:04 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 6-3 | 12:35:05 | MOVE Board -> Board: Kha'Zix (i:12.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-3 | 12:35:05 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 154 | 5 | Colosso | DA_Scuttlecrab18 | -0.2600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 6-4 | 12:36:38 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 168 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 6-4 | 12:36:38 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 165 | 5 | Colosso | DA_Scuttlecrab18 | 0.2500 |  |
| Jogador 3 | 6-4 | 12:36:39 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 167 | 5 | Colosso | DA_Scuttlecrab18 | -0.0800 |  |
| Jogador 3 | 6-4 | 12:36:39 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 165 | 5 | Colosso | DA_Scuttlecrab18 | -0.1700 |  |
| Jogador 3 | 6-4 | 12:36:40 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 167 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-4 | 12:36:40 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 166 | 5 | Colosso | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 3 | 6-4 | 12:36:41 | MOVE Board -> Board: Grompe (i:4.0) <-> Diana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 166 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 6-4 | 12:36:41 | MOVE Board -> Board: Diana (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 166 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-4 | 12:36:42 | MOVE Board -> Board: Diana (i:12.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 166 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-5 | 12:37:44 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 178 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-5 | 12:37:45 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 174 | 5 | Colosso | DA_Scuttlecrab18 | 0.0400 |  |
| Jogador 3 | 6-5 | 12:37:47 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 178 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-5 | 12:37:47 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 177 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-5 | 12:37:48 | MOVE Board -> Board: Akali (i:4.0) <-> Soraka (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 177 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 6-5 | 12:37:48 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 178 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-5 | 12:37:48 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 175 | 5 | Colosso | DA_Scuttlecrab18 | -0.2600 |  |
| Jogador 3 | 6-5 | 12:37:49 | MOVE Board -> Board: Soraka (i:8.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 175 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 6-5 | 12:37:49 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 175 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 6-6 | 12:38:54 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 190 | 5 | Colosso | DA_Scuttlecrab18 | 0.0200 |  |
| Jogador 3 | 6-6 | 12:38:55 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 187 | 5 | Colosso | DA_Scuttlecrab18 | 0.7900 |  |
| Jogador 3 | 6-6 | 12:38:55 | VENDEU: Rubrivira (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 191 | 5 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 6-6 | 12:38:56 | COMPROU: Draven (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 186 | 5 | Colosso | DA_Scuttlecrab18 | -0.1800 |  |
| Jogador 3 | 6-6 | 12:38:56 | VENDEU: Draven (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 191 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 6-6 | 12:38:57 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Colosso | DA_Scuttlecrab18 | 0.0900 |  |
| Jogador 3 | 6-6 | 12:38:57 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 191 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 6-6 | 12:38:57 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Colosso | DA_Scuttlecrab18 | 0.0900 |  |
| Jogador 3 | 6-6 | 12:38:58 | MOVE Board -> Board: Grompe (i:4.0) <-> Kha'Zix (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 6-7 | 12:39:54 | EQUIP_FROM_INVENTORY: TFT_Item_Deathblade -> Aronguejo (i:8.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 200 | 5 | Colosso | DA_Scuttlecrab18 | 0.0600 |  |
| Jogador 3 | 6-7 | 12:39:54 | VENDEU: Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 203 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 6-7 | 12:39:55 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 199 | 5 | Colosso | DA_Scuttlecrab18 | 0.1800 |  |
| Jogador 3 | 6-7 | 12:39:55 | VENDEU: Azuporã (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 203 | 5 | Colosso | DA_Scuttlecrab18 | -0.0500 |  |
| Jogador 3 | 6-7 | 12:39:56 | COMPROU: Lux (Congregação das Bruxas) (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 198 | 5 | Colosso | DA_Scuttlecrab18 | -0.1700 |  |
| Jogador 3 | 6-7 | 12:39:56 | MOVE Board -> Board: Kha'Zix (i:12.0) <-> Aronguejo (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 198 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 6-7 | 12:39:56 | MOVE Board -> Board: Aronguejo (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 198 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 6-7 | 12:39:57 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 198 | 5 | Colosso | DA_Scuttlecrab18 | -0.6800 |  |
| Jogador 4 | ? | 12:12:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | ? | 12:12:46 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | ? | 12:12:47 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | ? | 12:12:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:12:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 12:12:52 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:12:52 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-1 | 12:12:53 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 1-1 | 12:12:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:12:56 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4600 |  |
| Jogador 4 | 1-2 | 12:12:59 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 12:12:59 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 12:13:00 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 12:13:00 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-2 | 12:13:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 12:13:07 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 12:13:07 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 12:13:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 12:13:17 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 4 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-4 | 12:13:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 1-4 | 12:13:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-1 | 12:13:26 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 2-1 | 12:13:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 2-1 | 12:13:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-2 | 12:13:36 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 4 | 2-2 | 12:13:36 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-2 | 12:13:37 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-2 | 12:13:38 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-2 | 12:13:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 12:13:39 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 12:13:39 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 12:13:40 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 4 | 2-2 | 12:13:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 12:13:49 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-3 | 12:13:49 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-3 | 12:13:50 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 4 | 2-3 | 12:13:51 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-3 | 12:13:52 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-3 | 12:13:52 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 2-3 | 12:13:53 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 2-3 | 12:13:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 4 | 2-3 | 12:13:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.9500 |  |
| Jogador 4 | 2-4 | 12:14:03 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 1.0000 |  |
| Jogador 4 | 2-4 | 12:14:03 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 2-4 | 12:14:04 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 4 | 2-4 | 12:14:04 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 4 | 2-4 | 12:14:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-4 | 12:14:06 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.6200 |  |
| Jogador 4 | 2-4 | 12:14:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 2-4 | 12:14:06 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 4 | 2-4 | 12:14:07 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 4 | 2-5 | 12:14:18 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 4 | 2-5 | 12:14:19 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 4 | 2-5 | 12:14:19 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.4300 |  |
| Jogador 4 | 2-5 | 12:14:20 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-5 | 12:14:20 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 4 | 2-5 | 12:14:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-5 | 12:14:21 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 4 | 2-5 | 12:14:22 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 4 | 2-5 | 12:14:22 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-6 | 12:14:35 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 1.1200 |  |
| Jogador 4 | 2-6 | 12:14:35 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 4 | 2-6 | 12:14:36 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 4 | 2-6 | 12:14:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-6 | 12:14:37 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 4 | 2-6 | 12:14:37 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 2-6 | 12:14:38 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-6 | 12:14:38 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-6 | 12:14:39 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-7 | 12:14:53 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 2-7 | 12:14:54 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 4 | 2-7 | 12:14:54 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-7 | 12:14:55 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 2-7 | 12:14:55 | MOVE Board -> Board: Karma (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-7 | 12:14:56 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 12:14:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-1 | 12:15:13 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 4 | 3-1 | 12:15:14 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-1 | 12:15:14 | MOVE Bench -> Board: Yunara (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -1.0000 |  |
| Jogador 4 | 3-1 | 12:15:15 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.5000 |  |
| Jogador 4 | 3-1 | 12:15:15 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 4 | 3-1 | 12:15:16 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 3-1 | 12:15:16 | MOVE Board -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-1 | 12:15:17 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 4 | 3-1 | 12:15:17 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 4 | 3-2 | 12:15:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-2 | 12:15:35 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-2 | 12:15:35 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 4 | 3-2 | 12:15:36 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-2 | 12:15:36 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-2 | 12:15:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-3 | 12:15:57 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 4 | 3-3 | 12:15:57 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.7200 |  |
| Jogador 4 | 3-3 | 12:15:58 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Grompe (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 3-3 | 12:15:59 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Grompe (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 4 | 3-3 | 12:15:59 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Grompe (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 3-3 | 12:15:59 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-3 | 12:16:00 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 4 | 3-3 | 12:16:00 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.6800 |  |
| Jogador 4 | 3-3 | 12:16:01 | MOVE Board -> Board: Grompe (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 4 | 3-4 | 12:16:22 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 4 | 3-4 | 12:16:23 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Florescer | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 4 | 3-4 | 12:16:24 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Florescer | DA_KogMaw18_AD | 0.4800 |  |
| Jogador 4 | 3-4 | 12:16:24 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 3-4 | 12:16:25 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 12:16:25 | MOVE Board -> Board: Master Yi (i:6.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-4 | 12:16:26 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 4 | 3-4 | 12:16:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 12:16:50 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-5 | 12:16:51 | VENDEU: Alistar (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 3-5 | 12:16:51 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-5 | 12:16:52 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-5 | 12:16:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 4 | 3-5 | 12:16:53 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 4 | 3-5 | 12:16:54 | MOVE Board -> Board: Grompe (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-5 | 12:16:54 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 3-5 | 12:16:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Florescer | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-6 | 12:17:21 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Florescer | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 4 | 3-6 | 12:17:22 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_18_MasterYi_AD | 0.8500 |  |
| Jogador 4 | 3-6 | 12:17:22 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_18_MasterYi_AD | 0.4300 |  |
| Jogador 4 | 3-6 | 12:17:23 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Florescer | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 4 | 3-6 | 12:17:23 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Florescer | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 4 | 3-6 | 12:17:24 | VENDEU: Master Yi (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 1 | Florescer | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 4 | 3-6 | 12:17:24 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 1 | Florescer | DA_KogMaw18_AD | -0.1300 |  |
| Jogador 4 | 3-6 | 12:17:24 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 1 | Florescer | DA_KogMaw18_AD | -0.3400 |  |
| Jogador 4 | 3-6 | 12:17:25 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 1 | Florescer | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 4 | 3-7 | 12:17:54 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-7 | 12:17:55 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Florescer | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 4 | 3-7 | 12:17:56 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Florescer | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 4 | 3-7 | 12:17:56 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Florescer | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 4 | 3-7 | 12:17:57 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 12:17:57 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Florescer | DA_KogMaw18_AD | -0.2900 |  |
| Jogador 4 | 3-7 | 12:17:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Florescer | DA_KogMaw18_AD | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-1 | 12:18:34 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-1 | 12:18:35 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Florescer | DA_KogMaw18_AD | 0.9300 |  |
| Jogador 4 | 4-1 | 12:18:36 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Florescer | DA_KogMaw18_AD | 0.2600 |  |
| Jogador 4 | 4-1 | 12:18:37 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Florescer | DA_KogMaw18_AD | -0.5500 |  |
| Jogador 4 | 4-1 | 12:18:37 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Florescer | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 4 | 4-1 | 12:18:38 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Florescer | DA_KogMaw18_AD | -0.4500 |  |
| Jogador 4 | 4-1 | 12:18:38 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Florescer | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 4 | 4-1 | 12:18:39 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Florescer | DA_KogMaw18_AD | 0.3700 |  |
| Jogador 4 | 4-1 | 12:18:39 | MOVE Board -> Board: Grompe (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Florescer | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 4 | 4-2 | 12:19:19 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Florescer | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 4 | 4-2 | 12:19:20 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Florescer | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 4 | 4-2 | 12:19:21 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 4-2 | 12:19:21 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Florescer | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 4 | 4-2 | 12:19:22 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 4-2 | 12:19:22 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Florescer | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 4 | 4-2 | 12:19:23 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Florescer | DA_KogMaw18_AD | -0.2400 |  |
| Jogador 4 | 4-2 | 12:19:23 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Florescer | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 4 | 4-2 | 12:19:24 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Florescer | DA_KogMaw18_AD | 0.8800 |  |
| Jogador 4 | 4-3 | 12:20:00 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Florescer | DA_KogMaw18_AD | -0.4500 |  |
| Jogador 4 | 4-3 | 12:20:00 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 5 | Florescer | DA_KogMaw18_AD | -0.2400 |  |
| Jogador 4 | 4-3 | 12:20:01 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 5 | Florescer | DA_KogMaw18_AD | 0.4700 |  |
| Jogador 4 | 4-3 | 12:20:02 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 5 | Florescer | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 4 | 4-3 | 12:20:02 | MOVE Board -> Board: Yunara (i:4.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 5 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 4-3 | 12:20:03 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 5 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 4-3 | 12:20:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 5 | Florescer | DA_KogMaw18_AD | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-4 | 12:20:49 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-4 | 12:20:50 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Florescer | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 4 | 4-4 | 12:20:51 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 4-4 | 12:20:51 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Florescer | DA_KogMaw18_AD | -0.2200 |  |
| Jogador 4 | 4-4 | 12:20:52 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-4 | 12:20:52 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Florescer | DA_KogMaw18_AD | -0.2400 |  |
| Jogador 4 | 4-4 | 12:20:53 | MOVE Board -> Board: Karma (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-4 | 12:20:53 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 4-4 | 12:20:54 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Florescer | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 4 | 4-5 | 12:21:48 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-5 | 12:21:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Florescer | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 4 | 4-5 | 12:21:49 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Florescer | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 4 | 4-5 | 12:21:49 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Florescer | DA_KogMaw18_AD | 0.4400 |  |
| Jogador 4 | 4-5 | 12:21:50 | REROLL | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Florescer | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 4 | 4-5 | 12:21:51 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Florescer | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 4-5 | 12:21:51 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Florescer | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 4-5 | 12:21:52 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Florescer | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 4-5 | 12:21:52 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 4-6 | 12:22:40 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Florescer | DA_KogMaw18_AD | 0.9800 |  |
| Jogador 4 | 4-6 | 12:22:41 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Yunara (i:4.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Florescer | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 4-6 | 12:22:41 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Yunara (i:4.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Florescer | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 4 | 4-6 | 12:22:42 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Yunara (i:4.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Florescer | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 4 | 4-6 | 12:22:43 | VENDEU: Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-6 | 12:22:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 4-6 | 12:22:44 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Florescer | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 4 | 4-6 | 12:22:45 | VENDEU: Rammus (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-6 | 12:22:45 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Florescer | DA_KogMaw18_AD | -0.2500 |  |
| Jogador 4 | 4-7 | 12:23:35 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Florescer | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 4 | 4-7 | 12:23:36 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_TearOfTheGoddess -> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Florescer | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 4 | 4-7 | 12:23:37 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-7 | 12:23:37 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Florescer | DA_18_MasterYi_AD | 1.0500 |  |
| Jogador 4 | 4-7 | 12:23:38 | MOVE Bench -> Board: Ezreal (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Florescer | DA_18_MasterYi_AD | 0.4800 |  |
| Jogador 4 | 4-7 | 12:23:38 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Florescer | DA_18_MasterYi_AD | -0.2300 |  |
| Jogador 4 | 4-7 | 12:23:39 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Florescer | DA_18_MasterYi_AD | -0.2500 |  |
| Jogador 4 | 4-7 | 12:23:40 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Florescer | DA_18_MasterYi_AD | -0.0700 |  |
| Jogador 4 | 4-7 | 12:23:40 | VENDEU: Master Yi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Florescer | DA_KogMaw18_AD | -0.7100 |  |
| Jogador 5 | ? | 12:12:44 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | ? | 12:12:46 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 5 | ? | 12:12:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 12:12:51 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 12:12:52 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 12:12:52 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-1 | 12:12:53 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 12:12:54 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 12:12:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 12:12:56 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4300 |  |
| Jogador 5 | 1-2 | 12:12:59 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 1-2 | 12:12:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 12:13:07 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 12:13:07 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 12:13:09 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 12:13:17 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 5 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 5 | 1-4 | 12:13:18 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 5 | 1-4 | 12:13:18 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 12:13:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 12:13:26 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-1 | 12:13:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 12:13:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 12:13:36 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 5 | 2-2 | 12:13:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 2-2 | 12:13:37 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 5 | 2-2 | 12:13:38 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 12:13:38 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 5 | 2-2 | 12:13:39 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 12:13:39 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0300 |  |
| Jogador 5 | 2-2 | 12:13:40 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-2 | 12:13:40 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 12:13:49 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.3100 |  |
| Jogador 5 | 2-3 | 12:13:49 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-3 | 12:13:50 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-3 | 12:13:51 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-3 | 12:13:52 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.1700 |  |
| Jogador 5 | 2-3 | 12:13:52 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0800 |  |
| Jogador 5 | 2-3 | 12:13:53 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 12:13:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 12:13:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-4 | 12:14:03 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2900 |  |
| Jogador 5 | 2-4 | 12:14:03 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3400 |  |
| Jogador 5 | 2-4 | 12:14:04 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 2-4 | 12:14:04 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1200 |  |
| Jogador 5 | 2-4 | 12:14:05 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-4 | 12:14:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 12:14:06 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3500 |  |
| Jogador 5 | 2-4 | 12:14:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-4 | 12:14:07 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.4000 |  |
| Jogador 5 | 2-5 | 12:14:18 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3600 |  |
| Jogador 5 | 2-5 | 12:14:19 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0900 |  |
| Jogador 5 | 2-5 | 12:14:19 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 12:14:20 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 12:14:20 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-5 | 12:14:21 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 2-5 | 12:14:21 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.4300 |  |
| Jogador 5 | 2-5 | 12:14:22 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-5 | 12:14:22 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-6 | 12:14:35 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.3500 |  |
| Jogador 5 | 2-6 | 12:14:35 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.9600 |  |
| Jogador 5 | 2-6 | 12:14:36 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.2100 |  |
| Jogador 5 | 2-6 | 12:14:36 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-6 | 12:14:37 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-6 | 12:14:37 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.1100 |  |
| Jogador 5 | 2-6 | 12:14:38 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.4200 |  |
| Jogador 5 | 2-6 | 12:14:38 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.3800 |  |
| Jogador 5 | 2-6 | 12:14:39 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 2-7 | 12:14:53 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Yunara | 0.7500 |  |
| Jogador 5 | 2-7 | 12:14:54 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Yunara | 0.1900 |  |
| Jogador 5 | 2-7 | 12:14:54 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Yunara | 0.1100 |  |
| Jogador 5 | 2-7 | 12:14:55 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Yunara | 0.0300 |  |
| Jogador 5 | 2-7 | 12:14:55 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Tristana | -0.6200 |  |
| Jogador 5 | 2-7 | 12:14:56 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Tristana | -0.2700 |  |
| Jogador 5 | 2-7 | 12:14:56 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 2-7 | 12:14:57 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Tristana | -0.2400 |  |
| Jogador 5 | 2-7 | 12:14:57 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Tristana | -0.3500 |  |
| Jogador 5 | 3-1 | 12:15:13 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_18_Tristana | 0.6900 |  |
| Jogador 5 | 3-1 | 12:15:14 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Enfeitiçador | DA_18_Tristana | 0.2700 |  |
| Jogador 5 | 3-1 | 12:15:14 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-1 | 12:15:15 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Tristana | -0.1000 |  |
| Jogador 5 | 3-1 | 12:15:15 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_Tristana | -0.5400 |  |
| Jogador 5 | 3-1 | 12:15:16 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_Tristana | -0.2400 |  |
| Jogador 5 | 3-1 | 12:15:16 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_Tristana | -0.3400 |  |
| Jogador 5 | 3-1 | 12:15:17 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_Tristana | -0.2700 |  |
| Jogador 5 | 3-1 | 12:15:17 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_Tristana | -0.3200 |  |
| Jogador 5 | 3-2 | 12:15:34 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_18_Tristana | 0.8100 |  |
| Jogador 5 | 3-2 | 12:15:35 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_Tristana | 0.2100 |  |
| Jogador 5 | 3-2 | 12:15:35 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Tristana | 0.2800 |  |
| Jogador 5 | 3-2 | 12:15:36 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_Ahri | -0.1000 |  |
| Jogador 5 | 3-2 | 12:15:36 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_18_Azir | -0.0900 |  |
| Jogador 5 | 3-2 | 12:15:36 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_Azir | -0.0400 |  |
| Jogador 5 | 3-2 | 12:15:37 | MOVE Bench -> Board: Yunara (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 3-2 | 12:15:37 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_Azir | -0.4000 |  |
| Jogador 5 | 3-2 | 12:15:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_Azir | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-3 | 12:15:57 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Enfeitiçador | DA_18_Azir | 0.8300 |  |
| Jogador 5 | 3-3 | 12:15:57 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_18_Azir | 0.5200 |  |
| Jogador 5 | 3-3 | 12:15:58 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Enfeitiçador | DA_18_Azir | -0.0500 |  |
| Jogador 5 | 3-3 | 12:15:59 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Enfeitiçador | DA_18_Azir | 0.0200 |  |
| Jogador 5 | 3-3 | 12:15:59 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Enfeitiçador | DA_18_Azir | -0.3600 |  |
| Jogador 5 | 3-3 | 12:15:59 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Enfeitiçador | DA_18_Azir | -0.2500 |  |
| Jogador 5 | 3-3 | 12:16:00 | MOVE Bench -> Board: Karma (i:2.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Enfeitiçador | DA_18_Azir | 0.0300 |  |
| Jogador 5 | 3-3 | 12:16:00 | MOVE Bench -> Board: Yunara (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 3-3 | 12:16:01 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Enfeitiçador | DA_18_Azir | -0.3400 |  |
| Jogador 5 | 3-4 | 12:16:22 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_18_Azir | 0.8300 |  |
| Jogador 5 | 3-4 | 12:16:23 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_Azir | 0.1100 |  |
| Jogador 5 | 3-4 | 12:16:24 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_18_Azir | -0.6200 |  |
| Jogador 5 | 3-4 | 12:16:24 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 3-4 | 12:16:25 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_18_Azir | -0.2500 |  |
| Jogador 5 | 3-4 | 12:16:25 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_18_Azir | -0.2700 |  |
| Jogador 5 | 3-4 | 12:16:26 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Enfeitiçador | DA_18_Azir | -0.2800 |  |
| Jogador 5 | 3-4 | 12:16:26 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Enfeitiçador | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 3-4 | 12:16:26 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Enfeitiçador | DA_18_Azir | 0.1200 |  |
| Jogador 5 | 3-5 | 12:16:50 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Enfeitiçador | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 3-5 | 12:16:51 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Enfeitiçador | DA_18_Azir | 0.8300 |  |
| Jogador 5 | 3-5 | 12:16:51 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Enfeitiçador | DA_18_Azir | 0.0200 |  |
| Jogador 5 | 3-5 | 12:16:52 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Enfeitiçador | DA_18_Azir | 0.2500 |  |
| Jogador 5 | 3-5 | 12:16:52 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Enfeitiçador | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 3-5 | 12:16:53 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Enfeitiçador | DA_18_Azir | 0.0800 |  |
| Jogador 5 | 3-5 | 12:16:54 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Enfeitiçador | DA_18_Azir | -0.0400 |  |
| Jogador 5 | 3-5 | 12:16:54 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Enfeitiçador | DA_18_Azir | 0.0200 |  |
| Jogador 5 | 3-5 | 12:16:55 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Enfeitiçador | DA_18_Azir | -0.0200 |  |
| Jogador 5 | 3-6 | 12:17:21 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Enfeitiçador | DA_18_Azir | 0.8300 |  |
| Jogador 5 | 3-6 | 12:17:22 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Enfeitiçador | DA_18_Azir | -0.4800 |  |
| Jogador 5 | 3-6 | 12:17:22 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_18_Azir | 0.0200 |  |
| Jogador 5 | 3-6 | 12:17:23 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Enfeitiçador | DA_18_Azir | -0.0200 |  |
| Jogador 5 | 3-6 | 12:17:23 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_18_Azir | -0.2200 |  |
| Jogador 5 | 3-6 | 12:17:24 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Enfeitiçador | DA_18_Azir | 0.0100 |  |
| Jogador 5 | 3-6 | 12:17:24 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Enfeitiçador | DA_18_Azir | -0.0400 |  |
| Jogador 5 | 3-6 | 12:17:24 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Enfeitiçador | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 3-6 | 12:17:25 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Enfeitiçador | DA_18_Azir | -0.4300 |  |
| Jogador 5 | 3-7 | 12:17:54 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Enfeitiçador | DA_18_Azir | 0.9600 |  |
| Jogador 5 | 3-7 | 12:17:55 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Enfeitiçador | DA_18_Azir | 0.4000 |  |
| Jogador 5 | 3-7 | 12:17:56 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Enfeitiçador | DA_18_Azir | 0.1400 |  |
| Jogador 5 | 3-7 | 12:17:56 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Enfeitiçador | DA_18_Azir | 0.1700 |  |
| Jogador 5 | 3-7 | 12:17:57 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Azir | 0.1200 |  |
| Jogador 5 | 3-7 | 12:17:57 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Enfeitiçador | DA_18_Azir | -0.3000 |  |
| Jogador 5 | 3-7 | 12:17:59 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Enfeitiçador | DA_18_Azir | -0.5100 |  |
| Jogador 5 | 3-7 | 12:17:59 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Azir | -0.4100 |  |
| Jogador 5 | 3-7 | 12:18:00 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Enfeitiçador | DA_18_Azir | -0.2400 |  |
| Jogador 5 | 4-1 | 12:18:34 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_18_Azir | 0.1500 |  |
| Jogador 5 | 4-1 | 12:18:35 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Enfeitiçador | DA_18_Azir | 0.0100 |  |
| Jogador 5 | 4-1 | 12:18:36 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_18_Azir | 0.1200 |  |
| Jogador 5 | 4-1 | 12:18:37 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 4-1 | 12:18:37 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 5 | Enfeitiçador | DA_18_Azir | -0.2400 |  |
| Jogador 5 | 4-1 | 12:18:38 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Enfeitiçador | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 4-1 | 12:18:38 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_18_Azir | 0.7200 |  |
| Jogador 5 | 4-1 | 12:18:39 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Enfeitiçador | DA_18_Azir | -0.4800 |  |
| Jogador 5 | 4-1 | 12:18:39 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_18_Azir | 0.9200 |  |
| Jogador 5 | 4-2 | 12:19:19 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_18_Azir | 0.8900 |  |
| Jogador 5 | 4-2 | 12:19:20 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Enfeitiçador | DA_18_Azir | 0.3200 |  |
| Jogador 5 | 4-2 | 12:19:21 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Enfeitiçador | DA_18_Azir | -0.5200 |  |
| Jogador 5 | 4-2 | 12:19:21 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Enfeitiçador | DA_18_Azir | 0.1200 |  |
| Jogador 5 | 4-2 | 12:19:22 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 4-2 | 12:19:22 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 4-2 | 12:19:23 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Enfeitiçador | DA_18_Azir | 0.0700 |  |
| Jogador 5 | 4-2 | 12:19:23 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Enfeitiçador | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 4-2 | 12:19:24 | REROLL | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Enfeitiçador | DA_18_Azir | -0.1600 |  |
| Jogador 5 | 4-3 | 12:20:00 | COMPROU: Kobuko (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Enfeitiçador | DA_18_Azir | 0.6400 |  |
| Jogador 5 | 4-3 | 12:20:00 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Enfeitiçador | DA_18_Azir | -0.0400 |  |
| Jogador 5 | 4-3 | 12:20:01 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Enfeitiçador | DA_18_Azir | -0.1900 |  |
| Jogador 5 | 4-3 | 12:20:02 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 82 | 5 | Enfeitiçador | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 4-3 | 12:20:02 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Enfeitiçador | DA_18_Azir | -0.2700 |  |
| Jogador 5 | 4-3 | 12:20:03 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Enfeitiçador | DA_18_Azir | -0.0700 |  |
| Jogador 5 | 4-3 | 12:20:04 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Enfeitiçador | DA_18_Azir | 0.0200 |  |
| Jogador 5 | 4-3 | 12:20:04 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Enfeitiçador | DA_18_Azir | 0.8100 |  |
| Jogador 5 | 4-3 | 12:20:05 | VENDEU: Kobuko (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Enfeitiçador | DA_18_Azir | -0.5700 |  |
| Jogador 5 | 4-4 | 12:20:49 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Enfeitiçador | DA_18_Azir | 0.1500 |  |
| Jogador 5 | 4-4 | 12:20:50 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 4-4 | 12:20:51 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Enfeitiçador | DA_18_Azir | -0.2200 |  |
| Jogador 5 | 4-4 | 12:20:51 | VENDEU: Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Enfeitiçador | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 4-4 | 12:20:52 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Enfeitiçador | DA_18_Azir | -0.2400 |  |
| Jogador 5 | 4-4 | 12:20:52 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 85 | 5 | Enfeitiçador | DA_18_Azir | -0.0700 |  |
| Jogador 5 | 4-4 | 12:20:53 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Enfeitiçador | DA_18_Azir | 0.0100 |  |
| Jogador 5 | 4-4 | 12:20:53 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Enfeitiçador | DA_18_Azir | 0.9800 |  |
| Jogador 5 | 4-4 | 12:20:54 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Enfeitiçador | DA_18_Azir | -0.4200 |  |
| Jogador 5 | 4-5 | 12:21:48 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Enfeitiçador | DA_18_Azir | 0.9800 |  |
| Jogador 5 | 4-5 | 12:21:48 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Enfeitiçador | DA_18_Azir | -1.1100 |  |
| Jogador 5 | 4-5 | 12:21:49 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Enfeitiçador | DA_18_Azir | 1.0800 |  |
| Jogador 5 | 4-5 | 12:21:49 | COMPROU: Kobuko (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Enfeitiçador | DA_18_Azir | 0.5100 |  |
| Jogador 5 | 4-5 | 12:21:50 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Enfeitiçador | DA_18_Azir | 0.5600 |  |
| Jogador 5 | 4-5 | 12:21:51 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 94 | 5 | Enfeitiçador | DA_18_Azir | -0.1800 |  |
| Jogador 5 | 4-5 | 12:21:51 | VENDEU: Veigar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Enfeitiçador | DA_18_Azir | -0.7200 |  |
| Jogador 5 | 4-5 | 12:21:52 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Enfeitiçador | DA_18_Azir | -0.2700 |  |
| Jogador 5 | 4-5 | 12:21:52 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Enfeitiçador | DA_18_Azir | -0.0700 |  |
| Jogador 6 | ? | 12:12:44 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 12:12:46 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | -0.1500 |  |
| Jogador 6 | ? | 12:12:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 12:12:51 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 12:12:52 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 12:12:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 12:12:56 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2200 |  |
| Jogador 6 | 1-2 | 12:12:59 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 6 | 1-2 | 12:12:59 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 6 | 1-2 | 12:13:00 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 12:13:00 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 12:13:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-2 | 12:13:04 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.5700 |  |
| Jogador 6 | 1-3 | 12:13:07 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0200 |  |
| Jogador 6 | 1-3 | 12:13:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 6 | 1-4 | 12:13:17 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 6 | 1-4 | 12:13:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 6 | 1-4 | 12:13:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 2-1 | 12:13:26 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-1 | 12:13:26 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-1 | 12:13:27 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-1 | 12:13:28 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-1 | 12:13:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 12:13:36 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-2 | 12:13:36 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-2 | 12:13:37 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-2 | 12:13:38 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 12:13:38 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 12:13:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 12:13:49 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-3 | 12:13:49 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-3 | 12:13:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | 0.8100 |  |
| Jogador 6 | 2-3 | 12:13:51 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 12:13:52 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-3 | 12:13:52 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-3 | 12:13:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 12:13:53 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-3 | 12:13:53 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-4 | 12:14:03 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | 0.8600 |  |
| Jogador 6 | 2-4 | 12:14:03 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-4 | 12:14:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 12:14:04 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | -0.4500 |  |
| Jogador 6 | 2-4 | 12:14:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 12:14:06 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | -0.4900 |  |
| Jogador 6 | 2-4 | 12:14:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 6 | 2-4 | 12:14:06 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.2100 |  |
| Jogador 6 | 2-4 | 12:14:07 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Yorick | -0.6300 |  |
| Jogador 6 | 2-5 | 12:14:18 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 2-5 | 12:14:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 6 | 2-5 | 12:14:19 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Yorick | -0.1900 |  |
| Jogador 6 | 2-5 | 12:14:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | -0.0600 |  |
| Jogador 6 | 2-5 | 12:14:20 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | 0.0100 |  |
| Jogador 6 | 2-5 | 12:14:21 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Yorick | -1.0200 |  |
| Jogador 6 | 2-5 | 12:14:21 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.1600 |  |
| Jogador 6 | 2-5 | 12:14:22 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.6000 |  |
| Jogador 6 | 2-5 | 12:14:22 | MOVE Board -> Board: Rakan (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 2-6 | 12:14:35 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 6 | 2-6 | 12:14:35 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 6 | 2-6 | 12:14:36 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 6 | 2-6 | 12:14:36 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 6 | 2-6 | 12:14:37 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Xayah | -0.1600 |  |
| Jogador 6 | 2-6 | 12:14:37 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 2-6 | 12:14:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Xayah | -0.0400 |  |
| Jogador 6 | 2-6 | 12:14:38 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 2-6 | 12:14:39 | MOVE Board -> Board: Cascalho (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Xayah | -0.0500 |  |
| Jogador 6 | 2-7 | 12:14:53 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.2600 |  |
| Jogador 6 | 2-7 | 12:14:54 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.1900 |  |
| Jogador 6 | 2-7 | 12:14:54 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 6 | 2-7 | 12:14:55 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.1800 |  |
| Jogador 6 | 2-7 | 12:14:55 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | -0.1000 |  |
| Jogador 6 | 2-7 | 12:14:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 2-7 | 12:14:56 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 6 | 2-7 | 12:14:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 2-7 | 12:14:57 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 6 | 3-1 | 12:15:13 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_Fiddlesticks18 | 0.8400 |  |
| Jogador 6 | 3-1 | 12:15:14 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | 0.8200 |  |
| Jogador 6 | 3-1 | 12:15:14 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | 0.1600 |  |
| Jogador 6 | 3-1 | 12:15:15 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.0300 |  |
| Jogador 6 | 3-1 | 12:15:15 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_Fiddlesticks18 | -0.4200 |  |
| Jogador 6 | 3-1 | 12:15:16 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_Fiddlesticks18 | 0.1600 |  |
| Jogador 6 | 3-1 | 12:15:16 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_Fiddlesticks18 | 0.1900 |  |
| Jogador 6 | 3-1 | 12:15:17 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 6 | 3-1 | 12:15:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 6 | 3-2 | 12:15:34 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_Fiddlesticks18 | 0.8000 |  |
| Jogador 6 | 3-2 | 12:15:35 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.2800 |  |
| Jogador 6 | 3-2 | 12:15:35 | MOVE Bench -> Board: Ornn (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.6500 |  |
| Jogador 6 | 3-2 | 12:15:36 | MOVE Bench -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.7800 |  |
| Jogador 6 | 3-2 | 12:15:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-3 | 12:15:57 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.2600 |  |
| Jogador 6 | 3-3 | 12:15:57 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.1200 |  |
| Jogador 6 | 3-3 | 12:15:58 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 6 | 3-3 | 12:15:59 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 6 | 3-3 | 12:15:59 | MOVE Board -> Board: Tristana (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-3 | 12:15:59 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 3-3 | 12:16:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-4 | 12:16:22 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.5400 |  |
| Jogador 6 | 3-4 | 12:16:23 | MOVE Board -> Board: Zyra (i:8.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-4 | 12:16:24 | MOVE Board -> Board: Xayah (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-4 | 12:16:24 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-4 | 12:16:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-5 | 12:16:50 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_Fiddlesticks18 | 0.8300 |  |
| Jogador 6 | 3-5 | 12:16:51 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.8200 |  |
| Jogador 6 | 3-5 | 12:16:51 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 6 | 3-5 | 12:16:52 | MOVE Board -> Board: Rakan (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-5 | 12:16:52 | MOVE Board -> Board: Xayah (i:2.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0200 |  |
| Jogador 6 | 3-5 | 12:16:53 | MOVE Board -> Board: Zyra (i:8.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.0500 |  |
| Jogador 6 | 3-5 | 12:16:54 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-5 | 12:16:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-6 | 12:17:21 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.6600 |  |
| Jogador 6 | 3-6 | 12:17:22 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.0600 |  |
| Jogador 6 | 3-6 | 12:17:22 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.2900 |  |
| Jogador 6 | 3-6 | 12:17:23 | MOVE Board -> Board: Azir (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-6 | 12:17:23 | MOVE Board -> Board: Tristana (i:6.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | -0.0300 |  |
| Jogador 6 | 3-6 | 12:17:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 3-7 | 12:17:54 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.1700 |  |
| Jogador 6 | 3-7 | 12:17:55 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_SparringGloves -> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.2100 |  |
| Jogador 6 | 3-7 | 12:17:56 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_Fiddlesticks18 | 0.1600 |  |
| Jogador 6 | 3-7 | 12:17:56 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 6 | 3-7 | 12:17:57 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 6 | 3-7 | 12:17:57 | MOVE Board -> Board: Xayah (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-7 | 12:17:59 | MOVE Board -> Board: Tristana (i:6.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 3-7 | 12:17:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 4-1 | 12:18:34 | VENDEU: Diana (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Feérico | DA_Fiddlesticks18 | -0.4900 |  |
| Jogador 6 | 4-1 | 12:18:35 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 6 | 4-1 | 12:18:36 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Feérico | DA_18_Rakan | -0.4900 |  |
| Jogador 6 | 4-1 | 12:18:37 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-1 | 12:18:37 | MOVE Board -> Board: Azir (i:6.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 4-1 | 12:18:38 | MOVE Board -> Board: Zyra (i:8.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-1 | 12:18:38 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-1 | 12:18:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_Rakan | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-2 | 12:19:19 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Feérico | DA_18_Rakan | 0.0200 |  |
| Jogador 6 | 4-2 | 12:19:20 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Feérico | DA_18_Rakan | 0.5500 |  |
| Jogador 6 | 4-2 | 12:19:21 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-2 | 12:19:21 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Rakan | -0.2500 |  |
| Jogador 6 | 4-2 | 12:19:22 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Rakan | 0.0100 |  |
| Jogador 6 | 4-2 | 12:19:22 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-2 | 12:19:23 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-2 | 12:19:23 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Rakan | -0.0500 |  |
| Jogador 6 | 4-2 | 12:19:24 | MOVE Board -> Board: Rakan (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 4-3 | 12:20:00 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Feérico | DA_18_Rakan | 0.0800 |  |
| Jogador 6 | 4-3 | 12:20:00 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Feérico | DA_18_Rakan | -0.3100 |  |
| Jogador 6 | 4-3 | 12:20:01 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 4-3 | 12:20:02 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Feérico | DA_18_Rakan | -0.2500 |  |
| Jogador 6 | 4-3 | 12:20:02 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Feérico | DA_18_Rakan | 0.0100 |  |
| Jogador 6 | 4-3 | 12:20:03 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 4-3 | 12:20:04 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 4-3 | 12:20:04 | MOVE Board -> Board: Xayah (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 4-3 | 12:20:05 | MOVE Board -> Board: Rakan (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 4-4 | 12:20:49 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-4 | 12:20:50 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-4 | 12:20:51 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-4 | 12:20:51 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-4 | 12:20:52 | MOVE Board -> Board: Tristana (i:6.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 4-4 | 12:20:52 | MOVE Board -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-4 | 12:20:53 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Feérico | DA_18_Rakan | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-5 | 12:21:48 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-5 | 12:21:48 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Feérico | DA_18_Rakan | 0.3200 |  |
| Jogador 6 | 4-5 | 12:21:49 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Feérico | DA_18_Rakan | 0.0100 |  |
| Jogador 6 | 4-5 | 12:21:49 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 42 | 3 | Feérico | DA_18_Rakan | -0.2500 |  |
| Jogador 6 | 4-5 | 12:21:50 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 45 | 3 | Feérico | DA_18_Rakan | 0.0100 |  |
| Jogador 6 | 4-5 | 12:21:51 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Feérico | DA_18_Rakan | -0.0600 |  |
| Jogador 6 | 4-5 | 12:21:51 | REROLL | STABILIZE | STABILIZE: pressão de vida | 41 | 3 | Feérico | DA_18_Rakan | -0.1300 |  |
| Jogador 6 | 4-5 | 12:21:52 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Feérico | DA_18_Rakan | 0.0100 |  |
| Jogador 6 | 4-5 | 12:21:52 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 40 | 3 | Feérico | DA_18_Rakan | 0.8600 |  |
| Jogador 6 | 4-6 | 12:22:40 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 52 | 4 | Feérico | DA_18_Rakan | -0.0300 |  |
| Jogador 6 | 4-6 | 12:22:41 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 49 | 4 | Feérico | DA_18_Rakan | 0.0700 |  |
| Jogador 6 | 4-6 | 12:22:41 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Feérico | DA_18_Rakan | 0.0700 |  |
| Jogador 6 | 4-6 | 12:22:42 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 49 | 4 | Feérico | DA_18_Rakan | -0.0600 |  |
| Jogador 6 | 4-6 | 12:22:43 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Feérico | DA_18_Rakan | 0.0600 |  |
| Jogador 6 | 4-6 | 12:22:43 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 50 | 4 | Feérico | DA_18_Rakan | -0.2300 |  |
| Jogador 6 | 4-6 | 12:22:44 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 4-6 | 12:22:45 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 51 | 4 | Feérico | DA_18_Rakan | -0.0500 |  |
| Jogador 6 | 4-6 | 12:22:45 | REROLL | STABILIZE | STABILIZE: pressão de vida | 49 | 4 | Feérico | DA_18_Rakan | -0.2400 |  |
| Jogador 6 | 4-7 | 12:23:35 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 4 | Feérico | DA_18_Rakan | 0.0800 |  |
| Jogador 6 | 4-7 | 12:23:36 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 4 | Feérico | DA_18_Rakan | 0.0900 |  |
| Jogador 6 | 4-7 | 12:23:37 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 61 | 4 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 4-7 | 12:23:37 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 4 | Feérico | DA_18_Rakan | 1.0200 |  |
| Jogador 6 | 4-7 | 12:23:38 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 60 | 4 | Feérico | DA_18_Rakan | 0.1700 |  |
| Jogador 6 | 4-7 | 12:23:38 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 57 | 4 | Feérico | DA_18_Rakan | 0.9200 |  |
| Jogador 6 | 4-7 | 12:23:39 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 4 | Feérico | DA_18_Rakan | -0.5900 |  |
| Jogador 6 | 4-7 | 12:23:40 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 57 | 4 | Feérico | DA_18_Rakan | 0.2300 |  |
| Jogador 6 | 4-7 | 12:23:40 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Azir (i:6.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: pressão de vida | 57 | 4 | Feérico | DA_18_Rakan | 0.1200 |  |
| Jogador 6 | 5-1 | 12:24:34 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Tristana (i:6.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Feérico | DA_18_Rakan | 0.1100 |  |
| Jogador 6 | 5-1 | 12:24:34 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Rakan (i:4.0) (tabuleiro slot 13) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Feérico | DA_18_Rakan | 0.1200 |  |
| Jogador 6 | 5-1 | 12:24:35 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 5-1 | 12:24:35 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 66 | 5 | Feérico | DA_18_Zyra | 1.0400 |  |
| Jogador 6 | 5-1 | 12:24:36 | COMPROU: Alistar (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Feérico | DA_18_Zyra | 0.6800 |  |
| Jogador 6 | 5-1 | 12:24:36 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Feérico | DA_18_Zyra | 0.2300 |  |
| Jogador 6 | 5-1 | 12:24:37 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 60 | 5 | Feérico | DA_18_Zyra | -0.0300 |  |
| Jogador 6 | 5-1 | 12:24:37 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 57 | 5 | Feérico | DA_18_Zyra | -0.0300 |  |
| Jogador 6 | 5-1 | 12:24:38 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 5 | Feérico | DA_18_Zyra | 0.0400 |  |
| Jogador 6 | 5-2 | 12:25:24 | VENDEU: Alistar (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Feérico | DA_18_Zyra | -0.0400 |  |
| Jogador 6 | 5-2 | 12:25:25 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Feérico | DA_18_Zyra | 0.0500 |  |
| Jogador 6 | 5-2 | 12:25:25 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Feérico | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 5-2 | 12:25:26 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 69 | 5 | Feérico | DA_18_Zyra | 0.0500 |  |
| Jogador 6 | 5-2 | 12:25:26 | VENDEU: Zyra (i:16.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Feérico | DA_18_Rakan | -0.7500 |  |
| Jogador 6 | 5-2 | 12:25:26 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Feérico | DA_18_Rakan | -0.0500 |  |
| Jogador 6 | 5-2 | 12:25:27 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 5-2 | 12:25:27 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Feérico | DA_18_Rakan | -0.2800 |  |
| Jogador 6 | 5-2 | 12:25:28 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 7 | ? | 12:12:44 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 12:12:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 12:12:51 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 12:12:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 12:12:52 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-1 | 12:12:53 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-1 | 12:12:54 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 12:12:54 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 12:12:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 12:12:56 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 7 | 1-2 | 12:12:59 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 12:12:59 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 12:13:00 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 12:13:00 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 12:13:00 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 12:13:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 12:13:07 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-3 | 12:13:07 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-3 | 12:13:09 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 12:13:09 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2000 |  |
| Jogador 7 | 1-3 | 12:13:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 12:13:17 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8300 |  |
| Jogador 7 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-4 | 12:13:18 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 7 | 1-4 | 12:13:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 12:13:26 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 12:13:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-1 | 12:13:27 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 12:13:28 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 12:13:28 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 12:13:28 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-1 | 12:13:29 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | -0.6300 |  |
| Jogador 7 | 2-1 | 12:13:29 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 2-1 | 12:13:30 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Varus (i:2.0) (tabuleiro slot 9) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1500 |  |
| Jogador 7 | 2-2 | 12:13:36 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 1.0500 |  |
| Jogador 7 | 2-2 | 12:13:36 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.6500 |  |
| Jogador 7 | 2-2 | 12:13:37 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1700 |  |
| Jogador 7 | 2-2 | 12:13:38 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 12:13:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-3 | 12:13:49 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.3100 |  |
| Jogador 7 | 2-3 | 12:13:49 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 2-3 | 12:13:50 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Sentinel18 | -0.1300 |  |
| Jogador 7 | 2-3 | 12:13:51 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-3 | 12:13:52 | MOVE Board -> Board: Hecarim (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-3 | 12:13:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-3 | 12:13:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 12:14:03 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.3300 |  |
| Jogador 7 | 2-4 | 12:14:03 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 12:14:04 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | 0.3600 |  |
| Jogador 7 | 2-4 | 12:14:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 12:14:05 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-4 | 12:14:06 | MOVE Board -> Board: Varus (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-4 | 12:14:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 12:14:18 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Sentinel18 | 0.9100 |  |
| Jogador 7 | 2-5 | 12:14:19 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.8800 |  |
| Jogador 7 | 2-5 | 12:14:19 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.4600 |  |
| Jogador 7 | 2-5 | 12:14:20 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 12:14:20 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_Sentinel18 | -0.6200 |  |
| Jogador 7 | 2-5 | 12:14:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 12:14:21 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | -0.6300 |  |
| Jogador 7 | 2-5 | 12:14:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 2-5 | 12:14:22 | VENDEU: Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 2-6 | 12:14:35 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_KogMaw18_AD | -0.3600 |  |
| Jogador 7 | 2-6 | 12:14:35 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 2-6 | 12:14:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 2-6 | 12:14:36 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 7 | 2-6 | 12:14:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 2-6 | 12:14:37 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 2-6 | 12:14:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 2-6 | 12:14:38 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 2-6 | 12:14:39 | MOVE Board -> Board: Rakan (i:2.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 2-7 | 12:14:53 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 7 | 2-7 | 12:14:54 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 7 | 2-7 | 12:14:54 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 7 | 2-7 | 12:14:55 | MOVE Board -> Board: Yorick (i:2.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 2-7 | 12:14:55 | MOVE Board -> Board: Varus (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 2-7 | 12:14:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-1 | 12:15:13 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 7 | 3-1 | 12:15:14 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-1 | 12:15:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-1 | 12:15:15 | MOVE Board -> Board: Hecarim (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-1 | 12:15:15 | MOVE Board -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-1 | 12:15:16 | MOVE Board -> Board: Yorick (i:2.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-1 | 12:15:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-2 | 12:15:34 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 7 | 3-2 | 12:15:35 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 7 | 3-2 | 12:15:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-2 | 12:15:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-2 | 12:15:36 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 3-2 | 12:15:36 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 3-2 | 12:15:37 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 7 | 3-2 | 12:15:37 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 7 | 3-2 | 12:15:38 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 3-3 | 12:15:57 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 7 | 3-3 | 12:15:57 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 7 | 3-3 | 12:15:58 | MOVE Bench -> Board: Kog'Maw (i:12.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 7 | 3-3 | 12:15:59 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 7 | 3-3 | 12:15:59 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-3 | 12:15:59 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 7 | 3-3 | 12:16:00 | MOVE Board -> Board: Shen (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-3 | 12:16:00 | MOVE Board -> Board: Vi (i:6.0) <-> Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-3 | 12:16:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-4 | 12:16:22 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 7 | 3-4 | 12:16:23 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 7 | 3-4 | 12:16:24 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-4 | 12:16:24 | MOVE Board -> Board: Varus (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-4 | 12:16:25 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-5 | 12:16:50 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 7 | 3-5 | 12:16:51 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.1300 |  |
| Jogador 7 | 3-5 | 12:16:51 | MOVE Board -> Board: Shen (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-5 | 12:16:52 | MOVE Board -> Board: Vi (i:6.0) <-> Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-5 | 12:16:52 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-6 | 12:17:21 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.6500 |  |
| Jogador 7 | 3-6 | 12:17:22 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 7 | 3-6 | 12:17:22 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-6 | 12:17:23 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-6 | 12:17:23 | MOVE Board -> Board: Hecarim (i:6.0) <-> Varus (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 3-6 | 12:17:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-7 | 12:17:54 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 7 | 3-7 | 12:17:55 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 7 | 3-7 | 12:17:56 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 7 | 3-7 | 12:17:56 | MOVE Board -> Board: Varus (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-7 | 12:17:57 | MOVE Board -> Board: Vi (i:6.0) <-> Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 3-7 | 12:17:57 | MOVE Board -> Board: Kog'Maw (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 3-7 | 12:17:59 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-1 | 12:18:34 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 7 | 4-1 | 12:18:35 | MOVE Board -> Board: Rakan (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-1 | 12:18:36 | MOVE Board -> Board: Hecarim (i:6.0) <-> Varus (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 4-1 | 12:18:37 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-2 | 12:19:19 | MOVE Board -> Board: Varus (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-2 | 12:19:20 | MOVE Board -> Board: Vi (i:6.0) <-> Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-2 | 12:19:21 | MOVE Board -> Board: Varus (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 4-2 | 12:19:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-3 | 12:20:00 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_KogMaw18_AD | 0.6100 |  |
| Jogador 7 | 4-3 | 12:20:00 | MOVE Board -> Board: Hecarim (i:6.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-3 | 12:20:01 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-3 | 12:20:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 4-4 | 12:20:49 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-4 | 12:20:50 | VENDEU: Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 1 | Colosso | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 7 | 4-4 | 12:20:51 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 7 | 4-4 | 12:20:51 | MOVE Board -> Board: Vi (i:6.0) <-> Varus (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-4 | 12:20:52 | MOVE Board -> Board: Varus (i:4.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 4-4 | 12:20:52 | MOVE Board -> Board: Rakan (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-4 | 12:20:53 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 4-5 | 12:21:48 | VENDEU: Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 2 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 7 | 4-5 | 12:21:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Colosso | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 7 | 4-5 | 12:21:49 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-5 | 12:21:49 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-5 | 12:21:50 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 4-5 | 12:21:51 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Colosso | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 7 | 4-6 | 12:22:40 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 3 | Colosso | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 7 | 4-6 | 12:22:41 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 3 | Colosso | DA_KogMaw18_AD | 0.7100 |  |
| Jogador 7 | 4-6 | 12:22:41 | VENDEU: Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-6 | 12:22:42 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Colosso | DA_KogMaw18_AD | 0.7900 |  |
| Jogador 7 | 4-6 | 12:22:43 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Colosso | DA_KogMaw18_AD | 0.4800 |  |
| Jogador 7 | 4-6 | 12:22:43 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 4-6 | 12:22:44 | MOVE Board -> Board: Vi (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-6 | 12:22:45 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 3 | Colosso | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 7 | 4-7 | 12:23:35 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Colosso | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 7 | 4-7 | 12:23:36 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Colosso | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 7 | 4-7 | 12:23:37 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Colosso | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 7 | 4-7 | 12:23:37 | COMPROU: Ashe (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 7 | 4-7 | 12:23:38 | MOVE Board -> Board: Diana (i:6.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 4-7 | 12:23:38 | MOVE Board -> Board: Rakan (i:4.0) <-> Varus (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 4-7 | 12:23:39 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Colosso | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 7 | 5-1 | 12:24:34 | VENDEU: Hecarim (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 74 | 5 | Colosso | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 7 | 5-1 | 12:24:34 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_KogMaw18_AD | 0.4200 |  |
| Jogador 7 | 5-1 | 12:24:35 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-1 | 12:24:35 | MOVE Board -> Board: Diana (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-1 | 12:24:36 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 71 | 5 | Colosso | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 7 | 5-2 | 12:25:24 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 5-2 | 12:25:25 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_KogMaw18_AD | 0.5300 |  |
| Jogador 7 | 5-2 | 12:25:25 | MOVE Board -> Board: Varus (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-2 | 12:25:26 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 5-2 | 12:25:26 | MOVE Board -> Board: Diana (i:6.0) <-> Varus (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-2 | 12:25:26 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 86 | 5 | Colosso | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 7 | 5-3 | 12:26:22 | VENDEU: Ashe (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 105 | 5 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 7 | 5-3 | 12:26:22 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_KogMaw18_AD | 0.3500 |  |
| Jogador 7 | 5-3 | 12:26:22 | MOVE Board -> Board: Varus (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-3 | 12:26:23 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-3 | 12:26:23 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 5-3 | 12:26:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 102 | 5 | Colosso | DA_KogMaw18_AD | -0.1300 |  |
| Jogador 7 | 5-4 | 12:27:15 | VENDEU: Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 116 | 5 | Colosso | DA_KogMaw18_AD | -0.5900 |  |
| Jogador 7 | 5-4 | 12:27:17 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 113 | 5 | Colosso | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 7 | 5-4 | 12:27:18 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 5-4 | 12:27:18 | MOVE Board -> Board: Vi (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-4 | 12:27:19 | MOVE Board -> Board: Diana (i:6.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-4 | 12:27:19 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Colosso | DA_KogMaw18_AD | -0.2900 |  |
| Jogador 7 | 5-5 | 12:28:21 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Colosso | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 7 | 5-5 | 12:28:21 | MOVE Board -> Board: Rakan (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-5 | 12:28:22 | MOVE Board -> Board: Diana (i:6.0) <-> Varus (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 5-5 | 12:28:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Colosso | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 7 | 5-6 | 12:29:28 | VENDEU: Tristana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Colosso | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 7 | 5-6 | 12:29:29 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 141 | 5 | Colosso | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 7 | 5-6 | 12:29:29 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 141 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-6 | 12:29:30 | MOVE Board -> Board: Varus (i:4.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 141 | 5 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-6 | 12:29:30 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 141 | 5 | Colosso | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 7 | 5-7 | 12:30:26 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Varus (i:4.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Colosso | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 7 | 5-7 | 12:30:26 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Colosso | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 7 | 5-7 | 12:30:27 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 152 | 5 | Colosso | DA_KogMaw18_AD | 0.4400 |  |
| Jogador 7 | 5-7 | 12:30:27 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 152 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-7 | 12:30:28 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Colosso | DA_KogMaw18_AD | -0.4800 |  |
| Jogador 7 | 5-7 | 12:30:28 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 152 | 5 | Colosso | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 7 | 5-7 | 12:30:28 | MOVE Board -> Board: Vi (i:6.0) <-> Varus (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 152 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 5-7 | 12:30:29 | MOVE Board -> Board: Varus (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 152 | 5 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 5-7 | 12:30:29 | MOVE Board -> Board: Diana (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 152 | 5 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 6-1 | 12:32:00 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 164 | 5 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 6-1 | 12:32:00 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 161 | 5 | Colosso | DA_KogMaw18_AD | 0.8500 |  |
| Jogador 7 | 6-1 | 12:32:01 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 164 | 5 | Colosso | DA_KogMaw18_AD | -0.4600 |  |
| Jogador 7 | 6-1 | 12:32:01 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 162 | 5 | Colosso | DA_KogMaw18_AD | 1.0100 |  |
| Jogador 7 | 6-1 | 12:32:02 | COMPROU: Varus (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 161 | 5 | Colosso | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 7 | 6-1 | 12:32:02 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 160 | 5 | Colosso | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 7 | 6-1 | 12:32:02 | MOVE Board -> Board: Diana (i:6.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 160 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 6-1 | 12:32:03 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 160 | 5 | Colosso | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 6-1 | 12:32:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 160 | 5 | Colosso | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 7 | 6-2 | 12:33:37 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 176 | 5 | Colosso | DA_KogMaw18_AD | -0.6000 |  |
| Jogador 7 | 6-2 | 12:33:38 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 173 | 5 | Colosso | DA_KogMaw18_AD | 1.0800 |  |
| Jogador 7 | 6-2 | 12:33:38 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 171 | 5 | Colosso | DA_KogMaw18_AD | 0.6200 |  |
| Jogador 7 | 6-2 | 12:33:38 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 168 | 5 | Colosso | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 7 | 6-2 | 12:33:39 | REROLL | STABILIZE | STABILIZE: pressão de vida | 166 | 5 | Colosso | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 7 | 6-2 | 12:33:39 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 174 | 5 | Colosso | DA_KogMaw18_AD | -0.6000 |  |
| Jogador 7 | 6-2 | 12:33:39 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 171 | 5 | Colosso | DA_KogMaw18_AD | 1.0000 |  |
| Jogador 7 | 6-2 | 12:33:40 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 174 | 5 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 6-2 | 12:33:40 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 173 | 5 | Colosso | DA_KogMaw18_AD | 0.4200 |  |
| Jogador 7 | 6-3 | 12:35:02 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 187 | 5 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 6-3 | 12:35:02 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 184 | 5 | Colosso | DA_KogMaw18_AD | 1.1100 |  |
| Jogador 7 | 6-3 | 12:35:02 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 182 | 5 | Colosso | DA_KogMaw18_AD | 0.2700 |  |
| Jogador 7 | 6-3 | 12:35:03 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 181 | 5 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 7 | 6-3 | 12:35:03 | VENDEU: Kog'Maw (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 189 | 5 | Colosso | DA_KogMaw18_AD | -0.9500 |  |
| Jogador 7 | 6-3 | 12:35:04 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 187 | 5 | Colosso | DA_KogMaw18_AD | -0.2900 |  |
| Jogador 7 | 6-3 | 12:35:04 | VENDEU: Cascalho (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 188 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 6-3 | 12:35:05 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 186 | 5 | Colosso | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 7 | 6-3 | 12:35:05 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 184 | 5 | Colosso | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 7 | 6-4 | 12:36:38 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 197 | 5 | Colosso | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 7 | 6-4 | 12:36:38 | COMPROU: Varus (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 196 | 5 | Colosso | DA_KogMaw18_AD | 1.0200 |  |
| Jogador 7 | 6-4 | 12:36:39 | VENDEU: Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 198 | 5 | Colosso | DA_KogMaw18_AD | -0.5200 |  |
| Jogador 7 | 6-4 | 12:36:39 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 195 | 5 | Colosso | DA_KogMaw18_AD | 1.1100 |  |
| Jogador 7 | 6-4 | 12:36:40 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 195 | 5 | Colosso | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 7 | 6-4 | 12:36:40 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 192 | 5 | Colosso | DA_KogMaw18_AD | 0.4900 |  |
| Jogador 7 | 6-4 | 12:36:41 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 192 | 5 | Colosso | DA_KogMaw18_AD | 0.4400 |  |
| Jogador 7 | 6-4 | 12:36:41 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 190 | 5 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 6-4 | 12:36:42 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 190 | 5 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 8 | ? | 12:12:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | ? | 12:12:46 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | ? | 12:12:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 12:12:51 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 12:12:52 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-1 | 12:12:52 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-1 | 12:12:53 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3600 |  |
| Jogador 8 | 1-1 | 12:12:54 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-1 | 12:12:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 12:12:56 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5000 |  |
| Jogador 8 | 1-2 | 12:12:59 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 8 | 1-2 | 12:12:59 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 8 | 1-2 | 12:13:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 12:13:07 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-3 | 12:13:07 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 8 | 1-3 | 12:13:09 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1700 |  |
| Jogador 8 | 1-3 | 12:13:09 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 8 | 1-3 | 12:13:10 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 8 | 1-3 | 12:13:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 12:13:17 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.1100 |  |
| Jogador 8 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 1-4 | 12:13:17 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 1-4 | 12:13:18 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 1-4 | 12:13:18 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 1.1000 |  |
| Jogador 8 | 1-4 | 12:13:19 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 1-4 | 12:13:19 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 1-4 | 12:13:20 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.3200 |  |
| Jogador 8 | 1-4 | 12:13:20 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 2-1 | 12:13:26 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-1 | 12:13:26 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.3000 |  |
| Jogador 8 | 2-1 | 12:13:27 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | -0.2100 |  |
| Jogador 8 | 2-1 | 12:13:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-1 | 12:13:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-2 | 12:13:36 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | 1.0500 |  |
| Jogador 8 | 2-2 | 12:13:36 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | 0.3600 |  |
| Jogador 8 | 2-2 | 12:13:37 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-2 | 12:13:38 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2300 |  |
| Jogador 8 | 2-2 | 12:13:38 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | -0.1300 |  |
| Jogador 8 | 2-2 | 12:13:39 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | -0.1500 |  |
| Jogador 8 | 2-2 | 12:13:39 | MOVE Bench -> Board: Karma (i:2.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | -0.5300 |  |
| Jogador 8 | 2-2 | 12:13:40 | MOVE Bench -> Board: Karma (i:4.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-2 | 12:13:40 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 2-3 | 12:13:49 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_Karma18 | 0.2700 |  |
| Jogador 8 | 2-3 | 12:13:49 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 2-3 | 12:13:50 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-3 | 12:13:51 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Karma18 | 0.4800 |  |
| Jogador 8 | 2-3 | 12:13:52 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 2-3 | 12:13:52 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_Karma18 | -0.4000 |  |
| Jogador 8 | 2-3 | 12:13:53 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_Karma18 | -0.3100 |  |
| Jogador 8 | 2-3 | 12:13:53 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_Karma18 | 0.0400 |  |
| Jogador 8 | 2-3 | 12:13:53 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_Karma18 | -0.3600 |  |
| Jogador 8 | 2-4 | 12:14:03 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_Karma18 | 1.0400 |  |
| Jogador 8 | 2-4 | 12:14:03 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_Karma18 | 0.3700 |  |
| Jogador 8 | 2-4 | 12:14:04 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_Karma18 | 0.2900 |  |
| Jogador 8 | 2-4 | 12:14:04 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_Karma18 | -0.4900 |  |
| Jogador 8 | 2-4 | 12:14:05 | MOVE Bench -> Board: Rammus (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_Karma18 | -0.3100 |  |
| Jogador 8 | 2-4 | 12:14:06 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_Karma18 | -0.5800 |  |
| Jogador 8 | 2-4 | 12:14:06 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-4 | 12:14:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-4 | 12:14:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Enfeitiçador | DA_Karma18 | -0.1200 |  |
| Jogador 8 | 2-5 | 12:14:18 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_Karma18 | 0.3300 |  |
| Jogador 8 | 2-5 | 12:14:19 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-5 | 12:14:19 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 2-5 | 12:14:20 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-5 | 12:14:20 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_Karma18 | -0.3200 |  |
| Jogador 8 | 2-5 | 12:14:21 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_Karma18 | -0.4200 |  |
| Jogador 8 | 2-5 | 12:14:21 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_Karma18 | -0.1900 |  |
| Jogador 8 | 2-5 | 12:14:22 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Enfeitiçador | DA_Karma18 | -1.0200 |  |
| Jogador 8 | 2-5 | 12:14:22 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-6 | 12:14:35 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Enfeitiçador | DA_Karma18 | 0.2700 |  |
| Jogador 8 | 2-6 | 12:14:35 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-6 | 12:14:36 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 2-6 | 12:14:36 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_Karma18 | 0.2100 |  |
| Jogador 8 | 2-6 | 12:14:37 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_Karma18 | -0.4200 |  |
| Jogador 8 | 2-6 | 12:14:37 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_Karma18 | -0.3200 |  |
| Jogador 8 | 2-6 | 12:14:38 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Enfeitiçador | DA_Karma18 | -0.1800 |  |
| Jogador 8 | 2-6 | 12:14:38 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-6 | 12:14:39 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Enfeitiçador | DA_Karma18 | -0.4000 |  |
| Jogador 8 | 2-7 | 12:14:53 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Enfeitiçador | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-7 | 12:14:54 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-7 | 12:14:54 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-7 | 12:14:55 | MOVE Bench -> Board: Karma (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_Karma18 | -0.1300 |  |
| Jogador 8 | 2-7 | 12:14:55 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_Karma18 | -0.6500 |  |
| Jogador 8 | 2-7 | 12:14:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_Karma18 | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-1 | 12:15:13 | MOVE Bench -> Board: Lillia (i:8.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-1 | 12:15:14 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 3-1 | 12:15:14 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 3-1 | 12:15:15 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 3-1 | 12:15:15 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | 0.1000 |  |
| Jogador 8 | 3-1 | 12:15:16 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 3-1 | 12:15:16 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Enfeitiçador | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 3-1 | 12:15:17 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_Karma18 | -0.2600 |  |
| Jogador 8 | 3-1 | 12:15:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 3-2 | 12:15:34 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_Karma18 | 0.3100 |  |
| Jogador 8 | 3-2 | 12:15:35 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_Karma18 | 0.5300 |  |
| Jogador 8 | 3-2 | 12:15:35 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 3-2 | 12:15:36 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_Karma18 | -0.3100 |  |
| Jogador 8 | 3-2 | 12:15:36 | MOVE Board -> Board: Lillia (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 3-2 | 12:15:36 | MOVE Bench -> Board: Rammus (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_Karma18 | -0.2900 |  |
| Jogador 8 | 3-2 | 12:15:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_Karma18 | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-3 | 12:15:57 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Enfeitiçador | DA_Karma18 | 0.8500 |  |
| Jogador 8 | 3-3 | 12:15:57 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Enfeitiçador | DA_Karma18 | 0.1000 |  |
| Jogador 8 | 3-3 | 12:15:58 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Enfeitiçador | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 3-3 | 12:15:59 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_Karma18 | -0.2100 |  |
| Jogador 8 | 3-3 | 12:15:59 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 3-3 | 12:15:59 | MOVE Bench -> Board: Karma (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 3-3 | 12:16:00 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_Karma18 | -0.6500 |  |
| Jogador 8 | 3-3 | 12:16:00 | MOVE Bench -> Board: Rammus (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_Karma18 | -0.3700 |  |
| Jogador 8 | 3-3 | 12:16:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Enfeitiçador | DA_Karma18 | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-4 | 12:16:22 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Enfeitiçador | DA_Karma18 | 0.7400 |  |
| Jogador 8 | 3-4 | 12:16:23 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Enfeitiçador | DA_Karma18 | 0.8600 |  |
| Jogador 8 | 3-4 | 12:16:24 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Enfeitiçador | DA_Karma18 | 0.3000 |  |
| Jogador 8 | 3-4 | 12:16:24 | MOVE Bench -> Board: Karma (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Enfeitiçador | DA_Karma18 | -0.0600 |  |
| Jogador 8 | 3-4 | 12:16:25 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Enfeitiçador | DA_Karma18 | -0.6600 |  |
| Jogador 8 | 3-4 | 12:16:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 3 | Enfeitiçador | DA_Karma18 | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-5 | 12:16:50 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Enfeitiçador | DA_Karma18 | 0.8300 |  |
| Jogador 8 | 3-5 | 12:16:51 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Enfeitiçador | DA_Karma18 | -0.5800 |  |
| Jogador 8 | 3-5 | 12:16:51 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Enfeitiçador | DA_Karma18 | 0.3100 |  |
| Jogador 8 | 3-5 | 12:16:52 | MOVE Bench -> Board: Rammus (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Enfeitiçador | DA_Karma18 | -0.2700 |  |
| Jogador 8 | 3-5 | 12:16:52 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-5 | 12:16:53 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_Karma18 | 0.2900 |  |
| Jogador 8 | 3-5 | 12:16:54 | MOVE Bench -> Board: Karma (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 3-5 | 12:16:54 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_Karma18 | -0.6500 |  |
| Jogador 8 | 3-5 | 12:16:55 | MOVE Bench -> Board: Rammus (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_Karma18 | -0.4100 |  |
| Jogador 8 | 3-6 | 12:17:21 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-6 | 12:17:22 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Enfeitiçador | DA_Karma18 | 0.1300 |  |
| Jogador 8 | 3-6 | 12:17:22 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-6 | 12:17:23 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Enfeitiçador | DA_Karma18 | -0.2000 |  |
| Jogador 8 | 3-6 | 12:17:23 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-6 | 12:17:24 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Enfeitiçador | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 3-6 | 12:17:24 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-6 | 12:17:24 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_Karma18 | -0.2600 |  |
| Jogador 8 | 3-6 | 12:17:25 | MOVE Board -> Board: Master Yi (i:6.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-7 | 12:17:54 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 3-7 | 12:17:55 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_Karma18 | 0.2500 |  |
| Jogador 8 | 3-7 | 12:17:56 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 3-7 | 12:17:56 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_Karma18 | 0.9600 |  |
| Jogador 8 | 3-7 | 12:17:57 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Enfeitiçador | DA_Karma18 | 0.7400 |  |
| Jogador 8 | 3-7 | 12:17:57 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Enfeitiçador | DA_Karma18 | 0.6000 |  |
| Jogador 8 | 3-7 | 12:17:59 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Enfeitiçador | DA_Karma18 | -0.1500 |  |
| Jogador 8 | 3-7 | 12:17:59 | MOVE Board -> Board: Karma (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-7 | 12:18:00 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-1 | 12:18:34 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Enfeitiçador | DA_Karma18 | -0.5900 |  |
| Jogador 8 | 4-1 | 12:18:35 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Enfeitiçador | DA_Karma18 | 0.8400 |  |
| Jogador 8 | 4-1 | 12:18:36 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 4-1 | 12:18:37 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Enfeitiçador | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 4-1 | 12:18:37 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-1 | 12:18:38 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Enfeitiçador | DA_Karma18 | -0.2100 |  |
| Jogador 8 | 4-1 | 12:18:38 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 4-1 | 12:18:39 | VENDEU: Sivir (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Enfeitiçador | DA_Karma18 | -0.3500 |  |
| Jogador 8 | 4-1 | 12:18:39 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Enfeitiçador | DA_Karma18 | -0.5300 |  |
| Jogador 8 | 4-2 | 12:19:19 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 91 | 5 | Enfeitiçador | DA_Karma18 | 0.9200 |  |
| Jogador 8 | 4-2 | 12:19:20 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Enfeitiçador | DA_Karma18 | 0.3800 |  |
| Jogador 8 | 4-2 | 12:19:21 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Enfeitiçador | DA_Karma18 | 0.1700 |  |
| Jogador 8 | 4-2 | 12:19:21 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 4-2 | 12:19:22 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Enfeitiçador | DA_Karma18 | -0.1700 |  |
| Jogador 8 | 4-2 | 12:19:22 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-2 | 12:19:23 | MOVE Board -> Board: Lillia (i:8.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-2 | 12:19:23 | MOVE Board -> Board: Master Yi (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Enfeitiçador | DA_Karma18 | -0.0700 |  |
| Jogador 8 | 4-2 | 12:19:24 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Enfeitiçador | DA_Karma18 | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 4-3 | 12:20:00 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 95 | 5 | Enfeitiçador | DA_Karma18 | 0.9000 |  |
| Jogador 8 | 4-3 | 12:20:00 | VENDEU: Malphite (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Enfeitiçador | DA_Karma18 | -0.4100 |  |
| Jogador 8 | 4-3 | 12:20:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Enfeitiçador | DA_Karma18 | 0.9600 |  |
| Jogador 8 | 4-3 | 12:20:02 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Enfeitiçador | DA_Karma18 | 0.9600 |  |
| Jogador 8 | 4-3 | 12:20:02 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Enfeitiçador | DA_Karma18 | 0.6400 |  |
| Jogador 8 | 4-3 | 12:20:03 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 95 | 5 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 4-3 | 12:20:04 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 94 | 5 | Enfeitiçador | DA_Karma18 | -0.2800 |  |
| Jogador 8 | 4-3 | 12:20:04 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 94 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-3 | 12:20:05 | MOVE Board -> Board: Lillia (i:8.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 94 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-4 | 12:20:49 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Enfeitiçador | DA_Karma18 | 0.3800 |  |
| Jogador 8 | 4-4 | 12:20:50 | VENDEU: LeBlanc (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Enfeitiçador | DA_Karma18 | -0.6000 |  |
| Jogador 8 | 4-4 | 12:20:51 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Enfeitiçador | DA_Karma18 | 0.1600 |  |
| Jogador 8 | 4-4 | 12:20:51 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Enfeitiçador | DA_Karma18 | -0.5900 |  |
| Jogador 8 | 4-4 | 12:20:52 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Karma (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Enfeitiçador | DA_Karma18 | 0.1300 |  |
| Jogador 8 | 4-4 | 12:20:52 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Karma (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Enfeitiçador | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 4-4 | 12:20:53 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Karma (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Enfeitiçador | DA_Karma18 | 0.1300 |  |
| Jogador 8 | 4-4 | 12:20:53 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Enfeitiçador | DA_Karma18 | -0.2200 |  |
| Jogador 8 | 4-4 | 12:20:54 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-5 | 12:21:48 | VENDEU: Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 4-5 | 12:21:48 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Enfeitiçador | DA_Karma18 | 1.0000 |  |
| Jogador 8 | 4-5 | 12:21:49 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 4-5 | 12:21:49 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Enfeitiçador | DA_Karma18 | -0.2800 |  |
| Jogador 8 | 4-5 | 12:21:50 | VENDEU: Cassiopeia (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Enfeitiçador | DA_Karma18 | -0.6800 |  |
| Jogador 8 | 4-5 | 12:21:51 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Enfeitiçador | DA_Karma18 | -0.2900 |  |
| Jogador 8 | 4-5 | 12:21:51 | VENDEU: Rubrivirim (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 4-5 | 12:21:52 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Enfeitiçador | DA_Karma18 | -0.2900 |  |
| Jogador 8 | 4-5 | 12:21:52 | MOVE Board -> Board: Karma (i:2.0) <-> Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Enfeitiçador | DA_Karma18 | 0.0400 |  |
| Jogador 8 | 4-6 | 12:22:40 | VENDEU: Rubrivirim (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 4-6 | 12:22:41 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Enfeitiçador | DA_Karma18 | 0.6000 |  |
| Jogador 8 | 4-6 | 12:22:41 | VENDEU: Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 4-6 | 12:22:42 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Enfeitiçador | DA_Karma18 | 0.2800 |  |
| Jogador 8 | 4-6 | 12:22:43 | VENDEU: Ornn (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-6 | 12:22:43 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 4-6 | 12:22:44 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-6 | 12:22:45 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 4-6 | 12:22:45 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Enfeitiçador | DA_Karma18 | -0.0700 |  |
| Jogador 8 | 4-7 | 12:23:35 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Enfeitiçador | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 4-7 | 12:23:36 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NegatronCloak -> Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Enfeitiçador | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 4-7 | 12:23:37 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 4-7 | 12:23:37 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Enfeitiçador | DA_Karma18 | -0.2200 |  |
| Jogador 8 | 4-7 | 12:23:38 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 4-7 | 12:23:38 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 4-7 | 12:23:39 | VENDEU: Ornn (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 4-7 | 12:23:40 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Enfeitiçador | DA_Karma18 | -0.2800 |  |
| Jogador 8 | 4-7 | 12:23:40 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Enfeitiçador | DA_Karma18 | -0.0700 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 24 | 25 | 125 | 24 | 15 | 183 | 7 | 28 |
| Jogador 2 | 40 | 40 | 200 | 40 | 18 | 332 | 13 | 36 |
| Jogador 3 | 40 | 40 | 200 | 40 | 18 | 272 | 4 | 47 |
| Jogador 4 | 26 | 30 | 150 | 26 | 17 | 196 | 8 | 29 |
| Jogador 5 | 24 | 28 | 140 | 24 | 15 | 186 | 10 | 17 |
| Jogador 6 | 28 | 30 | 150 | 28 | 17 | 202 | 13 | 35 |
| Jogador 7 | 37 | 39 | 195 | 37 | 17 | 243 | 5 | 28 |
| Jogador 8 | 26 | 28 | 140 | 26 | 16 | 205 | 3 | 44 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 183 | 183 | 183 | 0 | 178 | 0 | 183 | 183 | 183 | 62/47 |
| Jogador 2 | 332 | 332 | 332 | 0 | 318 | 0 | 332 | 332 | 332 | 125/109 |
| Jogador 3 | 272 | 272 | 272 | 0 | 263 | 0 | 272 | 272 | 272 | 79/63 |
| Jogador 4 | 196 | 196 | 196 | 0 | 183 | 0 | 196 | 196 | 196 | 73/59 |
| Jogador 5 | 186 | 186 | 186 | 0 | 181 | 0 | 186 | 186 | 186 | 84/70 |
| Jogador 6 | 202 | 202 | 202 | 0 | 189 | 0 | 202 | 202 | 202 | 71/58 |
| Jogador 7 | 243 | 243 | 243 | 0 | 233 | 0 | 243 | 243 | 243 | 70/55 |
| Jogador 8 | 205 | 205 | 205 | 0 | 195 | 0 | 205 | 205 | 205 | 83/69 |

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
| Jogador 1 | 1-2 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42622989416122437 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3469875156879425 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25063249468803406 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0387812852859497 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 40 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0314135551452637 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 41 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9796043038368225 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19132192432880402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17696425318717957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 55 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 56 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3359656035900116 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 63 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12942641973495483 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 2-2 | 64 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060604825615882874 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2755759060382843 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00807955488562584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 68 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17284248769283295 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 2-2 | 69 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32699888944625854 | 0.0 | 0.0 | +e76c0caf-1c3d-493f-9a21-659dd8587fc2 / -— |
| Jogador 1 | 2-2 | 70 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.352742463350296 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 74 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3345659673213959 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 75 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17832036316394806 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 1 | 2-3 | 76 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15093669295310974 | 0.0 | 0.0 | +— / -e76c0caf-1c3d-493f-9a21-659dd8587fc2 |
| Jogador 1 | 2-3 | 77 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 78 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1169791221618652 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3642217814922333 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 84 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4286663234233856 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 85 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012633305042982101 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 87 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0242440700531006 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3258442282676697 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 94 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 1 | 2-5 | 95 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0037288148887455463 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 97 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06561169028282166 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 98 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004718039184808731 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 99 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015006372705101967 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 100 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479967594146729 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 10.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07185867428779602 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 3 | 0 | 10.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27010682225227356 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 105 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 3 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2985334098339081 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 106 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06937354803085327 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.690438698977232e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014103122986853123 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 109 | PASS | STABILIZE | 95.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 112 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0474052429199219 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-7 | 113 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9376266598701477 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 4 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3587802052497864 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 115 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 116 | PASS | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 6 | 10 | 1 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2631056606769562 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 123 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 10 | 1 | 20.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08154261857271194 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 124 | BUY_XP | STABILIZE | 95.0 | 6 | 10 | 1 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 125 | BUY_XP | STABILIZE | 95.0 | 6 | 6 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0023640748113393784 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 127 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 2 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3987067639827728 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 128 | BUY | STABILIZE | 95.0 | 6 | 2 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01202577818185091 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 1 | 3-1 | 129 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0014168692287057638 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 130 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015427687205374241 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 132 | BUY | STABILIZE | 85.0 | 6 | 5 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10312627255916595 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 1 | 3-2 | 133 | BUY | STABILIZE | 85.0 | 6 | 2 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0011185503099113703 | 0.0 | 0.0 | +dc9a3df1-7032-4c92-a919-ca17ae7639ea / -— |
| Jogador 1 | 3-2 | 134 | SELL | STABILIZE | 85.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0689999982714653 | 0.0 | 0.0 | +— / -dc9a3df1-7032-4c92-a919-ca17ae7639ea |
| Jogador 1 | 3-2 | 135 | SELL | STABILIZE | 85.0 | 6 | 2 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07505988329648972 | 0.0 | 0.0 | +— / -8e819ba6-a356-4d9b-a8c9-7493332900fb |
| Jogador 1 | 3-2 | 136 | BUY_XP | STABILIZE | 85.0 | 6 | 4 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013103440403938293 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0040281699039042 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 139 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01613207347691059 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 140 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 142 | BUY | STABILIZE | 75.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009283797815442085 | 0.0 | 0.0 | +e6ee6b15-d413-4678-8ffb-29272199a53d / -— |
| Jogador 1 | 3-3 | 143 | BUY | STABILIZE | 75.0 | 6 | 3 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009427152574062347 | 0.0 | 0.0 | +c30e7bdb-41d6-423c-9d7d-2e146472e724 / -— |
| Jogador 1 | 3-3 | 144 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013033933937549591 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 145 | SELL | STABILIZE | 75.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04137369990348816 | 0.0 | 0.0 | +— / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 3-3 | 146 | BUY | STABILIZE | 75.0 | 6 | 3 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18465444445610046 | 0.0 | 0.0 | +45450b46-63b4-488f-9469-3348c6da8f4b / -— |
| Jogador 1 | 3-3 | 147 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 148 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001247776672244072 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028704911470413208 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 0 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004617859143763781 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 152 | BUY | STABILIZE | 75.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001238382887095213 | 0.0 | 0.0 | +0450963e-c7e2-4ff5-a2f5-09e65fa63527 / -— |
| Jogador 1 | 3-4 | 153 | BUY | STABILIZE | 75.0 | 6 | 4 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006790158338844776 | 0.0 | 0.0 | +54b47885-6cb9-42e7-a9bb-049e0e2d2956 / -— |
| Jogador 1 | 3-4 | 154 | SELL | STABILIZE | 75.0 | 6 | 3 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02176666632294655 | 0.0 | 0.0 | +— / -54b47885-6cb9-42e7-a9bb-049e0e2d2956 |
| Jogador 1 | 3-4 | 155 | BUY | STABILIZE | 75.0 | 6 | 4 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08058388531208038 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 156 | SELL | STABILIZE | 75.0 | 6 | 2 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -bddefab1-7dd7-4954-816c-45dbd44b947b |
| Jogador 1 | 3-4 | 157 | SELL | STABILIZE | 75.0 | 6 | 4 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36899998784065247 | 0.0 | 0.0 | +— / -0450963e-c7e2-4ff5-a2f5-09e65fa63527 |
| Jogador 1 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005348100792616606 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015231316909193993 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 160 | PASS | STABILIZE | 75.0 | 6 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 162 | BUY | STABILIZE | 75.0 | 6 | 11 | 1 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7547684907913208 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 163 | MOVE_BENCH | STABILIZE | 75.0 | 6 | 9 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13319534063339233 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 164 | BUY | STABILIZE | 75.0 | 6 | 9 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016370702534914017 | 0.0 | 0.0 | +a9184317-58b7-4804-9aef-3e2c08c20935 / -— |
| Jogador 1 | 3-5 | 165 | BUY | STABILIZE | 75.0 | 6 | 8 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4374462366104126 | 0.0 | 0.0 | +f6e6e08d-ecfe-4c84-acfa-6ad8292968ee / -— |
| Jogador 1 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 75.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33450397849082947 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 7 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 7 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06460696458816528 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 169 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 7 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04749276116490364 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 170 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 7 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 172 | BUY | STABILIZE | 66.0 | 6 | 12 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7988572716712952 | 0.0 | 0.0 | +600071dd-5c17-4f03-903f-d1cd6c20bb28 / -— |
| Jogador 1 | 3-6 | 173 | SELL | STABILIZE | 66.0 | 6 | 11 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 |
| Jogador 1 | 3-6 | 174 | BUY | STABILIZE | 66.0 | 6 | 16 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28429898619651794 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -— |
| Jogador 1 | 3-6 | 175 | SELL | STABILIZE | 66.0 | 6 | 14 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007366666570305824 | 0.0 | 0.0 | +— / -c30e7bdb-41d6-423c-9d7d-2e146472e724 |
| Jogador 1 | 3-6 | 176 | BUY | STABILIZE | 66.0 | 6 | 17 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.804197371006012 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 66.0 | 6 | 15 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.724442159291357e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 66.0 | 6 | 15 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01503919716924429 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 179 | MOVE_BOARD | STABILIZE | 66.0 | 6 | 15 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005556438583880663 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 180 | PASS | STABILIZE | 66.0 | 6 | 15 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 182 | SELL | STABILIZE | 57.0 | 6 | 22 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022099999710917473 | 0.0 | 0.0 | +— / -e6ee6b15-d413-4678-8ffb-29272199a53d |
| Jogador 1 | 3-7 | 183 | BUY | STABILIZE | 57.0 | 6 | 25 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1008458361029625 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 1 | 3-7 | 184 | SELL | STABILIZE | 57.0 | 6 | 21 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -45450b46-63b4-488f-9469-3348c6da8f4b |
| Jogador 1 | 3-7 | 185 | BUY | STABILIZE | 57.0 | 6 | 24 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013018590398132801 | 0.0 | 0.0 | +c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 / -— |
| Jogador 1 | 3-7 | 186 | SELL | STABILIZE | 57.0 | 6 | 22 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 |
| Jogador 1 | 3-7 | 187 | BUY | STABILIZE | 57.0 | 6 | 24 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013021023944020271 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 1 | 3-7 | 188 | SELL | STABILIZE | 57.0 | 6 | 22 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -227dbcdb-af5c-4318-94d1-f01a7847d100 |
| Jogador 1 | 3-7 | 189 | BUY | STABILIZE | 57.0 | 6 | 24 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0889650285243988 | 0.0 | 0.0 | +0d8cf876-2884-4724-ab79-246f8e0406f0 / -— |
| Jogador 1 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 57.0 | 6 | 22 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001351501909084618 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 57.0 | 6 | 30 | 3 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19401468336582184 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 57.0 | 6 | 30 | 3 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20381973683834076 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 194 | SELL | STABILIZE | 57.0 | 6 | 30 | 3 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00026666666963137686 | 0.0 | 0.0 | +— / -0d8cf876-2884-4724-ab79-246f8e0406f0 |
| Jogador 1 | 4-1 | 195 | BUY | STABILIZE | 57.0 | 6 | 32 | 3 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005328916013240814 | 0.0 | 0.0 | +e7c8751e-5d30-4953-9508-35488b6c45db / -— |
| Jogador 1 | 4-1 | 196 | SELL | STABILIZE | 57.0 | 6 | 29 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056166667491197586 | 0.0 | 0.0 | +— / -e7c8751e-5d30-4953-9508-35488b6c45db |
| Jogador 1 | 4-1 | 197 | BUY | STABILIZE | 57.0 | 6 | 32 | 3 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07156393676996231 | 0.0 | 0.0 | +502a6e8c-8f81-456f-a1ef-c6bb8dd6fc7e / -— |
| Jogador 1 | 4-1 | 198 | SELL | STABILIZE | 57.0 | 6 | 29 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07132404297590256 | 0.0 | 0.0 | +— / -502a6e8c-8f81-456f-a1ef-c6bb8dd6fc7e |
| Jogador 1 | 4-1 | 199 | BUY | STABILIZE | 57.0 | 6 | 32 | 3 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08636299520730972 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 1 | 4-1 | 200 | SELL | STABILIZE | 57.0 | 6 | 29 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07263333350419998 | 0.0 | 0.0 | +— / -844f869e-0e0e-423a-8507-27efd66131f5 |
| Jogador 1 | 4-2 | 202 | BUY | STABILIZE | 45.0 | 6 | 41 | 4 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3779984712600708 | 0.0 | 0.0 | +6fa83356-562b-4a26-a77d-3e989089e70a / -— |
| Jogador 1 | 4-2 | 203 | SELL | STABILIZE | 45.0 | 6 | 40 | 4 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027315447106957436 | 0.0 | 0.0 | +— / -7306c9be-466e-498c-819e-274ff070c72b |
| Jogador 1 | 4-2 | 204 | BUY | STABILIZE | 45.0 | 6 | 44 | 4 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06202924996614456 | 0.0 | 0.0 | +301afc05-ad23-4ed2-a835-108235c399e0 / -— |
| Jogador 1 | 4-2 | 205 | SELL | STABILIZE | 45.0 | 6 | 42 | 4 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -301afc05-ad23-4ed2-a835-108235c399e0 |
| Jogador 1 | 4-2 | 206 | BUY | STABILIZE | 45.0 | 6 | 44 | 4 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28330910205841064 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 1 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 45.0 | 6 | 41 | 4 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 45.0 | 6 | 41 | 4 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014208241365849972 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 209 | PASS | STABILIZE | 45.0 | 6 | 41 | 4 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04357142746448517 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 212 | SELL | STABILIZE | 33.0 | 6 | 51 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -5af104f2-7959-4ca5-91a9-7d44494532ea |
| Jogador 1 | 4-3 | 213 | BUY | STABILIZE | 33.0 | 6 | 54 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9617370963096619 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8,d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 4-3 | 214 | BUY | STABILIZE | 33.0 | 6 | 52 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3146514594554901 | 0.0 | 0.0 | +6388773b-0e99-40a9-8d68-895dcf16fce6 / -— |
| Jogador 1 | 4-3 | 215 | BUY | STABILIZE | 33.0 | 6 | 49 | 4 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017337758094072342 | 0.0 | 0.0 | +ea460790-b046-451d-9174-8b613e476241 / -— |
| Jogador 1 | 4-3 | 216 | SELL | STABILIZE | 33.0 | 6 | 48 | 4 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5098999738693237 | 0.0 | 0.0 | +— / -5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 |
| Jogador 1 | 4-3 | 217 | BUY | STABILIZE | 33.0 | 6 | 53 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06743886321783066 | 0.0 | 0.0 | +cb30dcaa-bc26-4584-9b50-24e47e70fcb0 / -— |
| Jogador 1 | 4-3 | 218 | SELL | STABILIZE | 33.0 | 6 | 52 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026666666381061077 | 0.0 | 0.0 | +— / -cb30dcaa-bc26-4584-9b50-24e47e70fcb0 |
| Jogador 1 | 4-3 | 219 | SELL | STABILIZE | 33.0 | 6 | 53 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3959016501903534 | 0.0 | 0.0 | +— / -ea460790-b046-451d-9174-8b613e476241 |
| Jogador 1 | 4-3 | 220 | REROLL | STABILIZE | 33.0 | 6 | 54 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 222 | BUY | ALL_IN | 22.0 | 7 | 64 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3847157955169678 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 1 | 4-4 | 223 | BUY | ALL_IN | 22.0 | 7 | 61 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3965468406677246 | 0.0 | 0.0 | +ea88d306-ae6b-4dbe-b559-3371ba39613a / -— |
| Jogador 1 | 4-4 | 224 | SELL | ALL_IN | 22.0 | 7 | 58 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5536999702453613 | 0.0 | 0.0 | +— / -a9184317-58b7-4804-9aef-3e2c08c20935 |
| Jogador 1 | 4-4 | 225 | BUY | ALL_IN | 22.0 | 7 | 59 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1464194655418396 | 0.0 | 0.0 | +b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 / -— |
| Jogador 1 | 4-4 | 226 | MOVE_BENCH | ALL_IN | 22.0 | 7 | 55 | 5 | 26.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4002104103565216 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 227 | BUY | ALL_IN | 22.0 | 7 | 55 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11768779158592224 | 0.0 | 0.0 | +fb551efa-6ad5-4f97-aa05-bc5eb70943d4 / -— |
| Jogador 1 | 4-4 | 228 | MOVE_BOARD | ALL_IN | 22.0 | 7 | 51 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.1696641852031462e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 229 | MOVE_BOARD | ALL_IN | 22.0 | 7 | 51 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014887862838804722 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 230 | PASS | ALL_IN | 22.0 | 7 | 51 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4417354464530945 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 232 | SELL | ALL_IN | 22.0 | 7 | 63 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025066666305065155 | 0.0 | 0.0 | +— / -f6e6e08d-ecfe-4c84-acfa-6ad8292968ee |
| Jogador 1 | 4-5 | 233 | BUY | ALL_IN | 22.0 | 7 | 64 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11736778914928436 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 1 | 4-5 | 234 | SELL | ALL_IN | 22.0 | 7 | 61 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024206940084695816 | 0.0 | 0.0 | +— / -f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 |
| Jogador 1 | 4-5 | 235 | BUY | ALL_IN | 22.0 | 7 | 64 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10334960371255875 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -— |
| Jogador 1 | 4-5 | 236 | SELL | ALL_IN | 22.0 | 7 | 62 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020415838807821274 | 0.0 | 0.0 | +— / -b1efce8c-0cb0-47fc-a361-c50a76c0f9de |
| Jogador 1 | 4-5 | 237 | BUY | ALL_IN | 22.0 | 7 | 64 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060809820890426636 | 0.0 | 0.0 | +477a3c7c-70fe-4f67-ab00-8c9c397365bf / -— |
| Jogador 1 | 4-5 | 238 | SELL | ALL_IN | 22.0 | 7 | 62 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -477a3c7c-70fe-4f67-ab00-8c9c397365bf |
| Jogador 1 | 4-5 | 239 | BUY | ALL_IN | 22.0 | 7 | 64 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20276352763175964 | 0.0 | 0.0 | +7643f027-a90f-4f3a-8b4c-7be4cba17f95 / -— |
| Jogador 1 | 4-5 | 240 | MOVE_BOARD | ALL_IN | 22.0 | 7 | 61 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.841284549504053e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 242 | SELL | ALL_IN | 10.0 | 7 | 74 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -7643f027-a90f-4f3a-8b4c-7be4cba17f95 |
| Jogador 1 | 4-6 | 243 | BUY | ALL_IN | 10.0 | 7 | 77 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.536516010761261 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 1 | 4-6 | 244 | SELL | ALL_IN | 10.0 | 7 | 74 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -fb551efa-6ad5-4f97-aa05-bc5eb70943d4 |
| Jogador 1 | 4-6 | 245 | BUY | ALL_IN | 10.0 | 7 | 78 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8206081390380859 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -29a44465-8a09-49e7-abfc-a27e987543f1,6388773b-0e99-40a9-8d68-895dcf16fce6 |
| Jogador 1 | 4-6 | 246 | BUY | ALL_IN | 10.0 | 7 | 75 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0760725736618042 | 0.0 | 0.0 | +3bfc4626-3226-44b6-a401-ff9c18761448 / -— |
| Jogador 1 | 4-6 | 247 | BUY | ALL_IN | 10.0 | 7 | 72 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26804235577583313 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 1 | 4-6 | 248 | SELL | ALL_IN | 10.0 | 7 | 70 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06363333016633987 | 0.0 | 0.0 | +— / -023f01af-91d0-4e07-8229-2b7cded83151 |
| Jogador 1 | 4-6 | 249 | BUY | ALL_IN | 10.0 | 7 | 78 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2728401720523834 | 0.0 | 0.0 | +20821a31-3317-4f82-bbb2-b70cdebdd893 / -— |
| Jogador 1 | 4-6 | 250 | MOVE_BOARD | ALL_IN | 10.0 | 7 | 77 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29996994137763977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.16027452051639557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43195363879203796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5009031295776367 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1178059577941895 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11989116668701172 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3088749945163727 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40793588757514954 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 40 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0721161365509033 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 41 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20201948285102844 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4003269076347351 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024478765204548836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012103810906410217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 45 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0379815101623535 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18191413581371307 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.27329137921333313 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2662402093410492 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 56 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14821511507034302 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047492608428001404 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19650211930274963 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 2 | 2-1 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028999745845794678 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004016788676381111 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 62 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.047968864440918 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 63 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2347632199525833 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 64 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1532004475593567 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 65 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8824999928474426 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-2 | 66 | BUY_XP | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.000639524485450238 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 68 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999117702245712 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 70 | PASS | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2964060604572296 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 73 | BUY | STABILIZE | 90.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03773220628499985 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 74 | SELL | STABILIZE | 90.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 |
| Jogador 2 | 2-3 | 75 | BUY | STABILIZE | 90.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030421962961554527 | 0.0 | 0.0 | +e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 / -— |
| Jogador 2 | 2-3 | 76 | SELL | STABILIZE | 90.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12439871579408646 | 0.0 | 0.0 | +— / -7ca9b803-76eb-4283-9648-7f98bfd81149 |
| Jogador 2 | 2-3 | 77 | SELL | STABILIZE | 90.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05833333358168602 | 0.0 | 0.0 | +— / -e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 |
| Jogador 2 | 2-3 | 78 | BUY_XP | STABILIZE | 90.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 79 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40143001079559326 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 80 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014995808713138103 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 82 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35677048563957214 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 83 | BUY | STABILIZE | 90.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13672953844070435 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 84 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 85 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998373575508595 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 86 | PASS | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 92 | BUY | STABILIZE | 90.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3384873569011688 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 93 | BUY | STABILIZE | 90.0 | 5 | 2 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07552676647901535 | 0.0 | 0.0 | +eb214f08-2367-4b33-af94-8aa504781450 / -— |
| Jogador 2 | 2-5 | 94 | BUY | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10363173484802246 | 0.0 | 0.0 | +be53a299-cc3e-4af3-94f6-343f9de1e0a0 / -— |
| Jogador 2 | 2-5 | 95 | SELL | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3409999907016754 | 0.0 | 0.0 | +— / -eb214f08-2367-4b33-af94-8aa504781450 |
| Jogador 2 | 2-5 | 96 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3974502384662628 | 0.0 | 0.0 | +— / -— |
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
| Jogador 2 | 3-2 | 132 | BUY | STABILIZE | 67.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28682228922843933 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 133 | BUY | STABILIZE | 67.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24460309743881226 | 0.0 | 0.0 | +f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 / -— |
| Jogador 2 | 3-2 | 134 | BUY | STABILIZE | 67.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025663085281848907 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -— |
| Jogador 2 | 3-2 | 135 | SELL | STABILIZE | 67.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005759625229984522 | 0.0 | 0.0 | +— / -5489a8f6-2466-4171-b91e-64c367875d3c |
| Jogador 2 | 3-2 | 136 | SELL | STABILIZE | 67.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4323333203792572 | 0.0 | 0.0 | +— / -bbdd0918-bfda-49bc-9ae0-8894eaf11a5c |
| Jogador 2 | 3-2 | 137 | BUY_XP | STABILIZE | 67.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 138 | SELL | STABILIZE | 67.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020999999716877937 | 0.0 | 0.0 | +— / -f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 |
| Jogador 2 | 3-2 | 139 | BUY | STABILIZE | 67.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21058619022369385 | 0.0 | 0.0 | +e86a4466-cd1f-48a3-a825-cab2e361b72a / -— |
| Jogador 2 | 3-2 | 140 | SELL | STABILIZE | 67.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3596666753292084 | 0.0 | 0.0 | +— / -e86a4466-cd1f-48a3-a825-cab2e361b72a |
| Jogador 2 | 3-3 | 142 | BUY | STABILIZE | 67.0 | 6 | 9 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7998140454292297 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 143 | BUY | STABILIZE | 67.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004060382954776287 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 144 | SELL | STABILIZE | 67.0 | 6 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 3-3 | 145 | SELL | STABILIZE | 67.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -584e7960-a541-4d45-8ea1-8a75e288c387 |
| Jogador 2 | 3-3 | 146 | BUY | STABILIZE | 67.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057809364050626755 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 147 | SELL | STABILIZE | 67.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3503333330154419 | 0.0 | 0.0 | +— / -3880fbd9-322b-4375-b855-fbb779a0cb47 |
| Jogador 2 | 3-3 | 148 | BUY_XP | STABILIZE | 67.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 149 | SELL | STABILIZE | 67.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49430766701698303 | 0.0 | 0.0 | +— / -e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 3-3 | 150 | BUY_XP | STABILIZE | 67.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 152 | BUY | STABILIZE | 67.0 | 6 | 9 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01184503547847271 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -— |
| Jogador 2 | 3-4 | 153 | BUY | STABILIZE | 67.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44664132595062256 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 2 | 3-4 | 154 | BUY | STABILIZE | 67.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25828054547309875 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 155 | SELL | STABILIZE | 67.0 | 6 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 3-4 | 156 | SELL | STABILIZE | 67.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7856666445732117 | 0.0 | 0.0 | +— / -c4c0b136-020d-4c1e-9517-8e0bf4c5a628 |
| Jogador 2 | 3-4 | 157 | SELL | STABILIZE | 67.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0689999982714653 | 0.0 | 0.0 | +— / -c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 2 | 3-4 | 158 | BUY_XP | STABILIZE | 67.0 | 6 | 9 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 159 | SELL | STABILIZE | 67.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5679555535316467 | 0.0 | 0.0 | +— / -2ace989d-3e9e-483b-9b14-cd6b8f171f17 |
| Jogador 2 | 3-4 | 160 | BUY_XP | STABILIZE | 67.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 162 | BUY | STABILIZE | 67.0 | 7 | 10 | 1 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004380738362669945 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 163 | BUY | STABILIZE | 67.0 | 7 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0664554014801979 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 164 | BUY | STABILIZE | 67.0 | 7 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28559184074401855 | 0.0 | 0.0 | +b5cec20a-0619-4060-9f1b-e72942ac34dd / -— |
| Jogador 2 | 3-5 | 165 | SELL | STABILIZE | 67.0 | 7 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020999999716877937 | 0.0 | 0.0 | +— / -b5cec20a-0619-4060-9f1b-e72942ac34dd |
| Jogador 2 | 3-5 | 166 | BUY_XP | STABILIZE | 67.0 | 7 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 167 | SELL | STABILIZE | 67.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09478805214166641 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 3-5 | 168 | SELL | STABILIZE | 67.0 | 7 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09775499999523163 | 0.0 | 0.0 | +— / -cce8de69-f877-4e86-b720-6aea91e68f47 |
| Jogador 2 | 3-5 | 169 | BUY_XP | STABILIZE | 67.0 | 7 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 170 | SELL | STABILIZE | 67.0 | 7 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0210000276565552 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 3-6 | 172 | BUY | STABILIZE | 57.0 | 7 | 9 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8032166957855225 | 0.0 | 0.0 | +63304cf5-4aa7-473e-9bfb-ec04cd68ebbd / -— |
| Jogador 2 | 3-6 | 173 | BUY | STABILIZE | 57.0 | 7 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879561483860016 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-6 | 174 | BUY | STABILIZE | 57.0 | 7 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0092457951977849 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 175 | SELL | STABILIZE | 57.0 | 7 | 2 | 0 | 22.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0716666653752327 | 0.0 | 0.0 | +— / -23157bd6-5e8f-4416-bb7f-2e5d71a06543 |
| Jogador 2 | 3-6 | 176 | BUY | STABILIZE | 57.0 | 7 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23991107940673828 | 0.0 | 0.0 | +33a860e2-992f-4355-ab24-85b4a2576f90 / -— |
| Jogador 2 | 3-6 | 177 | SELL | STABILIZE | 57.0 | 7 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 3-6 | 178 | BUY | STABILIZE | 57.0 | 7 | 4 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06709463894367218 | 0.0 | 0.0 | +8fb80cc8-4120-41a0-bc96-35f81a466ed9 / -— |
| Jogador 2 | 3-6 | 179 | SELL | STABILIZE | 57.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050333332270383835 | 0.0 | 0.0 | +— / -8fb80cc8-4120-41a0-bc96-35f81a466ed9 |
| Jogador 2 | 3-6 | 180 | BUY_XP | STABILIZE | 57.0 | 7 | 4 | 0 | 22.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 182 | BUY | STABILIZE | 45.0 | 7 | 6 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8322303891181946 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -0c15e414-bc67-46de-a087-fb7708db0dfe,e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-7 | 183 | BUY | STABILIZE | 45.0 | 7 | 3 | 0 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28795599937438965 | 0.0 | 0.0 | +813260b6-a1b8-4a5c-978e-acd60b6b1082 / -— |
| Jogador 2 | 3-7 | 184 | SELL | STABILIZE | 45.0 | 7 | 2 | 0 | 22.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5389999747276306 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 3-7 | 185 | BUY | STABILIZE | 45.0 | 7 | 10 | 1 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6332849264144897 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 2 | 3-7 | 186 | BUY | STABILIZE | 45.0 | 7 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03923201560974121 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 187 | SELL | STABILIZE | 45.0 | 7 | 3 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06396391987800598 | 0.0 | 0.0 | +— / -e0445166-70a5-4135-a45e-ff238a95b228 |
| Jogador 2 | 3-7 | 188 | SELL | STABILIZE | 45.0 | 7 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -813260b6-a1b8-4a5c-978e-acd60b6b1082 |
| Jogador 2 | 3-7 | 189 | BUY | STABILIZE | 45.0 | 7 | 8 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06661622226238251 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 2 | 3-7 | 190 | BUY_XP | STABILIZE | 45.0 | 7 | 5 | 0 | 22.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 192 | BUY | STABILIZE | 45.0 | 7 | 7 | 0 | 22.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7921198010444641 | 0.0 | 0.0 | +a4188ec8-4188-4fdf-8d76-c559fc0c7daf / -33a860e2-992f-4355-ab24-85b4a2576f90,ed0dab77-fd87-4677-8428-7505ccd34b86 |
| Jogador 2 | 4-1 | 193 | BUY | STABILIZE | 45.0 | 7 | 4 | 0 | 22.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07350403815507889 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 2 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 45.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17551226913928986 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 195 | CRAFT_AND_EQUIP | STABILIZE | 45.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22029143571853638 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 196 | MOVE_BENCH | STABILIZE | 45.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40004467964172363 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 197 | MOVE_BOARD | STABILIZE | 45.0 | 7 | 1 | 0 | 28.0 | Colosso/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014996318146586418 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 198 | SELL | STABILIZE | 45.0 | 7 | 1 | 0 | 28.0 | Colosso/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5579555630683899 | 0.0 | 0.0 | +— / -a4188ec8-4188-4fdf-8d76-c559fc0c7daf |
| Jogador 2 | 4-1 | 199 | BUY | STABILIZE | 45.0 | 7 | 9 | 0 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27286288142204285 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 2 | 4-1 | 200 | BUY | STABILIZE | 45.0 | 7 | 5 | 0 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27772587537765503 | 0.0 | 0.0 | +1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 / -— |
| Jogador 2 | 4-2 | 202 | BUY | STABILIZE | 34.0 | 7 | 9 | 0 | 28.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8684539198875427 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-2 | 203 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 8 | 0 | 24.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15043893456459045 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 204 | BUY | STABILIZE | 34.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3152659833431244 | 0.0 | 0.0 | +9cb61b5c-2c8a-43a2-a854-517f4377f6db / -— |
| Jogador 2 | 4-2 | 205 | BUY | STABILIZE | 34.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24803310632705688 | 0.0 | 0.0 | +3fdd5708-2e07-4636-a598-d872f57e1c16 / -— |
| Jogador 2 | 4-2 | 206 | BUY | STABILIZE | 34.0 | 7 | 3 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1910504400730133 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -— |
| Jogador 2 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0013158273650333285 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013683016411960125 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 209 | PASS | STABILIZE | 34.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 210 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.58864825963974 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 212 | BUY | STABILIZE | 34.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7805762887001038 | 0.0 | 0.0 | +caf1c554-2223-4090-9f96-b551e5c579ce / -— |
| Jogador 2 | 4-3 | 213 | BUY | STABILIZE | 34.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.281523197889328 | 0.0 | 0.0 | +104aaac3-252c-4c1b-9ad8-fc10a35c6cda / -— |
| Jogador 2 | 4-3 | 214 | SELL | STABILIZE | 34.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -b7e13ed2-571b-4245-ba21-401b1eef8660 |
| Jogador 2 | 4-3 | 215 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.098680779337883 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 216 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1305512934923172 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 217 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.17050641775131226 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 218 | BUY | STABILIZE | 34.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6095683574676514 | 0.0 | 0.0 | +6538f28f-845f-4f45-92bf-120931553bec / -1d7ccf69-9aaa-4f0c-81ed-a94ef995d915,9cb61b5c-2c8a-43a2-a854-517f4377f6db |
| Jogador 2 | 4-3 | 219 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00011924472346436232 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 220 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014881313778460026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 222 | BUY | STABILIZE | 34.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42786887288093567 | 0.0 | 0.0 | +b80a9778-b2ce-411b-8d08-24549c04367c / -— |
| Jogador 2 | 4-4 | 223 | BUY | STABILIZE | 34.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3842567801475525 | 0.0 | 0.0 | +b26a039f-581c-4de2-8a75-f7e8a4ef0e4a / -— |
| Jogador 2 | 4-4 | 224 | SELL | STABILIZE | 34.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03991534560918808 | 0.0 | 0.0 | +— / -6538f28f-845f-4f45-92bf-120931553bec |
| Jogador 2 | 4-4 | 225 | BUY | STABILIZE | 34.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24312147498130798 | 0.0 | 0.0 | +ed23d828-f4bc-4d6c-8cc1-c074047dac8a / -— |
| Jogador 2 | 4-4 | 226 | BUY_XP | STABILIZE | 34.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 227 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.1261816982587334e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015015986748039722 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 229 | PASS | STABILIZE | 34.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 232 | SELL | STABILIZE | 34.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10400000214576721 | 0.0 | 0.0 | +— / -23793b7b-2dab-48f0-a8ba-db85fc14c1c5 |
| Jogador 2 | 4-5 | 233 | BUY | STABILIZE | 34.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7194305062294006 | 0.0 | 0.0 | +61362365-2cf7-40e4-95f9-98e28728fd39 / -— |
| Jogador 2 | 4-5 | 234 | SELL | STABILIZE | 34.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3788803815841675 | 0.0 | 0.0 | +— / -b26a039f-581c-4de2-8a75-f7e8a4ef0e4a |
| Jogador 2 | 4-5 | 235 | BUY | STABILIZE | 34.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19123618304729462 | 0.0 | 0.0 | +1ff42607-ccac-4d3f-8277-bccddf08862f / -— |
| Jogador 2 | 4-5 | 236 | BUY_XP | STABILIZE | 34.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 237 | BUY_XP | STABILIZE | 34.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 34.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499604806303978 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 240 | PASS | STABILIZE | 34.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 242 | SELL | STABILIZE | 34.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07653333246707916 | 0.0 | 0.0 | +— / -1ff42607-ccac-4d3f-8277-bccddf08862f |
| Jogador 2 | 4-6 | 243 | BUY | STABILIZE | 34.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2871851325035095 | 0.0 | 0.0 | +565ff610-fe51-470b-8452-a7eec5e31653 / -— |
| Jogador 2 | 4-6 | 244 | SELL | STABILIZE | 34.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0944666638970375 | 0.0 | 0.0 | +— / -ed23d828-f4bc-4d6c-8cc1-c074047dac8a |
| Jogador 2 | 4-6 | 245 | BUY | STABILIZE | 34.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20718827843666077 | 0.0 | 0.0 | +5c43307a-6d61-4493-a1ed-cb428d79a254 / -— |
| Jogador 2 | 4-6 | 246 | SELL | STABILIZE | 34.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5080000162124634 | 0.0 | 0.0 | +— / -565ff610-fe51-470b-8452-a7eec5e31653 |
| Jogador 2 | 4-6 | 247 | BUY | STABILIZE | 34.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2682144045829773 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 2 | 4-6 | 248 | BUY_XP | STABILIZE | 34.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 249 | BUY_XP | STABILIZE | 34.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 250 | SELL | STABILIZE | 34.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0051183272153139114 | 0.0 | 0.0 | +— / -db6b2dca-4de1-420e-aadb-943e19b6121a |
| Jogador 2 | 4-7 | 252 | BUY | STABILIZE | 34.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16625002026557922 | 0.0 | 0.0 | +ecf369a7-649e-45fe-ad90-8f29e1714fe6 / -— |
| Jogador 2 | 4-7 | 253 | SELL | STABILIZE | 34.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028699999675154686 | 0.0 | 0.0 | +— / -ecf369a7-649e-45fe-ad90-8f29e1714fe6 |
| Jogador 2 | 4-7 | 254 | BUY | STABILIZE | 34.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07274723052978516 | 0.0 | 0.0 | +5754c4b4-0a7d-49e5-93e4-b144c3090a41 / -— |
| Jogador 2 | 4-7 | 255 | SELL | STABILIZE | 34.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -5754c4b4-0a7d-49e5-93e4-b144c3090a41 |
| Jogador 2 | 4-7 | 256 | BUY | STABILIZE | 34.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24623224139213562 | 0.0 | 0.0 | +91966802-adc2-46d2-9e7e-194283bca85c / -— |
| Jogador 2 | 4-7 | 257 | BUY_XP | STABILIZE | 34.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07245906442403793 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 258 | MOVE_BENCH | STABILIZE | 34.0 | 8 | 3 | 0 | 36.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49572625756263733 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 259 | BUY | STABILIZE | 34.0 | 8 | 3 | 0 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09368912875652313 | 0.0 | 0.0 | +5416d773-cb2c-442a-8ee9-0d46d22c2087 / -— |
| Jogador 2 | 4-7 | 260 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 2 | 0 | 42.0 | Colosso/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 34.0 | 8 | 8 | 0 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08322665095329285 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 34.0 | 8 | 8 | 0 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.04378092661499977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 264 | SELL | STABILIZE | 34.0 | 8 | 8 | 0 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10400000214576721 | 0.0 | 0.0 | +— / -91966802-adc2-46d2-9e7e-194283bca85c |
| Jogador 2 | 5-1 | 265 | BUY | STABILIZE | 34.0 | 8 | 10 | 1 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7500465512275696 | 0.0 | 0.0 | +3658b5d8-450f-451a-8487-5b3bdd7c385b / -3fdd5708-2e07-4636-a598-d872f57e1c16,caf1c554-2223-4090-9f96-b551e5c579ce |
| Jogador 2 | 5-1 | 266 | BUY | STABILIZE | 34.0 | 8 | 7 | 0 | 42.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3122917413711548 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -— |
| Jogador 2 | 5-1 | 267 | BUY | STABILIZE | 34.0 | 8 | 4 | 0 | 42.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08427825570106506 | 0.0 | 0.0 | +c8706680-2712-4914-b6c0-59bf92a2796d / -— |
| Jogador 2 | 5-1 | 268 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002817881526425481 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 269 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012174895964562893 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 270 | PASS | STABILIZE | 34.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_CrimsonRaptor18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 272 | SELL | STABILIZE | 34.0 | 8 | 9 | 0 | 42.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47762221097946167 | 0.0 | 0.0 | +— / -3658b5d8-450f-451a-8487-5b3bdd7c385b |
| Jogador 2 | 5-2 | 273 | BUY | STABILIZE | 34.0 | 8 | 17 | 1 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27615460753440857 | 0.0 | 0.0 | +438ec27b-d901-437b-82b5-64e6d46fccb1 / -— |
| Jogador 2 | 5-2 | 274 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 13 | 1 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.767914106196258e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 275 | SELL | STABILIZE | 34.0 | 8 | 13 | 1 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08950906246900558 | 0.0 | 0.0 | +— / -438ec27b-d901-437b-82b5-64e6d46fccb1 |
| Jogador 2 | 5-2 | 276 | BUY | STABILIZE | 34.0 | 8 | 17 | 1 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012002246454358101 | 0.0 | 0.0 | +a5e92183-8d5d-434c-9294-47c6b7bfb91b / -— |
| Jogador 2 | 5-2 | 277 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 14 | 1 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.339891681112931e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 278 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 14 | 1 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015017542988061905 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 279 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 14 | 1 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014982661232352257 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 280 | PASS | STABILIZE | 34.0 | 8 | 14 | 1 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 282 | SELL | STABILIZE | 34.0 | 8 | 24 | 2 | 42.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -a5e92183-8d5d-434c-9294-47c6b7bfb91b |
| Jogador 2 | 5-3 | 283 | BUY | STABILIZE | 34.0 | 8 | 27 | 2 | 42.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8805070519447327 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -63304cf5-4aa7-473e-9bfb-ec04cd68ebbd,6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 5-3 | 284 | BUY | STABILIZE | 34.0 | 8 | 25 | 2 | 38.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09907373785972595 | 0.0 | 0.0 | +aea521ef-8511-4b98-9c6d-e83b814777df / -— |
| Jogador 2 | 5-3 | 285 | SELL | STABILIZE | 34.0 | 8 | 22 | 2 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -f6000a82-1241-4220-9362-c8d788472db0 |
| Jogador 2 | 5-3 | 286 | BUY | STABILIZE | 34.0 | 8 | 27 | 2 | 38.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08393111824989319 | 0.0 | 0.0 | +3329c812-11fa-4335-a982-f03e6ab28ee0 / -— |
| Jogador 2 | 5-3 | 287 | BUY_XP | STABILIZE | 34.0 | 8 | 23 | 2 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 288 | BUY_XP | STABILIZE | 34.0 | 8 | 19 | 1 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 289 | BUY_XP | STABILIZE | 34.0 | 8 | 15 | 1 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020000000949949026 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 290 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 11 | 1 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.298463641636772e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 292 | SELL | STABILIZE | 34.0 | 8 | 21 | 2 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.999999747378752e-05 | 0.0 | 0.0 | +— / -5416d773-cb2c-442a-8ee9-0d46d22c2087 |
| Jogador 2 | 5-4 | 293 | BUY | STABILIZE | 34.0 | 8 | 22 | 2 | 38.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.730701744556427 | 0.0 | 0.0 | +150a2da3-f559-4a40-a058-005e9c74e11f / -— |
| Jogador 2 | 5-4 | 294 | SELL | STABILIZE | 34.0 | 8 | 19 | 1 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3152763247489929 | 0.0 | 0.0 | +— / -217a3ebb-1953-4f1e-bfdd-a3c9438e791e |
| Jogador 2 | 5-4 | 295 | BUY | STABILIZE | 34.0 | 8 | 22 | 2 | 38.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3141654431819916 | 0.0 | 0.0 | +efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 / -— |
| Jogador 2 | 5-4 | 296 | SELL | STABILIZE | 34.0 | 8 | 21 | 2 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5879999995231628 | 0.0 | 0.0 | +— / -efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 |
| Jogador 2 | 5-4 | 297 | BUY | STABILIZE | 34.0 | 8 | 22 | 2 | 38.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3137812316417694 | 0.0 | 0.0 | +c07a17cf-e9e7-42be-b925-cb4f699593de / -— |
| Jogador 2 | 5-4 | 298 | MOVE_BENCH | STABILIZE | 34.0 | 8 | 21 | 2 | 38.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5709099769592285 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 299 | BUY | STABILIZE | 34.0 | 8 | 21 | 2 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.167785182595253 | 0.0 | 0.0 | +f087511a-d834-4f41-9b99-00bf0f6dc061 / -— |
| Jogador 2 | 5-4 | 300 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 16 | 1 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 302 | SELL | STABILIZE | 34.0 | 8 | 25 | 2 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014502585865557194 | 0.0 | 0.0 | +— / -f087511a-d834-4f41-9b99-00bf0f6dc061 |
| Jogador 2 | 5-5 | 303 | BUY | STABILIZE | 34.0 | 8 | 30 | 3 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7035755515098572 | 0.0 | 0.0 | +3c5f5211-f30d-44e7-ac68-0ce513a3d614 / -— |
| Jogador 2 | 5-5 | 304 | SELL | STABILIZE | 34.0 | 8 | 27 | 2 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3178541958332062 | 0.0 | 0.0 | +— / -1be0cdcc-ee10-44dc-ad1b-de9b53b25164 |
| Jogador 2 | 5-5 | 305 | BUY | STABILIZE | 34.0 | 8 | 30 | 3 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8367847800254822 | 0.0 | 0.0 | +01c587bb-ca4f-4690-9e4b-d1e9c44fd33e / -3c5f5211-f30d-44e7-ac68-0ce513a3d614,aea521ef-8511-4b98-9c6d-e83b814777df |
| Jogador 2 | 5-5 | 306 | BUY | STABILIZE | 34.0 | 8 | 27 | 2 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12409763038158417 | 0.0 | 0.0 | +551e9535-d584-4055-a544-ed78d65ecacb / -— |
| Jogador 2 | 5-5 | 307 | BUY | STABILIZE | 34.0 | 8 | 23 | 2 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011827613227069378 | 0.0 | 0.0 | +08731924-b808-4070-8c85-2c747847d835 / -— |
| Jogador 2 | 5-5 | 308 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 20 | 2 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0001580229145474732 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 309 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 20 | 2 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014873424544930458 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 310 | PASS | STABILIZE | 34.0 | 8 | 20 | 2 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03859894350171089 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 312 | SELL | STABILIZE | 34.0 | 8 | 31 | 3 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5576221942901611 | 0.0 | 0.0 | +— / -01c587bb-ca4f-4690-9e4b-d1e9c44fd33e |
| Jogador 2 | 5-6 | 313 | BUY | STABILIZE | 34.0 | 8 | 39 | 3 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27832645177841187 | 0.0 | 0.0 | +85fb6db6-e1b0-4fa1-b99a-2f205305ef0b / -— |
| Jogador 2 | 5-6 | 314 | SELL | STABILIZE | 34.0 | 8 | 36 | 3 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -08731924-b808-4070-8c85-2c747847d835 |
| Jogador 2 | 5-6 | 315 | BUY | STABILIZE | 34.0 | 8 | 39 | 3 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20187856256961823 | 0.0 | 0.0 | +9f1c634e-13c7-4b59-838c-4b676fa059be / -— |
| Jogador 2 | 5-6 | 316 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 35 | 3 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.17703676148085e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 317 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 35 | 3 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01497579738497734 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 318 | PASS | STABILIZE | 34.0 | 8 | 35 | 3 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.061140213161706924 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 322 | SELL | STABILIZE | 34.0 | 8 | 46 | 4 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05079999938607216 | 0.0 | 0.0 | +— / -9f1c634e-13c7-4b59-838c-4b676fa059be |
| Jogador 2 | 5-7 | 323 | BUY | STABILIZE | 34.0 | 8 | 50 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17799699306488037 | 0.0 | 0.0 | +9c3b3b78-e99c-4947-b958-cce156ecccb1 / -— |
| Jogador 2 | 5-7 | 324 | SELL | STABILIZE | 34.0 | 8 | 47 | 4 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0215000007301569 | 0.0 | 0.0 | +— / -9c3b3b78-e99c-4947-b958-cce156ecccb1 |
| Jogador 2 | 5-7 | 325 | BUY | STABILIZE | 34.0 | 8 | 50 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12655706703662872 | 0.0 | 0.0 | +a37d8478-8a98-4099-bb18-3602d68764f5 / -— |
| Jogador 2 | 5-7 | 326 | SELL | STABILIZE | 34.0 | 8 | 45 | 4 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03375356271862984 | 0.0 | 0.0 | +— / -a37d8478-8a98-4099-bb18-3602d68764f5 |
| Jogador 2 | 5-7 | 327 | BUY | STABILIZE | 34.0 | 8 | 50 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10153734683990479 | 0.0 | 0.0 | +68a0405b-6231-471f-98a5-1661d32f4ac4 / -— |
| Jogador 2 | 5-7 | 328 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 47 | 4 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 329 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 47 | 4 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 330 | PASS | STABILIZE | 34.0 | 8 | 47 | 4 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07415396720170975 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 332 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 8 | 59 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07452309876680374 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 333 | SELL | STABILIZE | 34.0 | 8 | 59 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035130757838487625 | 0.0 | 0.0 | +— / -68a0405b-6231-471f-98a5-1661d32f4ac4 |
| Jogador 2 | 6-1 | 334 | BUY | STABILIZE | 34.0 | 8 | 62 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0648605227470398 | 0.0 | 0.0 | +8538e488-6f36-433a-b261-73626f24bb07 / -— |
| Jogador 2 | 6-1 | 335 | SELL | STABILIZE | 34.0 | 8 | 58 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -8538e488-6f36-433a-b261-73626f24bb07 |
| Jogador 2 | 6-1 | 336 | BUY | STABILIZE | 34.0 | 8 | 62 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11795602738857269 | 0.0 | 0.0 | +e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 / -— |
| Jogador 2 | 6-1 | 337 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 59 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00040291069308295846 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 338 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 59 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015174422413110733 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 339 | PASS | STABILIZE | 34.0 | 8 | 59 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12813729047775269 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 342 | SELL | STABILIZE | 34.0 | 8 | 73 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03200000151991844 | 0.0 | 0.0 | +— / -e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 |
| Jogador 2 | 6-2 | 343 | BUY | STABILIZE | 34.0 | 8 | 76 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1988109052181244 | 0.0 | 0.0 | +6b7f5603-ce44-4b91-8a3e-939c4fbb26ac / -— |
| Jogador 2 | 6-2 | 344 | SELL | STABILIZE | 34.0 | 8 | 74 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -6b7f5603-ce44-4b91-8a3e-939c4fbb26ac |
| Jogador 2 | 6-2 | 345 | BUY | STABILIZE | 34.0 | 8 | 76 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0648675411939621 | 0.0 | 0.0 | +e7c18780-1d70-4a15-ad72-2eaa0f81df8d / -— |
| Jogador 2 | 6-2 | 346 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 72 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 347 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 72 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015361427329480648 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 348 | PASS | STABILIZE | 34.0 | 8 | 72 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14211662113666534 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 352 | SELL | STABILIZE | 34.0 | 8 | 86 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -e7c18780-1d70-4a15-ad72-2eaa0f81df8d |
| Jogador 2 | 6-3 | 353 | BUY | STABILIZE | 34.0 | 8 | 90 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9052297472953796 | 0.0 | 0.0 | +00497e43-57ef-4c25-a34b-0be0155bb92d / -— |
| Jogador 2 | 6-3 | 354 | SELL | STABILIZE | 34.0 | 8 | 86 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40446311235427856 | 0.0 | 0.0 | +— / -85fb6db6-e1b0-4fa1-b99a-2f205305ef0b |
| Jogador 2 | 6-3 | 355 | BUY | STABILIZE | 34.0 | 8 | 89 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38329052925109863 | 0.0 | 0.0 | +4b4293ce-1cca-473e-8c07-b441686985ac / -— |
| Jogador 2 | 6-3 | 356 | SELL | STABILIZE | 34.0 | 8 | 87 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10084377974271774 | 0.0 | 0.0 | +— / -4b4293ce-1cca-473e-8c07-b441686985ac |
| Jogador 2 | 6-3 | 357 | BUY | STABILIZE | 34.0 | 8 | 89 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2688571512699127 | 0.0 | 0.0 | +c4ec99e0-d973-42e9-a20e-1a9e7f5bf89a / -— |
| Jogador 2 | 6-3 | 358 | SELL | STABILIZE | 34.0 | 8 | 86 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07013333588838577 | 0.0 | 0.0 | +— / -c4ec99e0-d973-42e9-a20e-1a9e7f5bf89a |
| Jogador 2 | 6-3 | 359 | BUY | STABILIZE | 34.0 | 8 | 89 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18326017260551453 | 0.0 | 0.0 | +8025eaf5-b02b-4f94-b381-b94321bca206 / -— |
| Jogador 2 | 6-3 | 360 | SELL | STABILIZE | 34.0 | 8 | 85 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004174926318228245 | 0.0 | 0.0 | +— / -8025eaf5-b02b-4f94-b381-b94321bca206 |
| Jogador 2 | 6-4 | 362 | BUY | STABILIZE | 34.0 | 8 | 103 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9091736674308777 | 0.0 | 0.0 | +07080859-42b2-498e-9c11-257fea02f14b / -— |
| Jogador 2 | 6-4 | 363 | SELL | STABILIZE | 34.0 | 8 | 99 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -c07a17cf-e9e7-42be-b925-cb4f699593de |
| Jogador 2 | 6-4 | 364 | BUY | STABILIZE | 34.0 | 8 | 100 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26845845580101013 | 0.0 | 0.0 | +ffd44f6f-388e-4792-ae4f-77f2faa3e95f / -— |
| Jogador 2 | 6-4 | 365 | SELL | STABILIZE | 34.0 | 8 | 97 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06840000301599503 | 0.0 | 0.0 | +— / -ffd44f6f-388e-4792-ae4f-77f2faa3e95f |
| Jogador 2 | 6-4 | 366 | BUY | STABILIZE | 34.0 | 8 | 100 | 5 | 44.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21695642173290253 | 0.0 | 0.0 | +54b8f150-85a6-4fad-9a4f-3b04897733cf / -— |
| Jogador 2 | 6-4 | 367 | MOVE_BENCH | STABILIZE | 34.0 | 8 | 96 | 5 | 44.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.387981653213501 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 368 | MOVE_BENCH | STABILIZE | 34.0 | 8 | 96 | 5 | 46.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3890419602394104 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 369 | PASS | STABILIZE | 34.0 | 8 | 96 | 5 | 48.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16954949498176575 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 372 | SELL | STABILIZE | 34.0 | 8 | 109 | 5 | 48.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -11a1c814-5357-4f19-944f-aa11d6bf8384 |
| Jogador 2 | 6-5 | 373 | BUY | STABILIZE | 34.0 | 8 | 112 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.5883455872535706 | 0.0 | 0.0 | +2328111b-018a-4ca1-a9e7-f7cd9627fd43 / -— |
| Jogador 2 | 6-5 | 374 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 8 | 109 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.102141834795475 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 375 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 8 | 109 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11826559156179428 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 376 | SELL | STABILIZE | 34.0 | 8 | 109 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042399998754262924 | 0.0 | 0.0 | +— / -54b8f150-85a6-4fad-9a4f-3b04897733cf |
| Jogador 2 | 6-5 | 377 | BUY | STABILIZE | 34.0 | 8 | 113 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28999027609825134 | 0.0 | 0.0 | +80241b75-9eb3-4b89-a754-8df65ec59786 / -— |
| Jogador 2 | 6-5 | 378 | SELL | STABILIZE | 34.0 | 8 | 110 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4043188691139221 | 0.0 | 0.0 | +— / -80241b75-9eb3-4b89-a754-8df65ec59786 |
| Jogador 2 | 6-5 | 379 | BUY | STABILIZE | 34.0 | 8 | 113 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2502667009830475 | 0.0 | 0.0 | +6875f839-cf68-443f-9776-887087b375d3 / -— |
| Jogador 2 | 6-5 | 380 | SELL | STABILIZE | 34.0 | 8 | 110 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -6875f839-cf68-443f-9776-887087b375d3 |
| Jogador 2 | 6-6 | 382 | BUY | STABILIZE | 34.0 | 8 | 127 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1338726282119751 | 0.0 | 0.0 | +52799e57-7b54-4dc5-b7f8-c39c8f57e7fa / -— |
| Jogador 2 | 6-6 | 383 | SELL | STABILIZE | 34.0 | 8 | 123 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -52799e57-7b54-4dc5-b7f8-c39c8f57e7fa |
| Jogador 2 | 6-6 | 384 | BUY | STABILIZE | 34.0 | 8 | 127 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13387328386306763 | 0.0 | 0.0 | +49eaab97-475e-4663-a2b7-61d755bf19ca / -— |
| Jogador 2 | 6-6 | 385 | SELL | STABILIZE | 34.0 | 8 | 123 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -49eaab97-475e-4663-a2b7-61d755bf19ca |
| Jogador 2 | 6-6 | 386 | BUY | STABILIZE | 34.0 | 8 | 127 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10031957179307938 | 0.0 | 0.0 | +b5e5c8e4-7fb5-4b4b-b284-f0794e78eadc / -— |
| Jogador 2 | 6-6 | 387 | SELL | STABILIZE | 34.0 | 8 | 126 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025066666305065155 | 0.0 | 0.0 | +— / -b5e5c8e4-7fb5-4b4b-b284-f0794e78eadc |
| Jogador 2 | 6-6 | 388 | BUY | STABILIZE | 34.0 | 8 | 127 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10031963884830475 | 0.0 | 0.0 | +6f0b2edb-0f61-4838-b698-703f080582a1 / -— |
| Jogador 2 | 6-6 | 389 | SELL | STABILIZE | 34.0 | 8 | 126 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010333333164453506 | 0.0 | 0.0 | +— / -6f0b2edb-0f61-4838-b698-703f080582a1 |
| Jogador 2 | 6-6 | 390 | BUY | STABILIZE | 34.0 | 8 | 127 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20904532074928284 | 0.0 | 0.0 | +ee093d10-ed4b-4e0e-8e0a-37247f9aa517 / -— |
| Jogador 2 | 6-7 | 392 | SELL | STABILIZE | 34.0 | 8 | 138 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -ee093d10-ed4b-4e0e-8e0a-37247f9aa517 |
| Jogador 2 | 6-7 | 393 | BUY | STABILIZE | 34.0 | 8 | 141 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3871990144252777 | 0.0 | 0.0 | +a960f5cb-d806-4d73-9146-244e1ecde6f2 / -— |
| Jogador 2 | 6-7 | 394 | SELL | STABILIZE | 34.0 | 8 | 137 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45190000534057617 | 0.0 | 0.0 | +— / -2328111b-018a-4ca1-a9e7-f7cd9627fd43 |
| Jogador 2 | 6-7 | 395 | BUY | STABILIZE | 34.0 | 8 | 140 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13899438083171844 | 0.0 | 0.0 | +edd9f925-ac58-4285-a53c-ca70b782c682 / -— |
| Jogador 2 | 6-7 | 396 | SELL | STABILIZE | 34.0 | 8 | 136 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -edd9f925-ac58-4285-a53c-ca70b782c682 |
| Jogador 2 | 6-7 | 397 | BUY | STABILIZE | 34.0 | 8 | 140 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11530190706253052 | 0.0 | 0.0 | +389bcf7d-1a3c-4360-8bcf-a98cacecbaea / -— |
| Jogador 2 | 6-7 | 398 | SELL | STABILIZE | 34.0 | 8 | 138 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -389bcf7d-1a3c-4360-8bcf-a98cacecbaea |
| Jogador 2 | 6-7 | 399 | BUY | STABILIZE | 34.0 | 8 | 140 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029286431148648262 | 0.0 | 0.0 | +e8658026-70da-4dca-9f24-5a4aab392ddb / -— |
| Jogador 2 | 6-7 | 400 | SELL | STABILIZE | 34.0 | 8 | 139 | 5 | 48.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019866665825247765 | 0.0 | 0.0 | +— / -e8658026-70da-4dca-9f24-5a4aab392ddb |
| Jogador 2 | 7-1 | 402 | BUY | STABILIZE | 34.0 | 8 | 153 | 5 | 48.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.0838208198547363 | 0.0 | 0.0 | +d2e500c1-c1ae-40ce-b3d2-c7b688640a73 / -150a2da3-f559-4a40-a058-005e9c74e11f,c8706680-2712-4914-b6c0-59bf92a2796d |
| Jogador 2 | 7-1 | 403 | BUY | STABILIZE | 34.0 | 8 | 150 | 5 | 42.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.2997175455093384 | 0.0 | 0.0 | +f7f1b5db-dae6-4b1c-9a1f-94fefd1cf248 / -— |
| Jogador 2 | 7-1 | 404 | EQUIP_FROM_INVENTORY | STABILIZE | 34.0 | 8 | 147 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11376842111349106 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 405 | SELL | STABILIZE | 34.0 | 8 | 147 | 5 | 42.0 | Colosso/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.59015953540802 | 0.0 | 0.0 | +— / -d2e500c1-c1ae-40ce-b3d2-c7b688640a73 |
| Jogador 2 | 7-1 | 406 | BUY | STABILIZE | 34.0 | 8 | 155 | 5 | 42.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10600284487009048 | 0.0 | 0.0 | +280265b0-7892-4e7e-b654-e2cc7b0ea97b / -— |
| Jogador 2 | 7-1 | 407 | MOVE_BENCH | STABILIZE | 34.0 | 8 | 151 | 5 | 42.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4118663966655731 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 408 | BUY | STABILIZE | 34.0 | 8 | 151 | 5 | 50.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7691699266433716 | 0.0 | 0.0 | +e99948bb-f38f-41e0-b1c4-1864c35ffe14 / -— |
| Jogador 2 | 7-1 | 409 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 147 | 5 | 50.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0925304394504565e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 410 | MOVE_BOARD | STABILIZE | 34.0 | 8 | 147 | 5 | 50.0 | Colosso/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015031617134809494 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22444601356983185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0904720276594162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40667274594306946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0396608114242554 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.117977499961853 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009961719624698162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5896894335746765 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22690147161483765 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 40 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21204201877117157 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 42 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 43 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26404017210006714 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25187569856643677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23012398183345795 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3955889344215393 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21845154464244843 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007322629448026419 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 58 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9605410695075989 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 63 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3372155427932739 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 64 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3325497806072235 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2675749957561493 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 75 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.890117347240448 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4073878526687622 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 84 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15198536217212677 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 85 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08549651503562927 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 86 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 87 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07977400720119476 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 88 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01492172572761774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 89 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8983877301216125 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 93 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 94 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012155719101428986 | 0.0 | 0.0 | +— / -5ead8548-7453-4fa1-856e-674995576a48 |
| Jogador 3 | 2-5 | 95 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38355520367622375 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 96 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0810873880982399 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 97 | PASS | STABILIZE | 100.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 102 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 22.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9474028944969177 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -c70251e8-af44-4466-808f-d49e9e5f57e9,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5893630385398865 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 104 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499644637107849 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 105 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 2 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 2 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013116640970110893 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 108 | PASS | STABILIZE | 100.0 | 5 | 2 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 112 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8144195079803467 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 113 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33543241024017334 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 3 | 2-7 | 114 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16802388429641724 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 115 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 28.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 116 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 28.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4019553065299988 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015385122038424015 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 118 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014271140098571777 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 119 | PASS | STABILIZE | 100.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 122 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6974391341209412 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -— |
| Jogador 3 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24939414858818054 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 124 | SELL | STABILIZE | 100.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 3-1 | 125 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2831728160381317 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-1 | 126 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5034082531929016 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 127 | BUY_XP | STABILIZE | 100.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 128 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09958355128765106 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 129 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6546754240989685 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 130 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48733142018318176 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 132 | SELL | STABILIZE | 100.0 | 6 | 10 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -f19f9e7f-f189-47fe-b571-be5065c6eb39 |
| Jogador 3 | 3-2 | 133 | BUY | STABILIZE | 100.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8219898343086243 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 11 | 1 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4562878906726837 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 135 | BUY | STABILIZE | 100.0 | 6 | 11 | 1 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09128859639167786 | 0.0 | 0.0 | +f2020469-2f4e-4b95-96e4-1e7d091f1ab0 / -— |
| Jogador 3 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015495581552386284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 138 | PASS | STABILIZE | 100.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 142 | BUY | STABILIZE | 100.0 | 6 | 20 | 2 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7379761934280396 | 0.0 | 0.0 | +f0b6c16b-7610-454c-929d-7152f0a041d3 / -— |
| Jogador 3 | 3-3 | 143 | SELL | STABILIZE | 100.0 | 6 | 18 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3357555568218231 | 0.0 | 0.0 | +— / -2d1296a3-9aa4-42ab-8b86-34661e32a63d |
| Jogador 3 | 3-3 | 144 | BUY | STABILIZE | 100.0 | 6 | 21 | 2 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.060560062527656555 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 17 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005094967316836119 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 17 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 147 | PASS | STABILIZE | 100.0 | 6 | 17 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 152 | SELL | STABILIZE | 100.0 | 6 | 27 | 2 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0238735843449831 | 0.0 | 0.0 | +— / -f2020469-2f4e-4b95-96e4-1e7d091f1ab0 |
| Jogador 3 | 3-4 | 153 | BUY | STABILIZE | 100.0 | 6 | 28 | 2 | 34.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.812322735786438 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 3 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 25 | 2 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09883854538202286 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 155 | BUY_XP | STABILIZE | 100.0 | 6 | 25 | 2 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011656000278890133 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 156 | BUY_XP | STABILIZE | 100.0 | 6 | 21 | 2 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 157 | BUY_XP | STABILIZE | 100.0 | 6 | 17 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 158 | BUY_XP | STABILIZE | 100.0 | 6 | 13 | 1 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 159 | BUY_XP | STABILIZE | 100.0 | 6 | 9 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 160 | BUY_XP | STABILIZE | 100.0 | 6 | 5 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06353499740362167 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 162 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 9 | 0 | 34.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3997260332107544 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 163 | BUY | FAST8 | 100.0 | 7 | 9 | 0 | 40.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7637748122215271 | 0.0 | 0.0 | +5a16a58c-7001-4448-8ca5-6293f35e2c94 / -c3f8419e-a450-4247-bb65-8de8dba1c8ee,d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 3 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 6 | 0 | 28.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4257661998271942 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 165 | BUY | FAST8 | 100.0 | 7 | 6 | 0 | 40.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1841021329164505 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -— |
| Jogador 3 | 3-5 | 166 | MOVE_BENCH | FAST8 | 100.0 | 7 | 2 | 0 | 40.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0960879772901535 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 167 | MOVE_BENCH | FAST8 | 100.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6653690934181213 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 168 | MOVE_BENCH | FAST8 | 100.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08788936585187912 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 169 | MOVE_BENCH | FAST8 | 100.0 | 7 | 2 | 0 | 40.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08109857141971588 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 170 | MOVE_BENCH | FAST8 | 100.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.66535884141922 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 172 | SELL | FAST8 | 100.0 | 7 | 11 | 1 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5740000009536743 | 0.0 | 0.0 | +— / -5a16a58c-7001-4448-8ca5-6293f35e2c94 |
| Jogador 3 | 3-6 | 173 | BUY | FAST8 | 100.0 | 7 | 19 | 1 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7659956812858582 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -bca8862c-5e5b-4a51-9173-79218fbfea3d,f0b6c16b-7610-454c-929d-7152f0a041d3 |
| Jogador 3 | 3-6 | 174 | BUY | FAST8 | 100.0 | 7 | 17 | 1 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1421070545911789 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 3 | 3-6 | 175 | BUY | FAST8 | 100.0 | 7 | 14 | 1 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04130339249968529 | 0.0 | 0.0 | +daad4576-7a5d-4154-9b81-963d092a7207 / -— |
| Jogador 3 | 3-6 | 176 | BUY_XP | FAST8 | 100.0 | 7 | 13 | 1 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 177 | BUY_XP | FAST8 | 100.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 178 | BUY_XP | FAST8 | 100.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 179 | MOVE_BENCH | FAST8 | 100.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10187864303588867 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 180 | MOVE_BOARD | FAST8 | 100.0 | 7 | 1 | 0 | 38.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 182 | SELL | FAST8 | 90.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005002929363399744 | 0.0 | 0.0 | +— / -daad4576-7a5d-4154-9b81-963d092a7207 |
| Jogador 3 | 3-7 | 183 | BUY | FAST8 | 90.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6300621628761292 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 184 | BUY_XP | FAST8 | 90.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 185 | MOVE_BOARD | FAST8 | 90.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00356626627035439 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 186 | MOVE_BENCH | FAST8 | 90.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29161638021469116 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 187 | MOVE_BOARD | FAST8 | 90.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01475450024008751 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 188 | PASS | FAST8 | 90.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 192 | BUY | FAST8 | 90.0 | 7 | 5 | 0 | 46.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.712716281414032 | 0.0 | 0.0 | +f64919a5-eb2c-4e23-91ed-0067b3d90951 / -9028d514-586b-4d0e-b042-07389323c8cf,b75c9bc5-9bc7-465a-a97c-59156e5c482d |
| Jogador 3 | 4-1 | 193 | BUY | FAST8 | 90.0 | 7 | 2 | 0 | 46.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.28649234771728516 | 0.0 | 0.0 | +f8d6cf7b-e18c-4a52-87c6-8858f03eef72 / -— |
| Jogador 3 | 4-1 | 194 | CRAFT_AND_EQUIP | FAST8 | 90.0 | 7 | 0 | 0 | 46.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17436330020427704 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 195 | CRAFT_AND_EQUIP | FAST8 | 90.0 | 7 | 0 | 0 | 46.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18673132359981537 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 196 | MOVE_BOARD | FAST8 | 90.0 | 7 | 0 | 0 | 46.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 197 | MOVE_BOARD | FAST8 | 90.0 | 7 | 0 | 0 | 46.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 198 | PASS | FAST8 | 90.0 | 7 | 0 | 0 | 46.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 202 | BUY | FAST8 | 90.0 | 7 | 6 | 0 | 46.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2780874967575073 | 0.0 | 0.0 | +9bd6852a-b7a4-468c-a8cc-5318f7906eae / -— |
| Jogador 3 | 4-2 | 203 | MOVE_BOARD | FAST8 | 90.0 | 7 | 3 | 0 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 204 | MOVE_BOARD | FAST8 | 90.0 | 7 | 3 | 0 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015054366551339626 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 205 | PASS | FAST8 | 90.0 | 7 | 3 | 0 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 212 | MOVE_BOARD | FAST8 | 90.0 | 7 | 10 | 1 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 213 | MOVE_BOARD | FAST8 | 90.0 | 7 | 10 | 1 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 214 | PASS | FAST8 | 90.0 | 7 | 10 | 1 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 222 | MOVE_BOARD | FAST8 | 90.0 | 7 | 18 | 1 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 223 | MOVE_BOARD | FAST8 | 90.0 | 7 | 18 | 1 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 224 | PASS | FAST8 | 90.0 | 7 | 18 | 1 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027142856270074844 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 232 | MOVE_BOARD | FAST8 | 90.0 | 7 | 25 | 2 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 233 | MOVE_BOARD | FAST8 | 90.0 | 7 | 25 | 2 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014772392809391022 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 234 | PASS | FAST8 | 90.0 | 7 | 25 | 2 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11214285343885422 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 242 | SELL | FAST8 | 90.0 | 7 | 34 | 3 | 46.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011833333410322666 | 0.0 | 0.0 | +— / -f64919a5-eb2c-4e23-91ed-0067b3d90951 |
| Jogador 3 | 4-6 | 243 | BUY | FAST8 | 90.0 | 7 | 42 | 4 | 46.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7733235359191895 | 0.0 | 0.0 | +6ea982ab-292d-42fc-99e6-d67c89f9f4fe / -79786887-d318-4836-b2f0-c0f03e86cbe5,8a68772c-3f02-4f2e-882b-4fa69fbb6750 |
| Jogador 3 | 4-6 | 244 | MOVE_BENCH | STABILIZE | 90.0 | 7 | 39 | 3 | 34.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15063361823558807 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 245 | BUY | FAST8 | 90.0 | 7 | 39 | 3 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2713005542755127 | 0.0 | 0.0 | +84e865bc-366e-45cd-85e4-fa7314688368 / -— |
| Jogador 3 | 4-6 | 246 | MOVE_BOARD | FAST8 | 90.0 | 7 | 38 | 3 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.16185531928204e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 247 | MOVE_BOARD | FAST8 | 90.0 | 7 | 38 | 3 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999953098595142 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 248 | MOVE_BOARD | FAST8 | 90.0 | 7 | 38 | 3 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017258550971746445 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 249 | PASS | FAST8 | 90.0 | 7 | 38 | 3 | 38.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041428569704294205 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 252 | BUY | FAST8 | 90.0 | 7 | 49 | 4 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6905988454818726 | 0.0 | 0.0 | +0a6546e5-8a3b-461e-ad5d-3dbd49f21e2c / -— |
| Jogador 3 | 4-7 | 253 | MOVE_BOARD | FAST8 | 90.0 | 7 | 45 | 4 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00010564201511442661 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 254 | MOVE_BOARD | FAST8 | 90.0 | 7 | 45 | 4 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013716244138777256 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 255 | MOVE_BOARD | FAST8 | 90.0 | 7 | 45 | 4 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 256 | PASS | FAST8 | 90.0 | 7 | 45 | 4 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18642857670783997 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 90.0 | 7 | 56 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21795277297496796 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 90.0 | 7 | 56 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1540239453315735 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 264 | MOVE_BOARD | FAST8 | 90.0 | 7 | 56 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 265 | MOVE_BOARD | FAST8 | 90.0 | 7 | 56 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 266 | PASS | FAST8 | 90.0 | 7 | 56 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09173611551523209 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 272 | SELL | FAST8 | 90.0 | 7 | 70 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -f8d6cf7b-e18c-4a52-87c6-8858f03eef72 |
| Jogador 3 | 5-2 | 273 | BUY | FAST8 | 90.0 | 7 | 72 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.860397219657898 | 0.0 | 0.0 | +7a419783-907e-47e2-bf69-29a54ee18a02 / -— |
| Jogador 3 | 5-2 | 274 | MOVE_BOARD | FAST8 | 90.0 | 7 | 71 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.873379223444772e-08 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 275 | MOVE_BOARD | FAST8 | 90.0 | 7 | 71 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01732691377401352 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 276 | PASS | FAST8 | 90.0 | 7 | 71 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10282160341739655 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 282 | SELL | FAST8 | 74.0 | 7 | 81 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -84e865bc-366e-45cd-85e4-fa7314688368 |
| Jogador 3 | 5-3 | 283 | BUY | FAST8 | 74.0 | 7 | 82 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12969066202640533 | 0.0 | 0.0 | +dcb61be2-9a58-49bc-9f11-2f5fce42e7ea / -— |
| Jogador 3 | 5-3 | 284 | MOVE_BOARD | FAST8 | 74.0 | 7 | 79 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002326754154637456 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 285 | MOVE_BOARD | FAST8 | 74.0 | 7 | 79 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 286 | MOVE_BOARD | FAST8 | 74.0 | 7 | 79 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 287 | PASS | FAST8 | 74.0 | 7 | 79 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1091393530368805 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 292 | SELL | FAST8 | 58.0 | 7 | 90 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05175686255097389 | 0.0 | 0.0 | +— / -dcb61be2-9a58-49bc-9f11-2f5fce42e7ea |
| Jogador 3 | 5-4 | 293 | BUY | FAST8 | 58.0 | 7 | 93 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38187170028686523 | 0.0 | 0.0 | +bbfa514f-8d07-411b-aa19-4511ae5fb5cd / -— |
| Jogador 3 | 5-4 | 294 | SELL | FAST8 | 58.0 | 7 | 91 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5925999879837036 | 0.0 | 0.0 | +— / -bbfa514f-8d07-411b-aa19-4511ae5fb5cd |
| Jogador 3 | 5-4 | 295 | BUY | FAST8 | 58.0 | 7 | 93 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8424127101898193 | 0.0 | 0.0 | +407092ea-3a14-4555-9ebd-64a36c41d1d0 / -2fa86b11-4e28-4652-890e-f00a79068223,41db1132-4e1c-48eb-8a9b-1b2c74cb22ce |
| Jogador 3 | 5-4 | 296 | BUY | FAST8 | 58.0 | 7 | 91 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1342051774263382 | 0.0 | 0.0 | +674bcfdb-fddd-498c-ba65-ef3a3b989f07 / -— |
| Jogador 3 | 5-4 | 297 | MOVE_BOARD | FAST8 | 58.0 | 7 | 88 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.901743414440716e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 298 | MOVE_BOARD | FAST8 | 58.0 | 7 | 88 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999985694885254 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 299 | MOVE_BOARD | FAST8 | 58.0 | 7 | 88 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 300 | PASS | FAST8 | 58.0 | 7 | 88 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11645875871181488 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 302 | BUY | FAST8 | 58.0 | 7 | 99 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6420252919197083 | 0.0 | 0.0 | +d4c27edc-9b7e-4a31-a967-3aa80766b470 / -— |
| Jogador 3 | 5-5 | 303 | SELL | FAST8 | 58.0 | 7 | 96 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08615310490131378 | 0.0 | 0.0 | +— / -407092ea-3a14-4555-9ebd-64a36c41d1d0 |
| Jogador 3 | 5-5 | 304 | BUY | FAST8 | 58.0 | 7 | 101 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12045039236545563 | 0.0 | 0.0 | +0a29573e-2a7b-4719-9b6e-49c2f476bc04 / -— |
| Jogador 3 | 5-5 | 305 | SELL | FAST8 | 58.0 | 7 | 96 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02419999986886978 | 0.0 | 0.0 | +— / -0a29573e-2a7b-4719-9b6e-49c2f476bc04 |
| Jogador 3 | 5-5 | 306 | BUY | FAST8 | 58.0 | 7 | 101 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.061776332557201385 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 3 | 5-5 | 307 | MOVE_BOARD | FAST8 | 58.0 | 7 | 98 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 308 | MOVE_BOARD | FAST8 | 58.0 | 7 | 98 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999903738498688 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 309 | PASS | FAST8 | 58.0 | 7 | 98 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12479758262634277 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 312 | SELL | FAST8 | 42.0 | 7 | 109 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -f078e755-d142-4dad-99d0-7e7599e3016d |
| Jogador 3 | 5-6 | 313 | BUY | FAST8 | 42.0 | 7 | 112 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9334914088249207 | 0.0 | 0.0 | +8068dc77-9528-4a1d-b4dc-5ac216e8684f / -674bcfdb-fddd-498c-ba65-ef3a3b989f07,d4c27edc-9b7e-4a31-a967-3aa80766b470 |
| Jogador 3 | 5-6 | 314 | BUY | FAST8 | 42.0 | 7 | 109 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1010013148188591 | 0.0 | 0.0 | +8faad4f9-9f15-49e8-94af-b4d28879cc0d / -— |
| Jogador 3 | 5-6 | 315 | BUY | FAST8 | 42.0 | 7 | 106 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2585703134536743 | 0.0 | 0.0 | +3365b4aa-125c-4f72-bcc5-01c5a205b9b0 / -— |
| Jogador 3 | 5-6 | 316 | MOVE_BOARD | FAST8 | 42.0 | 7 | 102 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 317 | MOVE_BOARD | FAST8 | 42.0 | 7 | 102 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0150001747533679 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 318 | PASS | FAST8 | 42.0 | 7 | 102 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14015240967273712 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 322 | SELL | STABILIZE | 27.0 | 7 | 113 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12304262816905975 | 0.0 | 0.0 | +— / -8068dc77-9528-4a1d-b4dc-5ac216e8684f |
| Jogador 3 | 5-7 | 323 | BUY | STABILIZE | 27.0 | 7 | 121 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9510056376457214 | 0.0 | 0.0 | +5de51369-647a-45bd-95b7-c8efe44c5484 / -— |
| Jogador 3 | 5-7 | 324 | SELL | STABILIZE | 27.0 | 7 | 120 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -8faad4f9-9f15-49e8-94af-b4d28879cc0d |
| Jogador 3 | 5-7 | 325 | BUY | STABILIZE | 27.0 | 7 | 123 | 5 | 50.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7726971507072449 | 0.0 | 0.0 | +c5520bc4-3123-40f3-b275-83fa8cb06309 / -2a2066ee-841b-49d5-8b82-1d47feb36d8c,9bd6852a-b7a4-468c-a8cc-5318f7906eae |
| Jogador 3 | 5-7 | 326 | BUY | STABILIZE | 27.0 | 7 | 120 | 5 | 44.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08599930256605148 | 0.0 | 0.0 | +0a0e7d41-96bf-404f-a3bf-98df0a182b63 / -— |
| Jogador 3 | 5-7 | 327 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 117 | 5 | 44.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40085604786872864 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 328 | BUY | STABILIZE | 27.0 | 7 | 117 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010947338305413723 | 0.0 | 0.0 | +bdee5671-864a-47c9-9576-9e0d8d2a7c6a / -— |
| Jogador 3 | 5-7 | 329 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 115 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 330 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 115 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 332 | EQUIP_FROM_INVENTORY | STABILIZE | 27.0 | 7 | 126 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05824780464172363 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 333 | SELL | STABILIZE | 27.0 | 7 | 126 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -bdee5671-864a-47c9-9576-9e0d8d2a7c6a |
| Jogador 3 | 6-1 | 334 | BUY | STABILIZE | 27.0 | 7 | 128 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2720890939235687 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -— |
| Jogador 3 | 6-1 | 335 | SELL | STABILIZE | 27.0 | 7 | 124 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -0a0e7d41-96bf-404f-a3bf-98df0a182b63 |
| Jogador 3 | 6-1 | 336 | BUY | STABILIZE | 27.0 | 7 | 127 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11635567992925644 | 0.0 | 0.0 | +920ec426-49cf-489f-aad8-3f5461b93be6 / -— |
| Jogador 3 | 6-1 | 337 | SELL | STABILIZE | 27.0 | 7 | 124 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035466667264699936 | 0.0 | 0.0 | +— / -920ec426-49cf-489f-aad8-3f5461b93be6 |
| Jogador 3 | 6-1 | 338 | BUY | STABILIZE | 27.0 | 7 | 127 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1823813021183014 | 0.0 | 0.0 | +b1d58916-6d8b-4071-a37d-a478395e6a1e / -— |
| Jogador 3 | 6-1 | 339 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 124 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 340 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 124 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 342 | SELL | STABILIZE | 27.0 | 8 | 135 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06840460002422333 | 0.0 | 0.0 | +— / -b1d58916-6d8b-4071-a37d-a478395e6a1e |
| Jogador 3 | 6-2 | 343 | BUY | STABILIZE | 27.0 | 8 | 138 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.066685438156128 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -0a6546e5-8a3b-461e-ad5d-3dbd49f21e2c,527f78df-1e51-4731-9175-1c4812aa82ad |
| Jogador 3 | 6-2 | 344 | BUY | STABILIZE | 27.0 | 8 | 134 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13335342705249786 | 0.0 | 0.0 | +aa803972-8af8-46d7-b430-079819730c36 / -— |
| Jogador 3 | 6-2 | 345 | BUY | STABILIZE | 27.0 | 8 | 130 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27149730920791626 | 0.0 | 0.0 | +dc423197-9320-4651-b71d-a62086416f9d / -— |
| Jogador 3 | 6-2 | 346 | SELL | STABILIZE | 27.0 | 8 | 128 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5834555625915527 | 0.0 | 0.0 | +— / -2b10436d-ccfe-4329-aef8-2769899b3787 |
| Jogador 3 | 6-2 | 347 | BUY | STABILIZE | 27.0 | 8 | 139 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24288055300712585 | 0.0 | 0.0 | +92bac611-1820-42eb-8243-499f20058673 / -— |
| Jogador 3 | 6-2 | 348 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 138 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.5072065251995355e-09 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 349 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 138 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01607523299753666 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 350 | PASS | STABILIZE | 27.0 | 8 | 138 | 5 | 56.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24019400775432587 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 352 | BUY | STABILIZE | 27.0 | 8 | 149 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35344016551971436 | 0.0 | 0.0 | +5e8a73b8-846a-49a9-be41-30c3baf2cb55 / -— |
| Jogador 3 | 6-3 | 353 | SELL | STABILIZE | 27.0 | 8 | 147 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009600000455975533 | 0.0 | 0.0 | +— / -92bac611-1820-42eb-8243-499f20058673 |
| Jogador 3 | 6-3 | 354 | BUY | STABILIZE | 27.0 | 8 | 148 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06064991280436516 | 0.0 | 0.0 | +5d95f8bc-0c01-4c67-8764-4410eb32ee93 / -— |
| Jogador 3 | 6-3 | 355 | SELL | STABILIZE | 27.0 | 8 | 145 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -dc423197-9320-4651-b71d-a62086416f9d |
| Jogador 3 | 6-3 | 356 | BUY | STABILIZE | 27.0 | 8 | 147 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17152048647403717 | 0.0 | 0.0 | +46b04fe4-ef4d-4449-94d0-d8bc9660c4e0 / -— |
| Jogador 3 | 6-3 | 357 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 145 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 358 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 145 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 359 | PASS | STABILIZE | 27.0 | 8 | 145 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2470625638961792 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 362 | SELL | STABILIZE | 27.0 | 8 | 156 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00729750981554389 | 0.0 | 0.0 | +— / -46b04fe4-ef4d-4449-94d0-d8bc9660c4e0 |
| Jogador 3 | 6-4 | 363 | BUY | STABILIZE | 27.0 | 8 | 158 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006829742807894945 | 0.0 | 0.0 | +87726d3e-4b0d-41ae-bf43-893d4092bd5b / -— |
| Jogador 3 | 6-4 | 364 | SELL | STABILIZE | 27.0 | 8 | 154 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02117163874208927 | 0.0 | 0.0 | +— / -5d95f8bc-0c01-4c67-8764-4410eb32ee93 |
| Jogador 3 | 6-4 | 365 | BUY | STABILIZE | 27.0 | 8 | 157 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017379965633153915 | 0.0 | 0.0 | +f1ece814-0986-421f-b5df-0b457ebaa484 / -— |
| Jogador 3 | 6-4 | 366 | SELL | STABILIZE | 27.0 | 8 | 154 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -f1ece814-0986-421f-b5df-0b457ebaa484 |
| Jogador 3 | 6-4 | 367 | BUY | STABILIZE | 27.0 | 8 | 157 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017361512407660484 | 0.0 | 0.0 | +5184a53b-fca3-448c-b5ab-7daa37b0c259 / -— |
| Jogador 3 | 6-4 | 368 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 154 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 369 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 154 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013846129179000854 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 370 | PASS | STABILIZE | 27.0 | 8 | 154 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2559678256511688 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 372 | SELL | STABILIZE | 27.0 | 8 | 165 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -5184a53b-fca3-448c-b5ab-7daa37b0c259 |
| Jogador 3 | 6-5 | 373 | BUY | STABILIZE | 27.0 | 8 | 168 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.249909445643425 | 0.0 | 0.0 | +f55e2447-5d65-4f95-9f26-5b9017efefe0 / -— |
| Jogador 3 | 6-5 | 374 | SELL | STABILIZE | 27.0 | 8 | 165 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08313333243131638 | 0.0 | 0.0 | +— / -5e8a73b8-846a-49a9-be41-30c3baf2cb55 |
| Jogador 3 | 6-5 | 375 | BUY | STABILIZE | 27.0 | 8 | 167 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1666242778301239 | 0.0 | 0.0 | +d8ca1093-815c-4f3e-af3e-fd6c4ab6ecd8 / -— |
| Jogador 3 | 6-5 | 376 | SELL | STABILIZE | 27.0 | 8 | 165 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007024586200714111 | 0.0 | 0.0 | +— / -d8ca1093-815c-4f3e-af3e-fd6c4ab6ecd8 |
| Jogador 3 | 6-5 | 377 | BUY | STABILIZE | 27.0 | 8 | 167 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023366177454590797 | 0.0 | 0.0 | +9a2edb0f-a3cd-455c-8406-2a7ca80e3bc6 / -— |
| Jogador 3 | 6-5 | 378 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 166 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.367965473444201e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 379 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 166 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999940060079098 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 380 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 166 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-6 | 382 | SELL | STABILIZE | 27.0 | 8 | 177 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010333333164453506 | 0.0 | 0.0 | +— / -9a2edb0f-a3cd-455c-8406-2a7ca80e3bc6 |
| Jogador 3 | 6-6 | 383 | BUY | STABILIZE | 27.0 | 8 | 178 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035146135836839676 | 0.0 | 0.0 | +24d03668-5dc4-4b40-9439-a1d67522d0a3 / -— |
| Jogador 3 | 6-6 | 384 | SELL | STABILIZE | 27.0 | 8 | 174 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -87726d3e-4b0d-41ae-bf43-893d4092bd5b |
| Jogador 3 | 6-6 | 385 | BUY | STABILIZE | 27.0 | 8 | 178 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0055366032756865025 | 0.0 | 0.0 | +e903e009-8dae-4fc9-b0ec-bc028c3f9f3e / -— |
| Jogador 3 | 6-6 | 386 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 177 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-6 | 387 | SELL | STABILIZE | 27.0 | 8 | 177 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006488241255283356 | 0.0 | 0.0 | +— / -e903e009-8dae-4fc9-b0ec-bc028c3f9f3e |
| Jogador 3 | 6-6 | 388 | BUY | STABILIZE | 27.0 | 8 | 178 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2598058581352234 | 0.0 | 0.0 | +c3596d89-03d2-4fc7-afaf-591f10423252 / -— |
| Jogador 3 | 6-6 | 389 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 175 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-6 | 390 | MOVE_BOARD | STABILIZE | 27.0 | 8 | 175 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015415001660585403 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-7 | 392 | SELL | ALL_IN | 9.0 | 8 | 187 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -c3596d89-03d2-4fc7-afaf-591f10423252 |
| Jogador 3 | 6-7 | 393 | BUY | ALL_IN | 9.0 | 8 | 190 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7883643507957458 | 0.0 | 0.0 | +533790d1-aca6-417d-b163-b0bda70d1500 / -— |
| Jogador 3 | 6-7 | 394 | SELL | ALL_IN | 9.0 | 8 | 187 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.031942907720804214 | 0.0 | 0.0 | +— / -24d03668-5dc4-4b40-9439-a1d67522d0a3 |
| Jogador 3 | 6-7 | 395 | BUY | ALL_IN | 9.0 | 8 | 191 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18180431425571442 | 0.0 | 0.0 | +ff6d5b66-5b8f-49b1-bbad-4231b794c2f1 / -— |
| Jogador 3 | 6-7 | 396 | SELL | ALL_IN | 9.0 | 8 | 186 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -ff6d5b66-5b8f-49b1-bbad-4231b794c2f1 |
| Jogador 3 | 6-7 | 397 | BUY | ALL_IN | 9.0 | 8 | 191 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09345763921737671 | 0.0 | 0.0 | +0366f83c-b9d4-47c2-aa5e-4dc1021bd201 / -— |
| Jogador 3 | 6-7 | 398 | SELL | ALL_IN | 9.0 | 8 | 188 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020891867578029633 | 0.0 | 0.0 | +— / -0366f83c-b9d4-47c2-aa5e-4dc1021bd201 |
| Jogador 3 | 6-7 | 399 | BUY | ALL_IN | 9.0 | 8 | 191 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0937400832772255 | 0.0 | 0.0 | +14f6071d-5085-47a5-b657-04043b21adce / -— |
| Jogador 3 | 6-7 | 400 | MOVE_BOARD | ALL_IN | 9.0 | 8 | 188 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00017898462829180062 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 402 | EQUIP_FROM_INVENTORY | ALL_IN | 9.0 | 8 | 200 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05594846233725548 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 403 | SELL | ALL_IN | 9.0 | 8 | 200 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017071934416890144 | 0.0 | 0.0 | +— / -14f6071d-5085-47a5-b657-04043b21adce |
| Jogador 3 | 7-1 | 404 | BUY | ALL_IN | 9.0 | 8 | 203 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1760462075471878 | 0.0 | 0.0 | +1b7347d3-3505-47d6-a324-bbf75b32db31 / -— |
| Jogador 3 | 7-1 | 405 | SELL | ALL_IN | 9.0 | 8 | 199 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05006828531622887 | 0.0 | 0.0 | +— / -1b7347d3-3505-47d6-a324-bbf75b32db31 |
| Jogador 3 | 7-1 | 406 | BUY | ALL_IN | 9.0 | 8 | 203 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16747719049453735 | 0.0 | 0.0 | +0d4bcb6c-af4b-4726-a600-d24420cb04bd / -— |
| Jogador 3 | 7-1 | 407 | MOVE_BOARD | ALL_IN | 9.0 | 8 | 198 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 408 | MOVE_BOARD | ALL_IN | 9.0 | 8 | 198 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015370865352451801 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 409 | PASS | ALL_IN | 9.0 | 8 | 198 | 5 | 64.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6805257201194763 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2201479971408844 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09193183481693268 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4641140401363373 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16314318776130676 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0601743720471859 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0128185749053955 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 40 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3392305076122284 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 41 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9802137017250061 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18394431471824646 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2162981927394867 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 55 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 56 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9555449485778809 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 63 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 64 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 72 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9438915252685547 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 73 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0434497594833374 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 74 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3041950762271881 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 75 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Camille | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5619999766349792 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 76 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 77 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10036028176546097 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 79 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5416666865348816 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-3 | 80 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1373327672481537 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23761343955993652 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15833333134651184 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005146525800228119 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11433333158493042 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08100000023841858 | 0.0 | 0.0 | +— / -0b62545c-1de0-47d8-bb4c-119f7e1526b3 |
| Jogador 4 | 2-4 | 89 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24992735683918 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 90 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9549183249473572 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 4 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0011502504348755 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -86c535a4-a22b-4667-bc0f-46b4843d97cc,8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37761837244033813 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 94 | SELL | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -4b07138d-44fd-4515-8b65-d7db84f4639c |
| Jogador 4 | 2-5 | 95 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3863356411457062 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 4 | 2-5 | 96 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 97 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6152015328407288 | 0.0 | 0.0 | +— / -c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 4 | 2-5 | 98 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 1 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1482894867658615 | 0.0 | 0.0 | +— / -— |
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
| Jogador 4 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 82.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23672933876514435 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 125 | BUY | STABILIZE | 82.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02350044995546341 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 1 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 127 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 1 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01444273628294468 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 128 | PASS | STABILIZE | 82.0 | 6 | 1 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 132 | BUY | STABILIZE | 73.0 | 6 | 7 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379772901535034 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 133 | BUY | STABILIZE | 73.0 | 6 | 6 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879757285118103 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 5 | 0 | 16.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9983378648757935 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 135 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 5 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5012826323509216 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 136 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 5 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19315575063228607 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 137 | BUY | STABILIZE | 73.0 | 6 | 5 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2763775587081909 | 0.0 | 0.0 | +421bcbcb-ecb2-4af8-88d4-7be6cd284d27 / -— |
| Jogador 4 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 2 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011960487812757492 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 139 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 2 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4118227958679199 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 140 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 2 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3426705598831177 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 142 | BUY | STABILIZE | 73.0 | 6 | 8 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8033666610717773 | 0.0 | 0.0 | +409b32b9-5280-4d79-b5b2-871ed597ba56 / -— |
| Jogador 4 | 3-3 | 143 | BUY | STABILIZE | 73.0 | 6 | 5 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8028855919837952 | 0.0 | 0.0 | +52018505-08c9-471f-83b9-fd5066efe55a / -— |
| Jogador 4 | 3-3 | 144 | BUY | STABILIZE | 73.0 | 6 | 3 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1753115952014923 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 2 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0030303203966468573 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 2 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 147 | PASS | STABILIZE | 73.0 | 6 | 2 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 152 | SELL | STABILIZE | 64.0 | 6 | 7 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 3-4 | 153 | BUY | STABILIZE | 64.0 | 6 | 10 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7236784100532532 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 154 | EQUIP_FROM_INVENTORY | STABILIZE | 64.0 | 6 | 7 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09678264707326889 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 155 | EQUIP_FROM_INVENTORY | STABILIZE | 64.0 | 6 | 7 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0917966440320015 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 156 | EQUIP_FROM_INVENTORY | STABILIZE | 64.0 | 6 | 7 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.025030512362718582 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 157 | SELL | STABILIZE | 64.0 | 6 | 7 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -f71a7192-663d-46a0-93ef-b900c59c3bde |
| Jogador 4 | 3-4 | 158 | BUY | STABILIZE | 64.0 | 6 | 9 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8346766233444214 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -52018505-08c9-471f-83b9-fd5066efe55a,8052731e-e34c-4de7-84b1-2b986cfeddaa |
| Jogador 4 | 3-4 | 159 | BUY | STABILIZE | 64.0 | 6 | 7 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6800234913825989 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -— |
| Jogador 4 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 6 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0934445783495903 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 162 | BUY | STABILIZE | 64.0 | 6 | 11 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2053343653678894 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -— |
| Jogador 4 | 3-5 | 163 | SELL | STABILIZE | 64.0 | 6 | 9 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -7fd03119-ac82-49e1-b3bb-3a0caa31011f |
| Jogador 4 | 3-5 | 164 | BUY | STABILIZE | 64.0 | 6 | 14 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.482134610414505 | 0.0 | 0.0 | +661b176a-5963-4715-b9dd-aca29f552fa9 / -6bbf1aa9-e129-45c6-8668-699425d97c5d,764470bb-9820-4e49-98f9-5a5f0ce5ca8f |
| Jogador 4 | 3-5 | 165 | BUY | STABILIZE | 64.0 | 6 | 12 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05272701382637024 | 0.0 | 0.0 | +62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 / -— |
| Jogador 4 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 9 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00023144159058574587 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 9 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 9 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2790869474411011 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 169 | PASS | STABILIZE | 64.0 | 6 | 9 | 0 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 172 | BUY | STABILIZE | 64.0 | 6 | 16 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8030070066452026 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 173 | SELL | STABILIZE | 64.0 | 6 | 13 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022866666316986084 | 0.0 | 0.0 | +— / -661b176a-5963-4715-b9dd-aca29f552fa9 |
| Jogador 4 | 3-6 | 174 | BUY | STABILIZE | 64.0 | 6 | 18 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8026572465896606 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -— |
| Jogador 4 | 3-6 | 175 | SELL | STABILIZE | 64.0 | 6 | 16 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013390898704528809 | 0.0 | 0.0 | +— / -62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 |
| Jogador 4 | 3-6 | 176 | BUY | STABILIZE | 64.0 | 6 | 19 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09031298756599426 | 0.0 | 0.0 | +320038b5-88c4-48fe-a7fa-a30823d674c0 / -— |
| Jogador 4 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 18 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21669387817382812 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 18 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014215855859220028 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 179 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 18 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015312505885958672 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 180 | PASS | STABILIZE | 64.0 | 6 | 18 | 1 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 182 | SELL | STABILIZE | 64.0 | 6 | 26 | 2 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5009588003158569 | 0.0 | 0.0 | +— / -d754fcfc-6d22-4bc0-8643-8f4bef9afda5 |
| Jogador 4 | 3-7 | 183 | BUY | STABILIZE | 64.0 | 6 | 27 | 2 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8488476872444153 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-7 | 184 | MOVE_BENCH | STABILIZE | 64.0 | 6 | 24 | 2 | 20.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4293462932109833 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 185 | BUY | STABILIZE | 64.0 | 6 | 24 | 2 | 26.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04398501291871071 | 0.0 | 0.0 | +59f588eb-e3f3-4907-ab23-af073a26bd6a / -— |
| Jogador 4 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 22 | 2 | 26.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10484860092401505 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 187 | SELL | STABILIZE | 64.0 | 6 | 22 | 2 | 26.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5389999747276306 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 4 | 3-7 | 188 | SELL | STABILIZE | 64.0 | 6 | 30 | 3 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1319088637828827 | 0.0 | 0.0 | +— / -ac8f2a7d-1627-4aa4-a35b-805bce651b0e |
| Jogador 4 | 3-7 | 189 | BUY | STABILIZE | 64.0 | 6 | 31 | 3 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3410132825374603 | 0.0 | 0.0 | +eab06dbd-05d4-43b6-88f0-e6abb0e83d34 / -— |
| Jogador 4 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 29 | 2 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06127576529979706 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 192 | BUY | STABILIZE | 64.0 | 6 | 37 | 3 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7955379486083984 | 0.0 | 0.0 | +465ecc70-f5da-47f4-a7c0-2005a8ed24c1 / -— |
| Jogador 4 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 64.0 | 6 | 36 | 3 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19757625460624695 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 64.0 | 6 | 36 | 3 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23064827919006348 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 195 | BUY | STABILIZE | 64.0 | 6 | 36 | 3 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3079143464565277 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -— |
| Jogador 4 | 4-1 | 196 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 34 | 3 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 197 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 34 | 3 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29441460967063904 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 198 | PASS | STABILIZE | 64.0 | 6 | 34 | 3 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03857142850756645 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 202 | SELL | STABILIZE | 51.0 | 6 | 42 | 4 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00026666666963137686 | 0.0 | 0.0 | +— / -59f588eb-e3f3-4907-ab23-af073a26bd6a |
| Jogador 4 | 4-2 | 203 | BUY | STABILIZE | 51.0 | 6 | 44 | 4 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9252981543540955 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -23f4d10f-2614-47b2-bfb2-4fb276764b5e,fe6546c3-86ef-40e1-aa7e-ff7e400fe628 |
| Jogador 4 | 4-2 | 204 | BUY | STABILIZE | 51.0 | 6 | 42 | 4 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2593061327934265 | 0.0 | 0.0 | +090f2ba6-5514-49ba-a80d-a0711cd06245 / -— |
| Jogador 4 | 4-2 | 205 | SELL | STABILIZE | 51.0 | 6 | 39 | 3 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5450000166893005 | 0.0 | 0.0 | +— / -4363594b-375b-45d4-9b1a-0c1ab96367a1 |
| Jogador 4 | 4-2 | 206 | SELL | STABILIZE | 51.0 | 6 | 44 | 4 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2590000033378601 | 0.0 | 0.0 | +— / -090f2ba6-5514-49ba-a80d-a0711cd06245 |
| Jogador 4 | 4-2 | 207 | SELL | STABILIZE | 51.0 | 6 | 47 | 4 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45233333110809326 | 0.0 | 0.0 | +— / -eab06dbd-05d4-43b6-88f0-e6abb0e83d34 |
| Jogador 4 | 4-2 | 208 | BUY | STABILIZE | 51.0 | 6 | 49 | 4 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07151609659194946 | 0.0 | 0.0 | +55944609-f4df-4e53-a1d1-31c79a148b22 / -— |
| Jogador 4 | 4-2 | 209 | BUY | STABILIZE | 51.0 | 6 | 48 | 4 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36555546522140503 | 0.0 | 0.0 | +f394f34c-c68b-4213-9eb0-88f302976405 / -— |
| Jogador 4 | 4-2 | 210 | MOVE_BOARD | STABILIZE | 51.0 | 6 | 47 | 4 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3433130979537964 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 212 | BUY | STABILIZE | 39.0 | 6 | 57 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3619796335697174 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 4 | 4-3 | 213 | BUY | STABILIZE | 39.0 | 6 | 55 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07994556427001953 | 0.0 | 0.0 | +7b3e8122-3b51-46b5-94a8-68fb77156e0e / -— |
| Jogador 4 | 4-3 | 214 | SELL | STABILIZE | 39.0 | 6 | 52 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -210d2415-663d-4768-bbc2-238766c2b863 |
| Jogador 4 | 4-3 | 215 | BUY | STABILIZE | 39.0 | 6 | 54 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18724045157432556 | 0.0 | 0.0 | +60138930-82d5-4f1c-a5fe-a22ea4b70d36 / -— |
| Jogador 4 | 4-3 | 216 | SELL | STABILIZE | 39.0 | 6 | 51 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -60138930-82d5-4f1c-a5fe-a22ea4b70d36 |
| Jogador 4 | 4-3 | 217 | BUY | STABILIZE | 39.0 | 6 | 54 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20132119953632355 | 0.0 | 0.0 | +26462e09-ab6e-4b87-85a8-6bda974b0c45 / -— |
| Jogador 4 | 4-3 | 218 | REROLL | STABILIZE | 39.0 | 6 | 51 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24070000648498535 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 219 | SELL | STABILIZE | 39.0 | 6 | 49 | 4 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0746999979019165 | 0.0 | 0.0 | +— / -26462e09-ab6e-4b87-85a8-6bda974b0c45 |
| Jogador 4 | 4-3 | 220 | BUY | STABILIZE | 39.0 | 6 | 52 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8830143809318542 | 0.0 | 0.0 | +a7893c5d-2faa-4292-9240-f3cc5813151e / -— |
| Jogador 4 | 4-4 | 222 | SELL | STABILIZE | 39.0 | 7 | 61 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44530001282691956 | 0.0 | 0.0 | +— / -55944609-f4df-4e53-a1d1-31c79a148b22 |
| Jogador 4 | 4-4 | 223 | BUY | STABILIZE | 39.0 | 7 | 62 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24031446874141693 | 0.0 | 0.0 | +84a3b0f5-c448-4fe1-b001-5ceff2ed306a / -— |
| Jogador 4 | 4-4 | 224 | MOVE_BENCH | STABILIZE | 39.0 | 7 | 58 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4739694893360138 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 225 | BUY | STABILIZE | 39.0 | 7 | 58 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19865188002586365 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -— |
| Jogador 4 | 4-4 | 226 | MOVE_BOARD | STABILIZE | 39.0 | 7 | 55 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011357201263308525 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 227 | MOVE_BOARD | STABILIZE | 39.0 | 7 | 55 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006141571328043938 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 228 | PASS | STABILIZE | 39.0 | 7 | 55 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09417925775051117 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 232 | SELL | STABILIZE | 39.0 | 7 | 65 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026666666381061077 | 0.0 | 0.0 | +— / -f394f34c-c68b-4213-9eb0-88f302976405 |
| Jogador 4 | 4-5 | 233 | BUY | STABILIZE | 39.0 | 7 | 66 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02969937026500702 | 0.0 | 0.0 | +ac547bcb-d285-480d-b50e-3cfba572db5a / -— |
| Jogador 4 | 4-5 | 234 | SELL | STABILIZE | 39.0 | 7 | 62 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00860000029206276 | 0.0 | 0.0 | +— / -2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 |
| Jogador 4 | 4-5 | 235 | BUY | STABILIZE | 39.0 | 7 | 65 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22348587214946747 | 0.0 | 0.0 | +262702a6-b710-4129-9dc6-0c1a04514ff9 / -— |
| Jogador 4 | 4-5 | 236 | SELL | STABILIZE | 39.0 | 7 | 62 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -262702a6-b710-4129-9dc6-0c1a04514ff9 |
| Jogador 4 | 4-5 | 237 | BUY | STABILIZE | 39.0 | 7 | 65 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23982131481170654 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -— |
| Jogador 4 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 39.0 | 7 | 62 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0034863559994846582 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 39.0 | 7 | 62 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 240 | MOVE_BOARD | STABILIZE | 39.0 | 7 | 62 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3585646450519562 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 242 | SELL | STABILIZE | 26.0 | 7 | 72 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004399999976158142 | 0.0 | 0.0 | +— / -8aa832ec-4c09-43bd-ae21-baf7268e468d |
| Jogador 4 | 4-6 | 243 | BUY | STABILIZE | 26.0 | 7 | 75 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9431852102279663 | 0.0 | 0.0 | +27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 / -320038b5-88c4-48fe-a7fa-a30823d674c0,465ecc70-f5da-47f4-a7c0-2005a8ed24c1 |
| Jogador 4 | 4-6 | 244 | BUY | STABILIZE | 26.0 | 7 | 74 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18584726750850677 | 0.0 | 0.0 | +590d07db-5e90-4705-a7ae-96f84fd06382 / -— |
| Jogador 4 | 4-6 | 245 | BUY | STABILIZE | 26.0 | 7 | 71 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43655580282211304 | 0.0 | 0.0 | +18e21ac6-f873-4310-95c8-bd8e62612479 / -— |
| Jogador 4 | 4-6 | 246 | REROLL | STABILIZE | 26.0 | 7 | 68 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 247 | SELL | STABILIZE | 26.0 | 7 | 66 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5626333355903625 | 0.0 | 0.0 | +— / -27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 |
| Jogador 4 | 4-6 | 248 | BUY | STABILIZE | 26.0 | 7 | 69 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38028234243392944 | 0.0 | 0.0 | +d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 / -— |
| Jogador 4 | 4-6 | 249 | MOVE_BENCH | STABILIZE | 26.0 | 7 | 66 | 5 | 30.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10071923583745956 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 250 | SELL | STABILIZE | 26.0 | 7 | 66 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02185652032494545 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 4-7 | 252 | BUY | ALL_IN | 14.0 | 7 | 79 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9773849248886108 | 0.0 | 0.0 | +18d25cfb-d559-4efa-b708-c9987987590b / -— |
| Jogador 4 | 4-7 | 253 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 7 | 76 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14170067012310028 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 254 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 7 | 76 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07939355820417404 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 255 | EQUIP_FROM_INVENTORY | ALL_IN | 14.0 | 7 | 76 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14883120357990265 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 256 | SELL | ALL_IN | 14.0 | 7 | 76 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -84a3b0f5-c448-4fe1-b001-5ceff2ed306a |
| Jogador 4 | 4-7 | 257 | BUY | ALL_IN | 14.0 | 7 | 80 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04594724625349045 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 4 | 4-7 | 258 | REROLL | ALL_IN | 14.0 | 7 | 77 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 259 | SELL | ALL_IN | 14.0 | 7 | 75 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00426666671410203 | 0.0 | 0.0 | +— / -d381c462-a17f-4192-b694-66a7c3aaee4f |
| Jogador 4 | 4-7 | 260 | BUY | ALL_IN | 14.0 | 7 | 78 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2544110417366028 | 0.0 | 0.0 | +9af900db-c181-448a-9736-30f08f062a00 / -— |
| Jogador 4 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 14.0 | 7 | 86 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22425471246242523 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 14.0 | 7 | 86 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17509324848651886 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 264 | SELL | ALL_IN | 14.0 | 7 | 86 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -9af900db-c181-448a-9736-30f08f062a00 |
| Jogador 4 | 5-1 | 265 | BUY | ALL_IN | 14.0 | 7 | 89 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0512499809265137 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -18d25cfb-d559-4efa-b708-c9987987590b,d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 |
| Jogador 4 | 5-1 | 266 | MOVE_BENCH | ALL_IN | 14.0 | 7 | 86 | 5 | 26.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4756874740123749 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 267 | BUY | ALL_IN | 14.0 | 7 | 86 | 5 | 34.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22954502701759338 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -— |
| Jogador 4 | 5-1 | 268 | BUY | ALL_IN | 14.0 | 7 | 83 | 5 | 34.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24552232027053833 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -— |
| Jogador 4 | 5-1 | 269 | REROLL | ALL_IN | 14.0 | 7 | 80 | 5 | 34.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 270 | SELL | ALL_IN | 14.0 | 7 | 78 | 5 | 34.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7111999988555908 | 0.0 | 0.0 | +— / -4688e6f1-26c5-402d-8d27-0f9bce3a9681 |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.26577791571617126 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.24549612402915955 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12370830029249191 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11255644261837006 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17292346060276031 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012102286331355572 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4293290078639984 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2171582281589508 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3304295241832733 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 40 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28900668025016785 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 41 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0326523780822754 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19876615703105927 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2127651423215866 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4089089035987854 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2262270599603653 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 57 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9720555543899536 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 64 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0441662073135376 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12276236712932587 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 75 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2461235672235489 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4363267421722412 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 77 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16280490159988403 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03177344799041748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 79 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.258012056350708 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 80 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3106880486011505 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21872754395008087 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05810000002384186 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 85 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08817197382450104 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-4 | 86 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1673070639371872 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07833333313465118 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09790968894958496 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-4 | 89 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 90 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29024648666381836 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33943381905555725 | 0.0 | 0.0 | +2e4ab22c-62d7-425c-9528-2e1315655c24 / -— |
| Jogador 5 | 2-5 | 94 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06970000267028809 | 0.0 | 0.0 | +— / -486e92ad-4dcf-4c0e-a470-e0b87777d380 |
| Jogador 5 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1223333328962326 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 5 | 2-5 | 96 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3170259892940521 | 0.0 | 0.0 | +28f66ef1-93d6-4cc8-a0c9-e84e844dee28 / -— |
| Jogador 5 | 2-5 | 97 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 98 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3515999913215637 | 0.0 | 0.0 | +— / -28f66ef1-93d6-4cc8-a0c9-e84e844dee28 |
| Jogador 5 | 2-5 | 99 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3971157968044281 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36481964588165283 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09186519682407379 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06104522570967674 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 105 | BUY | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05930067226290703 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 106 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08731768280267715 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-6 | 107 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06522078812122345 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 108 | SELL | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43148890137672424 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-6 | 109 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005137316416949034 | 0.0 | 0.0 | +53312511-4e10-4904-82c0-8a8e69c039cd / -— |
| Jogador 5 | 2-6 | 110 | BUY | STABILIZE | 95.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0050762249156832695 | 0.0 | 0.0 | +b6a21130-c9dc-45ad-8ddb-9223b0ec8751 / -— |
| Jogador 5 | 2-7 | 112 | BUY | STABILIZE | 90.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34532737731933594 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 113 | BUY | STABILIZE | 90.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9630588889122009 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 114 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20998093485832214 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -— |
| Jogador 5 | 2-7 | 115 | SELL | STABILIZE | 90.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034699998795986176 | 0.0 | 0.0 | +— / -53312511-4e10-4904-82c0-8a8e69c039cd |
| Jogador 5 | 2-7 | 116 | SELL | STABILIZE | 90.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03592974692583084 | 0.0 | 0.0 | +— / -b6a21130-c9dc-45ad-8ddb-9223b0ec8751 |
| Jogador 5 | 2-7 | 117 | BUY | STABILIZE | 90.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10740545392036438 | 0.0 | 0.0 | +6eee9a92-4235-46af-ae42-c38acd6847ef / -— |
| Jogador 5 | 2-7 | 118 | SELL | STABILIZE | 90.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41966667771339417 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 2-7 | 119 | SELL | STABILIZE | 90.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37566667795181274 | 0.0 | 0.0 | +— / -6eee9a92-4235-46af-ae42-c38acd6847ef |
| Jogador 5 | 2-7 | 120 | BUY | STABILIZE | 90.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00808158703148365 | 0.0 | 0.0 | +c5593e47-f48a-4362-b230-dfa3d7d36ec9 / -— |
| Jogador 5 | 3-1 | 122 | BUY | STABILIZE | 90.0 | 6 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7501031756401062 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -46838f8d-8037-485c-8c34-9639f14ada19,837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 90.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.190902441740036 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 124 | BUY | STABILIZE | 90.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11416009068489075 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 125 | BUY | STABILIZE | 90.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028782688081264496 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 5 | 3-1 | 126 | SELL | STABILIZE | 90.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-1 | 127 | BUY | STABILIZE | 90.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2711927890777588 | 0.0 | 0.0 | +79ed9815-7667-4e50-86a3-420599ce8c79 / -— |
| Jogador 5 | 3-1 | 128 | SELL | STABILIZE | 90.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -c5593e47-f48a-4362-b230-dfa3d7d36ec9 |
| Jogador 5 | 3-1 | 129 | SELL | STABILIZE | 90.0 | 6 | 8 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2409999966621399 | 0.0 | 0.0 | +— / -79ed9815-7667-4e50-86a3-420599ce8c79 |
| Jogador 5 | 3-1 | 130 | BUY | STABILIZE | 90.0 | 6 | 10 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35375088453292847 | 0.0 | 0.0 | +f7526b6b-8c94-4229-bd3f-1e538c769fec / -— |
| Jogador 5 | 3-2 | 132 | BUY | STABILIZE | 90.0 | 6 | 16 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6885117888450623 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 133 | BUY | STABILIZE | 90.0 | 6 | 13 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27089130878448486 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -— |
| Jogador 5 | 3-2 | 134 | SELL | STABILIZE | 90.0 | 6 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -f7526b6b-8c94-4229-bd3f-1e538c769fec |
| Jogador 5 | 3-2 | 135 | SELL | STABILIZE | 90.0 | 6 | 12 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09637503325939178 | 0.0 | 0.0 | +— / -a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 |
| Jogador 5 | 3-2 | 136 | SELL | STABILIZE | 90.0 | 6 | 14 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5380130410194397 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-2 | 137 | BUY | STABILIZE | 90.0 | 6 | 17 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23666338622570038 | 0.0 | 0.0 | +35a674f6-a230-480b-a93f-f7ec76d78658 / -— |
| Jogador 5 | 3-2 | 138 | SELL | STABILIZE | 90.0 | 6 | 15 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3356666564941406 | 0.0 | 0.0 | +— / -35a674f6-a230-480b-a93f-f7ec76d78658 |
| Jogador 5 | 3-2 | 139 | BUY | STABILIZE | 90.0 | 6 | 17 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27131813764572144 | 0.0 | 0.0 | +d218597b-b641-4a4c-867a-41227b83fcff / -— |
| Jogador 5 | 3-2 | 140 | SELL | STABILIZE | 90.0 | 6 | 15 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32100000977516174 | 0.0 | 0.0 | +— / -d218597b-b641-4a4c-867a-41227b83fcff |
| Jogador 5 | 3-3 | 142 | BUY | STABILIZE | 81.0 | 6 | 23 | 2 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8105481266975403 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -— |
| Jogador 5 | 3-3 | 143 | BUY | STABILIZE | 81.0 | 6 | 21 | 2 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2107120305299759 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 144 | BUY | STABILIZE | 81.0 | 6 | 17 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2809866666793823 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 145 | SELL | STABILIZE | 81.0 | 6 | 14 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09771686047315598 | 0.0 | 0.0 | +— / -e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 3-3 | 146 | SELL | STABILIZE | 81.0 | 6 | 17 | 1 | 16.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09300000220537186 | 0.0 | 0.0 | +— / -8a4d0946-b80f-4fbb-ab7c-d43c2697c34e |
| Jogador 5 | 3-3 | 147 | BUY | STABILIZE | 81.0 | 6 | 21 | 2 | 16.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036542944610118866 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-3 | 148 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 18 | 1 | 16.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014042627066373825 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 149 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 18 | 1 | 14.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40409326553344727 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 150 | PASS | STABILIZE | 81.0 | 6 | 18 | 1 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057500001043081284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 152 | BUY | STABILIZE | 69.0 | 6 | 25 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8257275819778442 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 5 | 3-4 | 153 | BUY | STABILIZE | 69.0 | 6 | 24 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5212894082069397 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -— |
| Jogador 5 | 3-4 | 154 | SELL | STABILIZE | 69.0 | 6 | 23 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05374174192547798 | 0.0 | 0.0 | +— / -a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 5 | 3-4 | 155 | BUY | STABILIZE | 69.0 | 6 | 26 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02253960259258747 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 156 | SELL | STABILIZE | 69.0 | 6 | 24 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3615274727344513 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 3-4 | 157 | BUY | STABILIZE | 69.0 | 6 | 26 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2549080550670624 | 0.0 | 0.0 | +46fc5f36-cf3e-422e-89f3-9501ec9d7d12 / -— |
| Jogador 5 | 3-4 | 158 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 24 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025188252329826355 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 159 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 24 | 2 | 16.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03190363943576813 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 160 | SELL | STABILIZE | 69.0 | 6 | 24 | 2 | 14.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34149613976478577 | 0.0 | 0.0 | +— / -46fc5f36-cf3e-422e-89f3-9501ec9d7d12 |
| Jogador 5 | 3-5 | 162 | BUY | STABILIZE | 69.0 | 6 | 34 | 3 | 14.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8287336826324463 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -02c39b42-90d5-4e01-9380-460b6c1cb993,eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 3-5 | 163 | BUY | STABILIZE | 69.0 | 6 | 33 | 3 | 12.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10566095262765884 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-5 | 164 | SELL | STABILIZE | 69.0 | 6 | 30 | 3 | 12.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6195003986358643 | 0.0 | 0.0 | +— / -ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 3-5 | 165 | BUY | STABILIZE | 69.0 | 6 | 33 | 3 | 12.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030352018773555756 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 30 | 3 | 12.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2482115924358368 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 167 | BUY | STABILIZE | 69.0 | 6 | 30 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26965585350990295 | 0.0 | 0.0 | +6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 / -— |
| Jogador 5 | 3-5 | 168 | BUY | STABILIZE | 69.0 | 6 | 29 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2766876816749573 | 0.0 | 0.0 | +c3a766c4-2db6-4b3f-88e9-a855fef1e6f6 / -— |
| Jogador 5 | 3-5 | 169 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 27 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 170 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 27 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12459477037191391 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 172 | SELL | STABILIZE | 57.0 | 6 | 35 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0018333332845941186 | 0.0 | 0.0 | +— / -6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 |
| Jogador 5 | 3-6 | 173 | BUY | STABILIZE | 57.0 | 6 | 36 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8302032947540283 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 5 | 3-6 | 174 | SELL | STABILIZE | 57.0 | 6 | 35 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -c3a766c4-2db6-4b3f-88e9-a855fef1e6f6 |
| Jogador 5 | 3-6 | 175 | BUY | STABILIZE | 57.0 | 6 | 37 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2542777955532074 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-6 | 176 | SELL | STABILIZE | 57.0 | 6 | 35 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004410458728671074 | 0.0 | 0.0 | +— / -9bbd1da9-6a26-472c-912e-165ea4031b90 |
| Jogador 5 | 3-6 | 177 | BUY | STABILIZE | 57.0 | 6 | 38 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08281192183494568 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -— |
| Jogador 5 | 3-6 | 178 | SELL | STABILIZE | 57.0 | 6 | 37 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038233332335948944 | 0.0 | 0.0 | +— / -bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 |
| Jogador 5 | 3-6 | 179 | BUY | STABILIZE | 57.0 | 6 | 38 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01618153601884842 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-6 | 180 | SELL | STABILIZE | 57.0 | 6 | 36 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023282840847969055 | 0.0 | 0.0 | +— / -750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 5 | 3-7 | 182 | BUY | STABILIZE | 57.0 | 6 | 47 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8297297358512878 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -— |
| Jogador 5 | 3-7 | 183 | SELL | STABILIZE | 57.0 | 6 | 45 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47653263807296753 | 0.0 | 0.0 | +— / -ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 3-7 | 184 | BUY | STABILIZE | 57.0 | 6 | 46 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02153662033379078 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 185 | SELL | STABILIZE | 57.0 | 6 | 43 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022099999710917473 | 0.0 | 0.0 | +— / -8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 |
| Jogador 5 | 3-7 | 186 | BUY | STABILIZE | 57.0 | 6 | 46 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22025446593761444 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 5 | 3-7 | 187 | SELL | STABILIZE | 57.0 | 6 | 43 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 5 | 3-7 | 188 | BUY | STABILIZE | 57.0 | 6 | 46 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04335850104689598 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 189 | SELL | STABILIZE | 57.0 | 6 | 44 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008933333680033684 | 0.0 | 0.0 | +— / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 5 | 3-7 | 190 | SELL | STABILIZE | 57.0 | 6 | 46 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43148890137672424 | 0.0 | 0.0 | +— / -1457cd1e-c240-4ce5-9217-a91bddfc8807 |
| Jogador 5 | 4-1 | 192 | BUY | STABILIZE | 57.0 | 6 | 57 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.961811363697052 | 0.0 | 0.0 | +0c07379e-5dd1-42e9-aa7a-a764f949deee / -135065df-1ebc-413d-86f1-4df28bd3ee41,691cde76-cf1b-4a60-b818-65f790e312ec |
| Jogador 5 | 4-1 | 193 | BUY | STABILIZE | 57.0 | 6 | 55 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.39914071559906006 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 57.0 | 6 | 52 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13963034749031067 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 195 | CRAFT_AND_EQUIP | STABILIZE | 57.0 | 6 | 52 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16698326170444489 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 196 | BUY | STABILIZE | 57.0 | 6 | 52 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12279527634382248 | 0.0 | 0.0 | +f6de9b7d-1373-459e-b34a-7b878d1a1268 / -— |
| Jogador 5 | 4-1 | 197 | BUY | STABILIZE | 57.0 | 6 | 51 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29693999886512756 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 5 | 4-1 | 198 | SELL | STABILIZE | 57.0 | 6 | 48 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5098999738693237 | 0.0 | 0.0 | +— / -0c07379e-5dd1-42e9-aa7a-a764f949deee |
| Jogador 5 | 4-1 | 199 | SELL | STABILIZE | 57.0 | 6 | 53 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4062469005584717 | 0.0 | 0.0 | +— / -f6de9b7d-1373-459e-b34a-7b878d1a1268 |
| Jogador 5 | 4-1 | 200 | BUY | STABILIZE | 57.0 | 6 | 54 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24341624975204468 | 0.0 | 0.0 | +6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 / -— |
| Jogador 5 | 4-2 | 202 | BUY | STABILIZE | 44.0 | 6 | 63 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15007029473781586 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 5 | 4-2 | 203 | SELL | STABILIZE | 44.0 | 6 | 59 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01133333332836628 | 0.0 | 0.0 | +— / -6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 |
| Jogador 5 | 4-2 | 204 | BUY | STABILIZE | 44.0 | 6 | 60 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12162931263446808 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 5 | 4-2 | 205 | SELL | STABILIZE | 44.0 | 6 | 59 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033206090331077576 | 0.0 | 0.0 | +— / -9593a62e-442f-410a-8a0c-7d781e2487cc |
| Jogador 5 | 4-2 | 206 | BUY | STABILIZE | 44.0 | 6 | 60 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23654714226722717 | 0.0 | 0.0 | +02c8aff1-803e-42bc-b7c2-f7cd6d986b4f / -— |
| Jogador 5 | 4-2 | 207 | SELL | STABILIZE | 44.0 | 6 | 58 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 |
| Jogador 5 | 4-2 | 208 | BUY | STABILIZE | 44.0 | 6 | 61 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.719045877456665 | 0.0 | 0.0 | +dde5ed69-0fc4-4d15-b12c-a5252a239040 / -— |
| Jogador 5 | 4-2 | 209 | SELL | STABILIZE | 44.0 | 6 | 59 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.475163996219635 | 0.0 | 0.0 | +— / -4d8c374c-264c-47d9-8cfc-78cbf64ceda0 |
| Jogador 5 | 4-2 | 210 | BUY | STABILIZE | 44.0 | 6 | 61 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9215076565742493 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -02c8aff1-803e-42bc-b7c2-f7cd6d986b4f,dde5ed69-0fc4-4d15-b12c-a5252a239040 |
| Jogador 5 | 4-3 | 212 | BUY | STABILIZE | 32.0 | 6 | 70 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8884167075157166 | 0.0 | 0.0 | +72c247af-bdc3-410c-98dd-dd72b56f2818 / -— |
| Jogador 5 | 4-3 | 213 | BUY | STABILIZE | 32.0 | 6 | 67 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32039856910705566 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -— |
| Jogador 5 | 4-3 | 214 | SELL | STABILIZE | 32.0 | 6 | 65 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5160999894142151 | 0.0 | 0.0 | +— / -fff5cc22-5f1a-47a4-93e3-9772177b0910 |
| Jogador 5 | 4-3 | 215 | BUY | STABILIZE | 32.0 | 6 | 70 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12309960275888443 | 0.0 | 0.0 | +333b0a0b-8868-40b2-96e9-71e468c5dd1f / -— |
| Jogador 5 | 4-3 | 216 | SELL | STABILIZE | 32.0 | 6 | 69 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033238694071769714 | 0.0 | 0.0 | +— / -333b0a0b-8868-40b2-96e9-71e468c5dd1f |
| Jogador 5 | 4-3 | 217 | BUY | STABILIZE | 32.0 | 6 | 70 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02591162919998169 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 5 | 4-3 | 218 | MOVE_BENCH | STABILIZE | 32.0 | 6 | 67 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06945070624351501 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 219 | SELL | STABILIZE | 32.0 | 6 | 67 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00426666671410203 | 0.0 | 0.0 | +— / -27a4bd22-9c1f-4f9f-9192-06ea4933feb5 |
| Jogador 5 | 4-3 | 220 | REROLL | STABILIZE | 32.0 | 6 | 70 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 222 | BUY | ALL_IN | 19.0 | 6 | 79 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6366511583328247 | 0.0 | 0.0 | +8995f621-b355-44ec-816e-797184bdc266 / -— |
| Jogador 5 | 4-4 | 223 | SELL | ALL_IN | 19.0 | 6 | 78 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042399998754262924 | 0.0 | 0.0 | +— / -d9fdb961-a3e3-4e39-9970-e46ffd59fc3b |
| Jogador 5 | 4-4 | 224 | BUY | ALL_IN | 19.0 | 6 | 82 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.189165398478508 | 0.0 | 0.0 | +bae633d7-8337-461a-9a84-9c9758392bb6 / -— |
| Jogador 5 | 4-4 | 225 | SELL | ALL_IN | 19.0 | 6 | 81 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -bae633d7-8337-461a-9a84-9c9758392bb6 |
| Jogador 5 | 4-4 | 226 | BUY | ALL_IN | 19.0 | 6 | 82 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2684903144836426 | 0.0 | 0.0 | +cc9b5fff-2223-4721-a8b2-4f70e196b851 / -— |
| Jogador 5 | 4-4 | 227 | REROLL | ALL_IN | 19.0 | 6 | 80 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 228 | SELL | ALL_IN | 19.0 | 6 | 78 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -cc9b5fff-2223-4721-a8b2-4f70e196b851 |
| Jogador 5 | 4-4 | 229 | BUY | ALL_IN | 19.0 | 6 | 80 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8066591024398804 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 5 | 4-4 | 230 | SELL | ALL_IN | 19.0 | 6 | 77 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5727666616439819 | 0.0 | 0.0 | +— / -8995f621-b355-44ec-816e-797184bdc266 |
| Jogador 5 | 4-5 | 232 | BUY | ALL_IN | 19.0 | 6 | 89 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15214289724826813 | 0.0 | 0.0 | +9717d30c-f073-470c-a6ce-7db8257de559 / -— |
| Jogador 5 | 4-5 | 233 | SELL | ALL_IN | 19.0 | 6 | 88 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03325957432389259 | 0.0 | 0.0 | +— / -9717d30c-f073-470c-a6ce-7db8257de559 |
| Jogador 5 | 4-5 | 234 | BUY | ALL_IN | 19.0 | 6 | 89 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22226370871067047 | 0.0 | 0.0 | +0f5471bd-1451-4979-adc9-aced6bb63610 / -— |
| Jogador 5 | 4-5 | 235 | SELL | ALL_IN | 19.0 | 6 | 85 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -0f5471bd-1451-4979-adc9-aced6bb63610 |
| Jogador 5 | 4-5 | 236 | BUY | ALL_IN | 19.0 | 6 | 89 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23732902109622955 | 0.0 | 0.0 | +fe12befc-b473-4f91-9e51-558a03efa3ad / -— |
| Jogador 5 | 4-5 | 237 | REROLL | ALL_IN | 19.0 | 6 | 87 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 238 | SELL | ALL_IN | 19.0 | 6 | 85 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -fe12befc-b473-4f91-9e51-558a03efa3ad |
| Jogador 5 | 4-5 | 239 | BUY | ALL_IN | 19.0 | 6 | 87 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9819838404655457 | 0.0 | 0.0 | +7e0d7932-1b83-4918-9292-6e60957e6022 / -— |
| Jogador 5 | 4-5 | 240 | SELL | ALL_IN | 19.0 | 6 | 86 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41544443368911743 | 0.0 | 0.0 | +— / -d8ecc66e-097d-4caa-a657-90fcd1286c2b |
| Jogador 5 | 4-6 | 242 | BUY | ALL_IN | 8.0 | 6 | 99 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9806833267211914 | 0.0 | 0.0 | +d1bc6c5b-74a5-46db-b00f-e91265546f5d / -— |
| Jogador 5 | 4-6 | 243 | SELL | ALL_IN | 8.0 | 6 | 96 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1088999509811401 | 0.0 | 0.0 | +— / -2e4ab22c-62d7-425c-9528-2e1315655c24 |
| Jogador 5 | 4-6 | 244 | BUY | ALL_IN | 8.0 | 6 | 97 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0755349397659302 | 0.0 | 0.0 | +d366508d-f33b-485a-8ff3-e5d0a248ae3e / -7e0d7932-1b83-4918-9292-6e60957e6022,9c678a7f-3209-4d1b-addd-385f7d4b89fa |
| Jogador 5 | 4-6 | 245 | BUY | ALL_IN | 8.0 | 6 | 96 | 5 | 16.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5135740637779236 | 0.0 | 0.0 | +f8a93323-530e-4f9c-99d7-a5ec83b78992 / -— |
| Jogador 5 | 4-6 | 246 | MOVE_BENCH | ALL_IN | 8.0 | 6 | 95 | 5 | 16.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5590391159057617 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 247 | BUY | ALL_IN | 8.0 | 6 | 95 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17624826729297638 | 0.0 | 0.0 | +68301141-c9f1-4303-9775-753520772836 / -— |
| Jogador 5 | 4-6 | 248 | SELL | ALL_IN | 8.0 | 6 | 94 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7214999794960022 | 0.0 | 0.0 | +— / -d366508d-f33b-485a-8ff3-e5d0a248ae3e |
| Jogador 5 | 4-6 | 249 | BUY | ALL_IN | 8.0 | 6 | 97 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26979267597198486 | 0.0 | 0.0 | +b9b38183-663e-43a4-9f9d-02f1bd4d2d24 / -— |
| Jogador 5 | 4-6 | 250 | REROLL | ALL_IN | 8.0 | 6 | 95 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | -0.15334774553775787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Sentry | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17399217188358307 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2196885347366333 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0373011827468872 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039901405572891235 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012773334980010986 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011599136516451836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5747041702270508 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0245673656463623 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 40 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 52 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12828443944454193 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15200024843215942 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 54 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29008981585502625 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 55 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 56 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2643762528896332 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 63 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24777653813362122 | 0.0 | 0.0 | +048e9074-b134-49ed-a105-88dca63d1aa3 / -— |
| Jogador 6 | 2-2 | 64 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -6a01f661-884f-4c25-9dbe-384a6fe3a5e6 |
| Jogador 6 | 2-2 | 65 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07944674044847488 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 66 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 72 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28945407271385193 | 0.0 | 0.0 | +b1ecd1fa-793c-40ad-a9e3-9d35d5030339 / -— |
| Jogador 6 | 2-3 | 73 | BUY | STABILIZE | 89.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1797129511833191 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 74 | BUY | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2379678636789322 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 75 | SELL | STABILIZE | 89.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14519049227237701 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-3 | 76 | SELL | STABILIZE | 89.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1519312858581543 | 0.0 | 0.0 | +— / -b1ecd1fa-793c-40ad-a9e3-9d35d5030339 |
| Jogador 6 | 2-3 | 77 | PASS | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 82 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18286050856113434 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 83 | BUY | STABILIZE | 83.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24070146679878235 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 84 | BUY | STABILIZE | 83.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8070191144943237 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 85 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 86 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013266666792333126 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-4 | 87 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10965890437364578 | 0.0 | 0.0 | +— / -048e9074-b134-49ed-a105-88dca63d1aa3 |
| Jogador 6 | 2-4 | 88 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 89 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14377303421497345 | 0.0 | 0.0 | +— / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 |
| Jogador 6 | 2-4 | 90 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1437721997499466 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-5 | 92 | BUY | STABILIZE | 83.0 | 5 | 10 | 1 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8596822023391724 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 93 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28843051195144653 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 94 | BUY_XP | STABILIZE | 83.0 | 5 | 7 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 95 | SELL | STABILIZE | 83.0 | 5 | 3 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45227429270744324 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-5 | 96 | BUY_XP | STABILIZE | 83.0 | 5 | 5 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 97 | SELL | STABILIZE | 83.0 | 5 | 1 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49317389726638794 | 0.0 | 0.0 | +— / -a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 2-5 | 98 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 99 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 0 | 0 | 8.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21166107058525085 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 100 | SELL | STABILIZE | 83.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-6 | 102 | BUY | STABILIZE | 78.0 | 6 | 9 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3203580975532532 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 103 | BUY_XP | STABILIZE | 78.0 | 6 | 6 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 104 | SELL | STABILIZE | 78.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18617047369480133 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 2-6 | 105 | BUY_XP | STABILIZE | 78.0 | 6 | 5 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006841098889708519 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 107 | SELL | STABILIZE | 78.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-6 | 108 | BUY | STABILIZE | 78.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15727946162223816 | 0.0 | 0.0 | +2a7dd07f-3b48-489c-8822-9ec2434a01cf / -— |
| Jogador 6 | 2-6 | 109 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6007081270217896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 0 | 0 | 12.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020107917487621307 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 112 | BUY | STABILIZE | 73.0 | 6 | 7 | 0 | 12.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3116063177585602 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 113 | BUY | STABILIZE | 73.0 | 6 | 4 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3593784272670746 | 0.0 | 0.0 | +dc83202b-476c-4438-90aa-a615b764b7e4 / -— |
| Jogador 6 | 2-7 | 114 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 3 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11269524693489075 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 115 | SELL | STABILIZE | 73.0 | 6 | 3 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05471719801425934 | 0.0 | 0.0 | +— / -2a7dd07f-3b48-489c-8822-9ec2434a01cf |
| Jogador 6 | 2-7 | 116 | SELL | STABILIZE | 73.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16103507578372955 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 2-7 | 117 | BUY | STABILIZE | 73.0 | 6 | 8 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12512731552124023 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 2-7 | 118 | BUY_XP | STABILIZE | 73.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 1 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 1 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05214992165565491 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 122 | BUY | STABILIZE | 73.0 | 6 | 8 | 0 | 12.0 | Feérico/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2603727877140045 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 73.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1875360906124115 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 124 | BUY | STABILIZE | 73.0 | 6 | 5 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0960426777601242 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 1 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17545253038406372 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 126 | SELL | STABILIZE | 73.0 | 6 | 1 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09626878798007965 | 0.0 | 0.0 | +— / -9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 3-1 | 127 | BUY_XP | STABILIZE | 73.0 | 6 | 4 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 128 | SELL | STABILIZE | 73.0 | 6 | 0 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05166666582226753 | 0.0 | 0.0 | +— / -4eedd873-e4ec-41e5-9f5e-48e443e80f86 |
| Jogador 6 | 3-1 | 129 | BUY_XP | STABILIZE | 73.0 | 6 | 4 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 130 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 0 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06224236264824867 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 132 | BUY | STABILIZE | 73.0 | 6 | 6 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379753828048706 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -18934be2-4988-4f62-9f62-07ba151231f2,53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 3-2 | 133 | BUY | STABILIZE | 73.0 | 6 | 5 | 0 | 14.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8159373998641968 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 4 | 0 | 10.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16408124566078186 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 135 | BUY | STABILIZE | 73.0 | 6 | 4 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030394606292247772 | 0.0 | 0.0 | +4278eb73-acda-419d-bf9e-53a29ff6900d / -— |
| Jogador 6 | 3-2 | 136 | SELL | STABILIZE | 73.0 | 6 | 3 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41608887910842896 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 3-2 | 137 | EQUIP_FROM_INVENTORY | STABILIZE | 73.0 | 6 | 6 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15578892827033997 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 138 | EQUIP_FROM_INVENTORY | STABILIZE | 73.0 | 6 | 6 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.18792887032032013 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 139 | EQUIP_FROM_INVENTORY | STABILIZE | 73.0 | 6 | 6 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14461596310138702 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 140 | BUY_XP | STABILIZE | 73.0 | 6 | 6 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 142 | BUY | STABILIZE | 64.0 | 7 | 7 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7998296618461609 | 0.0 | 0.0 | +31c30451-3999-47b1-8bcf-77e137137b2a / -— |
| Jogador 6 | 3-3 | 143 | BUY | STABILIZE | 64.0 | 7 | 4 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2789018154144287 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 144 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 1 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6458050608634949 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 145 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 1 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.783056378364563 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 146 | PASS | STABILIZE | 64.0 | 7 | 1 | 0 | 8.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 152 | BUY | STABILIZE | 54.0 | 7 | 7 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2619107663631439 | 0.0 | 0.0 | +2ed895f2-1e83-426c-88fc-b9fb6403835d / -— |
| Jogador 6 | 3-4 | 153 | MOVE_BENCH | STABILIZE | 54.0 | 7 | 3 | 0 | 12.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11909588426351547 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 54.0 | 7 | 3 | 0 | 16.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13768821954727173 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 155 | BUY | STABILIZE | 54.0 | 7 | 3 | 0 | 22.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022509735077619553 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 6 | 3-4 | 156 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 0 | 0 | 22.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 0 | 0 | 22.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0184048879891634 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 158 | PASS | STABILIZE | 54.0 | 7 | 0 | 0 | 22.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 162 | BUY | STABILIZE | 54.0 | 7 | 6 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5395960211753845 | 0.0 | 0.0 | +5b95b64a-b46a-4827-8613-307c8dadc072 / -— |
| Jogador 6 | 3-5 | 163 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 3 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004180470947176218 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 164 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 3 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 3 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013265577144920826 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 166 | PASS | STABILIZE | 54.0 | 7 | 3 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 172 | BUY | STABILIZE | 54.0 | 7 | 9 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8333377838134766 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -31c30451-3999-47b1-8bcf-77e137137b2a,a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 |
| Jogador 6 | 3-6 | 173 | BUY | STABILIZE | 54.0 | 7 | 6 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8228267431259155 | 0.0 | 0.0 | +ab472080-6e4b-4b75-b37d-cf10da9a5a0d / -333cdd27-0114-4d36-8ffa-e79b0f43b8e8,5b95b64a-b46a-4827-8613-307c8dadc072 |
| Jogador 6 | 3-6 | 174 | BUY | STABILIZE | 54.0 | 7 | 3 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1119227483868599 | 0.0 | 0.0 | +604cc5dc-6c20-4d5a-b3a7-8862adfe1930 / -— |
| Jogador 6 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 0 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011332052759826183 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 0 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015492071397602558 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 0 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04706452414393425 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 0 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001173888798803091 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 179 | PASS | STABILIZE | 54.0 | 7 | 0 | 0 | 24.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 182 | BUY | STABILIZE | 54.0 | 7 | 7 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6560235619544983 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 6 | 3-7 | 183 | BUY | STABILIZE | 54.0 | 7 | 3 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06021269038319588 | 0.0 | 0.0 | +604a85af-ff68-41a7-8795-73fdc7723c0e / -— |
| Jogador 6 | 3-7 | 184 | BUY | STABILIZE | 54.0 | 7 | 1 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2861500382423401 | 0.0 | 0.0 | +3a40e3a6-b3e3-4f35-8fa0-e81c89d72db6 / -— |
| Jogador 6 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 0 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 0 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02859533578157425 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 187 | PASS | STABILIZE | 54.0 | 7 | 0 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 192 | BUY | STABILIZE | 54.0 | 7 | 6 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.17149734497070312 | 0.0 | 0.0 | +a8a8381a-f3a8-45ec-9106-293d73fca0c8 / -— |
| Jogador 6 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 54.0 | 7 | 3 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.205855131149292 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 54.0 | 7 | 3 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15899713337421417 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 195 | BUY | STABILIZE | 54.0 | 7 | 3 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06117289140820503 | 0.0 | 0.0 | +45d53a67-4ed4-495d-8751-5ea0f72f91e9 / -— |
| Jogador 6 | 4-1 | 196 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 1 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10121149569749832 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 197 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 1 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 1 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 199 | PASS | STABILIZE | 54.0 | 7 | 1 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 202 | SELL | STABILIZE | 54.0 | 7 | 8 | 0 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -ab472080-6e4b-4b75-b37d-cf10da9a5a0d |
| Jogador 6 | 4-2 | 203 | BUY | STABILIZE | 54.0 | 7 | 16 | 1 | 30.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11469417810440063 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 6 | 4-2 | 204 | SELL | STABILIZE | 54.0 | 7 | 12 | 1 | 30.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 4-2 | 205 | BUY | STABILIZE | 54.0 | 7 | 20 | 2 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01274770125746727 | 0.0 | 0.0 | +ef54ddfd-f436-4813-9585-cb652488ffa3 / -— |
| Jogador 6 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 18 | 1 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.839303308770468e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 18 | 1 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014977709390223026 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 18 | 1 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997401274740696 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 209 | PASS | STABILIZE | 54.0 | 7 | 18 | 1 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027142856270074844 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 212 | SELL | STABILIZE | 43.0 | 7 | 24 | 2 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02199999988079071 | 0.0 | 0.0 | +— / -3a40e3a6-b3e3-4f35-8fa0-e81c89d72db6 |
| Jogador 6 | 4-3 | 213 | BUY | STABILIZE | 43.0 | 7 | 25 | 2 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5515926480293274 | 0.0 | 0.0 | +a9588010-57fa-4baf-b226-a30f519342e7 / -— |
| Jogador 6 | 4-3 | 214 | SELL | STABILIZE | 43.0 | 7 | 23 | 2 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008730537258088589 | 0.0 | 0.0 | +— / -dc83202b-476c-4438-90aa-a615b764b7e4 |
| Jogador 6 | 4-3 | 215 | BUY | STABILIZE | 43.0 | 7 | 24 | 2 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24658982455730438 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -— |
| Jogador 6 | 4-3 | 216 | SELL | STABILIZE | 43.0 | 7 | 20 | 2 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -604a85af-ff68-41a7-8795-73fdc7723c0e |
| Jogador 6 | 4-3 | 217 | BUY | STABILIZE | 43.0 | 7 | 22 | 2 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0063643986359238625 | 0.0 | 0.0 | +840740a6-45be-4107-a4b7-b10cefe1a667 / -— |
| Jogador 6 | 4-3 | 218 | SELL | STABILIZE | 43.0 | 7 | 20 | 2 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -840740a6-45be-4107-a4b7-b10cefe1a667 |
| Jogador 6 | 4-3 | 219 | BUY | STABILIZE | 43.0 | 7 | 22 | 2 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.052866775542497635 | 0.0 | 0.0 | +badbffc5-dd49-4cd8-8b4d-941ae020e6e3 / -— |
| Jogador 6 | 4-3 | 220 | MOVE_BOARD | STABILIZE | 43.0 | 7 | 20 | 2 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.558079909766093e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 222 | SELL | STABILIZE | 32.0 | 7 | 28 | 2 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08405357599258423 | 0.0 | 0.0 | +— / -badbffc5-dd49-4cd8-8b4d-941ae020e6e3 |
| Jogador 6 | 4-4 | 223 | BUY | STABILIZE | 32.0 | 7 | 30 | 3 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31388741731643677 | 0.0 | 0.0 | +ddae48a6-5360-4660-9fa1-143ac35635ee / -— |
| Jogador 6 | 4-4 | 224 | SELL | STABILIZE | 32.0 | 7 | 27 | 2 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024602217599749565 | 0.0 | 0.0 | +— / -ef54ddfd-f436-4813-9585-cb652488ffa3 |
| Jogador 6 | 4-4 | 225 | BUY | STABILIZE | 32.0 | 7 | 29 | 2 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2501438856124878 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 6 | 4-4 | 226 | SELL | STABILIZE | 32.0 | 7 | 26 | 2 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -ddae48a6-5360-4660-9fa1-143ac35635ee |
| Jogador 6 | 4-4 | 227 | BUY | STABILIZE | 32.0 | 7 | 29 | 2 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016110921278595924 | 0.0 | 0.0 | +5477420d-3b98-4863-b2e7-f414d3fa1f01 / -— |
| Jogador 6 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 28 | 2 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.274206781294197e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 229 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 28 | 2 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015015781857073307 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 230 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 28 | 2 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015065081417560577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 232 | SELL | STABILIZE | 32.0 | 7 | 36 | 3 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0070333331823349 | 0.0 | 0.0 | +— / -5477420d-3b98-4863-b2e7-f414d3fa1f01 |
| Jogador 6 | 4-5 | 233 | BUY | STABILIZE | 32.0 | 7 | 37 | 3 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009776595048606396 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 6 | 4-5 | 234 | SELL | STABILIZE | 32.0 | 7 | 35 | 3 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -7fb0217d-521c-42b5-995c-81e299b3b934 |
| Jogador 6 | 4-5 | 235 | BUY | STABILIZE | 32.0 | 7 | 37 | 3 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01020246185362339 | 0.0 | 0.0 | +ded275a3-9551-4816-8112-f0a25524412c / -— |
| Jogador 6 | 4-5 | 236 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 36 | 3 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 237 | MOVE_BOARD | STABILIZE | 32.0 | 7 | 36 | 3 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014992908574640751 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 238 | PASS | STABILIZE | 32.0 | 7 | 36 | 3 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06002962961792946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 242 | SELL | STABILIZE | 32.0 | 7 | 45 | 4 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00880112312734127 | 0.0 | 0.0 | +— / -ded275a3-9551-4816-8112-f0a25524412c |
| Jogador 6 | 4-6 | 243 | BUY | STABILIZE | 32.0 | 7 | 46 | 4 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3196195363998413 | 0.0 | 0.0 | +6eecc806-dcf8-47df-bc1d-bc5bc5f07099 / -— |
| Jogador 6 | 4-6 | 244 | SELL | STABILIZE | 32.0 | 7 | 42 | 4 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01254189107567072 | 0.0 | 0.0 | +— / -d175e09c-3ed6-4fb3-8c97-0c167862e29e |
| Jogador 6 | 4-6 | 245 | BUY | STABILIZE | 32.0 | 7 | 45 | 4 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2500656545162201 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 6 | 4-6 | 246 | SELL | STABILIZE | 32.0 | 7 | 42 | 4 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014299999922513962 | 0.0 | 0.0 | +— / -bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 6 | 4-6 | 247 | BUY | STABILIZE | 32.0 | 7 | 45 | 4 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05732518061995506 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -— |
| Jogador 6 | 4-6 | 248 | REROLL | STABILIZE | 32.0 | 7 | 43 | 4 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1340000033378601 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 249 | SELL | STABILIZE | 32.0 | 7 | 41 | 4 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005799999926239252 | 0.0 | 0.0 | +— / -3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 |
| Jogador 6 | 4-6 | 250 | BUY | STABILIZE | 32.0 | 7 | 43 | 4 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8588707447052002 | 0.0 | 0.0 | +80130f72-2d7c-49db-8d6f-4c0a962260e8 / -— |
| Jogador 6 | 4-7 | 252 | SELL | STABILIZE | 32.0 | 7 | 51 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025066666305065155 | 0.0 | 0.0 | +— / -4278eb73-acda-419d-bf9e-53a29ff6900d |
| Jogador 6 | 4-7 | 253 | BUY | STABILIZE | 32.0 | 7 | 52 | 5 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0728551596403122 | 0.0 | 0.0 | +9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 / -— |
| Jogador 6 | 4-7 | 254 | SELL | STABILIZE | 32.0 | 7 | 49 | 4 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06959611177444458 | 0.0 | 0.0 | +— / -03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 |
| Jogador 6 | 4-7 | 255 | BUY | STABILIZE | 32.0 | 7 | 53 | 5 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059667788445949554 | 0.0 | 0.0 | +55cd39c0-65d5-410e-917e-501f584115fa / -— |
| Jogador 6 | 4-7 | 256 | SELL | STABILIZE | 32.0 | 7 | 49 | 4 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06097232922911644 | 0.0 | 0.0 | +— / -55cd39c0-65d5-410e-917e-501f584115fa |
| Jogador 6 | 4-7 | 257 | BUY | STABILIZE | 32.0 | 7 | 53 | 5 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22976775467395782 | 0.0 | 0.0 | +e5f38fbd-826a-4067-a33f-86cf7eb98f30 / -— |
| Jogador 6 | 4-7 | 258 | SELL | STABILIZE | 32.0 | 7 | 50 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -e5f38fbd-826a-4067-a33f-86cf7eb98f30 |
| Jogador 6 | 4-7 | 259 | BUY | STABILIZE | 32.0 | 7 | 53 | 5 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05148301273584366 | 0.0 | 0.0 | +c7a7408a-e7bd-428d-9935-4d5a002d8d9f / -— |
| Jogador 6 | 4-7 | 260 | REROLL | STABILIZE | 32.0 | 7 | 51 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24070000648498535 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 32.0 | 7 | 59 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08325660973787308 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 32.0 | 7 | 59 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08968379348516464 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 264 | SELL | STABILIZE | 32.0 | 7 | 59 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015508285723626614 | 0.0 | 0.0 | +— / -c7a7408a-e7bd-428d-9935-4d5a002d8d9f |
| Jogador 6 | 5-1 | 265 | BUY | STABILIZE | 32.0 | 7 | 61 | 5 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0212916135787964 | 0.0 | 0.0 | +e9bb05f6-3838-423a-bfd2-3791379b479e / -3cb4d077-df9a-4fd2-9a68-7301aff1b657,3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 5-1 | 266 | MOVE_BENCH | STABILIZE | 32.0 | 7 | 60 | 5 | 26.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16881988942623138 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 267 | BUY | STABILIZE | 32.0 | 7 | 60 | 5 | 32.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9151100516319275 | 0.0 | 0.0 | +9a96b07c-5b37-4be7-855e-dc2d942e7171 / -— |
| Jogador 6 | 5-1 | 268 | SELL | STABILIZE | 32.0 | 7 | 57 | 5 | 32.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -e9bb05f6-3838-423a-bfd2-3791379b479e |
| Jogador 6 | 5-1 | 269 | BUY | STABILIZE | 32.0 | 7 | 60 | 5 | 32.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.232732892036438 | 0.0 | 0.0 | +1c5a9322-14c8-4df9-937b-842dcaa1f372 / -— |
| Jogador 6 | 5-1 | 270 | EQUIP_FROM_INVENTORY | STABILIZE | 32.0 | 7 | 57 | 5 | 32.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12162905186414719 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 272 | EQUIP_FROM_INVENTORY | ALL_IN | 16.0 | 7 | 67 | 5 | 32.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1085408478975296 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 273 | EQUIP_FROM_INVENTORY | ALL_IN | 16.0 | 7 | 67 | 5 | 32.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12460542470216751 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 274 | SELL | ALL_IN | 16.0 | 7 | 67 | 5 | 32.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00426666671410203 | 0.0 | 0.0 | +— / -a8a8381a-f3a8-45ec-9106-293d73fca0c8 |
| Jogador 6 | 5-2 | 275 | BUY | ALL_IN | 16.0 | 7 | 70 | 5 | 32.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0443270206451416 | 0.0 | 0.0 | +57ba484a-6228-4263-8171-00a8a5893bea / -2ed895f2-1e83-426c-88fc-b9fb6403835d,665661af-7240-4a65-bf3d-f4ecf3532a85 |
| Jogador 6 | 5-2 | 276 | BUY | ALL_IN | 16.0 | 7 | 66 | 5 | 24.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6794546246528625 | 0.0 | 0.0 | +95eba9e8-10f5-48d5-86de-3d9a446b2e65 / -45d53a67-4ed4-495d-8751-5ea0f72f91e9,a9588010-57fa-4baf-b226-a30f519342e7 |
| Jogador 6 | 5-2 | 277 | MOVE_BENCH | ALL_IN | 16.0 | 7 | 64 | 5 | 24.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23089778423309326 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 278 | BUY | ALL_IN | 16.0 | 7 | 64 | 5 | 30.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028275419026613235 | 0.0 | 0.0 | +7f9f3188-2482-4518-9fd2-34f0ea1527a9 / -— |
| Jogador 6 | 5-2 | 279 | BUY | ALL_IN | 16.0 | 7 | 60 | 5 | 30.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03033512830734253 | 0.0 | 0.0 | +0c96798c-ee23-488b-974f-74e8e3da6aa6 / -— |
| Jogador 6 | 5-2 | 280 | BUY | ALL_IN | 16.0 | 7 | 57 | 5 | 30.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0352703295648098 | 0.0 | 0.0 | +eb418af1-c963-4da2-b052-86a153fc5ba1 / -— |
| Jogador 6 | 5-3 | 282 | SELL | ALL_IN | 2.0 | 7 | 67 | 5 | 30.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03936666622757912 | 0.0 | 0.0 | +— / -95eba9e8-10f5-48d5-86de-3d9a446b2e65 |
| Jogador 6 | 5-3 | 283 | BUY | ALL_IN | 2.0 | 7 | 72 | 5 | 30.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0458744540810585 | 0.0 | 0.0 | +8da82a9e-0746-43e1-81c3-fa22ec3bb863 / -— |
| Jogador 6 | 5-3 | 284 | SELL | ALL_IN | 2.0 | 7 | 70 | 5 | 30.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010333333164453506 | 0.0 | 0.0 | +— / -eb418af1-c963-4da2-b052-86a153fc5ba1 |
| Jogador 6 | 5-3 | 285 | BUY | ALL_IN | 2.0 | 7 | 71 | 5 | 30.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045873984694480896 | 0.0 | 0.0 | +6fb5e8f1-2656-486b-9478-161c1b430d5f / -— |
| Jogador 6 | 5-3 | 286 | SELL | ALL_IN | 2.0 | 7 | 69 | 5 | 30.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7487000226974487 | 0.0 | 0.0 | +— / -57ba484a-6228-4263-8171-00a8a5893bea |
| Jogador 6 | 5-3 | 287 | BUY | ALL_IN | 2.0 | 7 | 80 | 5 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04928618296980858 | 0.0 | 0.0 | +91eb044c-6989-4b6a-a9fa-a59f75b56743 / -— |
| Jogador 6 | 5-3 | 288 | SELL | ALL_IN | 2.0 | 7 | 77 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -8da82a9e-0746-43e1-81c3-fa22ec3bb863 |
| Jogador 6 | 5-3 | 289 | BUY | ALL_IN | 2.0 | 7 | 79 | 5 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2804301083087921 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -— |
| Jogador 6 | 5-3 | 290 | SELL | ALL_IN | 2.0 | 7 | 76 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -6fb5e8f1-2656-486b-9478-161c1b430d5f |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589178562164307 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2799173593521118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.143971249461174 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012334865517914295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40434256196022034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0484532117843628 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23116838932037354 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004352054558694363 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005867671221494675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 30 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0368695259094238 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 40 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24539557099342346 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007539904909208417 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 42 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1995791792869568 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 43 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8280844688415527 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19951866567134857 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2452055960893631 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3010636866092682 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 56 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 62 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.047563910484314 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15446484088897705 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 65 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17882473766803741 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04722195118665695 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 68 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-2 | 69 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.110329769551754 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 70 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15401297807693481 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 72 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475443601608276 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 73 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6454002857208252 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 6 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1713351160287857 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 75 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09766016155481339 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 76 | PASS | STABILIZE | 95.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3059629797935486 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20850159227848053 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.127519890666008 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 87 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016079558059573174 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 88 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32838308811187744 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 93 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043666668236255646 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 7 | 2-5 | 94 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3646250069141388 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 95 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007801025174558163 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 97 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005423958878964186 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 98 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9129713773727417 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 7 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8820824027061462 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 104 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45766666531562805 | 0.0 | 0.0 | +— / -dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 7 | 2-6 | 105 | SELL | STABILIZE | 95.0 | 5 | 4 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04100000113248825 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 2-6 | 106 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6187363266944885 | 0.0 | 0.0 | +— / -caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 7 | 2-6 | 107 | BUY_XP | STABILIZE | 95.0 | 5 | 6 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 108 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6250932812690735 | 0.0 | 0.0 | +— / -599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 7 | 2-6 | 109 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050634998828172684 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 110 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6269999742507935 | 0.0 | 0.0 | +— / -fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 2-7 | 112 | BUY | STABILIZE | 95.0 | 6 | 12 | 1 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3618015646934509 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 113 | BUY | STABILIZE | 95.0 | 6 | 9 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03434183821082115 | 0.0 | 0.0 | +ac02c0c4-a10d-497d-b6c1-d458ad7ae58c / -— |
| Jogador 7 | 2-7 | 114 | BUY_XP | STABILIZE | 95.0 | 6 | 7 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 115 | SELL | STABILIZE | 95.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -ac02c0c4-a10d-497d-b6c1-d458ad7ae58c |
| Jogador 7 | 2-7 | 116 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 117 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 2-7 | 118 | BUY_XP | STABILIZE | 95.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.4217367808887502e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 122 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28448379039764404 | 0.0 | 0.0 | +033a84d9-70f6-46a8-a6eb-a2f03be70400 / -— |
| Jogador 7 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22388724982738495 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 124 | BUY | STABILIZE | 95.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0318019799888134 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 7 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002020705258473754 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012984788976609707 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 127 | PASS | STABILIZE | 95.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 132 | BUY | STABILIZE | 95.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2754090130329132 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -— |
| Jogador 7 | 3-2 | 133 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.668932863045484e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 134 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 135 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.0797838260477874e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0264296792447567 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 138 | PASS | STABILIZE | 95.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 142 | BUY | STABILIZE | 95.0 | 6 | 9 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379747271537781 | 0.0 | 0.0 | +652ff984-c3ac-48d7-9fb6-e95aed0a047d / -242805ca-f275-4e04-a2f5-81e0b6680dd1,7159421f-b5ea-4d10-9cc5-59186d62983d |
| Jogador 7 | 3-3 | 143 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 8 | 0 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16409257054328918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 144 | BUY_XP | STABILIZE | 95.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 145 | BUY_XP | STABILIZE | 95.0 | 6 | 4 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 146 | SELL | STABILIZE | 95.0 | 6 | 0 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -652ff984-c3ac-48d7-9fb6-e95aed0a047d |
| Jogador 7 | 3-3 | 147 | SELL | STABILIZE | 95.0 | 6 | 3 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6309999823570251 | 0.0 | 0.0 | +— / -033a84d9-70f6-46a8-a6eb-a2f03be70400 |
| Jogador 7 | 3-3 | 148 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02827499993145466 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 149 | MOVE_BENCH | STABILIZE | 95.0 | 7 | 1 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21331879496574402 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 95.0 | 7 | 1 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015768513083457947 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 152 | BUY | STABILIZE | 85.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379969596862793 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -4e206e09-40e3-4699-81cb-8aaf01109dea,a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 7 | 3-4 | 153 | BUY | STABILIZE | 85.0 | 7 | 5 | 0 | 28.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8329989910125732 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -2c7e844d-925a-43bb-8be8-65a71d11f964,6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 85.0 | 7 | 2 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2901264727115631 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 155 | BUY | STABILIZE | 85.0 | 7 | 2 | 0 | 34.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013147030957043171 | 0.0 | 0.0 | +94d1da64-f0c8-4fd8-a610-b7e86f10378e / -— |
| Jogador 7 | 3-4 | 156 | MOVE_BOARD | STABILIZE | 85.0 | 7 | 0 | 0 | 34.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0012164446525275707 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 157 | MOVE_BENCH | STABILIZE | 85.0 | 7 | 0 | 0 | 34.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13773459196090698 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 158 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 159 | MOVE_BOARD | FAST8 | 85.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014984424225986004 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 160 | PASS | FAST8 | 85.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 162 | BUY | FAST8 | 85.0 | 7 | 5 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11273466795682907 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 163 | BUY | FAST8 | 85.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10141684114933014 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 7 | 3-5 | 164 | MOVE_BOARD | FAST8 | 85.0 | 7 | 1 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.192668373230845e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 165 | MOVE_BOARD | FAST8 | 85.0 | 7 | 1 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014872988685965538 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 166 | PASS | FAST8 | 85.0 | 7 | 1 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 172 | BUY | FAST8 | 74.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13520340621471405 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 173 | BUY | FAST8 | 74.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13075724244117737 | 0.0 | 0.0 | +69ccc61a-403b-4025-8359-b2061dc6ad10 / -— |
| Jogador 7 | 3-6 | 174 | MOVE_BOARD | FAST8 | 74.0 | 7 | 0 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 175 | MOVE_BOARD | FAST8 | 74.0 | 7 | 0 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014971211552619934 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 176 | PASS | FAST8 | 74.0 | 7 | 0 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 182 | BUY | FAST8 | 74.0 | 7 | 6 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6534867286682129 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 183 | BUY | FAST8 | 74.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20988193154335022 | 0.0 | 0.0 | +21135c93-ae87-47a0-899c-7eaa0c2c30b8 / -— |
| Jogador 7 | 3-7 | 184 | MOVE_BOARD | FAST8 | 74.0 | 7 | 0 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.5622425735273282e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 185 | MOVE_BOARD | FAST8 | 74.0 | 7 | 0 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999831095337868 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 186 | MOVE_BOARD | FAST8 | 74.0 | 7 | 0 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016113940626382828 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 187 | PASS | FAST8 | 74.0 | 7 | 0 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 74.0 | 7 | 5 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.055321309715509415 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 74.0 | 7 | 5 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06955357640981674 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 194 | BUY | FAST8 | 74.0 | 7 | 5 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12288027256727219 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 7 | 4-1 | 195 | MOVE_BOARD | FAST8 | 74.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0011137566762045026 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 196 | MOVE_BOARD | FAST8 | 74.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015004700981080532 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 197 | MOVE_BOARD | FAST8 | 74.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015004504472017288 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 198 | PASS | FAST8 | 74.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 202 | BUY | FAST8 | 74.0 | 7 | 9 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18485991656780243 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -— |
| Jogador 7 | 4-2 | 203 | MOVE_BOARD | FAST8 | 74.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 204 | MOVE_BOARD | FAST8 | 74.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016350924968719482 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 205 | PASS | FAST8 | 74.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 212 | MOVE_BOARD | FAST8 | 74.0 | 7 | 14 | 1 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001355198910459876 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 213 | MOVE_BOARD | FAST8 | 74.0 | 7 | 14 | 1 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014995464123785496 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 214 | MOVE_BOARD | FAST8 | 74.0 | 7 | 14 | 1 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000584535300732 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 215 | PASS | FAST8 | 74.0 | 7 | 14 | 1 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 222 | BUY | FAST8 | 74.0 | 7 | 22 | 2 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.614243745803833 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 7 | 4-4 | 223 | MOVE_BOARD | FAST8 | 74.0 | 7 | 19 | 1 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 224 | MOVE_BOARD | FAST8 | 74.0 | 7 | 19 | 1 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999444596469402 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 225 | PASS | FAST8 | 74.0 | 7 | 19 | 1 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027857143431901932 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 232 | MOVE_BOARD | FAST8 | 74.0 | 7 | 26 | 2 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.042493977365666e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 233 | SELL | FAST8 | 74.0 | 7 | 26 | 2 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04516666755080223 | 0.0 | 0.0 | +— / -42f739bb-e676-4a27-a96f-c09d09d592bb |
| Jogador 7 | 4-5 | 234 | BUY | FAST8 | 74.0 | 7 | 27 | 2 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7519415616989136 | 0.0 | 0.0 | +f3e882b5-333e-44e3-ae82-cacacc8b1137 / -— |
| Jogador 7 | 4-5 | 235 | MOVE_BOARD | FAST8 | 74.0 | 7 | 24 | 2 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.03060004272993e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 236 | MOVE_BOARD | FAST8 | 74.0 | 7 | 24 | 2 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016309212893247604 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 237 | MOVE_BOARD | FAST8 | 74.0 | 7 | 24 | 2 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 238 | PASS | FAST8 | 74.0 | 7 | 24 | 2 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03142857179045677 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 242 | SELL | FAST8 | 74.0 | 7 | 34 | 3 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -69ccc61a-403b-4025-8359-b2061dc6ad10 |
| Jogador 7 | 4-6 | 243 | BUY | FAST8 | 74.0 | 7 | 37 | 3 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27799737453460693 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -— |
| Jogador 7 | 4-6 | 244 | MOVE_BOARD | FAST8 | 74.0 | 7 | 36 | 3 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0012979136081412435 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 245 | MOVE_BOARD | FAST8 | 74.0 | 7 | 36 | 3 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 246 | MOVE_BOARD | FAST8 | 74.0 | 7 | 36 | 3 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01629791408777237 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 247 | PASS | FAST8 | 74.0 | 7 | 36 | 3 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03999999910593033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 252 | SELL | FAST8 | 74.0 | 7 | 48 | 4 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061533331871032715 | 0.0 | 0.0 | +— / -97d52b06-365b-44ad-b4f9-63e0f9503c8a |
| Jogador 7 | 4-7 | 253 | BUY | FAST8 | 74.0 | 7 | 51 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7124413847923279 | 0.0 | 0.0 | +50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de / -— |
| Jogador 7 | 4-7 | 254 | SELL | FAST8 | 74.0 | 7 | 49 | 4 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00016666666488163173 | 0.0 | 0.0 | +— / -f384fea6-9b6f-4f9c-81ec-a8284d5ba140 |
| Jogador 7 | 4-7 | 255 | BUY | FAST8 | 74.0 | 7 | 51 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7899826169013977 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -0cf5c315-d2f3-4854-a95b-07912b83ea81,5b96c8f7-bacb-47df-8666-30d30d49549d |
| Jogador 7 | 4-7 | 256 | MOVE_BENCH | FAST8 | 74.0 | 7 | 48 | 4 | 36.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4769648313522339 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 257 | MOVE_BOARD | FAST8 | 74.0 | 7 | 48 | 4 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016526252031326294 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 258 | MOVE_BOARD | FAST8 | 74.0 | 7 | 48 | 4 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 259 | PASS | FAST8 | 74.0 | 7 | 48 | 4 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18857142329216003 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 262 | BUY | FAST8 | 74.0 | 7 | 60 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.046639952808618546 | 0.0 | 0.0 | +d22aa2b7-7c7c-4d47-89be-0f1b8755971c / -— |
| Jogador 7 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 74.0 | 7 | 57 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.058169085532426834 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 264 | CRAFT_AND_EQUIP | FAST8 | 74.0 | 7 | 57 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13237205147743225 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 265 | BUY | FAST8 | 74.0 | 7 | 57 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26178380846977234 | 0.0 | 0.0 | +4e6b6f57-7f94-46ba-b832-c3198d4a5949 / -— |
| Jogador 7 | 5-1 | 266 | MOVE_BOARD | FAST8 | 74.0 | 7 | 52 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 267 | MOVE_BOARD | FAST8 | 74.0 | 7 | 52 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012130720540881157 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 268 | PASS | FAST8 | 74.0 | 7 | 52 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08911579847335815 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 272 | SELL | FAST8 | 74.0 | 7 | 66 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5394164323806763 | 0.0 | 0.0 | +— / -5a6985d6-5377-425c-b4a3-c53dc138b288 |
| Jogador 7 | 5-2 | 273 | BUY | FAST8 | 74.0 | 7 | 74 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4166088402271271 | 0.0 | 0.0 | +a267d973-f857-4dda-89e1-209bff42ab6f / -— |
| Jogador 7 | 5-2 | 274 | MOVE_BOARD | FAST8 | 74.0 | 7 | 71 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0006058603175915778 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 275 | MOVE_BOARD | FAST8 | 74.0 | 7 | 71 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 276 | PASS | FAST8 | 74.0 | 7 | 71 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10282160341739655 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 282 | SELL | FAST8 | 74.0 | 7 | 85 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 5-3 | 283 | BUY | FAST8 | 74.0 | 7 | 88 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5284470319747925 | 0.0 | 0.0 | +0b38218d-9c50-41ac-b761-115c054bf314 / -— |
| Jogador 7 | 5-3 | 284 | MOVE_BOARD | FAST8 | 74.0 | 7 | 86 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006187866674736142 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 285 | MOVE_BOARD | FAST8 | 74.0 | 7 | 86 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015056274831295013 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 286 | MOVE_BOARD | FAST8 | 74.0 | 7 | 86 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01495665218681097 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 287 | PASS | FAST8 | 74.0 | 7 | 86 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2688155472278595 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 292 | SELL | FAST8 | 74.0 | 7 | 100 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010466666892170906 | 0.0 | 0.0 | +— / -4e6b6f57-7f94-46ba-b832-c3198d4a5949 |
| Jogador 7 | 5-4 | 293 | BUY | FAST8 | 74.0 | 7 | 105 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3516976833343506 | 0.0 | 0.0 | +83a3ef65-b342-4ec8-b2d1-be99c3602f81 / -— |
| Jogador 7 | 5-4 | 294 | MOVE_BOARD | FAST8 | 74.0 | 7 | 102 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.073477389785694e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 295 | MOVE_BOARD | FAST8 | 74.0 | 7 | 102 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014970170333981514 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 296 | MOVE_BOARD | FAST8 | 74.0 | 7 | 102 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015022311359643936 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 297 | PASS | FAST8 | 74.0 | 7 | 102 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12818440794944763 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 302 | SELL | FAST8 | 74.0 | 7 | 115 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -3b934078-806c-40f0-b102-e9131220f70e |
| Jogador 7 | 5-5 | 303 | BUY | FAST8 | 74.0 | 7 | 116 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7579317688941956 | 0.0 | 0.0 | +0a6e3194-ed55-43ad-ac66-31e08ccda7aa / -a267d973-f857-4dda-89e1-209bff42ab6f,d22aa2b7-7c7c-4d47-89be-0f1b8755971c |
| Jogador 7 | 5-5 | 304 | BUY | FAST8 | 74.0 | 7 | 113 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09480125457048416 | 0.0 | 0.0 | +b250e22d-7193-4ea5-879d-5c7b41145719 / -— |
| Jogador 7 | 5-5 | 305 | MOVE_BOARD | FAST8 | 74.0 | 7 | 112 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 306 | MOVE_BOARD | FAST8 | 74.0 | 7 | 112 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 307 | PASS | FAST8 | 74.0 | 7 | 112 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29076236486434937 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 312 | BUY | FAST8 | 74.0 | 7 | 125 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1051681786775589 | 0.0 | 0.0 | +c2bf43be-e6e1-47ed-bcb4-606e37f26671 / -— |
| Jogador 7 | 5-6 | 313 | MOVE_BOARD | FAST8 | 74.0 | 7 | 122 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 314 | MOVE_BOARD | FAST8 | 74.0 | 7 | 122 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000072307884693 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 315 | PASS | FAST8 | 74.0 | 7 | 122 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14548039436340332 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 322 | SELL | FAST8 | 74.0 | 7 | 136 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08356666564941406 | 0.0 | 0.0 | +— / -0a6e3194-ed55-43ad-ac66-31e08ccda7aa |
| Jogador 7 | 5-7 | 323 | BUY | FAST8 | 74.0 | 7 | 144 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2789737284183502 | 0.0 | 0.0 | +c93990ff-0a6f-46bc-8fc1-12623d55abc1 / -— |
| Jogador 7 | 5-7 | 324 | MOVE_BOARD | FAST8 | 74.0 | 7 | 141 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0003797932877205312 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 325 | MOVE_BOARD | FAST8 | 74.0 | 7 | 141 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014615102671086788 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 326 | PASS | FAST8 | 74.0 | 7 | 141 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16237029433250427 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 332 | EQUIP_FROM_INVENTORY | FAST8 | 74.0 | 7 | 154 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13674964010715485 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 333 | SELL | FAST8 | 74.0 | 7 | 154 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.053032517433166504 | 0.0 | 0.0 | +— / -b250e22d-7193-4ea5-879d-5c7b41145719 |
| Jogador 7 | 6-1 | 334 | BUY | FAST8 | 74.0 | 7 | 155 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4378586411476135 | 0.0 | 0.0 | +9af00d66-f862-45b7-98d4-93fbd69fedba / -— |
| Jogador 7 | 6-1 | 335 | MOVE_BOARD | FAST8 | 74.0 | 7 | 152 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.2091993236681446e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 336 | SELL | FAST8 | 74.0 | 7 | 152 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48391202092170715 | 0.0 | 0.0 | +— / -0b38218d-9c50-41ac-b761-115c054bf314 |
| Jogador 7 | 6-1 | 337 | BUY | FAST8 | 74.0 | 7 | 154 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03962520882487297 | 0.0 | 0.0 | +17279599-f3fc-4cf2-874f-da62a23ac238 / -— |
| Jogador 7 | 6-1 | 338 | MOVE_BOARD | FAST8 | 74.0 | 7 | 152 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.698810178320855e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 339 | MOVE_BOARD | FAST8 | 74.0 | 7 | 152 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998231083154678 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 340 | MOVE_BOARD | FAST8 | 74.0 | 7 | 152 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 342 | SELL | FAST8 | 56.0 | 7 | 162 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018008656799793243 | 0.0 | 0.0 | +— / -17279599-f3fc-4cf2-874f-da62a23ac238 |
| Jogador 7 | 6-2 | 343 | BUY | FAST8 | 56.0 | 7 | 164 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8494591116905212 | 0.0 | 0.0 | +3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 / -— |
| Jogador 7 | 6-2 | 344 | SELL | FAST8 | 56.0 | 7 | 161 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45723333954811096 | 0.0 | 0.0 | +— / -9af00d66-f862-45b7-98d4-93fbd69fedba |
| Jogador 7 | 6-2 | 345 | BUY | FAST8 | 56.0 | 7 | 164 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0114858150482178 | 0.0 | 0.0 | +2ac6d717-87f1-4421-929e-1934a9317e72 / -21135c93-ae87-47a0-899c-7eaa0c2c30b8,50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de |
| Jogador 7 | 6-2 | 346 | BUY | FAST8 | 56.0 | 7 | 162 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4003041088581085 | 0.0 | 0.0 | +a810e10d-e7ef-4ece-8fb2-8b6471b557ec / -— |
| Jogador 7 | 6-2 | 347 | BUY | FAST8 | 56.0 | 7 | 161 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32848361134529114 | 0.0 | 0.0 | +425a58b3-d906-4381-9afc-00f9852c9982 / -— |
| Jogador 7 | 6-2 | 348 | MOVE_BOARD | FAST8 | 56.0 | 7 | 160 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 349 | MOVE_BOARD | FAST8 | 56.0 | 7 | 160 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499857846647501 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 350 | PASS | FAST8 | 56.0 | 7 | 160 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19594807922840118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 352 | SELL | STABILIZE | 37.0 | 7 | 171 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -2ac6d717-87f1-4421-929e-1934a9317e72 |
| Jogador 7 | 6-3 | 353 | BUY | STABILIZE | 37.0 | 7 | 176 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0781720876693726 | 0.0 | 0.0 | +4321582a-0b45-4666-a119-7b49e92d012a / -3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77,c93990ff-0a6f-46bc-8fc1-12623d55abc1 |
| Jogador 7 | 6-3 | 354 | BUY | STABILIZE | 37.0 | 7 | 173 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6217300891876221 | 0.0 | 0.0 | +04ebf9b8-7683-4270-b98a-a3bfb342dcf8 / -— |
| Jogador 7 | 6-3 | 355 | BUY | STABILIZE | 37.0 | 7 | 171 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18938946723937988 | 0.0 | 0.0 | +d47034a1-8b51-4b82-b1b4-5f2aee8f959a / -— |
| Jogador 7 | 6-3 | 356 | REROLL | STABILIZE | 37.0 | 7 | 168 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 357 | SELL | STABILIZE | 37.0 | 7 | 166 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -4321582a-0b45-4666-a119-7b49e92d012a |
| Jogador 7 | 6-3 | 358 | BUY | STABILIZE | 37.0 | 7 | 174 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9972710609436035 | 0.0 | 0.0 | +c55e9bf2-c9cf-4b76-a40c-6e8d73205402 / -— |
| Jogador 7 | 6-3 | 359 | SELL | STABILIZE | 37.0 | 7 | 171 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -c2bf43be-e6e1-47ed-bcb4-606e37f26671 |
| Jogador 7 | 6-3 | 360 | BUY | STABILIZE | 37.0 | 7 | 174 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41652244329452515 | 0.0 | 0.0 | +9f271ee0-c506-40b7-b3f3-bac209974ba2 / -— |
| Jogador 7 | 6-4 | 362 | SELL | ALL_IN | 18.0 | 7 | 184 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -d47034a1-8b51-4b82-b1b4-5f2aee8f959a |
| Jogador 7 | 6-4 | 363 | BUY | ALL_IN | 18.0 | 7 | 187 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1111680269241333 | 0.0 | 0.0 | +bfff6629-3ccc-4136-82a4-319a2fc5350e / -83a3ef65-b342-4ec8-b2d1-be99c3602f81,c55e9bf2-c9cf-4b76-a40c-6e8d73205402 |
| Jogador 7 | 6-4 | 364 | BUY | ALL_IN | 18.0 | 7 | 184 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27285951375961304 | 0.0 | 0.0 | +b053a0fd-0f0b-4343-a920-f0a36d36e771 / -— |
| Jogador 7 | 6-4 | 365 | BUY | ALL_IN | 18.0 | 7 | 182 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01468709111213684 | 0.0 | 0.0 | +497fbcb9-9d15-43f0-ad71-96eeceeee99d / -— |
| Jogador 7 | 6-4 | 366 | SELL | ALL_IN | 18.0 | 7 | 181 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.953499972820282 | 0.0 | 0.0 | +— / -bfff6629-3ccc-4136-82a4-319a2fc5350e |
| Jogador 7 | 6-4 | 367 | BUY | ALL_IN | 18.0 | 7 | 189 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2852117419242859 | 0.0 | 0.0 | +ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 / -— |
| Jogador 7 | 6-4 | 368 | SELL | ALL_IN | 18.0 | 7 | 187 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00025250413455069065 | 0.0 | 0.0 | +— / -497fbcb9-9d15-43f0-ad71-96eeceeee99d |
| Jogador 7 | 6-4 | 369 | BUY | ALL_IN | 18.0 | 7 | 188 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34253230690956116 | 0.0 | 0.0 | +a5247b50-831c-4600-bac0-e9bcdfa3ce1c / -— |
| Jogador 7 | 6-4 | 370 | REROLL | ALL_IN | 18.0 | 7 | 186 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 372 | SELL | ALL_IN | 18.0 | 7 | 195 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08139999955892563 | 0.0 | 0.0 | +— / -b053a0fd-0f0b-4343-a920-f0a36d36e771 |
| Jogador 7 | 6-5 | 373 | BUY | ALL_IN | 18.0 | 7 | 197 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.023306965827942 | 0.0 | 0.0 | +25029b69-ee52-4788-840e-006ff9e57d5d / -— |
| Jogador 7 | 6-5 | 374 | SELL | ALL_IN | 18.0 | 7 | 196 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5211377143859863 | 0.0 | 0.0 | +— / -ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 |
| Jogador 7 | 6-5 | 375 | BUY | ALL_IN | 18.0 | 7 | 198 | 5 | 42.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1107836961746216 | 0.0 | 0.0 | +db7ea53f-4df7-4c05-9462-75b527575615 / -ad1693cd-1ab5-43a9-8164-25929b8bd68e,f3e882b5-333e-44e3-ae82-cacacc8b1137 |
| Jogador 7 | 6-5 | 376 | MOVE_BENCH | ALL_IN | 18.0 | 7 | 195 | 5 | 30.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2854958474636078 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 377 | BUY | ALL_IN | 18.0 | 7 | 195 | 5 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4903540313243866 | 0.0 | 0.0 | +051d83d1-972e-42b2-ab59-376c753ad24e / -— |
| Jogador 7 | 6-5 | 378 | MOVE_BENCH | ALL_IN | 18.0 | 7 | 192 | 5 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4352008104324341 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 379 | BUY | ALL_IN | 18.0 | 7 | 192 | 5 | 40.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033326905220746994 | 0.0 | 0.0 | +bf33b437-04ac-4dd7-8c7d-ad48546675b8 / -— |
| Jogador 7 | 6-5 | 380 | MOVE_BOARD | ALL_IN | 18.0 | 7 | 190 | 5 | 40.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031589943915605545 | 0.0 | 0.0 | +88a02960-5ebe-4b20-b667-1a8ce2728578 / -— |
| Jogador 8 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16182130575180054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3620654344558716 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012301865965127945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5032565593719482 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0140845775604248 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36052340269088745 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 39 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2815742790699005 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 40 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.976382315158844 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 41 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17352721095085144 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25140801072120667 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 43 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11591137945652008 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 52 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1142686605453491 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -88a02960-5ebe-4b20-b667-1a8ce2728578,dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 2-1 | 53 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20080365240573883 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 54 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17912892997264862 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059163305908441544 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 56 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1034753322601318 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 57 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12414442747831345 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03405940160155296 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-1 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32108646631240845 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03419312834739685 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 62 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26139435172080994 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 63 | BUY | STABILIZE | 95.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2963879704475403 | 0.0 | 0.0 | +ebe77c97-f249-4265-ae03-bc8115a4795f / -— |
| Jogador 8 | 2-2 | 64 | SELL | STABILIZE | 95.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2130347341299057 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-2 | 65 | BUY_XP | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 66 | PASS | STABILIZE | 95.0 | 4 | 2 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 8 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0461432933807373 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 73 | BUY | STABILIZE | 90.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3648192286491394 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 74 | SELL | STABILIZE | 90.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-3 | 75 | BUY | STABILIZE | 90.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2261732518672943 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 76 | SELL | STABILIZE | 90.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13300000131130219 | 0.0 | 0.0 | +— / -ebe77c97-f249-4265-ae03-bc8115a4795f |
| Jogador 8 | 2-3 | 77 | SELL | STABILIZE | 90.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1451670527458191 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5311523675918579 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 79 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 7 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08555368334054947 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 80 | SELL | STABILIZE | 90.0 | 4 | 7 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10100000351667404 | 0.0 | 0.0 | +— / -a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 8 | 2-4 | 82 | BUY | STABILIZE | 84.0 | 5 | 15 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27009159326553345 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 83 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 12 | 1 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0941268801689148 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 84 | BUY | STABILIZE | 84.0 | 5 | 12 | 1 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08631152659654617 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 85 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 9 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48135578632354736 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 86 | BUY | STABILIZE | 84.0 | 5 | 9 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11592976003885269 | 0.0 | 0.0 | +3644801e-2247-403d-8b81-d2d3f15c2f55 / -— |
| Jogador 8 | 2-4 | 87 | SELL | STABILIZE | 84.0 | 5 | 8 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3996666669845581 | 0.0 | 0.0 | +— / -3644801e-2247-403d-8b81-d2d3f15c2f55 |
| Jogador 8 | 2-4 | 88 | SELL | STABILIZE | 84.0 | 5 | 9 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3076666593551636 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-4 | 89 | BUY | STABILIZE | 84.0 | 5 | 12 | 1 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03955617919564247 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 8 | 2-4 | 90 | SELL | STABILIZE | 84.0 | 5 | 11 | 1 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3569999933242798 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 8 | 2-5 | 92 | BUY | STABILIZE | 84.0 | 5 | 19 | 1 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0393832921981812 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 93 | BUY | STABILIZE | 84.0 | 5 | 18 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3651624917984009 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 94 | BUY | STABILIZE | 84.0 | 5 | 16 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2903115451335907 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 95 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49045076966285706 | 0.0 | 0.0 | +— / -35e1a0f6-207d-4df2-b096-fc07962d094a |
| Jogador 8 | 2-5 | 96 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 15 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30819740891456604 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 97 | SELL | STABILIZE | 84.0 | 5 | 15 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5798666477203369 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-5 | 98 | BUY | STABILIZE | 84.0 | 5 | 18 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0894991084933281 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-5 | 99 | BUY_XP | STABILIZE | 84.0 | 5 | 16 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 100 | BUY_XP | STABILIZE | 84.0 | 5 | 12 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 102 | BUY | STABILIZE | 78.0 | 5 | 14 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3309357762336731 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 103 | BUY | STABILIZE | 78.0 | 5 | 11 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1426135003566742 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 104 | SELL | STABILIZE | 78.0 | 5 | 8 | 0 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022038543596863747 | 0.0 | 0.0 | +— / -c0d8da9e-5ede-4a26-8c5c-e2a908318bfd |
| Jogador 8 | 2-6 | 105 | BUY | STABILIZE | 78.0 | 5 | 10 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05084475129842758 | 0.0 | 0.0 | +b482ecdd-cc1a-40fa-8c21-cd1cac92b594 / -— |
| Jogador 8 | 2-6 | 106 | SELL | STABILIZE | 78.0 | 5 | 9 | 0 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3184834420681 | 0.0 | 0.0 | +— / -b482ecdd-cc1a-40fa-8c21-cd1cac92b594 |
| Jogador 8 | 2-6 | 107 | SELL | STABILIZE | 78.0 | 5 | 10 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42233332991600037 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 2-6 | 108 | SELL | STABILIZE | 78.0 | 5 | 13 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18618203699588776 | 0.0 | 0.0 | +— / -87600495-fe90-4832-ab42-9a5cb0ebe3f4 |
| Jogador 8 | 2-6 | 109 | SELL | STABILIZE | 78.0 | 5 | 16 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 2-6 | 110 | BUY | STABILIZE | 78.0 | 5 | 17 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09266417473554611 | 0.0 | 0.0 | +c9a1ea77-662a-469a-ba7f-eac0713c0c52 / -— |
| Jogador 8 | 2-7 | 112 | BUY | STABILIZE | 78.0 | 5 | 22 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27489688992500305 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 113 | BUY | STABILIZE | 78.0 | 5 | 19 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14102372527122498 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 114 | SELL | STABILIZE | 78.0 | 5 | 16 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05789843946695328 | 0.0 | 0.0 | +— / -c9a1ea77-662a-469a-ba7f-eac0713c0c52 |
| Jogador 8 | 2-7 | 115 | BUY | STABILIZE | 78.0 | 5 | 18 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21169519424438477 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 116 | SELL | STABILIZE | 78.0 | 5 | 17 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42164742946624756 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 2-7 | 117 | SELL | STABILIZE | 78.0 | 5 | 18 | 1 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31700000166893005 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 2-7 | 118 | SELL | STABILIZE | 78.0 | 5 | 21 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1827651709318161 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 2-7 | 119 | BUY | STABILIZE | 78.0 | 5 | 24 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14491163194179535 | 0.0 | 0.0 | +60b0249f-e02f-4aca-b90d-75e9bcc822b8 / -— |
| Jogador 8 | 2-7 | 120 | SELL | STABILIZE | 78.0 | 5 | 23 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39600232243537903 | 0.0 | 0.0 | +— / -60b0249f-e02f-4aca-b90d-75e9bcc822b8 |
| Jogador 8 | 3-1 | 122 | BUY | STABILIZE | 78.0 | 5 | 31 | 3 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.13894668221473694 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 123 | BUY | STABILIZE | 78.0 | 5 | 27 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.001843540812842548 | 0.0 | 0.0 | +88420167-3841-43dd-b1d0-3e5ab2294c78 / -— |
| Jogador 8 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 78.0 | 5 | 25 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2646680474281311 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 25 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1317739337682724 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 126 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 25 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6527205109596252 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 127 | PASS | STABILIZE | 78.0 | 5 | 25 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02250000089406967 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 132 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 32 | 3 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0058861589059233665 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 133 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 32 | 3 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09884148091077805 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 134 | BUY | STABILIZE | 68.0 | 5 | 32 | 3 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09028962254524231 | 0.0 | 0.0 | +5326031a-1b7e-4dbd-b58b-1e81029d42a1 / -— |
| Jogador 8 | 3-2 | 135 | SELL | STABILIZE | 68.0 | 5 | 30 | 3 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04899999871850014 | 0.0 | 0.0 | +— / -88420167-3841-43dd-b1d0-3e5ab2294c78 |
| Jogador 8 | 3-2 | 136 | BUY | STABILIZE | 68.0 | 5 | 32 | 3 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09874159842729568 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 137 | SELL | STABILIZE | 68.0 | 5 | 31 | 3 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3930000066757202 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-2 | 138 | SELL | STABILIZE | 68.0 | 5 | 32 | 3 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3889999985694885 | 0.0 | 0.0 | +— / -5326031a-1b7e-4dbd-b58b-1e81029d42a1 |
| Jogador 8 | 3-2 | 139 | BUY | STABILIZE | 68.0 | 5 | 34 | 3 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2645508646965027 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 140 | BUY_XP | STABILIZE | 68.0 | 5 | 30 | 3 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056210000067949295 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 142 | BUY | STABILIZE | 58.0 | 6 | 34 | 3 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31011125445365906 | 0.0 | 0.0 | +1af578c1-57cf-4752-93e7-d0eebc6e8ae5 / -— |
| Jogador 8 | 3-3 | 143 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 32 | 3 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5294569730758667 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 144 | BUY | STABILIZE | 58.0 | 6 | 32 | 3 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07554195821285248 | 0.0 | 0.0 | +3bf8af53-85e7-4e5b-8cf8-b7198a955e8d / -— |
| Jogador 8 | 3-3 | 145 | BUY | STABILIZE | 58.0 | 6 | 31 | 3 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3079966902732849 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 58.0 | 6 | 28 | 2 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05154852941632271 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 147 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 28 | 2 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28810492157936096 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 148 | PASS | STABILIZE | 58.0 | 6 | 28 | 2 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 152 | BUY | STABILIZE | 58.0 | 6 | 36 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8463318347930908 | 0.0 | 0.0 | +eb7e36f0-cef9-4a2e-979a-f8a357da73e8 / -— |
| Jogador 8 | 3-4 | 153 | BUY | STABILIZE | 58.0 | 6 | 35 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1024957150220871 | 0.0 | 0.0 | +e8355df5-8ee7-44a3-ab88-3708c14fd5dc / -— |
| Jogador 8 | 3-4 | 154 | SELL | STABILIZE | 58.0 | 6 | 34 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39244478940963745 | 0.0 | 0.0 | +— / -e8355df5-8ee7-44a3-ab88-3708c14fd5dc |
| Jogador 8 | 3-4 | 155 | BUY | STABILIZE | 58.0 | 6 | 35 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21372292935848236 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 156 | SELL | STABILIZE | 58.0 | 6 | 32 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09300000220537186 | 0.0 | 0.0 | +— / -3bf8af53-85e7-4e5b-8cf8-b7198a955e8d |
| Jogador 8 | 3-4 | 157 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 33 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06575667858123779 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 158 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 33 | 3 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.65160071849823 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 159 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 33 | 3 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37427741289138794 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 160 | PASS | STABILIZE | 58.0 | 6 | 33 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12449999898672104 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 162 | BUY | STABILIZE | 58.0 | 6 | 41 | 4 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7436921000480652 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 163 | BUY | STABILIZE | 58.0 | 6 | 39 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8641573190689087 | 0.0 | 0.0 | +6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 / -1af578c1-57cf-4752-93e7-d0eebc6e8ae5,9b5e9e71-6772-49bc-979f-11f446f27b11 |
| Jogador 8 | 3-5 | 164 | BUY | STABILIZE | 58.0 | 6 | 37 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29538819193840027 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 8 | 3-5 | 165 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 34 | 3 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06324248760938644 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 34 | 3 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6610158085823059 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 167 | PASS | STABILIZE | 58.0 | 6 | 34 | 3 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.125 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 172 | BUY | STABILIZE | 58.0 | 6 | 44 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8281553983688354 | 0.0 | 0.0 | +b55260cd-3c6a-4cb8-99d0-b7c6471103ad / -— |
| Jogador 8 | 3-6 | 173 | SELL | STABILIZE | 58.0 | 6 | 41 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 |
| Jogador 8 | 3-6 | 174 | BUY | STABILIZE | 58.0 | 6 | 46 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30979347229003906 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -— |
| Jogador 8 | 3-6 | 175 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 44 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27134400606155396 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 176 | SELL | STABILIZE | 58.0 | 6 | 44 | 4 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010833333246409893 | 0.0 | 0.0 | +— / -82e109f9-54c8-492d-93e5-7e0dd0034b15 |
| Jogador 8 | 3-6 | 177 | BUY | STABILIZE | 58.0 | 6 | 47 | 4 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2934829592704773 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 178 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 43 | 4 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06575667858123779 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 179 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 43 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6516499519348145 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 180 | MOVE_BENCH | STABILIZE | 58.0 | 6 | 43 | 4 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4097152352333069 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 182 | SELL | STABILIZE | 48.0 | 6 | 52 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -e4605ac7-0b51-4f1c-a658-f7d25f9a9dae |
| Jogador 8 | 3-7 | 183 | BUY | STABILIZE | 48.0 | 6 | 55 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1310417503118515 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 184 | SELL | STABILIZE | 48.0 | 6 | 52 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -4ac49c80-f0c3-47ae-a031-96928d244e13 |
| Jogador 8 | 3-7 | 185 | BUY | STABILIZE | 48.0 | 6 | 56 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19863104820251465 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 8 | 3-7 | 186 | SELL | STABILIZE | 48.0 | 6 | 53 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -112206a4-c285-4f76-878a-056248cba468 |
| Jogador 8 | 3-7 | 187 | BUY | STABILIZE | 48.0 | 6 | 56 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047420307993888855 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 8 | 3-7 | 188 | SELL | STABILIZE | 48.0 | 6 | 55 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005741680972278118 | 0.0 | 0.0 | +— / -a14e4b8f-77c5-4909-a9ee-0044b836a877 |
| Jogador 8 | 3-7 | 189 | BUY | STABILIZE | 48.0 | 6 | 56 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26260659098625183 | 0.0 | 0.0 | +3625f791-4c9f-4b95-bdf7-4a322dcd55d3 / -— |
| Jogador 8 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 54 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 48.0 | 6 | 64 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18419773876667023 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 48.0 | 6 | 64 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24980567395687103 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 194 | SELL | STABILIZE | 48.0 | 6 | 64 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -3625f791-4c9f-4b95-bdf7-4a322dcd55d3 |
| Jogador 8 | 4-1 | 195 | BUY | STABILIZE | 48.0 | 6 | 66 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9612974524497986 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -64afe66e-d5a9-466c-a4ff-9d32c9f153ce,f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 4-1 | 196 | BUY | STABILIZE | 48.0 | 6 | 65 | 5 | 26.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7415582537651062 | 0.0 | 0.0 | +88035b70-61e0-4279-9d55-e451f412f0d3 / -— |
| Jogador 8 | 4-1 | 197 | MOVE_BENCH | STABILIZE | 48.0 | 6 | 62 | 5 | 26.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5952591896057129 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 198 | BUY | STABILIZE | 48.0 | 6 | 62 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14880964159965515 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 8 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 60 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003772716037929058 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 60 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 202 | SELL | STABILIZE | 48.0 | 6 | 71 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -2faa526c-d29e-47a9-9eb3-5030750cb483 |
| Jogador 8 | 4-2 | 203 | BUY | STABILIZE | 48.0 | 6 | 74 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8445054888725281 | 0.0 | 0.0 | +7e0c9595-0ca2-44d4-bfe9-3752c7a89e0d / -— |
| Jogador 8 | 4-2 | 204 | SELL | STABILIZE | 48.0 | 6 | 73 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -1e81ac95-667f-494d-89eb-2bcdcf887a7e |
| Jogador 8 | 4-2 | 205 | BUY | STABILIZE | 48.0 | 6 | 75 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048125822097063065 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -— |
| Jogador 8 | 4-2 | 206 | SELL | STABILIZE | 48.0 | 6 | 72 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -849ea0fc-7f61-4907-8abb-b25c8cc82efc |
| Jogador 8 | 4-2 | 207 | BUY | STABILIZE | 48.0 | 6 | 75 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20788632333278656 | 0.0 | 0.0 | +08a36d54-bb5c-48a6-afb1-e0f9943bf069 / -— |
| Jogador 8 | 4-2 | 208 | SELL | STABILIZE | 48.0 | 6 | 71 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 |
| Jogador 8 | 4-2 | 209 | SELL | STABILIZE | 48.0 | 6 | 74 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35153332352638245 | 0.0 | 0.0 | +— / -08a36d54-bb5c-48a6-afb1-e0f9943bf069 |
| Jogador 8 | 4-2 | 210 | SELL | STABILIZE | 48.0 | 6 | 78 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5297554731369019 | 0.0 | 0.0 | +— / -88035b70-61e0-4279-9d55-e451f412f0d3 |
| Jogador 8 | 4-3 | 212 | BUY | STABILIZE | 48.0 | 6 | 93 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.923139750957489 | 0.0 | 0.0 | +579b987a-fedf-45d8-92fc-634a041d3d4f / -— |
| Jogador 8 | 4-3 | 213 | BUY | STABILIZE | 48.0 | 6 | 91 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38226082921028137 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 8 | 4-3 | 214 | BUY | STABILIZE | 48.0 | 6 | 88 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16971343755722046 | 0.0 | 0.0 | +8455b875-27e0-4172-9311-5cbb3e2242b9 / -— |
| Jogador 8 | 4-3 | 215 | SELL | STABILIZE | 48.0 | 6 | 85 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04198592156171799 | 0.0 | 0.0 | +— / -8455b875-27e0-4172-9311-5cbb3e2242b9 |
| Jogador 8 | 4-3 | 216 | BUY | STABILIZE | 48.0 | 6 | 88 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17108340561389923 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 8 | 4-3 | 217 | SELL | STABILIZE | 48.0 | 6 | 86 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -e85c6ab6-f36c-40b4-88e2-b7380b4c9652 |
| Jogador 8 | 4-3 | 218 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 88 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 219 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 88 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06664257496595383 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 220 | PASS | STABILIZE | 48.0 | 6 | 88 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1068849265575409 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 222 | BUY | STABILIZE | 37.0 | 6 | 98 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9030803442001343 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -— |
| Jogador 8 | 4-4 | 223 | SELL | STABILIZE | 37.0 | 6 | 95 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41057777404785156 | 0.0 | 0.0 | +— / -a23ee552-279e-4c6c-aa05-6197043e8f1d |
| Jogador 8 | 4-4 | 224 | BUY | STABILIZE | 37.0 | 6 | 99 | 5 | 28.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9610081911087036 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,7e0c9595-0ca2-44d4-bfe9-3752c7a89e0d |
| Jogador 8 | 4-4 | 225 | BUY | STABILIZE | 37.0 | 6 | 98 | 5 | 26.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9607531428337097 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -579b987a-fedf-45d8-92fc-634a041d3d4f,b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 |
| Jogador 8 | 4-4 | 226 | MOVE_BENCH | STABILIZE | 37.0 | 6 | 96 | 5 | 26.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6402055621147156 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 227 | BUY | STABILIZE | 37.0 | 6 | 96 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006459187716245651 | 0.0 | 0.0 | +a58767a1-d7c1-48e9-94ae-df46a364ef92 / -— |
| Jogador 8 | 4-4 | 228 | BUY | STABILIZE | 37.0 | 6 | 95 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2830265462398529 | 0.0 | 0.0 | +3a1de7b3-af72-4024-8105-588fa4ec946b / -— |
| Jogador 8 | 4-4 | 229 | MOVE_BOARD | STABILIZE | 37.0 | 6 | 94 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 230 | MOVE_BOARD | STABILIZE | 37.0 | 6 | 94 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 232 | BUY | STABILIZE | 37.0 | 6 | 104 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37559202313423157 | 0.0 | 0.0 | +772bccc4-15f4-4de2-95f8-82d0ed9a72d2 / -— |
| Jogador 8 | 4-5 | 233 | SELL | STABILIZE | 37.0 | 6 | 102 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -734c25e1-eddf-4452-a04a-1b39db3b94d0 |
| Jogador 8 | 4-5 | 234 | BUY | STABILIZE | 37.0 | 6 | 107 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15659277141094208 | 0.0 | 0.0 | +4a885bc0-41b4-43f1-94d3-8e755a10645c / -— |
| Jogador 8 | 4-5 | 235 | SELL | STABILIZE | 37.0 | 6 | 104 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -5f9e16e2-0766-403f-a85a-f6a735c04261 |
| Jogador 8 | 4-5 | 236 | EQUIP_FROM_INVENTORY | STABILIZE | 37.0 | 6 | 107 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1299111694097519 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 237 | EQUIP_FROM_INVENTORY | STABILIZE | 37.0 | 6 | 107 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.17732809484004974 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 238 | EQUIP_FROM_INVENTORY | STABILIZE | 37.0 | 6 | 107 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13047081232070923 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 239 | BUY | STABILIZE | 37.0 | 6 | 107 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21643424034118652 | 0.0 | 0.0 | +815aab3d-cea8-4ca6-aea3-3c9d656e6edd / -— |
| Jogador 8 | 4-5 | 240 | MOVE_BOARD | STABILIZE | 37.0 | 6 | 105 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003626120975241065 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 242 | SELL | ALL_IN | 25.0 | 6 | 116 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -3a1de7b3-af72-4024-8105-588fa4ec946b |
| Jogador 8 | 4-6 | 243 | BUY | ALL_IN | 25.0 | 6 | 117 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0012813806533813 | 0.0 | 0.0 | +57d86f23-f167-472f-9878-21dcddc0a5f7 / -9af097e2-729d-474a-9a7e-b266c665c606,b55260cd-3c6a-4cb8-99d0-b7c6471103ad |
| Jogador 8 | 4-6 | 244 | BUY | ALL_IN | 25.0 | 6 | 114 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023844948038458824 | 0.0 | 0.0 | +d80c845d-24bc-4053-a60d-5d0122839b0c / -— |
| Jogador 8 | 4-6 | 245 | BUY | ALL_IN | 25.0 | 6 | 113 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28277823328971863 | 0.0 | 0.0 | +362f7357-283e-4f88-bff3-ffa6314af821 / -— |
| Jogador 8 | 4-6 | 246 | SELL | ALL_IN | 25.0 | 6 | 111 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.680400013923645 | 0.0 | 0.0 | +— / -57d86f23-f167-472f-9878-21dcddc0a5f7 |
| Jogador 8 | 4-6 | 247 | BUY | ALL_IN | 25.0 | 6 | 119 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28643569350242615 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -— |
| Jogador 8 | 4-6 | 248 | SELL | ALL_IN | 25.0 | 6 | 118 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -a3def045-2a10-4672-a6d6-255c40fd1c90 |
| Jogador 8 | 4-6 | 249 | BUY | ALL_IN | 25.0 | 6 | 119 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28643929958343506 | 0.0 | 0.0 | +943437ce-e190-4790-986b-4e66e49637a7 / -— |
| Jogador 8 | 4-6 | 250 | MOVE_BOARD | ALL_IN | 25.0 | 6 | 118 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04249582439661026 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 252 | SELL | ALL_IN | 12.0 | 6 | 129 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -943437ce-e190-4790-986b-4e66e49637a7 |
| Jogador 8 | 4-7 | 253 | BUY | ALL_IN | 12.0 | 6 | 130 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6010078191757202 | 0.0 | 0.0 | +2949d735-3c16-4a45-835b-e11a9c12b16a / -— |
| Jogador 8 | 4-7 | 254 | SELL | ALL_IN | 12.0 | 6 | 127 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015009548515081406 | 0.0 | 0.0 | +— / -a58767a1-d7c1-48e9-94ae-df46a364ef92 |
| Jogador 8 | 4-7 | 255 | BUY | ALL_IN | 12.0 | 6 | 128 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2755766212940216 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 8 | 4-7 | 256 | SELL | ALL_IN | 12.0 | 6 | 126 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014139821752905846 | 0.0 | 0.0 | +— / -d80c845d-24bc-4053-a60d-5d0122839b0c |
| Jogador 8 | 4-7 | 257 | BUY | ALL_IN | 12.0 | 6 | 127 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09219378978013992 | 0.0 | 0.0 | +0d120db3-34e2-47e3-a57c-0d65dcc56342 / -— |
| Jogador 8 | 4-7 | 258 | SELL | ALL_IN | 12.0 | 6 | 125 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -815aab3d-cea8-4ca6-aea3-3c9d656e6edd |
| Jogador 8 | 4-7 | 259 | BUY | ALL_IN | 12.0 | 6 | 127 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018852893263101578 | 0.0 | 0.0 | +ff181737-4995-4a67-add2-4f55cebabbee / -— |
| Jogador 8 | 4-7 | 260 | REROLL | ALL_IN | 12.0 | 6 | 126 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 262 | CRAFT_AND_EQUIP | ALL_IN | 12.0 | 6 | 135 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17807935178279877 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 12.0 | 6 | 135 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12055497616529465 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 264 | SELL | ALL_IN | 12.0 | 6 | 135 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017017455771565437 | 0.0 | 0.0 | +— / -ff181737-4995-4a67-add2-4f55cebabbee |
| Jogador 8 | 5-1 | 265 | BUY | ALL_IN | 12.0 | 6 | 136 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22138391435146332 | 0.0 | 0.0 | +4b1f1146-d580-41e9-987f-c32b1eb98b75 / -— |
| Jogador 8 | 5-1 | 266 | SELL | ALL_IN | 12.0 | 6 | 134 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -4b1f1146-d580-41e9-987f-c32b1eb98b75 |
| Jogador 8 | 5-1 | 267 | BUY | ALL_IN | 12.0 | 6 | 136 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020044509321451187 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -— |
| Jogador 8 | 5-1 | 268 | SELL | ALL_IN | 12.0 | 6 | 135 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016697708517313004 | 0.0 | 0.0 | +— / -8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 |
| Jogador 8 | 5-1 | 269 | BUY | ALL_IN | 12.0 | 6 | 136 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28043484687805176 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 8 | 5-1 | 270 | REROLL | ALL_IN | 12.0 | 6 | 133 | 5 | 32.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 183 | 165 | 91 | 6 | 7 | 0 | 1 | 0 | 77 | 34.0 |
- Jogador 1 — gasto por ação: BUY: 131g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 47g, stage 3: 52g, stage 4: 60g
| Jogador 2 | 332 | 405 | 248 | 15 | 21 | 0 | 0 | 0 | 147 | 50.0 |
- Jogador 2 — gasto por ação: BUY: 309g, BUY_XP: 96g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 58g, stage 3: 103g, stage 4: 75g, stage 5: 78g, stage 6: 70g, stage 7: 14g
| Jogador 3 | 272 | 261 | 127 | 7 | 14 | 1 | 0 | 0 | 198 | 64.0 |
- Jogador 3 — gasto por ação: BUY: 197g, BUY_XP: 64g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 46g, stage 3: 76g, stage 4: 16g, stage 5: 41g, stage 6: 66g, stage 7: 9g
| Jogador 4 | 196 | 194 | 112 | 7 | 6 | 1 | 4 | 0 | 86 | 34.0 |
- Jogador 4 — gasto por ação: BUY: 154g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 8g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 69g, stage 3: 43g, stage 4: 65g, stage 5: 11g
| Jogador 5 | 186 | 190 | 125 | 6 | 4 | 0 | 4 | 0 | 93 | 18.0 |
- Jogador 5 — gasto por ação: BUY: 158g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 8g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 59g, stage 3: 63g, stage 4: 61g
| Jogador 6 | 202 | 218 | 120 | 6 | 11 | 0 | 2 | 0 | 78 | 30.0 |
- Jogador 6 — gasto por ação: BUY: 166g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 69g, stage 3: 54g, stage 4: 59g, stage 5: 31g
| Jogador 7 | 243 | 208 | 102 | 4 | 10 | 1 | 2 | 0 | 190 | 40.0 |
- Jogador 7 — gasto por ação: BUY: 156g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 64g, stage 3: 48g, stage 4: 17g, stage 5: 26g, stage 6: 47g
| Jogador 8 | 205 | 183 | 123 | 9 | 3 | 1 | 2 | 0 | 131 | 32.0 |
- Jogador 8 — gasto por ação: BUY: 163g, BUY_XP: 16g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 58g, stage 3: 53g, stage 4: 57g, stage 5: 8g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 8 | 6 |
- Jogador 1 · 2-7 · step 116: PASS com 4g, HP 95, nível 6/8 (STABILIZE).
- Jogador 1 · 3-4 · step 160: PASS com 6g, HP 75, nível 6/8 (STABILIZE).
- Jogador 1 · 3-6 · step 180: PASS com 15g, HP 66, nível 6/8 (STABILIZE).
- Jogador 1 · 4-2 · step 209: PASS com 41g, HP 45, nível 6/8 (STABILIZE).
- Jogador 1 · 4-3 · step 220: REROLL com 54g, HP 33, nível 6/8 (STABILIZE).
- Jogador 1 · 4-4 · step 230: PASS com 51g, HP 22, nível 7/8 (ALL_IN).
| Jogador 2 | 24 | 0 |
| Jogador 3 | 16 | 13 |
- Jogador 3 · 3-2 · step 138: PASS com 10g, HP 100, nível 6/8 (STABILIZE).
- Jogador 3 · 3-3 · step 147: PASS com 17g, HP 100, nível 6/8 (STABILIZE).
- Jogador 3 · 4-3 · step 214: PASS com 10g, HP 90, nível 7/8 (FAST8).
- Jogador 3 · 4-4 · step 224: PASS com 18g, HP 90, nível 7/8 (FAST8).
- Jogador 3 · 4-5 · step 234: PASS com 25g, HP 90, nível 7/8 (FAST8).
- Jogador 3 · 4-6 · step 249: PASS com 38g, HP 90, nível 7/8 (FAST8).
- Jogador 3 · 4-7 · step 256: PASS com 45g, HP 90, nível 7/8 (FAST8).
- Jogador 3 · 5-1 · step 266: PASS com 56g, HP 90, nível 7/8 (FAST8).
- Jogador 3 · 5-2 · step 276: PASS com 71g, HP 90, nível 7/8 (FAST8).
- Jogador 3 · 5-3 · step 287: PASS com 79g, HP 74, nível 7/8 (FAST8).
- Jogador 3 · 5-4 · step 300: PASS com 88g, HP 58, nível 7/8 (FAST8).
- Jogador 3 · 5-5 · step 309: PASS com 98g, HP 58, nível 7/8 (FAST8).
- Jogador 3 · 5-6 · step 318: PASS com 102g, HP 42, nível 7/8 (FAST8).
| Jogador 4 | 8 | 8 |
- Jogador 4 · 3-5 · step 169: PASS com 9g, HP 64, nível 6/8 (STABILIZE).
- Jogador 4 · 3-6 · step 180: PASS com 18g, HP 64, nível 6/8 (STABILIZE).
- Jogador 4 · 4-1 · step 198: PASS com 34g, HP 64, nível 6/8 (STABILIZE).
- Jogador 4 · 4-3 · step 218: REROLL com 51g, HP 39, nível 6/8 (STABILIZE).
- Jogador 4 · 4-4 · step 228: PASS com 55g, HP 39, nível 7/8 (STABILIZE).
- Jogador 4 · 4-6 · step 246: REROLL com 68g, HP 26, nível 7/8 (STABILIZE).
- Jogador 4 · 4-7 · step 258: REROLL com 77g, HP 14, nível 7/8 (ALL_IN).
- Jogador 4 · 5-1 · step 269: REROLL com 80g, HP 14, nível 7/8 (ALL_IN).
| Jogador 5 | 6 | 5 |
- Jogador 5 · 3-3 · step 150: PASS com 18g, HP 81, nível 6/8 (STABILIZE).
- Jogador 5 · 4-3 · step 220: REROLL com 70g, HP 32, nível 6/8 (STABILIZE).
- Jogador 5 · 4-4 · step 227: REROLL com 80g, HP 19, nível 6/8 (ALL_IN).
- Jogador 5 · 4-5 · step 237: REROLL com 87g, HP 19, nível 6/8 (ALL_IN).
- Jogador 5 · 4-6 · step 250: REROLL com 95g, HP 8, nível 6/8 (ALL_IN).
| Jogador 6 | 12 | 4 |
- Jogador 6 · 4-2 · step 209: PASS com 18g, HP 54, nível 7/8 (STABILIZE).
- Jogador 6 · 4-5 · step 238: PASS com 36g, HP 32, nível 7/8 (STABILIZE).
- Jogador 6 · 4-6 · step 248: REROLL com 43g, HP 32, nível 7/8 (STABILIZE).
- Jogador 6 · 4-7 · step 260: REROLL com 51g, HP 32, nível 7/8 (STABILIZE).
| Jogador 7 | 12 | 16 |
- Jogador 7 · 4-2 · step 205: PASS com 7g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 4-3 · step 215: PASS com 14g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 4-4 · step 225: PASS com 19g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 4-5 · step 238: PASS com 24g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 4-6 · step 247: PASS com 36g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 4-7 · step 259: PASS com 48g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 5-1 · step 268: PASS com 52g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 5-2 · step 276: PASS com 71g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 5-3 · step 287: PASS com 86g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 5-4 · step 297: PASS com 102g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 5-5 · step 307: PASS com 112g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 5-6 · step 315: PASS com 122g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 5-7 · step 326: PASS com 141g, HP 74, nível 7/8 (FAST8).
- Jogador 7 · 6-2 · step 350: PASS com 160g, HP 56, nível 7/8 (FAST8).
- Jogador 7 · 6-3 · step 356: REROLL com 168g, HP 37, nível 7/8 (STABILIZE).
- Jogador 7 · 6-4 · step 370: REROLL com 186g, HP 18, nível 7/8 (ALL_IN).
| Jogador 8 | 4 | 7 |
- Jogador 8 · 3-1 · step 127: PASS com 25g, HP 78, nível 5/8 (STABILIZE).
- Jogador 8 · 3-3 · step 148: PASS com 28g, HP 58, nível 6/8 (STABILIZE).
- Jogador 8 · 3-4 · step 160: PASS com 33g, HP 58, nível 6/8 (STABILIZE).
- Jogador 8 · 3-5 · step 167: PASS com 34g, HP 58, nível 6/8 (STABILIZE).
- Jogador 8 · 4-3 · step 220: PASS com 88g, HP 48, nível 6/8 (STABILIZE).
- Jogador 8 · 4-7 · step 260: REROLL com 126g, HP 12, nível 6/8 (ALL_IN).
- Jogador 8 · 5-1 · step 270: REROLL com 133g, HP 12, nível 6/8 (ALL_IN).

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
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 183 | 37 | 39 | 107 | 0.0043 | 0.1529 | 0.0016 | 0.3412 | 0.0027 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0209 (62 ações), BUY_XP: Δ 0.0061 (8 ações), CRAFT_AND_EQUIP: Δ 0.0028 (5 ações), MOVE_BENCH: Δ -0.0518 (15 ações), MOVE_BOARD: Δ 0.0485 (42 ações), PASS: Δ 0.0000 (15 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0214 (35 ações)
| Jogador 2 | 332 | 47 | 40 | 245 | 0.0025 | 0.6853 | 0.0010 | 0.3796 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0010 (125 ações), BUY_XP: Δ 0.0065 (24 ações), CRAFT_AND_EQUIP: Δ 0.0010 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (7 ações), MOVE_BENCH: Δ 0.0507 (20 ações), MOVE_BOARD: Δ -0.0194 (43 ações), PASS: Δ 0.0000 (17 ações), SELL: Δ 0.0069 (89 ações)
| Jogador 3 | 272 | 47 | 39 | 186 | 0.0022 | 0.5188 | 0.0009 | 0.3260 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0127 (79 ações), BUY_XP: Δ 0.0061 (16 ações), CRAFT_AND_EQUIP: Δ 0.0106 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0169 (30 ações), MOVE_BOARD: Δ 0.0074 (68 ações), PASS: Δ 0.0000 (31 ações), SELL: Δ 0.0108 (39 ações)
| Jogador 4 | 196 | 41 | 33 | 122 | -0.0008 | -0.1485 | -0.0013 | 0.4025 | 0.0005 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0268 (73 ações), BUY_XP: Δ 0.0135 (8 ações), CRAFT_AND_EQUIP: Δ 0.0020 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0860 (6 ações), MOVE_BENCH: Δ 0.0065 (16 ações), MOVE_BOARD: Δ -0.0048 (30 ações), PASS: Δ 0.0462 (13 ações), REROLL: Δ 0.0000 (4 ações), SELL: Δ 0.0153 (39 ações)
| Jogador 5 | 186 | 28 | 25 | 133 | 0.0021 | -0.0713 | 0.0001 | 0.3383 | 0.0020 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0063 (84 ações), BUY_XP: Δ 0.0162 (6 ações), CRAFT_AND_EQUIP: Δ 0.0489 (5 ações), MOVE_BENCH: Δ -0.0586 (14 ações), MOVE_BOARD: Δ 0.1148 (7 ações), PASS: Δ 0.0000 (8 ações), REROLL: Δ 0.0000 (4 ações), SELL: Δ 0.0102 (58 ações)
| Jogador 6 | 202 | 37 | 34 | 131 | 0.0044 | -0.1841 | 0.0024 | 0.4505 | 0.0020 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0217 (71 ações), BUY_XP: Δ 0.0022 (12 ações), CRAFT_AND_EQUIP: Δ 0.0324 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (6 ações), MOVE_BENCH: Δ 0.0761 (13 ações), MOVE_BOARD: Δ 0.0181 (32 ações), PASS: Δ 0.0000 (15 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0136 (44 ações)
| Jogador 7 | 243 | 51 | 48 | 144 | -0.0002 | 0.3661 | -0.0018 | 0.3925 | 0.0016 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0140 (70 ações), BUY_XP: Δ 0.0081 (12 ações), CRAFT_AND_EQUIP: Δ 0.0086 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0601 (3 ações), MOVE_BENCH: Δ 0.0585 (12 ações), MOVE_BOARD: Δ 0.0082 (75 ações), PASS: Δ 0.0000 (29 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ -0.0218 (33 ações)
| Jogador 8 | 205 | 33 | 32 | 140 | 0.0016 | -0.0739 | -0.0004 | 0.3476 | 0.0020 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0012 (83 ações), BUY_XP: Δ 0.0122 (4 ações), CRAFT_AND_EQUIP: Δ 0.0030 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0157 (27 ações), MOVE_BOARD: Δ -0.0149 (14 ações), PASS: Δ 0.0000 (10 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0025 (55 ações)
- Jogador 1 — rounds avaliados: 24; correlação estrutural/combate: -0.083; posicional/combate: -0.371.
- Jogador 1 — combate positive: score estrutural prévio 0.191
  score posicional prévio 0.291
- Jogador 1 — combate negative: score estrutural prévio 0.216
  score posicional prévio 0.398
- Jogador 2 — rounds avaliados: 40; correlação estrutural/combate: 0.030; posicional/combate: 0.049.
- Jogador 2 — combate positive: score estrutural prévio 0.709
  score posicional prévio 0.379
- Jogador 2 — combate negative: score estrutural prévio 0.738
  score posicional prévio 0.366
- Jogador 3 — rounds avaliados: 40; correlação estrutural/combate: -0.221; posicional/combate: -0.201.
- Jogador 3 — combate positive: score estrutural prévio 0.383
  score posicional prévio 0.289
- Jogador 3 — combate negative: score estrutural prévio 0.565
  score posicional prévio 0.366
- Jogador 4 — rounds avaliados: 26; correlação estrutural/combate: 0.319; posicional/combate: 0.010.
- Jogador 4 — combate positive: score estrutural prévio 0.015
  score posicional prévio 0.410
- Jogador 4 — combate negative: score estrutural prévio -0.197
  score posicional prévio 0.391
- Jogador 5 — rounds avaliados: 24; correlação estrutural/combate: -0.133; posicional/combate: -0.271.
- Jogador 5 — combate positive: score estrutural prévio -0.102
  score posicional prévio 0.327
- Jogador 5 — combate negative: score estrutural prévio -0.042
  score posicional prévio 0.350
- Jogador 6 — rounds avaliados: 28; correlação estrutural/combate: 0.185; posicional/combate: -0.072.
- Jogador 6 — combate positive: score estrutural prévio 0.220
  score posicional prévio 0.433
- Jogador 6 — combate negative: score estrutural prévio -0.244
  score posicional prévio 0.460
- Jogador 7 — rounds avaliados: 37; correlação estrutural/combate: 0.111; posicional/combate: -0.201.
- Jogador 7 — combate positive: score estrutural prévio 0.425
  score posicional prévio 0.372
- Jogador 7 — combate negative: score estrutural prévio 0.365
  score posicional prévio 0.428
- Jogador 8 — rounds avaliados: 26; correlação estrutural/combate: 0.263; posicional/combate: 0.116.
- Jogador 8 — combate positive: score estrutural prévio 0.051
  score posicional prévio 0.353
- Jogador 8 — combate negative: score estrutural prévio -0.211
  score posicional prévio 0.341

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 206 | OK (206) | 5 | 0 | 0 | 1 | 5 | 0 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_HextechGunblade, TFT_Item_InfinityEdge, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 372 | OK (372) | 9 | 0 | 0 | 0 | 9 | 3 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_GargoyleStoneplate, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_Quicksilver, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 311 | OK (311) | 9 | 0 | 0 | 0 | 9 | 1 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Deathblade, TFT_Item_GuinsoosRageblade, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_RedBuff, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 221 | OK (221) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_BlueBuff, TFT_Item_JeweledGauntlet, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 209 | OK (209) | 5 | 0 | 0 | 1 | 5 | 0 |
- Jogador 5 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_IonicSpark, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_PowerGauntlet; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 229 | OK (229) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 6 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_InfinityEdge, TFT_Item_Morellonomicon, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 279 | OK (279) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 7 — IDs equipados observados: TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 230 | OK (230) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 8 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_DragonsClaw, TFT_Item_HextechGunblade, TFT_Item_JeweledGauntlet, TFT_Item_LastWhisper, TFT_Item_Morellonomicon, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
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
| Jogador 1 | 2-7 | 6 | 2.000 | 2.000 | 1 → 2 | 2 → 2 | 21% → 18% | 7 → 10 | 3 | 6 → 6 | -0.072 | 0.000 |
| Jogador 1 | 3-1 | 10 | 4.000 | 0.000 | 2 → 2 | 2 → 2 | 18% → 21% | 10 → 5 | 10 | 6 → 6 | -0.006 | -0.268 |
| Jogador 1 | 3-2 | 10 | 0.000 | 2.000 | 2 → 2 | 2 → 2 | 21% → 21% | 5 → 6 | 9 | 6 → 6 | 0.007 | -0.263 |
| Jogador 1 | 3-3 | 10 | 0.000 | 12.000 | 2 → 2 | 2 → 2 | 21% → 21% | 6 → 6 | 9 | 6 → 6 | -0.000 | 0.286 |
| Jogador 1 | 3-4 | 10 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 21% → 21% | 6 → 11 | 5 | 6 → 6 | -0.008 | 0.000 |
| Jogador 1 | 3-5 | 10 | 2.000 | 2.000 | 2 → 2 | 2 → 2 | 21% → 21% | 11 → 12 | 4 | 6 → 6 | 0.040 | -0.254 |
| Jogador 1 | 3-6 | 10 | 0.000 | -4.000 | 2 → 2 | 2 → 4 | 21% → 21% | 12 → 22 | 5 | 6 → 6 | -0.004 | -0.254 |
| Jogador 1 | 3-7 | 10 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 21% → 21% | 22 → 30 | 10 | 6 → 6 | -0.016 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | -4.000 | 2 → 2 | 4 → 4 | 21% → 21% | 30 → 41 | 9 | 6 → 6 | 0.000 | -0.291 |
| Jogador 1 | 4-2 | 9 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 21% → 21% | 41 → 51 | 6 | 6 → 6 | 0.009 | -0.307 |
| Jogador 1 | 4-3 | 10 | 0.000 | -8.000 | 2 → 2 | 4 → 3 | 21% → 21% | 51 → 64 | 9 | 6 → 7 | 0.004 | -0.268 |
| Jogador 1 | 4-4 | 10 | 8.000 | 18.000 | 2 → 2 | 3 → 3 | 21% → 25% | 64 → 63 | 14 | 7 → 7 | 0.030 | 0.000 |
| Jogador 1 | 4-5 | 10 | 0.000 | 4.000 | 2 → 2 | 3 → 3 | 25% → 25% | 63 → 74 | 10 | 7 → 7 | -0.008 | -0.281 |
| Jogador 1 | 4-6 | 10 | -34.000 | -46.000 | 2 → 0 | 3 → 0 | 25% → 0% | 74 → 77 | 12 | 7 → 7 | -0.089 | -0.271 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 26, COMPOSITION_COMPATIBILITY: 20, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 43 ações e piorou em 41.
- Jogador 1 — estado final: ouro 77, nível 7, vida 10.0, colocação 8.
| Jogador 2 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.161 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.109 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 3 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 10 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 11% → 14% | 4 → 5 | 5 | 4 → 4 | 0.026 | -0.226 |
| Jogador 2 | 2-2 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 1 | 14% → 14% | 5 → 6 | 8 | 4 → 4 | 0.033 | -0.243 |
| Jogador 2 | 2-3 | 10 | 6.000 | -2.000 | 1 → 1 | 1 → 1 | 14% → 18% | 6 → 6 | 10 | 4 → 5 | 0.009 | 0.251 |
| Jogador 2 | 2-4 | 6 | 0.000 | 12.000 | 1 → 1 | 1 → 1 | 18% → 18% | 6 → 5 | 6 | 5 → 5 | 0.003 | 0.000 |
| Jogador 2 | 2-5 | 10 | 4.000 | 2.000 | 1 → 1 | 1 → 1 | 18% → 18% | 5 → 7 | 5 | 5 → 5 | 0.003 | -0.243 |
| Jogador 2 | 2-6 | 10 | 0.000 | -4.000 | 1 → 1 | 1 → 2 | 18% → 18% | 7 → 7 | 14 | 5 → 5 | 0.001 | -0.249 |
| Jogador 2 | 2-7 | 10 | 2.000 | 4.000 | 1 → 1 | 2 → 3 | 18% → 21% | 7 → 6 | 10 | 5 → 6 | 0.012 | 0.000 |
| Jogador 2 | 3-1 | 10 | 0.000 | 4.000 | 1 → 1 | 3 → 2 | 21% → 21% | 6 → 6 | 12 | 6 → 6 | 0.000 | -0.273 |
| Jogador 2 | 3-2 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 9 | 9 | 6 → 6 | 0.000 | 0.276 |
| Jogador 2 | 3-3 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 3 | 21% → 21% | 9 → 9 | 18 | 6 → 6 | 0.000 | 0.272 |
| Jogador 2 | 3-4 | 10 | 0.000 | -6.000 | 1 → 1 | 3 → 3 | 21% → 21% | 9 → 10 | 14 | 6 → 7 | 0.005 | 0.000 |
| Jogador 2 | 3-5 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 2 | 21% → 21% | 10 → 9 | 15 | 7 → 7 | 0.000 | -0.258 |
| Jogador 2 | 3-6 | 10 | 0.000 | 10.000 | 1 → 1 | 2 → 3 | 21% → 21% | 9 → 6 | 17 | 7 → 7 | 0.000 | -0.276 |
| Jogador 2 | 3-7 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 21% → 21% | 6 → 7 | 18 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 10 | 6.000 | 0.000 | 1 → 1 | 3 → 2 | 21% → 25% | 7 → 9 | 12 | 7 → 7 | 0.001 | -0.263 |
| Jogador 2 | 4-2 | 10 | 8.000 | 6.000 | 1 → 1 | 2 → 2 | 25% → 25% | 9 → 7 | 8 | 7 → 7 | 0.008 | 0.298 |
| Jogador 2 | 4-3 | 10 | 0.000 | 8.000 | 1 → 1 | 2 → 2 | 25% → 25% | 7 → 9 | 8 | 7 → 7 | -0.008 | 0.285 |
| Jogador 2 | 4-4 | 9 | 0.000 | 8.000 | 1 → 1 | 2 → 4 | 25% → 25% | 9 → 8 | 12 | 7 → 7 | -0.033 | 0.000 |
| Jogador 2 | 4-5 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 8 → 7 | 13 | 7 → 7 | 0.002 | 0.298 |
| Jogador 2 | 4-6 | 10 | 0.000 | -6.000 | 1 → 1 | 4 → 4 | 25% → 25% | 7 → 9 | 12 | 7 → 7 | 0.000 | 0.301 |
| Jogador 2 | 4-7 | 10 | 6.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 29% | 9 → 8 | 10 | 7 → 8 | 0.004 | 0.000 |
| Jogador 2 | 5-1 | 10 | 0.000 | 8.000 | 1 → 1 | 4 → 4 | 29% → 29% | 8 → 9 | 9 | 8 → 8 | -0.001 | 0.307 |
| Jogador 2 | 5-2 | 10 | 0.000 | -6.000 | 1 → 1 | 4 → 4 | 29% → 29% | 9 → 24 | 7 | 8 → 8 | 0.030 | 0.297 |
| Jogador 2 | 5-3 | 10 | -4.000 | 4.000 | 1 → 1 | 4 → 3 | 29% → 25% | 24 → 21 | 21 | 8 → 8 | 0.006 | 0.297 |
| Jogador 2 | 5-4 | 10 | 6.000 | 4.000 | 1 → 1 | 3 → 3 | 25% → 29% | 21 → 25 | 10 | 8 → 8 | -0.001 | 0.000 |
| Jogador 2 | 5-5 | 10 | 0.000 | 4.000 | 1 → 1 | 3 → 2 | 29% → 29% | 25 → 31 | 13 | 8 → 8 | -0.046 | 0.292 |
| Jogador 2 | 5-6 | 8 | 0.000 | -4.000 | 1 → 1 | 2 → 3 | 29% → 29% | 31 → 46 | 7 | 8 → 8 | 0.038 | 0.000 |
| Jogador 2 | 5-7 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 29% → 29% | 46 → 59 | 11 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 9 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 29% | 59 → 73 | 7 | 8 → 8 | -0.066 | 0.339 |
| Jogador 2 | 6-2 | 8 | 0.000 | 2.000 | 1 → 1 | 3 → 3 | 29% → 29% | 73 → 86 | 6 | 8 → 8 | -0.006 | 0.376 |
| Jogador 2 | 6-3 | 10 | 0.000 | -6.000 | 1 → 1 | 3 → 3 | 29% → 29% | 86 → 103 | 13 | 8 → 8 | 0.000 | 0.316 |
| Jogador 2 | 6-4 | 9 | 4.000 | 10.000 | 1 → 0 | 3 → 4 | 29% → 29% | 103 → 109 | 11 | 8 → 8 | 0.086 | 0.000 |
| Jogador 2 | 6-5 | 10 | 0.000 | -6.000 | 0 → 0 | 4 → 5 | 29% → 29% | 109 → 127 | 9 | 8 → 8 | 0.006 | 0.321 |
| Jogador 2 | 6-6 | 10 | 0.000 | 6.000 | 0 → 0 | 5 → 5 | 29% → 29% | 127 → 138 | 13 | 8 → 8 | 0.000 | 0.305 |
| Jogador 2 | 6-7 | 10 | 0.000 | -4.000 | 0 → 0 | 5 → 4 | 29% → 29% | 138 → 153 | 11 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 7-1 | 10 | 2.000 | 8.000 | 0 → 0 | 4 → 5 | 29% → 29% | 153 → 148 | 14 | 8 → 8 | -0.049 | 0.302 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 56, COMPOSITION_COMPATIBILITY: 34, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 25; mudanças de composição: 0; posicionamento melhorou em 50 ações e piorou em 40.
- Jogador 2 — estado final: ouro 148, nível 8, vida 34.0, colocação 1.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.060 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 3 | 1-4 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.002 | 0.000 |
| Jogador 3 | 2-1 | 8 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.009 | 0.320 |
| Jogador 3 | 2-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.653 |
| Jogador 3 | 2-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 8 | 7 | 4 → 5 | 0.006 | 0.502 |
| Jogador 3 | 2-4 | 9 | 6.000 | 2.000 | 1 → 1 | 1 → 2 | 14% → 18% | 8 → 6 | 8 | 5 → 5 | 0.024 | 0.000 |
| Jogador 3 | 2-5 | 7 | 4.000 | -4.000 | 1 → 1 | 2 → 3 | 18% → 18% | 6 → 9 | 5 | 5 → 5 | 0.010 | 0.370 |
| Jogador 3 | 2-6 | 8 | 6.000 | -6.000 | 1 → 2 | 3 → 1 | 18% → 18% | 9 → 10 | 7 | 5 → 5 | -0.013 | 0.332 |
| Jogador 3 | 2-7 | 9 | 2.000 | 10.000 | 2 → 2 | 1 → 2 | 18% → 21% | 10 → 7 | 10 | 5 → 6 | 0.059 | 0.000 |
| Jogador 3 | 3-1 | 10 | 0.000 | 6.000 | 2 → 2 | 2 → 3 | 21% → 21% | 7 → 10 | 9 | 6 → 6 | 0.006 | 0.272 |
| Jogador 3 | 3-2 | 8 | 4.000 | -6.000 | 2 → 2 | 3 → 2 | 21% → 21% | 10 → 20 | 2 | 6 → 6 | -0.066 | 0.351 |
| Jogador 3 | 3-3 | 7 | 0.000 | 8.000 | 2 → 2 | 2 → 3 | 21% → 21% | 20 → 27 | 6 | 6 → 6 | -0.034 | 0.426 |
| Jogador 3 | 3-4 | 10 | 0.000 | 4.000 | 2 → 2 | 3 → 4 | 21% → 21% | 27 → 9 | 27 | 6 → 7 | 0.003 | 0.000 |
| Jogador 3 | 3-5 | 10 | 2.000 | 6.000 | 2 → 2 | 4 → 3 | 21% → 21% | 9 → 11 | 7 | 7 → 7 | -0.003 | 0.290 |
| Jogador 3 | 3-6 | 10 | 2.000 | -6.000 | 2 → 3 | 3 → 2 | 21% → 21% | 11 → 6 | 18 | 7 → 7 | 0.004 | -0.258 |
| Jogador 3 | 3-7 | 8 | 8.000 | -4.000 | 3 → 3 | 2 → 3 | 21% → 25% | 6 → 5 | 7 | 7 → 7 | 0.031 | 0.000 |
| Jogador 3 | 4-1 | 8 | 0.000 | 4.000 | 3 → 3 | 3 → 2 | 25% → 25% | 5 → 6 | 5 | 7 → 7 | 0.000 | 0.350 |
| Jogador 3 | 4-2 | 5 | 0.000 | 6.000 | 3 → 3 | 2 → 3 | 25% → 25% | 6 → 10 | 3 | 7 → 7 | -0.003 | 0.587 |
| Jogador 3 | 4-3 | 4 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 25% → 25% | 10 → 18 | 0 | 7 → 7 | 0.000 | 0.753 |
| Jogador 3 | 4-4 | 4 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 25% → 25% | 18 → 25 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 4 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 25% → 25% | 25 → 34 | 0 | 7 → 7 | 0.024 | 0.740 |
| Jogador 3 | 4-6 | 9 | 4.000 | -14.000 | 3 → 4 | 3 → 2 | 25% → 25% | 34 → 49 | 4 | 7 → 7 | -0.025 | 0.340 |
| Jogador 3 | 4-7 | 6 | 0.000 | 8.000 | 4 → 4 | 2 → 3 | 25% → 25% | 49 → 56 | 4 | 7 → 7 | 0.151 | 0.000 |
| Jogador 3 | 5-1 | 6 | 0.000 | 0.000 | 4 → 4 | 3 → 3 | 25% → 25% | 56 → 70 | 0 | 7 → 7 | 0.000 | 0.512 |
| Jogador 3 | 5-2 | 6 | 0.000 | -2.000 | 4 → 4 | 3 → 4 | 25% → 25% | 70 → 81 | 1 | 7 → 7 | -0.159 | -0.467 |
| Jogador 3 | 5-3 | 7 | 0.000 | 4.000 | 4 → 4 | 4 → 4 | 25% → 25% | 81 → 90 | 3 | 7 → 7 | 0.126 | -0.400 |
| Jogador 3 | 5-4 | 10 | 0.000 | 0.000 | 4 → 4 | 4 → 3 | 25% → 25% | 90 → 99 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-5 | 9 | 0.000 | 4.000 | 4 → 4 | 3 → 4 | 25% → 25% | 99 → 109 | 11 | 7 → 7 | 0.015 | -0.306 |
| Jogador 3 | 5-6 | 8 | 0.000 | 8.000 | 4 → 4 | 4 → 3 | 25% → 25% | 109 → 113 | 10 | 7 → 7 | -0.016 | -0.350 |
| Jogador 3 | 5-7 | 10 | 6.000 | -12.000 | 4 → 5 | 3 → 3 | 25% → 25% | 113 → 126 | 9 | 7 → 7 | 0.009 | 0.000 |
| Jogador 3 | 6-1 | 10 | 0.000 | 4.000 | 5 → 5 | 3 → 4 | 25% → 25% | 126 → 135 | 10 | 7 → 8 | 0.005 | 0.000 |
| Jogador 3 | 6-2 | 10 | 8.000 | -16.000 | 5 → 5 | 4 → 3 | 25% → 29% | 135 → 149 | 11 | 8 → 8 | -0.095 | 0.000 |
| Jogador 3 | 6-3 | 9 | 0.000 | 8.000 | 5 → 5 | 3 → 3 | 29% → 29% | 149 → 156 | 7 | 8 → 8 | 0.000 | 0.000 |
| Jogador 3 | 6-4 | 10 | 0.000 | 4.000 | 5 → 5 | 3 → 3 | 29% → 29% | 156 → 165 | 10 | 8 → 8 | 0.036 | 0.000 |
| Jogador 3 | 6-5 | 10 | 0.000 | -2.000 | 5 → 5 | 3 → 3 | 29% → 29% | 165 → 177 | 6 | 8 → 8 | 0.063 | 0.000 |
| Jogador 3 | 6-6 | 10 | 0.000 | 4.000 | 5 → 5 | 3 → 3 | 29% → 29% | 177 → 187 | 8 | 8 → 8 | -0.088 | -0.285 |
| Jogador 3 | 6-7 | 10 | 0.000 | -2.000 | 5 → 5 | 3 → 4 | 29% → 29% | 187 → 200 | 14 | 8 → 8 | -0.004 | 0.000 |
| Jogador 3 | 7-1 | 9 | -64.000 | -42.000 | 5 → 0 | 4 → 0 | 29% → 0% | 200 → 198 | 9 | 8 → 8 | -0.071 | -0.311 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 23, COMPOSITION_COMPATIBILITY: 28, IMMEDIATE_UPGRADE: 12, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 52 ações e piorou em 43.
- Jogador 3 — estado final: ouro 198, nível 8, vida 9.0, colocação 2.
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
| Jogador 4 | 3-1 | 8 | 0.000 | 12.000 | 0 → 0 | 2 → 3 | 21% → 21% | 7 → 7 | 6 | 6 → 6 | 0.014 | -0.317 |
| Jogador 4 | 3-2 | 10 | 6.000 | 2.000 | 0 → 0 | 3 → 2 | 21% → 21% | 7 → 8 | 5 | 6 → 6 | -0.024 | 0.272 |
| Jogador 4 | 3-3 | 7 | 0.000 | 12.000 | 0 → 0 | 2 → 4 | 21% → 21% | 8 → 7 | 6 | 6 → 6 | -0.010 | -0.362 |
| Jogador 4 | 3-4 | 10 | 0.000 | 0.000 | 0 → 0 | 4 → 5 | 21% → 21% | 7 → 11 | 6 | 6 → 6 | 0.030 | 0.000 |
| Jogador 4 | 3-5 | 9 | 0.000 | 2.000 | 0 → 0 | 5 → 4 | 21% → 21% | 11 → 16 | 7 | 6 → 6 | -0.090 | 0.302 |
| Jogador 4 | 3-6 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 6 | 21% → 21% | 16 → 26 | 6 | 6 → 6 | 0.079 | 0.281 |
| Jogador 4 | 3-7 | 10 | 0.000 | -8.000 | 0 → 0 | 6 → 4 | 21% → 21% | 26 → 37 | 7 | 6 → 6 | -0.054 | 0.000 |
| Jogador 4 | 4-1 | 8 | 0.000 | 6.000 | 0 → 0 | 4 → 6 | 21% → 21% | 37 → 42 | 3 | 6 → 6 | -0.057 | -0.356 |
| Jogador 4 | 4-2 | 10 | 0.000 | -12.000 | 0 → 0 | 6 → 5 | 21% → 21% | 42 → 57 | 7 | 6 → 6 | 0.094 | -0.276 |
| Jogador 4 | 4-3 | 10 | 0.000 | 10.000 | 0 → 0 | 5 → 6 | 21% → 21% | 57 → 61 | 15 | 6 → 7 | 0.004 | 0.285 |
| Jogador 4 | 4-4 | 8 | 4.000 | 8.000 | 0 → 0 | 6 → 5 | 21% → 25% | 61 → 65 | 7 | 7 → 7 | -0.029 | 0.000 |
| Jogador 4 | 4-5 | 10 | 0.000 | 6.000 | 0 → 0 | 5 → 5 | 25% → 25% | 65 → 72 | 10 | 7 → 7 | -0.075 | -0.280 |
| Jogador 4 | 4-6 | 10 | 2.000 | 2.000 | 0 → 0 | 5 → 5 | 25% → 25% | 72 → 79 | 12 | 7 → 7 | 0.001 | -0.286 |
| Jogador 4 | 4-7 | 10 | 0.000 | 4.000 | 0 → 0 | 5 → 6 | 25% → 25% | 79 → 86 | 11 | 7 → 7 | 0.016 | 0.000 |
| Jogador 4 | 5-1 | 10 | -32.000 | -50.000 | 0 → 0 | 6 → 0 | 25% → 0% | 86 → 86 | 11 | 7 → 7 | 0.015 | -0.290 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 26, COMPOSITION_COMPATIBILITY: 18, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 19; mudanças de composição: 0; posicionamento melhorou em 47 ações e piorou em 34.
- Jogador 4 — estado final: ouro 86, nível 7, vida 14.0, colocação 6.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.112 | 0.000 |
| Jogador 5 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.003 | 0.000 |
| Jogador 5 | 2-1 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.000 | 0.340 |
| Jogador 5 | 2-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.641 |
| Jogador 5 | 2-3 | 10 | 6.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 5 | 11 | 4 → 5 | -0.007 | -0.237 |
| Jogador 5 | 2-4 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 5 → 6 | 11 | 5 → 5 | 0.000 | 0.000 |
| Jogador 5 | 2-5 | 10 | 2.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 6 → 6 | 13 | 5 → 6 | -0.006 | 0.259 |
| Jogador 5 | 2-6 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 9 | 7 | 6 → 6 | 0.019 | -0.237 |
| Jogador 5 | 2-7 | 10 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 9 → 11 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-1 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 1 | 21% → 21% | 11 → 16 | 10 | 6 → 6 | 0.001 | 0.281 |
| Jogador 5 | 3-2 | 10 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 16 → 23 | 9 | 6 → 6 | 0.000 | -0.254 |
| Jogador 5 | 3-3 | 10 | 2.000 | 8.000 | 0 → 0 | 1 → 2 | 21% → 21% | 23 → 25 | 12 | 6 → 6 | 0.001 | -0.281 |
| Jogador 5 | 3-4 | 10 | -4.000 | 2.000 | 0 → 0 | 2 → 4 | 21% → 21% | 25 → 34 | 6 | 6 → 6 | -0.001 | 0.000 |
| Jogador 5 | 3-5 | 10 | 4.000 | 10.000 | 0 → 0 | 4 → 3 | 21% → 21% | 34 → 35 | 10 | 6 → 6 | -0.035 | -0.291 |
| Jogador 5 | 3-6 | 10 | 0.000 | -6.000 | 0 → 0 | 3 → 4 | 21% → 21% | 35 → 47 | 6 | 6 → 6 | 0.000 | 0.272 |
| Jogador 5 | 3-7 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 4 | 21% → 21% | 47 → 57 | 10 | 6 → 6 | -0.000 | 0.000 |
| Jogador 5 | 4-1 | 10 | 0.000 | 6.000 | 0 → 0 | 4 → 3 | 21% → 21% | 57 → 63 | 10 | 6 → 6 | 0.024 | -0.280 |
| Jogador 5 | 4-2 | 10 | 0.000 | 4.000 | 0 → 0 | 3 → 2 | 21% → 21% | 63 → 70 | 11 | 6 → 6 | -0.006 | -0.281 |
| Jogador 5 | 4-3 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 21% → 21% | 70 → 79 | 11 | 6 → 6 | 0.025 | -0.285 |
| Jogador 5 | 4-4 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 4 | 21% → 21% | 79 → 89 | 9 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-5 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 5 | 21% → 21% | 89 → 99 | 10 | 6 → 6 | 0.000 | -0.273 |
| Jogador 5 | 4-6 | 10 | -18.000 | -36.000 | 0 → 0 | 5 → 0 | 21% → 0% | 99 → 93 | 10 | 6 → 6 | -0.043 | -0.290 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 33, COMPOSITION_COMPATIBILITY: 29, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 16; mudanças de composição: 1; posicionamento melhorou em 30 ações e piorou em 26.
- Jogador 5 — estado final: ouro 93, nível 6, vida 8.0, colocação 7.
| Jogador 6 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.163 | 0.000 |
| Jogador 6 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.039 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.021 | -0.404 |
| Jogador 6 | 2-2 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | -0.010 | -0.430 |
| Jogador 6 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 9 | 5 | 4 → 5 | -0.005 | -0.369 |
| Jogador 6 | 2-4 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 3 | 14% → 14% | 9 → 10 | 13 | 5 → 5 | 0.006 | 0.000 |
| Jogador 6 | 2-5 | 10 | 2.000 | -12.000 | 0 → 0 | 3 → 4 | 14% → 18% | 10 → 9 | 15 | 5 → 6 | 0.052 | -0.242 |
| Jogador 6 | 2-6 | 10 | 2.000 | 0.000 | 0 → 0 | 4 → 3 | 18% → 21% | 9 → 7 | 13 | 6 → 6 | 0.010 | -0.237 |
| Jogador 6 | 2-7 | 10 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 7 → 8 | 11 | 6 → 6 | 0.009 | 0.000 |
| Jogador 6 | 3-1 | 10 | 4.000 | -4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 8 → 6 | 15 | 6 → 6 | 0.067 | 0.291 |
| Jogador 6 | 3-2 | 10 | -4.000 | 2.000 | 0 → 0 | 3 → 1 | 21% → 14% | 6 → 7 | 7 | 6 → 7 | -0.017 | -0.259 |
| Jogador 6 | 3-3 | 6 | 0.000 | 12.000 | 0 → 1 | 1 → 2 | 14% → 18% | 7 → 7 | 6 | 7 → 7 | -0.028 | -0.447 |
| Jogador 6 | 3-4 | 8 | 18.000 | -4.000 | 1 → 1 | 2 → 2 | 18% → 25% | 7 → 6 | 7 | 7 → 7 | 0.007 | 0.000 |
| Jogador 6 | 3-5 | 6 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 6 → 9 | 3 | 7 → 7 | 0.026 | 0.514 |
| Jogador 6 | 3-6 | 9 | 0.000 | 6.000 | 1 → 1 | 3 → 1 | 25% → 25% | 9 → 7 | 9 | 7 → 7 | -0.047 | 0.307 |
| Jogador 6 | 3-7 | 7 | 0.000 | 14.000 | 1 → 1 | 1 → 2 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | -0.003 | 0.000 |
| Jogador 6 | 4-1 | 9 | 0.000 | 10.000 | 1 → 1 | 2 → 2 | 25% → 25% | 6 → 8 | 5 | 7 → 7 | 0.076 | 0.343 |
| Jogador 6 | 4-2 | 9 | 0.000 | -12.000 | 1 → 1 | 2 → 2 | 25% → 25% | 8 → 24 | 6 | 7 → 7 | 0.023 | -0.297 |
| Jogador 6 | 4-3 | 10 | 0.000 | 8.000 | 1 → 1 | 2 → 3 | 25% → 25% | 24 → 28 | 10 | 7 → 7 | -0.004 | -0.268 |
| Jogador 6 | 4-4 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 28 → 36 | 7 | 7 → 7 | -0.011 | 0.000 |
| Jogador 6 | 4-5 | 8 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 36 → 45 | 3 | 7 → 7 | 0.001 | 0.367 |
| Jogador 6 | 4-6 | 10 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 25% → 25% | 45 → 51 | 14 | 7 → 7 | 0.000 | 0.288 |
| Jogador 6 | 4-7 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 25% → 25% | 51 → 59 | 14 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 10 | 2.000 | 2.000 | 1 → 1 | 4 → 4 | 25% → 21% | 59 → 67 | 7 | 7 → 7 | 0.005 | -0.290 |
| Jogador 6 | 5-2 | 10 | -2.000 | 12.000 | 1 → 1 | 4 → 2 | 21% → 21% | 67 → 67 | 14 | 7 → 7 | -0.017 | -0.278 |
| Jogador 6 | 5-3 | 10 | -30.000 | -68.000 | 1 → 0 | 2 → 0 | 21% → 0% | 67 → 78 | 10 | 7 → 7 | -0.072 | -0.273 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 28, COMPOSITION_COMPATIBILITY: 26, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 42 ações e piorou em 38.
- Jogador 6 — estado final: ouro 78, nível 7, vida 2.0, colocação 4.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.043 | 0.000 |
| Jogador 7 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.077 | 0.000 |
| Jogador 7 | 2-1 | 6 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.016 | 0.427 |
| Jogador 7 | 2-2 | 10 | -2.000 | 4.000 | 0 → 0 | 3 → 2 | 14% → 11% | 8 → 8 | 8 | 4 → 4 | 0.015 | -0.247 |
| Jogador 7 | 2-3 | 6 | 8.000 | 0.000 | 0 → 1 | 2 → 2 | 11% → 14% | 8 → 9 | 5 | 4 → 5 | 0.071 | 0.456 |
| Jogador 7 | 2-4 | 8 | 6.000 | 4.000 | 1 → 1 | 2 → 2 | 14% → 18% | 9 → 5 | 11 | 5 → 5 | 0.001 | 0.000 |
| Jogador 7 | 2-5 | 8 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 18% → 18% | 5 → 7 | 8 | 5 → 5 | 0.041 | 0.314 |
| Jogador 7 | 2-6 | 10 | 0.000 | -12.000 | 1 → 1 | 2 → 3 | 18% → 18% | 7 → 12 | 12 | 5 → 6 | 0.005 | 0.251 |
| Jogador 7 | 2-7 | 10 | 2.000 | -2.000 | 1 → 1 | 3 → 3 | 18% → 21% | 12 → 6 | 17 | 6 → 6 | 0.004 | 0.000 |
| Jogador 7 | 3-1 | 7 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 21% → 21% | 6 → 8 | 5 | 6 → 6 | -0.003 | 0.409 |
| Jogador 7 | 3-2 | 8 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 21% → 21% | 8 → 9 | 7 | 6 → 6 | -0.073 | 0.346 |
| Jogador 7 | 3-3 | 10 | 8.000 | -16.000 | 1 → 1 | 3 → 2 | 21% → 21% | 9 → 6 | 13 | 6 → 7 | 0.027 | -0.268 |
| Jogador 7 | 3-4 | 10 | 12.000 | -8.000 | 1 → 3 | 2 → 0 | 21% → 25% | 6 → 5 | 6 | 7 → 7 | 0.019 | 0.000 |
| Jogador 7 | 3-5 | 6 | 0.000 | 8.000 | 3 → 3 | 0 → 0 | 25% → 25% | 5 → 7 | 4 | 7 → 7 | 0.024 | -0.454 |
| Jogador 7 | 3-6 | 6 | 0.000 | 14.000 | 3 → 3 | 0 → 0 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | 0.047 | 0.489 |
| Jogador 7 | 3-7 | 7 | 0.000 | 12.000 | 3 → 3 | 0 → 1 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | -0.091 | 0.000 |
| Jogador 7 | 4-1 | 8 | 0.000 | 6.000 | 3 → 3 | 1 → 1 | 25% → 25% | 5 → 9 | 3 | 7 → 7 | 0.060 | 0.376 |
| Jogador 7 | 4-2 | 5 | 0.000 | 4.000 | 3 → 3 | 1 → 1 | 25% → 25% | 9 → 14 | 2 | 7 → 7 | -0.099 | 0.570 |
| Jogador 7 | 4-3 | 5 | 0.000 | 0.000 | 3 → 3 | 1 → 1 | 25% → 25% | 14 → 22 | 0 | 7 → 7 | 0.139 | 0.570 |
| Jogador 7 | 4-4 | 5 | 0.000 | 6.000 | 3 → 3 | 1 → 2 | 25% → 25% | 22 → 26 | 3 | 7 → 7 | 0.011 | 0.000 |
| Jogador 7 | 4-5 | 8 | 0.000 | 4.000 | 3 → 3 | 2 → 3 | 25% → 25% | 26 → 34 | 3 | 7 → 7 | -0.093 | 0.363 |
| Jogador 7 | 4-6 | 7 | 0.000 | -4.000 | 3 → 3 | 3 → 3 | 25% → 25% | 34 → 48 | 1 | 7 → 7 | 0.000 | 0.433 |
| Jogador 7 | 4-7 | 9 | 0.000 | -6.000 | 3 → 3 | 3 → 3 | 25% → 25% | 48 → 60 | 5 | 7 → 7 | -0.009 | 0.000 |
| Jogador 7 | 5-1 | 8 | 0.000 | 16.000 | 3 → 3 | 3 → 3 | 25% → 25% | 60 → 66 | 8 | 7 → 7 | 0.090 | 0.376 |
| Jogador 7 | 5-2 | 6 | 0.000 | -6.000 | 3 → 3 | 3 → 4 | 25% → 25% | 66 → 85 | 3 | 7 → 7 | -0.095 | 0.489 |
| Jogador 7 | 5-3 | 7 | 0.000 | -2.000 | 3 → 3 | 4 → 5 | 25% → 25% | 85 → 100 | 2 | 7 → 7 | 0.036 | 0.412 |
| Jogador 7 | 5-4 | 7 | 0.000 | -4.000 | 3 → 3 | 5 → 5 | 25% → 25% | 100 → 115 | 3 | 7 → 7 | 0.003 | 0.000 |
| Jogador 7 | 5-5 | 7 | 0.000 | 0.000 | 3 → 3 | 5 → 4 | 25% → 25% | 115 → 125 | 4 | 7 → 7 | 0.046 | 0.000 |
| Jogador 7 | 5-6 | 5 | 0.000 | 6.000 | 3 → 3 | 4 → 4 | 25% → 25% | 125 → 136 | 3 | 7 → 7 | -0.001 | 0.591 |
| Jogador 7 | 5-7 | 6 | 0.000 | -6.000 | 3 → 3 | 4 → 4 | 25% → 25% | 136 → 154 | 3 | 7 → 7 | -0.051 | 0.000 |
| Jogador 7 | 6-1 | 10 | 0.000 | 4.000 | 3 → 3 | 4 → 4 | 25% → 25% | 154 → 162 | 5 | 7 → 7 | 0.037 | -0.285 |
| Jogador 7 | 6-2 | 10 | 0.000 | 0.000 | 3 → 3 | 4 → 3 | 25% → 25% | 162 → 171 | 7 | 7 → 7 | 0.010 | -0.280 |
| Jogador 7 | 6-3 | 10 | 0.000 | -8.000 | 3 → 3 | 3 → 4 | 25% → 25% | 171 → 184 | 14 | 7 → 7 | -0.032 | -0.295 |
| Jogador 7 | 6-4 | 10 | 0.000 | -6.000 | 3 → 3 | 4 → 4 | 25% → 25% | 184 → 195 | 12 | 7 → 7 | 0.038 | 0.000 |
| Jogador 7 | 6-5 | 10 | -42.000 | -38.000 | 3 → 0 | 4 → 0 | 25% → 0% | 195 → 190 | 9 | 7 → 7 | -0.144 | -0.300 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 17, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 11, PAIR_POTENTIAL: 18; mudanças de composição: 0; posicionamento melhorou em 58 ações e piorou em 50.
- Jogador 7 — estado final: ouro 190, nível 7, vida 18.0, colocação 3.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.113 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.074 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 3 | 3 → 4 | 0.007 | 0.000 |
| Jogador 8 | 2-1 | 10 | 6.000 | 0.000 | 0 → 1 | 2 → 0 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.024 | -0.242 |
| Jogador 8 | 2-2 | 6 | 0.000 | 2.000 | 1 → 1 | 0 → 0 | 14% → 14% | 6 → 8 | 7 | 4 → 4 | 0.010 | -0.404 |
| Jogador 8 | 2-3 | 10 | -2.000 | 0.000 | 1 → 1 | 0 → 1 | 14% → 14% | 8 → 15 | 5 | 4 → 5 | -0.022 | -0.253 |
| Jogador 8 | 2-4 | 10 | 6.000 | 0.000 | 1 → 1 | 1 → 1 | 14% → 18% | 15 → 19 | 8 | 5 → 5 | 0.079 | 0.000 |
| Jogador 8 | 2-5 | 10 | 4.000 | 2.000 | 1 → 1 | 1 → 2 | 18% → 18% | 19 → 14 | 16 | 5 → 5 | 0.020 | -0.243 |
| Jogador 8 | 2-6 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 1 | 18% → 18% | 14 → 22 | 9 | 5 → 5 | 0.000 | 0.251 |
| Jogador 8 | 2-7 | 10 | 0.000 | -4.000 | 1 → 1 | 1 → 1 | 18% → 18% | 22 → 31 | 8 | 5 → 5 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 7 | -4.000 | 16.000 | 1 → 1 | 1 → 1 | 18% → 18% | 31 → 32 | 6 | 5 → 5 | -0.112 | -0.376 |
| Jogador 8 | 3-2 | 10 | 6.000 | -2.000 | 1 → 1 | 1 → 1 | 18% → 18% | 32 → 34 | 11 | 5 → 6 | 0.065 | -0.258 |
| Jogador 8 | 3-3 | 8 | 6.000 | 6.000 | 1 → 1 | 1 → 1 | 18% → 21% | 34 → 36 | 6 | 6 → 6 | 0.014 | 0.358 |
| Jogador 8 | 3-4 | 10 | 0.000 | 6.000 | 1 → 1 | 1 → 2 | 21% → 21% | 36 → 41 | 5 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-5 | 7 | -4.000 | 14.000 | 1 → 1 | 2 → 2 | 21% → 21% | 41 → 44 | 7 | 6 → 6 | -0.069 | 0.395 |
| Jogador 8 | 3-6 | 10 | 4.000 | 0.000 | 1 → 1 | 2 → 3 | 21% → 21% | 44 → 52 | 9 | 6 → 6 | 0.049 | -0.263 |
| Jogador 8 | 3-7 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 3 | 21% → 21% | 52 → 64 | 9 | 6 → 6 | 0.022 | 0.000 |
| Jogador 8 | 4-1 | 10 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 21% → 21% | 64 → 71 | 6 | 6 → 6 | -0.021 | 0.296 |
| Jogador 8 | 4-2 | 10 | 0.000 | -18.000 | 1 → 1 | 3 → 3 | 21% → 21% | 71 → 93 | 8 | 6 → 6 | 0.006 | 0.293 |
| Jogador 8 | 4-3 | 10 | 0.000 | 10.000 | 1 → 1 | 3 → 4 | 21% → 21% | 93 → 98 | 10 | 6 → 6 | -0.038 | -0.268 |
| Jogador 8 | 4-4 | 10 | 4.000 | -2.000 | 1 → 1 | 4 → 3 | 21% → 21% | 98 → 104 | 8 | 6 → 6 | -0.010 | 0.000 |
| Jogador 8 | 4-5 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 104 → 116 | 7 | 6 → 6 | 0.013 | -0.276 |
| Jogador 8 | 4-6 | 10 | 0.000 | -6.000 | 1 → 1 | 3 → 2 | 21% → 21% | 116 → 129 | 8 | 6 → 6 | 0.047 | -0.285 |
| Jogador 8 | 4-7 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 4 | 21% → 21% | 129 → 135 | 10 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 10 | -32.000 | -38.000 | 1 → 0 | 4 → 0 | 21% → 0% | 135 → 131 | 8 | 6 → 6 | -0.067 | -0.285 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 32, COMPOSITION_COMPATIBILITY: 31, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 38 ações e piorou em 33.
- Jogador 8 — estado final: ouro 131, nível 6, vida 12.0, colocação 5.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 62 | 35 | 1 | 1 | 2 | 0 | 0 | 0 | 15 | 0 | 1 | 0 |
| Jogador 2 | 125 | 89 | 6 | 7 | 10 | 1 | 0 | 0 | 28 | 9 | 2 | 0 |
| Jogador 3 | 79 | 39 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 0 |
| Jogador 4 | 73 | 39 | 0 | 0 | 0 | 2 | 1 | 0 | 6 | 6 | 2 | 0 |
| Jogador 5 | 84 | 58 | 4 | 6 | 9 | 3 | 2 | 1 | 16 | 1 | 2 | 0 |
| Jogador 6 | 71 | 44 | 0 | 0 | 0 | 1 | 1 | 0 | 10 | 3 | 1 | 0 |
| Jogador 7 | 70 | 33 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 1 | 0 | 0 |
| Jogador 8 | 83 | 55 | 7 | 8 | 12 | 0 | 1 | 0 | 10 | 0 | 2 | 0 |
- Jogador 1 — venda DA_18_Ornn (2-5, step 94): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Camille (4-4, step 224): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 2 — venda DA_18_KhaZix (3-1, step 127): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Caitlyn (3-2, step 136): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Warwick (3-4, step 156): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Sejuani (3-5, step 170): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rakan (4-3, step 214): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Cassiopeia (4-5, step 234): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_KhaZix (5-4, step 294): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rengar (5-5, step 304): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_18_Rengar (6-3, step 354): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Veigar (6-5, step 372): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_KhaZix (6-5, step 378): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Cassiopeia (6-7, step 394): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_RekSai (3-3, step 143): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Rakan (2-7, step 116): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Akali_AD (3-7, step 182): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_MasterYi_AD (3-7, step 187): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Warwick (4-2, step 207): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Leona (4-4, step 222): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_Tristana (3-2, step 136): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (3-5, step 164): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_Kobuko (3-7, step 183): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Yunara (4-2, step 209): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_Kobuko (4-4, step 230): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_Karma18 (4-6, step 243): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Veigar (4-6, step 248): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-6, step 107): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 6 — venda DA_18_Sentry (3-2, step 136): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Xayah (5-1, step 268): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Zyra (5-3, step 286): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Camille (2-6, step 104): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Hecarim (5-2, step 272): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Shen (6-1, step 336): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Tristana (6-2, step 344): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_KogMaw18_AD (6-4, step 366): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_Murkwolf18 (6-5, step 374): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_Karma18 (2-6, step 109): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Veigar (4-2, step 202): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_MasterYi_AD (4-2, step 210): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rakan (4-5, step 235): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **4**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| LOW | Jogador 1 | 2-3 | 75 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 1 | 2-5 | 94 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 3-2 | 134 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Elise) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 1 | 4-3 | 219 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 1 | 2-2 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 527 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-3 | 634 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 733 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-6 | 988 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 989 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1076 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1209 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1210 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1346 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-2 | 1347 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1486 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-3 | 1487 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1625 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-4 | 1626 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1762 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-6 | 1904 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-7 | 2040 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-1 | 2175 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 2301 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-3 | 2437 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-4 | 2573 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-4 | 2574 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 2715 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-5 | 2716 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-6 | 2852 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 4-6 | 2853 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 3-5 | 1881 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-1 | 2278 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-5 | 95 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-5 | 97 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Leona) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-6 | 110 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-7 | 115 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_RekSai) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-1 | 126 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-1 | 127 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-2 | 136 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-2 | 140 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-3 | 147 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Cassiopeia) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-4 | 155 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-4 | 156 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-4 | 156 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Warwick) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-5 | 167 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-5 | 170 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-6 | 177 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 2 | 3-7 | 187 | PURCHASE_SALE_REVIEW | Compra de DA_18_Lillia foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 2 | 4-3 | 214 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-5 | 234 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-4 | 294 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-3 | 354 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 6-5 | 372 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-5 | 378 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-7 | 394 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-1 | 265 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-1 | 266 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-1 | 267 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-1 | 268 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-1 | 269 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-1 | 270 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-1 | 271 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 305 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 306 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 307 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 308 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 309 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 310 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 311 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 7-1 | 402 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 7-1 | 403 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 7-1 | 404 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-2 | 2448 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2592 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 2714 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-4 | 2715 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2854 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-5 | 2855 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 2993 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-6 | 2994 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 3128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-7 | 3129 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 3269 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-1 | 3270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 3407 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-2 | 3408 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-3 | 3543 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-3 | 3544 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-4 | 3687 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-4 | 3688 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-5 | 3832 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-5 | 3833 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-6 | 3946 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-6 | 3947 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-7 | 4084 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-1 | 4210 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-2 | 4325 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-2 | 4326 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-3 | 4464 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 6-3 | 4465 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-4 | 4592 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-5 | 4734 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-6 | 4874 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-7 | 5011 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 7-1 | 5151 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| MEDIUM | Jogador 2 | 5-1 | 3384 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-4 | 3809 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-5 | 3923 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-6 | 4061 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 4187 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 6-1 | 4302 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 6-3 | 4569 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 3 | 3-3 | 143 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-1 | 450 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-2 | 512 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-3 | 582 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-4 | 700 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-5 | 794 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-6 | 900 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 1019 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1151 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1259 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-3 | 1355 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-3 | 1356 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1483 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-4 | 1484 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1617 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-5 | 1618 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 1751 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-6 | 1752 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 1859 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 1970 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 2042 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-3 | 2102 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-4 | 2166 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-5 | 2230 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-6 | 2355 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-6 | 2356 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-7 | 2442 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-1 | 2532 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-2 | 2620 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-2 | 2621 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-3 | 2725 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-4 | 2867 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-5 | 2993 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-6 | 3104 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-7 | 3246 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-2 | 3521 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 6-2 | 3522 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-3 | 3650 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 6-3 | 3651 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-4 | 3788 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-5 | 3927 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-6 | 4069 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 6-6 | 4070 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-7 | 4209 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 6-7 | 4210 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 7-1 | 4338 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 7-1 | 4339 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 3-1 | 1236 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-2 | 1332 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 6-1 | 3498 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 6-2 | 3627 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 6-3 | 3765 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 4 | 2-6 | 104 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 4 | 2-7 | 116 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 3-7 | 187 | SOLD_CORE_UNIT | Venda de 'DA_18_MasterYi_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 4-2 | 206 | PURCHASE_SALE_REVIEW | Compra de DA_18_MasterYi_AD foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 4-2 | 207 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 5-1 | 265 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 5-1 | 266 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 5-1 | 267 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 5-1 | 268 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 5-1 | 269 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 2-5 | 849 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-6 | 981 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-3 | 1456 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-3 | 1457 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-4 | 1598 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-4 | 1599 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-5 | 1718 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-5 | 1719 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-6 | 1854 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-6 | 1855 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 1990 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-7 | 1991 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-1 | 2102 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-1 | 2103 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 2239 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-2 | 2240 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-3 | 2376 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-3 | 2377 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-4 | 2489 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-4 | 2490 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 2626 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-5 | 2627 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-6 | 2768 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-6 | 2769 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-7 | 2906 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-7 | 2907 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-1 | 3046 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-1 | 3047 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 3-5 | 1831 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-7 | 2079 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-3 | 2466 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-4 | 87 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 107 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Elise) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-7 | 118 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rakan) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-7 | 119 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Scuttlecrab18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-1 | 129 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-2 | 136 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-2 | 138 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-2 | 140 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 3-4 | 156 | PURCHASE_SALE_REVIEW | Compra de DA_18_Warwick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 5 | 3-4 | 160 | PURCHASE_SALE_REVIEW | Compra de DA_18_Alistar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 3-7 | 183 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-1 | 199 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_RekSai) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 4-4 | 230 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 4-6 | 248 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
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
| LOW | Jogador 5 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-3 | 558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 690 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 823 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 957 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-7 | 1092 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-1 | 1227 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1360 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-3 | 1494 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-4 | 1626 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1763 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1899 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-7 | 2034 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-1 | 2173 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 2311 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-6 | 2863 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 4-6 | 2864 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 3-2 | 1471 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 2-3 | 76 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 6 | 3-2 | 136 | SOLD_CORE_UNIT | Venda de 'DA_18_Sentry' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 5-1 | 268 | SOLD_CORE_UNIT | Venda de 'DA_18_Xayah' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 5-3 | 286 | SOLD_CORE_UNIT | Venda de 'DA_18_Zyra' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
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
| LOW | Jogador 6 | 3-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 2-7 | 1071 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1202 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1342 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1426 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1533 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1534 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-5 | 1618 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1619 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-6 | 1741 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-6 | 1742 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-7 | 1838 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1839 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-1 | 1965 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 1966 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 2089 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 2225 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 2362 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-5 | 2476 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 2613 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-7 | 2751 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 2895 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 3033 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-3 | 3172 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-3 | 3173 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 4-1 | 2066 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-4 | 2453 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-6 | 104 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 5-2 | 272 | SOLD_CORE_UNIT | Venda de 'DA_18_Hecarim' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 6-1 | 336 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Shen' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 6-4 | 366 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 2-4 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 7 | 3-1 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 7 | 3-5 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 238 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 253 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 254 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 255 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 256 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 257 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 258 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 259 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 261 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 262 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 263 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 264 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 265 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 266 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 267 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 268 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 271 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 429 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 567 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-3 | 655 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-7 | 1150 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1251 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1361 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1492 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1627 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1713 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1797 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 1898 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-7 | 1899 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 2011 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-1 | 2012 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2089 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-2 | 2090 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2167 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2246 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2362 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-5 | 2363 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2460 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-6 | 2461 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2584 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-2 | 2791 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-5 | 3990 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 6-5 | 3991 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-4 | 43 | PURCHASE_SALE_REVIEW | Compra de DA_18_RekSai foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-4 | 87 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kobuko) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-4 | 88 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_KhaZix) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-4 | 90 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sentry) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 8 | 2-5 | 95 | PURCHASE_SALE_REVIEW | Compra de DA_18_Warwick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-6 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_RekSai) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-6 | 107 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Diana) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-6 | 109 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Karma18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 2-7 | 116 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-7 | 117 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Vi18) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-7 | 120 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Ornn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-2 | 137 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-2 | 138 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-4 | 154 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kobuko) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 8 | 4-2 | 202 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-2 | 209 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Sivir) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 4-2 | 210 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-5 | 235 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
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
| LOW | Jogador 8 | 2-6 | 1082 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-6 | 1083 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 2-7 | 1215 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1216 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-1 | 1312 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1313 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-2 | 1447 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-2 | 1448 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-3 | 1556 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1557 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-4 | 1690 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-4 | 1691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-5 | 1787 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-5 | 1788 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-6 | 1922 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-6 | 1923 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-7 | 2058 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 2059 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 2195 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 2196 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2333 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-2 | 2334 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2467 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 2468 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 2608 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-4 | 2609 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 2752 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-5 | 2753 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-6 | 2890 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-6 | 2891 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-7 | 3028 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-7 | 3029 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-1 | 3171 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 5-1 | 3172 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 2-7 | 1289 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-2 | 1533 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-3 | 1667 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-4 | 1764 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
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
